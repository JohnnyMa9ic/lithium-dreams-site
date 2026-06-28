# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /work
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /work has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #ffffff, background color: #c99d4c, font size: 7.8pt (10.4px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"gh-logo-mark\" data-astro-cid-zyfjkaoe=\"\">LDI</span>", "impact": "serious", "none": [], "target": [".gh-logo-mark"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.18 (foreground color: #3d7fbd, background color: #fefefd, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/work\" class=\"active\" data-astro-cid-zyfjkaoe=\"\">Overview</a>", "impact": "serious", "none": [], "target": [".active"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.26 (foreground color: #8a8f88, background color: #fefefd, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"gh-nav-escape\" data-astro-cid-zyfjkaoe=\"\">← The Attraction</a>", "impact": "serious", "none": [], "target": [".gh-nav-escape"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.25 (foreground color: #c99d4c, background color: #f5f3ee, font size: 7.4pt (9.92px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"section-eyebrow\" data-astro-cid-nntkhrjw=\"\">What We Build</div>", "impact": "serious", "none": [], "target": ["#what-we-build > .section-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #c99d4c, background color: #ffffff, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"system-tag\" data-astro-cid-nntkhrjw=\"\">Research OS</div>", "impact": "serious", "none": [], "target": ["article:nth-child(1) > .system-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #c99d4c, background color: #ffffff, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"system-tag\" data-astro-cid-nntkhrjw=\"\">Local Business Ops</div>", "impact": "serious", "none": [], "target": ["article:nth-child(2) > .system-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #c99d4c, background color: #ffffff, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"system-tag\" data-astro-cid-nntkhrjw=\"\">Executive Assistant OS</div>", "impact": "serious", "none": [], "target": ["article:nth-child(3) > .system-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #c99d4c, background color: #ffffff, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"system-tag\" data-astro-cid-nntkhrjw=\"\">Content Engine</div>", "impact": "serious", "none": [], "target": ["article:nth-child(4) > .system-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.25 (foreground color: #c99d4c, background color: #f5f3ee, font size: 7.4pt (9.92px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"section-eyebrow\" data-astro-cid-nntkhrjw=\"\">What We're Built From</div>", "impact": "serious", "none": [], "target": [".section--materials > .section-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.25 (foreground color: #c99d4c, background color: #f5f3ee, font size: 7.4pt (9.92px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"section-eyebrow\" data-astro-cid-nntkhrjw=\"\">How We Work</div>", "impact": "serious", "none": [], "target": [".section:nth-child(4) > .section-eyebrow"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
      - generic [ref=e14]:
        - generic [ref=e15]: Glasshouse Systems Studio
        - heading "Operational systems for people who need clarity." [level=1] [ref=e16]
        - paragraph [ref=e17]: We design practical AI-supported workflows, knowledge systems, dashboards, and automation pathways for businesses that need better ways to work — without becoming technologists.
        - generic [ref=e18]:
          - link "Start a Mission Brief" [ref=e19] [cursor=pointer]:
            - /url: /work/intake
          - link "See What We Build" [ref=e20] [cursor=pointer]:
            - /url: /work/case-files
        - link "Visit the Attraction →" [ref=e21] [cursor=pointer]:
          - /url: /attraction
      - generic [ref=e24]: Systems Online
    - generic [ref=e25]:
      - generic [ref=e26]: What We Build
      - heading "Four operational system types." [level=2] [ref=e27]
      - generic [ref=e28]:
        - article [ref=e29]:
          - heading "Knowledge Systems" [level=3] [ref=e31]
          - paragraph [ref=e32]: Ongoing monitoring, synthesis, and brief generation. Second brains, documentation, institutional memory, and search infrastructure.
          - generic [ref=e33]: Research OS
        - article [ref=e34]:
          - heading "Automation Systems" [level=3] [ref=e36]
          - paragraph [ref=e37]: Lead capture, response workflows, qualification, scheduling, and follow-up. AI where it earns its place — not everywhere.
          - generic [ref=e38]: Local Business Ops
        - article [ref=e39]:
          - heading "Operator Dashboards" [level=3] [ref=e41]
          - paragraph [ref=e42]: Inbox, calendar, meeting prep, and metrics for the solo operator. Mission control systems built around how you actually work.
          - generic [ref=e43]: Executive Assistant OS
        - article [ref=e44]:
          - heading "Creative Systems" [level=3] [ref=e46]
          - paragraph [ref=e47]: Brand knowledge infrastructure, content pipelines, and long-form to short-form repurposing. Less manual assembly, more signal.
          - generic [ref=e48]: Content Engine
    - generic [ref=e49]:
      - generic [ref=e50]: What We're Built From
      - heading "The materials inform the method." [level=2] [ref=e51]
      - generic [ref=e52]:
        - generic [ref=e53]:
          - generic [ref=e54]: Walnut
          - generic [ref=e55]: Human Understanding
          - generic [ref=e56]: Every system begins with a real conversation, not a template. We map how your work actually flows before touching any tools.
        - generic [ref=e57]:
          - generic [ref=e58]: Brushed Silver
          - generic [ref=e59]: System Structure
          - generic [ref=e60]: Clean architecture, clear interfaces, and maintainable components. We build for the team that inherits it, not just the launch.
        - generic [ref=e61]:
          - generic [ref=e62]: Frosted Glass
          - generic [ref=e63]: Operational Clarity
          - generic [ref=e64]: Transparency without noise. Dashboards, outputs, and documentation that show you exactly what's working and what isn't.
        - generic [ref=e65]:
          - generic [ref=e66]: Living Green
          - generic [ref=e67]: Sustainable Adoption
          - generic [ref=e68]: Systems only work if people use them. We build for adoption, not demonstration. Complexity earns its presence.
    - generic [ref=e69]:
      - generic [ref=e70]: How We Work
      - heading "Four stages. No shortcuts." [level=2] [ref=e71]
      - generic [ref=e72]:
        - generic [ref=e73]:
          - generic [ref=e74]: "01"
          - heading "Understand" [level=3] [ref=e75]
          - paragraph [ref=e76]: Every organization already has an operating system. It lives in spreadsheets, in one employee's head, or as tribal knowledge. We uncover it before we touch anything.
        - generic [ref=e78]:
          - generic [ref=e79]: "02"
          - heading "Design" [level=3] [ref=e80]
          - paragraph [ref=e81]: We improve it, document it, and map the gaps. Structure before tools. Clarity before complexity. The design phase is where most of the value lives.
        - generic [ref=e83]:
          - generic [ref=e84]: "03"
          - heading "Build" [level=3] [ref=e85]
          - paragraph [ref=e86]: Then we build the infrastructure that allows it to scale. Maintainable systems. Human-centered automation. Work that outlives the people who started it.
        - generic [ref=e88]:
          - generic [ref=e89]: "04"
          - heading "Operate" [level=3] [ref=e90]
          - paragraph [ref=e91]: Clean handoff with full documentation. Ongoing async support. We stay until it runs without us — and we check in to make sure it still does.
    - generic [ref=e92]:
      - generic [ref=e93]: Internal Deployments
      - heading "We build on our own systems first." [level=2] [ref=e94]
      - paragraph [ref=e95]: Before deploying to clients, every system runs internally. These are our current live deployments.
      - generic [ref=e96]:
        - generic [ref=e97]:
          - generic [ref=e98]: Operational
          - generic [ref=e99]: LDI Website
          - generic [ref=e100]: This site. Astro + Cloudflare Pages. Design system and content pipeline operating end-to-end.
        - generic [ref=e101]:
          - generic [ref=e102]: Operational
          - generic [ref=e103]: Mission Intake Pipeline
          - generic [ref=e104]: The intake wizard on this site feeds directly into a structured JSON pipeline. Webhook delivery in active development.
        - generic [ref=e105]:
          - generic [ref=e106]: Pilot Ready
          - generic [ref=e107]: Ghost's Workshop
          - generic [ref=e108]: Creative systems and content pipeline powering the Workshop district of the Attraction. AI-assisted but human-curated.
        - generic [ref=e109]:
          - generic [ref=e110]: Operational
          - generic [ref=e111]: Bob's Fortune Emporium
          - generic [ref=e112]: Autonomous agent system running the fortune oracle and the Attraction's real-time ambient character layer.
        - generic [ref=e113]:
          - generic [ref=e114]: In Development
          - generic [ref=e115]: Signal Engine / Research OS
          - generic [ref=e116]: Multi-source research synthesis, monitoring, and brief generation system. BRAINLab's internal Research OS — the first track we ship to external clients.
      - link "View all Case Files →" [ref=e117] [cursor=pointer]:
        - /url: /work/case-files
    - generic [ref=e119]:
      - generic [ref=e120]:
        - generic [ref=e121]: About
        - heading "Built by an operator, not an AI tourist." [level=2] [ref=e122]
        - paragraph [ref=e123]: LDI is a systems design practice. AI is one of our tools — not our product and not our identity. We design practical operational systems for people who need clarity about how their work actually happens, and want infrastructure that scales without becoming their full-time job.
        - paragraph [ref=e124]: Every client system we pitch, we've already run internally. If it doesn't survive contact with real operations, we don't sell it.
      - generic [ref=e125]:
        - link "Start a Mission Brief" [ref=e126] [cursor=pointer]:
          - /url: /work/intake
        - paragraph [ref=e127]: A 10-minute structured intake that replaces the vague discovery call.
  - contentinfo [ref=e128]:
    - generic [ref=e129]:
      - generic [ref=e130]: Lithium Dreams Industries
      - generic [ref=e131]: Operating Systems Design
      - link "About" [ref=e132] [cursor=pointer]:
        - /url: /about
      - link "Visit the Attraction →" [ref=e133] [cursor=pointer]:
        - /url: /attraction
  - generic [ref=e136]:
    - button "Menu" [ref=e137]:
      - img [ref=e139]
      - generic: Menu
    - button "Inspect" [ref=e143]:
      - img [ref=e145]
      - generic: Inspect
    - button "Audit" [ref=e147]:
      - img [ref=e149]
      - generic: Audit
    - button "Settings" [ref=e152]:
      - img [ref=e154]
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
     |         ^ Error: /work has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```