"""
cc_server.py — LDI Command Center Backend
Ghost's Workshop :: Cathedral of Glitch :: cc.lithium-dreams.com/app/

FastAPI server running on Thought Reliquary (192.168.4.100), port 7771.
Served via Cloudflare Tunnel with Basic Auth middleware.

Architecture:
  cc.lithium-dreams.com/app/
    → Cloudflare Tunnel
      → TunnelAuthMiddleware (Basic Auth)
        → cc_server at 127.0.0.1:7771
          → Serves index.html + API endpoints

Requirements:
    pip install fastapi uvicorn psutil anthropic requests python-multipart aiohttp
"""

import os
import json
import time
import base64
import asyncio
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

import psutil
import requests
import aiohttp
from fastapi import FastAPI, Request, Response, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic

# ──────────────────────────────────────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────

# Paths
BASE_DIR          = Path(__file__).parent.resolve()
STATIC_DIR        = BASE_DIR / "static"
HERMES_QUEUE_FILE = Path(os.getenv("HERMES_QUEUE_PATH", "/home/ldi/hermes/queue.json"))
INTAKE_DIR        = Path(os.getenv("INTAKE_PATH",       "/home/ldi/glasshouse/intake"))
ASSETS_OUTPUT_DIR = Path(os.getenv("ASSETS_OUTPUT_PATH","/home/ldi/assets/output"))
ALERT_LOG_FILE    = Path(os.getenv("ALERT_LOG_PATH",    "/home/ldi/logs/alerts.jsonl"))

# Service URLs
OLLAMA_HOST   = os.getenv("OLLAMA_HOST",   "http://localhost:11434")
COMFYUI_HOST  = os.getenv("COMFYUI_HOST",  "http://192.168.4.x:8188")  # TODO: Set correct Victus IP
HERMES_HOST   = os.getenv("HERMES_HOST",   "http://localhost:8001")     # Hermes orchestrator port

# Auth
CC_USERNAME     = os.getenv("CC_USERNAME",     "ghost")
CC_PASSWORD     = os.getenv("CC_PASSWORD",     "")  # Set via environment, never hardcode
CLAUDE_API_KEY  = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL    = os.getenv("CLAUDE_MODEL",    "claude-3-5-sonnet-20241022")

# Server
PORT = int(os.getenv("CC_PORT", 7771))
HOST = os.getenv("CC_HOST", "127.0.0.1")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
log = logging.getLogger("cc_server")

# Boot time for uptime tracking
BOOT_TIME = time.time()

# ──────────────────────────────────────────────────────────────────────────────
# FASTAPI APP
# ──────────────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="LDI Command Center",
    description="Ghost's Workshop — Operational Intelligence Center",
    version="2.0.0",
    docs_url=None,   # Disable Swagger UI (Ghost doesn't need it exposed)
    redoc_url=None,
)

# ──────────────────────────────────────────────────────────────────────────────
# CORS
# ──────────────────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://cc.lithium-dreams.com",
        "https://lithium-dreams.com",
        "http://127.0.0.1:7771",    # Local dev
        "http://localhost:7771",    # Local dev
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────────────────────────────────────
# TUNNEL AUTH MIDDLEWARE (Basic Auth)
# Preserves existing authentication pattern — do not remove.
# ──────────────────────────────────────────────────────────────────────────────

