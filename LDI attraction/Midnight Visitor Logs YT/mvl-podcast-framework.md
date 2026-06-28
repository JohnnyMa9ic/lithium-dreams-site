# MIDNIGHT VISITOR LOG
## Podcast Script Format Framework
### Lithium Dreams Industries · Broadcast Division
#### Document ID: OM-0013 · Revision 2037.1

> *"Same log. Different medium. The signal finds what it finds."*

---

## PURPOSE

The podcast version of a Midnight Visitor Log episode is a **direct audio adaptation** of the video script — stripped of all visual production cues and restructured for pure audio delivery. The same facts, the same voice, the same Joe Bob energy. Different room.

The podcast version is also the cleanest proof-of-concept for the headless production loop: one script → two broadcast formats, zero additional research.

---

## WHAT GETS STRIPPED

Remove every element that only makes sense visually:

| Video Script Element | Podcast Treatment |
|---------------------|-------------------|
| `[B-ROLL: aerial of Point Pleasant]` | Remove entirely |
| `[TO CAMERA]` | Remove — all delivery is assumed direct |
| `[VOICEOVER]` | Remove — all delivery is voiceover |
| `[HOST — ON CAMERA. Seated...]` | Remove stage direction; keep the words |
| `[MAP OVERLAY of Ohio River]` | Convert to audio description if essential; remove if not |
| `[TITLE CARD]` | Replace with audio intro bumper note |
| `[PAUSE]` | Keep — pause direction is valuable for recorded delivery |
| `[BEAT]` | Keep |
| `[TITLE CARD / INTRO MUSIC]` | Replace with `[AUDIO: INTRO BUMPER]` |
| Chapter marker timestamps | Convert to audio chapter markers (see Section 3) |

---

## PODCAST SCRIPT FORMAT

### Header Block

```
═══════════════════════════════════════════════════════
  MIDNIGHT VISITOR LOG — PODCAST VERSION
  Episode [###]: [TITLE]
  Lithium Dreams Industries · Filed after closing.
  Audio runtime estimate: [XX] min
  Recording notes: [Any special delivery notes]
═══════════════════════════════════════════════════════
```

---

### Standard Section Format

```
[AUDIO: INTRO BUMPER — atmospheric theme, ~10 seconds, fade under]

[CHAPTER 1 — THE COLD OPEN]

[HOST]
[Script text — no stage directions except PAUSE and BEAT]
[PAUSE]
[Script continues]

[AUDIO: BUMPER — short transition tone, 3-5 seconds]

[CHAPTER 2 — THE PLACE]
[HOST]
[Script continues...]
```

---

### Approved Audio Cues (podcast-only)

| Cue | Usage | Duration |
|-----|-------|----------|
| `[AUDIO: INTRO BUMPER]` | Opens every episode | ~15 sec |
| `[AUDIO: TRANSITION — short]` | Between major sections | 3–5 sec |
| `[AUDIO: TRANSITION — long]` | Before anchor event section | 5–8 sec |
| `[AUDIO: AMBIENT — low]` | Under witness account readings (optional) | Sustained at -18dB |
| `[AUDIO: OUTRO BUMPER]` | Closes every episode, under signoff | ~15 sec |
| `[PAUSE]` | Deliberate silence — host direction | 2–4 sec |
| `[BEAT]` | Brief breath before resuming | 1 sec |

---

### Visual-to-Audio Conversion Rules

**When video script says:** `[B-ROLL: archival footage of the Silver Bridge]`
**Podcast version:** Remove entirely — the narration carries the image

**When video script says:** `[MAP showing Ohio River corridor]`
**Podcast version:** Add one verbal orientation sentence if the geography is essential:
> *"For those of you listening — Point Pleasant sits right on the Ohio River, with Gallipolis, Ohio on the other side. The bridge connected them."*
Then proceed.

**When video script says:** `[HOST reads witness account aloud, text on screen]`
**Podcast version:** Same delivery, no change needed. Add `[SLIGHT PAUSE before returning to narration]`

