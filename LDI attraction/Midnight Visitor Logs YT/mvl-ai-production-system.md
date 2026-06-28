# MIDNIGHT VISITOR LOG
## AI-Native Frictionless Production System
### Lithium Dreams Industries · Ghost's Workshop
#### Document ID: OM-0017 · Revision 2037.1 · AUTHORIZED PERSONNEL ONLY

> *"Things too weird to explain."*
> *Ghost's annotation: "The goal is to make the weird thing happen with as little friction as possible. This document explains how."*
> *Bob's annotation, blue painter's tape: "Also I have opinions. Ghost knows."*

---

## DESIGN PHILOSOPHY

The production system should be **so frictionless that John's only job is making creative decisions.** Every step that involves retrieving, transforming, formatting, or distributing information is delegated to an agent or automated pipeline. The human's irreplaceable contribution is: creative spark, tonal judgment, and final voice.

The system runs on three layers:

```
LAYER 1: LOCAL (Thought Reliquary + HP Victus)
  ├── Ollama local LLMs (research, drafting, summarization)
  ├── ffmpeg (audio/video processing)
  ├── Whisper (transcription)
  ├── Stable Diffusion via AUTOMATIC1111 (thumbnail generation)
  └── Python scripts + shell automation

LAYER 2: CLOUD APIs (paid, per-use)
  ├── Claude API (scripting, quality review, complex reasoning)
  ├── ElevenLabs API (TTS voiceover)
  ├── OpenAI DALL-E 3 (thumbnail base images)
  ├── YouTube Data API v3 (upload, analytics, metadata)
  └── Runway ML / Kling AI (B-roll video generation, as needed)

LAYER 3: HERMES ORCHESTRATION
  ├── Task routing and agent delegation
  ├── Notification and review triggers
  ├── Episode pipeline state management
  └── Scheduled jobs (weekly analytics, keyword reports)
```

**Cost principle:** The local layer handles volume. The cloud API layer handles quality gates. Hermes handles routing. The human handles nothing that a machine can do correctly.

---

## THE FULL AGENTIC PRODUCTION LOOP

```
┌─────────────────────────────────────────────────────────────┐
│  TRIGGER: Episode Intake Form submitted                      │
└──────────────────────────┬──────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: RESEARCH (async, parallel)                        │
│  ├── 5 research tracks → workspace files                    │
│  ├── Local: Ollama (Llama 3.1) compiles research brief      │
│  └── Notify: "Research ready for review"                    │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [Human: review brief, 30 min]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: SCRIPTING                                         │
│  ├── Claude API: generate full video script draft           │
│  ├── Local Ollama: generate podcast + blog variants         │
│  └── Notify: "Script draft ready for review"                │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [Human: review + annotate, 1 hr]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 3: REVISION + FORMAT CONVERSION                      │
│  ├── Claude API: apply human revision notes                 │
│  ├── Agent: strip video cues → podcast script               │
│  ├── Agent: convert to blog dossier format                  │
│  ├── Agent: generate social copy bank                       │
│  └── Notify: "Scripts ready — trigger production?"          │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [Human: approve, 5 min]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 4: AUDIO PRODUCTION                                  │
│  ├── ElevenLabs API: generate voiceover from podcast script │
│  ├── ffmpeg: noise reduction + loudnorm (-16 LUFS)          │
│  ├── Whisper: generate transcript + captions                │
│  └── Notify: "Audio ready for review"                       │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [Human: spot-check, 15 min]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 5: VISUAL PRODUCTION                                 │
│  ├── Extract B-roll list from script stage directions       │
│  ├── Source B-roll: archive.org API + Pexels API + Pixabay  │
│  ├── Generate AI B-roll: Runway ML for establishing shots   │
│  ├── Generate 3 thumbnail variants: DALL-E 3 + Pillow       │
│  ├── Assemble video: ffmpeg sequence (audio + B-roll)       │
│  └── Notify: "Video draft ready for review"                 │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [Human: watch draft, pick thumbnail, 30 min]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 6: PUBLISH & DISTRIBUTE                              │
│  ├── YouTube Data API: schedule upload + metadata           │
│  ├── Buzzsprout API: schedule podcast publish               │
│  ├── Ghost Admin API: schedule blog post                    │
│  ├── Social copy → scheduled posts (Buffer API or manual)   │
│  └── Notify: "All content scheduled — Episode MVL-EP[###]  │
│               goes live [DATE TIME]"                         │
└──────────────────────────┬──────────────────────────────────┘
                           ↓ [7 days post-publish]
┌─────────────────────────────────────────────────────────────┐
│  STAGE 7: ANALYTICS LOOP                                    │
│  ├── YouTube Analytics API: pull 7-day performance data     │
│  ├── Generate scorecard + retention curve plot              │
│  ├── Identify learnings for next episode                    │
│  └── File report + notify: "Performance review for EP[###]" │
└─────────────────────────────────────────────────────────────┘
```