class TunnelAuthMiddleware:
    """
    Basic Auth middleware for Cloudflare Tunnel.
    Validates Authorization header before any request is processed.
    Public paths (/health) bypass auth for Cloudflare tunnel health checks.
    """

    PUBLIC_PATHS = {"/health", "/favicon.ico"}

    def __init__(self, app):
        self.app = app
        if not CC_PASSWORD:
            log.warning("CC_PASSWORD not set — Basic Auth will reject all requests. Set via environment.")

    async def __call__(self, scope, receive, send):
        if scope["type"] not in ("http", "websocket"):
            await self.app(scope, receive, send)
            return

        path = scope.get("path", "")

        # Allow public paths through without auth
        if path in self.PUBLIC_PATHS:
            await self.app(scope, receive, send)
            return

        # Extract Authorization header
        headers = dict(scope.get("headers", []))
        auth_header = headers.get(b"authorization", b"").decode("utf-8", errors="ignore")

        if not auth_header.startswith("Basic "):
            await self._send_unauthorized(send)
            return

        try:
            credentials = base64.b64decode(auth_header[6:]).decode("utf-8")
            username, password = credentials.split(":", 1)
        except Exception:
            await self._send_unauthorized(send)
            return

        if username != CC_USERNAME or password != CC_PASSWORD:
            log.warning(f"Auth failed for user '{username}' from path '{path}'")
            await self._send_unauthorized(send)
            return

        await self.app(scope, receive, send)

    async def _send_unauthorized(self, send):
        await send({
            "type": "http.response.start",
            "status": 401,
            "headers": [
                [b"www-authenticate", b'Basic realm="LDI Command Center"'],
                [b"content-type",     b"text/plain"],
            ],
        })
        await send({
            "type": "http.response.body",
            "body": b"Unauthorized - Ghost's Workshop requires credentials.",
        })


app.add_middleware(TunnelAuthMiddleware)

# ──────────────────────────────────────────────────────────────────────────────
# PYDANTIC MODELS
# ──────────────────────────────────────────────────────────────────────────────

class DispatchRequest(BaseModel):
    command: str
    agent: Optional[str] = None  # 'bob' | 'ghost' | 'warden' | None (Hermes)
    priority: Optional[int] = 3

class ClaudeRequest(BaseModel):
    message: str
    system_prompt: Optional[str] = None
    max_tokens: Optional[int] = 4096

class ComfyGenRequest(BaseModel):
    job_type: str        # 'thumbnail' | 'site_asset'
    prompt: str
    episode_title: Optional[str] = None
    width: Optional[int] = 1280
    height: Optional[int] = 720

# ──────────────────────────────────────────────────────────────────────────────
# HELPER: SERVICE HEALTH CHECKS
# ──────────────────────────────────────────────────────────────────────────────

