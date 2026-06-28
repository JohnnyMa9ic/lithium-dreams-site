# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /work/case-files
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /work/case-files has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #ffffff, background color: #c99d4c, font size: 7.8pt (10.4px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"gh-logo-mark\" data-astro-cid-zyfjkaoe=\"\">LDI</span>", "impact": "serious", "none": [], "target": [".gh-logo-mark"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.18 (foreground color: #3d7fbd, background color: #fefefd, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/work/case-files\" class=\"active\" data-astro-cid-zyfjkaoe=\"\">Case Files</a>", "impact": "serious", "none": [], "target": [".active"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.26 (foreground color: #8a8f88, background color: #fefefd, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"gh-nav-escape\" data-astro-cid-zyfjkaoe=\"\">← The Attraction</a>", "impact": "serious", "none": [], "target": [".gh-nav-escape"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.25 (foreground color: #c99d4c, background color: #f5f3ee, font size: 7.4pt (9.92px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"page-eyebrow\" data-astro-cid-24nodo3f=\"\">Case Files</div>", "impact": "serious", "none": [], "target": [".page-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.39 (foreground color: #2e7d4f, background color: #e7f2e9, font size: 7.0pt (9.28px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"case-status case-status--operational\" data-astro-cid-24nodo3f=\"\">Operational</span>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-meta > .case-status--operational.case-status"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.19 (foreground color: #8a8f88, background color: #fcfbfa, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"case-id\" data-astro-cid-24nodo3f=\"\">FILE — 001</span>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-meta > .case-id"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.41 (foreground color: #c99d4c, background color: #fcfbfa, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"case-track\" data-astro-cid-24nodo3f=\"\">Creative Systems · Content Engine</div>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-track"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.19 (foreground color: #8a8f88, background color: #fcfbfa, font size: 7.4pt (9.92px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"outcome-label\" data-astro-cid-24nodo3f=\"\">Architecture</span>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-outcomes > .case-outcome:nth-child(1) > .outcome-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.19 (foreground color: #8a8f88, background color: #fcfbfa, font size: 7.4pt (9.92px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"outcome-label\" data-astro-cid-24nodo3f=\"\">Status</span>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-outcomes > .case-outcome:nth-child(2) > .outcome-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.19 (foreground color: #8a8f88, background color: #fcfbfa, font size: 7.4pt (9.92px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"outcome-label\" data-astro-cid-24nodo3f=\"\">Key result</span>", "impact": "serious", "none": [], "target": [".case-card--featured > .case-outcomes > .case-outcome:nth-child(3) > .outcome-label"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - navigation [ref=e2]:
    - link "LDI Work" [ref=e3] [cursor=pointer]:
      - /url: /work
      - generic [ref=e4]: LDI
      - generic [ref=e5]: Lithium Dreams Industries
    - generic [ref=e6]:
      - link "Overview" [ref=e7] [cursor=pointer]:
        - /url: /work
      - link "Mission Intake" [ref=e8] [cursor=pointer]:
        - /url: /work/intake
      - link "Case Files" [ref=e9] [cursor=pointer]:
        - /url: /work/case-files
      - link "About" [ref=e10] [cursor=pointer]:
        - /url: /about
    - link "← The Attraction" [ref=e11] [cursor=pointer]:
      - /url: /attraction
  - main [ref=e12]:
    - generic [ref=e13]:
      - generic [ref=e14]: Case Files
      - heading "Internal deployments first." [level=1] [ref=e15]
      - paragraph [ref=e16]: We don't pitch client work we haven't run ourselves. These are LDI's live internal deployments — each one is a real system operating under real conditions. Client engagements come after the internal proof of concept holds up.
    - generic [ref=e17]:
      - article [ref=e18]:
        - generic [ref=e19]:
          - generic [ref=e20]: Operational
          - generic [ref=e21]: FILE — 001
        - heading "LDI Website" [level=2] [ref=e22]
        - generic [ref=e23]: Creative Systems · Content Engine
        - paragraph [ref=e24]: The site you're on. Astro 7 + Cloudflare Pages. Full design system with dark attraction aesthetic and light Glasshouse corporate identity running as two distinct modes under a single build. Deployed continuously via GitHub → Cloudflare. Sub-second TTFB globally.
        - generic [ref=e25]:
          - generic [ref=e26]:
            - generic [ref=e27]: Architecture
            - generic [ref=e28]: Astro + Cloudflare Pages
          - generic [ref=e29]:
            - generic [ref=e30]: Status
            - generic [ref=e31]: Live — this session
          - generic [ref=e32]:
            - generic [ref=e33]: Key result
            - generic [ref=e34]: Two visual identities, one coherent build
      - article [ref=e35]:
        - generic [ref=e36]:
          - generic [ref=e37]: Operational
          - generic [ref=e38]: FILE — 002
        - heading "Mission Intake Pipeline" [level=2] [ref=e39]
        - generic [ref=e40]: Automation Systems · Research OS
        - paragraph [ref=e41]: The intake wizard on this page feeds a structured JSON pipeline. 6-step guided brief replaces the vague discovery call. JSON output with copy/download. Webhook delivery to structured intake queue in active development.
        - generic [ref=e42]:
          - generic [ref=e43]:
            - generic [ref=e44]: Architecture
            - generic [ref=e45]: Vanilla JS wizard + JSON pipeline
          - generic [ref=e46]:
            - generic [ref=e47]: Status
            - generic [ref=e48]: Form live — webhook in dev
      - article [ref=e49]:
        - generic [ref=e50]:
          - generic [ref=e51]: Operational
          - generic [ref=e52]: FILE — 003
        - heading "Bob's Fortune Emporium" [level=2] [ref=e53]
        - generic [ref=e54]: Executive Assistant OS · Operator Dashboards
        - paragraph [ref=e55]: "Autonomous agent system running the fortune oracle and ambient character layer of the Attraction. Bob is the orchestrator: multi-model routing, async handoff bus, cron-scheduled operations, and real-time response. Built on the BRAINLab agent platform (Hermes gateway)."
        - generic [ref=e56]:
          - generic [ref=e57]:
            - generic [ref=e58]: Architecture
            - generic [ref=e59]: Hermes gateway · Mac Mini orchestrator
          - generic [ref=e60]:
            - generic [ref=e61]: Status
            - generic [ref=e62]: Running — nightly cron + live dispatch
      - article [ref=e63]:
        - generic [ref=e64]:
          - generic [ref=e65]: Pilot Ready
          - generic [ref=e66]: FILE — 004
        - heading "Ghost's Workshop" [level=2] [ref=e67]
        - generic [ref=e68]: Creative Systems · Content Engine
        - paragraph [ref=e69]: Creative systems and content pipeline powering the Workshop district of the Attraction. AI-assisted generation with human curation and lore consistency enforcement. Acts as internal proof-of-concept for content engine client engagements.
        - generic [ref=e70]:
          - generic [ref=e71]:
            - generic [ref=e72]: Architecture
            - generic [ref=e73]: Multi-agent creative pipeline
          - generic [ref=e74]:
            - generic [ref=e75]: Status
            - generic [ref=e76]: Pilot — not yet client-ready
      - article [ref=e77]:
        - generic [ref=e78]:
          - generic [ref=e79]: In Development
          - generic [ref=e80]: FILE — 005
        - heading "Signal Engine / Research OS" [level=2] [ref=e81]
        - generic [ref=e82]: Research OS · Knowledge Systems
        - paragraph [ref=e83]: Multi-source research synthesis, monitoring, and structured brief generation. BRAINLab's internal Research OS — ongoing monitoring across sources, AI-assisted synthesis, and scheduled brief delivery. The first Research OS track we plan to offer to external clients. Internal version running on the BRAINLab platform with Perplexity + Claude routing.
        - generic [ref=e84]:
          - generic [ref=e85]:
            - generic [ref=e86]: Architecture
            - generic [ref=e87]: Hermes · Perplexity · Claude · cron delivery
          - generic [ref=e88]:
            - generic [ref=e89]: Status
            - generic [ref=e90]: Internal — client release TBD
          - generic [ref=e91]:
            - generic [ref=e92]: Priority
            - generic [ref=e93]: First external track to ship
    - generic [ref=e94]:
      - generic [ref=e95]:
        - generic [ref=e96]: Ready to start?
        - paragraph [ref=e97]: Every client engagement begins with a mission brief. It takes 10 minutes and replaces the vague discovery call.
      - link "Start a Mission Brief →" [ref=e98] [cursor=pointer]:
        - /url: /work/intake
  - contentinfo [ref=e99]:
    - generic [ref=e100]:
      - generic [ref=e101]: Lithium Dreams Industries
      - generic [ref=e102]: Operating Systems Design
      - link "About" [ref=e103] [cursor=pointer]:
        - /url: /about
      - link "Visit the Attraction →" [ref=e104] [cursor=pointer]:
        - /url: /attraction
  - generic [ref=e107]:
    - button "Menu" [ref=e108]:
      - img [ref=e110]
      - generic: Menu
    - button "Inspect" [ref=e114]:
      - img [ref=e116]
      - generic: Inspect
    - button "Audit" [ref=e118]:
      - img [ref=e120]
      - generic: Audit
    - button "Settings" [ref=e123]:
      - img [ref=e125]
      - generic: Settings
