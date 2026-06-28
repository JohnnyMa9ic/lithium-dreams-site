# LDI Command Center — Deployment Guide
**Ghost's Workshop :: Cathedral of Glitch :: Thought Reliquary**

Target: `cc.lithium-dreams.com/app/` → Cloudflare Tunnel → `127.0.0.1:7771`

---

## Prerequisites

- Ubuntu 24.04 (Thought Reliquary at 192.168.4.100)
- Docker + Docker Compose installed
- Cloudflare Tunnel already configured (`cloudflared`)
- Environment variables set (see below)

---

## Directory Structure

```
/home/ldi/cc/
├── index.html          ← The dashboard (copy from this repo)
├── cc_server.py        ← FastAPI server
├── requirements.txt    ← Python deps
├── Dockerfile
├── docker-compose.yml
├── .env                ← Secrets (never commit)
└── workflows/          ← ComfyUI workflow JSON templates
    ├── thumbnail.json
    └── site_asset.json
```

Set this up:

```bash
mkdir -p /home/ldi/cc/workflows
cp index.html cc_server.py requirements.txt Dockerfile docker-compose.yml /home/ldi/cc/
```

---

## Environment Variables

Create `/home/ldi/cc/.env`:

```env
# ─── Authentication ────────────────────────────────
CC_USERNAME=ghost
CC_PASSWORD=your_secure_password_here

# ─── Server ────────────────────────────────────────
CC_HOST=127.0.0.1
CC_PORT=7771

# ─── AI APIs ───────────────────────────────────────
ANTHROPIC_API_KEY=sk-ant-...
CLAUDE_MODEL=claude-3-5-sonnet-20241022

# ─── Local services ────────────────────────────────
OLLAMA_HOST=http://localhost:11434
COMFYUI_HOST=http://192.168.4.X:8188   # Replace X with Victus IP
HERMES_HOST=http://localhost:8001       # Your Hermes orchestrator port

# ─── Paths ─────────────────────────────────────────
HERMES_QUEUE_PATH=/home/ldi/hermes/queue.json
INTAKE_PATH=/home/ldi/glasshouse/intake
ASSETS_OUTPUT_PATH=/home/ldi/assets/output
ALERT_LOG_PATH=/home/ldi/logs/alerts.jsonl
EPISODES_PATH=/home/ldi/episodes/tracker.json

# ─── Signal/Social APIs (wire as you connect them) ─
YOUTUBE_API_KEY=
YOUTUBE_CHANNEL_ID=
TRANSISTOR_API_KEY=
TRANSISTOR_SHOW_ID=
CLOUDFLARE_API_TOKEN=
CLOUDFLARE_ZONE_ID=
CONVERTKIT_API_KEY=
```

Secure the file:
```bash
chmod 600 /home/ldi/cc/.env
```

---

## requirements.txt

```
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
psutil>=6.0.0
anthropic>=0.34.0
aiohttp>=3.10.0
python-multipart>=0.0.9
pydantic>=2.0.0
```

---

## Dockerfile

```dockerfile
FROM python:3.12-slim

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY cc_server.py .
COPY index.html .
COPY workflows/ ./workflows/

# Create log directories
RUN mkdir -p /home/ldi/logs /home/ldi/hermes /home/ldi/glasshouse/intake /home/ldi/assets/output /home/ldi/episodes

# Non-root user for security
RUN useradd -m -u 1000 ghost && chown -R ghost:ghost /app /home/ldi
USER ghost

EXPOSE 7771

CMD ["python", "-m", "uvicorn", "cc_server:app", "--host", "0.0.0.0", "--port", "7771", "--workers", "1"]
```

---

## docker-compose.yml

```yaml
version: "3.9"

services:
  cc_server:
    build: .
    container_name: ldi-cc-server
    restart: unless-stopped

    ports:
      # Bind only to localhost — Cloudflare Tunnel connects here
      - "127.0.0.1:7771:7771"

    env_file:
      - .env

    volumes:
      # Mount host paths so cc_server can read Hermes queue, intake files, etc.
      - /home/ldi/hermes:/home/ldi/hermes
      - /home/ldi/glasshouse:/home/ldi/glasshouse
      - /home/ldi/assets:/home/ldi/assets
      - /home/ldi/episodes:/home/ldi/episodes
      - /home/ldi/logs:/home/ldi/logs

    # Host network access needed for Ollama (localhost:11434) health checks
    # If Ollama runs in Docker, use its container name instead
    network_mode: "host"
    # NOTE: With host networking, ports mapping above is ignored.
    # cc_server binds to 127.0.0.1:7771 directly on the host.

    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:7771/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s

    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
```

> **Note on network_mode host**: Required so cc_server can reach `localhost:11434` (Ollama) 
> and `localhost:8001` (Hermes) without complex Docker networking. If those services 
> also run in Docker, remove `network_mode: "host"` and use Docker network bridges instead.

---

## Build and Start

```bash
cd /home/ldi/cc

# Build image
docker compose build

# Start in detached mode
docker compose up -d

# Verify it's running
docker compose ps
docker compose logs -f cc_server

# Test health endpoint (no auth required)
curl http://127.0.0.1:7771/health
# Expected: {"status":"ok","uptime":5}

# Test authenticated endpoint
curl -u ghost:your_password http://127.0.0.1:7771/api/status
```