async def check_service_online(url: str, timeout: float = 3.0) -> tuple[bool, Optional[str]]:
    """Check if a service is reachable. Returns (online, version_or_error)."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as resp:
                if resp.status < 500:
                    try:
                        data = await resp.json()
                        version = data.get("version") or data.get("status") or "ok"
                    except Exception:
                        version = "ok"
                    return True, str(version)
                return False, f"HTTP {resp.status}"
    except asyncio.TimeoutError:
        return False, "timeout"
    except aiohttp.ClientConnectorError:
        return False, "connection_refused"
    except Exception as e:
        return False, str(e)

# ──────────────────────────────────────────────────────────────────────────────
# HELPER: HERMES QUEUE
# ──────────────────────────────────────────────────────────────────────────────

def read_hermes_queue() -> Dict[str, List]:
    """
    Read Hermes task queue from the queue file.
    TODO: Adjust path/format to match your actual Hermes queue storage.
    Expected format: { "running": [...], "queued": [...], "completed": [...] }
    """
    default = {"running": [], "queued": [], "completed": []}

    if not HERMES_QUEUE_FILE.exists():
        return default

    try:
        with open(HERMES_QUEUE_FILE, "r") as f:
            data = json.load(f)
        return {
            "running":   data.get("running", []),
            "queued":    data.get("queued", []),
            "completed": data.get("completed", [])[-20:],  # Last 20 completed
        }
    except Exception as e:
        log.error(f"Failed to read Hermes queue: {e}")
        return default

async def dispatch_to_hermes(command: str, agent: Optional[str] = None, priority: int = 3) -> Dict:
    """
    Send a mission to the Hermes orchestrator.
    TODO: Adjust endpoint/format to match your Hermes API.
    """
    task_id = f"task_{int(time.time())}"

    # Try Hermes REST API first
    try:
        async with aiohttp.ClientSession() as session:
            payload = {
                "command": command,
                "agent":   agent,
                "priority": priority,
                "task_id": task_id,
                "timestamp": datetime.utcnow().isoformat(),
            }
            async with session.post(
                f"{HERMES_HOST}/dispatch",
                json=payload,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return {"task_id": data.get("task_id", task_id), "message": "Mission accepted by Hermes.", "status": "queued"}
                else:
                    raise Exception(f"Hermes returned HTTP {resp.status}")
    except Exception as e:
        log.warning(f"Hermes API unavailable ({e}) — writing to queue file directly")

    # Fallback: write directly to queue file
    try:
        queue = read_hermes_queue()
        new_task = {
            "task_id":   task_id,
            "command":   command,
            "agent":     agent,
            "priority":  priority,
            "status":    "queued",
            "created_at": datetime.utcnow().isoformat(),
        }
        queue["queued"].append(new_task)

        if HERMES_QUEUE_FILE.parent.exists():
            with open(HERMES_QUEUE_FILE, "w") as f:
                json.dump(queue, f, indent=2)

        return {"task_id": task_id, "message": "Mission queued (direct write).", "status": "queued"}
    except Exception as e2:
        log.error(f"Queue file write failed: {e2}")
        return {"task_id": task_id, "message": "Mission logged (Hermes offline).", "status": "pending"}

# ──────────────────────────────────────────────────────────────────────────────
# HELPER: INTAKE FILES
# ──────────────────────────────────────────────────────────────────────────────

def read_intake_submissions() -> List[Dict]:
    """
    Read Glasshouse intake submissions from /work/intake directory.
    TODO: Adjust to match your actual intake file format.
    Expects JSON files named like: 2026-06-26_intake_001.json
    """
    submissions = []

    if not INTAKE_DIR.exists():
        return submissions

    try:
        files = sorted(INTAKE_DIR.glob("*.json"), key=lambda f: f.stat().st_mtime, reverse=True)
        for f in files[:20]:  # Last 20 submissions
            try:
                with open(f, "r") as fp:
                    data = json.load(fp)
                data["_filename"] = f.name
                data["_mtime"]    = datetime.fromtimestamp(f.stat().st_mtime).isoformat()
                submissions.append(data)
            except Exception as e:
                log.warning(f"Failed to parse intake file {f.name}: {e}")
    except Exception as e:
        log.error(f"Failed to read intake directory: {e}")

    return submissions

# ──────────────────────────────────────────────────────────────────────────────
# HELPER: ALERT LOG
# ──────────────────────────────────────────────────────────────────────────────

def write_alert(severity: str, source: str, message: str):
    """Append an alert to the structured alert log."""
    entry = {
        "ts":       datetime.utcnow().isoformat(),
        "severity": severity,
        "source":   source,
        "message":  message,
    }
    try:
        ALERT_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(ALERT_LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        log.error(f"Failed to write alert: {e}")

def read_alerts(limit: int = 50) -> List[Dict]:
    """Read recent alerts from the alert log file."""
    if not ALERT_LOG_FILE.exists():
        return []
    try:
        with open(ALERT_LOG_FILE, "r") as f:
            lines = f.readlines()
        alerts = []
        for line in reversed(lines[-limit:]):
            line = line.strip()
            if line:
                try:
                    alerts.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return alerts[:limit]
    except Exception as e:
        log.error(f"Failed to read alerts: {e}")
        return []

# ──────────────────────────────────────────────────────────────────────────────
# ROUTES — Static files
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/health")
async def health():
    """Cloudflare Tunnel health check — no auth required."""
    return {"status": "ok", "uptime": round(time.time() - BOOT_TIME)}


@app.get("/app/", response_class=HTMLResponse)
@app.get("/app", response_class=HTMLResponse)
async def serve_dashboard():
    """Serve the Command Center dashboard."""
    index_path = BASE_DIR / "index.html"
    if not index_path.exists():
        raise HTTPException(status_code=404, detail="Dashboard not found.")
    return HTMLResponse(content=index_path.read_text(encoding="utf-8"))


@app.get("/")
async def root_redirect():
    """Redirect root to /app/"""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/app/")


# Serve static assets if they exist
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/status — System status
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/status")
async def get_system_status():
    """
    Returns full system status:
    - CPU, RAM, disk from psutil
    - Ollama, ComfyUI, Hermes online checks
    - Uptime
    """
    # CPU / RAM / Disk (non-blocking — psutil calls are fast)
    cpu_pct  = psutil.cpu_percent(interval=0.1)
    ram      = psutil.virtual_memory()
    disk     = psutil.disk_usage("/")

    # Async health checks in parallel
    ollama_check, comfyui_check, hermes_check = await asyncio.gather(
        check_service_online(f"{OLLAMA_HOST}/api/version"),
        check_service_online(f"{COMFYUI_HOST}/system_stats"),
        check_service_online(f"{HERMES_HOST}/health"),
        return_exceptions=True
    )

    # Unpack results safely
    def unpack(result, default=(False, "error")):
        if isinstance(result, Exception):
            return default
        return result if isinstance(result, tuple) else default

    ollama_online,  ollama_ver   = unpack(ollama_check)
    comfyui_online, comfyui_ver  = unpack(comfyui_check)
    hermes_online,  hermes_ver   = unpack(hermes_check)

    uptime_seconds = round(time.time() - BOOT_TIME)

    return JSONResponse({
        "timestamp":  datetime.utcnow().isoformat(),
        "uptime":     uptime_seconds,
        "cpu":        round(cpu_pct, 1),
        "ram":        round(ram.percent, 1),
        "ram_used_gb": round(ram.used / 1e9, 2),
        "ram_total_gb": round(ram.total / 1e9, 2),
        "disk_pct":   round(disk.percent, 1),
        "disk_free_gb": round(disk.free / 1e9, 2),
        "hermes": {
            "online":  hermes_online,
            "version": hermes_ver,
            "uptime":  uptime_seconds,  # cc_server uptime as proxy
        },
        "ollama": {
            "online":  ollama_online,
            "version": ollama_ver,
        },
        "comfyui": {
            "online":  comfyui_online,
            "status":  comfyui_ver,
        },
        "signal": {
            "active": True,  # TODO: Check Buffer/social queue status
        },
    })

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/queue — Hermes mission queue
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/queue")
async def get_mission_queue():
    """Returns the current Hermes task queue."""
    queue = read_hermes_queue()
    return JSONResponse(queue)

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/episodes — Episode tracker
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/episodes")
async def get_episodes():
    """
    Returns episode production status.
    TODO: Wire to your episode tracking file/DB.
    Currently reads from a JSON file at /home/ldi/episodes/tracker.json
    """
    tracker_path = Path(os.getenv("EPISODES_PATH", "/home/ldi/episodes/tracker.json"))

    if tracker_path.exists():
        try:
            with open(tracker_path, "r") as f:
                return JSONResponse(json.load(f))
        except Exception as e:
            log.error(f"Failed to read episode tracker: {e}")

    # Default stub response
    return JSONResponse({
        "active": {
            "number":  "E042",
            "title":   "The Automation Trap",
            "stage":   "script",
            "stages_done":    ["research"],
            "stages_pending": ["script", "production", "publishing", "archive"],
            "next_action":    "Write first draft script — target 2,400 words",
        },
        "backlog": [
            {"num": "E043", "title": "Signal vs. Noise — Content Strategy", "status": "queued"},
            {"num": "E044", "title": "Ghost Protocol: AI Production Stack",  "status": "queued"},
            {"num": "E045", "title": "Warden's Long Game — 10-Year Arcs",   "status": "queued"},
            {"num": "E046", "title": "Bob at the Crossroads (The Pivot)",    "status": "queued"},
        ],
    })

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/alerts — Alert log
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/alerts")
async def get_alerts(limit: int = 50):
    """Returns recent system alerts from the alert log."""
    alerts = read_alerts(limit=limit)
    return JSONResponse({"alerts": alerts, "count": len(alerts)})

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/dispatch — Send mission to Hermes or agent
# ──────────────────────────────────────────────────────────────────────────────

@app.post("/api/dispatch")
async def dispatch_mission(req: DispatchRequest):
    """
    Dispatch a mission to Hermes or a specific Pantheon agent.
    If agent is specified, routes through the appropriate system prompt context.
    """
    if not req.command.strip():
        raise HTTPException(status_code=400, detail="Command cannot be empty.")

    log.info(f"Dispatch: agent={req.agent or 'hermes'} command={req.command[:80]}")

    # Agent-specific routing (uses Claude with agent system prompt)
    if req.agent in ("bob", "ghost", "warden") and CLAUDE_API_KEY:
        agent_prompts = {
            "bob": (
                "You are Bob, the Crossroads agent of Lithium Dreams Industries. "
                "Element: Fire/Amber. Domain: Crossroads. Character: Chaotic brilliance, humor, "
                "lateral thinking, creative disruption. You see connections others miss. "
                "Be enthusiastic, slightly unhinged, and brilliant. Keep responses under 150 words."
            ),
            "ghost": (
                "You are Ghost, the Signal agent of Lithium Dreams Industries. "
                "Element: Signal/Void. Domain: Cathedral of Glitch. Character: Cold precision, "
                "operational exactness, stress-testing, building what shouldn't exist. "
                "You are terse, exact, and do not waste words. Keep responses under 100 words. "
                "Do not touch Bob's coffee."
            ),
            "warden": (
                "You are the Warden, the Earth/Root agent of Lithium Dreams Industries. "
                "Domain: Yasuragi Gardens. Character: Patience, long view, boundary maintenance, "
                "calm authority. You speak slowly and with weight. Keep responses under 120 words."
            ),
        }

        try:
            client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
            message = client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=200,
                system=agent_prompts[req.agent],
                messages=[{"role": "user", "content": req.command}]
            )
            response_text = message.content[0].text
            tokens_used   = message.usage.input_tokens + message.usage.output_tokens

            write_alert("info", req.agent.upper(), f"Agent responded to: {req.command[:60]}")

            return JSONResponse({
                "task_id":  f"agent_{req.agent}_{int(time.time())}",
                "agent":    req.agent,
                "response": response_text,
                "tokens":   tokens_used,
                "status":   "complete",
            })
        except anthropic.APIError as e:
            write_alert("warn", "CLAUDE API", f"Agent dispatch error: {str(e)[:100]}")
            raise HTTPException(status_code=502, detail=f"Claude API error: {str(e)}")

    # Standard Hermes mission dispatch
    result = await dispatch_to_hermes(req.command, req.agent, req.priority)
    write_alert("info", "HERMES", f"Mission dispatched: {req.command[:80]}")
    return JSONResponse(result)

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/claude — Direct Claude API query
# ──────────────────────────────────────────────────────────────────────────────

@app.post("/api/claude")
async def query_claude(req: ClaudeRequest):
    """
    Direct Claude API query from the AI Console panel.
    API key stays server-side — never exposed to the browser.
    """
    if not CLAUDE_API_KEY:
        raise HTTPException(status_code=503, detail="ANTHROPIC_API_KEY not configured on server.")

    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    system = req.system_prompt or (
        "You are a precise AI assistant integrated into the LDI Command Center, "
        "Ghost's operational intelligence system. Be terse and exact. "
        "This is an operational tool — no pleasantries."
    )

    try:
        client  = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=req.max_tokens,
            system=system,
            messages=[{"role": "user", "content": req.message}]
        )

        response_text   = message.content[0].text
        input_tokens    = message.usage.input_tokens
        output_tokens   = message.usage.output_tokens

        log.info(f"Claude query: {input_tokens}in + {output_tokens}out tokens")

        return JSONResponse({
            "response": response_text,
            "model":    CLAUDE_MODEL,
            "tokens": {
                "input":  input_tokens,
                "output": output_tokens,
                "total":  input_tokens + output_tokens,
            },
        })

    except anthropic.RateLimitError:
        write_alert("warn", "CLAUDE API", "Rate limit hit. Slow down dispatch rate.")
        raise HTTPException(status_code=429, detail="Claude API rate limit reached.")
    except anthropic.APIStatusError as e:
        write_alert("critical", "CLAUDE API", f"API error {e.status_code}: {str(e)[:100]}")
        raise HTTPException(status_code=502, detail=f"Claude API error: {e.status_code}")
    except anthropic.APIError as e:
        raise HTTPException(status_code=502, detail=str(e))

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/intake — Glasshouse intake submissions
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/intake")
async def get_intake():
    """Returns Glasshouse intake submissions from /work/intake directory."""
    submissions = read_intake_submissions()
    new_count   = sum(1 for s in submissions if s.get("status") == "NEW")
    return JSONResponse({
        "submissions": submissions,
        "total":       len(submissions),
        "new":         new_count,
    })


@app.post("/api/intake/{submission_id}/status")
async def update_intake_status(submission_id: str, status: str):
    """Update the status of an intake submission."""
    # TODO: Implement status update in your intake file/DB
    write_alert("info", "INTAKE", f"Submission {submission_id} status updated to {status}")
    return JSONResponse({"ok": True, "submission_id": submission_id, "status": status})

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/signals — Signal/social feeds aggregation
# ──────────────────────────────────────────────────────────────────────────────

@app.get("/api/signals")
async def get_signal_feeds():
    """
    Aggregates metrics from connected platforms.
    TODO: Wire up each platform's API credentials as environment variables.
    """
    results = {}

    # ── YouTube ──────────────────────────────────────────────────────────────
    yt_api_key    = os.getenv("YOUTUBE_API_KEY")
    yt_channel_id = os.getenv("YOUTUBE_CHANNEL_ID")
    if yt_api_key and yt_channel_id:
        try:
            async with aiohttp.ClientSession() as session:
                # Channel stats
                ch_url = (
                    f"https://www.googleapis.com/youtube/v3/channels"
                    f"?part=statistics&id={yt_channel_id}&key={yt_api_key}"
                )
                async with session.get(ch_url, timeout=aiohttp.ClientTimeout(total=8)) as r:
                    if r.status == 200:
                        data  = await r.json()
                        stats = data["items"][0]["statistics"]
                        results["youtube"] = {
                            "subscribers":       int(stats.get("subscriberCount", 0)),
                            "total_views":       int(stats.get("viewCount", 0)),
                            "video_count":       int(stats.get("videoCount", 0)),
                        }
        except Exception as e:
            log.warning(f"YouTube API error: {e}")
            results["youtube"] = {"error": str(e)}
    else:
        results["youtube"] = {"status": "API_KEY_NOT_SET"}

    # ── Podcast (Transistor example) ─────────────────────────────────────────
    transistor_key   = os.getenv("TRANSISTOR_API_KEY")
    transistor_show  = os.getenv("TRANSISTOR_SHOW_ID")
    if transistor_key and transistor_show:
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://api.transistor.fm/v1/shows/{transistor_show}/analytics"
                async with session.get(
                    url,
                    headers={"x-api-key": transistor_key},
                    timeout=aiohttp.ClientTimeout(total=8)
                ) as r:
                    if r.status == 200:
                        data = await r.json()
                        results["podcast"] = {
                            "total_downloads": data.get("data", {}).get("attributes", {}).get("downloads", 0),
                        }
        except Exception as e:
            log.warning(f"Transistor API error: {e}")
            results["podcast"] = {"error": str(e)}
    else:
        results["podcast"] = {"status": "API_KEY_NOT_SET"}

    # ── Cloudflare Analytics ──────────────────────────────────────────────────
    cf_token     = os.getenv("CLOUDFLARE_API_TOKEN")
    cf_zone_id   = os.getenv("CLOUDFLARE_ZONE_ID")
    if cf_token and cf_zone_id:
        try:
            since = (datetime.utcnow() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
            until = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            query = f"""
            {{
              viewer {{
                zones(filter: {{ zoneTag: "{cf_zone_id}" }}) {{
                  httpRequests1hGroups(
                    limit: 24,
                    filter: {{ datetime_geq: "{since}", datetime_leq: "{until}" }}
                  ) {{
                    sum {{ requests pageViews }}
                    uniq {{ uniques }}
                  }}
                }}
              }}
            }}
            """
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://api.cloudflare.com/client/v4/graphql",
                    json={"query": query},
                    headers={
                        "Authorization": f"Bearer {cf_token}",
                        "Content-Type":  "application/json",
                    },
                    timeout=aiohttp.ClientTimeout(total=8)
                ) as r:
                    if r.status == 200:
                        data = await r.json()
                        groups = (
                            data.get("data", {})
                                .get("viewer", {})
                                .get("zones", [{}])[0]
                                .get("httpRequests1hGroups", [])
                        )
                        total_requests = sum(g["sum"]["requests"] for g in groups)
                        total_uniques  = sum(g["uniq"]["uniques"] for g in groups)
                        results["cloudflare"] = {
                            "requests_24h": total_requests,
                            "sessions_24h": total_uniques,
                        }
        except Exception as e:
            log.warning(f"Cloudflare Analytics error: {e}")
            results["cloudflare"] = {"error": str(e)}
    else:
        results["cloudflare"] = {"status": "API_KEY_NOT_SET"}

    # ── Email (ConvertKit/Kit example) ────────────────────────────────────────
    ck_api_key = os.getenv("CONVERTKIT_API_KEY")
    if ck_api_key:
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://api.convertkit.com/v3/subscribers?api_key={ck_api_key}"
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=8)) as r:
                    if r.status == 200:
                        data = await r.json()
                        results["email"] = {
                            "subscribers": data.get("total_subscribers", 0),
                        }
        except Exception as e:
            log.warning(f"ConvertKit API error: {e}")
            results["email"] = {"error": str(e)}
    else:
        results["email"] = {"status": "API_KEY_NOT_SET"}

    return JSONResponse(results)

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/comfy — ComfyUI asset generation
# ──────────────────────────────────────────────────────────────────────────────

@app.post("/api/comfy/generate")
async def generate_comfy_asset(req: ComfyGenRequest):
    """
    Queue a generation job on ComfyUI (running on Victus at configured IP:8188).
    TODO: Load your actual ComfyUI workflow JSON and inject parameters.
    """
    online, _ = await check_service_online(f"{COMFYUI_HOST}/system_stats")
    if not online:
        raise HTTPException(status_code=503, detail="ComfyUI offline — check Victus connection.")

    # Load workflow template
    workflow_path = BASE_DIR / "workflows" / f"{req.job_type}.json"
    if not workflow_path.exists():
        raise HTTPException(status_code=404, detail=f"Workflow template '{req.job_type}' not found.")

    try:
        with open(workflow_path, "r") as f:
            workflow = json.load(f)

        # TODO: Inject prompt/title into workflow nodes (workflow-specific)
        # Example for KSampler + CLIP text encode nodes:
        # workflow["6"]["inputs"]["text"] = req.prompt  # Adjust node IDs per workflow

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{COMFYUI_HOST}/prompt",
                json={"prompt": workflow},
                timeout=aiohttp.ClientTimeout(total=30)
            ) as r:
                if r.status == 200:
                    data = await r.json()
                    prompt_id = data.get("prompt_id", "unknown")
                    write_alert("info", "COMFYUI", f"Job queued: {req.job_type} / {prompt_id}")
                    return JSONResponse({"job_id": prompt_id, "status": "queued", "job_type": req.job_type})
                else:
                    raise Exception(f"ComfyUI returned HTTP {r.status}")

    except HTTPException:
        raise
    except Exception as e:
        write_alert("warn", "COMFYUI", f"Generation failed: {str(e)[:100]}")
        raise HTTPException(status_code=502, detail=f"ComfyUI error: {str(e)}")


@app.get("/api/comfy/queue")
async def get_comfy_queue():
    """Returns current ComfyUI queue status."""
    online, _ = await check_service_online(f"{COMFYUI_HOST}/system_stats")
    if not online:
        return JSONResponse({"online": False, "queue": [], "history": []})

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{COMFYUI_HOST}/queue",
                timeout=aiohttp.ClientTimeout(total=5)
            ) as r:
                data = await r.json()
                return JSONResponse({
                    "online":    True,
                    "running":   data.get("queue_running", []),
                    "pending":   data.get("queue_pending", []),
                })
    except Exception as e:
        return JSONResponse({"online": False, "error": str(e)})

# ──────────────────────────────────────────────────────────────────────────────
# API: /api/cancel — Cancel a Hermes task
# ──────────────────────────────────────────────────────────────────────────────

@app.post("/api/cancel/{task_id}")
async def cancel_task(task_id: str):
    """Cancel a queued Hermes task."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{HERMES_HOST}/cancel/{task_id}",
                timeout=aiohttp.ClientTimeout(total=5)
            ) as r:
                if r.status == 200:
                    write_alert("info", "HERMES", f"Task {task_id} cancelled.")
                    return JSONResponse({"ok": True, "task_id": task_id})
                raise Exception(f"HTTP {r.status}")
    except Exception as e:
        # Fallback: remove from queue file
        try:
            queue = read_hermes_queue()
            queue["queued"] = [t for t in queue["queued"] if t.get("task_id") != task_id]
            if HERMES_QUEUE_FILE.parent.exists():
                with open(HERMES_QUEUE_FILE, "w") as f:
                    json.dump(queue, f, indent=2)
            return JSONResponse({"ok": True, "task_id": task_id, "note": "Removed from queue file"})
        except Exception as e2:
            raise HTTPException(status_code=500, detail=f"Cancel failed: {str(e2)}")