```

# Test source

```ts
  1  | import { test, expect } from '@playwright/test';
  2  | import AxeBuilder from '@axe-core/playwright';
  3  | import path from 'path';
  4  | import fs from 'fs';
  5  | import { ROUTES } from './routes';
  6  | 
  7  | const TODAY = new Date().toISOString().split('T')[0];
  8  | const REVIEW_DIR = path.join(process.cwd(), 'reviews', `${TODAY}-opening-day`);
  9  | 
  10 | test.beforeAll(() => {
  11 |   fs.mkdirSync(REVIEW_DIR, { recursive: true });
  12 | });
  13 | 
  14 | test.describe('accessibility — axe-core', () => {
  15 |   for (const route of ROUTES) {
  16 |     test(`${route.path}`, async ({ page }) => {
  17 |       await page.goto(route.path);
  18 |       await page.waitForLoadState('networkidle');
  19 | 
  20 |       const results = await new AxeBuilder({ page })
  21 |         .withTags(['wcag2a', 'wcag2aa'])
  22 |         .analyze();
  23 | 
  24 |       // Write full results to review dir
  25 |       const outFile = path.join(REVIEW_DIR, `axe-${route.name}.json`);
  26 |       fs.writeFileSync(outFile, JSON.stringify(results, null, 2));
  27 | 
  28 |       const critical = results.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
  29 |       expect(
  30 |         critical,
  31 |         `${route.path} has ${critical.length} critical/serious a11y violations:\n` +
  32 |           critical.map(v => `  [${v.impact}] ${v.id}: ${v.description}`).join('\n')
> 33 |       ).toHaveLength(0);
     |         ^ Error: /work/case-files has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```