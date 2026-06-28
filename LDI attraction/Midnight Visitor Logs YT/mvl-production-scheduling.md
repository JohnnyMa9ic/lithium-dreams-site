# MIDNIGHT VISITOR LOG
## Production Scheduling & Episode Pipeline Framework
### Lithium Dreams Industries · Operations Division
#### Document ID: OM-0015 · Revision 2037.1

> *Ghost's note: "Every episode is a system. Systems either hold or they don't. This one holds."*
> *Bob's annotation: "Ghost is right. I hate when Ghost is right."*

---

## DESIGN PRINCIPLE

The production system is built for **one person running an AI-assisted pipeline with constrained time**. John is a supply chain specialist by day, an architect of realms by night. The system cannot assume eight free hours per week. It must be designed to survive on two or three, with the AI handling everything that doesn't require a human.

**Core rule:** Every phase that can be delegated to an agent, must be delegated to an agent. The human's irreplaceable contribution is: creative direction, quality judgment, and final delivery voice.

---

## THE EPISODE PIPELINE — FIVE STAGES

```
STAGE 1: CONCEPTION (1 hour human time)
    ↓
STAGE 2: RESEARCH (agent-handled, async)
    ↓
STAGE 3: SCRIPT (agent draft + human review)
    ↓
STAGE 4: PRODUCTION (agent-handled, async)
    ↓
STAGE 5: PUBLISH & DISTRIBUTE (semi-automated)
```

**Total human time per episode target:** 4–6 hours across 2–3 weeks
**Agent time:** 8–12 hours (runs async, overnight, or while John is at work)

---

## STAGE 1: CONCEPTION
**Human time: ~1 hour**

| Task | Who | Time |
|------|-----|------|
| Complete Episode Intake Form (OM-0012 template) | Human | 20 min |
| Assign episode to attraction room and content lane | Human | 5 min |
| Draft 3 thumbnail concept options | Human or agent | 15 min |
| Identify primary research targets for Track 1 | Human | 10 min |
| Queue episode in Hermes production backlog | Agent | 5 min |

**Output:** Completed intake form + backlog entry with research queue

---

## STAGE 2: RESEARCH
**Human time: 30 min review**
**Agent time: 3–5 hours**

All five research tracks run in parallel via Hermes / Claude Code delegation.

```
[Hermes trigger: "Begin research phase for MVL-EP[###]"]
    → Agent A: Track 1 — Timeline
    → Agent B: Track 2 — Witness File
    → Agent C: Track 3 — Anchor Event
    → Agent D: Track 4 — Geographic Clusters
    → Agent E: Track 5 — Theory Landscape
    [All save to workspace: ep[###]-track[N]-[name].md]
    → Research Review Agent: compile ep[###]-research-brief.md
    → Notify: "Research complete for MVL-EP[###]"
```

**Human review:** Read compiled brief (~30 min). Flag: any [BOB FLAG] items needing verification. Approve for scripting or send back for specific additional research.

---

## STAGE 3: SCRIPT
**Human time: 1.5–2 hours**
**Agent time: 1 hour draft**

```
[Hermes trigger: "Begin script draft for MVL-EP[###]"]
    → Script Agent: reads research brief, applies OM-0012 framework v2,
      generates full video script to mvl-ep[###]-script-draft.md
    → Notify: "Script draft ready for review"

[Human review: 45–60 min]
    → Read full draft aloud (or read silently with delivery in mind)
    → Mark: [TIGHTEN] / [EXPAND] / [WRONG TONE] / [NEEDS SOURCE] / [KEEPER]
    → Write revision notes in-line

[Hermes trigger: "Revise script for MVL-EP[###] per review notes"]
    → Revision Agent: applies human notes, generates mvl-ep[###]-script-v2.md
    → Notify: "Revision ready"

[Human final read: 15–20 min]
    → Approve or flag for second revision
    → On approval: trigger format conversions
```

