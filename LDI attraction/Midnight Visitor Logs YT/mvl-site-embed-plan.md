# OM-0019 — PODCAST + YOUTUBE EMBED PLAN
## Lithium Dreams Industries · Operations Memorandum
## The Midnight Visitor Log · Broadcast Architecture

```
╔══════════════════════════════════════════════════════════════════╗
║  DOCUMENT ID  : OM-0019                                          ║
║  CLASSIFICATION: BROADCAST INFRASTRUCTURE · INTERNAL USE ONLY   ║
║  STATUS       : ACTIVE                                           ║
║  FILED BY     : Operations, Imagineering Division                ║
║  DATE         : 2026-06-26                                       ║
║  SUBJECT      : /broadcasts — Full Embed Architecture Plan       ║
║  SIGNOFF      : Keep the log open. I'll see you in the dark.     ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SECTION 1 — THE /BROADCASTS HUB PAGE

### Concept: THE BROADCAST TOWER

The `/broadcasts` page is the transmission node — the place where The Midnight Visitor Log signal originates and is received. Visually, it should feel like an unmanned monitoring station that has been running since someone last checked it. Analog dials. Signal bars that pulse irregularly. A timestamp that keeps updating because something is always being recorded.

---

### Page Header

```
┌─────────────────────────────────────────────────────────┐
│  ▓▓▓   BROADCAST TOWER — LDI SIGNAL OPERATIONS   ▓▓▓   │
│  ████████████████████████████████████████████████████  │
│  ACC. BRD-001                                           │
│  SIGNAL STATUS: ████ ACTIVE  ░░░ RECORDING  ···DORMANT  │
│  LAST TRANSMISSION: [dynamic — latest episode date]    │
└─────────────────────────────────────────────────────────┘
```

Hero area: full-width dark panel with subtle TV static noise texture (CSS `background-image: url('/assets/noise.png')` at low opacity overlaid on the dark background). A large waveform or signal-bar SVG animation pulses slowly. The accession number ACC. BRD-001 is stamped in the corner in monospace. The Signal Status badge updates dynamically based on whether a new episode has dropped in the last 7 days (ACTIVE), 7-30 days (RECORDING), or 30+ days (DORMANT).

---

### Content Sections

#### 1A — Latest Episode (Featured)

Positioned immediately below the hero, spanning full width or two-column layout (YouTube left, podcast right on desktop; stacked on mobile).

```
┌────────────────────────────────────────────────────┐
│  LATEST TRANSMISSION                               │
│  ─────────────────────────────────────────────── │
│  MVL-EP[###] · [EPISODE TITLE]                     │
│  CASE: [SUBJECT] · FILED: [DATE]                   │
│  STATUS: ██ ON AIR                                 │
│                                                    │
│  [YouTube embed — 16:9]    [Buzzsprout embed]      │
│                                                    │
│  [READ THE FULL CASE FILE →]                       │
└────────────────────────────────────────────────────┘
```

The "READ THE FULL CASE FILE →" button links to `/broadcasts/midnight-visitor-log/[latest-episode-slug]`.

#### 1B — Signal Status Panel

A narrow, full-width bar styled like a hardware status readout:

```
SIGNAL STATUS   TOWER: ONLINE   FEED: ACTIVE   LAST PING: [timestamp]
RECORDING QUEUE: [next episode date if known, else "UNDISCLOSED"]
```

This can be static HTML updated per episode. If the team later wants it dynamic, it can pull from a JSON file in the Astro `public/` folder.

#### 1C — Episode Archive Grid

Below the featured episode: a grid of dossier-style episode cards. Desktop: 3 columns. Tablet: 2 columns. Mobile: 1 column.

**Episode Card anatomy:**

```
┌─────────────────────────────────┐
│  [thumbnail — 16:9 image]       │
├─────────────────────────────────┤
│  MVL-EP[###]          ARCHIVED  │
│  ─────────────────────────────  │
│  EPISODE [##]: [TITLE]          │
│  CASE: [SUBJECT]                │
│  FILED: [DATE]                  │
│                                 │
│  [tag] [tag] [tag]              │
│                                 │
│  OPEN CASE FILE →               │
└─────────────────────────────────┘
```

Cards have a subtle border in LDI's UI green (`#4ade80` or matching existing brand accent), 1px solid, with a hover state that adds a faint glow (box-shadow: `0 0 8px rgba(74, 222, 128, 0.3)`). Background: slightly lighter than the page background to read as a card.

#### 1D — Submit to the Witness Registry

CTA block at the bottom of the /broadcasts page. Styled as an institutional form request notice:

```
┌────────────────────────────────────────────────────────┐
│  WITNESS REGISTRY — OPEN FOR SUBMISSIONS               │
│  ─────────────────────────────────────────────────── │
│  Did you see something? Hear something? Find something │
│  in a field that wasn't there yesterday?               │
│                                                        │
│  The Log is accepting field reports.                   │
│  Submissions are reviewed and may be filed.            │
│                                                        │
│  [SUBMIT A FIELD REPORT]                               │
└────────────────────────────────────────────────────────┘
```

Button links to the Witness Registry submission page (see OM-0020, Tier 4).

---

### URL Structure

```
/broadcasts                                  ← Hub page (ACC. BRD-001)
/broadcasts/midnight-visitor-log             ← Series index (ACC. BRD-002)
/broadcasts/midnight-visitor-log/[slug]      ← Individual episode pages
```

Example slug format: `ep001-mothman-signal` or `ep014-the-cathedral-frequency`

Astro file structure:
```
src/pages/
  broadcasts/
    index.astro                              ← /broadcasts hub
    midnight-visitor-log/
      index.astro                            ← series index
      [...slug].astro                        ← dynamic episode route
```

Episode data can live in:
- `src/content/episodes/` as Markdown/MDX files (Astro Content Collections)
- Frontmatter holds metadata; body is the dossier blog post

---

## SECTION 2 — EPISODE PAGE TEMPLATE

### `/broadcasts/midnight-visitor-log/[slug]`

---

### Episode Header

```
╔══════════════════════════════════════════════════════════════════╗
║  MIDNIGHT VISITOR LOG · EPISODE [##] · [DATE] · CASE: [SUBJECT] ║
║  ACC. MVL-EP[###]                    STATUS: ██ ON AIR           ║
╚══════════════════════════════════════════════════════════════════╝
```

- `MIDNIGHT VISITOR LOG` — small-caps or tracked uppercase, muted color
- `EPISODE [##]` — large, prominent
- `[DATE]` — formatted as `YYYY · MON · DD` for dossier aesthetic
- `CASE: [SUBJECT]` — the cryptid/subject name, styled as a label
- Accession number `MVL-EP[###]` — bottom left, monospace, small
- Status badge — top right, one of: `ON AIR` / `ARCHIVED` / `FIELD RECORDING`

Status badge colors (matching LDI badge system):
- `ON AIR` → ACTIVE (green glow)
- `ARCHIVED` → neutral/muted
- `FIELD RECORDING` → FLICKERING (amber pulse animation)

---

### Embed Layout

**Recommended order (top to bottom):**

1. YouTube embed (primary)
2. Podcast (Buzzsprout) embed (secondary)
3. Dossier blog post body

**Reasoning:** Visitors arriving from YouTube search or the YouTube channel will expect video first. The podcast embed directly below serves listeners who prefer audio-only and reinforces cross-platform presence. The written dossier content serves SEO and long-form readers who find the page via search. This order also matches typical consumption patterns: watch/listen first, then read the expanded case notes.

**Two-column option (desktop only):** On screens wider than 1024px, the YouTube embed and a sidebar can sit side-by-side, with the podcast embed below the video in the main column. This avoids the podcast embed feeling like an afterthought.

```
Desktop layout:
┌──────────────────────────┬─────────────────┐
│  [YouTube embed — 16:9]  │  CASE FILE STATS│
│                          │  ─────────────  │
│  [Buzzsprout embed]      │  Episode length │
│                          │  Witness count  │
│  [Dossier body text]     │  Theories filed │
│                          │  Case status    │
│                          │                 │
│                          │  [INCIDENT TAGS]│
└──────────────────────────┴─────────────────┘
```

---

### Case File Stats Sidebar

```
┌─────────────────────────┐
│  CASE FILE              │
│  ───────────────────── │
│  EPISODE LENGTH  [mm:ss]│
│  WITNESSES       [##]   │
│  THEORIES FILED  [##]   │
│  CASE STATUS     OPEN   │
│  ───────────────────── │
│  INCIDENT TAGS          │
│  [#appalachia]          │
│  [#mothman]             │
│  [#electromagnetic]     │
│  [#eyewitness]          │
└─────────────────────────┘
```

Incident tags are internal taxonomy links. Clicking a tag goes to `/broadcasts?tag=mothman` (filtered archive view — phase 2 feature; initially just decorative with `href="#"`).

---

### Dossier Blog Post Body

The written content below the embeds. Typography recommendations:
- Monospace font for "field notes" styled callout blocks
- Horizontal rules using box-drawing characters: `────────────────────`
- Pull quotes or key witness statements set in a dark box with a left border accent
- Images (if any) captioned with `[EXHIBIT A — PHOTOGRAPH, DATE UNKNOWN]` style labels

---

### Navigation Footer

```
← PREVIOUS CASE FILE: MVL-EP[###] — [TITLE]
→ NEXT CASE FILE: MVL-EP[###] — [TITLE]
```

Plus the Subscribe CTA block:

```
┌─────────────────────────────────────────────────────────┐
│  SUBSCRIBE TO THE SIGNAL                                │
│  ─────────────────────────────────────────────────── │
│  The Log continues. New transmissions are filed        │
│  when evidence permits.                                 │
│                                                         │
│  [YOUTUBE — @LithiumDreamsTV]  [PODCAST — BUZZSPROUT]  │
└─────────────────────────────────────────────────────────┘
```

---

## SECTION 3 — YOUTUBE EMBED TECHNICAL SPEC

### Parameters

| Parameter        | Value               | Reason                                              |
|------------------|---------------------|-----------------------------------------------------|
| `autoplay`       | `0`                 | Never autoplay — intrusive, penalized by browsers   |
| `rel`            | `0`                 | Suppress related videos from other channels         |
| `modestbranding` | `1`                 | Reduces YouTube branding in controls                |
| `color`          | `white`             | White progress bar (matches dark LDI aesthetic)     |
| `origin`         | `https://lithium-dreams.com` | Required for postMessage security        |

Privacy mode: `youtube-nocookie.com` — does not set cookies until the user interacts with the player. Required for GDPR compliance and good practice.

---

### Responsive Wrapper CSS

```css
/* _embeds.css or inline in component */
.yt-embed-wrapper {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 aspect ratio */
  overflow: hidden;
  background-color: #0a0a0a;
}

.yt-embed-wrapper iframe {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  border: none;
}

/* Optional: LDI border treatment */
.yt-embed-wrapper {
  border: 1px solid rgba(74, 222, 128, 0.2);
}
```

---

### Lazy Load with Click-to-Play Poster

Instead of loading the iframe immediately (which fires a YouTube network request and slows page load), render a thumbnail image with a play button overlay. The iframe is injected on click.

This technique (sometimes called "lite-youtube") reduces initial page load by ~500ms–1s for episode pages with embeds.

---

### YoutubeEmbed.astro

```astro
---
// src/components/YoutubeEmbed.astro
// Usage: <YoutubeEmbed videoId="dQw4w9WgXcQ" title="Episode 01: The Mothman Signal" />

export interface Props {
  videoId: string;
  title: string;
  posterQuality?: 'default' | 'mqdefault' | 'hqdefault' | 'sddefault' | 'maxresdefault';
}

const {
  videoId,
  title,
  posterQuality = 'hqdefault',
} = Astro.props;

const posterUrl = `https://i.ytimg.com/vi/${videoId}/${posterQuality}.jpg`;
const embedUrl = `https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1&color=white&origin=https://lithium-dreams.com`;
---

<div
  class="yt-embed-wrapper"
  data-video-id={videoId}
  data-embed-url={embedUrl}
  role="button"
  tabindex="0"
  aria-label={`Play video: ${title}`}
>
  <img
    src={posterUrl}
    alt={`Thumbnail for ${title}`}
    class="yt-poster"
    loading="lazy"
    decoding="async"
  />
  <button class="yt-play-btn" aria-hidden="true">
    <!-- Play triangle SVG -->
    <svg viewBox="0 0 68 48" width="68" height="48" xmlns="http://www.w3.org/2000/svg">
      <path d="M66.52 7.74c-.78-2.93-2.49-5.41-5.42-6.19C55.79.13 34 0 34 0S12.21.13 6.9 1.55c-2.93.78-4.63 3.26-5.42 6.19C.06 13.05 0 24 0 24s.06 10.95 1.48 16.26c.78 2.93 2.49 5.41 5.42 6.19C12.21 47.87 34 48 34 48s21.79-.13 27.1-1.55c2.93-.78 4.64-3.26 5.42-6.19C67.94 34.95 68 24 68 24s-.06-10.95-1.48-16.26z" fill="#ff0000"/>
      <path d="M45 24 27 14v20" fill="#fff"/>
    </svg>
  </button>
</div>

<style>
  .yt-embed-wrapper {
    position: relative;
    width: 100%;
    padding-top: 56.25%;
    overflow: hidden;
    background-color: #0a0a0a;
    cursor: pointer;
    border: 1px solid rgba(74, 222, 128, 0.2);
  }

  .yt-poster {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: filter 0.2s ease;
  }

  .yt-embed-wrapper:hover .yt-poster {
    filter: brightness(0.8);
  }

  .yt-play-btn {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: none;
    border: none;
    cursor: pointer;
    opacity: 0.9;
    transition: opacity 0.2s ease, transform 0.2s ease;
  }

  .yt-embed-wrapper:hover .yt-play-btn {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1.1);
  }

  .yt-embed-wrapper iframe {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    border: none;
  }
</style>

<script>
  document.querySelectorAll('.yt-embed-wrapper').forEach((wrapper) => {
    const activate = () => {
      const embedUrl = wrapper.getAttribute('data-embed-url');
      const iframe = document.createElement('iframe');
      iframe.src = embedUrl;
      iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
      iframe.allowFullscreen = true;
      iframe.title = wrapper.getAttribute('aria-label') || 'YouTube video';
      // Remove poster and button, insert iframe
      wrapper.innerHTML = '';
      wrapper.appendChild(iframe);
    };

    wrapper.addEventListener('click', activate);
    wrapper.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') activate();
    });
  });
