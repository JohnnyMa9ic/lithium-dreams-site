# LDI Corporate v2 Prototype
## Glasshouse Systems Studio

This is a standalone HTML/CSS/JS prototype for the Lithium Dreams Industries corporate side.

## What this contains

- Bright Glasshouse Systems Studio visual language
- Corporate homepage layout
- Four service cards
- Four Materials section
- Guided Mission Intake wizard
- Live Mission Brief preview
- JSON output, copy, and download
- Internal deployment case files
- About section
- Responsive layout

## Design direction

The corporate side should contrast the attraction.

- Attraction: night, rain, neon, mystery, Bob
- Corporate: daylight, glass, plants, clarity, trust

The corporate side should feel like a premium systems architecture studio inside a glass conservatory.

## How to run

Open `index.html` in a browser.

No build step required.

## How to port to React / Cloudflare

Suggested component breakdown:

- `CorporateShell`
- `CorporateHeader`
- `HeroGlasshouse`
- `SystemsGrid`
- `MaterialsBoard`
- `ApproachTimeline`
- `MissionIntakeWizard`
- `BriefPreview`
- `InternalCaseFiles`
- `FounderAbout`
- `CorporateFooter`

Preserve the wizard logic:
- step state
- form data state
- live preview
- JSON generation
- copy/download/export
- webhook delivery later

## Next implementation step

Replace local JSON-only submission with:

Form state
→ Cloudflare Worker endpoint
→ email notification
→ markdown brief generation
→ kanban/task creation
→ Hermes review pipeline