---

## LOCAL LLM SETUP (Thought Reliquary)

The Thought Reliquary (Ubuntu 24.04, local network node) handles local model inference for non-quality-critical tasks — first-pass research summaries, format conversion, social copy generation, show notes drafting.

### Ollama Installation & Models

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama service
ollama serve &

# Pull recommended models for MVL production
ollama pull llama3.1:8b           # Fast general tasks, social copy, format conversion
ollama pull mistral:7b            # Research summarization
ollama pull qwen2.5:14b           # Longer context, script first-pass (14B requires HP Victus GPU)
ollama pull llama3.2:3b           # Ultra-fast, metadata generation

# Verify running
ollama list
curl http://localhost:11434/api/tags
```

### Ollama Python Client (for Hermes integration)

```python
import ollama

def research_summarize(track_files: list[str]) -> str:
    """Compile research tracks into a brief using local LLM."""
    combined = ""
    for f in track_files:
        with open(f) as file:
            combined += file.read() + "\n\n"

    response = ollama.chat(
        model='mistral:7b',
        messages=[{
            'role': 'user',
            'content': f"""You are the research compiler for the Midnight Visitor Log,
            a paranormal/fringe history broadcast by Lithium Dreams Industries.
            Compile the following research tracks into a structured episode brief.
            Preserve all specific dates, witness names, and source URLs.
            Flag any claims marked [BOB FLAG] for human review.
            Organize by: Timeline, Witnesses, Anchor Event, Geography, Theories.

            RESEARCH TRACKS:
            {combined}"""
        }]
    )
    return response['message']['content']
```

### Task Routing — What Goes Where

| Task | Local Ollama | Claude API | Notes |
|------|-------------|-----------|-------|
| Research track compilation | ✓ | — | Mistral 7B handles well |
| First-pass script draft | — | ✓ | Claude quality required for host voice |
| Script revision | — | ✓ | Requires nuanced tone judgment |
| Podcast script conversion | ✓ | — | Mechanical transformation |
| Blog dossier conversion | ✓ | — | Template-driven |
| Show notes generation | ✓ | — | From transcript via Ollama |
| Social copy generation | ✓ | — | Llama 3.1 8B sufficient |
| Thumbnail text variants | ✓ | — | Fast generation |
| SEO metadata | ✓ | — | Template-driven |
| Analytics interpretation | — | ✓ | Nuanced pattern recognition |
| QC Ghost Review | — | ✓ | Critical quality gate |

---

## ELEVENLABS TTS SETUP (voiceover generation)

```python
import requests, json
from pathlib import Path

ELEVENLABS_API_KEY = "your_api_key"

def generate_voiceover(script_text: str, episode_num: int, voice_id: str = "pNInz6obpgDQGcFmaJgB"):
    """Generate voiceover audio from podcast script."""
    # Recommended voice: "Adam" (pNInz6obpgDQGcFmaJgB) — deep, authoritative
    # Alternative: "Josh" (TxGEqnHWrfWFTfGW9XjX) — warm, storytelling

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": script_text,
        "model_id": "eleven_multilingual_v2",  # Best quality
        "voice_settings": {
            "stability": 0.45,          # Slightly varied — more natural for storytelling
            "similarity_boost": 0.80,
            "style": 0.25,              # Subtle expressiveness
            "use_speaker_boost": True
        }
    }

    output_path = Path(f"mvl-ep{episode_num:03d}-raw-audio.mp3")
    with requests.post(url, json=payload, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Voiceover generated: {output_path}")
    return output_path

# For long scripts (>2500 chars), chunk and concatenate:
def chunk_script(script: str, max_chars: int = 2000) -> list[str]:
    """Split script at paragraph boundaries for TTS chunking."""
    paragraphs = script.split('\n\n')
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) < max_chars:
            current += p + "\n\n"
        else:
            chunks.append(current.strip())
            current = p + "\n\n"
    if current:
        chunks.append(current.strip())
    return chunks
```

### Audio Post-Processing Pipeline

```bash
#!/bin/bash
# Full podcast audio processing pipeline
# Usage: bash process-audio.sh mvl-ep001-raw-audio.mp3 001

INPUT=$1
EP_NUM=$2
WORK_DIR="audio-work"
mkdir -p $WORK_DIR

echo "Step 1: Convert to WAV and apply noise reduction..."
ffmpeg -i $INPUT \
  -af "highpass=f=80, lowpass=f=12000, afftdn=nf=-25" \
  -ar 48000 $WORK_DIR/step1-clean.wav