</script>
```

---

## SECTION 4 — PODCAST EMBED TECHNICAL SPEC

### Buzzsprout Embed Code Pattern

Buzzsprout provides a standard `<iframe>` embed. The URL format is:

```
https://www.buzzsprout.com/[PODCAST_ID]/[EPISODE_ID]?client_source=small_player&iframe=true
```

Replace `[PODCAST_ID]` with the LDI Buzzsprout podcast ID (found in the Buzzsprout dashboard under Podcast Settings → Embed Player). Replace `[EPISODE_ID]` for specific episodes, or use the playlist/podcast-wide embed for the hub page.

**Hub page:** Use the podcast-wide embed (no episode ID) — shows the full episode list inside the player.

**Episode pages:** Use the episode-specific embed ID for that episode.

---

### Placement Recommendation

**Place the podcast embed BELOW the YouTube embed, ABOVE the dossier body text.**

Reasoning:
1. YouTube is the primary discovery platform for new audiences — video first.
2. The podcast embed serves returning listeners who came for audio — they'll scroll past the video to find it.
3. The dossier text below both embeds serves search traffic and long-form readers, who are typically not in consumption mode and don't mind scrolling.
4. Placing the podcast embed ABOVE YouTube would prioritize the smaller audience and push the highest-engagement element (video) down the page without benefit.

---

### LDI Radio Widget vs. Episode Embed

**They should be complementary, not identical:**

| | LDI Radio (Header Widget) | Episode Page Embed |
|---|---|---|
| **Feed** | Latest episode auto-loaded, always current | Specific episode only |
| **Purpose** | Ambient presence, discovery, "signal is live" | Deep engagement, full episode |
| **Context** | Every page — persistent presence | Episode pages only |
| **Interaction** | Click to expand → link to /broadcasts | Full Buzzsprout player inline |

The Radio widget in the header should pull from the Buzzsprout RSS feed and display the latest episode. It does NOT need to be a full player — it functions as a signal beacon. The full episode player lives on the episode page.

---

### PodcastEmbed.astro

```astro
---
// src/components/PodcastEmbed.astro
// Usage:
//   Specific episode: <PodcastEmbed podcastId="XXXXXX" episodeId="XXXXXXXXX" title="Episode 01" />
//   Full podcast player: <PodcastEmbed podcastId="XXXXXX" title="The Midnight Visitor Log" />

