# Lithium Dreams Industries — Agent Context

You are working on the public-facing site for **Lithium Dreams Industries**, a lore-first creative studio site built as an old roadside attraction that secretly houses a sophisticated creative laboratory. John is the operator. Ghost (operational), Bob (chaotic/warm), and Warden (quiet/botanical) are the three characters embedded in the site's fiction.

**You are not building a portfolio or dashboard. You are renovating an old roadside attraction.**

---

## Repo & Deploy

```
Repo:    /Volumes/The Crossroads/claude-projects/lithium-dreams-site
GitHub:  https://github.com/JohnnyMa9ic/lithium-dreams-site
Deploy:  git push origin main → Cloudflare Workers auto-builds (no manual wrangler needed)
Live:    https://lithium-dreams.com
```

Deploy workflow:
```bash
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" add <files>
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" commit -m "your message"
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" push origin main
```
Cloudflare picks up the push and rebuilds. No `wrangler deploy` required.

---

## Stack

- **Astro** static site (Cloudflare Workers adapter injected at build time — do not add it locally)
- **TypeScript** for data files
- **Vanilla CSS** with CSS custom properties (no Tailwind, no CSS-in-JS)
- **No framework components** — Astro `.astro` files only

---

## Route Map

| Route | File | Status |
|---|---|---|
| `/` | `src/pages/index.astro` | Live — front gate homepage |
| `/attraction` | `src/pages/attraction.astro` | Live — Main Midway interactive map |
| `/gift-shop` | `src/pages/gift-shop.astro` | Placeholder |
| `/arcade` | `src/pages/arcade.astro` | Placeholder |
| `/museum` | `src/pages/museum.astro` | Placeholder |
| `/fortune` | `src/pages/fortune.astro` | Placeholder |
| `/employees-only` | `src/pages/employees-only.astro` | Locked/teaser |
| `/chapel` | `src/pages/chapel/index.astro` | Placeholder |
| `/chapel/back-room` | `src/pages/chapel/back-room.astro` | Hidden Cathedral teaser (not in nav) |
| `/workshop` | `src/pages/workshop.astro` | Ghost's Workshop — access portal to cc.lithium-dreams.com |
| `/crossroads` | `src/pages/crossroads.astro` | Deeper lore hub placeholder |

---

## Component Inventory

All components are in `src/components/`. Use these — do not create generic HTML cards.

| Component | Usage |
|---|---|
| `Layout.astro` | Wraps every page. Props: `title`, `activePage` (nav highlight) |
| `CRTFrame.astro` | Monochrome terminal/monitor frame. Prop: `label` (header text) |
| `MaintenanceTag.astro` | Status badge. Props: `status` (StatusTag string), `size` (sm/md/lg) |
| `DistrictCard.astro` | Navigation card for Midway districts. Accepts District data shape |
| `TicketButton.astro` | CTA button styled as a ticket stub |
| `LockedDoor.astro` | Locked/restricted access placeholder |
| `MuseumPlaque.astro` | Museum-style content card with placard aesthetic |
| `FortuneCard.astro` | Bob's fortune machine card |
| `EmployeeNotice.astro` | Staff notice / bulletin board card |
| `NeonSign.astro` | Neon-glow text element |

---

## Design Tokens

All tokens are in `src/styles/tokens.css` and available globally as CSS variables.

**Palette:**
```css
--ldi-black: #0A0A0C        /* page background */
--road-asphalt: #1A1C1F     /* card backgrounds */
--rain-slate: #2C3038       /* borders, dividers */
--neon-amber: #E8A420       /* primary accent, CTA highlight */
--ghost-blue: #4DB8D4       /* Ghost/Workshop accent */
--warden-teal: #2E8B6E      /* Warden/garden accent */
--moss-green: #4A6741       /* secondary green */
--brass: #B5893E            /* aged metal accent */
--paper: #E8DEC8            /* light text, paper elements */
--warning-red: #C23B22      /* alerts, warnings */
```

**Typography:**
```css
--font-display: 'Bebas Neue'    /* headings, signage */
--font-sub: 'Oswald'            /* subheadings */
--font-body: 'IBM Plex Sans'    /* body text */
--font-mono: 'IBM Plex Mono'    /* terminals, code, Ghost areas */
```