---

## Cloudflare Tunnel Configuration

Your tunnel config (`~/.cloudflared/config.yml` or `/etc/cloudflared/config.yml`) 
should already have the cc subdomain. Verify it routes to port 7771:

```yaml
tunnel: YOUR_TUNNEL_ID
credentials-file: /home/ldi/.cloudflared/YOUR_TUNNEL_ID.json

ingress:
  # Ghost's Workshop Command Center
  - hostname: cc.lithium-dreams.com
    service: http://127.0.0.1:7771
    originRequest:
      httpHostHeader: cc.lithium-dreams.com

  # Main site (example)
  - hostname: lithium-dreams.com
    service: http://127.0.0.1:2368

  # Catch-all required by cloudflared
  - service: http_status:404
```

The Basic Auth challenge happens in `TunnelAuthMiddleware` inside cc_server — 
**not** in Cloudflare Access. This is intentional for Ghost's access model.

Restart the tunnel after config changes:
```bash
sudo systemctl restart cloudflared
# or if running as a user service:
cloudflared tunnel run
```

---

## Update Process

```bash
cd /home/ldi/cc

# Pull new files (or copy from build)
cp /path/to/new/index.html .
cp /path/to/new/cc_server.py .

# Rebuild and restart (zero-downtime for static assets, brief restart for server)
docker compose build cc_server
docker compose up -d --no-deps cc_server

# Verify
docker compose logs -f cc_server --tail=20
```

For index.html-only changes (no Python changes), you can copy the file 
without rebuilding — the container reads it from the build context directly.
If you mount it as a volume instead:

```yaml
# Add to docker-compose.yml volumes:
- ./index.html:/app/index.html:ro
```

Then changes to index.html apply immediately without rebuild.

---

## Wiring the Astro /workshop Page

In the Astro site's workshop page (`src/pages/workshop/index.astro` or similar),
the "ENTER WORKSHOP" button should already link to `https://cc.lithium-dreams.com/app/`.

Verify the link target in the Astro source:

```astro
---
// src/pages/attraction/workshop/index.astro (or similar path)
---
<a 
  href="https://cc.lithium-dreams.com/app/" 
  class="enter-workshop-btn"
  rel="noopener"
>
  ENTER WORKSHOP
</a>
```

No changes needed if it already links there. The tunnel handles the routing.

---

## ComfyUI Workflow Templates

Place ComfyUI workflow JSON files in `/home/ldi/cc/workflows/`:

```bash
/home/ldi/cc/workflows/
├── thumbnail.json    ← Episode thumbnail generation workflow
└── site_asset.json   ← Site asset generation workflow
```

Export these from your ComfyUI instance:
1. Build your workflow in ComfyUI
2. Click "Save (API Format)" (enable developer mode in settings first)
3. Save as `thumbnail.json` / `site_asset.json`

Then update `cc_server.py` `generate_comfy_asset()` to inject your prompt 
into the correct workflow node IDs.

---

## API Endpoint Reference

All endpoints require Basic Auth except `/health`.

| Method | Path                          | Description                          |
|--------|-------------------------------|--------------------------------------|
| GET    | `/health`                     | Health check (no auth)               |
| GET    | `/app/`                       | Dashboard HTML                       |
| GET    | `/api/status`                 | System status (CPU, RAM, services)   |
| GET    | `/api/queue`                  | Hermes mission queue                 |
| GET    | `/api/episodes`               | Episode tracker data                 |
| GET    | `/api/alerts`                 | Alert log                            |
| POST   | `/api/dispatch`               | Dispatch mission / agent prompt      |
| POST   | `/api/claude`                 | Direct Claude API query              |
| GET    | `/api/intake`                 | Glasshouse intake submissions        |
| POST   | `/api/intake/{id}/status`     | Update intake status                 |
| GET    | `/api/signals`                | Social/signal feed metrics           |
| POST   | `/api/comfy/generate`         | Queue ComfyUI generation job         |
| GET    | `/api/comfy/queue`            | ComfyUI queue status                 |
| POST   | `/api/cancel/{task_id}`       | Cancel a Hermes task                 |

---

## Troubleshooting

**cc_server not responding:**
```bash
docker compose logs cc_server --tail=50
# Check if port 7771 is in use
ss -tlnp | grep 7771
```

**Cloudflare Tunnel 502:**
```bash
# Verify cc_server is running
curl http://127.0.0.1:7771/health
# Check tunnel logs
sudo journalctl -u cloudflared -n 50
```

**Ollama shows OFFLINE in dashboard:**
```bash
curl http://localhost:11434/api/version
# If that works but dashboard shows offline, the /api/status check may be timing out
# Check cc_server logs for "ollama" timeout messages
```

**ComfyUI shows OFFLINE:**
```bash
# Confirm Victus IP
ping 192.168.4.X  # Replace with actual Victus IP
curl http://192.168.4.X:8188/system_stats
# Update COMFYUI_HOST in .env and restart
```

**Auth rejected (401):**
- Confirm `CC_USERNAME` and `CC_PASSWORD` match what you're sending
- Check that `.env` was loaded: `docker compose exec cc_server env | grep CC_`

---

*"We build what shouldn't exist." — Ghost*