export interface Props {
  podcastId: string;
  episodeId?: string;
  title: string;
}

const { podcastId, episodeId, title } = Astro.props;

// Buzzsprout embed URL
const embedSrc = episodeId
  ? `https://www.buzzsprout.com/${podcastId}/${episodeId}?client_source=small_player&iframe=true`
  : `https://www.buzzsprout.com/${podcastId}?client_source=small_player&iframe=true`;
---

<div class="podcast-embed-wrapper">
  <div class="podcast-embed-label">
    <span class="podcast-label-text">▶ AUDIO TRANSMISSION — {title}</span>
    <span class="podcast-badge">BUZZSPROUT</span>
  </div>
  <iframe
    src={embedSrc}
    loading="lazy"
    width="100%"
    height="200"
    frameborder="0"
    scrolling="no"
    title={`Podcast: ${title}`}
    allow="autoplay"
  ></iframe>
</div>

<style>
  .podcast-embed-wrapper {
    width: 100%;
    margin: 1.5rem 0;
    border: 1px solid rgba(74, 222, 128, 0.2);
    background-color: #0d0d0d;
  }

  .podcast-embed-label {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0.75rem;
    background-color: rgba(74, 222, 128, 0.05);
    border-bottom: 1px solid rgba(74, 222, 128, 0.15);
    font-family: 'Courier New', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: rgba(74, 222, 128, 0.7);
  }

  .podcast-badge {
    font-size: 0.6rem;
    border: 1px solid rgba(74, 222, 128, 0.3);
    padding: 0.1rem 0.35rem;
    color: rgba(74, 222, 128, 0.5);
  }

  .podcast-embed-wrapper iframe {
    display: block;
    width: 100%;
    border: none;
  }