**Format conversions (agent-handled, simultaneous):**
- Podcast version → `mvl-ep[###]-podcast-script.md`
- Blog dossier → `mvl-ep[###]-blog-dossier.md`
- Social copy → `mvl-ep[###]-social-copy.md`

---

## STAGE 4: PRODUCTION
**Human time: 30–45 min**
**Agent/tool time: 4–6 hours**

### 4A — Audio Production

```
[ElevenLabs API or local TTS]
Input: mvl-ep[###]-podcast-script.md (clean, no stage directions)
Output: mvl-ep[###]-raw-audio.mp3

[ffmpeg processing pipeline]
1. Highpass filter (remove below 80Hz)
2. Noise reduction (afftdn)
3. Loudnorm two-pass (target -16 LUFS for Apple Podcasts)
Output: mvl-ep[###]-audio-normalized.wav

[Whisper transcription]
Input: mvl-ep[###]-audio-normalized.wav
Output: mvl-ep[###]-transcript.txt (used for captions, show notes)
```

**Human review: 15 min** — spot-check audio, flag any TTS errors for re-generation

### 4B — Video Production

```
[B-roll generation / sourcing]
→ B-roll list extracted from script stage directions
→ Source: archive.org (public domain), Pexels/Pixabay API (free stock),
  or Runway ML Gen4 API for AI-generated establishing shots
→ Save to ep[###]-broll/ directory

[Video assembly — DaVinci Resolve or FFmpeg sequence]
→ Audio: mvl-ep[###]-audio-normalized.wav
→ Visuals: B-roll per script timecodes
→ Text overlays: Witness quotes, section titles (ImageMagick or Resolve)
→ Chapter markers: embedded per section timestamps
→ Output: mvl-ep[###]-video-draft.mp4

[Thumbnail generation]
→ Generate 3 variants using DALL-E 3 / Midjourney / Stable Diffusion
→ Composite text overlay via ImageMagick
→ Save: ep[###]-thumb-A.jpg, ep[###]-thumb-B.jpg, ep[###]-thumb-C.jpg
```

**Human review: 20–30 min** — watch the draft at 1.5x, flag timing issues and B-roll misfits

### 4C — Final Export

```
[Video export]
→ 1080p H.264, -crf 18, AAC audio 192kbps
→ mvl-ep[###]-final.mp4

[Audio export]
→ 128kbps stereo MP3
→ mvl-ep[###]-podcast-final.mp3

[Thumbnail select]
→ Human picks from three variants (5 min decision)
→ Selected thumbnail: ep[###]-thumb-selected.jpg
```

---

## STAGE 5: PUBLISH & DISTRIBUTE
**Human time: 30–45 min**
**Agent/tool time: automated**

### YouTube Upload

```python
# YouTube Data API v3 — video upload
# See Algorithm Optimization Framework (OM-0016) for full implementation

upload_metadata = {
    "title": "MVL-EP[###] — [TITLE] | Midnight Visitor Log",
    "description": [formatted description with chapters + sources],
    "tags": ["midnight visitor log", "lithium dreams", "cryptids", ...],
    "categoryId": "27",  # Education
    "defaultLanguage": "en",
    "thumbnail": "ep[###]-thumb-selected.jpg"
}
```

**Manual steps (YouTube requires human interaction for new channels):**
- Upload video via YouTube Studio (or API after channel trust established)
- Set scheduled publish time (Tuesday 8 PM CDT recommended — see Algorithm Framework)
- Add end screen elements (15 sec from end — subscribe card + next video card)
- Add cards at 20%, 50%, and 80% of video

### Podcast Publish

```bash
# Buzzsprout API publish (automated)
curl -X POST https://www.buzzsprout.com/api/[PODCAST_ID]/episodes.json \
  -H "Authorization: Token token=[API_KEY]" \
  -F "title=MVL-EP[###] — [TITLE]" \
  -F "description=@ep[###]-show-notes.txt" \
  -F "audio_file=@mvl-ep[###]-podcast-final.mp3" \
  -F "published_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
```

### Blog / Website Publish