**Spacing:** `--space-xs` (0.25rem) → `--space-sm` → `--space-md` → `--space-lg` → `--space-xl` (4rem)

**Utility classes** (defined in `global.css`):
- `.mono` — applies `--font-mono`
- `.text-dim` — muted/secondary text color

---

## Data Files

### `src/data/districts.ts`
Array of `District` objects powering the Midway district cards. Shape:
```typescript
{
  title: string
  description: string
  status: StatusTag   // 'OPEN' | 'FLICKERING' | 'STAFF ONLY' | 'UNDER REPAIR' | 'BY APPOINTMENT' | 'RESTRICTED' | 'COMING SOON' | 'ARCHIVED' | 'UNSTABLE'
  href: string
  icon: string
  microcopy: string   // deadpan one-liner shown on card
  inNav: boolean      // whether to include in top nav
}
```

### `src/data/microcopy.ts`
Pool of deadpan ambient microcopy strings. Add new ones here; they surface in random placements across the site.

---

## Design Rules

1. **Build places, not pages.** A `/museum` page should feel like a museum room, not a blog list.
2. **Every UI element should feel like a physical artifact.** Cards = placards or clipboards. Buttons = ticket stubs. Alerts = maintenance tags.
3. **The site should smile before it mystifies.** Welcoming first, strange second.
4. **Deadpan microcopy. Never winking.** Sincere, not ironic.
5. **One impossible thing per screen.** Restraint is the move.
6. **Nothing overly polished.** Slightly worn, hand-built, accumulated, loved, repaired.
7. **Ghost's Workshop = operational, not decorative.** Ghost-blue (`--ghost-blue`), monospace, CRT frames, green status dots.
8. **Bob's areas = warm, chaotic, funny, handmade.** Amber accents, cluttered, personality-forward.
9. **Warden's areas = quiet, botanical, patient.** Teal accents, breathing room, slow.
10. **Cathedral of Glitch is NOT the homepage.** It lives only at `/chapel/back-room` — beautiful, fractured, cold, abandoned.
11. **Never SaaS cards.** If it looks like a startup dashboard, redo it.

---

## Common Task Patterns

### Add a new page
1. Create `src/pages/[route].astro`
2. Use `<Layout title="..." activePage="/route">` wrapper
3. Use appropriate components — `CRTFrame` for Ghost areas, `MuseumPlaque` for Museum, etc.
4. If it's a new district, add it to `src/data/districts.ts`

### Update a district's status tag
Edit the `status` field in `src/data/districts.ts`. Valid values: `OPEN | FLICKERING | STAFF ONLY | UNDER REPAIR | BY APPOINTMENT | RESTRICTED | COMING SOON | ARCHIVED | UNSTABLE`

### Add microcopy
Add strings to `src/data/microcopy.ts`. Keep them deadpan and sincere.

### Update the Midway hotspot map
The panorama hotspot overlays are in `src/pages/attraction.astro`. They are absolutely-positioned transparent `<a>` tags with percentage-based coordinates over the panorama image. The Employees Only door hotspot links to `/workshop`.

### Update the Workshop status panel
The SYSTEM STATUS CRT frame is in `src/pages/workshop.astro`. Edit the `<p>` lines inside `<CRTFrame label="SYSTEM STATUS">` to reflect current infrastructure state.

### Change what the "ENTER WORKSHOP" button points to
In `src/pages/workshop.astro`, find `<a href="https://cc.lithium-dreams.com/app/" class="enter-btn">` and update the href.

---

## Key External Connections

| Service | URL | Notes |
|---|---|---|
| Command Center | `https://cc.lithium-dreams.com/app/` | Cloudflare Tunnel → cc_server at 127.0.0.1:7771 on Mac Mini. Password protected. |
| Cloudflare Workers | Auto-deploy on push to main | No manual deploy needed |

---

## What NOT to do

- Do not add `@astrojs/cloudflare` adapter locally — Cloudflare injects it at build time
- Do not run `wrangler deploy` manually — push to git triggers the build
- Do not create React/Vue/Svelte components — Astro components only
- Do not add Tailwind — vanilla CSS with custom properties only
- Do not make it look like a SaaS dashboard
- Do not put the Cathedral on the homepage