**When video script says:** `[TITLE CARD: "THEORY BREAK"]`
**Podcast version:**
```
[AUDIO: TRANSITION — short]
[HOST]
"Alright. Three theories. We're going to walk through all of them, and I'm going to try not to pick one. Here we go."
```

---

## AUDIO CHAPTER STRUCTURE

Podcast chapters should match the video chapter markers. Submit to podcast platforms as chapter metadata.

| Chapter | Title | Timing Note |
|---------|-------|-------------|
| 1 | The Cold Open | 0:00 |
| 2 | The Place | After intro bumper |
| 3 | The Witnesses | Act II opening |
| 4 | The Anchor Event | Major transition |
| 5 | Three Theories | Theory break |
| 6 | Today / The Open Door | Act III |
| 7 | Close | Signoff |

**Technical implementation:**
Podcast chapter metadata can be embedded via:
- **Podbean:** Chapter markers via API at publish time
- **Buzzsprout:** Chapter markers in show notes (timestamp format: `00:00 Chapter Name`)
- **RSS feed:** Podlove Simple Chapters namespace in feed XML

---

## AUDIO PRODUCTION SPECS

**Target loudness:** -16 LUFS (Apple Podcasts standard) / -14 LUFS (Spotify)
Use ffmpeg loudnorm two-pass:
```bash
# Pass 1 — analyze
ffmpeg -i input.wav -af loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json -f null -

# Pass 2 — normalize (plug in measured_I, measured_TP, measured_LRA, measured_thresh from pass 1)
ffmpeg -i input.wav \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=[VAL]:measured_TP=[VAL]:measured_LRA=[VAL]:measured_thresh=[VAL]:offset=[VAL]:linear=true" \
  -ar 44100 -ac 2 output_normalized.wav
```

**Noise reduction (pre-normalization):**
```bash
ffmpeg -i input.wav \
  -af "highpass=f=80, lowpass=f=12000, afftdn=nf=-25" \
  output_clean.wav
```

**Export format:** 128kbps stereo MP3 for distribution; keep WAV master

**Intro/outro music:** Atmospheric instrumental; not horror, not ambient drone — something that feels like driving at night with the radio on. Loops cleanly for variable-length intros.

---

## SHOW NOTES TEMPLATE

Generated per episode — can be automated via Ollama/local LLM from transcript.

```
# [EPISODE TITLE] — Midnight Visitor Log Ep. [###]

Filed after closing at the Last Roadside Attraction.

[2-3 sentence episode description in host voice. Not a synopsis — a provocation.]

---

## In This Log:
- [Key point 1]
- [Key point 2]
- [Key point 3]

## Chapters:
00:00 The Cold Open
[XX:XX] The Place
[XX:XX] The Witnesses
[XX:XX] The Anchor Event
[XX:XX] Three Theories
[XX:XX] The Open Door
[XX:XX] Close

## Sources Filed:
[Primary sources with URLs — formatted as "Source Name — URL"]

## From the Gift Shop:
[Link to any related LDI product or postcard]

---
*Midnight Visitor Log is a Lithium Dreams Industries broadcast.*
*Filed after closing at the Last Roadside Attraction.*
*"The weirdness is not decoration. The system keeps receipts."*
```

---

## DISTRIBUTION CHECKLIST

- [ ] Audio normalized to -16 LUFS
- [ ] MP3 exported at 128kbps stereo
- [ ] Episode title follows format: `MVL-EP[###] — [TITLE]`
- [ ] Show notes written (or auto-generated and reviewed)
- [ ] Chapters mapped with timestamps
- [ ] Transcript generated (Whisper: `whisper output_normalized.wav --model medium`)
- [ ] Published to Buzzsprout or Podbean via API
- [ ] RSS feed updated and validated (`curl https://[feedurl] | xmllint --format -`)
- [ ] Submitted to: Spotify / Apple Podcasts / YouTube Music / Amazon Music
- [ ] Cross-promotion post drafted for LDI social

---

*OM-0013 · Podcast Script Format Framework*
*The Midnight Visitor Log · Lithium Dreams Industries*
*June 2026*