```bash
# Ghost Admin API — programmatic post creation
curl -X POST https://[GHOST_URL]/ghost/api/admin/posts/ \
  -H "Authorization: Ghost [JWT_TOKEN]" \
  -H "Content-Type: application/json" \
  -d @ep[###]-ghost-payload.json
```

Ghost payload generated automatically from blog dossier markdown via conversion script.

### Social Distribution

See Social Media Optimization Framework (OM-0016) for platform-specific social copy and scheduling.

---

## PRODUCTION CALENDAR — RECOMMENDED CADENCE

**Target:** 1 episode per 3 weeks (sustainable for one person with AI assistance)
**Burst mode:** 1 episode per 2 weeks if 2 episodes are in parallel pipeline

```
WEEK 1: CONCEPTION + RESEARCH
  Mon:  Complete Episode Intake Form (1 hr)
  Mon:  Launch research agents (30 min setup)
  Wed:  Review research brief (30 min)
  Fri:  Approve for scripting

WEEK 2: SCRIPT + PRODUCTION
  Mon:  Script draft delivered by agent
  Mon:  Script review + revision notes (1 hr)
  Tue:  Revised script delivered
  Wed:  Script approval + trigger production pipeline (20 min)
  Thu:  Audio review (15 min)
  Fri:  Video draft review (30 min)
  Fri:  Thumbnail selection (5 min)

WEEK 3: PUBLISH
  Mon:  Final export review (20 min)
  Tue:  Schedule YouTube upload + podcast + blog (30 min)
  Tue 8PM CDT: Episode goes live (automated)
  Wed:  Post social clips (automated from social copy)
  Fri:  Pull analytics report (automated — see OM-0016)
```

**Overlap:** Begin Week 1 of next episode during Week 3 of current episode. Two episodes in pipeline at all times once the system is running.

---

## EPISODE BACKLOG MANAGEMENT

Track all episodes in a simple Kanban using this status schema:

```
STATUS OPTIONS:
[ CONCEPT ]    → Idea logged, intake form not yet complete
[ INTAKE ]     → Intake form complete, research not yet started
[ RESEARCH ]   → Research agents running
[ SCRIPTING ]  → Script in draft or revision
[ PRODUCTION ] → Audio/video in production
[ REVIEW ]     → Final human review
[ SCHEDULED ]  → Set for publish, automated
[ PUBLISHED ]  → Live
[ ANALYZED ]   → Post-publish analytics reviewed, learnings filed
```

**In Hermes:** Each episode is a project node. Status updates trigger next-phase notifications.

---

## BACKLOG SEEDING — FIRST 10 EPISODE CONCEPTS

Ready to move to intake:

| # | Subject | Room | Type | Joe Bob Quotient |
|---|---------|------|------|-----------------|
| 1 | The Mothman (Point Pleasant) | Museum | Visitor Log | 3 |
| 2 | Skinwalker Ranch — BAASS & the Government | Employees Only | Visitor Log | 3 |
| 3 | The Flatwoods Monster (1952 WV) | Museum | Visitor Log | 4 |
| 4 | Bohemian Grove — What Actually Happens | Museum | Visitor Log | 3 |
| 5 | The Devil's Tramping Ground (NC) | Roadside | Roadside Incident | 3 |
| 6 | USA's Up All Night: The B-Movie Industrial Complex | Bob's | Bob's Unverified | 4 |
| 7 | The Lubbock Lights (1951) | Museum | Visitor Log | 2 |
| 8 | Meow Wolf — The Art That Became a Myth | Roadside | Roadside Incident | 3 |
| 9 | The Sallie House (Atchison, KS) | Museum | Visitor Log | 3 |
| 10 | The Lost Highway: Route 666 | Roadside | Roadside Incident | 4 |

---

*OM-0015 · Production Scheduling & Episode Pipeline Framework*
*The Midnight Visitor Log · Lithium Dreams Industries*
*"The system either holds or it doesn't. This one holds."*
*June 2026*