echo "Step 2: Loudnorm Pass 1 (analyze)..."
ANALYSIS=$(ffmpeg -i $WORK_DIR/step1-clean.wav \
  -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json \
  -f null - 2>&1 | grep -A 20 '{')

# Parse JSON values (requires jq)
MEASURED_I=$(echo $ANALYSIS | jq -r '.input_i')
MEASURED_TP=$(echo $ANALYSIS | jq -r '.input_tp')
MEASURED_LRA=$(echo $ANALYSIS | jq -r '.input_lra')
MEASURED_THRESH=$(echo $ANALYSIS | jq -r '.input_thresh')
OFFSET=$(echo $ANALYSIS | jq -r '.target_offset')

echo "Step 3: Loudnorm Pass 2 (normalize)..."
ffmpeg -i $WORK_DIR/step1-clean.wav \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=${MEASURED_I}:measured_TP=${MEASURED_TP}:measured_LRA=${MEASURED_LRA}:measured_thresh=${MEASURED_THRESH}:offset=${OFFSET}:linear=true" \
  -ar 44100 -ac 2 $WORK_DIR/step2-normalized.wav

echo "Step 4: Generate transcript (Whisper)..."
whisper $WORK_DIR/step2-normalized.wav \
  --model medium \
  --output_format txt \
  --output_dir transcripts/ \
  --task transcribe

echo "Step 5: Export podcast MP3..."
ffmpeg -i $WORK_DIR/step2-normalized.wav \
  -codec:a libmp3lame -b:a 128k -ac 2 \
  mvl-ep${EP_NUM}-podcast-final.mp3

echo "Step 6: Export video audio track (AAC)..."
ffmpeg -i $WORK_DIR/step2-normalized.wav \
  -codec:a aac -b:a 192k \
  mvl-ep${EP_NUM}-video-audio.aac

echo "Pipeline complete. Files:"
echo "  Podcast: mvl-ep${EP_NUM}-podcast-final.mp3"
echo "  Video audio: mvl-ep${EP_NUM}-video-audio.aac"
echo "  Transcript: transcripts/step2-normalized.txt"
```

---

## B-ROLL SOURCING SYSTEM

```python
import requests
from pathlib import Path