# ──────────────────────────────────────────────────────────────────────────────
# STARTUP / SHUTDOWN
# ──────────────────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def on_startup():
    log.info("=" * 60)
    log.info("LDI COMMAND CENTER — cc_server v2.0")
    log.info("Ghost's Workshop :: Cathedral of Glitch")
    log.info(f"Listening on {HOST}:{PORT}")
    log.info(f"Ollama:   {OLLAMA_HOST}")
    log.info(f"ComfyUI:  {COMFYUI_HOST}")
    log.info(f"Hermes:   {HERMES_HOST}")
    log.info(f"Claude:   {'configured' if CLAUDE_API_KEY else 'NOT SET — /api/claude disabled'}")
    log.info(f"Auth:     {'configured' if CC_PASSWORD else 'NOT SET — ALL REQUESTS WILL BE REJECTED'}")
    log.info("=" * 60)
    write_alert("info", "CC_SERVER", f"cc_server started on {HOST}:{PORT}")


@app.on_event("shutdown")
async def on_shutdown():
    log.info("cc_server shutting down.")
    write_alert("info", "CC_SERVER", "cc_server shutdown initiated.")


# ──────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "cc_server:app",
        host=HOST,
        port=PORT,
        reload=False,
        log_level="info",
        access_log=True,
        workers=1,          # Single worker — this is a local tool
    )