</style>
```

---

## SECTION 5 — LDI RADIO WIDGET UPGRADE

### Current State
The header LDI Radio widget has a waveform animation but is presumably static or decorative.

### Upgraded Behavior

**States:**
- `SIGNAL: ACTIVE` — a new episode dropped in the last 14 days → shows episode title, pulsing waveform
- `SIGNAL: DORMANT` — no episode in 14+ days → flat waveform, muted indicator
- `LOADING` — brief state while RSS fetches

**On click:**
- If ACTIVE: expand to show a mini player preview + "OPEN FULL BROADCAST →" link to `/broadcasts`
- If DORMANT: link directly to `/broadcasts` with "LAST TRANSMISSION: [date]"

---

### RSS Feed Integration (Astro)

**Option A — Build-time fetch (SSG, simplest):**

Fetch the Buzzsprout RSS feed during `astro build`. Inject latest episode title/date as a static prop into the header. Updates on each deploy.

```astro
---
// In your Layout.astro or Header.astro
const RSS_URL = 'https://feeds.buzzsprout.com/[PODCAST_ID].rss';

let latestEpisode = null;
let signalStatus = 'DORMANT';

try {
  const res = await fetch(RSS_URL);
  const xml = await res.text();
  // Minimal XML parse — extract first <item>
  const titleMatch = xml.match(/<item>[\s\S]*?<title><!\[CDATA\[(.*?)\]\]><\/title>/);
  const pubDateMatch = xml.match(/<item>[\s\S]*?<pubDate>(.*?)<\/pubDate>/);

  if (titleMatch && pubDateMatch) {
    const pubDate = new Date(pubDateMatch[1]);
    const daysSince = (Date.now() - pubDate.getTime()) / (1000 * 60 * 60 * 24);
    latestEpisode = {
      title: titleMatch[1],
      date: pubDate.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
    };
    signalStatus = daysSince < 14 ? 'ACTIVE' : 'DORMANT';
  }
} catch (e) {
  // Fail silently — widget shows DORMANT
}
---
```

**Option B — Client-side fetch (works on static deploy, slight flicker):**

Use a `<script>` tag in the Radio widget component to fetch the RSS feed via a CORS proxy or a Cloudflare Worker that proxies the Buzzsprout RSS feed. Cloudflare Pages Functions are ideal for this.

```
// functions/api/latest-episode.js  (Cloudflare Pages Function)
export async function onRequest(context) {
  const res = await fetch('https://feeds.buzzsprout.com/[PODCAST_ID].rss');
  const xml = await res.text();
  // Parse and return JSON
  const titleMatch = xml.match(/<item>[\s\S]*?<title><!\[CDATA\[(.*?)\]\]><\/title>/);
  const pubDateMatch = xml.match(/<item>[\s\S]*?<pubDate>(.*?)<\/pubDate>/);
  const data = {
    title: titleMatch?.[1] ?? null,
    pubDate: pubDateMatch?.[1] ?? null,
  };
  return new Response(JSON.stringify(data), {
    headers: { 'Content-Type': 'application/json', 'Cache-Control': 'max-age=3600' }
  });
}
```

Then the widget `fetch('/api/latest-episode')` on mount.

**Recommendation:** Use Option A (build-time) for simplicity. Option B for real-time accuracy. Given LDI posts episodes periodically rather than continuously, build-time is sufficient — Cloudflare Pages redeploys can be triggered after each episode publishes.

---

### Widget States CSS Notes

```css
/* Waveform animation — ACTIVE state */
.ldi-radio[data-status="active"] .waveform-bar {
  animation: waveform-pulse 1.2s ease-in-out infinite;
}

