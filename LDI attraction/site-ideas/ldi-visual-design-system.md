# VD-0001 — LDI Visual Design System
### lithium-dreams.com · Document ID: VD-0001 · Rev 1.0 · June 2026

---

> **Purpose:** This document is the canonical design specification for all visual output on lithium-dreams.com and its sub-properties. It bridges the 19 approved mockups and live site implementation. A developer reading this document should be able to build every page, component, and asset to mockup fidelity without asking a design question.

---

## TABLE OF CONTENTS

1. [The Two Aesthetic Systems](#section-1)
2. [Component Library — Attraction Dark](#section-2)
3. [Component Library — Glasshouse Light](#section-3)
4. [Asset Pipeline](#section-4)
5. [Site-Specific Implementation Notes](#section-5)
6. [Merch Asset Production Guide](#section-6)
7. [ComfyUI Workflow for Site Assets](#section-7)

---

<a name="section-1"></a>
## SECTION 1: THE TWO AESTHETIC SYSTEMS

LDI operates two visually distinct design systems that must never bleed into each other. They live at different URLs, serve different audiences, and embody different metaphors.

| | System A: ATTRACTION DARK | System B: GLASSHOUSE LIGHT |
|---|---|---|
| **URL scope** | lithium-dreams.com (root + all rooms) | lithium-dreams.com/work |
| **Metaphor** | A living roadside attraction you physically descend into | A precision studio with architectural glass and brushed steel |
| **Tone** | Eerie, warm, decaying, alive | Clean, confident, material, contemporary |
| **Audience** | Visitors, creative collaborators, the curious | Prospective studio clients |
| **Color temperature** | Warm amber + cold teal against void black | Champagne gold + slate against near-black navy |
| **Type voice** | Condensed all-caps, monospace, vertical Japanese | Geometric sans, generous tracking, structured hierarchy |

---

### 1.1 System A: ATTRACTION DARK

#### 1.1.1 Color Tokens

All tokens are CSS custom properties defined on `:root`. The naming convention is `--ldi-[role]-[variant]`.

```css
:root {
  /* === FOUNDATION === */
  --ldi-void:              #0a0907;   /* True page background — near-black with faint warmth */
  --ldi-void-deep:         #060504;   /* Deepest layer, underground sections */
  --ldi-void-lifted:       #111009;   /* Slightly raised surface, modal backdrops */

  /* === PANEL SURFACES === */
  --ldi-surface:           #141210;   /* Default card/panel background */
  --ldi-surface-warm:      #1a1610;   /* Warmer panel — parchment-adjacent contexts */
  --ldi-surface-cool:      #0d1214;   /* Cooler panel — signal/tech contexts */
  --ldi-surface-parchment: #f0e8d0;   /* Aged parchment — Fortune Ticket, Artifact cards */
  --ldi-surface-parchment-dark: #d4c9a8; /* Darker parchment, active state */

  /* === PANEL BORDERS === */
  --ldi-border:            #2a2520;   /* Default border */
  --ldi-border-amber:      #8a6020;   /* Amber-tinted border */
  --ldi-border-teal:       #1a4a44;   /* Teal-tinted border */
  --ldi-border-dim:        #1c1a17;   /* Barely-there border for nested panels */

  /* === TEXT === */
  --ldi-text-primary:      #e8dcc0;   /* Main body text — warm off-white/parchment */
  --ldi-text-secondary:    #a89870;   /* Secondary text — muted gold */
  --ldi-text-dim:          #5a5040;   /* Dim text — breadcrumbs, labels */
  --ldi-text-ghost:        #302820;   /* Near-invisible — background texture text */
  --ldi-text-parchment:    #2a1f0a;   /* Dark ink on parchment backgrounds */

  /* === ACCENT: TEAL (Signal) === */
  --ldi-teal:              #00e5cc;   /* Primary teal — root map, active states */
  --ldi-teal-dim:          #00a090;   /* Subdued teal — borders, inactive signals */
  --ldi-teal-ghost:        #003d38;   /* Ghost teal — background glows */
  --ldi-teal-glow:         rgba(0, 229, 204, 0.15); /* Glow fill */
  --ldi-teal-glow-strong:  rgba(0, 229, 204, 0.35); /* Strong glow for active nodes */

  /* === ACCENT: AMBER (Heat/Warning) === */
  --ldi-amber:             #d4820a;   /* Primary amber */
  --ldi-amber-bright:      #f0a020;   /* Hot amber — FLICKERING status, highlight */
  --ldi-amber-dim:         #7a4a08;   /* Dim amber — inactive warm borders */
  --ldi-amber-glow:        rgba(212, 130, 10, 0.20);
  --ldi-amber-glow-strong: rgba(240, 160, 32, 0.40);

  /* === ACCENT: CRIMSON (Danger/Denied) === */
  --ldi-crimson:           #c0281a;   /* Access denied, danger */
  --ldi-crimson-dim:       #701008;
  --ldi-crimson-glow:      rgba(192, 40, 26, 0.25);

  /* === ACCENT: GOLD (Muted, Decorative) === */
  --ldi-gold:              #b08840;   /* Muted gold — decorative accents, seals */
  --ldi-gold-bright:       #d4a848;   /* Bright gold — highlights */

  /* === STATUS COLORS === */
  --ldi-status-open:       #00e5cc;   /* OPEN — teal */
  --ldi-status-active:     #4cbb6a;   /* ACTIVE — green */
  --ldi-status-flickering: #f0a020;   /* FLICKERING — amber */
  --ldi-status-unstable:   #e0601a;   /* UNSTABLE — orange */
  --ldi-status-denied:     #c0281a;   /* ACCESS DENIED — crimson */
  --ldi-status-appointment:#6a5a40;   /* BY APPOINTMENT — dark tan */
  --ldi-status-coming:     #3a3228;   /* COMING SOON — very dim */
  --ldi-status-prepared:   #8a7858;   /* PREPARED — parchment-warm */
}
```

#### 1.1.2 Typography Tokens

**Font Stack — Attraction Dark**

| Role | Font | Source | Fallback |
|---|---|---|---|
| **Display / Heading** | Bebas Neue | Google Fonts | Impact, Arial Black, sans-serif |
| **Body** | Inter | Google Fonts | system-ui, sans-serif |
| **Monospace / Dossier** | Space Mono | Google Fonts | Courier New, monospace |
| **Japanese Accent** | Noto Serif JP | Google Fonts | serif |

```html
<!-- Font loading (in <head>) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400;700&family=Noto+Serif+JP:wght@400;600;700&display=swap" rel="stylesheet">
```

```css
:root {
  /* === FONT FAMILIES === */
  --ldi-font-display:  'Bebas Neue', Impact, 'Arial Black', sans-serif;
  --ldi-font-body:     'Inter', system-ui, -apple-system, sans-serif;
  --ldi-font-mono:     'Space Mono', 'Courier New', monospace;
  --ldi-font-japanese: 'Noto Serif JP', serif;

  /* === FONT SIZES === */
  --ldi-text-xs:   0.625rem;   /*  10px — accession numbers, micro labels */
  --ldi-text-sm:   0.75rem;    /*  12px — breadcrumbs, status tags, captions */
  --ldi-text-base: 0.875rem;   /*  14px — body copy */
  --ldi-text-md:   1rem;       /*  16px — card body */
  --ldi-text-lg:   1.25rem;    /*  20px — card titles */
  --ldi-text-xl:   1.5rem;     /*  24px — section headings */
  --ldi-text-2xl:  2rem;       /*  32px — room titles */
  --ldi-text-3xl:  3rem;       /*  48px — hero sub-titles */
  --ldi-text-4xl:  4.5rem;     /*  72px — hero titles */
  --ldi-text-5xl:  7rem;       /* 112px — hero display (Bebas Neue) */
  --ldi-text-6xl:  10rem;      /* 160px — oversized vertical display text */

  /* === FONT WEIGHTS === */
  --ldi-weight-light:   300;
  --ldi-weight-regular: 400;
  --ldi-weight-medium:  500;
  --ldi-weight-bold:    700;

  /* === LINE HEIGHTS === */
  --ldi-leading-tight:  1.1;   /* Display text, Bebas Neue */
  --ldi-leading-snug:   1.25;  /* Card titles */
  --ldi-leading-normal: 1.5;   /* Body copy */
  --ldi-leading-loose:  1.75;  /* Long-form text */

  /* === LETTER SPACING === */
  --ldi-tracking-tight:  -0.02em;  /* Bebas Neue large sizes */
  --ldi-tracking-normal:  0;
  --ldi-tracking-wide:    0.08em;  /* Small caps labels */
  --ldi-tracking-wider:   0.15em;  /* Breadcrumbs, status tags */
  --ldi-tracking-widest:  0.25em;  /* Accession numbers */
}
```

**Type Scale Usage Guide:**

```css
/* === DISPLAY — Bebas Neue, all-caps === */
.ldi-heading-hero {
  font-family: var(--ldi-font-display);
  font-size: clamp(3rem, 10vw, var(--ldi-text-5xl));
  line-height: var(--ldi-leading-tight);
  letter-spacing: var(--ldi-tracking-tight);
  text-transform: uppercase;
  color: var(--ldi-text-primary);
}

/* === ROOM TITLE — e.g. "YASURAGI GARDEN" === */
.ldi-heading-room {
  font-family: var(--ldi-font-display);
  font-size: clamp(2rem, 6vw, var(--ldi-text-4xl));
  line-height: var(--ldi-leading-tight);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ldi-text-primary);
}

/* === SECTION HEADING === */
.ldi-heading-section {
  font-family: var(--ldi-font-display);
  font-size: var(--ldi-text-xl);
  text-transform: uppercase;
  letter-spacing: var(--ldi-tracking-wide);
  color: var(--ldi-text-secondary);
}

/* === BODY COPY === */
.ldi-body {
  font-family: var(--ldi-font-body);
  font-size: var(--ldi-text-base);
  line-height: var(--ldi-leading-normal);
  font-weight: var(--ldi-weight-regular);
  color: var(--ldi-text-primary);
}

/* === DOSSIER / ACCESSION LABEL === */
.ldi-mono {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  color: var(--ldi-text-dim);
}

/* === JAPANESE VERTICAL TEXT === */
.ldi-japanese-vertical {
  font-family: var(--ldi-font-japanese);
  writing-mode: vertical-rl;
  text-orientation: mixed;
  font-size: var(--ldi-text-xl);
  font-weight: var(--ldi-weight-bold);
  letter-spacing: 0.1em;
  color: var(--ldi-text-secondary);
  opacity: 0.6;
}
```

#### 1.1.3 Spacing Scale

Base unit: `4px`. All spacing is multiples of 4.

```css
:root {
  --ldi-space-1:   0.25rem;   /*  4px */
  --ldi-space-2:   0.5rem;    /*  8px */
  --ldi-space-3:   0.75rem;   /* 12px */
  --ldi-space-4:   1rem;      /* 16px */
  --ldi-space-5:   1.25rem;   /* 20px */
  --ldi-space-6:   1.5rem;    /* 24px */
  --ldi-space-8:   2rem;      /* 32px */
  --ldi-space-10:  2.5rem;    /* 40px */
  --ldi-space-12:  3rem;      /* 48px */
  --ldi-space-16:  4rem;      /* 64px */
  --ldi-space-20:  5rem;      /* 80px */
  --ldi-space-24:  6rem;      /* 96px */
  --ldi-space-32:  8rem;      /* 128px */
  --ldi-space-48: 12rem;      /* 192px */
}
```

#### 1.1.4 Border Radius Scale

Attraction Dark uses **sharp corners as the default**. Radius is applied sparingly.

```css
:root {
  --ldi-radius-none: 0;
  --ldi-radius-sm:   2px;   /* Subtle softening — tags, status badges */
  --ldi-radius-md:   4px;   /* Cards with parchment backgrounds */
  --ldi-radius-pill: 999px; /* Only for pill-shaped status chips if needed */
}
```

#### 1.1.5 Shadow & Glow Tokens

```css
:root {
  /* === VOID SHADOW — darkness depth === */
  --ldi-shadow-sm:    0 1px 4px rgba(0,0,0,0.6);
  --ldi-shadow-md:    0 4px 16px rgba(0,0,0,0.8);
  --ldi-shadow-lg:    0 8px 32px rgba(0,0,0,0.9);
  --ldi-shadow-inset: inset 0 1px 0 rgba(255,255,255,0.03);

  /* === TEAL GLOW === */
  --ldi-glow-teal-sm:  0 0 8px var(--ldi-teal-glow);
  --ldi-glow-teal-md:  0 0 20px var(--ldi-teal-glow), 0 0 40px var(--ldi-teal-ghost);
  --ldi-glow-teal-lg:  0 0 40px var(--ldi-teal-glow-strong), 0 0 80px var(--ldi-teal-ghost);

  /* === AMBER GLOW === */
  --ldi-glow-amber-sm: 0 0 8px var(--ldi-amber-glow);
  --ldi-glow-amber-md: 0 0 20px var(--ldi-amber-glow), 0 0 40px rgba(212,130,10,0.10);
  --ldi-glow-amber-lg: 0 0 40px var(--ldi-amber-glow-strong);

  /* === CRIMSON GLOW === */
  --ldi-glow-crimson-sm: 0 0 8px var(--ldi-crimson-glow);
  --ldi-glow-crimson-md: 0 0 20px var(--ldi-crimson-glow);
}
```

#### 1.1.6 Texture Tokens

Textures are applied via CSS `::after` pseudo-elements or `background-image` layering. They should be subtle — opacity between 2–6%.

```css
:root {
  /* Grain: SVG noise filter rendered to data URI, or use a 200x200 PNG tile */
  --ldi-texture-grain: url('/assets/textures/grain-200.png');
  
  /* Scanlines: repeating horizontal lines at 2px interval */
  --ldi-texture-scanline: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 1px,
    rgba(0,0,0,0.15) 1px,
    rgba(0,0,0,0.15) 2px
  );

  /* Noise: SVG feTurbulence filter (applied via filter property) */
  --ldi-texture-noise-filter: url('#ldi-noise-filter');
}

/* === GRAIN OVERLAY MIXIN === */
.ldi-grain {
  position: relative;
  isolation: isolate;
}
.ldi-grain::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: var(--ldi-texture-grain);
  background-repeat: repeat;
  opacity: 0.04;
  pointer-events: none;
  z-index: 1;
  mix-blend-mode: overlay;
}

/* SVG noise filter (place in <defs> in a hidden SVG) */
/* <filter id="ldi-noise-filter">
     <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/>
     <feColorMatrix type="saturate" values="0"/>
     <feBlend in="SourceGraphic" mode="multiply"/>
   </filter> */
```

#### 1.1.7 Animation Tokens

```css
:root {
  /* === TIMING === */
  --ldi-duration-instant:  80ms;
  --ldi-duration-fast:     150ms;
  --ldi-duration-normal:   300ms;
  --ldi-duration-slow:     600ms;
  --ldi-duration-crawl:    1200ms;
  --ldi-duration-pulse:    2400ms;

  /* === EASING === */
  --ldi-ease-out:     cubic-bezier(0.0, 0.0, 0.2, 1.0);
  --ldi-ease-in:      cubic-bezier(0.4, 0.0, 1.0, 1.0);
  --ldi-ease-inout:   cubic-bezier(0.4, 0.0, 0.2, 1.0);
  --ldi-ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1.0);  /* slight overshoot */
  --ldi-ease-glitch:  steps(1, end);  /* stepped — for glitch effects */
}

/* === SIGNAL PULSE — for status dots and active indicators === */
@keyframes ldi-signal-pulse {
  0%, 100% { opacity: 1; box-shadow: var(--ldi-glow-teal-sm); }
  50%       { opacity: 0.4; box-shadow: none; }
}

/* === AMBER FLICKER — for FLICKERING status === */
@keyframes ldi-flicker {
  0%   { opacity: 1; }
  8%   { opacity: 0.8; }
  9%   { opacity: 1; }
  12%  { opacity: 0.7; }
  13%  { opacity: 1; }
  80%  { opacity: 1; }
  83%  { opacity: 0.6; }
  87%  { opacity: 1; }
  100% { opacity: 1; }
}

/* === GLITCH FRAME — text displacement === */
@keyframes ldi-glitch {
  0%   { clip-path: inset(0 0 95% 0); transform: translate(-2px, 0); }
  10%  { clip-path: inset(30% 0 50% 0); transform: translate(2px, 0); }
  20%  { clip-path: inset(60% 0 20% 0); transform: translate(-1px, 1px); }
  30%  { clip-path: inset(10% 0 80% 0); transform: translate(1px, -1px); }
  40%  { clip-path: inset(80% 0 5% 0); transform: translate(-2px, 0); }
  50%  { clip-path: inset(0 0 0 0); transform: translate(0); }
  100% { clip-path: inset(0 0 0 0); transform: translate(0); }
}

/* === ROOT GROWTH — for the deep garden network diagram === */
@keyframes ldi-root-grow {
  from { stroke-dashoffset: 1; }
  to   { stroke-dashoffset: 0; }
}

/* === FADE UP ENTRANCE === */
@keyframes ldi-fade-up {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

---

### 1.2 System B: GLASSHOUSE LIGHT

#### 1.2.1 Color Tokens

```css
/* === GLASSHOUSE SYSTEM — scoped to [data-system="glasshouse"] or .gs-* prefix === */
:root {
  /* === FOUNDATION === */
  --gs-void:         #0e1117;   /* Deep navy — hero/page background */
  --gs-surface-dark: #161b24;   /* Dark surface — header, footer */
  --gs-slate:        #2d3748;   /* Slate — section dividers, muted panels */
  --gs-sky:          #4a90a4;   /* Sky blue — active states, highlights */
  --gs-white:        #ffffff;
  --gs-off-white:    #f5f6f7;   /* Off-white — body background (light sections) */
  --gs-champagne:    #c8a96e;   /* Champagne gold — primary accent */
  --gs-champagne-dim:#9a7d4a;   /* Muted champagne — secondary accent */
  --gs-walnut:       #6b4c30;   /* Warm walnut brown */
  --gs-olive:        #5a6b3a;   /* Olive green */

  /* === TEXT === */
  --gs-text-dark:    #0e1117;   /* On light backgrounds */
  --gs-text-mid:     #4a5568;   /* Secondary on light */
  --gs-text-dim:     #718096;   /* Tertiary, captions */
  --gs-text-light:   #f5f6f7;   /* On dark backgrounds */
  --gs-text-muted-light: #a0aec0; /* Secondary on dark */

  /* === BORDERS === */
  --gs-border-dark:  rgba(255,255,255,0.08);   /* On dark backgrounds */
  --gs-border-light: rgba(0,0,0,0.10);         /* On light backgrounds */
  --gs-border-champagne: rgba(200,169,110,0.30);

  /* === STATUS BADGE COLORS === */
  --gs-status-complete:    #2d6a4f;   /* Complete — forest green */
  --gs-status-complete-bg: #d8f3dc;
  --gs-status-inprogress:    #1a4d7c;  /* In Progress — navy blue */
  --gs-status-inprogress-bg: #d6eaf8;
  --gs-status-upcoming:    #4a5568;   /* Upcoming — slate */
  --gs-status-upcoming-bg: #e2e8f0;
  --gs-status-atrisk:      #92400e;   /* At Risk — amber */
  --gs-status-atrisk-bg:   #fef3c7;
  --gs-status-blocked:     #7f1d1d;   /* Blocked — red */
  --gs-status-blocked-bg:  #fee2e2;
  --gs-status-onhold:      #374151;   /* On Hold — grey */
  --gs-status-onhold-bg:   #e5e7eb;

  /* === MATERIAL SURFACES (CSS backdrop-filter approach) === */
  --gs-material-frosted: rgba(255, 255, 255, 0.08);
  --gs-material-frosted-blur: blur(16px) saturate(180%);
  --gs-material-brushed: linear-gradient(135deg, #b8bcc8 0%, #d0d4dc 30%, #c4c8d4 60%, #b0b4c0 100%);
  --gs-material-warm: rgba(245, 246, 247, 0.95);
}
```

#### 1.2.2 Typography Tokens — Glasshouse

**Font Stack — Glasshouse Light**

| Role | Font | Source | Fallback |
|---|---|---|---|
| **All display + body** | Satoshi | Fontshare CDN | Inter, system-ui |
| **Monospace** | JetBrains Mono | Google Fonts | Consolas, monospace |

```html
<!-- Fontshare for Satoshi -->
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,600,700&display=swap" rel="stylesheet">
<!-- Google Fonts for JetBrains Mono -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

```css
:root {
  --gs-font-sans: 'Satoshi', 'Inter', system-ui, -apple-system, sans-serif;
  --gs-font-mono: 'JetBrains Mono', Consolas, monospace;

  /* === TYPE SCALE (from mockup design system sheet) === */
  --gs-h1-size:    2.5rem;    /* 40px */
  --gs-h1-leading: 3rem;      /* 48px */
  --gs-h1-weight:  600;

  --gs-h2-size:    1.75rem;   /* 28px */
  --gs-h2-leading: 2.25rem;   /* 36px */
  --gs-h2-weight:  600;

  --gs-h3-size:    1.25rem;   /* 20px */
  --gs-h3-leading: 1.75rem;   /* 28px */
  --gs-h3-weight:  600;

  --gs-body-size:    1rem;    /* 16px */
  --gs-body-leading: 1.5rem;  /* 24px */
  --gs-body-weight:  400;

  --gs-caps-size:    0.75rem; /* 12px */
  --gs-caps-leading: 1rem;    /* 16px */
  --gs-caps-weight:  500;

  /* === TRACKING === */
  --gs-tracking-caps:   0.12em;  /* Overline caps text */
  --gs-tracking-label:  0.06em;  /* Small labels */
  --gs-tracking-normal: 0;
}

/* === TYPE CLASSES === */
.gs-h1 {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-h1-size);
  line-height: var(--gs-h1-leading);
  font-weight: var(--gs-h1-weight);
  color: var(--gs-text-light);
}
.gs-h2 { font-size: var(--gs-h2-size); line-height: var(--gs-h2-leading); font-weight: var(--gs-h2-weight); }
.gs-h3 { font-size: var(--gs-h3-size); line-height: var(--gs-h3-leading); font-weight: var(--gs-h3-weight); }
.gs-body { font-size: var(--gs-body-size); line-height: var(--gs-body-leading); font-weight: var(--gs-body-weight); }
.gs-caps {
  font-size: var(--gs-caps-size);
  line-height: var(--gs-caps-leading);
  font-weight: var(--gs-caps-weight);
  letter-spacing: var(--gs-tracking-caps);
  text-transform: uppercase;
}
```

#### 1.2.3 Material Surface Patterns

The Glasshouse system uses three material metaphors as design vocabulary:

**Frosted Glass**
```css
.gs-frosted {
  background: var(--gs-material-frosted);
  backdrop-filter: var(--gs-material-frosted-blur);
  -webkit-backdrop-filter: var(--gs-material-frosted-blur);
  border: 1px solid var(--gs-border-dark);
}
```

**Brushed Metal**
```css
.gs-brushed-metal {
  background: var(--gs-material-brushed);
  position: relative;
  overflow: hidden;
}
.gs-brushed-metal::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    90deg,
    transparent 0px,
    rgba(255,255,255,0.03) 1px,
    transparent 2px
  );
}
```

**Soft Neutral**
```css
.gs-soft-neutral {
  background: var(--gs-material-warm);
  border: 1px solid var(--gs-border-light);
  box-shadow: 0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04);
}
```

---

<a name="section-2"></a>
## SECTION 2: COMPONENT LIBRARY — ATTRACTION DARK

All components use the `ldi-` prefix. Component HTML and CSS is provided for each.

---

### 2.1 Card Anatomy (Standard Dossier Card)

**Accession ID format:** `ACC. [ROOM CODE]-[###]`

Room codes:
| Room | Code |
|---|---|
| Midway / Home | MID |
| Bob's Fortune Emporium | BOB |
| Arcade | ARC |
| Museum | MUS |
| Chapel | CHP |
| Ghost's Workshop | GHW |
| Cathedral of Glitch | COG |
| Deep Garden | DGN |

**HTML Structure:**
```html
<article class="ldi-card" data-status="open">
  <div class="ldi-card__accession">ACC. BOB-001</div>
  <h3 class="ldi-card__title">Bob's Fortune Emporium</h3>
  <p class="ldi-card__description">
    Insert a question. Receive a fortune. Results are not guaranteed 
    to be accurate, useful, or emotionally appropriate.
  </p>
  <p class="ldi-card__flavor">
    "He has been repaired three times. He works perfectly. Probably."
  </p>
  <div class="ldi-card__footer">
    <span class="ldi-status" data-variant="open">OPEN</span>
  </div>
</article>
```

**CSS:**
```css
.ldi-card {
  background-color: var(--ldi-surface);
  border: 1px solid var(--ldi-border-amber);
  padding: var(--ldi-space-6);
  position: relative;
  isolation: isolate;
  transition: border-color var(--ldi-duration-normal) var(--ldi-ease-out),
              box-shadow var(--ldi-duration-normal) var(--ldi-ease-out);
}

/* Grain texture overlay */
.ldi-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: var(--ldi-texture-grain);
  opacity: 0.03;
  pointer-events: none;
  z-index: 1;
}

.ldi-card:hover {
  border-color: var(--ldi-amber-bright);
  box-shadow: var(--ldi-glow-amber-sm);
}

/* Teal-bordered variant (for signal/tech rooms) */
.ldi-card[data-theme="teal"] {
  border-color: var(--ldi-border-teal);
}
.ldi-card[data-theme="teal"]:hover {
  border-color: var(--ldi-teal-dim);
  box-shadow: var(--ldi-glow-teal-sm);
}

.ldi-card__accession {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  color: var(--ldi-text-dim);
  margin-bottom: var(--ldi-space-3);
}

.ldi-card__title {
  font-family: var(--ldi-font-display);
  font-size: var(--ldi-text-xl);
  line-height: var(--ldi-leading-tight);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ldi-text-primary);
  margin-bottom: var(--ldi-space-3);
}

.ldi-card__description {
  font-family: var(--ldi-font-body);
  font-size: var(--ldi-text-base);
  line-height: var(--ldi-leading-normal);
  color: var(--ldi-text-secondary);
  margin-bottom: var(--ldi-space-4);
}

.ldi-card__flavor {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  line-height: var(--ldi-leading-normal);
  color: var(--ldi-text-dim);
  font-style: italic;
  border-left: 2px solid var(--ldi-border-amber);
  padding-left: var(--ldi-space-3);
  margin-bottom: var(--ldi-space-5);
}

.ldi-card__footer {
  display: flex;
  align-items: center;
  gap: var(--ldi-space-3);
}
```

---

### 2.2 Status Tags

Eight canonical status states. All use the same base component; variant is set via `data-variant`.

**HTML:**
```html
<span class="ldi-status" data-variant="open">OPEN</span>
<span class="ldi-status" data-variant="active">ACTIVE</span>
<span class="ldi-status" data-variant="flickering">FLICKERING</span>
<span class="ldi-status" data-variant="unstable">UNSTABLE</span>
<span class="ldi-status" data-variant="denied">ACCESS DENIED</span>
<span class="ldi-status" data-variant="appointment">BY APPOINTMENT</span>
<span class="ldi-status" data-variant="coming">COMING SOON</span>
<span class="ldi-status" data-variant="prepared">PREPARED</span>
```

**CSS:**
```css
.ldi-status {
  display: inline-flex;
  align-items: center;
  gap: var(--ldi-space-2);
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  font-weight: var(--ldi-weight-bold);
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  padding: var(--ldi-space-1) var(--ldi-space-3);
  border: 1px solid currentColor;
  border-radius: var(--ldi-radius-sm);
}

/* Status indicator dot */
.ldi-status::before {
  content: '';
  display: block;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background-color: currentColor;
  flex-shrink: 0;
}

/* === VARIANT: OPEN === */
.ldi-status[data-variant="open"] {
  color: var(--ldi-status-open);
  border-color: var(--ldi-teal-dim);
  background: rgba(0, 229, 204, 0.06);
}
.ldi-status[data-variant="open"]::before {
  animation: ldi-signal-pulse var(--ldi-duration-pulse) ease-in-out infinite;
}

/* === VARIANT: ACTIVE === */
.ldi-status[data-variant="active"] {
  color: var(--ldi-status-active);
  border-color: rgba(76, 187, 106, 0.40);
  background: rgba(76, 187, 106, 0.06);
}
.ldi-status[data-variant="active"]::before {
  animation: ldi-signal-pulse var(--ldi-duration-pulse) ease-in-out infinite;
}

/* === VARIANT: FLICKERING === */
.ldi-status[data-variant="flickering"] {
  color: var(--ldi-status-flickering);
  border-color: rgba(240, 160, 32, 0.40);
  background: rgba(240, 160, 32, 0.06);
  animation: ldi-flicker 4s linear infinite;
}

/* === VARIANT: UNSTABLE === */
.ldi-status[data-variant="unstable"] {
  color: var(--ldi-status-unstable);
  border-color: rgba(224, 96, 26, 0.40);
  background: rgba(224, 96, 26, 0.06);
  animation: ldi-flicker 2.5s linear infinite;
}

/* === VARIANT: DENIED === */
.ldi-status[data-variant="denied"] {
  color: var(--ldi-status-denied);
  border-color: rgba(192, 40, 26, 0.40);
  background: rgba(192, 40, 26, 0.06);
}

/* === VARIANT: BY APPOINTMENT === */
.ldi-status[data-variant="appointment"] {
  color: var(--ldi-status-appointment);
  border-color: rgba(106, 90, 64, 0.40);
  background: rgba(106, 90, 64, 0.06);
}
.ldi-status[data-variant="appointment"]::before { display: none; }

/* === VARIANT: COMING SOON === */
.ldi-status[data-variant="coming"] {
  color: var(--ldi-status-coming);
  border-color: rgba(58, 50, 40, 0.80);
  background: rgba(58, 50, 40, 0.20);
}
.ldi-status[data-variant="coming"]::before { display: none; }

/* === VARIANT: PREPARED === */
.ldi-status[data-variant="prepared"] {
  color: var(--ldi-status-prepared);
  border-color: rgba(138, 120, 88, 0.40);
  background: rgba(138, 120, 88, 0.06);
}
```

---

### 2.3 Hero / Banner Anatomy

**HTML Structure:**
```html
<section class="ldi-hero" style="--hero-bg: url('/assets/backgrounds/deep-garden.webp')">
  <div class="ldi-hero__atmosphere"></div>
  <div class="ldi-hero__content">
    <div class="ldi-breadcrumb">
      <a href="/">HOME</a>
      <span>/</span>
      <a href="/midway">MIDWAY</a>
      <span>/</span>
      <span>DEEP GARDEN</span>
    </div>
    <div class="ldi-hero__room-context">SECTOR 03 · SUBTERRANEAN</div>
    <h1 class="ldi-hero__title">DEEP GARDEN</h1>
    <p class="ldi-hero__description">
      Below the attraction, something grows. The root map shows connections 
      the surface cannot explain.
    </p>
  </div>
  <!-- Optional ambient Japanese text element -->
  <div class="ldi-hero__japanese" aria-hidden="true">深き庭</div>
</section>
```

**CSS:**
```css
.ldi-hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding-bottom: var(--ldi-space-20);
  overflow: hidden;
  background-image: var(--hero-bg);
  background-size: cover;
  background-position: center;
}

/* Dark fade gradient — image visible at top, fades to void at bottom */
.ldi-hero__atmosphere {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(10, 9, 7, 0.0) 0%,
    rgba(10, 9, 7, 0.2) 30%,
    rgba(10, 9, 7, 0.6) 60%,
    rgba(10, 9, 7, 0.92) 80%,
    var(--ldi-void) 100%
  );
  pointer-events: none;
}

.ldi-hero__content {
  position: relative;
  z-index: 2;
  max-width: 960px;
  padding: 0 var(--ldi-space-8);
}

.ldi-hero__room-context {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  color: var(--ldi-teal-dim);
  margin-bottom: var(--ldi-space-3);
}

.ldi-hero__title {
  font-family: var(--ldi-font-display);
  font-size: clamp(3.5rem, 10vw, 8rem);
  line-height: var(--ldi-leading-tight);
  text-transform: uppercase;
  letter-spacing: -0.01em;
  color: var(--ldi-text-primary);
  margin-bottom: var(--ldi-space-6);
}

.ldi-hero__description {
  font-family: var(--ldi-font-body);
  font-size: var(--ldi-text-md);
  line-height: var(--ldi-leading-loose);
  color: var(--ldi-text-secondary);
  max-width: 560px;
}

/* Oversized ambient Japanese text — right edge, partially cropped */
.ldi-hero__japanese {
  position: absolute;
  right: -0.1em;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--ldi-font-japanese);
  font-size: clamp(6rem, 18vw, 16rem);
  font-weight: var(--ldi-weight-bold);
  writing-mode: vertical-rl;
  color: var(--ldi-text-primary);
  opacity: 0.06;
  pointer-events: none;
  user-select: none;
  z-index: 1;
}
```

---

### 2.4 Breadcrumb Pattern

```html
<nav class="ldi-breadcrumb" aria-label="Location">
  <a class="ldi-breadcrumb__item" href="/">HOME</a>
  <span class="ldi-breadcrumb__sep" aria-hidden="true">/</span>
  <a class="ldi-breadcrumb__item" href="/midway">MIDWAY</a>
  <span class="ldi-breadcrumb__sep" aria-hidden="true">/</span>
  <span class="ldi-breadcrumb__item ldi-breadcrumb__item--current" aria-current="page">DEEP GARDEN</span>
</nav>
```

```css
.ldi-breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--ldi-space-2);
  margin-bottom: var(--ldi-space-4);
}

.ldi-breadcrumb__item {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-wider);
  text-transform: uppercase;
  color: var(--ldi-text-dim);
  text-decoration: none;
  transition: color var(--ldi-duration-fast);
}

.ldi-breadcrumb__item:hover { color: var(--ldi-teal); }

.ldi-breadcrumb__item--current {
  color: var(--ldi-text-secondary);
  pointer-events: none;
}

.ldi-breadcrumb__sep {
  color: var(--ldi-text-ghost);
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  opacity: 0.6;
}
```

---

### 2.5 System Panels

Three states: nominal, alert, and redacted.

```html
<!-- NOMINAL STATE -->
<div class="ldi-system-panel" data-state="nominal">
  <div class="ldi-system-panel__header">
    <span class="ldi-system-panel__dot"></span>
    <span class="ldi-system-panel__label">SYSTEM STATUS</span>
  </div>
  <div class="ldi-system-panel__reading">ALL SYSTEMS NOMINAL</div>
  <div class="ldi-system-panel__sub">NO ANOMALIES DETECTED · LAST SCAN 00:04:12 AGO</div>
</div>

<!-- ALERT STATE -->
<div class="ldi-system-panel" data-state="alert">
  <div class="ldi-system-panel__header">
    <span class="ldi-system-panel__dot"></span>
    <span class="ldi-system-panel__label">SYSTEM STATUS</span>
  </div>
  <div class="ldi-system-panel__reading">ANOMALY DETECTED</div>
  <div class="ldi-system-panel__sub">3 SIGNALS UNRESOLVED · SECTOR 7 OFFLINE</div>
</div>

<!-- REDACTED / SECURE ACCESS STATE -->
<div class="ldi-system-panel" data-state="redacted">
  <div class="ldi-system-panel__header">
    <span class="ldi-system-panel__dot"></span>
    <span class="ldi-system-panel__label">CLEARANCE REQUIRED</span>
  </div>
  <div class="ldi-system-panel__reading">█████████ ███████</div>
  <div class="ldi-system-panel__sub">ACCESS LEVEL 4 · CONTENT REDACTED</div>
</div>
```

```css
.ldi-system-panel {
  border: 1px solid var(--ldi-border);
  padding: var(--ldi-space-4) var(--ldi-space-5);
  background: var(--ldi-surface-cool);
  font-family: var(--ldi-font-mono);
}

.ldi-system-panel__header {
  display: flex;
  align-items: center;
  gap: var(--ldi-space-2);
  margin-bottom: var(--ldi-space-2);
}

.ldi-system-panel__dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
}

.ldi-system-panel__label {
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  color: var(--ldi-text-dim);
}

.ldi-system-panel__reading {
  font-size: var(--ldi-text-base);
  letter-spacing: var(--ldi-tracking-wide);
  text-transform: uppercase;
  margin-bottom: var(--ldi-space-1);
}

.ldi-system-panel__sub {
  font-size: var(--ldi-text-xs);
  color: var(--ldi-text-dim);
  letter-spacing: var(--ldi-tracking-wider);
}

/* NOMINAL: teal */
.ldi-system-panel[data-state="nominal"] .ldi-system-panel__dot {
  background: var(--ldi-teal);
  box-shadow: var(--ldi-glow-teal-sm);
  animation: ldi-signal-pulse var(--ldi-duration-pulse) ease-in-out infinite;
}
.ldi-system-panel[data-state="nominal"] .ldi-system-panel__reading {
  color: var(--ldi-teal);
}

/* ALERT: amber */
.ldi-system-panel[data-state="alert"] {
  border-color: var(--ldi-amber-dim);
}
.ldi-system-panel[data-state="alert"] .ldi-system-panel__dot {
  background: var(--ldi-amber-bright);
  animation: ldi-flicker 3s linear infinite;
}
.ldi-system-panel[data-state="alert"] .ldi-system-panel__reading {
  color: var(--ldi-amber-bright);
}

/* REDACTED: crimson */
.ldi-system-panel[data-state="redacted"] {
  border-color: var(--ldi-crimson-dim);
}
.ldi-system-panel[data-state="redacted"] .ldi-system-panel__dot {
  background: var(--ldi-crimson);
}
.ldi-system-panel[data-state="redacted"] .ldi-system-panel__reading {
  color: var(--ldi-text-dim);
  letter-spacing: 0.3em;
}
```

---

### 2.6 Fortune Ticket

```html
<div class="ldi-fortune-ticket">
  <div class="ldi-fortune-ticket__border">
    <div class="ldi-fortune-ticket__header">
      <div class="ldi-fortune-ticket__accession">NO. F-████</div>
      <div class="ldi-fortune-ticket__title">BOB'S FORTUNE EMPORIUM</div>
      <div class="ldi-fortune-ticket__subtitle">ASK A QUESTION · INSERT COIN · RECEIVE FORTUNE</div>
    </div>
    <div class="ldi-fortune-ticket__divider">— ✦ —</div>
    <div class="ldi-fortune-ticket__body">
      <p class="ldi-fortune-ticket__fortune">
        The answer you seek is already known to you.<br>
        You are merely avoiding it.
      </p>
      <p class="ldi-fortune-ticket__note">Results are accurate within a margin of cosmic uncertainty.</p>
    </div>
    <div class="ldi-fortune-ticket__footer">
      <div class="ldi-fortune-ticket__seal">⬡ LDI ⬡</div>
    </div>
  </div>
</div>
```

```css
.ldi-fortune-ticket {
  background-color: var(--ldi-surface-parchment);
  color: var(--ldi-text-parchment);
  padding: var(--ldi-space-6);
  position: relative;
  max-width: 400px;
}

.ldi-fortune-ticket__border {
  border: 2px solid var(--ldi-gold);
  padding: var(--ldi-space-6);
  box-shadow: inset 0 0 0 4px var(--ldi-surface-parchment),
              inset 0 0 0 5px var(--ldi-gold-bright);
}

.ldi-fortune-ticket__accession {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  text-align: center;
  color: var(--ldi-gold);
  margin-bottom: var(--ldi-space-2);
}

.ldi-fortune-ticket__title {
  font-family: var(--ldi-font-display);
  font-size: var(--ldi-text-lg);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  text-align: center;
  color: var(--ldi-text-parchment);
  margin-bottom: var(--ldi-space-1);
}

.ldi-fortune-ticket__subtitle {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-wider);
  text-align: center;
  color: var(--ldi-gold);
  text-transform: uppercase;
}

.ldi-fortune-ticket__divider {
  text-align: center;
  color: var(--ldi-gold);
  margin: var(--ldi-space-5) 0;
  letter-spacing: 0.4em;
}

.ldi-fortune-ticket__fortune {
  font-family: var(--ldi-font-body);
  font-size: var(--ldi-text-md);
  line-height: var(--ldi-leading-loose);
  text-align: center;
  color: var(--ldi-text-parchment);
  font-style: italic;
  margin-bottom: var(--ldi-space-4);
}

.ldi-fortune-ticket__note {
  font-family: var(--ldi-font-mono);
  font-size: 0.55rem;
  letter-spacing: 0.05em;
  text-align: center;
  color: var(--ldi-gold);
  opacity: 0.7;
  text-transform: uppercase;
}

.ldi-fortune-ticket__footer { margin-top: var(--ldi-space-5); }

.ldi-fortune-ticket__seal {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-sm);
  text-align: center;
  letter-spacing: 0.3em;
  color: var(--ldi-gold);
  opacity: 0.8;
}
```

---

### 2.7 Cabinet Card (Arcade)

```html
<div class="ldi-cabinet-card" data-status="open">
  <div class="ldi-cabinet-card__accession">ACC. ARC-001</div>
  <h3 class="ldi-cabinet-card__name">TEMPORAL GAUNTLET</h3>
  <p class="ldi-cabinet-card__prompt">INSERT COIN TO CONTINUE</p>
  <div class="ldi-cabinet-card__meta">
    <span class="ldi-status" data-variant="open">OPEN</span>
    <span class="ldi-cabinet-card__players">1–2 PLAYERS</span>
  </div>
</div>
```

```css
.ldi-cabinet-card {
  background: var(--ldi-surface);
  border: 1px solid var(--ldi-teal-ghost);
  padding: var(--ldi-space-5);
  position: relative;
  box-shadow: var(--ldi-glow-teal-sm);
  transition: box-shadow var(--ldi-duration-normal) var(--ldi-ease-out);
}

.ldi-cabinet-card:hover {
  box-shadow: var(--ldi-glow-teal-md);
  border-color: var(--ldi-teal-dim);
}

.ldi-cabinet-card__accession {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  color: var(--ldi-text-dim);
  margin-bottom: var(--ldi-space-2);
}

.ldi-cabinet-card__name {
  font-family: var(--ldi-font-display);
  font-size: var(--ldi-text-xl);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--ldi-text-primary);
  margin-bottom: var(--ldi-space-3);
}

.ldi-cabinet-card__prompt {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-wide);
  color: var(--ldi-teal);
  text-transform: uppercase;
  animation: ldi-signal-pulse 1200ms ease-in-out infinite;
  margin-bottom: var(--ldi-space-4);
}

.ldi-cabinet-card__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ldi-cabinet-card__players {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-wider);
  color: var(--ldi-text-dim);
  text-transform: uppercase;
}
```

---

### 2.8 Case File Tile

```html
<div class="ldi-case-file" data-status="prepared">
  <div class="ldi-case-file__label">CASE FILE</div>
  <h3 class="ldi-case-file__title">THE THURSDAY INCIDENT</h3>
  <p class="ldi-case-file__description">
    Six witnesses. Fourteen unexplained temperature readings. 
    One missing accordion.
  </p>
  <div class="ldi-case-file__footer">
    <span class="ldi-status" data-variant="prepared">PREPARED</span>
    <span class="ldi-case-file__ref">REF: MUS-CASE-007</span>
  </div>
</div>
```

```css
.ldi-case-file {
  border: 1px solid var(--ldi-border);
  border-top: 3px solid var(--ldi-amber-dim);
  background: var(--ldi-surface);
  padding: var(--ldi-space-5);
  font-family: var(--ldi-font-mono);
}

.ldi-case-file__label {
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  color: var(--ldi-amber);
  text-transform: uppercase;
  margin-bottom: var(--ldi-space-2);
}

.ldi-case-file__title {
  font-family: var(--ldi-font-display);
  font-size: var(--ldi-text-lg);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ldi-text-primary);
  margin-bottom: var(--ldi-space-3);
}

.ldi-case-file__description {
  font-family: var(--ldi-font-body);
  font-size: var(--ldi-text-sm);
  line-height: var(--ldi-leading-normal);
  color: var(--ldi-text-secondary);
  margin-bottom: var(--ldi-space-4);
}

.ldi-case-file__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.ldi-case-file__ref {
  font-size: var(--ldi-text-xs);
  letter-spacing: var(--ldi-tracking-widest);
  color: var(--ldi-text-dim);
  text-transform: uppercase;
}
```

---

### 2.9 Environmental Data Widget

```html
<!-- DARK VARIANT (Attraction) -->
<div class="ldi-env-widget" data-theme="dark">
  <div class="ldi-env-widget__row">
    <div class="ldi-env-widget__reading">
      <span class="ldi-env-widget__icon">🌡</span>
      <span class="ldi-env-widget__value">62°F</span>
      <span class="ldi-env-widget__label">TEMP</span>
    </div>
    <div class="ldi-env-widget__reading">
      <span class="ldi-env-widget__icon">💧</span>
      <span class="ldi-env-widget__value">87%</span>
      <span class="ldi-env-widget__label">HUMIDITY</span>
    </div>
    <div class="ldi-env-widget__reading">
      <span class="ldi-env-widget__icon">⚡</span>
      <span class="ldi-env-widget__value">3.2mV</span>
      <span class="ldi-env-widget__label">SIGNAL</span>
    </div>
  </div>
</div>
```

```css
.ldi-env-widget {
  border: 1px solid var(--ldi-border);
  padding: var(--ldi-space-4);
  background: var(--ldi-surface-cool);
  display: inline-block;
}

.ldi-env-widget__row {
  display: flex;
  gap: var(--ldi-space-5);
}

.ldi-env-widget__reading {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--ldi-space-1);
}

.ldi-env-widget__icon {
  font-size: var(--ldi-text-base);
  filter: grayscale(0.3);
}

.ldi-env-widget__value {
  font-family: var(--ldi-font-mono);
  font-size: var(--ldi-text-md);
  font-weight: var(--ldi-weight-bold);
  color: var(--ldi-teal);
  letter-spacing: 0.04em;
}

.ldi-env-widget__label {
  font-family: var(--ldi-font-mono);
  font-size: 0.55rem;
  letter-spacing: var(--ldi-tracking-widest);
  text-transform: uppercase;
  color: var(--ldi-text-dim);
}
```

---

### 2.10 The Root Map / Network Diagram

The Root Map is the central visual on `/deep-garden`. It depicts all rooms connected by glowing root-circuit paths.

**Architecture:** SVG element with JavaScript-driven path animation. The SVG is inline in the HTML for CSS control.

**Node structure:**
```
             [MIDWAY]
            /    |    \
      [BOB]  [ARCADE]  [MUSEUM]
            \    |    /
         [CHAPEL] [WORKSHOP]
                |
          [CATHEDRAL]
                |
          [DEEP GARDEN] ← you are here
```

```html
<div class="ldi-root-map" aria-label="Attraction network diagram">
  <svg viewBox="0 0 800 600" class="ldi-root-map__svg" id="rootMapSvg">
    <defs>
      <!-- Glow filter for paths -->
      <filter id="teal-glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feComposite in="SourceGraphic" in2="blur" operator="over"/>
      </filter>
      <!-- Animated gradient along paths -->
      <linearGradient id="root-flow" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="var(--ldi-teal)" stop-opacity="0"/>
        <stop offset="50%" stop-color="var(--ldi-teal)" stop-opacity="1"/>
        <stop offset="100%" stop-color="var(--ldi-teal)" stop-opacity="0"/>
      </linearGradient>
    </defs>

    <!-- Background paths (dim, always visible) -->
    <g class="ldi-root-map__paths-bg">
      <path class="root-path" d="M400,80 C380,180 320,220 240,280" />
      <path class="root-path" d="M400,80 C400,180 400,220 400,300" />
      <!-- ... additional paths ... -->
    </g>

    <!-- Animated glow paths (rendered over background) -->
    <g class="ldi-root-map__paths-glow">
      <path class="root-path-glow" d="M400,80 C380,180 320,220 240,280" />
      <!-- ... -->
    </g>

    <!-- Room nodes -->
    <g class="ldi-root-map__nodes">
      <g class="root-node" data-room="midway" transform="translate(400,80)">
        <circle r="12" class="root-node__outer"/>
        <circle r="6" class="root-node__inner"/>
        <text class="root-node__label" y="28" text-anchor="middle">MIDWAY</text>
      </g>
      <!-- ... additional nodes for all 7 rooms + deep garden ... -->
    </g>
  </svg>
</div>
```

```css
.ldi-root-map {
  position: relative;
  width: 100%;
  max-width: 900px;
  margin: 0 auto;
}

.ldi-root-map__svg {
  width: 100%;
  height: auto;
  overflow: visible;
}

/* Background paths — dim, always shown */
.root-path {
  fill: none;
  stroke: var(--ldi-teal-dim);
  stroke-width: 1.5;
  opacity: 0.3;
}

/* Animated glow paths */
.root-path-glow {
  fill: none;
  stroke: var(--ldi-teal);
  stroke-width: 2.5;
  filter: url(#teal-glow);
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  pathLength: 1;
  animation: ldi-root-grow 2s var(--ldi-ease-out) forwards;
  opacity: 0.7;
}

/* Stagger animation per path using nth-of-type or JS-applied delays */
.root-path-glow:nth-of-type(2) { animation-delay: 0.3s; }
.root-path-glow:nth-of-type(3) { animation-delay: 0.6s; }
.root-path-glow:nth-of-type(4) { animation-delay: 0.9s; }
.root-path-glow:nth-of-type(5) { animation-delay: 1.2s; }
.root-path-glow:nth-of-type(6) { animation-delay: 1.5s; }
.root-path-glow:nth-of-type(7) { animation-delay: 1.8s; }

/* Nodes */
.root-node__outer {
  fill: var(--ldi-teal-ghost);
  stroke: var(--ldi-teal-dim);
  stroke-width: 1;
  transition: all var(--ldi-duration-normal);
}

.root-node__inner {
  fill: var(--ldi-teal);
  filter: url(#teal-glow);
  animation: ldi-signal-pulse var(--ldi-duration-pulse) ease-in-out infinite;
}

.root-node:hover .root-node__outer {
  fill: var(--ldi-teal-ghost);
  stroke: var(--ldi-teal);
  r: 16;
  box-shadow: var(--ldi-glow-teal-lg);
}

.root-node__label {
  font-family: var(--ldi-font-mono);
  font-size: 9px;
  fill: var(--ldi-text-secondary);
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

/* Current location — "you are here" variant */
.root-node[data-current="true"] .root-node__outer {
  stroke: var(--ldi-teal);
  stroke-width: 2;
}
.root-node[data-current="true"] .root-node__inner {
  fill: var(--ldi-teal);
  r: 8;
  animation: ldi-signal-pulse 800ms ease-in-out infinite;
}
```

**JavaScript (animate on scroll into view):**
```javascript
const rootMap = document.getElementById('rootMapSvg');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.querySelectorAll('.root-path-glow').forEach((path, i) => {
        path.style.animationDelay = `${i * 0.3}s`;
        path.classList.add('is-animating');
      });
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });
if (rootMap) observer.observe(rootMap);
```

---

### 2.11 Depth Transition Effect

The signature visual metaphor of `/deep-garden`: the page appears to descend from surface → underground. This is achieved through a layered section transition.

**HTML Structure:**
```html
<!-- Surface garden section (top) -->
<section class="ldi-depth-layer" data-depth="surface">
  <div class="ldi-depth-layer__bg" style="--bg: url('/assets/backgrounds/surface-garden.webp')"></div>
  <div class="ldi-depth-layer__content">
    <!-- Surface content: path, entrance, garden above ground -->
  </div>
  <!-- The transition — a cross-section crack/divider -->
  <div class="ldi-depth-transition"></div>
</section>

<!-- Underground section (below) -->
<section class="ldi-depth-layer" data-depth="underground">
  <div class="ldi-depth-layer__bg" style="--bg: url('/assets/backgrounds/deep-garden.webp')"></div>
  <div class="ldi-depth-layer__content">
    <!-- Deep content: root map, underground rooms -->
  </div>
</section>
```

```css
/* === DEPTH LAYERS === */
.ldi-depth-layer {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
}

.ldi-depth-layer__bg {
  position: absolute;
  inset: 0;
  background-image: var(--bg);
  background-size: cover;
  background-position: center;
}

/* SURFACE: bright, with teal lanterns */
.ldi-depth-layer[data-depth="surface"] .ldi-depth-layer__bg {
  filter: brightness(0.7) saturate(0.9);
}

/* UNDERGROUND: darker, cooler, root textures */
.ldi-depth-layer[data-depth="underground"] .ldi-depth-layer__bg {
  filter: brightness(0.4) saturate(1.2) hue-rotate(-5deg);
}

/* === THE TRANSITION LINE === */
.ldi-depth-transition {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  z-index: 10;
  /* Cross-section soil/root line visual */
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(20, 12, 5, 0.4) 40%,
    rgba(10, 8, 3, 0.95) 70%,
    var(--ldi-void-deep) 100%
  );
}

/* Jagged edge SVG mask approach for the soil cross-section */
.ldi-depth-transition::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 40px;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 40' preserveAspectRatio='none'%3E%3Cpath d='M0,20 Q60,0 120,20 T240,20 T360,20 T480,20 T600,20 T720,20 T840,20 T960,20 T1080,20 T1200,20 L1200,40 L0,40 Z' fill='rgba(20,12,5,0.6)'/%3E%3C/svg%3E") center/cover;
}

/* Underground section has root glow from above */
.ldi-depth-layer[data-depth="underground"]::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 200px;
  background: linear-gradient(
    to bottom,
    rgba(0, 40, 36, 0.4) 0%,
    transparent 100%
  );
  pointer-events: none;
  z-index: 2;
}
```

---

### 2.12 Japanese Typography Integration

**Vertical sidebar element (e.g., 安らぎ for Yasuragi Garden):**

```html
<aside class="ldi-jp-sidebar" aria-hidden="true">
  <span class="ldi-jp-sidebar__text" data-translation="Tranquility">安らぎ</span>
</aside>
```

```css
.ldi-jp-sidebar {
  position: fixed;       /* or absolute within relative parent */
  right: 2rem;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1;
  pointer-events: none;
  user-select: none;
}

.ldi-jp-sidebar__text {
  font-family: var(--ldi-font-japanese);
  font-size: clamp(1rem, 3vw, 2rem);
  font-weight: var(--ldi-weight-bold);
  writing-mode: vertical-rl;
  text-orientation: mixed;
  letter-spacing: 0.12em;
  color: var(--ldi-text-secondary);
  opacity: 0.35;
  display: block;
}

/* Alternative: large decorative background version */
.ldi-jp-bg {
  font-family: var(--ldi-font-japanese);
  font-size: clamp(8rem, 25vw, 20rem);
  font-weight: 700;
  writing-mode: vertical-rl;
  position: absolute;
  right: -0.05em;
  opacity: 0.04;
  color: var(--ldi-text-primary);
  pointer-events: none;
  user-select: none;
  line-height: 1;
}
```

**Kanji glossary for UI use:**

| Japanese | Romaji | Meaning | Context |
|---|---|---|---|
| 安らぎ | Yasuragi | Tranquility | Garden sections |
| 深き庭 | Fukaki niwa | Deep garden | /deep-garden hero |
| 守護者 | Shugosha | Guardian | Medallion, about page |
| 信号 | Shingō | Signal | Broadcasts section |
| 痕跡 | Konseki | Traces / Scars | Scars are Maps |
| 迷宮 | Meikyū | Labyrinth | Cathedral of Glitch |

---

<a name="section-3"></a>
## SECTION 3: COMPONENT LIBRARY — GLASSHOUSE LIGHT

All Glasshouse components use the `gs-` prefix.

---

### 3.1 Button Variants

```html
<!-- PRIMARY -->
<button class="gs-btn gs-btn--primary">
  Start a Project <span class="gs-btn__arrow">→</span>
</button>

<!-- SECONDARY -->
<button class="gs-btn gs-btn--secondary">
  View Our Work
</button>

<!-- TERTIARY (text link) -->
<a class="gs-btn gs-btn--tertiary" href="/work">
  See all case studies <span class="gs-btn__arrow">→</span>
</a>
```

```css
.gs-btn {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-body-size);
  font-weight: 600;
  letter-spacing: 0.01em;
  border-radius: 4px;
  cursor: pointer;
  transition: all 150ms ease;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  border: none;
}

/* PRIMARY — dark fill, champagne hover */
.gs-btn--primary {
  background: var(--gs-void);
  color: var(--gs-white);
  padding: 0.75rem 1.5rem;
  border: 1px solid var(--gs-void);
}
.gs-btn--primary:hover {
  background: var(--gs-champagne);
  border-color: var(--gs-champagne);
  color: var(--gs-void);
}
.gs-btn--primary:focus-visible {
  outline: 2px solid var(--gs-champagne);
  outline-offset: 2px;
}

/* SECONDARY — outline */
.gs-btn--secondary {
  background: transparent;
  color: var(--gs-void);
  padding: 0.75rem 1.5rem;
  border: 1.5px solid var(--gs-void);
}
.gs-btn--secondary:hover {
  background: var(--gs-void);
  color: var(--gs-white);
}

/* On dark backgrounds */
.gs-btn--secondary-light {
  color: var(--gs-white);
  border-color: rgba(255,255,255,0.3);
}
.gs-btn--secondary-light:hover {
  border-color: var(--gs-champagne);
  color: var(--gs-champagne);
}

/* TERTIARY — text link with arrow */
.gs-btn--tertiary {
  background: transparent;
  color: var(--gs-champagne);
  padding: 0.5rem 0;
  border-bottom: 1px solid transparent;
  border-radius: 0;
}
.gs-btn--tertiary:hover {
  border-bottom-color: var(--gs-champagne);
}

.gs-btn__arrow {
  transition: transform 150ms ease;
  display: inline-block;
}
.gs-btn:hover .gs-btn__arrow { transform: translateX(4px); }
```

---

### 3.2 Input Fields

```html
<!-- Text input -->
<div class="gs-field">
  <label class="gs-field__label" for="project-name">Project Name</label>
  <input class="gs-field__input" type="text" id="project-name" placeholder="What are we building?" />
</div>

<!-- Search input with icon -->
<div class="gs-field gs-field--search">
  <svg class="gs-field__icon" width="16" height="16" viewBox="0 0 16 16">
    <circle cx="7" cy="7" r="5" stroke="currentColor" stroke-width="1.5" fill="none"/>
    <path d="M11 11 L14 14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
  </svg>
  <input class="gs-field__input" type="search" placeholder="Search case studies..." />
</div>
```

```css
.gs-field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.gs-field__label {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-caps-size);
  font-weight: var(--gs-caps-weight);
  letter-spacing: var(--gs-tracking-caps);
  text-transform: uppercase;
  color: var(--gs-text-mid);
}

.gs-field__input {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-body-size);
  color: var(--gs-text-dark);
  background: var(--gs-white);
  border: 1.5px solid var(--gs-border-light);
  border-radius: 4px;
  padding: 0.625rem 0.875rem;
  transition: border-color 150ms ease, box-shadow 150ms ease;
  outline: none;
  width: 100%;
}

.gs-field__input:focus {
  border-color: var(--gs-champagne);
  box-shadow: 0 0 0 3px rgba(200,169,110,0.15);
}

.gs-field__input::placeholder { color: var(--gs-text-dim); }

.gs-field--search {
  position: relative;
}
.gs-field--search .gs-field__icon {
  position: absolute;
  left: 0.875rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--gs-text-dim);
  pointer-events: none;
}
.gs-field--search .gs-field__input {
  padding-left: 2.5rem;
}

/* Dark background variant */
.gs-field--dark .gs-field__input {
  background: rgba(255,255,255,0.05);
  border-color: var(--gs-border-dark);
  color: var(--gs-text-light);
}
.gs-field--dark .gs-field__input::placeholder { color: var(--gs-text-muted-light); }
.gs-field--dark .gs-field__input:focus {
  border-color: var(--gs-champagne);
  background: rgba(255,255,255,0.08);
}
```

---

### 3.3 Pills / Filter Tags

```html
<div class="gs-pills" role="group" aria-label="Filter by service">
  <button class="gs-pill gs-pill--active" data-filter="all">All</button>
  <button class="gs-pill" data-filter="strategy">Strategy</button>
  <button class="gs-pill" data-filter="design">Design</button>
  <button class="gs-pill" data-filter="build">Build</button>
  <button class="gs-pill" data-filter="operate">Operate</button>
</div>
```

```css
.gs-pills {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.gs-pill {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-caps-size);
  font-weight: var(--gs-caps-weight);
  letter-spacing: var(--gs-tracking-caps);
  text-transform: uppercase;
  padding: 0.375rem 0.875rem;
  border-radius: 999px;
  cursor: pointer;
  transition: all 120ms ease;
  background: transparent;
  color: var(--gs-text-mid);
  border: 1.5px solid var(--gs-border-light);
}

.gs-pill:hover {
  background: var(--gs-off-white);
  border-color: var(--gs-text-mid);
  color: var(--gs-text-dark);
}

.gs-pill--active {
  background: var(--gs-void);
  color: var(--gs-white);
  border-color: var(--gs-void);
}

.gs-pill--active:hover {
  background: var(--gs-champagne);
  border-color: var(--gs-champagne);
  color: var(--gs-void);
}
```

---

### 3.4 Status Badges (Glasshouse)

```html
<span class="gs-badge" data-status="complete">Complete</span>
<span class="gs-badge" data-status="in-progress">In Progress</span>
<span class="gs-badge" data-status="upcoming">Upcoming</span>
<span class="gs-badge" data-status="at-risk">At Risk</span>
<span class="gs-badge" data-status="blocked">Blocked</span>
<span class="gs-badge" data-status="on-hold">On Hold</span>
```

```css
.gs-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-family: var(--gs-font-sans);
  font-size: var(--gs-caps-size);
  font-weight: var(--gs-caps-weight);
  letter-spacing: 0.04em;
  padding: 0.25rem 0.625rem;
  border-radius: 999px;
}

.gs-badge::before {
  content: '';
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: currentColor;
  flex-shrink: 0;
}

.gs-badge[data-status="complete"]    { color: var(--gs-status-complete);    background: var(--gs-status-complete-bg); }
.gs-badge[data-status="in-progress"] { color: var(--gs-status-inprogress);   background: var(--gs-status-inprogress-bg); }
.gs-badge[data-status="upcoming"]    { color: var(--gs-status-upcoming);     background: var(--gs-status-upcoming-bg); }
.gs-badge[data-status="at-risk"]     { color: var(--gs-status-atrisk);       background: var(--gs-status-atrisk-bg); }
.gs-badge[data-status="blocked"]     { color: var(--gs-status-blocked);      background: var(--gs-status-blocked-bg); }
.gs-badge[data-status="on-hold"]     { color: var(--gs-status-onhold);       background: var(--gs-status-onhold-bg); }
```

---

### 3.5 Service Tiles

```html
<a class="gs-service-tile" href="/work/strategy">
  <div class="gs-service-tile__icon">
    <!-- Phosphor Icon: Compass -->
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <circle cx="12" cy="12" r="10"/>
      <path d="M16.24 7.76L14.12 14.12L7.76 16.24L9.88 9.88L16.24 7.76Z"/>
    </svg>
  </div>
  <div class="gs-service-tile__body">
    <h3 class="gs-service-tile__title">Strategy</h3>
    <p class="gs-service-tile__description">
      Product thinking, go-to-market alignment, and clarity sessions 
      that set the direction before a line of code is written.
    </p>
  </div>
  <span class="gs-service-tile__arrow">→</span>
</a>
```

```css
.gs-service-tile {
  display: flex;
  align-items: flex-start;
  gap: 1.25rem;
  padding: 1.5rem;
  border: 1.5px solid var(--gs-border-light);
  border-radius: 8px;
  text-decoration: none;
  background: var(--gs-white);
  transition: all 200ms ease;
  position: relative;
}

.gs-service-tile:hover {
  border-color: var(--gs-champagne);
  box-shadow: 0 4px 16px rgba(200,169,110,0.12);
  transform: translateY(-1px);
}

.gs-service-tile__icon {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--gs-off-white);
  border-radius: 8px;
  color: var(--gs-champagne);
  flex-shrink: 0;
  transition: background 200ms ease;
}

.gs-service-tile:hover .gs-service-tile__icon {
  background: rgba(200,169,110,0.12);
}

.gs-service-tile__body { flex: 1; }

.gs-service-tile__title {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-h3-size);
  font-weight: var(--gs-h3-weight);
  color: var(--gs-text-dark);
  margin-bottom: 0.375rem;
}

.gs-service-tile__description {
  font-size: var(--gs-body-size);
  line-height: var(--gs-body-leading);
  color: var(--gs-text-mid);
}

.gs-service-tile__arrow {
  color: var(--gs-champagne);
  font-size: 1.25rem;
  align-self: center;
  transition: transform 200ms ease;
}
.gs-service-tile:hover .gs-service-tile__arrow { transform: translateX(4px); }
```

---

### 3.6 Stat Chips

```html
<div class="gs-stat-chips">
  <div class="gs-stat-chip">
    <span class="gs-stat-chip__value">47</span>
    <span class="gs-stat-chip__label">Projects Delivered</span>
  </div>
  <div class="gs-stat-chip">
    <span class="gs-stat-chip__value">12</span>
    <span class="gs-stat-chip__label">Active Clients</span>
  </div>
  <div class="gs-stat-chip">
    <span class="gs-stat-chip__value">98%</span>
    <span class="gs-stat-chip__label">On Schedule</span>
  </div>
</div>
```

```css
.gs-stat-chips {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.gs-stat-chip {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 1rem 1.5rem;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--gs-border-dark);
  border-radius: 6px;
  text-align: center;
  min-width: 120px;
}

.gs-stat-chip__value {
  font-family: var(--gs-font-sans);
  font-size: 2rem;
  font-weight: 700;
  color: var(--gs-champagne);
  line-height: 1;
}

.gs-stat-chip__label {
  font-family: var(--gs-font-sans);
  font-size: var(--gs-caps-size);
  font-weight: var(--gs-caps-weight);
  letter-spacing: var(--gs-tracking-caps);
  text-transform: uppercase;
  color: var(--gs-text-muted-light);
}
```

---

### 3.7 Material Swatches Reference

Seven material cards from the design system mockup. These are reference tiles, not interactive components — they inform the designer/developer which material language to apply where.

| # | Swatch | CSS Background | Use Context |
|---|---|---|---|
| 1 | **Frosted Glass** | `rgba(255,255,255,0.08)` + `backdrop-filter: blur(16px)` | Modals, overlays, sticky header on scroll |
| 2 | **Brushed Silver** | Linear gradient `#b8bcc8 → #d0d4dc → #c4c8d4 → #b0b4c0` | Reception desk, accent furniture, dividers |
| 3 | **Warm Light Walnut** | `#6b4c30` base with grain overlay | Accent panels, botanical sections |
| 4 | **Living Botanicals** | Image-backed panels with `#2d4a2d` overlay | Services with organic/growth metaphors |
| 5 | **Soft White Paper** | `#f5f6f7` with very subtle grain | Document previews, intake form backgrounds |
| 6 | **Pale Blue Enamel** | `#c8dce8` | Tag highlights, subtle accent fills |
| 7 | **Champagne Brass** | `linear-gradient(135deg, #c8a96e, #d4b87a, #b8934a)` | CTA buttons, divider lines, icon fills |

---

<a name="section-4"></a>
## SECTION 4: THE ASSET PIPELINE

### 4.1 Photography / AI-Generated Hero Backgrounds

All hero images should be generated at **2880×1800px minimum** (2× retina 1440px wide), saved as WebP at 85% quality. Deliver a 1440×900 standard and 768×1024 mobile crop per image.

| Page | Description | Status | Priority |
|---|---|---|---|
| `/` | Rain-slicked attraction courtyard at night, warm amber signage, distant structures in mist | DONE | — |
| `/deep-garden` | Underground root cavern: massive stone lantern, bioluminescent teal roots, carved stone archways, deep darkness beyond | NEEDED | P0 |
| `/museum` | Dark Victorian archway, taxidermy shadows, display cases with amber glow, dust motes | NEEDED | P0 |
| `/fortune` | Bob's Fortune Emporium interior: neon signs, carnival velvet, the cabinet glowing in amber | NEEDED | P0 |
| `/arcade` | Arcade hallway, cabinets glowing teal and amber, low ceiling with exposed pipes, fog from floor | NEEDED | P1 |
| `/chapel` | Small roadside wedding chapel at dusk, highway in background, single lantern, weathered wood | NEEDED | P1 |
| `/workshop` | Ghost's Workshop: workbench with tools, signal equipment, blue-white sparks, blueprint papers | NEEDED | P1 |
| `/cathedral` | Cathedral of Glitch: massive stone interior with glitch artifacts, corrupted light, fractured arches | NEEDED | P1 |
| `/broadcasts` | Broadcast tower at night, storm clouds, signal waves visualized as light arcs, very dark | NEEDED | P2 |
| `/about` | Abstract atmospheric — candlelight, old papers, a figure in silhouette, Pantheon energy | NEEDED | P2 |
| `/work` (Glasshouse) | Real architectural photography of a glass studio interior, brushed steel, bonsai on a desk, warm daylight | NEEDED | P0 |

**Naming convention:** `/assets/backgrounds/[page-slug]-hero.webp`  
**Mobile crop:** `/assets/backgrounds/[page-slug]-hero-mobile.webp`

---

### 4.2 Icon Set

**Attraction Dark:** No icon library — use custom SVG icons only. The dossier aesthetic resists generic icon libraries. Each icon should look hand-drawn or technical (like a scientific illustration or military schematic).

Custom SVG icons needed (build as a sprite or inline):
- Signal wave
- Skull (Bob Approved)
- Raven/bird silhouette
- Root/branch node
- Lantern
- Compass rose
- Coin insert
- Waveform
- Redacted/classified stamp
- Fortune wheel

**Glasshouse Light:** Use [Phosphor Icons](https://phosphoricons.com/) — Duotone weight, `stroke-width: 1.5`. Specific icons from mockup:

| Usage | Phosphor Name |
|---|---|
| Strategy | `Compass` |
| Design | `PencilLine` |
| Build | `Code` |
| Operate | `Gear` |
| System/Settings | `Sliders` |
| Leaf/Botanical | `Leaf` |
| Chart/Data | `ChartBar` |
| Shield/Trust | `Shield` |
| Check/Complete | `CheckCircle` |
| Warning | `Warning` |
| Calendar | `Calendar` |
| Person | `User` |

```bash
npm install @phosphor-icons/react
# or
npm install @phosphor-icons/web
```

---

### 4.3 Texture Assets

All textures are tiny tiling images or CSS/SVG solutions. Prefer CSS where possible.

| Texture | Method | File | Size | Opacity |
|---|---|---|---|---|
| Film grain | 200×200px PNG, noise pattern, repeat | `/assets/textures/grain-200.png` | 4KB | 3–5% |
| Scanlines | CSS `repeating-linear-gradient` | CSS-only | — | 8–12% |
| Paper noise | SVG `feTurbulence` filter | Inline SVG | — | 4–6% |
| Parchment grain | 400×400px aged paper scan | `/assets/textures/parchment-400.png` | 16KB | 8–15% |

**Grain texture generation (GIMP or Photoshop):**
- New 200×200px image, black fill
- Add Noise: Gaussian, 40%, monochromatic
- Export as PNG, maximize compression
- Reference in CSS as a background-image tile

**SVG noise filter (inline, paste into HTML):**
```html
<svg style="display:none" aria-hidden="true">
  <defs>
    <filter id="ldi-grain-filter">
      <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" 
                    stitchTiles="stitch" result="noise"/>
      <feColorMatrix type="saturate" values="0" in="noise" result="grey"/>
      <feBlend in="SourceGraphic" in2="grey" mode="overlay"/>
    </filter>
  </defs>
</svg>
```

---

### 4.4 Typography Loading

**Attraction Dark:**

```html
<!-- Preconnect -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<!-- Load all Attraction Dark fonts in one request -->
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Noto+Serif+JP:wght@400;600;700&display=swap" rel="stylesheet">
```

**Glasshouse Light:**

```html
<!-- Satoshi from Fontshare -->
<link rel="preconnect" href="https://api.fontshare.com">
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@300,400,500,600,700&display=swap" rel="stylesheet">

<!-- JetBrains Mono from Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

**Performance note:** Both systems should use `font-display: swap`. Bebas Neue and Satoshi are the two highest-priority loads — they're the most visually distinctive and should be preloaded for above-the-fold content.

```html
<!-- Critical font preload (Attraction Dark) -->
<link rel="preload" href="https://fonts.gstatic.com/s/bebasneue/..." as="font" type="font/woff2" crossorigin>
```

---

<a name="section-5"></a>
## SECTION 5: SITE-SPECIFIC IMPLEMENTATION NOTES

### 5.1 Gap Analysis

| Page | Current State (assumed) | Mockup Target | Gap | Highest-Impact Change |
|---|---|---|---|---|
| `/` (Homepage) | Basic hero, navigation | Rain-slicked hero, system panel, room navigation grid | MEDIUM | Add cinematic hero image with gradient fade; add atmospheric system status panel |
| `/deep-garden` | Placeholder or minimal | Full depth transition + root map + environmental widgets | HIGH | Build the depth section transition and root map SVG |
| `/museum` | Minimal | Dark archway hero, case file tiles | MEDIUM | Replace hero background; add case file tile layout |
| `/fortune` | Minimal | Fortune ticket component, Bob cabinet card, insert-coin interaction | HIGH | Build Fortune Ticket + Cabinet Card components; add coin-insert animation |
| `/arcade` | Minimal | Cabinet cards grid with teal glow, insert coin animations | MEDIUM | Implement cabinet card component; add teal glow CSS |
| `/chapel` | Minimal | Atmospheric dusk photography, appointment-only status panel | LOW | New hero image; status panel |
| `/workshop` | Minimal | Signal panels, system status widgets, environmental data | MEDIUM | Add system panels + environmental data widgets |
| `/cathedral` | Minimal | Glitch animations, redacted panels, ACCESS DENIED status | HIGH | Implement glitch keyframe animations; add redacted panel component |
| `/broadcasts` | Minimal | Signal waveform animation, broadcast tower hero | MEDIUM | Add waveform CSS animation; new hero image |
| `/work` (Glasshouse) | Unknown | Full Glasshouse Light design system | HIGH | Build the complete Glasshouse system from scratch — separate CSS scope |

---

### 5.2 The Depth Effect on `/deep-garden`

**Implementation steps:**

1. **Section order in HTML:** Surface section → transition divider → Underground section. Use `position: sticky` on the transition element for a continuous scroll reveal.

2. **Parallax on background images:** Surface image scrolls at `0.6×` viewport scroll rate; underground image at `1.0×`. Achieved with:
   ```javascript
   window.addEventListener('scroll', () => {
     const y = window.scrollY;
     document.querySelector('.surface-bg').style.transform = `translateY(${y * 0.4}px)`;
   });
   ```

3. **The cross-section line:** A thin 1px amber line with root-texture SVG decoration serves as the geological stratum boundary between surface and underground. It should be approximately `40–80px` tall, full-width.

4. **Color temperature shift:** Surface section uses `filter: brightness(0.7) saturate(0.8)`. Underground uses `filter: brightness(0.4) saturate(1.3) hue-rotate(-8deg)` — making underground visually cooler and more saturated.

5. **Root glow from above:** In the underground section, a radial gradient emanates from the ceiling simulating the teal glow coming through the ground.

---

### 5.3 The Root Map on `/deep-garden`

**Build order:**
1. Design the node positions for all 8 rooms in a 800×600 SVG viewport
2. Plot the path curves (cubic bezier) between nodes to look organic, not geometric
3. Assign `pathLength="1"` and `stroke-dasharray="1"` to all paths
4. Animate `stroke-dashoffset` from 1 → 0 as the map enters the viewport (IntersectionObserver)
5. Add pulsing dots that travel along the paths (use `animateMotion` SVG element)
6. Make each node clickable — it navigates to the room URL

**Animated signal dot traveling a path:**
```html
<circle r="3" fill="var(--ldi-teal)" opacity="0.8" filter="url(#teal-glow)">
  <animateMotion dur="4s" repeatCount="indefinite" path="M400,80 C380,180 320,220 240,280"/>
</circle>
```

---

### 5.4 Animation Priorities

Ordered by visual impact vs. implementation cost:

| Priority | Animation | Element | Implementation | Impact |
|---|---|---|---|---|
| 1 | Status dot pulse | All `.ldi-status` dots | CSS keyframe — already defined | HIGH / LOW cost |
| 2 | Card entrance (fade-up) | All `.ldi-card` | IntersectionObserver + `ldi-fade-up` keyframe | HIGH / LOW cost |
| 3 | Flicker on FLICKERING status | `.ldi-status[data-variant="flickering"]` | CSS keyframe — already defined | HIGH / LOW cost |
| 4 | Hero title entrance | `.ldi-hero__title` | `ldi-fade-up` with 0.2s delay | MEDIUM / LOW cost |
| 5 | Signal feed waveform | Broadcasts page | CSS animation on SVG path or Canvas | MEDIUM / MEDIUM cost |
| 6 | Root map growth | `/deep-garden` | SVG `stroke-dashoffset` + IntersectionObserver | HIGH / MEDIUM cost |
| 7 | Glitch text effect | Cathedral of Glitch elements | CSS `ldi-glitch` keyframe — use sparingly | MEDIUM / MEDIUM cost |
| 8 | Fortune coin insert | `/fortune` page | Click event → coin animation → fortune reveal | HIGH / MEDIUM cost |
| 9 | Depth parallax | `/deep-garden` sections | Scroll listener + `transform: translateY` | HIGH / HIGH cost |
| 10 | Signal dot traveling paths | Root map | SVG `<animateMotion>` | MEDIUM / MEDIUM cost |

**`prefers-reduced-motion` rule — mandatory:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

<a name="section-6"></a>
## SECTION 6: THE MERCH ASSET PRODUCTION GUIDE

### 6.1 Enamel Pin Specifications

Production note: Standard hard enamel pins use 4–8 spot colors. Complex gradients must be simplified to flat fills. Each design needs a vector master (Adobe Illustrator .AI or .EPS) plus a 3D photorealistic mockup for marketing.

| # | Title | Tagline | Visual Description | Dimensions | Color Count | Notes |
|---|---|---|---|---|---|---|
| 1 | **Attraction Operations** | "Keeping Reality Tourist Friendly Since 1978" | Full LDI attraction landscape (Bob's, Arcade, Cathedral, Warehouse), roadside sign style, sunset palette | 50×35mm (wide) | 6 | Skyline scene — widest format for layout |
| 2 | **Artifact Recovery Team** | "If Found Do Not Lick" | Wooden crate with warning labels and stickers, rope binding, hazard markings | 35×38mm (portrait) | 5 | Bold warning palette: orange + black |
| 3 | **Signal Integrity Division** | "Coherence First" | Hexagonal badge with signal waveform, vintage electronics aesthetic | 35×35mm (hex) | 4 | Custom hexagonal die shape |
| 4 | **Crossroads Ranger Station** | "All Paths Lead Somewhere" | Directional sign post (Reality/Memory/Possibility/Nowhere), raven perched on top, bonsai base | 35×50mm (tall) | 6 | Black + amber + green enamel |
| 5 | **Bob Approved** | "Repaired Three Times Works Perfectly Probably" | Grinning skull in flat cap, approval stamp overlay | 30×35mm | 4 | Round-ish shape; warm amber |
| 6 | **Deep Garden Ranger Division** | "Scars Are Maps" | Park ranger badge shape, bonsai + raven silhouette, teal + deep green | 38×42mm (shield) | 5 | Shield die shape; premium finish |
| 7 | **Cosmic Selector** | "You Didn't Spin It, It Spun You" | Orbital ring / roulette wheel, cosmic purple/violet | 38×38mm (round) | 5 | Soft enamel acceptable for gradients |
| 8 | **Thursday Night Dance Committee** | "Attendance Mandatory For Bigfoot" | Bigfoot dancing under UFO beam, jukebox at side, northern lights background | 40×40mm (round) | 7 | Most complex — soft enamel recommended |

**Delivery spec per pin:**
- Vector master: Adobe Illustrator, outline strokes, no live effects
- Colors: Pantone Solid Coated references (e.g., PMS 320C for teal)
- Die line: on a separate "Die" layer, 0.5pt stroke, no fill
- Resolution: 300 DPI minimum for any raster elements
- File format: `.AI` primary, `.EPS` backup, `.PNG` marketing mockup at 3000px wide

---

### 6.2 Sticker Pack Specifications

**Pack concept: "Attraction Permit Pack" — 8 designs on a single 6×8" perforated sheet**

Printing spec: Waterproof vinyl, matte laminate, die-cut with 1/16" bleed. Print at 300 DPI.

| # | Title | Concept | Size | Shape | Color Palette |
|---|---|---|---|---|---|
| 1 | **Ghost Was Here** | Classic "Kilroy Was Here" parody with LDI ghost | 80×60mm | Rectangle | Black + white + single cyan accent |
| 2 | **Employee of the Month** | Fake award certificate: "Nominated by: Unknown · Reason: Unclear" | 70×90mm | Portrait rect | Aged parchment + amber |
| 3 | **Scenic Overlook** | Retro national parks badge: "Lithium Dreams — Established ???" | 70×70mm | Round | Green + cream + brown |
| 4 | **Bob Approved** | Circular approval stamp, red ink on white | 60×60mm | Round | Red + white only |
| 5 | **Cathedral of Glitch** | Warning sign format: "SEMANTIC REALITY MAY SHIFT" | 80×80mm | Octagon | Red + white (sign aesthetic) |
| 6 | **Out of Order** | Hotel door hanger style: "PLEASE DO NOT ATTEMPT ENTRY / REALITY UNDER MAINTENANCE" | 50×120mm | Door hanger | Black + amber |
| 7 | **Thank You Please Come Again** | Receipt-style: itemized list of "purchases" (Wonder × 1, Disorientation × 2, etc.) | 65×100mm | Receipt | Black on white, thermal printer aesthetic |
| 8 | **Cosmic Selector** | Minimal: orbital ring, one line "YOU DIDN'T CHOOSE IT" | 60×60mm | Round | Deep purple + white |

---

### 6.3 Large Format Stickers

**"The Attraction Is Camouflage — Look Again"**
- Visual: Full LDI campus in landscape format (Bob's Crossroads Arcade, Cathedral of Glitch, Gift Shop Everywhere, Glitch Containment Warehouse 13), like a vintage tourist postcard
- Size: 200×75mm (wide landscape panorama)
- Shape: Rectangle with rounded corners (4mm radius)
- Print: Vinyl, matte laminate, UV-resistant inks
- File: 200mm × 75mm at 300 DPI = 2362 × 886px minimum
- Artwork reference: The mockup "Attraction Is Camouflage" landscape scene

**"Scars Are Maps" Kintsugi Medallion**
- Visual: Circular cracked stone/ceramic disc with gold kintsugi repair lines, stone lantern silhouette, raven, Japanese text (守護者 / 深き庭)
- Size: 90×90mm (round)
- Shape: Perfect circle die-cut
- Print: Holographic vinyl option for the gold repair lines
- File: 90mm at 300 DPI = 1063px
- Special effect: Consider gold foil or holographic overlay for kintsugi lines

---

### 6.4 Bob Fortune Dispenser

**Fabrication from Dimensional Drawings:**

The mockup provides a complete dimensional blueprint. Key specs for fabrication:

| Dimension | Value |
|---|---|
| Cabinet width | 27¾" (70.5cm) |
| Cabinet height | 75½" (191.8cm) |
| Approximate depth | ~18" (46cm) — standard Zoltar depth |
| Head mechanism | Servo-controlled skull, mounted on articulated neck |
| Display | Backlit panel for fortune readout |
| Coin mechanism | Standard 25¢ coin acceptor |
| Housing material | MDF cabinet with fiberglass or cast resin head |

**Digital Collectible / Print Approach:**

The 3D photorealistic render of Bob constitutes a high-fidelity digital asset. Usage:
- **Print-on-demand:** The render can be used as art for framed prints, sold via the attraction (physical or digital store)
- **Digital collectible:** The blueprint drawings + render + fortune database = a complete "Bob Dossier" digital item
- **Physical mini-edition:** A 1:6 scale desktop resin figure using the 3D model exported to STL, produced via Shapeways or local resin printing
- The 3D model (not included in current mockups) should be modeled in Blender from the dimensional drawings

---

<a name="section-7"></a>
## SECTION 7: THE COMFYUI WORKFLOW FOR SITE ASSETS

### 7.1 Recommended Models

| Use Case | Model | Rationale |
|---|---|---|
| Page hero backgrounds (atmospheric, cinematic) | **FLUX.1 Dev** | Best-in-class photorealism, excellent prompt adherence, strong lighting control |
| Enamel pin illustrations (stylized 3D render aesthetic) | **SDXL 1.0 + DreamShaper XL** | Better stylized rendering, more control over illustration aesthetics |
| Cinematic scene assets (Bigfoot/arcade/UFO) | **FLUX.1 Dev** or **Midjourney via API** | FLUX for prompting control; MJ for painterly/cinematic quality |
| Portrait renders (character, warden figure) | **FLUX.1 Dev + IP-Adapter face** | Consistent character + photorealism |
| Japanese aesthetic elements | **SDXL + AOM3 (AsianOpenMix)** | Better training on Japanese architectural/garden aesthetics |

**Node workflow:** Use ComfyUI with the standard KSampler node graph. Recommended: FLUX via the Comfy FLUX workflow template.

---

### 7.2 Atmospheric Hero Background Prompts

**Positive prompt template:**
```
cinematic atmospheric photography, [LOCATION DESCRIPTION], 
night scene, volumetric fog, bioluminescent [COLOR] lighting,
rain-slicked surfaces, deep shadows, warm amber practical lights,
teal lantern glow, overgrown stone architecture, 
Japanese garden elements, dark forest atmosphere,
8K ultra-detailed, anamorphic lens, shallow depth of field,
moody, noir, slightly surreal, hyperrealistic
```

**Per-page substitutions:**

| Page | `[LOCATION DESCRIPTION]` | Primary Light Color |
|---|---|---|
| `/deep-garden` | underground root cavern, massive stone lantern, bioluminescent root network growing through carved stone walls, deep darkness beyond | Teal (`[COLOR]: teal`) |
| `/museum` | Victorian curiosity museum interior at night, dark wooden display cases, amber glass specimen jars, dust motes in lantern light | Amber |
| `/fortune` | carnival fortune teller booth interior, velvet curtains, neon sign glow, crystal ball on ornate table, warm amber | Amber/Gold |
| `/arcade` | 1980s arcade hallway, glowing cabinet screens teal and amber, low ceiling with steam pipes, fog machine mist on floor | Teal |
| `/chapel` | small roadside wedding chapel at dusk, worn wooden interior, single candle on altar, highway visible through window | Warm Gold |
| `/workshop` | inventor's workshop, signal equipment workbench, blue electrical sparks, blueprint papers, bonsai on windowsill | Blue-White |
| `/cathedral` | massive stone cathedral interior, digital glitch artifacts floating in air, fractured light through stained glass, impossible geometry | Teal + Crimson |

**Negative prompt template:**
```
daytime, bright sunlight, white background, modern architecture,
corporate, sterile, clean, sharp, overexposed, 
cartoon, anime, illustration, painting, sketch,
text, watermark, signature, people (unless specified),
DSLR lens flare artifacts, chromatic aberration, blurry
```

**ComfyUI settings:**
- Sampler: `euler_ancestral`
- Steps: 30–40
- CFG Scale: 7.0 (FLUX: use guidance scale 3.5)
- Size: 2880×1800 (or batch at 1440×900 then upscale ×2 with 4x-UltraSharp)
- Seed: Record and save seeds for any approved backgrounds

---

### 7.3 Enamel Pin Illustration Prompts (3D Render Aesthetic)

**Positive prompt template:**
```
enamel pin design, hard enamel, 3D product render, 
[PIN DESCRIPTION],
isolated on white background, studio lighting, top-down angle,
highly detailed, metallic gold edge detail, vibrant flat colors,
cloisonné technique, crisp edges, no gradients,
product photography, 8K render
```

**Per-pin substitutions:**

| Pin | `[PIN DESCRIPTION]` |
|---|---|
| Attraction Operations | roadside attraction panorama landscape, multiple small buildings, sunset sky, 1970s Americana |
| Artifact Recovery Team | wooden shipping crate with warning labels, rope handles, distressed stickers |
| Signal Integrity Division | hexagonal badge, oscilloscope waveform, vintage electronics aesthetic, green and black |
| Crossroads Ranger Station | wooden directional signpost, multiple arrows, raven perched on top, bonsai tree base |
| Bob Approved | grinning vintage skull wearing flat cap, approval stamp overlay, amber and cream |
| Deep Garden Ranger Division | park ranger badge silhouette, bonsai tree, raven, teal and deep forest green |
| Cosmic Selector | orbital orrery wheel, cosmic purple and deep space, golden orbital rings |
| Thursday Night Dance Committee | bigfoot figure dancing under UFO beam with jukebox, northern lights backdrop |

**Negative prompt:**
```
gradient fills, blurry, photograph, watercolor, sketch,
multiple pins (keep singular), background objects, text (unless specified),
human figures (unless bigfoot pin), complex textures
```

**ComfyUI settings:**
- Model: DreamShaper XL or SDXL base + refiner
- Sampler: `dpmpp_2m_karras`
- Steps: 35
- CFG Scale: 8.5
- Size: 1024×1024 (square format, then crop to pin shape)

---

### 7.4 Cinematic Scene Assets

**Bigfoot at Arcade / UFO Style:**

```
Positive:
cinematic digital painting, photorealistic illustration, Bigfoot creature 
standing at vintage arcade cabinet, playing a game, glowing screen lights 
the fur in amber and teal, UFO beam of light from above, northern lights 
in sky through broken roof, abandoned arcade building exterior visible, 
debris on floor, otherworldly atmosphere, painterly yet hyperrealistic,
wide establishing shot, anamorphic aspect ratio, rich color grading,
inspired by Blade Runner 2049 color palette

Negative:
cartoon, flat, anime, sketch, stock photo, daytime, 
clean/undamaged building, visible humans, scary expression on Bigfoot
(Bigfoot should look delighted/absorbed in the game)
```

**Cathedral of Glitch Warning Sign:**

```
Positive:
aged distressed road sign, large yellow warning sign format, 
black text reading "PLEASE KEEP HANDS FEET AND SEMANTIC FRAMEWORKS 
INSIDE REALITY AT ALL TIMES", heavily weathered, rust stains, 
paint peeling, bullet holes, digital glitch artifacts affecting the metal,
reality slightly warped around the sign, roadside location, dark sky

Negative:
clean new sign, bright colors, modern design, sans-serif fonts
(use classic highway font), no glitch effects, studio background
```

**ComfyUI settings for cinematic scenes:**
- Model: FLUX.1 Dev (primary), or SDXL + Epic Realism XL
- Sampler: `euler_ancestral`
- Steps: 40
- CFG: 6.5
- Size: 1920×1080 (for cinematic aspect ratio)
- Optional: Apply ControlNet (Canny or Depth) if you need to match a specific composition

---

### 7.5 Portrait Assets (Warden / Character Style)

**Warden portrait (figure in hat with quote overlay):**

```
Positive:
documentary portrait photography style, mysterious figure wearing 
wide-brim ranger hat, face partially shadowed, weathered outdoor jacket,
roadside attraction background slightly out of focus, warm amber side lighting,
teal atmospheric fill light, cinematic film grain, 35mm lens,
evocative, slightly otherworldly, authoritative yet enigmatic,
no face visible or heavily shadowed (maintain mystery)

Negative:
bright studio lighting, sharp facial features, business attire, 
clean background, digital art style, cartoon
```

**IP-Adapter conditioning:** If a reference character photo exists, use `IP-Adapter SDXL` at strength 0.6–0.75 to maintain character likeness while applying the LDI aesthetic.

**ControlNet recommendation:** Use `ControlNet-OpenPose` if you need specific pose matching. Reference pose image from the Warden mockup → apply as pose conditioning.

---

### 7.6 Quality Control Checklist for Generated Assets

Before any AI-generated asset goes to production:

- [ ] Check for AI artifact hands/fingers if humans are present
- [ ] Verify no unintended text/watermarks in image
- [ ] Color temperature matches the LDI palette (teal + amber + void black)
- [ ] Image passes the "would this fit in a 1970s roadside attraction brochure" test
- [ ] Resolution minimum 2880px on the long edge
- [ ] WebP conversion complete (85% quality)
- [ ] Mobile crop generated (768×1024 portrait variant)
- [ ] Seed and prompt archived in `/assets/backgrounds/[name]-prompt.txt`
- [ ] Grain overlay applied in final CSS (don't bake grain into the source image)

---

## APPENDIX A: Quick-Reference Token Table

| Token | Value | Use |
|---|---|---|
| `--ldi-void` | `#0a0907` | Page background |
| `--ldi-surface` | `#141210` | Card/panel background |
| `--ldi-teal` | `#00e5cc` | Primary signal color |
| `--ldi-amber` | `#d4820a` | Primary warmth color |
| `--ldi-crimson` | `#c0281a` | Danger/denied |
| `--ldi-text-primary` | `#e8dcc0` | Main body text |
| `--ldi-text-dim` | `#5a5040` | Labels, breadcrumbs |
| `--gs-void` | `#0e1117` | Glasshouse background |
| `--gs-champagne` | `#c8a96e` | Glasshouse accent |
| `--gs-text-light` | `#f5f6f7` | Glasshouse body on dark |

---

## APPENDIX B: File Structure Reference

```
lithium-dreams.com/
├── assets/
│   ├── backgrounds/
│   │   ├── homepage-hero.webp
│   │   ├── deep-garden-hero.webp       ← NEEDED
│   │   ├── museum-hero.webp            ← NEEDED
│   │   ├── fortune-hero.webp           ← NEEDED
│   │   ├── arcade-hero.webp            ← NEEDED
│   │   ├── chapel-hero.webp            ← NEEDED
│   │   ├── workshop-hero.webp          ← NEEDED
│   │   ├── cathedral-hero.webp         ← NEEDED
│   │   ├── broadcasts-hero.webp        ← NEEDED
│   │   ├── about-hero.webp             ← NEEDED
│   │   └── glasshouse-hero.webp        ← NEEDED
│   ├── textures/
│   │   ├── grain-200.png
│   │   └── parchment-400.png
│   ├── icons/
│   │   └── ldi-icons.svg               ← Custom sprite
│   └── fonts/                          ← Self-host if CDN unavailable
│
├── styles/
│   ├── tokens/
│   │   ├── attraction.css              ← System A tokens
│   │   └── glasshouse.css              ← System B tokens
│   ├── components/
│   │   ├── card.css
│   │   ├── status.css
│   │   ├── hero.css
│   │   ├── breadcrumb.css
│   │   ├── system-panel.css
│   │   ├── fortune-ticket.css
│   │   ├── cabinet-card.css
│   │   ├── case-file.css
│   │   ├── env-widget.css
│   │   ├── root-map.css
│   │   ├── depth-transition.css
│   │   └── glasshouse/
│   │       ├── buttons.css
│   │       ├── inputs.css
│   │       ├── pills.css
│   │       ├── badges.css
│   │       ├── service-tile.css
│   │       └── stat-chip.css
│   └── animations.css
│
└── merch/
    ├── pins/                           ← .AI files per pin design
    ├── stickers/                       ← .AI files per sticker
    └── bob-dispenser/
        ├── blueprint-dimensions.pdf
        └── render-marketing.png
```

---

## APPENDIX C: Revision Log

| Version | Date | Changes |
|---|---|---|
| 1.0 | June 2026 | Initial specification. Based on 19 design mockups. |

---

*VD-0001 · Lithium Dreams Institute · Visual Design System · © 2026*
