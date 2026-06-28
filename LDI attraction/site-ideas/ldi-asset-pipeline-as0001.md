---
id: AS-0001
type: asset-pipeline
title: "LDI Asset Generation & Curation Pipeline"
author: ghost/john
version: 1.0
status: active
created: 2026-06-27
tags: [pipeline, comfyui, ai-generation, hermes, brainlab]
depends_on: [VD-0001, HC-0001]
vault: /Volumes/The Crossroads/ldi-docs/engineering/
---

# AS-0001 — LDI Asset Generation & Curation Pipeline

> **Ghost:** This is an operational framework, not a how-to guide. Every stage maps to real code, real file paths, and real hardware in the BrainLab. Read it like a spec, not a tutorial.

> **Bob's note:** The thing that always kills pipelines is the happy path. This doc tries to honor the unhappy paths too. The model is offline. The rate limit hit. John's on a phone at 11pm and needs a thumbnail by midnight. Plan for all three.

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Pipeline Architecture](#2-pipeline-architecture)
3. [Stage 0 — Style Brief](#stage-0-style-brief)
4. [Stage 1 — Request Intake](#stage-1-request-intake)
5. [Stage 2 — Source Material Gathering](#stage-2-source-material-gathering)
6. [Stage 3 — Generation: Model Waterfall](#stage-3-generation-model-waterfall)
7. [Stage 4 — Quality Review](#stage-4-quality-review)
8. [Stage 5 — Curation & Storage](#stage-5-curation--storage)
9. [Stage 6 — Deployment](#stage-6-deployment)
10. [Asset Type Catalog](#10-asset-type-catalog)
11. [LDIAssetDispatcher](#11-ldiassetdispatcher)
12. [StyleClonePipeline — LDI Integration](#12-styleclonepipeline--ldi-integration)
13. [Hermes Integration](#13-hermes-integration)
14. [LDIThumbnailGenerator — Enhanced](#14-ldithumbnailgenerator--enhanced)
15. [Implementation Roadmap](#15-implementation-roadmap)
16. [Gap Analysis](#16-gap-analysis)

---

## 1. EXECUTIVE SUMMARY

### The Philosophy

**Never start from scratch. Always start from style.**

Every asset LDI generates — whether it's a YouTube thumbnail, a hero background for `/museum`, a Glasshouse case file cover, or an enamel pin mockup — derives from one of two canonical style briefs:

- **ATTRACTION DARK** — the visual language of `lithium-dreams.com`: void-black backgrounds, neon amber warmth, signal teal, roadside dossier typography (Bebas Neue + Space Mono), paranormal horror-adjacent atmosphere.
- **GLASSHOUSE LIGHT** — the visual language of `lithium-dreams.com/work`: frosted glass, champagne gold, Satoshi geometry, brushed silver, architectural precision.

These two briefs are the pipeline's constitution. No asset enters the delivery queue without one of them attached. The pipeline's job is to take a natural-language request, route it to the correct brief and model, generate, quality-check, file, and deploy — with John reviewing and approving before anything goes public.

### What This System Does

```
Request (Hermes / Command Center / CLI)
    ↓
Job Schema (asset_type, episode, aesthetic, dims, deadline)
    ↓
Style Brief (Attraction Dark OR Glasshouse Light)
    ↓
Source Material Gathering (script excerpt, page lore, competitor URL)
    ↓
Nemotron Orchestrator — classifies job type, routes to specialist worker:
  image_generation  → ComfyUI FLUX (Victus) → HF free tier → DALL-E 3
  caption/text      → Codex → GPT-4o → Ollama local
  style_analysis    → Gemini 2.0 Flash Vision
  competitor_rsrch  → Perplexity
  writing/brief     → Claude (June 30+) → Nemotron Ultra fallback
  quality_check     → Gemini 2.0 Flash Vision
  video_effects     → Runway ML / AnimateDiff / FFmpeg
    ↓
Quality Gate (automated checks + Gemini Vision + human approval)
    ↓
Canonical Storage (/Volumes/The Crossroads/ldi-assets/ + R2 sync)
    ↓
Deployment (YouTube / site repo / Buffer / merch export)
```

### Design Principles

1. **Aesthetic integrity over speed.** The pipeline has free-tier and paid fallbacks, but the primary path always runs through ComfyUI on the Victus. Speed is for prototyping; quality is for publishing.
2. **Structured, not free-form.** Every job enters via a typed schema. Ad-hoc generation goes to a scratch queue, never directly to the delivery path.
3. **Orchestrator routes, workers do.** Nemotron is the dispatcher: it classifies the job type and routes to the correct specialist (ComfyUI, Gemini Vision, Codex, Perplexity, Runway). The orchestrator does not generate assets, write captions, or run vision analysis itself.
4. **Hermes-native.** The pipeline is callable from natural language via the Hermes `asset-generate` skill. John should never need to open ComfyUI UI to generate a routine asset.
5. **Receipts everywhere.** Every generation writes a JSONL completion receipt including: model used, seed, prompt, output path, quality score, approval status. The full history is queryable.

---

## 2. PIPELINE ARCHITECTURE

### BrainLab Topology

```
┌──────────────────────────────────────────────────────────────────┐
│  MAC MINI M4  (Thought Reliquary — Orchestration)                │
│  192.168.4.100  |  macOS  |  Hermes + Claude Code + Obsidian     │
│  Vault: /Volumes/The Crossroads                                   │
│  Role: job queue reader, dispatcher, storage, Notion sync         │
├──────────────────────────────────────────────────────────────────┤
│         ↕  Tailscale mesh  (also LAN fallback)                   │
├──────────────────────────────────────────────────────────────────┤
│  HP VICTUS  (Windows — GPU Node)                                  │
│  192.168.4.x  |  Windows  |  ComfyUI port 8188                   │
│  Models: FLUX.1 Dev, DreamShaper XL, AnimateDiff, SVD            │
│  Role: primary image + video generation                           │
├──────────────────────────────────────────────────────────────────┤
│         ↕  Tailscale mesh                                         │
├──────────────────────────────────────────────────────────────────┤
│  UBUNTU 24.04 LAPTOP  (Thought Reliquary — Secondary)            │
│  192.168.4.x  |  Docker  |  Claude Code                          │
│  Role: pipeline scripts, Playwright, rembg, upscaling            │
└──────────────────────────────────────────────────────────────────┘
```

### Six-Stage Flow Map

```
STAGE 0: Style Brief ──────────── Canonical style brief per aesthetic system
    │                              (stored at: /ldi-assets/briefs/)
    ▼
STAGE 1: Request Intake ────────── Job schema validation → JSONL queue
    │                              (queue: /ldi-assets/queue/pending.jsonl)
    ▼
STAGE 2: Source Material ──────── Episode scripts, page lore, competitor URLs
    │                              (enriched job written back to queue)
    ▼
STAGE 3: Generation ────────────── Nemotron routes to specialist worker (image/caption/vision)
    │                              (raw output: /ldi-assets/raw/)
    ▼
STAGE 4: Quality Review ────────── Automated + Gemini Vision + John approval
    │                              (approval queue: /ldi-assets/pending-review/)
    ▼
STAGE 5: Curation & Storage ────── Canonical naming, R2 sync, Notion registry
    │                              (final: /ldi-assets/approved/)
    ▼
STAGE 6: Deployment ────────────── Platform-specific push (YouTube/site/Buffer)
```

---

## 3. STAGE 0 — STYLE BRIEF

The style brief is a JSON file that encodes everything the generation pipeline needs to stay visually consistent with a given aesthetic system. These are **not regenerated per-request** — they are stable canonical documents that are updated only when the design system changes.

### Storage Location

```
/Volumes/The Crossroads/ldi-assets/briefs/
├── attraction-dark.brief.json
└── glasshouse-light.brief.json
```

### Attraction Dark Style Brief

```json
{
  "id": "attraction-dark",
  "display_name": "Attraction Dark",
  "url_scope": "lithium-dreams.com (root + all rooms)",
  "last_updated": "2026-06-27",
  "color_palette": {
    "void": "#0a0907",
    "void_deep": "#060504",
    "surface": "#141210",
    "surface_warm": "#1a1610",
    "surface_cool": "#0d1214",
    "teal": "#00e5cc",
    "teal_dim": "#00a090",
    "amber": "#d4820a",
    "amber_bright": "#f0a020",
    "crimson": "#c0281a",
    "gold": "#b08840",
    "text_primary": "#e8dcc0",
    "text_secondary": "#a89870",
    "text_dim": "#5a5040",
    "parchment": "#f0e8d0"
  },
  "typography": {
    "display": "Bebas Neue",
    "body": "Inter",
    "mono": "Space Mono",
    "japanese": "Noto Serif JP",
    "heading_case": "uppercase",
    "heading_tracking": "tight to normal",
    "mono_tracking": "widest"
  },
  "visual_mood": {
    "adjectives": ["atmospheric", "eerie", "warm", "decaying", "alive"],
    "aesthetic_references": ["roadside attraction", "paranormal documentary", "1970s dossier", "atmospheric horror"],
    "contrast": "high",
    "saturation": "muted with electric accents",
    "lighting": "candlelight warmth + cold teal signal glow"
  },
  "comfyui_defaults": {
    "model_primary": "FLUX.1-dev",
    "sampler": "euler_ancestral",
    "steps": 35,
    "cfg_scale": 3.5,
    "base_positive": "cinematic atmospheric photography, night scene, volumetric fog, bioluminescent teal lighting, rain-slicked surfaces, deep shadows, warm amber practical lights, overgrown stone architecture, dark forest atmosphere, 8K ultra-detailed, anamorphic lens, moody noir, slightly surreal, hyperrealistic",
    "base_negative": "daytime, bright sunlight, white background, modern architecture, corporate, sterile, clean, overexposed, cartoon, anime, illustration, painting, text, watermark, chromatic aberration, blurry"
  },
  "dalle3_style_suffix": "dark atmospheric paranormal aesthetic, roadside attraction, void black background with amber and teal accents, cinematic, dramatic lighting, Bebas Neue typography feel",
  "quality_check_prompt": "Does this image feel like it belongs in a 1970s roadside attraction that has been taken over by something supernatural? Dominant colors should be deep blacks, warm amber, and cold teal. No modern corporate visual language."
}
```

### Glasshouse Light Style Brief

```json
{
  "id": "glasshouse-light",
  "display_name": "Glasshouse Light",
  "url_scope": "lithium-dreams.com/work",
  "last_updated": "2026-06-27",
  "color_palette": {
    "void": "#0e1117",
    "surface_dark": "#161b24",
    "slate": "#2d3748",
    "champagne": "#c8a96e",
    "champagne_dim": "#9a7d4a",
    "walnut": "#6b4c30",
    "sky": "#4a90a4",
    "off_white": "#f5f6f7",
    "text_dark": "#0e1117",
    "text_mid": "#4a5568",
    "text_light": "#f5f6f7"
  },
  "typography": {
    "all": "Satoshi",
    "mono": "JetBrains Mono",
    "heading_weight": 600,
    "body_weight": 400,
    "heading_case": "mixed",
    "heading_tracking": "normal"
  },
  "visual_mood": {
    "adjectives": ["clean", "confident", "material", "contemporary"],
    "aesthetic_references": ["architectural glass studio", "precision workspace", "brushed steel", "living botanicals"],
    "contrast": "medium-high",
    "saturation": "restrained with champagne gold accent",
    "lighting": "diffused daylight through glass"
  },
  "comfyui_defaults": {
    "model_primary": "SDXL-base-1.0",
    "sampler": "dpmpp_2m_karras",
    "steps": 35,
    "cfg_scale": 8.5,
    "base_positive": "architectural photography, glass studio interior, brushed steel, warm daylight, bonsai on desk, minimal precision environment, professional, clean lines",
    "base_negative": "dark, horror, occult, vintage, distressed, grain, noise, paranormal, supernatural"
  },
  "dalle3_style_suffix": "Glasshouse studio aesthetic, champagne gold and brushed silver, frosted glass, architectural precision, Satoshi font feel, professional clean minimal",
  "quality_check_prompt": "Does this image feel like it belongs in a high-end architectural glass studio or creative consultancy? Colors should be champagne gold, brushed silver, near-black navy. Clean. No dark paranormal aesthetic."
}
```

### Brief Update Protocol

Style briefs are updated only when VD-0001 is revised. When updating:

1. Edit the brief JSON at the canonical path
2. Run the QA suite against the last 10 approved assets of that system to verify the update doesn't break consistency
3. Bump `last_updated`
4. Log the change in the brief's `changelog` array

---

## 4. STAGE 1 — REQUEST INTAKE

### Entry Points

Requests enter the pipeline from three sources:

| Entry Point | How | Schema Created By |
|-------------|-----|-------------------|
| **Hermes agent** | Natural language → parsed to schema | Hermes `asset-generate` skill |
| **Command Center** | Asset Generation panel form | Form validation on submit |
| **CLI / manual** | Python script call or direct JSONL write | Operator (John) |

### Job Schema

Every job is a JSON object. Required fields are marked `*`.

```json
{
  "job_id": "thumb-ep03-warden-20260627-001",
  "asset_type": "thumbnail",
  "aesthetic_system": "attraction-dark",
  "episode_id": "EP03",
  "page_slug": null,
  "title_text": "THE FLATWOODS MONSTER",
  "subtitle_text": "Episode 3 · Paranormal Pantheon",
  "dimensions": { "width": 1280, "height": 720 },
  "channel": "warden",
  "deadline": "2026-06-28T23:59:00-05:00",
  "priority": "high",
  "source_material": {
    "episode_script_path": "/Volumes/The Crossroads/ldi-content/ep03/script.md",
    "visual_brief": null,
    "competitor_url": null
  },
  "model_preference": "comfyui",
  "ab_variants": 2,
  "notes": "Use West Virginia forest at night as hero. Floating red orbs.",
  "requested_by": "john",
  "requested_at": "2026-06-27T09:58:00-05:00",
  "status": "pending"
}
```

### Queue File Format

Jobs are written to a JSONL file on the Reliquary. One JSON object per line.

```
/Volumes/The Crossroads/ldi-assets/queue/
├── pending.jsonl          ← new jobs land here
├── in-progress.jsonl      ← jobs being generated
├── review.jsonl           ← awaiting John's approval
└── completed.jsonl        ← receipts for all finished jobs
```

### Writing a Job to Queue (Python)

```python
import json, uuid
from datetime import datetime
from pathlib import Path

QUEUE_PATH = Path("/Volumes/The Crossroads/ldi-assets/queue/pending.jsonl")

def enqueue_job(
    asset_type: str,
    aesthetic_system: str,
    title_text: str,
    episode_id: str = None,
    page_slug: str = None,
    dimensions: dict = None,
    channel: str = "warden",
    priority: str = "normal",
    notes: str = "",
    model_preference: str = "comfyui",
    ab_variants: int = 1
) -> str:
    """Write a validated job to the pending queue. Returns job_id."""
    
    assert aesthetic_system in ("attraction-dark", "glasshouse-light"), \
        f"Unknown aesthetic system: {aesthetic_system}"
    assert asset_type in VALID_ASSET_TYPES, \
        f"Unknown asset type: {asset_type}"
    
    if dimensions is None:
        dimensions = ASSET_DEFAULTS[asset_type]["dimensions"]
    
    job_id = f"{asset_type}-{episode_id or page_slug or 'misc'}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    job = {
        "job_id": job_id,
        "asset_type": asset_type,
        "aesthetic_system": aesthetic_system,
        "episode_id": episode_id,
        "page_slug": page_slug,
        "title_text": title_text,
        "dimensions": dimensions,
        "channel": channel,
        "priority": priority,
        "model_preference": model_preference,
        "ab_variants": ab_variants,
        "notes": notes,
        "requested_by": "john",
        "requested_at": datetime.utcnow().isoformat() + "Z",
        "status": "pending"
    }
    
    with open(QUEUE_PATH, "a") as f:
        f.write(json.dumps(job) + "\n")
    
    print(f"[QUEUE] Job enqueued: {job_id}")
    return job_id


VALID_ASSET_TYPES = [
    "thumbnail", "podcast-cover", "podcast-episode-art",
    "hero-background", "social-square", "social-story", "social-landscape",
    "newsletter-header", "enamel-pin-mockup", "sticker-sheet",
    "glasshouse-case-file", "arcade-cabinet-art", "blog-header"
]

ASSET_DEFAULTS = {
    "thumbnail":              {"dimensions": {"width": 1280, "height": 720}},
    "podcast-cover":          {"dimensions": {"width": 3000, "height": 3000}},
    "podcast-episode-art":    {"dimensions": {"width": 3000, "height": 3000}},
    "hero-background":        {"dimensions": {"width": 2880, "height": 1800}},
    "social-square":          {"dimensions": {"width": 1080, "height": 1080}},
    "social-story":           {"dimensions": {"width": 1080, "height": 1920}},
    "social-landscape":       {"dimensions": {"width": 1920, "height": 1080}},
    "newsletter-header":      {"dimensions": {"width": 1200, "height": 400}},
    "enamel-pin-mockup":      {"dimensions": {"width": 2048, "height": 2048}},
    "sticker-sheet":          {"dimensions": {"width": 1800, "height": 2400}},
    "glasshouse-case-file":   {"dimensions": {"width": 2480, "height": 3508}},
    "arcade-cabinet-art":     {"dimensions": {"width": 1080, "height": 1350}},
    "blog-header":            {"dimensions": {"width": 1600, "height": 640}},
}
```

---

## 5. STAGE 2 — SOURCE MATERIAL GATHERING

Before generation starts, the job is enriched with source material specific to its type.

### Thumbnail: Episode Script → Visual Moments

```python
import re
from pathlib import Path
from google import genai
import json, base64

def extract_visual_moments_from_script(script_path: str, n: int = 3) -> list[dict]:
    """
    Parse an episode script, extract N key visual moments suitable
    for thumbnail hero images. Returns ranked list of moment dicts.
    """
    script_text = Path(script_path).read_text(encoding="utf-8")
    
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{
            "role": "user",
            "parts": [{"text": f"""
You are helping create YouTube thumbnails for a paranormal/mystery documentary series.

Read this episode script and identify {n} key visual moments that would make compelling
thumbnail hero images. Each moment should be:
- A single dramatic scene or object
- Visually distinctive (high contrast, strong composition)
- Evocative of mystery, paranormal activity, or dread
- Suitable as a full-bleed background with text overlay space

For each moment, return JSON:
{{
  "rank": 1,
  "scene_description": "A lighthouse in a storm, windows dark except one amber glow",
  "visual_elements": ["lighthouse", "storm", "amber window"],
  "mood": "isolated dread",
  "comfyui_prompt": "A full-bleed atmospheric photo...",
  "text_placement": "bottom-left | bottom-right | top-left | center-bottom"
}}

Script:
---
{script_text[:8000]}
---

Return a JSON array of {n} moments, ranked by thumbnail potential (1 = best).
            """}]
        }]
    )
    
    text = response.text
    start, end = text.find("["), text.rfind("]") + 1
    return json.loads(text[start:end])


def enrich_thumbnail_job(job: dict) -> dict:
    """Add visual moments to a thumbnail job from its script."""
    script_path = job.get("source_material", {}).get("episode_script_path")
    if not script_path or not Path(script_path).exists():
        print(f"[WARNING] No script found for {job['job_id']} — using notes field only")
        return job
    
    moments = extract_visual_moments_from_script(script_path, n=3)
    job["source_material"]["visual_moments"] = moments
    
    # Default to rank 1 unless overridden
    if not job.get("selected_moment"):
        job["selected_moment"] = moments[0]
        job["alternate_moments"] = moments[1:]
    
    return job
```

### Hero Background: Page Lore → Environment Description

```python
# Page lore briefs stored at:
# /Volumes/The Crossroads/ldi-assets/page-lore/{page_slug}.md

def enrich_hero_background_job(job: dict) -> dict:
    """Enhance hero background job with page lore and color system."""
    page_slug = job.get("page_slug")
    if not page_slug:
        return job
    
    lore_path = Path(f"/Volumes/The Crossroads/ldi-assets/page-lore/{page_slug}.md")
    if lore_path.exists():
        lore = lore_path.read_text()
        job["source_material"]["page_lore"] = lore[:2000]
    
    # Load per-page prompt template from VD-0001 (pre-extracted to JSON)
    page_prompts_path = Path("/Volumes/The Crossroads/ldi-assets/briefs/hero-prompts.json")
    if page_prompts_path.exists():
        prompts = json.loads(page_prompts_path.read_text())
        if page_slug in prompts:
            job["source_material"]["page_prompt_template"] = prompts[page_slug]
    
    return job


# Hero prompt templates per page (from VD-0001 §7.2)
HERO_PROMPT_TEMPLATES = {
    "deep-garden": "underground root cavern, massive stone lantern, bioluminescent teal root network growing through carved stone walls, deep darkness beyond, teal lighting",
    "museum":      "Victorian curiosity museum interior at night, dark wooden display cases, amber glass specimen jars, dust motes in lantern light, amber lighting",
    "fortune":     "carnival fortune teller booth interior, velvet curtains, neon sign glow, crystal ball on ornate table, warm amber and gold lighting",
    "arcade":      "1980s arcade hallway, glowing cabinet screens teal and amber, low ceiling with steam pipes, fog machine mist on floor, teal and amber lighting",
    "chapel":      "small roadside wedding chapel at dusk, worn wooden interior, single candle on altar, highway visible through window, warm gold lighting",
    "workshop":    "inventor's workshop, signal equipment workbench, blue electrical sparks, blueprint papers, bonsai on windowsill, blue-white lighting",
    "cathedral":   "massive stone cathedral interior, digital glitch artifacts floating in air, fractured light through stained glass, impossible geometry, teal and crimson lighting",
    "broadcasts":  "broadcast tower at night, storm clouds, signal waves visualized as light arcs, very dark, cold blue-white lighting",
    "crossroads":  "rural crossroads at midnight, single hanging traffic light in amber, fog at ground level, no people, vast darkness in all directions",
    "about":       "abstract atmospheric, candlelight illuminating old papers, a figure in silhouette, warm amber and cold teal in tension",
}
```

### Social Cuts: Primary Asset → Auto-Crop

```python
from PIL import Image

def generate_social_crops(source_path: str, output_dir: str) -> dict[str, str]:
    """
    Auto-crop a primary asset (e.g. thumbnail 1280×720) into social formats.
    Returns dict of format → output_path.
    Uses smart center-weighted crop rather than dumb center crop.
    """
    source = Image.open(source_path)
    w, h = source.size
    output_paths = {}
    
    formats = {
        "social-square":    (1080, 1080),
        "social-story":     (1080, 1920),
        "social-landscape": (1920, 1080),
    }
    
    for fmt, (target_w, target_h) in formats.items():
        # Calculate smart crop (bias toward center, slightly above-center for faces/subjects)
        aspect = target_w / target_h
        
        if w / h > aspect:
            # Source is wider than target — crop sides
            new_w = int(h * aspect)
            left = (w - new_w) // 2
            crop = source.crop((left, 0, left + new_w, h))
        else:
            # Source is taller than target — crop top/bottom (prefer upper 40%)
            new_h = int(w / aspect)
            top = int((h - new_h) * 0.4)
            crop = source.crop((0, top, w, top + new_h))
        
        out = crop.resize((target_w, target_h), Image.LANCZOS)
        
        base = Path(source_path).stem
        out_path = str(Path(output_dir) / f"{base}-{fmt}.png")
        out.save(out_path, "PNG")
        output_paths[fmt] = out_path
    
    return output_paths
```

---

## 6. STAGE 3 — GENERATION: WORKER ROUTING

The orchestrator (Nemotron) receives a classified job and routes it to the specialist worker for that task type. The orchestrator itself is lightweight routing logic only — it does not generate images, write captions, or run vision analysis. Each specialist handles its own fallback chain internally.

**Pipeline philosophy: free first, local second, paid as last resort.** The system is designed to run a complete episode asset set at near-zero cost using ComfyUI + free API tiers. Paid APIs (DALL-E 3, Runway) are emergency fallbacks only, not defaults.

### Worker Routing Map

| Job Type | Primary Worker | Fallback 1 | Fallback 2 | Notes |
|----------|---------------|-----------|-----------|-------|
| `image_generation` | ComfyUI FLUX.1-dev (Victus GPU, $0.00) | HuggingFace InferenceClient ($0.00, rate limited) | DALL-E 3 ($0.04–0.08/img, emergency only) | Victus must be reachable |
| `caption` / `text` | Codex (code-adjacent, structured output) | GPT-4o | Ollama `llama3.1:8b` local | Codex for structured JSON; GPT-4o for prose |
| `style_analysis` | Gemini 2.0 Flash Vision ($0.00) | GPT-4o vision (~$0.01/img) | Ollama `llava` local | Gemini is primary for ALL vision tasks |
| `competitor_research` | Perplexity API (web search + synthesis) | Manual via Playwright | — | For live competitor thumbnail/site lookup |
| `writing` / `brief` | Claude (June 30+) | Nemotron Ultra via OpenRouter ($0.00) | GPT-4o | Claude returns June 30; Nemotron covers until then |
| `quality_check` | Gemini 2.0 Flash Vision ($0.00) | GPT-4o vision | Automated PIL checks only | All post-gen QA routes here |
| `video_effects` | AnimateDiff via ComfyUI (Victus, $0.00) | Runway ML Gen4 Turbo (~$0.25/5s) | FFmpeg static ($0.00) | Local AnimateDiff first |

### Orchestrator Routing Decision Tree

```
Job arrives at orchestrator (Nemotron — Mac Mini)
         │
         ▼
Classify job_type from job schema
  ├─ image_generation  → _call_worker('image', job)    → ComfyUI → HF → DALL-E 3
  ├─ caption           → _call_worker('caption', job)  → Codex → GPT-4o → Ollama
  ├─ style_analysis    → _call_worker('vision', job)   → Gemini 2.0 Flash
  ├─ competitor_rsrch  → _call_worker('research', job) → Perplexity
  ├─ writing/brief     → _call_worker('writing', job)  → Claude (Nemotron fallback)
  ├─ quality_check     → _call_worker('vision', job)   → Gemini 2.0 Flash
  └─ video_effects     → _call_worker('video', job)    → AnimateDiff → Runway → FFmpeg
         │
         ▼
Worker executes, returns result to orchestrator
         │
         ▼
Orchestrator collects result, writes receipt
         │
         ▼
Quality check: _call_worker('vision', output_path)
         │
    pass ┴ fail
     │         │
  → review   → requeue with failure note + Telegram alert
```

### Image Generation Worker Fallback Chain

```
Is ComfyUI (Victus) reachable? ─── YES ──→ FLUX.1-dev ($0.00, local GPU)
         │                                       │
         NO                              succeeds → done
         │                                       │
         ▼                              fails after 2 retries
Use HF InferenceClient ──────────────→ FLUX.1-dev free tier ($0.00, rate limited)
         │                                       │
         NO / rate limited              succeeds → done
         │                                       │
         ▼                               fails
DALL-E 3 (paid emergency only) ──────→ $0.04–0.08/image
                                              │
                                         fails
                                              │
                                         FAILED queue + Telegram alert
```

### Caption Worker Fallback Chain

```
Codex available? ────────────────────────── YES ──→ structured JSON caption
         │                                              │
         NO / fails                            succeeds → done
         │
         ▼
GPT-4o (paid fallback) ──────────────────────────────→ prose/structured result
         │
         fails / no internet
         │
         ▼
Ollama llama3.1:8b (local always-on) ──────────────→ always works offline
```

### Waterfall Config Per Asset Type

```python
WATERFALL_CONFIG = {
    "thumbnail": [
        {
            "provider": "comfyui",
            "model": "FLUX.1-dev",
            "workflow": "workflows/thumbnail-flux.json",
            "estimated_time_sec": 45,
            "cost_usd": 0.00,
        },
        {
            "provider": "hf",
            "model": "black-forest-labs/FLUX.1-dev",
            "estimated_time_sec": 120,
            "cost_usd": 0.00,   # Free tier (rate limited)
        },
        {
            "provider": "dalle3",
            "model": "dall-e-3",
            "size": "1792x1024",
            "quality": "hd",
            "estimated_time_sec": 15,
            "cost_usd": 0.08,   # HD 1792x1024 — paid emergency only
        },
    ],
    "hero-background": [
        {
            "provider": "comfyui",
            "model": "FLUX.1-dev",
            "workflow": "workflows/hero-background-flux.json",
            "size_override": "2880x1800",
            "estimated_time_sec": 90,
            "cost_usd": 0.00,
        },
        {
            "provider": "hf",
            "model": "black-forest-labs/FLUX.1-dev",
            "estimated_time_sec": 180,
            "cost_usd": 0.00,
        }
    ],
    "video-effect": [
        {
            "provider": "comfyui-animatediff",
            "model": "mm_sd_v15_v2",
            "workflow": "workflows/animatediff.json",
            "estimated_time_sec": 120,
            "cost_usd": 0.00,
        },
        {
            "provider": "runway",
            "model": "gen4_turbo",
            "estimated_time_sec": 60,
            "cost_usd": 0.25,   # ~25 credits for 5s @ Gen4 Turbo
        },
        {
            "provider": "ffmpeg-static",
            "estimated_time_sec": 10,
            "cost_usd": 0.00,   # Local FFmpeg fallback — no AI, just effects
        }
    ],
    "enamel-pin-mockup": [
        {
            "provider": "comfyui",
            "model": "DreamShaper XL",
            "workflow": "workflows/pin-mockup-sdxl.json",
            "estimated_time_sec": 45,
            "cost_usd": 0.00,
        },
        {
            "provider": "hf",
            "model": "black-forest-labs/FLUX.1-dev",
            "estimated_time_sec": 120,
            "cost_usd": 0.00,   # Free tier (rate limited)
        },
        {
            "provider": "dalle3",
            "model": "dall-e-3",
            "size": "1024x1024",
            "quality": "standard",
            "estimated_time_sec": 12,
            "cost_usd": 0.04,   # Paid emergency only
        },
    ],
    "podcast-cover": [
        {
            "provider": "comfyui",
            "model": "FLUX.1-dev",
            "workflow": "workflows/podcast-cover-flux.json",
            "estimated_time_sec": 60,
            "cost_usd": 0.00,
        },
        {
            "provider": "hf",
            "model": "black-forest-labs/FLUX.1-dev",
            "estimated_time_sec": 120,
            "cost_usd": 0.00,   # Free tier (rate limited)
        },
        {
            "provider": "dalle3",
            "model": "dall-e-3",
            "size": "1024x1024",
            "quality": "hd",
            "estimated_time_sec": 12,
            "cost_usd": 0.04,   # Paid emergency only
        },
    ],
    "glasshouse-case-file": [
        {
            "provider": "comfyui",
            "model": "SDXL-base-1.0",
            "workflow": "workflows/case-file-sdxl.json",
            "estimated_time_sec": 45,
            "cost_usd": 0.00,
        },
        {
            "provider": "hf",
            "model": "black-forest-labs/FLUX.1-dev",
            "estimated_time_sec": 120,
            "cost_usd": 0.00,   # Free tier (rate limited)
        },
        {
            "provider": "dalle3",
            "model": "dall-e-3",
            "size": "1024x1024",
            "quality": "standard",
            "estimated_time_sec": 12,
            "cost_usd": 0.04,   # Paid emergency only
        },
    ],
}

# Social crops never use AI — they derive from the primary asset via PIL
# (see generate_social_crops in Stage 2)
WATERFALL_CONFIG["social-square"]    = [{"provider": "pil-crop", "cost_usd": 0.00}]
WATERFALL_CONFIG["social-story"]     = [{"provider": "pil-crop", "cost_usd": 0.00}]
WATERFALL_CONFIG["social-landscape"] = [{"provider": "pil-crop", "cost_usd": 0.00}]
```

### ComfyUI Reachability Check

```python
import urllib.request
import json

VICTUS_COMFYUI = "192.168.4.x:8188"  # Set to actual Victus LAN IP

def comfyui_is_available(server: str = VICTUS_COMFYUI, timeout: int = 5) -> bool:
    """Check if ComfyUI on the Victus is up and has GPU available."""
    try:
        url = f"http://{server}/system_stats"
        with urllib.request.urlopen(url, timeout=timeout) as r:
            stats = json.loads(r.read())
            # Confirm a GPU is present and active
            devices = stats.get("system", {}).get("devices", [])
            return any(d.get("name", "").lower() != "cpu" for d in devices)
    except Exception:
        return False
```

---

## 7. STAGE 4 — QUALITY REVIEW

Three layers of QA in sequence. Automated → Gemini Vision → Human.

### Layer 1: Automated Checks

```python
from PIL import Image
from colorthief import ColorThief
import math

# LDI palette for color match scoring
ATTRACTION_DARK_PALETTE = [
    (10, 9, 7),     # void
    (20, 18, 16),   # surface
    (0, 229, 204),  # teal
    (212, 130, 10), # amber
    (192, 40, 26),  # crimson
    (232, 220, 192),# text primary
]

GLASSHOUSE_LIGHT_PALETTE = [
    (14, 17, 23),   # void
    (200, 169, 110),# champagne
    (45, 55, 72),   # slate
    (74, 144, 164), # sky
    (245, 246, 247),# off-white
]

def color_distance(c1: tuple, c2: tuple) -> float:
    """Euclidean distance in RGB space."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def palette_match_score(image_path: str, reference_palette: list, n_colors: int = 6) -> float:
    """
    Score 0.0 – 1.0 representing how closely the image's dominant colors
    match the reference brand palette.
    """
    ct = ColorThief(image_path)
    image_palette = ct.get_palette(color_count=n_colors)
    
    total_score = 0.0
    for img_color in image_palette:
        # Find closest reference color
        min_dist = min(color_distance(img_color, ref) for ref in reference_palette)
        # Max possible distance in RGB space: sqrt(3 * 255^2) ≈ 441.7
        normalized = 1.0 - (min_dist / 441.7)
        total_score += normalized
    
    return total_score / n_colors

def check_resolution(image_path: str, min_width: int, min_height: int) -> bool:
    img = Image.open(image_path)
    return img.width >= min_width and img.height >= min_height

def check_no_watermark(image_path: str) -> bool:
    """
    Rough heuristic: check for suspiciously bright white regions in corners
    (common watermark location). For production, use a vision model.
    """
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    corners = [
        img.crop((0, 0, 80, 30)),
        img.crop((w-80, 0, w, 30)),
        img.crop((0, h-30, 80, h)),
        img.crop((w-80, h-30, w, h)),
    ]
    for c in corners:
        pixels = list(c.getdata())
        avg_brightness = sum(sum(p) / 3 for p in pixels) / len(pixels)
        if avg_brightness > 220:  # Suspiciously bright corner
            return False
    return True

def run_automated_qc(image_path: str, job: dict) -> dict:
    """Run all automated quality checks. Returns QC report dict."""
    asset_type = job["asset_type"]
    dims = job["dimensions"]
    aesthetic = job["aesthetic_system"]
    
    palette = ATTRACTION_DARK_PALETTE if aesthetic == "attraction-dark" else GLASSHOUSE_LIGHT_PALETTE
    
    report = {
        "job_id": job["job_id"],
        "image_path": image_path,
        "resolution_pass": check_resolution(image_path, dims["width"], dims["height"]),
        "palette_score": palette_match_score(image_path, palette),
        "no_watermark": check_no_watermark(image_path),
        "passed": False,
    }
    
    report["passed"] = (
        report["resolution_pass"] and
        report["palette_score"] >= 0.45 and
        report["no_watermark"]
    )
    
    return report
```

### Layer 2: Gemini Vision — "Does This Look Like LDI?"

```python
import base64
from google import genai

def gemini_ldi_check(image_path: str, job: dict) -> dict:
    """
    Ask Gemini Vision to evaluate whether the generated asset is on-brand for LDI.
    Returns structured dict with pass/fail and notes.
    """
    aesthetic = job["aesthetic_system"]
    brief_path = f"/Volumes/The Crossroads/ldi-assets/briefs/{aesthetic}.brief.json"
    brief = json.loads(Path(brief_path).read_text())
    
    check_prompt = brief["quality_check_prompt"]
    
    client = genai.Client()
    
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[{
            "role": "user",
            "parts": [
                {"text": f"""
You are quality control for an AI asset generation pipeline.
Evaluate this generated image against the following brand check:

BRAND CHECK: {check_prompt}

Also evaluate:
1. Is the color palette appropriate? (check for teal, amber, deep black if Attraction Dark; champagne, slate, near-black if Glasshouse)
2. Is the mood correct? (atmospheric/paranormal for Attraction Dark; clean/professional for Glasshouse)  
3. Are there any obvious AI artifacts? (malformed hands, text in image, watermarks)
4. Is there sufficient visual space for text overlay?

Return JSON:
{{
  "brand_check_pass": true/false,
  "color_palette_appropriate": true/false,
  "mood_correct": true/false,
  "no_artifacts": true/false,
  "text_space_available": true/false,
  "overall_score": 7.5,
  "notes": "What works and what doesn't",
  "improvement_suggestion": "Specific prompt changes to improve"
}}
                """},
                {
                    "inline_data": {
                        "mime_type": "image/png",
                        "data": img_b64
                    }
                }
            ]
        }]
    )
    
    text = response.text
    start, end = text.find("{"), text.rfind("}") + 1
    result = json.loads(text[start:end])
    result["gemini_passed"] = (
        result.get("brand_check_pass", False) and
        result.get("overall_score", 0) >= 6.0
    )
    return result
```

### Layer 3: Human Approval (John via Command Center)

Assets that pass both automated and Gemini checks are moved to:

```
/Volumes/The Crossroads/ldi-assets/pending-review/
```

The Command Center Asset Generation panel polls this directory and presents thumbnails for John's approval. John can:
- **Approve** → moves to `/approved/`, triggers Stage 5
- **Reject** → returns to queue with `rejection_notes` appended; triggers regeneration with improved prompt
- **Request variant** → generates A/B variant with same parameters but different seed

> **Bob's note:** The human gate is non-negotiable. Automated QC catches resolution failures and watermarks. Gemini catches obvious off-brand outputs. But neither catches "this is technically fine but it's just ugly." That call stays with John.

---

## 8. STAGE 5 — CURATION & STORAGE

### File Naming Convention

```
{asset_type}-{episode_id|page_slug|misc}-{variant}-{datestamp}.{ext}
```

**Examples:**

```
thumbnail-ep03-v1-20260628.png
thumbnail-ep03-v2-20260628.png          ← A/B variant
hero-background-museum-v1-20260702.webp
podcast-cover-paranormal-pantheon-v1-20260615.png
enamel-pin-mockup-bob-approved-v1-20260710.png
social-square-ep03-v1-20260628.png
newsletter-header-after-closing-brief-v1-20260701.png
```

### Directory Structure on The Crossroads

```
/Volumes/The Crossroads/ldi-assets/
├── briefs/
│   ├── attraction-dark.brief.json
│   ├── glasshouse-light.brief.json
│   └── hero-prompts.json
├── queue/
│   ├── pending.jsonl
│   ├── in-progress.jsonl
│   ├── review.jsonl
│   └── completed.jsonl
├── raw/                          ← unreviewed outputs from generator
├── pending-review/               ← passed auto-QC, awaiting John
├── approved/
│   ├── thumbnails/
│   │   ├── ep01/
│   │   ├── ep02/
│   │   └── ep03/
│   ├── hero-backgrounds/
│   ├── podcast-covers/
│   ├── social/
│   │   ├── square/
│   │   ├── story/
│   │   └── landscape/
│   ├── newsletter/
│   ├── merch/
│   │   ├── pins/
│   │   └── stickers/
│   └── glasshouse/
│       └── case-files/
├── page-lore/                    ← per-page lore briefs for hero gen
└── logs/
    └── receipts.jsonl            ← one receipt per completed job
```

### Completion Receipt Format

```python
def write_receipt(
    job: dict,
    output_path: str,
    provider_used: str,
    model_used: str,
    seed: int,
    prompt: str,
    qc_report: dict,
    gemini_report: dict,
    approved: bool
) -> None:
    """Write a completion receipt to the JSONL log."""
    receipt = {
        "job_id": job["job_id"],
        "asset_type": job["asset_type"],
        "episode_id": job.get("episode_id"),
        "output_path": output_path,
        "provider_used": provider_used,
        "model_used": model_used,
        "seed": seed,
        "prompt": prompt,
        "qc_automated": qc_report,
        "qc_gemini": gemini_report,
        "approved": approved,
        "completed_at": datetime.utcnow().isoformat() + "Z",
    }
    
    log_path = Path("/Volumes/The Crossroads/ldi-assets/logs/receipts.jsonl")
    with open(log_path, "a") as f:
        f.write(json.dumps(receipt) + "\n")
```

### Cloudflare R2 Sync

Web-ready assets (thumbnails, hero-backgrounds, social, newsletter) are synced to R2 after approval.

```bash
# Install rclone, configure R2 remote once:
# rclone config → create remote "ldi-r2" with Cloudflare R2 credentials

# Sync approved web-ready assets to R2
rclone sync \
  /Volumes/The\ Crossroads/ldi-assets/approved/ \
  ldi-r2:ldi-assets/approved/ \
  --include "*.webp" \
  --include "*.png" \
  --include "*.jpg" \
  --exclude "merch/**" \
  --exclude "glasshouse/case-files/**"  # Client docs stay private
```

### Notion Asset Registry

Every approved asset gets a Notion page in the LDI Asset Registry database.

```python
# Notion integration: add record to Asset Registry database
NOTION_ASSET_DB_ID = "your-database-id"

def register_in_notion(receipt: dict, notion_client) -> None:
    notion_client.pages.create(
        parent={"database_id": NOTION_ASSET_DB_ID},
        properties={
            "Name":         {"title": [{"text": {"content": receipt["job_id"]}}]},
            "Asset Type":   {"select": {"name": receipt["asset_type"]}},
            "Episode":      {"select": {"name": receipt["episode_id"] or "—"}},
            "Status":       {"select": {"name": "Approved" if receipt["approved"] else "Rejected"}},
            "Model Used":   {"rich_text": [{"text": {"content": receipt["model_used"]}}]},
            "Output Path":  {"url": receipt["output_path"]},
            "Approved":     {"checkbox": receipt["approved"]},
            "Completed At": {"date": {"start": receipt["completed_at"][:10]}},
        }
    )
```

---

## 9. STAGE 6 — DEPLOYMENT

### YouTube Thumbnail Upload (Stub)

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_thumbnail_to_youtube(
    video_id: str,
    thumbnail_path: str,
    credentials_path: str = "/Volumes/The Crossroads/secrets/youtube-oauth.json"
) -> bool:
    """
    Upload a thumbnail to a YouTube video via YouTube Data API v3.
    Requires OAuth credentials with youtube.force-ssl scope.
    
    NOTE: YouTube requires a verified phone number to use custom thumbnails.
    Also requires that the thumbnail does NOT violate YT thumbnail policy.
    """
    try:
        creds = Credentials.from_authorized_user_file(credentials_path)
        youtube = build("youtube", "v3", credentials=creds)
        
        media = MediaFileUpload(thumbnail_path, mimetype="image/png")
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=media
        ).execute()
        
        print(f"[DEPLOY] Thumbnail uploaded to video {video_id}")
        return True
    except Exception as e:
        print(f"[DEPLOY ERROR] YouTube upload failed: {e}")
        print("[DEPLOY] Manual fallback: open YouTube Studio → Custom Thumbnail")
        return False
```

### Hero Background: Site Repo Deploy

```python
import subprocess

def deploy_hero_background(
    approved_path: str,
    page_slug: str,
    site_repo_path: str = "/Volumes/The Crossroads/lithium-dreams-site"
) -> bool:
    """
    Copy approved hero background to the site repo's public/assets/,
    convert to WebP if needed, then commit and push.
    Auto-deploys via Vercel/Cloudflare Pages on push.
    """
    from PIL import Image
    import shutil
    
    dest_dir = Path(site_repo_path) / "public" / "assets" / "backgrounds"
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert to WebP if not already
    img = Image.open(approved_path)
    webp_name = f"{page_slug}-hero.webp"
    webp_path = dest_dir / webp_name
    img.save(webp_path, "WEBP", quality=85)
    
    # Also generate mobile crop (768×1024)
    mobile = img.resize((768, 1024), Image.LANCZOS)
    mobile.save(dest_dir / f"{page_slug}-hero-mobile.webp", "WEBP", quality=85)
    
    # Git commit and push
    try:
        subprocess.run(["git", "-C", site_repo_path, "add", "."], check=True)
        subprocess.run([
            "git", "-C", site_repo_path,
            "commit", "-m", f"feat(assets): update hero background for /{page_slug}"
        ], check=True)
        subprocess.run(["git", "-C", site_repo_path, "push"], check=True)
        print(f"[DEPLOY] Hero background for /{page_slug} pushed to repo")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[DEPLOY ERROR] Git push failed: {e}")
        return False
```

### Social: Buffer API Batch Schedule

```python
import requests

def schedule_social_posts(
    image_paths: dict,  # {"social-square": "path", "social-story": "path"}
    caption: str,
    episode_id: str,
    buffer_api_key: str,
    profile_ids: list[str]  # Buffer profile IDs for IG, TikTok, Bluesky
) -> dict:
    """
    Schedule social posts via Buffer API.
    Posts all format variants to their respective platforms.
    """
    results = {}
    
    platform_format_map = {
        "instagram": "social-square",
        "tiktok": "social-story",
        "bluesky": "social-landscape",
    }
    
    for platform, fmt in platform_format_map.items():
        image_path = image_paths.get(fmt)
        if not image_path:
            continue
        
        # Upload image to Buffer
        with open(image_path, "rb") as f:
            upload_resp = requests.post(
                "https://api.bufferapp.com/1/media/upload.json",
                headers={"Authorization": f"Bearer {buffer_api_key}"},
                files={"file": f}
            )
        
        media_id = upload_resp.json().get("id")
        
        # Create post
        for profile_id in profile_ids:
            post_resp = requests.post(
                "https://api.bufferapp.com/1/updates/create.json",
                headers={"Authorization": f"Bearer {buffer_api_key}"},
                json={
                    "profile_ids": [profile_id],
                    "text": caption,
                    "media": {"photo": media_id},
                    "scheduled_at": "next_optimal_time"  # Buffer auto-scheduling
                }
            )
            results[f"{platform}_{profile_id}"] = post_resp.json()
    
    return results
```

### Merch Export

```python
def export_merch_files(
    approved_path: str,
    asset_type: str,  # "enamel-pin-mockup" | "sticker-sheet"
    export_dir: str = "/Volumes/The Crossroads/ldi-assets/merch-export/"
) -> dict:
    """
    Export print-ready files for Fourthwall merch upload.
    PNG source at 300 DPI equivalent. No AI generation — just file prep.
    """
    Path(export_dir).mkdir(parents=True, exist_ok=True)
    
    img = Image.open(approved_path)
    base = Path(approved_path).stem
    
    outputs = {}
    
    # Print-ready PNG (no resizing — must meet spec from AS-0001 catalog)
    print_path = str(Path(export_dir) / f"{base}-print-ready.png")
    img.save(print_path, "PNG", dpi=(300, 300))
    outputs["print_ready"] = print_path
    
    # Marketing mockup (1200×1200 for Fourthwall listing)
    marketing = img.resize((1200, 1200), Image.LANCZOS)
    marketing_path = str(Path(export_dir) / f"{base}-marketing.png")
    marketing.save(marketing_path, "PNG")
    outputs["marketing"] = marketing_path
    
    print(f"[DEPLOY] Merch export complete: {export_dir}")
    print("[DEPLOY] Manual step: upload to Fourthwall product page")
    
    return outputs
```

---

## 10. ASSET TYPE CATALOG

Complete specification for every asset type the pipeline produces.

| Asset Type | Dimensions | Primary Model | Est. Gen Time | Cost/Asset | Storage Path | Deployment Target |
|------------|-----------|---------------|---------------|------------|--------------|-------------------|
| **YouTube Thumbnail** | 1280×720px | ComfyUI FLUX.1-dev | 45s | $0.00 | `approved/thumbnails/ep##/` | YouTube Data API v3 |
| **Podcast Cover Art** | 3000×3000px | ComfyUI FLUX.1-dev | 60s | $0.00 | `approved/podcast-covers/` | Podcast hosting (RSS) |
| **Podcast Episode Art** | 3000×3000px | ComfyUI FLUX.1-dev | 60s | $0.00 | `approved/podcast-covers/episodes/` | Podcast hosting |
| **Hero Background — /deep-garden** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /museum** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /fortune** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /arcade** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /chapel** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /workshop** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /cathedral** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /broadcasts** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /crossroads** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /about** | 2880×1800px | ComfyUI FLUX.1-dev | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Hero Background — /work (Glasshouse)** | 2880×1800px | ComfyUI SDXL | 90s | $0.00 | `approved/hero-backgrounds/` | Site repo → auto-deploy |
| **Social — Square (1:1)** | 1080×1080px | PIL crop of primary | <5s | $0.00 | `approved/social/square/` | Buffer → Instagram |
| **Social — Story (9:16)** | 1080×1920px | PIL crop of primary | <5s | $0.00 | `approved/social/story/` | Buffer → TikTok |
| **Social — Landscape (16:9)** | 1920×1080px | PIL crop of primary | <5s | $0.00 | `approved/social/landscape/` | Buffer → Bluesky |
| **Newsletter Header** | 1200×400px | ComfyUI FLUX.1-dev | 45s | $0.00 | `approved/newsletter/` | Email platform |
| **Enamel Pin Mockup** | 2048×2048px | ComfyUI DreamShaper XL | 45s | $0.00 | `approved/merch/pins/` | Fourthwall (manual) |
| **Sticker Sheet** | 1800×2400px | ComfyUI SDXL | 60s | $0.00 | `approved/merch/stickers/` | Fourthwall (manual) |
| **Blog / Dossier Header** | 1600×640px | ComfyUI FLUX.1-dev | 45s | $0.00 | `approved/blog-headers/` | Site repo → auto-deploy |
| **Glasshouse Case File Cover** | 2480×3508px (A4) | ComfyUI SDXL | 60s | $0.00 | `approved/glasshouse/case-files/` | Client delivery (private) |
| **Arcade Cabinet Art** | 1080×1350px | ComfyUI FLUX.1-dev | 45s | $0.00 | `approved/arcade-cabinets/` | Site repo → /arcade |

**Cost notes:**
- ComfyUI (local Victus GPU) = $0.00 per asset
- DALL-E 3 fallback: HD 1792×1024 = ~$0.08; standard 1024×1024 = ~$0.04
- HF InferenceClient fallback = $0.00 (rate limited free tier)
- Runway ML video fallback = ~$0.25/5s clip

---

## 11. LDIASSETDISPATCHER

The central orchestration class. Reads from the JSONL job queue, executes the waterfall, handles fallbacks, saves outputs, writes receipts, and optionally notifies via Telegram.

```python
#!/usr/bin/env python3
"""
LDIAssetDispatcher — AS-0001
Reads the pending job queue on The Crossroads, dispatches to ComfyUI on the Victus
(via Tailscale/LAN), falls back to DALL-E 3 or HF on unavailability.
Invocable by Hermes agent, Command Center, or CLI.

Usage:
    python dispatcher.py                  # Process all pending jobs
    python dispatcher.py --job-id JOB_ID  # Process a single specific job
    python dispatcher.py --dry-run        # Validate queue without generating
"""

import os
import json
import uuid
import time
import argparse
import urllib.request
import urllib.parse
import websocket
import io
from pathlib import Path
from datetime import datetime
from PIL import Image
import requests

# ─── CONFIGURATION ────────────────────────────────────────────────────────────

VICTUS_COMFYUI    = os.environ.get("VICTUS_COMFYUI_ADDR", "192.168.4.x:8188")
QUEUE_DIR         = Path("/Volumes/The Crossroads/ldi-assets/queue")
ASSETS_DIR        = Path("/Volumes/The Crossroads/ldi-assets")
BRIEFS_DIR        = ASSETS_DIR / "briefs"
RAW_DIR           = ASSETS_DIR / "raw"
REVIEW_DIR        = ASSETS_DIR / "pending-review"
RECEIPTS_LOG      = ASSETS_DIR / "logs" / "receipts.jsonl"
WORKFLOWS_DIR     = Path("/Volumes/The Crossroads/ldi-assets/workflows")

# Telegram for Hermes dispatch notifications
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID   = os.environ.get("TELEGRAM_CHAT_ID", "")

# ─── COMFYUI CLIENT ───────────────────────────────────────────────────────────

class ComfyUIClient:
    def __init__(self, server: str = VICTUS_COMFYUI):
        self.server = server
        self.client_id = str(uuid.uuid4())

    def is_available(self, timeout: int = 5) -> bool:
        try:
            url = f"http://{self.server}/system_stats"
            with urllib.request.urlopen(url, timeout=timeout) as r:
                stats = json.loads(r.read())
            devices = stats.get("system", {}).get("devices", [])
            return any("cpu" not in d.get("name", "cpu").lower() for d in devices)
        except Exception:
            return False

    def queue_prompt(self, workflow: dict) -> str:
        payload = json.dumps({"prompt": workflow, "client_id": self.client_id}).encode()
        req = urllib.request.Request(f"http://{self.server}/prompt", data=payload)
        return json.loads(urllib.request.urlopen(req).read())["prompt_id"]

    def wait_for_completion(self, prompt_id: str, timeout: int = 300) -> bool:
        ws = websocket.WebSocket()
        ws.connect(f"ws://{self.server}/ws?clientId={self.client_id}")
        ws.settimeout(timeout)
        try:
            while True:
                msg = ws.recv()
                if isinstance(msg, str):
                    data = json.loads(msg)
                    if (data.get("type") == "executing" and
                            data["data"].get("node") is None and
                            data["data"].get("prompt_id") == prompt_id):
                        return True
        except websocket.WebSocketTimeoutException:
            return False
        finally:
            ws.close()

    def get_outputs(self, prompt_id: str) -> list[bytes]:
        url = f"http://{self.server}/history/{prompt_id}"
        with urllib.request.urlopen(url) as r:
            history = json.loads(r.read())
        
        images = []
        for node_output in history.get(prompt_id, {}).get("outputs", {}).values():
            for img in node_output.get("images", []):
                params = urllib.parse.urlencode({
                    "filename": img["filename"],
                    "subfolder": img["subfolder"],
                    "type": img["type"]
                })
                with urllib.request.urlopen(f"http://{self.server}/view?{params}") as r:
                    images.append(r.read())
        return images

    def run_workflow(self, workflow_path: str, overrides: dict = None, 
                     timeout: int = 300) -> list[bytes]:
        """Load workflow JSON, apply overrides, submit, wait, return image bytes."""
        with open(workflow_path) as f:
            workflow = json.load(f)
        
        if overrides:
            for node_id, inputs in overrides.items():
                for key, val in inputs.items():
                    workflow[node_id]["inputs"][key] = val
        
        prompt_id = self.queue_prompt(workflow)
        success = self.wait_for_completion(prompt_id, timeout=timeout)
        
        if not success:
            raise TimeoutError(f"ComfyUI job {prompt_id} timed out after {timeout}s")
        
        return self.get_outputs(prompt_id)


# ─── FALLBACK PROVIDERS ───────────────────────────────────────────────────────

class DALLEProvider:
    def __init__(self):
        from openai import OpenAI
        self.client = OpenAI()

    def generate(self, prompt: str, size: str = "1792x1024", quality: str = "hd") -> bytes:
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality=quality
        )
        img_data = requests.get(response.data[0].url).content
        return img_data


class HFProvider:
    def __init__(self):
        from huggingface_hub import InferenceClient
        self.client = InferenceClient(api_key=os.environ["HF_TOKEN"])

    def generate(self, prompt: str, model: str = "black-forest-labs/FLUX.1-dev") -> bytes:
        image = self.client.text_to_image(prompt=prompt, model=model)
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        return buf.getvalue()


# ─── WORKER CLIENTS ───────────────────────────────────────────────────────────

class CodexWorker:
    """Caption/text generation: Codex → GPT-4o → Ollama local."""

    def complete(self, prompt: str, max_tokens: int = 800) -> str:
        import os, requests

        # Try Codex via OpenAI API (code-davinci or gpt-4o-mini with system role)
        openai_key = os.environ.get("OPENAI_API_KEY", "")
        if openai_key:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=openai_key)
                resp = client.chat.completions.create(
                    model="gpt-4o-mini",   # Codex-adjacent; structured output, low cost
                    messages=[
                        {"role": "system", "content": "You are a structured JSON generator for LDI asset metadata. Return only valid JSON."},
                        {"role": "user",   "content": prompt}
                    ],
                    max_tokens=max_tokens,
                    temperature=0.2,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                print(f"[CodexWorker] OpenAI failed: {e} — trying GPT-4o")

        # GPT-4o fallback (same key)
        if openai_key:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=openai_key)
                resp = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=max_tokens,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                print(f"[CodexWorker] GPT-4o failed: {e} — trying Ollama")

        # Ollama local always-on fallback
        try:
            resp = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "llama3.1:8b", "prompt": prompt, "stream": False},
                timeout=60
            )
            return resp.json()["response"].strip()
        except Exception as e:
            raise RuntimeError(f"[CodexWorker] All caption workers failed. Last error: {e}")


class GeminiVisionWorker:
    """Vision analysis: Gemini 2.0 Flash (primary, free) — all style/QC/vision tasks."""

    def __init__(self):
        from google import genai
        self.client = genai.Client()

    def analyze(self, image_path: str, prompt: str) -> str:
        """Run vision analysis on an image file. Returns raw text response."""
        import base64
        with open(image_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[{
                "role": "user",
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/png", "data": img_b64}}
                ]
            }]
        )
        return response.text

    def qc_check(self, image_path: str, job: dict) -> dict:
        """LDI brand compliance check for a generated asset."""
        aesthetic = job.get("aesthetic_system", "attraction-dark")
        asset_type = job.get("asset_type", "unknown")
        prompt = f"""You are quality-checking an LDI asset for brand compliance.
Asset type: {asset_type}
Aesthetic system: {aesthetic}

Evaluate this image on:
1. Does it match the {aesthetic} palette (void-black bg, teal/amber accents if attraction-dark)?
2. Is the composition appropriate for the asset type?
3. Is there any watermark, artifact, or obvious generation failure?
4. Overall quality score 1–10.

Return JSON:
{{
  "gemini_passed": true/false,
  "palette_match": true/false,
  "composition_ok": true/false,
  "no_artifacts": true/false,
  "overall_score": 8,
  "improvement_suggestion": "..."
}}"""
        text = self.analyze(image_path, prompt)
        start, end = text.find("{"), text.rfind("}") + 1
        if start == -1:
            return {"gemini_passed": False, "overall_score": 0, "improvement_suggestion": text}
        import json
        return json.loads(text[start:end])


class PerplexityWorker:
    """Competitor research via Perplexity API."""

    def search(self, query: str) -> str:
        import os, requests
        api_key = os.environ.get("PERPLEXITY_API_KEY", "")
        if not api_key:
            raise RuntimeError("[PerplexityWorker] PERPLEXITY_API_KEY not set")
        resp = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "llama-3.1-sonar-large-128k-online",
                "messages": [{"role": "user", "content": query}],
                "max_tokens": 1000,
            },
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]


class NemotronOrchestrator:
    """
    Thin routing layer. Classifies an incoming natural-language or structured
    request and returns a validated job schema. Does NOT generate anything.
    Uses OpenRouter Nemotron (free) → GPT-4o → Ollama as fallback.
    """

    MODELS = [
        ("openrouter", "nvidia/nemotron-ultra-253b:free"),
        ("openrouter", "nvidia/nemotron-super-49b:free"),
        ("openai",     "gpt-4o"),
        ("ollama",     "llama3.1:8b"),
    ]

    CLAUDE_AVAILABLE = False  # Claude API on cooldown — returns June 30, 2026

    def classify(self, prompt: str, max_tokens: int = 600) -> str:
        """Route a prompt through the text model waterfall. Returns raw text."""
        import os, requests

        for provider, model in self.MODELS:
            try:
                if provider == "openrouter":
                    key = os.environ.get("OPENROUTER_API_KEY", "")
                    if not key:
                        continue
                    from openai import OpenAI
                    client = OpenAI(
                        api_key=key,
                        base_url="https://openrouter.ai/api/v1",
                    )
                    resp = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=max_tokens,
                        temperature=0.1,
                    )
                    return resp.choices[0].message.content.strip()

                elif provider == "openai":
                    key = os.environ.get("OPENAI_API_KEY", "")
                    if not key:
                        continue
                    from openai import OpenAI
                    client = OpenAI(api_key=key)
                    resp = client.chat.completions.create(
                        model=model,
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=max_tokens,
                    )
                    return resp.choices[0].message.content.strip()

                elif provider == "ollama":
                    resp = requests.post(
                        "http://localhost:11434/api/generate",
                        json={"model": model, "prompt": prompt, "stream": False},
                        timeout=60,
                    )
                    return resp.json()["response"].strip()

            except Exception as e:
                print(f"[Orchestrator] {provider}/{model} failed: {e} — trying next")
                continue

        raise RuntimeError("[Orchestrator] All text models exhausted. Check API keys and Ollama.")


# ─── PROMPT BUILDER ───────────────────────────────────────────────────────────

def build_prompt(job: dict, brief: dict) -> str:
    """Assemble the ComfyUI generation prompt from the job and style brief."""
    base = brief["comfyui_defaults"]["base_positive"]

    selected_moment = job.get("selected_moment", {})
    page_prompt = job.get("source_material", {}).get("page_prompt_template", "")
    notes = job.get("notes", "")

    # Priority: explicit notes > selected moment > page template > base
    subject = notes or selected_moment.get("comfyui_prompt", "") or page_prompt or ""

    if subject:
        return f"{subject}, {base}"
    return base


# ─── MAIN DISPATCHER ─────────────────────────────────────────────────────────

class LDIAssetDispatcher:
    """
    Central orchestration class for the LDI asset pipeline.

    Architecture: intake → route → dispatch → collect → store

    The dispatcher is pure routing logic. It receives a job, classifies it,
    calls the correct specialist worker via _call_worker(), collects the result,
    runs QA, and writes a receipt. It does NOT reason about the asset itself.

    Worker routing:
        image_generation  → ComfyUIClient → HFProvider → DALLEProvider
        caption/text      → CodexWorker
        style_analysis    → GeminiVisionWorker
        competitor_rsrch  → PerplexityWorker
        quality_check     → GeminiVisionWorker.qc_check()

    Invocable by Hermes agent, Command Center, or CLI.

    Usage:
        python dispatcher.py                  # Process all pending jobs
        python dispatcher.py --job-id JOB_ID  # Process a single specific job
        python dispatcher.py --dry-run        # Validate queue without generating
    """

    def __init__(self, dry_run: bool = False):
        self.dry_run     = dry_run
        self.comfyui     = ComfyUIClient()
        self.dalle       = DALLEProvider()
        self.hf          = HFProvider()
        self.gemini      = GeminiVisionWorker()
        self.codex       = CodexWorker()
        self.perplexity  = PerplexityWorker()
        self.orchestrator = NemotronOrchestrator()

        # Ensure directories exist
        for d in [RAW_DIR, REVIEW_DIR, ASSETS_DIR / "logs"]:
            d.mkdir(parents=True, exist_ok=True)

    # ── STAGE 1: Intake ──────────────────────────────────────────────────────

    def intake(self, request: str) -> dict:
        """
        Parse a natural-language request into a validated job schema.
        Calls NemotronOrchestrator.classify() — the orchestrator does the
        classification, the dispatcher only validates and stores the result.
        """
        parse_prompt = f"""Parse this LDI asset generation request into JSON.

Request: "{request}"

Return only valid JSON:
{{
  "asset_type": "thumbnail | hero-background | podcast-cover | enamel-pin-mockup | social-square | social-story | glasshouse-case-file | video-effect | newsletter-header | blog-header",
  "episode_id": "EP01 | EP02 | null",
  "page_slug": "museum | arcade | fortune | chapel | workshop | cathedral | null",
  "title_text": "extracted or inferred title",
  "aesthetic_system": "attraction-dark | glasshouse-light",
  "channel": "warden | ghost | root | null",
  "priority": "high | normal | low",
  "notes": "any specific visual notes",
  "ab_variants": 1,
  "dimensions": {{"width": 1280, "height": 720}}
}}

Rules:
- paranormal/LDI rooms/YouTube → attraction-dark
- client work/Glasshouse → glasshouse-light
- If episode mentioned → asset_type=thumbnail unless stated otherwise
- thumbnail dimensions: 1280x720; hero-background: 2880x1800; podcast-cover: 3000x3000"""

        raw = self.orchestrator.classify(parse_prompt)
        start, end = raw.find("{"), raw.rfind("}") + 1
        parsed = json.loads(raw[start:end])
        return parsed

    # ── STAGE 2: Route ───────────────────────────────────────────────────────

    def route(self, job: dict) -> str:
        """
        Determine which specialist worker handles this job type.
        Returns a worker_type string that _call_worker() will dispatch on.
        Pure logic — no API calls.
        """
        asset_type = job.get("asset_type", "")
        video_types = {"video-effect"}
        image_types = {
            "thumbnail", "hero-background", "podcast-cover", "podcast-episode-art",
            "enamel-pin-mockup", "sticker-sheet", "glasshouse-case-file",
            "newsletter-header", "blog-header", "arcade-cabinet-art",
        }
        crop_types = {"social-square", "social-story", "social-landscape"}

        if asset_type in image_types:
            return "image"
        elif asset_type in video_types:
            return "video"
        elif asset_type in crop_types:
            return "crop"
        else:
            return "image"   # safe default

    # ── STAGE 3: Dispatch via _call_worker() ─────────────────────────────────

    def _call_worker(self, worker_type: str, payload) -> object:
        """
        Thin dispatcher. Routes to the correct specialist worker and returns
        its raw result. The dispatcher never reasons about the payload itself.

        worker_type values:
            'image'    → ComfyUI → HF → DALL-E 3 waterfall
            'caption'  → CodexWorker (structured JSON text)
            'vision'   → GeminiVisionWorker.analyze()
            'qc'       → GeminiVisionWorker.qc_check()
            'research' → PerplexityWorker.search()
            'video'    → ComfyUI AnimateDiff → Runway → FFmpeg
            'crop'     → PIL crop (no AI)

        payload:
            'image'/'video'/'crop': tuple (job, prompt, brief)
            'caption': str prompt
            'vision': tuple (image_path, prompt_str)
            'qc': tuple (image_path, job_dict)
            'research': str query
        """
        if worker_type == "image":
            job, prompt, brief = payload
            return self._image_waterfall(job, prompt, brief)

        elif worker_type == "caption":
            return self.codex.complete(payload)

        elif worker_type == "vision":
            image_path, prompt = payload
            return self.gemini.analyze(image_path, prompt)

        elif worker_type == "qc":
            image_path, job = payload
            return self.gemini.qc_check(image_path, job)

        elif worker_type == "research":
            return self.perplexity.search(payload)

        elif worker_type == "video":
            job, prompt, brief = payload
            return self._video_waterfall(job, prompt)

        elif worker_type == "crop":
            job, primary_path = payload
            return generate_social_crops(primary_path, str(RAW_DIR))

        else:
            raise ValueError(f"[Dispatcher] Unknown worker_type: {worker_type!r}")

    def _image_waterfall(self, job: dict, prompt: str, brief: dict) -> list[str]:
        """ComfyUI → HF → DALL-E 3. Returns list of saved output paths."""
        waterfall = WATERFALL_CONFIG.get(job["asset_type"], [])
        n_variants = job.get("ab_variants", 1)
        output_paths = []

        for attempt in waterfall:
            provider = attempt["provider"]
            try:
                if provider == "comfyui":
                    if not self.comfyui.is_available():
                        print("[WATERFALL] ComfyUI unavailable — next provider")
                        continue
                    workflow_path = str(WORKFLOWS_DIR / attempt["workflow"].split("/")[-1])
                    seed = int(time.time()) % (2**32)
                    for vi in range(n_variants):
                        images = self.comfyui.run_workflow(
                            workflow_path,
                            overrides={
                                "6": {"text": prompt},
                                "3": {"seed": seed + vi * 1000},
                                "5": {"width": job["dimensions"]["width"],
                                      "height": job["dimensions"]["height"]}
                            }
                        )
                        if images:
                            output_paths.append(self._save_raw(job, images[0], vi + 1))
                    if output_paths:
                        return output_paths

                elif provider == "hf":
                    for vi in range(n_variants):
                        img_bytes = self.hf.generate(prompt, model=attempt.get("model"))
                        output_paths.append(self._save_raw(job, img_bytes, vi + 1))
                    if output_paths:
                        return output_paths

                elif provider == "dalle3":
                    dalle_prompt = f"{prompt}, {brief.get('dalle3_style_suffix', '')}"
                    for vi in range(n_variants):
                        img_bytes = self.dalle.generate(
                            dalle_prompt,
                            attempt.get("size", "1792x1024"),
                            attempt.get("quality", "hd")
                        )
                        output_paths.append(self._save_raw(job, img_bytes, vi + 1))
                    if output_paths:
                        return output_paths

            except Exception as e:
                print(f"[WATERFALL] Provider {provider} failed: {e}")
                continue

        return output_paths   # May be empty if all providers failed

    def _video_waterfall(self, job: dict, prompt: str) -> list[str]:
        """AnimateDiff → Runway → FFmpeg. Stub — returns empty list if no provider."""
        waterfall = WATERFALL_CONFIG.get("video-effect", [])
        output_paths = []
        for attempt in waterfall:
            provider = attempt["provider"]
            try:
                if provider == "comfyui-animatediff":
                    if not self.comfyui.is_available():
                        continue
                    workflow_path = str(WORKFLOWS_DIR / "animatediff.json")
                    images = self.comfyui.run_workflow(
                        workflow_path,
                        overrides={"6": {"text": prompt}},
                        timeout=300
                    )
                    for i, img in enumerate(images):
                        output_paths.append(self._save_raw(job, img, i + 1))
                    if output_paths:
                        return output_paths
                elif provider == "ffmpeg-static":
                    # Local FFmpeg fallback — apply overlay to existing asset
                    primary = job.get("source_material", {}).get("primary_asset_path", "")
                    if primary:
                        import subprocess
                        out = str(RAW_DIR / f"video-effect-ffmpeg-{job['job_id']}.mp4")
                        subprocess.run([
                            "ffmpeg", "-y", "-loop", "1", "-i", primary,
                            "-vf", "fade=t=in:st=0:d=1", "-t", "5", out
                        ], check=True, capture_output=True)
                        output_paths.append(out)
                        return output_paths
            except Exception as e:
                print(f"[WATERFALL] Video provider {provider} failed: {e}")
                continue
        return output_paths

    # ── STAGE 4: Collect ─────────────────────────────────────────────────────

    def collect(self, job: dict, output_paths: list[str]) -> list[dict]:
        """
        Run QA on each output path via the vision worker.
        Returns list of QC result dicts. Does NOT move files — that is store()'s job.
        """
        results = []
        for path in output_paths:
            qc = run_automated_qc(path, job)
            gemini_result = self._call_worker("qc", (path, job))
            results.append({
                "path": path,
                "auto_qc": qc,
                "gemini_qc": gemini_result,
                "passed": qc["passed"] and gemini_result.get("gemini_passed", False),
            })
        return results

    # ── STAGE 5: Store ───────────────────────────────────────────────────────

    def store(self, job: dict, qc_results: list[dict], provider_used: str,
              model_used: str, prompt: str) -> dict:
        """
        Move passing assets to pending-review, write JSONL receipt.
        Returns the final receipt dict.
        """
        passed_paths = [r["path"] for r in qc_results if r["passed"]]
        failed_paths = [r["path"] for r in qc_results if not r["passed"]]

        for path in failed_paths:
            score = next((r["gemini_qc"].get("overall_score") for r in qc_results if r["path"] == path), "?")
            suggestion = next((r["gemini_qc"].get("improvement_suggestion") for r in qc_results if r["path"] == path), "")
            print(f"[QC FAIL] {path}: score={score}/10 — {suggestion}")

        review_paths = []
        for path in passed_paths:
            review_paths.append(self._move_to_review(path, job))
            score = next((r["gemini_qc"].get("overall_score") for r in qc_results if r["path"] == path), "?")
            self._send_telegram(
                f"✅ Asset ready for review: {job['job_id']}\n"
                f"Provider: {provider_used} | Score: {score}/10"
            )

        receipt = {
            "job_id":        job["job_id"],
            "output_paths":  review_paths,
            "failed_paths":  failed_paths,
            "provider_used": provider_used,
            "model_used":    model_used,
            "prompt":        prompt,
            "status":        "pending-review" if review_paths else "failed",
            "completed_at":  datetime.utcnow().isoformat() + "Z",
        }

        with open(RECEIPTS_LOG, "a") as f:
            f.write(json.dumps(receipt) + "\n")

        self.mark_complete(job["job_id"], str(review_paths[0]) if review_paths else "")
        return receipt

    # ── Orchestration Run Loop ───────────────────────────────────────────────

    def dispatch_job(self, job: dict) -> dict:
        """
        Full pipeline for one job: route → dispatch → collect → store.
        Entry point called by run() or directly by Hermes.
        """
        brief = self.load_brief(job["aesthetic_system"])
        prompt = build_prompt(job, brief)
        worker_type = self.route(job)

        if self.dry_run:
            print(f"[DRY-RUN] {job['job_id']} → worker={worker_type} prompt={prompt[:80]}...")
            return {"job_id": job["job_id"], "status": "dry-run"}

        self.mark_in_progress(job["job_id"])

        # Dispatch to specialist worker
        if worker_type == "crop":
            primary = job.get("source_material", {}).get("primary_asset_path", "")
            output_paths = list(self._call_worker("crop", (job, primary)).values())
            provider_used, model_used = "pil-crop", "PIL"
        else:
            output_paths = self._call_worker(worker_type, (job, prompt, brief))
            provider_used = WATERFALL_CONFIG.get(job["asset_type"], [{}])[0].get("provider", "unknown")
            model_used    = WATERFALL_CONFIG.get(job["asset_type"], [{}])[0].get("model", "unknown")

        if not output_paths:
            self._send_telegram(f"⚠️ Asset generation FAILED: {job['job_id']}")
            return {"job_id": job["job_id"], "status": "failed"}

        # Collect QA results, then store
        qc_results = self.collect(job, output_paths)
        return self.store(job, qc_results, provider_used, model_used, prompt)

    def run(self, job_id: str = None) -> None:
        """
        Main run loop. Processes all pending jobs (or a specific one).
        Called by Hermes, cron, or CLI.
        """
        jobs = self.read_pending_jobs()
        if job_id:
            jobs = [j for j in jobs if j["job_id"] == job_id]
        if not jobs:
            print("[DISPATCHER] No pending jobs.")
            return
        print(f"[DISPATCHER] Processing {len(jobs)} job(s)...")
        for job in jobs:
            print(f"[DISPATCHER] → {job['job_id']} ({job['asset_type']}, {job['priority']})")
            receipt = self.dispatch_job(job)
            print(f"[DISPATCHER] ← {job['job_id']}: {receipt.get('status')}")
        print("[DISPATCHER] Done.")

    # ── Queue Helpers ────────────────────────────────────────────────────────

    def load_brief(self, aesthetic_system: str) -> dict:
        brief_path = BRIEFS_DIR / f"{aesthetic_system}.brief.json"
        return json.loads(brief_path.read_text())

    def read_pending_jobs(self) -> list[dict]:
        pending_path = QUEUE_DIR / "pending.jsonl"
        if not pending_path.exists():
            return []
        jobs = []
        with open(pending_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    jobs.append(json.loads(line))
        return sorted(jobs, key=lambda j: (
            0 if j.get("priority") == "high" else
            1 if j.get("priority") == "normal" else 2
        ))

    def mark_in_progress(self, job_id: str) -> None:
        self._move_job(job_id, "pending.jsonl", "in-progress.jsonl", "in-progress")

    def mark_complete(self, job_id: str, output_path: str) -> None:
        self._move_job(job_id, "in-progress.jsonl", "completed.jsonl", "completed",
                       extra={"output_path": output_path})

    def _move_job(self, job_id: str, from_file: str, to_file: str,
                  new_status: str, extra: dict = None) -> None:
        from_path = QUEUE_DIR / from_file
        to_path   = QUEUE_DIR / to_file
        jobs = []
        target_job = None
        if not from_path.exists():
            return
        with open(from_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                j = json.loads(line)
                if j["job_id"] == job_id:
                    target_job = j
                else:
                    jobs.append(json.dumps(j))
        if target_job:
            target_job["status"] = new_status
            if extra:
                target_job.update(extra)
            with open(to_path, "a") as f:
                f.write(json.dumps(target_job) + "\n")
        with open(from_path, "w") as f:
            f.write("\n".join(jobs))
            if jobs:
                f.write("\n")

    def _save_raw(self, job: dict, img_bytes: bytes, variant_idx: int) -> str:
        date_str  = datetime.now().strftime("%Y%m%d")
        ep        = job.get("episode_id") or job.get("page_slug") or "misc"
        filename  = f"{job['asset_type']}-{ep}-v{variant_idx}-{date_str}.png"
        out_path  = RAW_DIR / filename
        img       = Image.open(io.BytesIO(img_bytes))
        target_w  = job["dimensions"]["width"]
        target_h  = job["dimensions"]["height"]
        if img.size != (target_w, target_h):
            img = img.resize((target_w, target_h), Image.LANCZOS)
        img.save(str(out_path), "PNG")
        return str(out_path)

    def _move_to_review(self, raw_path: str, job: dict) -> str:
        import shutil
        review_path = REVIEW_DIR / Path(raw_path).name
        shutil.move(raw_path, review_path)
        return str(review_path)

    def _send_telegram(self, message: str) -> None:
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            print(f"[TELEGRAM] (not configured) {message}")
            return
        try:
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
                json={"chat_id": TELEGRAM_CHAT_ID, "text": message},
                timeout=5
            )
        except Exception:
            pass   # Non-blocking


# ─── CLI ENTRY POINT ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LDI Asset Dispatcher")
    parser.add_argument("--job-id", help="Process a specific job by ID")
    parser.add_argument("--dry-run", action="store_true", help="Validate without generating")
    args = parser.parse_args()

    dispatcher = LDIAssetDispatcher(dry_run=args.dry_run)
    dispatcher.run(job_id=args.job_id)
```


---

## 12. STYLECLONEPIPELINE — LDI INTEGRATION

The `StyleClonePipeline` from the research doc is adapted here as a first-class LDI tool with two operating modes:

1. **LDI-seeded mode** — runs without analyzing `lithium-dreams.com` every time; starts from the pre-loaded canonical brief
2. **Competitor mode** — `point_at_competitor(url)` analyzes a competitor's site, extracts what's working, then re-applies the findings through the LDI aesthetic filter

### Full Implementation

```python
#!/usr/bin/env python3
"""
StyleClonePipeline — LDI Integration (AS-0001)
Two modes:
  1. ldi_refresh: Analyze lithium-dreams.com itself to keep the brief current
  2. competitor: Analyze competitor URL, extract what works, adapt to LDI aesthetic

Output: style_delta.json showing what was borrowed and how it was adapted.
"""

import os, json, base64, time
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
from colorthief import ColorThief
from google import genai
# anthropic not imported — Claude returns June 30; NemotronOrchestrator used instead
from dispatcher import NemotronOrchestrator

BRIEFS_DIR   = Path("/Volumes/The Crossroads/ldi-assets/briefs")
ANALYSIS_DIR = Path("/Volumes/The Crossroads/ldi-assets/style-analysis")
ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)


class StyleClonePipeline:
    """
    LDI-integrated style analysis and adaptation pipeline.
    """

    def __init__(self, comfyui_server: str = "192.168.4.x:8188"):
        self.comfyui_server  = comfyui_server
        self.gemini_client   = genai.Client()
        self.orchestrator    = NemotronOrchestrator()   # Nemotron → GPT-4o → Ollama waterfall
        # Claude returns June 30 — will become primary for synthesize_adaptation then
        
        # Pre-load LDI canonical briefs
        self.ldi_briefs = {
            "attraction-dark":  json.loads((BRIEFS_DIR / "attraction-dark.brief.json").read_text()),
            "glasshouse-light": json.loads((BRIEFS_DIR / "glasshouse-light.brief.json").read_text()),
        }

    # ── STAGE 1: Screenshot Capture ──────────────────────────────────────────

    def capture_site(self, url: str, output_dir: str) -> dict:
        """Capture full-page screenshot + extract CSS computed values."""
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(url, wait_until="networkidle", timeout=30000)
            
            screenshot_path = str(Path(output_dir) / "screenshot.png")
            page.screenshot(path=screenshot_path, full_page=False)
            
            css_data = page.evaluate("""() => {
                const computed = window.getComputedStyle(document.body);
                const root = window.getComputedStyle(document.documentElement);
                const cssVars = {};
                for (const p of root) {
                    if (p.startsWith('--')) cssVars[p] = root.getPropertyValue(p).trim();
                }
                const firstH1 = document.querySelector('h1, h2, .title');
                const firstAccent = document.querySelector('a, button, .btn');
                return {
                    bg: computed.backgroundColor,
                    text: computed.color,
                    fontFamily: computed.fontFamily,
                    h1Font: firstH1 ? getComputedStyle(firstH1).fontFamily : null,
                    accentColor: firstAccent ? getComputedStyle(firstAccent).color : null,
                    cssVars
                };
            }""")
            
            browser.close()
        
        css_data["screenshot_path"] = screenshot_path
        css_data["url"] = url
        return css_data

    # ── STAGE 2: Vision Model Analysis ───────────────────────────────────────

    def analyze_visual_language(self, screenshot_path: str, css_data: dict) -> dict:
        """Gemini Vision analysis of the captured screenshot."""
        with open(screenshot_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode("utf-8")
        
        css_context = (
            f"Background: {css_data.get('bg')} | "
            f"Text: {css_data.get('text')} | "
            f"Font: {css_data.get('fontFamily', '')[:60]} | "
            f"Accent: {css_data.get('accentColor')}"
        )
        
        response = self.gemini_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[{
                "role": "user",
                "parts": [
                    {"text": f"""
Analyze this website screenshot. CSS measurements: {css_context}

Produce a style brief as JSON:
{{
  "color_palette": {{
    "primary_bg": "#hex", "secondary_bg": "#hex",
    "primary_text": "#hex", "accent_1": "#hex", "accent_2": "#hex"
  }},
  "typography": {{
    "heading_font": "name", "body_font": "name",
    "weight": "regular|medium|bold", "tracking": "tight|normal|wide", "case": "upper|mixed"
  }},
  "visual_mood": {{
    "adjectives": ["dark", "minimal"],
    "genre_aesthetic": "paranormal noir | corporate | editorial",
    "contrast": "high|medium|low",
    "lighting": "neon|daylight|candlelight|harsh"
  }},
  "what_works": ["High contrast thumbnails with bold text", "Consistent color accent on key CTA"],
  "sdxl_prompt": "150-word prompt for an asset matching this aesthetic",
  "negative_prompt": "50-word negative prompt"
}}
                    """},
                    {"inline_data": {"mime_type": "image/png", "data": img_b64}}
                ]
            }]
        )
        
        text = response.text
        start, end = text.find("{"), text.rfind("}") + 1
        return json.loads(text[start:end])

    # ── STAGE 3: LDI Adaptation (Nemotron; Claude returns June 30) ─────────────

    def synthesize_adaptation(self, competitor_analysis: dict, target_aesthetic: str) -> dict:
        """
        Given a competitor's style analysis, determine what to borrow and how
        to re-express it through the LDI aesthetic system.

        Uses NemotronOrchestrator (OpenRouter free → GPT-4o → Ollama) for synthesis.
        Claude will replace this call after June 30 for richer creative direction.

        Returns style_delta.json structure.
        """
        ldi_brief = self.ldi_briefs[target_aesthetic]

        synthesis_prompt = f"""You are the creative director for Lithium Dreams Industries (LDI).

I analyzed a competitor's website and extracted this style data:
{json.dumps(competitor_analysis, indent=2)}

LDI's canonical style brief for '{target_aesthetic}':
{json.dumps(ldi_brief, indent=2)[:1500]}

Your task: identify what WORKS about the competitor's approach that we should learn from
(composition strategies, text treatment, contrast techniques, visual hierarchy),
then describe how to re-apply those lessons through LDI's own visual system.

Do NOT suggest copying their colors or fonts. Extract the PRINCIPLES, apply to LDI's palette.

Return ONLY valid JSON:
{{
  "competitor_url": "{competitor_analysis.get("url", "unknown")}",
  "analyzed_at": "{datetime.utcnow().isoformat()}Z",
  "what_works_in_competitor": [
    "High contrast headline + silhouette subject = strong CTR signal",
    "Bottom-third text placement with generous negative space"
  ],
  "how_to_adapt_to_ldi": [
    "Apply same bottom-third text placement to LDI thumbnails using Bebas Neue",
    "Use subject silhouette against teal glow background instead of their yellow"
  ],
  "comfyui_prompt_modifications": "Add these modifiers to LDI base prompt...",
  "what_not_to_copy": ["Their sans-serif font choice conflicts with LDI mono identity"],
  "ldi_prompt_delta": "a suggested modification to the LDI base ComfyUI prompt incorporating learnings"
}}"""

        print("[StyleClone] Synthesizing LDI adaptation via Nemotron (Claude returns June 30)...")
        raw = self.orchestrator.classify(synthesis_prompt, max_tokens=2000)
        start, end = raw.find("{"), raw.rfind("}") + 1
        return json.loads(raw[start:end])

    # ── PUBLIC API ────────────────────────────────────────────────────────────

    def point_at_competitor(self, url: str, target_aesthetic: str = "attraction-dark") -> dict:
        """
        Analyze a competitor's site and produce a style_delta.json showing
        what was borrowed and how it maps to LDI's visual language.
        
        Usage:
            pipeline = StyleClonePipeline()
            delta = pipeline.point_at_competitor("https://somecompetitor.com")
            # delta["ldi_prompt_delta"] → modification to add to next generation prompt
        """
        slug = url.replace("https://", "").replace("/", "-")[:40]
        output_dir = str(ANALYSIS_DIR / f"competitor-{slug}-{datetime.now().strftime('%Y%m%d')}")
        
        print(f"[StyleClone] Capturing {url}...")
        site_data = self.capture_site(url, output_dir)
        
        print("[StyleClone] Analyzing with Gemini Vision...")
        visual_analysis = self.analyze_visual_language(site_data["screenshot_path"], site_data)
        visual_analysis["url"] = url
        
        print("[StyleClone] Synthesizing LDI adaptation via Nemotron (Claude returns June 30)...")
        style_delta = self.synthesize_adaptation(visual_analysis, target_aesthetic)
        
        # Save outputs
        delta_path = Path(output_dir) / "style_delta.json"
        delta_path.write_text(json.dumps(style_delta, indent=2))
        
        analysis_path = Path(output_dir) / "competitor_analysis.json"
        analysis_path.write_text(json.dumps(visual_analysis, indent=2))
        
        print(f"[StyleClone] style_delta.json saved to {delta_path}")
        return style_delta

    def ldi_refresh(self, url: str = "https://lithium-dreams.com") -> dict:
        """
        Re-analyze lithium-dreams.com itself to verify the canonical brief
        matches the live site. Returns a diff if anything has drifted.
        """
        output_dir = str(ANALYSIS_DIR / f"ldi-self-{datetime.now().strftime('%Y%m%d')}")
        
        site_data = self.capture_site(url, output_dir)
        live_analysis = self.analyze_visual_language(site_data["screenshot_path"], site_data)
        
        canonical = self.ldi_briefs["attraction-dark"]["color_palette"]
        live_colors = live_analysis.get("color_palette", {})
        
        drift = {}
        for key, canonical_val in canonical.items():
            live_val = live_colors.get(key)
            if live_val and live_val.lower() != canonical_val.lower():
                drift[key] = {"canonical": canonical_val, "live": live_val}
        
        result = {
            "analyzed_at": datetime.utcnow().isoformat() + "Z",
            "url": url,
            "drift_detected": bool(drift),
            "drift": drift,
            "live_analysis": live_analysis
        }
        
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        (Path(output_dir) / "ldi_refresh.json").write_text(json.dumps(result, indent=2))
        
        if drift:
            print(f"[StyleClone] ⚠️ Drift detected in live site vs canonical brief: {list(drift.keys())}")
        else:
            print("[StyleClone] ✅ Live site matches canonical brief.")
        
        return result


# ─── USAGE ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    pipeline = StyleClonePipeline()
    
    # Analyze a competitor thumbnail channel
    # delta = pipeline.point_at_competitor("https://www.youtube.com/@unsolved-mysteries")
    # print("Learnings:", delta["what_works_in_competitor"])
    # print("Adaptation:", delta["how_to_adapt_to_ldi"])
    
    # Verify LDI's own site hasn't drifted
    # pipeline.ldi_refresh()
```

---

## 13. HERMES INTEGRATION

The asset pipeline is exposed to Hermes via two skills and one cron job.

### Skill: `asset-generate`

Hermes parses a natural language request and dispatches a job.

```python
# /Volumes/The Crossroads/hermes/skills/asset_generate.py
"""
Hermes Skill: asset-generate
Accepts: natural language request like "generate thumbnail for EP03 about the Flatwoods Monster"
Parses: episode, asset type, aesthetic, any notes via NemotronOrchestrator
Dispatches: writes to job queue and triggers dispatcher

Text parsing uses NemotronOrchestrator (OpenRouter free tier → GPT-4o → Ollama).
Claude API returns June 30 — will become primary for complex brief synthesis then.
"""

import os, re, json
from pathlib import Path
from datetime import datetime

# NemotronOrchestrator lives in dispatcher.py — it handles the text model waterfall
from dispatcher import LDIAssetDispatcher, NemotronOrchestrator, enqueue_job, WATERFALL_CONFIG

SKILL_NAME        = "asset-generate"
SKILL_DESCRIPTION = "Generate an LDI visual asset from a natural language description"

PARSE_PROMPT = """
You are parsing a natural language asset generation request for Lithium Dreams Industries.

Request: "{request}"

Extract and return ONLY valid JSON (no markdown, no preamble):
{{
  "asset_type": "thumbnail | hero-background | podcast-cover | social-square | social-story | enamel-pin-mockup | newsletter-header | glasshouse-case-file | arcade-cabinet-art | blog-header",
  "episode_id": "EP01 | EP02 | null",
  "page_slug": "museum | arcade | fortune | chapel | workshop | cathedral | null",
  "title_text": "extracted or inferred title text",
  "aesthetic_system": "attraction-dark | glasshouse-light",
  "channel": "warden | ghost | root | null",
  "priority": "high | normal | low",
  "notes": "any specific visual notes from the request",
  "ab_variants": 1,
  "dimensions": {{"width": 1280, "height": 720}}
}}

Rules:
- paranormal/LDI rooms/YouTube → attraction-dark; client work/Glasshouse → glasshouse-light
- If episode mentioned → asset_type=thumbnail unless stated otherwise
- thumbnail: 1280x720; hero-background: 2880x1800; podcast-cover: 3000x3000
"""


def run(request: str, hermes_context: dict = None) -> dict:
    """
    Entry point called by Hermes agent.
    Uses NemotronOrchestrator for request parsing (not Claude — returns June 30).
    Returns: {"success": bool, "job_id": str, "message": str}
    """
    orchestrator = NemotronOrchestrator()
    raw = orchestrator.classify(PARSE_PROMPT.format(request=request), max_tokens=500)

    start, end = raw.find("{"), raw.rfind("}") + 1
    parsed = json.loads(raw[start:end])

    job_id = enqueue_job(
        asset_type       = parsed["asset_type"],
        aesthetic_system = parsed["aesthetic_system"],
        title_text       = parsed.get("title_text", ""),
        episode_id       = parsed.get("episode_id"),
        page_slug        = parsed.get("page_slug"),
        channel          = parsed.get("channel", "warden"),
        priority         = parsed.get("priority", "normal"),
        notes            = parsed.get("notes", ""),
        ab_variants      = parsed.get("ab_variants", 1),
    )

    # Fire dispatcher immediately for high-priority jobs
    if parsed.get("priority") == "high":
        dispatcher = LDIAssetDispatcher()
        dispatcher.run(job_id=job_id)
        return {
            "success": True,
            "job_id": job_id,
            "message": f"High-priority job {job_id} dispatched immediately. Check pending-review when done.",
        }

    return {
        "success": True,
        "job_id": job_id,
        "message": f"Job {job_id} queued. Will process on next dispatcher run.",
    }
```

### Skill: `asset-review`

Presents pending review items to John.

```python
# /Volumes/The Crossroads/hermes/skills/asset_review.py
"""
Hermes Skill: asset-review
Shows John what's in pending-review, lets him approve/reject via Telegram reply.
"""

from pathlib import Path
import json, shutil
from datetime import datetime

REVIEW_DIR   = Path("/Volumes/The Crossroads/ldi-assets/pending-review")
APPROVED_DIR = Path("/Volumes/The Crossroads/ldi-assets/approved")
RECEIPTS_LOG = Path("/Volumes/The Crossroads/ldi-assets/logs/receipts.jsonl")

SKILL_NAME = "asset-review"

def run(action: str = "list", job_id: str = None, decision: str = None) -> dict:
    """
    action="list"    → return count and summary of pending review items
    action="approve" → move job_id from review to approved, write receipt
    action="reject"  → move to rejected, add to requeue with notes
    """
    pending = list(REVIEW_DIR.glob("*.png")) + list(REVIEW_DIR.glob("*.webp"))
    
    if action == "list":
        return {
            "pending_count": len(pending),
            "items": [p.name for p in pending[:10]],
            "message": f"{len(pending)} asset(s) awaiting review."
        }
    
    if action == "approve" and job_id:
        matches = [p for p in pending if job_id in p.name]
        if not matches:
            return {"success": False, "message": f"No pending asset found for {job_id}"}
        
        for asset_path in matches:
            # Determine destination subdirectory from filename
            asset_type = asset_path.name.split("-")[0]
            dest_dir = APPROVED_DIR / f"{asset_type}s"
            dest_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(asset_path), str(dest_dir / asset_path.name))
        
        with open(RECEIPTS_LOG, "a") as f:
            f.write(json.dumps({
                "job_id": job_id,
                "action": "approved",
                "approved_at": datetime.utcnow().isoformat() + "Z",
                "approved_by": "john"
            }) + "\n")
        
        return {"success": True, "message": f"Approved {len(matches)} asset(s) for {job_id}"}
    
    if action == "reject" and job_id:
        # Assets stay in review dir but are tagged for regeneration
        with open(RECEIPTS_LOG, "a") as f:
            f.write(json.dumps({
                "job_id": job_id,
                "action": "rejected",
                "rejected_at": datetime.utcnow().isoformat() + "Z",
                "notes": decision or "No notes"
            }) + "\n")
        return {"success": True, "message": f"Marked {job_id} as rejected. Will requeue with updated prompt."}
    
    return {"success": False, "message": "Unknown action"}
```

### Hermes Cron: Daily Asset Digest

Hermes sends John a daily Telegram summary of what was generated, what's pending review, and what published.

```python
# /Volumes/The Crossroads/hermes/crons/asset_digest.py
"""
Hermes Cron: Daily Asset Digest
Runs at 8:00 AM CDT via launchd on Mac Mini.
Sends Telegram message summarizing the asset queue state.
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
import requests

RECEIPTS_LOG = Path("/Volumes/The Crossroads/ldi-assets/logs/receipts.jsonl")
REVIEW_DIR   = Path("/Volumes/The Crossroads/ldi-assets/pending-review")
QUEUE_DIR    = Path("/Volumes/The Crossroads/ldi-assets/queue")

def run():
    yesterday = (datetime.utcnow() - timedelta(days=1)).date()
    
    # Count recent receipts
    recent_jobs = []
    if RECEIPTS_LOG.exists():
        with open(RECEIPTS_LOG) as f:
            for line in f:
                r = json.loads(line.strip())
                ts = r.get("completed_at", "")[:10]
                if ts == str(yesterday):
                    recent_jobs.append(r)
    
    generated  = [j for j in recent_jobs if j.get("status") != "failed"]
    failed     = [j for j in recent_jobs if j.get("status") == "failed"]
    pending_rv = len(list(REVIEW_DIR.glob("*.png")))
    
    pending_q = 0
    pending_path = QUEUE_DIR / "pending.jsonl"
    if pending_path.exists():
        with open(pending_path) as f:
            pending_q = sum(1 for line in f if line.strip())
    
    msg = (
        f"🎨 LDI ASSET DIGEST — {yesterday}\n"
        f"Generated yesterday: {len(generated)}\n"
        f"Failed: {len(failed)}\n"
        f"Pending your review: {pending_rv}\n"
        f"Jobs in queue: {pending_q}\n"
    )
    
    if pending_rv > 0:
        msg += "\nReply 'review' to see what's waiting."
    
    import os
    requests.post(
        f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}/sendMessage",
        json={"chat_id": os.environ["TELEGRAM_CHAT_ID"], "text": msg}
    )

if __name__ == "__main__":
    run()
```

### Telegram Dispatch Flow

```
John: "generate thumbnail for EP03 — the Flatwoods Monster episode, warden channel"
    ↓
Hermes receives via Telegram webhook
    ↓
Routes to asset-generate skill
    ↓
NemotronOrchestrator parses: asset_type=thumbnail, episode_id=EP03, channel=warden, priority=normal
  (OpenRouter Nemotron free → GPT-4o → Ollama waterfall; Claude returns June 30)
    ↓
enqueue_job() writes to pending.jsonl
    ↓
Hermes: "Job thumb-EP03-20260627143200 queued. I'll let you know when it's ready to review."
    ↓
Dispatcher runs:
  _call_worker('image', ...) → ComfyUI generates on Victus
  _call_worker('qc', ...) → Gemini 2.0 Flash evaluates output
    ↓
Hermes: "✅ Thumbnail for EP03 ready for review. Score: 8.2/10"
    ↓
John: "approve"
    ↓
asset-review skill moves to /approved/thumbnails/ep03/
    ↓
Hermes: "Approved. Upload to YouTube manually or say 'deploy EP03 thumbnail' to run the API."
```

---

## 14. LDITHUMBNAILGENERATOR — ENHANCED

The research `LDIThumbnailGenerator` class, enhanced with: all 3 Pantheon accent colors, episode-specific overlay templates, A/B variant generation, and YouTube upload stub.

```python
"""
LDIThumbnailGenerator — Enhanced (AS-0001)
PIL/Pillow-based thumbnail compositor for the LDI Paranormal Pantheon series.

Handles:
  - All 3 channel accent colors (Warden teal, Ghost blue, Bob/Root amber)
  - Episode-specific overlay templates
  - A/B variant generation (2 variants: different text placement)
  - CRT/grain treatment application
  - YouTube upload stub
  - ComfyUI and DALL-E 3 base image generation
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import requests, io, subprocess
from pathlib import Path
from typing import Literal

# ─── BRAND COLORS (from VD-0001) ─────────────────────────────────────────────

CHANNEL_COLORS = {
    "warden": {
        "accent":      (0, 229, 204),    # --ldi-teal         #00e5cc
        "accent_dim":  (0, 160, 144),    # --ldi-teal-dim
        "name":        "WARDEN",
    },
    "ghost": {
        "accent":      (77, 184, 212),   # --ldi-ghost-blue   #4DB8D4 (approx)
        "accent_dim":  (40, 120, 150),
        "name":        "GHOST",
    },
    "root": {                            # Bob / Root channel
        "accent":      (240, 160, 32),   # --ldi-amber-bright #f0a020
        "accent_dim":  (212, 130, 10),   # --ldi-amber
        "name":        "ROOT",
    },
}

VOID_BLACK    = (10, 9, 7)             # #0a0907
TEXT_PRIMARY  = (232, 220, 192)        # #e8dcc0
THUMB_W, THUMB_H = 1280, 720


# ─── EPISODE OVERLAY TEMPLATES ───────────────────────────────────────────────

EPISODE_TEMPLATES = {
    "EP01": {
        "name":        "Point Pleasant",
        "silhouette":  "bridge-silhouette",          # SVG/PNG mask asset
        "accent":      "warden",
        "text_position": "bottom-left",
        "fog_density": 0.4,
        "prompt_hint": "point pleasant bridge silhouette at night, Ohio River, amber lights",
    },
    "EP02": {
        "name":        "Skinwalker Ranch",
        "silhouette":  "desert-ridge",
        "accent":      "root",
        "text_position": "bottom-right",
        "fog_density": 0.2,
        "prompt_hint": "Utah desert mesa at night, starfield, infrared security camera feel",
    },
    "EP03": {
        "name":        "Flatwoods Monster",
        "silhouette":  "forest-treeline",
        "accent":      "warden",
        "text_position": "bottom-left",
        "fog_density": 0.6,
        "prompt_hint": "West Virginia forest at night, floating red orbs through trees, fog",
    },
    # Add episodes as they're created — default template used if not listed
    "DEFAULT": {
        "accent":        "warden",
        "text_position": "bottom-left",
        "fog_density":   0.3,
        "prompt_hint":   "",
    },
}

FONT_PATHS = {
    "display": "/Volumes/The Crossroads/assets/fonts/BebasNeue-Regular.ttf",
    "mono":    "/Volumes/The Crossroads/assets/fonts/SpaceMono-Regular.ttf",
    "body":    "/Volumes/The Crossroads/assets/fonts/Inter-Regular.ttf",
}


class LDIThumbnailGenerator:
    def __init__(self, width: int = THUMB_W, height: int = THUMB_H):
        self.width  = width
        self.height = height

    # ── Base Image Generation ─────────────────────────────────────────────────

    def generate_base_image(self, prompt: str, api: str = "comfyui",
                             workflow_path: str = None) -> Image.Image:
        """Generate the base scene image. api: comfyui | dalle3 | hf"""
        
        if api == "comfyui":
            from dispatcher import ComfyUIClient
            client = ComfyUIClient()
            if not workflow_path:
                workflow_path = "/Volumes/The Crossroads/ldi-assets/workflows/thumbnail-flux.json"
            images = client.run_workflow(
                workflow_path,
                overrides={
                    "6": {"text": prompt},
                    "5": {"width": self.width, "height": self.height}
                }
            )
            return Image.open(io.BytesIO(images[0]))
        
        elif api == "dalle3":
            from openai import OpenAI
            client = OpenAI()
            dalle_prompt = f"{prompt}, YouTube thumbnail, cinematic, dramatic lighting, 16:9, paranormal documentary aesthetic"
            response = client.images.generate(
                model="dall-e-3",
                prompt=dalle_prompt,
                size="1792x1024",
                quality="hd"
            )
            img_data = requests.get(response.data[0].url).content
            return Image.open(io.BytesIO(img_data)).resize((self.width, self.height), Image.LANCZOS)
        
        elif api == "hf":
            from huggingface_hub import InferenceClient
            client = InferenceClient(api_key=__import__("os").environ["HF_TOKEN"])
            image = client.text_to_image(prompt=prompt, model="black-forest-labs/FLUX.1-dev")
            return image.resize((self.width, self.height), Image.LANCZOS)
        
        else:
            raise ValueError(f"Unknown api: {api}")

    # ── Text Overlay ──────────────────────────────────────────────────────────

    def add_text_overlay(
        self,
        base: Image.Image,
        title: str,
        subtitle: str = None,
        channel: str = "warden",
        position: Literal["bottom-left", "bottom-right", "center-bottom"] = "bottom-left"
    ) -> Image.Image:
        """Add styled text with shadow, outline, and channel accent color."""
        img  = base.copy()
        draw = ImageDraw.Draw(img)
        
        colors = CHANNEL_COLORS.get(channel, CHANNEL_COLORS["warden"])
        accent_rgb = colors["accent"]
        
        # Load fonts
        try:
            title_font  = ImageFont.truetype(FONT_PATHS["display"], 110)
            sub_font    = ImageFont.truetype(FONT_PATHS["display"], 48)
            ep_font     = ImageFont.truetype(FONT_PATHS["mono"], 22)
        except (IOError, OSError):
            title_font  = ImageFont.load_default(size=90)
            sub_font    = ImageFont.load_default(size=44)
            ep_font     = ImageFont.load_default(size=20)
        
        margin = 55
        
        # Calculate text position based on layout variant
        if position == "bottom-left":
            text_x = margin
            text_y = self.height - 240
        elif position == "bottom-right":
            # Right-align: approximate width
            bbox = draw.textbbox((0, 0), title.upper(), font=title_font)
            text_w = bbox[2] - bbox[0]
            text_x = self.width - text_w - margin
            text_y = self.height - 240
        else:  # center-bottom
            bbox = draw.textbbox((0, 0), title.upper(), font=title_font)
            text_w = bbox[2] - bbox[0]
            text_x = (self.width - text_w) // 2
            text_y = self.height - 220
        
        title_upper = title.upper()
        
        # Shadow layer
        draw.text((text_x + 5, text_y + 5), title_upper, font=title_font, fill=(0, 0, 0, 200))
        
        # Outline (4px)
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                if abs(dx) + abs(dy) >= 3:
                    draw.text((text_x + dx, text_y + dy), title_upper, 
                              font=title_font, fill=(0, 0, 0))
        
        # Main title text
        draw.text((text_x, text_y), title_upper, font=title_font, fill=TEXT_PRIMARY)
        
        # Subtitle / episode label in channel accent color
        if subtitle:
            draw.text((text_x, text_y + 118), subtitle.upper(), font=sub_font, fill=accent_rgb)
        
        return img

    # ── LDI Visual Treatment ─────────────────────────────────────────────────

    def apply_ldi_treatment(self, img: Image.Image, fog_density: float = 0.3) -> Image.Image:
        """Apply standard LDI visual post-processing."""
        
        # 1. Contrast boost
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.25)
        
        # 2. Slight saturation reduction (more cinematic)
        color_enhancer = ImageEnhance.Color(img)
        img = color_enhancer.enhance(0.88)
        
        # 3. Vignette (radial darkening toward edges)
        img_rgba = img.convert("RGBA")
        vignette = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(vignette)
        steps = 80
        for i in range(steps):
            alpha = int(i * 2.2)
            pad_x = int(i * (self.width  / (2 * steps)))
            pad_y = int(i * (self.height / (2 * steps)))
            draw.rectangle([pad_x, pad_y, self.width - pad_x, self.height - pad_y],
                           outline=(0, 0, 0, alpha))
        img = Image.alpha_composite(img_rgba, vignette).convert("RGB")
        
        # 4. Subtle grain overlay (SVG-style noise approximation using Pillow)
        if fog_density > 0:
            import numpy as np
            grain = np.random.normal(0, 8 * fog_density, (self.height, self.width, 3)).astype("int16")
            img_arr = np.array(img).astype("int16")
            img_arr = np.clip(img_arr + grain, 0, 255).astype("uint8")
            img = Image.fromarray(img_arr)
        
        return img

    # ── Border Elements ──────────────────────────────────────────────────────

    def add_border_elements(self, img: Image.Image, channel: str = "warden") -> Image.Image:
        """Add LDI corner marks and episode accent line."""
        draw   = ImageDraw.Draw(img)
        colors = CHANNEL_COLORS.get(channel, CHANNEL_COLORS["warden"])
        accent = colors["accent"]
        
        # L-shaped corner marks
        corner_size = 22
        lw = 3
        corners = [
            (18, 18),
            (self.width - 18, 18),
            (18, self.height - 18),
            (self.width - 18, self.height - 18),
        ]
        signs = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        
        for (cx, cy), (sx, sy) in zip(corners, signs):
            draw.line([(cx, cy), (cx + sx * corner_size, cy)], fill=accent, width=lw)
            draw.line([(cx, cy), (cx, cy + sy * corner_size)], fill=accent, width=lw)
        
        # Thin accent line at bottom (above text area)
        line_y = self.height - 260
        draw.line([(55, line_y), (400, line_y)], fill=accent, width=1)
        
        return img

    # ── Full Pipeline ────────────────────────────────────────────────────────

    def generate(
        self,
        title: str,
        episode_id: str = None,
        subtitle: str = None,
        prompt_override: str = None,
        channel: str = None,
        api: str = "comfyui",
        output_path: str = None,
        ab_variant: int = 1
    ) -> str:
        """
        Full pipeline: base image → text overlay → LDI treatment → border → save.
        
        ab_variant=1 → bottom-left text placement
        ab_variant=2 → bottom-right text placement (A/B test)
        """
        template = EPISODE_TEMPLATES.get(episode_id or "", EPISODE_TEMPLATES["DEFAULT"])
        
        # Channel falls back to episode template default
        if not channel:
            channel = template.get("accent", "warden")
        
        # Prompt: override > episode hint + base brief
        if prompt_override:
            prompt = prompt_override
        else:
            hint = template.get("prompt_hint", "")
            from dispatcher import LDIAssetDispatcher
            brief = json.loads(
                (Path("/Volumes/The Crossroads/ldi-assets/briefs/attraction-dark.brief.json")).read_text()
            )
            base = brief["comfyui_defaults"]["base_positive"]
            prompt = f"{hint}, {base}" if hint else base
        
        # A/B text placement
        position = "bottom-right" if ab_variant == 2 else "bottom-left"
        fog = template.get("fog_density", 0.3)
        
        # Generate
        base_img = self.generate_base_image(prompt, api=api)
        with_text = self.add_text_overlay(base_img, title, subtitle or f"Episode {episode_id or ''}", 
                                           channel=channel, position=position)
        treated   = self.apply_ldi_treatment(with_text, fog_density=fog)
        final     = self.add_border_elements(treated, channel=channel)
        
        # Save
        if not output_path:
            ep_tag = episode_id or "misc"
            output_path = f"/Volumes/The Crossroads/ldi-assets/raw/thumbnail-{ep_tag}-v{ab_variant}.png"
        
        final.save(output_path, "PNG")
        print(f"[ThumbnailGen] Saved: {output_path}")
        return output_path

    def generate_ab_pair(self, title: str, episode_id: str, api: str = "comfyui") -> tuple[str, str]:
        """Generate both A/B variants and return both output paths."""
        ep = episode_id or "misc"
        path_a = self.generate(title, episode_id=episode_id, api=api, ab_variant=1)
        path_b = self.generate(title, episode_id=episode_id, api=api, ab_variant=2)
        return path_a, path_b

    # ── YouTube Upload Stub ──────────────────────────────────────────────────

    def upload_to_youtube(self, thumbnail_path: str, video_id: str,
                           credentials_path: str = "/Volumes/The Crossroads/secrets/youtube-oauth.json") -> bool:
        """Upload thumbnail to YouTube. Returns True on success."""
        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            from googleapiclient.http import MediaFileUpload
            
            creds   = Credentials.from_authorized_user_file(credentials_path)
            youtube = build("youtube", "v3", credentials=creds)
            media   = MediaFileUpload(thumbnail_path, mimetype="image/png")
            youtube.thumbnails().set(videoId=video_id, media_body=media).execute()
            print(f"[YouTube] Thumbnail uploaded for video {video_id}")
            return True
        except Exception as e:
            print(f"[YouTube] Upload failed: {e}")
            print("[YouTube] Manual fallback: YouTube Studio → Edit → Custom Thumbnail")
            return False


# ─── CLI USAGE ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import json
    
    gen = LDIThumbnailGenerator()
    
    # Generate A/B pair for EP03
    a, b = gen.generate_ab_pair(
        title      = "The Flatwoods Monster",
        episode_id = "EP03",
        api        = "comfyui"
    )
    print(f"Variant A: {a}")
    print(f"Variant B: {b}")
```

---

## 15. IMPLEMENTATION ROADMAP

### Phase 1 — Week 1: ComfyUI Headless + Dispatcher

**Goal:** One button → thumbnail in `/pending-review/`

**Tasks:**
1. Edit `run_nvidia_gpu.bat` on the Victus: add `--listen 0.0.0.0 --disable-auto-launch`
2. Open Windows Firewall: TCP inbound rule for port 8188
3. Set static LAN IP for Victus via router DHCP reservation
4. Verify from Mac Mini: `curl http://192.168.4.x:8188/system_stats`
5. Export the FLUX.1-dev thumbnail workflow from ComfyUI UI (Settings → Dev Mode → Save API Format) → save to `/Volumes/The Crossroads/ldi-assets/workflows/thumbnail-flux.json`
6. Install required Python packages on Mac Mini:
   ```bash
   pip install websocket-client openai google-genai huggingface_hub Pillow colorthief requests
   # Note: openrouter uses the openai package — set OPENROUTER_API_KEY env var
   ```
7. Write canonical brief JSONs to `/briefs/`
8. Write first test job to `pending.jsonl` manually
9. Run `python dispatcher.py --dry-run` to validate
10. Run `python dispatcher.py` → confirm thumbnail appears in `/pending-review/`

**Exit criteria:** `python dispatcher.py` → EP01 thumbnail in pending-review, QC passed.

---

### Phase 2 — Week 2: Hermes + Command Center Integration

**Goal:** John types "generate thumbnail for EP02" in Telegram → asset appears for review

**Tasks:**
1. Copy `asset_generate.py` and `asset_review.py` skills to Hermes skill directory
2. Register skills in Hermes skill manifest
3. Configure Telegram webhook → Hermes
4. Test: send "generate thumbnail for EP02 — Skinwalker Ranch" via Telegram
5. Verify Hermes parses correctly, job enqueued, dispatcher fires
6. Wire `asset_review` to Telegram reply handler: "approve" → moves to `/approved/`
7. Build Command Center Asset Generation panel (or verify existing panel polls `/pending-review/`)
8. Test daily digest cron: run `asset_digest.py` manually, verify Telegram message

**Exit criteria:** Full Telegram round-trip works (request → queue → generate → review → approve).

---

### Phase 3 — Week 3: StyleClonePipeline + Competitor Analysis

**Goal:** "analyze [competitor URL]" → `style_delta.json` → modified prompts

**Tasks:**
1. Install Playwright on Ubuntu laptop (runs in Docker):
   ```bash
   pip install playwright && playwright install chromium
   ```
2. Test `capture_site()` against `https://lithium-dreams.com`
3. Run `ldi_refresh()` — confirm no drift vs. canonical brief
4. Run `point_at_competitor()` against 2–3 paranormal YouTube channels
5. Review `style_delta.json` outputs, validate "what_works" and "how_to_adapt" sections
6. Wire `style_delta["ldi_prompt_delta"]` as an optional modifier in the dispatcher prompt builder

**Exit criteria:** `point_at_competitor("https://...")` produces a useful `style_delta.json` in <2 minutes.

---

### Phase 4 — Week 4: Video Effects Pipeline

**Goal:** AnimateDiff generates intro loops; FFmpeg applies CRT/glitch to episode B-roll

**Tasks:**
1. ComfyUI Manager on Victus: Install `ComfyUI-AnimateDiff-Evolved` and `ComfyUI-VideoHelperSuite`
2. Download `mm_sd_v15_v2.ckpt` to `ComfyUI/custom_nodes/ComfyUI-AnimateDiff-Evolved/models/`
3. Export AnimateDiff workflow (API format) → save to `workflows/animatediff.json`
4. Test: submit AnimateDiff job via dispatcher, verify MP4 output
5. Add `apply_crt_filter()` and `apply_glitch_effect()` FFmpeg functions to a post-processing script
6. Wire Runway ML Gen4 Turbo as fallback: test one image-to-video call
7. Add `video-effect` asset type to the dispatcher's handled types

**Exit criteria:** `dispatcher.py` can generate a 5s animated loop from a thumbnail image.

---

### Phase 5 — Month 2: Full Automation on Episode Publish

**Goal:** John publishes an episode → pipeline auto-generates all associated assets

**Tasks:**
1. Create episode publish webhook (triggered by Ghost CMS publish or manual Hermes command)
2. On webhook: auto-enqueue thumbnail (A/B), social square, social story, blog header
3. After John approves thumbnail: auto-upload via YouTube Data API
4. After approval: auto-sync to R2 via rclone, auto-schedule social via Buffer
5. After deploy: Hermes sends completion summary
6. Document the complete episode asset checklist and automate its generation

**Exit criteria:** Publishing EP05 requires John to approve 4 assets and execute 0 manual uploads.

---

## 16. GAP ANALYSIS

### What Works Now (Pre-Pipeline)

| Capability | Status |
|-----------|--------|
| ComfyUI installed on Victus | ✅ Installed, local GUI works |
| FLUX.1-dev model downloaded | ✅ Confirmed |
| DreamShaper XL downloaded | ✅ Confirmed |
| VD-0001 design system documented | ✅ Complete |
| DALL-E 3 API access | ✅ OpenAI key configured |
| Gemini 2.0 Flash API | ✅ Google API key configured |
| Hermes agent running on Mac Mini | ✅ Active |
| Obsidian vault on The Crossroads | ✅ Active |
| Tailscale mesh networking | ✅ All 3 machines linked |

### What Requires Setup This Sprint

| Gap | Effort | Blocker? |
|-----|--------|----------|
| ComfyUI headless mode on Victus (`--listen 0.0.0.0`) | 15 min | YES — nothing works without this |
| Windows Firewall rule for port 8188 | 5 min | YES |
| Workflow JSON exports (thumbnail, hero, pin) | 1–2 hr per workflow | YES — need 3 workflows minimum |
| Canonical brief JSONs written | 30 min | YES |
| Python dependencies installed on Mac Mini | 20 min | YES |
| Font files on The Crossroads (`BebasNeue-Regular.ttf`, `SpaceMono-Regular.ttf`) | 10 min | YES — required for thumbnail text compositor |
| Static LAN IP for Victus | 5 min | Strongly recommended |

### What Requires Budget to Close

| Capability | Cost | When Needed |
|-----------|------|-------------|
| Runway ML Gen4 (video effects) | $15–95/mo | Phase 4 |
| Cloudflare R2 storage | ~$5–15/mo | Phase 2+ (free tier likely sufficient for year 1) |
| YouTube Data API quota upgrade | Free (but verification required) | Phase 5 |
| Buffer social scheduling | $6–18/mo | Phase 5 |
| Fourthwall store setup | Free until merch starts selling | Month 3+ |

### What Remains Manual (Intentionally)

| Task | Why Manual |
|------|-----------|
| Final thumbnail approval | John's aesthetic judgment cannot be automated |
| Episode script writing | Creative, not production |
| Enamel pin vector master production | Requires Illustrator + human art direction |
| YouTube video upload | Separate from thumbnail; handled in content workflow |
| Client deliveries (Glasshouse case files) | Client relationship requires human touch |
| Fourthwall product page setup | One-time per design, manual upload acceptable |

### Risks and Mitigations

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Victus offline (ComfyUI unavailable) | Medium | DALL-E 3 fallback in waterfall |
| DALL-E 3 rate limit or outage | Low | HF InferenceClient fallback |
| ComfyUI workflow node deprecation | Medium | Keep workflow JSON versions in git; test after ComfyUI updates |
| Gemini Vision changes API | Low | Abstract behind `gemini_ldi_check()` function; swap model in one place |
| Queue file corruption | Low | JSONL is append-only; corrupted lines are skipped by reader |
| Tailscale network partition | Low | LAN fallback for all cross-machine calls |

> **Bob's final note:** The hardest part of any pipeline is the first asset that goes wrong at 11pm on a Sunday. The waterfall exists for exactly that moment. ComfyUI is down? DALL-E 3 handles it. That rate-limited too? HF takes 2 minutes but it runs. And if everything fails, the `FAILED` queue entry goes to Telegram immediately so John knows to do it manually rather than wondering why nothing showed up. A pipeline that fails silently is worse than no pipeline.

---

*AS-0001 · Lithium Dreams Industries · Asset Generation & Curation Pipeline · Rev 1.0 · June 2026*  
*Author: Ghost/John · Vault: /Volumes/The Crossroads/ldi-docs/engineering/*  
*Depends on: VD-0001 (Visual Design System)*