/* DORMANT state — flat, no animation */
.ldi-radio[data-status="dormant"] .waveform-bar {
  animation: none;
  height: 2px;
  opacity: 0.3;
}

@keyframes waveform-pulse {
  0%, 100% { transform: scaleY(0.3); }
  50% { transform: scaleY(1); }
}
```

---

## SECTION 6 — NAV UPGRADE

### Current Nav

```
ATTRACTION · GIFT SHOP · ARCADE · MUSEUM · FORTUNE · CHAPEL · GARDEN · EMPLOYEES ONLY · ABOUT
```

### Problem

BROADCASTS is not just a content section — it's the primary ongoing creative output of LDI. It deserves a nav position that reflects that, without disrupting the Attraction aesthetic.

### Recommended Nav Label

**`THE LOG`** — short, evocative, fits the Attraction voice. "The Midnight Visitor Log" → abbreviated to "The Log."

Alternative options (ranked):
1. **`THE LOG`** ← recommended
2. `TRANSMISSIONS` — broadcast aesthetic, slightly more descriptive
3. `THE BROADCAST TOWER` — too long for nav
4. `BROADCASTS` — too generic, doesn't fit LDI voice

### Updated Nav Order

```
ATTRACTION · THE LOG · GIFT SHOP · ARCADE · MUSEUM · FORTUNE · CHAPEL · GARDEN · EMPLOYEES ONLY · ABOUT
```

**Placement reasoning:** THE LOG goes second, immediately after ATTRACTION, because:
1. It's the most active, frequently updated part of the site
2. It drives repeat visits — returning fans come back for new episodes
3. Putting it early rewards the core audience
4. ATTRACTION stays first as the primary location-setting element

### Mobile Nav

On mobile, THE LOG should appear in the top 4 items (most tapped). Consider: ATTRACTION · THE LOG · FORTUNE · [MENU →]

### Status Indicator on Nav Link

The nav item `THE LOG` can carry a small status badge that matches the Signal Status:

```html
<a href="/broadcasts">
  THE LOG
  <span class="nav-badge active" aria-label="Signal Active">●</span>