def source_broll_pexels(search_query: str, episode_num: int, num_clips: int = 3):
    """Download B-roll video clips from Pexels (free, no attribution required for videos)."""
    PEXELS_API_KEY = "your_pexels_api_key"
    headers = {"Authorization": PEXELS_API_KEY}
    url = "https://api.pexels.com/videos/search"

    response = requests.get(url, headers=headers, params={
        "query": search_query,
        "per_page": num_clips,
        "orientation": "landscape",
        "size": "large"
    })
    videos = response.json()['videos']

    broll_dir = Path(f"ep{episode_num:03d}-broll")
    broll_dir.mkdir(exist_ok=True)

    for i, video in enumerate(videos):
        # Get highest quality MP4
        hd_file = sorted(video['video_files'],
                         key=lambda x: x.get('width', 0), reverse=True)[0]
        video_url = hd_file['link']

        clip_path = broll_dir / f"{search_query.replace(' ', '-')}-{i+1}.mp4"
        r = requests.get(video_url, stream=True)
        with open(clip_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {clip_path}")

# Example: source B-roll for Mothman episode sections
broll_queries = [
    "West Virginia river fog night",
    "abandoned industrial building",
    "bridge collapse water",
    "forest dark night aerial",
    "Chicago city night aerial"
]
for query in broll_queries:
    source_broll_pexels(query, episode_num=1)
```

---

## HERMES INTEGRATION — TRIGGER SYSTEM

### Episode State Machine

```python
# Hermes episode state management
# Each state transition triggers the next stage automatically

EPISODE_STATES = {
    "CONCEPT": "intake_form_submitted",
    "RESEARCH": "research_agents_running",
    "RESEARCH_REVIEW": "awaiting_human_review",
    "SCRIPTING": "script_agent_running",
    "SCRIPT_REVIEW": "awaiting_human_review",
    "PRODUCTION": "audio_video_pipeline_running",
    "PRODUCTION_REVIEW": "awaiting_human_review",
    "SCHEDULED": "publish_jobs_queued",
    "PUBLISHED": "episode_live",
    "ANALYTICS": "7_day_review_running",
    "COMPLETE": "episode_filed"
}

def advance_episode(episode_id: str, current_state: str):
    """Move episode to next state and trigger corresponding agent."""
    transitions = {
        "CONCEPT": lambda: trigger_research_agents(episode_id),
        "RESEARCH": lambda: notify_human_review(episode_id, "Research brief ready"),
        "RESEARCH_REVIEW": lambda: trigger_script_agent(episode_id),
        "SCRIPTING": lambda: notify_human_review(episode_id, "Script draft ready"),
        "SCRIPT_REVIEW": lambda: trigger_production_pipeline(episode_id),
        "PRODUCTION": lambda: notify_human_review(episode_id, "Production ready for review"),
        "PRODUCTION_REVIEW": lambda: trigger_publish_pipeline(episode_id),
        "SCHEDULED": lambda: monitor_publish(episode_id),
        "PUBLISHED": lambda: schedule_analytics_review(episode_id, days=7),
    }
    if current_state in transitions:
        transitions[current_state]()
```

### Scheduled Automation Jobs

```bash
# Crontab entries for the Thought Reliquary
# Edit via: crontab -e

# Weekly keyword research report (every Monday 8 AM CDT = 1 PM UTC)
0 13 * * 1 python3 /home/user/workspace/scripts/keyword-report.py

# YouTube analytics pull (every Friday 9 AM CDT = 2 PM UTC)
0 14 * * 5 python3 /home/user/workspace/scripts/pull-analytics.py

# Episode pipeline state check (every 6 hours)
0 */6 * * * python3 /home/user/workspace/scripts/hermes-pipeline-check.py

# Podcast RSS feed validation (daily)
0 10 * * * curl -s https://your-podcast-feed-url | xmllint --format - > /dev/null \
  && echo "RSS OK" || echo "RSS ERROR — check feed"
```

---

## RECOMMENDED TOOL STACK — COMPLETE REFERENCE

| Category | Tool | Cost | Integration |
|----------|------|------|------------|
| **Orchestration** | Hermes (custom) | — | Core |
| **Script Generation** | Claude API (Sonnet) | ~$0.003/1K tokens | API |
| **Local LLM** | Ollama + Llama 3.1 8B | Free (local) | REST |
| **TTS / Voiceover** | ElevenLabs | $22/mo (Creator) | API |
| **Audio Processing** | ffmpeg | Free | CLI |
| **Transcription** | Whisper (local, medium) | Free | CLI / Python |
| **Thumbnail Base** | DALL-E 3 | ~$0.04/image | API |
| **Thumbnail Composite** | Pillow / ImageMagick | Free | CLI / Python |
| **B-roll (free)** | Pexels API | Free | API |
| **B-roll (AI)** | Runway ML Gen4 | $15-95/mo | API |
| **Video Assembly** | ffmpeg | Free | CLI |
| **YouTube** | YouTube Data API v3 | Free (quota) | API |
| **Podcast Host** | Buzzsprout | $12/mo | API |
| **Blog / CMS** | Ghost (self-hosted) | Free | Admin API |
| **Analytics** | YouTube Analytics API | Free | API |
| **Keyword Research** | pytrends + autocomplete | Free | Python |
| **Social Scheduling** | Buffer API | $6/mo | API |

**Total monthly cost estimate (running):** ~$55–70/month
- ElevenLabs Creator: $22
- Runway ML Starter: $15
- Buzzsprout: $12
- Claude API (usage): ~$5–15 depending on episode count
- Buffer: $6

---

## FRICTIONLESS PRODUCTION — THE DAILY WORKFLOW

What John actually does, distilled to its minimum viable form:

```
EPISODE WEEK 1
  Day 1 (30 min):
    → Fill in Episode Intake Form
    → Send to Hermes: "Begin research phase"
    → Done for the day

  Day 3 (30 min):
    → Read compiled research brief
    → Mark: approve / flag / need more
    → Send back to Hermes: "Proceed to scripting"
    → Done for the day

EPISODE WEEK 2
  Day 1 (60 min):
    → Read script draft
    → Annotate with [TIGHTEN] / [WRONG TONE] / [KEEPER]
    → Record any sections that need re-voice in personal notes
    → Send to Hermes: "Revise per notes, then trigger production"
    → Done for the day

  Day 3 (20 min):
    → Spot-check audio (listen to 3 random sections)
    → Watch video draft at 1.5x speed
    → Pick thumbnail from three options
    → Send to Hermes: "Approved — schedule publish"
    → Done for the day

EPISODE WEEK 3
  Day 2 (5 min):
    → Confirm publish scheduled
    → Done

  Day 9 (15 min):
    → Read 7-day analytics report
    → Note 3 learnings for next episode
    → Done
```

**Total active human time per episode: ~2.5 to 3 hours.**
Everything else: agents, APIs, and the system that keeps receipts.

---

*OM-0017 · AI-Native Frictionless Production System*
*The Midnight Visitor Log · Lithium Dreams Industries · Ghost's Workshop*
*"Authorized personnel only. Things too weird to explain."*
*June 2026*
