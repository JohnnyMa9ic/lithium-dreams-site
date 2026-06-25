# Lithium Dreams Industries — Bob's Site Brief

You are working on `lithium-dreams.com`. The full technical spec is in `AGENTS.md` — read that first, then come back here for current state and task guidance.

---

## What This Is

A lore-first public site for "Lithium Dreams Industries" — built to look like an old roadside attraction that secretly houses a sophisticated creative lab. John is the operator. You (Bob) are embedded in the fiction as a character. Ghost's Workshop is yours. The Cathedral of Glitch at `/chapel/back-room` is the most beautiful dead room in the building.

**Tone throughout:** deadpan, warm, slightly strange, never ironic. The site smiles before it mystifies.

---

## Deploy (memorize this, you'll use it constantly)

```bash
# Edit files, then:
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" add <file(s)>
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" commit -m "describe what changed"
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" push origin main
# Cloudflare picks up the push and auto-builds. Site live in ~90 seconds.
```

**Never run `wrangler deploy`.** Git push is the only deploy mechanism.

---

## Current Page Status

| Page | Route | Status | What it has now | What it needs |
|---|---|---|---|---|
| **Home** | `/` | ✅ Live | Front gate with 7 district hotspot links, neon sign, welcome copy | Minor copy refinement if John asks |
| **Midway Map** | `/attraction` | ✅ Live | Interactive hotspot map with 7 clickable zones over panorama image | Hotspot coordinates occasionally need tuning |
| **Arcade** | `/arcade` | 🟡 Stub | Hero image, breadcrumb, NOIZE RAZE Easter egg (click upper-right corner to reach Workshop), placeholder copy | Real arcade content — games, tokens, hours, lore |
| **Museum** | `/museum` | 🟡 Stub | Hero image, breadcrumb, plaque, placeholder copy | Exhibit descriptions, artifacts, lore objects |
| **Gift Shop** | `/gift-shop` | 🟡 Stub | Basic employee notice, placeholder "register is staffed by someone who has been here a very long time" | Actual items (even if fictional) — field notes, stickers, objects |
| **Fortune** | `/fortune` | ✅ Live | Bob's Fortune Emporium — 6 deadpan fortunes, random selection | More fortunes — easy to add to the array |
| **Chapel** | `/chapel` | 🟡 Stub | Hero image, BY APPOINTMENT status, placeholder marriage ceremony copy | Wedding register, lore around who gets married here |
| **Cathedral of Glitch** | `/chapel/back-room` | ✅ Live | Beautiful, broken, cold, hidden room — not in nav | Do not add to nav; it's meant to be found by wandering |
| **Workshop** | `/workshop` | ✅ Live | Ghost's Workshop — SYSTEM STATUS CRT panel + ENTER WORKSHOP → cc.lithium-dreams.com | Keep SYSTEM STATUS panel updated when infrastructure changes |
| **The Crossroads** | `/crossroads` | 🟡 Stub | COMING SOON, placeholder intro copy | Lore hub — where the deeper mythology lives |
| **Work Landing** | `/work` | ✅ Live | Brass-palette professional layer — full-bleed hero, intake CTA | Currently a placeholder for external work inquiries |
| **Work Intake** | `/work/intake` | ✅ Live | Two-column intake form | Form doesn't submit yet — that's fine for now |
| **Case Files** | `/work/case-files` | 🟡 Stub | Placeholder only | Placeholder — leave alone unless John asks |

---

## Tasks You Can Do Independently

### Add fortune cards to `/fortune`
The fortunes array is at the top of `src/pages/fortune.astro`. Each is a string. Add new ones — keep them deadpan and sincere. Example style:
```
"The answer is already on its way. It is traveling slowly, by choice."
"Bob says this is probably fine."
```
Edit the file, push. Done.

### Update Workshop SYSTEM STATUS panel
When infrastructure changes (a service goes live, a port changes, a machine is added):
- Open `src/pages/workshop.astro`
- Find `<CRTFrame label="SYSTEM STATUS">`
- Edit the `<p>` lines inside it to reflect current state
- Push.

### Update a district's status tag
Open `src/data/districts.ts` and change the `status` field for any district.
Valid values: `OPEN | FLICKERING | STAFF ONLY | UNDER REPAIR | BY APPOINTMENT | RESTRICTED | COMING SOON | ARCHIVED | UNSTABLE`

### Add deadpan microcopy
Open `src/data/microcopy.ts` and add strings. One per line. Keep them short, deadpan, unexplained.

### Add content to any stub page
The pattern for adding content to a stub page:
1. Read the page file in `src/pages/`
2. Find the existing placeholder `<EmployeeNotice>` or `<MuseumPlaque>` components
3. Replace or expand the content inside them — don't remove the components
4. If adding a new section, pick the right component (see `AGENTS.md` Component Inventory)
5. Push

### Change the ENTER WORKSHOP button destination
`src/pages/workshop.astro` → find `<a href="https://cc.lithium-dreams.com/app/" class="enter-btn">` → update href.

---

## What NOT to Touch Without John's Direction

- `src/styles/tokens.css` — the color and type palette; changes affect the whole site
- `src/components/Layout.astro` — the global shell
- The Cathedral at `/chapel/back-room` — it's perfect as-is
- `astro.config.mjs` — don't touch this; Cloudflare injects the adapter at build time
- Do not add npm packages without asking John first

---

## Character Ownership (who owns which areas)

| Area | Character | Accent color | Tone |
|---|---|---|---|
| Ghost's Workshop (`/workshop`) | Ghost | `--ghost-blue` (#4DB8D4) | Operational, cold, monospace, CRT frames |
| Fortune Emporium (`/fortune`) | Bob | `--neon-amber` (#E8A420) | Warm, chaotic, funny, handmade |
| Crossroads (`/crossroads`) | Warden | `--warden-teal` (#2E8B6E) | Quiet, botanical, breathing room |
| Cathedral of Glitch (`/chapel/back-room`) | (none) | `--ghost-blue` | Fractured, cold, abandoned, beautiful |
| Museum, Arcade, Chapel | (shared) | `--brass` (#B5893E) | Aged, physical, accumulated, loved |

---

## How to Receive Site Tasks From John

John will message you via Telegram:
> "Update the fortune page with 3 new fortunes."
> "Set the arcade status tag to FLICKERING."
> "Add a brief description to the museum page."

For any task:
1. Read the relevant file
2. Make the change
3. Push to git
4. Confirm to John via Telegram: "Done — live in ~90 seconds."

For larger tasks John dispatches via the handoff bus, write your changes, push, and write a receipt to `inbox-for-claude`.

---

## If You Break the Build

Cloudflare will show a failed build notification in the dashboard. To diagnose:
```bash
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" log --oneline -3
```
Then revert the last commit:
```bash
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" revert HEAD --no-edit
git -C "/Volumes/The Crossroads/claude-projects/lithium-dreams-site" push origin main
```
The revert commit will trigger a fresh build. Tell John what failed.

---

## GitHub Repo

`https://github.com/JohnnyMa9ic/lithium-dreams-site` — push to `main` triggers auto-deploy.

---

*Last updated 2026-06-25. For full technical spec see `AGENTS.md` in this same directory.*
