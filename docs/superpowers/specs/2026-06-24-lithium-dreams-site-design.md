# Lithium Dreams Industries — Site Design Spec v0.1

## Summary

Build the front gate and main midway of The Last Roadside Attraction. Static Astro site deployed to Cloudflare Pages at `lithium-dreams.com`. Version 0.1 establishes bones: route structure, artifact component library, homepage rainy scene, district grid, and placeholder pages for all districts.

## Stack

| Layer | Choice | Reason |
|---|---|---|
| Framework | Astro v7, static output | No client JS needed; deploys flat to Pages |
| Styling | CSS custom properties, no Tailwind | Hand-built feel; variables match LDI token spec |
| Components | Pure `.astro` files | Simple, no React overhead |
| Fonts | Google Fonts CDN | Bebas Neue + Oswald + IBM Plex Sans/Mono |
| Deploy | Cloudflare Pages | lithium-dreams.com already on Cloudflare |

## Design Tokens

```css
--ldi-black: #0A0A0C
--road-asphalt: #1A1C1F
--rain-slate: #2C3038
--neon-amber: #E8A420
--ghost-blue: #4DB8D4
--warden-teal: #2E8B6E
--moss-green: #4A6741
--brass: #B5893E
--paper: #E8DEC8
--warning-red: #C23B22
```

## Typography

| Role | Font | Weight |
|---|---|---|
| Display / headings | Bebas Neue | 400 |
| Subheadings / buttons | Oswald | 600 |
| Body text | IBM Plex Sans | 400/600 |
| Terminal / monospace | IBM Plex Mono | 400/600 |

## Routes

| Route | Name | Status | Notes |
|---|---|---|---|
| `/` | Front Gate | Build | Rainy scene, OPEN neon, TicketButton CTA |
| `/attraction` | Main Midway | Build | 8-card district grid |
| `/gift-shop` | Gift Shop | Placeholder | OPEN |
| `/arcade` | Arcade | Placeholder | FLICKERING |
| `/museum` | Museum | Placeholder | OPEN |
| `/fortune` | Fortune Emporium | Placeholder | UNSTABLE |
| `/employees-only` | Employees Only | Placeholder | RESTRICTED — LockedDoor component |
| `/chapel` | Wedding Chapel | Placeholder | BY APPOINTMENT |
| `/chapel/back-room` | Cathedral of Glitch | Placeholder | Hidden — not in nav; cold blue palette |
| `/workshop` | Ghost's Workshop | Placeholder | STAFF ONLY |
| `/crossroads` | The Crossroads | Placeholder | COMING SOON |

## Components

| Component | Analog | Use |
|---|---|---|
| `Layout` | — | HTML shell, nav, fonts, token imports |
| `TicketButton` | Ticket stub | Primary CTA buttons |
| `DistrictCard` | Clipboard/label | Midway district cards |
| `MaintenanceTag` | Yellow caution tag | Status alerts, notices |
| `NeonSign` | Neon sign | OPEN sign, accent labels |
| `LockedDoor` | Staff door | Restricted-access pages |
| `CRTFrame` | CRT monitor | Loading states, terminal displays |
| `MuseumPlaque` | Museum placard | Lore text, archive entries |
| `EmployeeNotice` | Laminated notice | Warnings, cryptid bureaucracy |
| `FortuneCard` | Fortune machine card | Bob's emporium, random prompts |

## Data

- `districts.ts` — 8 midway districts with title, description, status, href, icon, microcopy
- `microcopy.ts` — pool of deadpan one-liners for ambient use

## Homepage Concept

Full-viewport dark scene (`--ldi-black`). Canvas rain overlay — 150 angled drops, cold blue-gray, RAF loop. Centered content stack: "LITHIUM DREAMS INDUSTRIES" small header → "THE LAST ROADSIDE ATTRACTION" Bebas Neue at ~8vw → Oswald subtext → NeonSign OPEN (amber flicker) → TicketButton "ENTER THE ATTRACTION" → secondary nav links.

## Cathedral Doctrine (back-room)

The only page that breaks the amber palette. Background shifts to deep blue-black (`#050810`). Ghost-blue accents. CRTFrame with corrupted text. Locked tape visual. No nav back — visitors who find it found it.

## Non-Negotiables

- No SaaS cards. No generic grids. Everything is an artifact.
- Hand-built feel — slight imperfections in typography spacing are fine.
- Humor is deadpan, never winking.
- The Cathedral is not horror. It is abandoned beauty.
