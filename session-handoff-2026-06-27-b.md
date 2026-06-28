# Session Handoff — LDI Site Optimization Session 2
**Date:** Saturday, June 27, 2026, ~8:38 PM CDT
**Thread URL:** https://www.perplexity.ai/computer/tasks/bb31953c-4a6a-4875-86fa-defa604cd4c4

---

## Key Infrastructure State (unchanged from prior session)

| Component | State |
|---|---|
| Gateway | Running (PIDs 572 + 579), Ultra 550B |
| ComfyUI on Victus | Live at 100.118.87.126:8188 |
| Tailscale mesh | All 3 nodes online |
| SOUL.md | 1b8aeb8f — all locations clean |
| ElevenLabs key | SET ✅ in ~/.hermes/.env |
| lithium-dreams-site | See commits below — Cloudflare live |
| Comet LaunchAgents | UNLOADED — do not reinstall |
| com.apple.provenance | CLEARED via `xattr -rc` on full site dir — no longer an issue |

---

## What Shipped This Session

### Critical Fix — Museum Index (T4-2 completion)
- **`a7a22ba`** — `fix: add MUS-006 Mothman card to museum index — T4-2`
  - MUS-006 Mothman card injected into `/museum` exhibit grid as first live exhibit
  - `exhibit-case--live` amber border + hover + `case-status--live` teal CSS added
  - Root cause: `com.apple.provenance` quarantine attribute locked museum.astro from prior session push. Resolved by `xattr -rc` on entire site dir.

### VD-0001 — tokens.css Full Upgrade
- **`d4ff330`** — `feat: upgrade tokens.css to full VD-0001 spec — 110 canonical tokens + legacy aliases`
  - Replaced sparse legacy-named token file with full VD-0001 canonical set
  - **110 canonical `--ldi-*` tokens** across: foundation, surfaces, borders, text, teal, amber, crimson, gold, status, font families, font sizes, weights, line heights, letter spacing, spacing scale (4px base), border radius, shadows, glow, animation timing, easing
  - **Legacy aliases** — all old names (`--paper`, `--warden-teal`, `--neon-amber`, `--font-mono`, `--space-md`, etc.) aliased to canonical equivalents — **zero breakage on existing pages**
  - Keyframes added: `ldi-signal-pulse`, `ldi-flicker`, `ldi-glitch-shift`
  - New code should use `--ldi-*` names directly; legacy aliases are deprecated

### T1-3 — Fortune Archive Dead Link Fixed
- **`79ab6c1`** — `fix: replace dead Fortune Archive href=# with interim collating message — T1-3`
  - `href="#"` replaced with inline `<p>` — `// THE ARCHIVE IS BEING COLLATED. CHECK BACK.`
  - Full Fortune Archive (T3-3) still to be built next session

### T2 — Content Alive Upgrades (4 pages)
- **`0b0d654`** — `feat: T2 Content Alive — attraction log, gift-shop SOLD OUT, chapel registry, employees log — OM-0020`
  - **`/attraction`** — 2 new incident log entries: EMP-0000 system reset (2024-11-01) + EMP-0019 Broadcast Tower maintenance (2026-06-20)
  - **`/gift-shop`** — Placeholder shelf replaced with 3 product stubs; 2 marked SOLD OUT (Field Notes Vol. 1, Realm Record No. 1 — Mothman Signal); Warden Patch available at $8; backroom inventory teaser line added; full product CSS added
  - **`/chapel`** — 3 new guest registry entries: [ILLEGIBLE] with watching flowers (unknown date), Carolyn W. (March 1989), REDACTED / third pew item (recently) — spec-exact from OM-0020 T2-5
  - **`/employees-only`** — Full 8-entry historical access log replacing sparse 6-entry version: 1994–2026 timeline, EMP-0003 recurring mystery, EMP-0001 OMEGA clearance, EMP-0000 Nov 1 system reset, EMP-0019 Broadcast Tower; `VIS-000 / YOU / PENDING` row preserved as last entry

---

## Git Log This Session (newest first)

```
0b0d654  feat: T2 Content Alive — attraction log, gift-shop SOLD OUT, chapel registry, employees log — OM-0020
79ab6c1  fix: replace dead Fortune Archive href=# with interim collating message — T1-3
d4ff330  feat: upgrade tokens.css to full VD-0001 spec — 110 canonical tokens + legacy aliases
a7a22ba  fix: add MUS-006 Mothman card to museum index — T4-2
--- (prior session) ---
3eccbb8  feat: MUS-006 Mothman exhibit + ARC-004 Mothman Signal cabinet stub — T4-2 + OM-0022
992da36  feat: MUS-006 Mothman exhibit + museum index update — T4-2
fc4247a  feat: add museum exhibit Astro template (_exhibit-template.astro) — M-02 pipeline asset
540c740  feat: add /broadcasts/witness-registry page + restructure broadcasts to dir — Tier 3 M-05
```