</a>
```

The badge pulses green when a new episode has dropped in the last 14 days, goes dark otherwise. This is the broadcast equivalent of a notification dot — implemented with the same build-time RSS fetch from Section 5.

---

## SECTION 7 — SEO + METADATA STRATEGY

### Title Tag Format

```
[Episode Title] | Midnight Visitor Log Ep. [##] | Lithium Dreams Industries
```

Example:
```
The Mothman Signal | Midnight Visitor Log Ep. 01 | Lithium Dreams Industries
```

Max 60 characters for the primary phrase. The full title can be longer — Google truncates but the full string is indexed.

### Meta Description Pattern

Cold, institutional, search-optimized. Lead with the subject, end with the hook.

Template:
```
[Subject] · Case filed [Month Year]. [One sentence on the incident/topic in LDI voice.] Watch + listen to The Midnight Visitor Log on Lithium Dreams Industries.
```

Example:
```
Mothman · Case filed November 2024. Electromagnetic interference, bridge lights, and 23 witnesses who all looked up at the same time. Watch + listen to The Midnight Visitor Log on Lithium Dreams Industries.
```

120-155 characters. Keywords: episode subject name, "Midnight Visitor Log", "cryptid podcast", subject-specific search terms.

### Open Graph Image Strategy

Each episode needs a distinct OG image (1200×630px). Options:

**A — YouTube thumbnail:** Use the episode's YouTube thumbnail directly. Buzzsprout may also provide episode artwork. This is the simplest approach — consistent with what users see on YouTube/Spotify.

**B — LDI-branded OG template:** A dark, dossier-style template with:
- Episode number top-left (monospace)
- Episode title centered (large, tracked uppercase)
- Case subject bottom (muted, smaller)
- LDI logo / accession number bottom-right
- Noise texture background
- Thin green/teal border

Option B is strongly preferred — the LDI aesthetic in social card previews is a marketing asset. When someone shares an episode link on social, the card should look unmistakably LDI.

Generate these as static images per episode (Figma template or a simple script using Canvas/Satori for automated generation on Cloudflare).

**Astro Head component:**
```astro
---
// In episode [...slug].astro
const { episode } = Astro.props;
---
<head>
  <title>{episode.title} | Midnight Visitor Log Ep. {episode.number} | Lithium Dreams Industries</title>
  <meta name="description" content={episode.metaDescription} />
  <meta property="og:title" content={`${episode.title} | Midnight Visitor Log`} />
  <meta property="og:description" content={episode.metaDescription} />
  <meta property="og:image" content={`https://lithium-dreams.com/og/episodes/${episode.slug}.jpg`} />
  <meta property="og:type" content="video.other" />
  <meta property="og:url" content={`https://lithium-dreams.com/broadcasts/midnight-visitor-log/${episode.slug}`} />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content={`https://lithium-dreams.com/og/episodes/${episode.slug}.jpg`} />
</head>
```

### VideoObject Structured Data

Add JSON-LD to each episode page for VideoObject schema — this enables rich results in Google Search (video thumbnails, duration, upload date).

```astro
---
const videoSchema = {
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": episode.title,
  "description": episode.metaDescription,
  "thumbnailUrl": `https://i.ytimg.com/vi/${episode.youtubeId}/hqdefault.jpg`,
  "uploadDate": episode.publishDate,  // ISO 8601: "2024-11-01"
  "duration": episode.duration,       // ISO 8601: "PT45M30S"
  "contentUrl": `https://www.youtube.com/watch?v=${episode.youtubeId}`,
  "embedUrl": `https://www.youtube-nocookie.com/embed/${episode.youtubeId}`,
  "publisher": {
    "@type": "Organization",
    "name": "Lithium Dreams Industries",
    "url": "https://lithium-dreams.com"
  }
};
---
<script type="application/ld+json" set:html={JSON.stringify(videoSchema)}></script>
```

### Podcast RSS Feed Integration

Buzzsprout auto-generates a valid RSS 2.0 feed with Apple Podcasts and Spotify extensions. Link it in the `<head>` of every page (or at minimum the /broadcasts pages):

```html
<link
  rel="alternate"
  type="application/rss+xml"
  title="The Midnight Visitor Log — Lithium Dreams Industries"
  href="https://feeds.buzzsprout.com/[PODCAST_ID].rss"
/>
```

This enables podcast apps and feed readers to autodiscover the show from the website URL — a small SEO and discoverability win that takes one line to implement.

---

```
╔══════════════════════════════════════════════════════════╗
║  OM-0019 · END OF DOCUMENT                               ║
║  Filed after closing at the Last Roadside Attraction.    ║
╚══════════════════════════════════════════════════════════╝
```