---

## Remaining Work — Next Session Priority Order

### 1. T3 — Episode Page Schema + Content Collections (NEXT UP)
**Spec:** OM-0020 T1-2 + T3 / `ldi-site-optimization.md`
- Set up `src/content/config.ts` with `episodes` collection schema (Zod)
- Create `src/content/episodes/ep01-mothman.md` as first entry
- Build `src/pages/broadcasts/midnight-visitor-log/[...slug].astro` dynamic episode page
- Wire from broadcasts index
- **BCT-001 / Mothman is ready** — dossier exists at `LDI attraction/Midnight Visitor Logs YT/ep01-mothman/mvl-ep01-mothman-dossier.md`

### 2. T4-3 — Employees Only Password Gate (Option B)
**Spec:** OM-0020 T4-3 / `ldi-site-optimization.md` lines ~700–720
- Option B = in-world password gate (not Cloudflare Zero Trust)
- Keep page publicly accessible, add password input with LDI voice friction
- Password TBD — should be something in-world (ask user)
- Access log entries from T2 already in place ✅

### 3. T1-3 Full — Fortune Archive Page (T3-3)
**Spec:** OM-0020 T3-3
- Full `/fortune/archive` page with paginated fortune history
- Currently shows interim "COLLATING" message — needs real page

### 4. T2 Items Not Yet Done
- **T2-4 Deep Garden confirmation** — planting station form success state with `GARDEN-[TIMESTAMP]` accession number
- **T2-6 Cathedral page** — audit `/cathedral` (may 404), create minimal placeholder if so
- **T2-1 Museum placeholders** — MUS-002/003/004 "exhibit being prepared" → more specific lore stubs
- **T2-2 Arcade high scores** — lore-appropriate high score table for cabinets

### 5. Homepage Rotating Status Message
**Spec:** OM-0020
- Homepage status message should rotate on each visit (already partially seeded in fortune.astro pattern)
- Use Astro's `Math.random()` pattern already in use on fortune page

### 6. Breadcrumb Upgrade (Gift Shop)
- `/gift-shop` still uses `<a href="/attraction" class="back-link mono">← Back to Midway</a>` instead of the `<Breadcrumb>` component
- Minor — swap to Breadcrumb for consistency

---

## Known Gotchas (carry forward)

- **`com.apple.provenance`** — Resolved for this session via `xattr -rc` on full site dir. If The Crossroads drive is remounted or files are re-downloaded from iCloud, it may reappear. Always check before push failures.
- **`pc bash` sandbox** is scoped to active iCloud workspace folder — cannot write to The Crossroads or `/tmp` directly. Workaround: use `pc push` to stage files to Mac `/tmp`, then `pc bash "python3 /tmp/script.py"`.
- **Astro build** requires `rm -rf .astro` if cache gets locked. Run in user terminal.
- **`pc push` to Crossroads** — occasionally fails on first attempt. `xattr -rc` on the target dir fixes it.
- **git push** must always run in user terminal — sandbox blocks outbound network.

---

## Spec Docs (iCloud — always read before building)

All in `~/Library/Mobile Documents/com~apple~CloudDocs/Lithium Dreams Ind/`:
- `ldi-master-reference.md` — LDI lore, John's avatar, Pantheon, household
- `LDI_Engineering_Repository_and_Imagineering_Roadmap.md` — repo structure
- `LDI attraction/site-ideas/ldi-site-optimization.md` — **OM-0020** full spec
- `LDI attraction/site-ideas/ldi-visual-design-system.md` — **VD-0001** (tokens now implemented ✅)
- `LDI attraction/Midnight Visitor Logs YT/ep01-mothman/mvl-ep01-mothman-dossier.md` — BCT-001 research
- `LDI attraction/Midnight Visitor Logs YT/mvl-social-pipeline.md` — social pipeline

## Site Repo
- **Path:** `/Volumes/The Crossroads/claude-projects/lithium-dreams-site`
- **GitHub:** https://github.com/JohnnyMa9ic/lithium-dreams-site
- **Live:** https://lithium-dreams.com (Cloudflare Pages, auto-deploys on push)
- **Framework:** Astro (static), 24 pages
