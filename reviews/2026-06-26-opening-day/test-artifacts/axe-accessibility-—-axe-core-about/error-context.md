# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /about
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /about has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.94 (foreground color: #816020, background color: #1a1c1f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"hero-eyebrow mono\" data-astro-cid-ta2fbyqs=\"\">Est. Year 1</p>", "impact": "serious", "none": [], "target": [".hero-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.71 (foreground color: #62605a, background color: #1a1c1f, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"hero-sub\" data-astro-cid-ta2fbyqs=\"\">Operational systems. Multi-agent infrastructure. Physical fabrication. One operator.</p>", "impact": "serious", "none": [], "target": [".hero-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.32 (foreground color: #634814, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"section-mark mono\" data-astro-cid-ta2fbyqs=\"\">01 — The Operator</div>", "impact": "serious", "none": [], "target": [".about-section:nth-child(2) > .section-mark.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"meta-role mono text-dim\" data-astro-cid-ta2fbyqs=\"\">Founder / Operator</span>", "impact": "serious", "none": [], "target": [".meta-role"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/studio\" class=\"cta-link cta--dim\" data-astro-cid-ta2fbyqs=\"\">Read the full studio story →</a>", "impact": "serious", "none": [], "target": ["a[href$=\"studio\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"cta-link cta--dim\" data-astro-cid-ta2fbyqs=\"\">See the Attraction →</a>", "impact": "serious", "none": [], "target": [".cta--dim.cta-link[href$=\"attraction\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.32 (foreground color: #634814, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"section-mark mono\" data-astro-cid-ta2fbyqs=\"\">02 — The Mission</div>", "impact": "serious", "none": [], "target": [".about-section:nth-child(3) > .section-mark.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.84 (foreground color: #8f6618, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"pillar-label mono\" data-astro-cid-ta2fbyqs=\"\">Operational clarity</span>", "impact": "serious", "none": [], "target": [".pillar:nth-child(1) > .pillar-label.mono"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - link "Skip to main content" [ref=e2] [cursor=pointer]:
    - /url: "#main-content"
  - navigation [ref=e3]:
    - link "Lithium Dreams Industries" [ref=e4] [cursor=pointer]:
      - /url: /
      - generic [ref=e5]: Lithium Dreams
      - generic [ref=e6]: Industries
    - generic [ref=e7]:
      - link "Attraction" [ref=e8] [cursor=pointer]:
        - /url: /attraction
      - link "Gift Shop" [ref=e9] [cursor=pointer]:
        - /url: /gift-shop
      - link "Arcade" [ref=e10] [cursor=pointer]:
        - /url: /arcade
      - link "Museum" [ref=e11] [cursor=pointer]:
        - /url: /museum
      - link "Fortune" [ref=e12] [cursor=pointer]:
        - /url: /fortune
      - link "Chapel" [ref=e13] [cursor=pointer]:
        - /url: /chapel
      - link "Garden" [ref=e14] [cursor=pointer]:
        - /url: /deep-garden
      - link "Employees Only" [ref=e15] [cursor=pointer]:
        - /url: /employees-only
      - link "About" [ref=e16] [cursor=pointer]:
        - /url: /about
    - link "LDI" [ref=e18] [cursor=pointer]:
      - /url: /work
  - main [ref=e19]:
    - generic [ref=e21]:
      - paragraph [ref=e22]: Est. Year 1
      - heading "About LDI" [level=1] [ref=e23]
      - paragraph [ref=e24]: Operational systems. Multi-agent infrastructure. Physical fabrication. One operator.
    - generic [ref=e27]:
      - navigation "Breadcrumb" [ref=e28]:
        - list [ref=e29]:
          - listitem [ref=e30]:
            - link "Home" [ref=e31] [cursor=pointer]:
              - /url: /
            - generic [ref=e32]: /
          - listitem [ref=e33]:
            - generic [ref=e34]: About
      - generic [ref=e35]:
        - generic [ref=e36]: 01 — The Operator
        - generic [ref=e37]:
          - generic [ref=e38]:
            - img "The Operator — hands writing in a notebook" [ref=e39]
            - generic [ref=e40]:
              - generic [ref=e41]: J. Burroughs
              - generic [ref=e42]: Founder / Operator
          - generic [ref=e43]:
            - paragraph [ref=e44]: "LDI is the operational practice of J. Burroughs — a systems designer with extensive experience running complex, multi-vendor environments at the institutional scale. The background is healthcare supply chain and procurement: high-stakes coordination, real constraints, the specific discipline of keeping systems functional under conditions they weren't designed for."
            - paragraph [ref=e45]: That work produced a methodology. Build for clarity first. Automate second. Keep the human in the loop always. LDI applies that methodology beyond its institutional origin — to any environment where the infrastructure has gotten ahead of the ability to see it clearly.
            - paragraph [ref=e46]: The current LDI stack runs a three-agent AI orchestration system (BRAINLab) across three machines. Bob handles dispatch and mission routing. Ghost maintains signal path integrity. The Warden monitors the perimeter. The Operator watches all three and tries to distinguish working systems from very confident noise.
            - paragraph [ref=e47]: "The Object Lab produces physical work from the same infrastructure: 3D-printed structures, cast collectibles, numbered editions made here. The Glasshouse Studio applies the same methodology to client work — operational clarity for people who need an enterprise-grade system without an enterprise department to run it."
            - generic [ref=e48]:
              - link "Work with LDI →" [ref=e49] [cursor=pointer]:
                - /url: /work
              - link "Read the full studio story →" [ref=e50] [cursor=pointer]:
                - /url: /studio
              - link "See the Attraction →" [ref=e51] [cursor=pointer]:
                - /url: /attraction
      - generic [ref=e52]:
        - generic [ref=e53]: 02 — The Mission
        - generic [ref=e54]:
          - blockquote [ref=e55]: "\"We build systems that hold up under strange conditions — because most conditions are stranger than they look.\""
          - generic [ref=e56]:
            - generic [ref=e57]:
              - generic [ref=e58]: Operational clarity
              - paragraph [ref=e59]: Systems that can be understood, traced, and corrected by a person at 2am without reading the source code.
            - generic [ref=e60]:
              - generic [ref=e61]: Infrastructure as material
              - paragraph [ref=e62]: The plumbing is the art. Routing, dispatching, logging — these are design decisions, not utility decisions.
            - generic [ref=e63]:
              - generic [ref=e64]: Human-in-the-loop
              - paragraph [ref=e65]: Agents are workers. The human is the architect. Nothing runs autonomously that hasn't earned it.
      - generic [ref=e66]:
        - generic [ref=e67]: 03 — The Operating Layer
        - paragraph [ref=e68]: LDI runs on a three-agent stack. They are listed here for transparency. Do not ask them to take the day off.
        - generic [ref=e69]:
          - generic [ref=e70]:
            - generic [ref=e72]: Bob
            - generic [ref=e74]: Quarterback / Orchestrator
            - paragraph [ref=e75]: Primary dispatch agent. Routes missions, runs research, manages the queue. When something needs to get done and no one's looking, Bob handles it. He does not wear a suit.
            - generic [ref=e76]: Mac Mini — always on
          - generic [ref=e77]:
            - generic [ref=e79]: Ghost
            - generic [ref=e81]: Infrastructure / Signal Routing
            - paragraph [ref=e82]: Keeps the pipes clean. Handles gateway maintenance, signal path integrity, and the cold coffee situation in the Workshop. Ghost does not explain himself. He doesn't need to.
            - link "Workshop — operational" [ref=e84] [cursor=pointer]:
              - /url: /workshop
          - generic [ref=e85]:
            - generic [ref=e87]: Warden
            - generic [ref=e89]: Boundary Patrol / Access
            - paragraph [ref=e90]: Monitors the perimeter, logs access events, and reports anomalies to the Operator. Warden patrols the boundary between the known and whatever that is in the back lot.
            - generic [ref=e91]: All sectors — active
      - generic [ref=e92]:
        - generic [ref=e93]: 04 — The Attraction
        - generic [ref=e94]:
          - paragraph [ref=e95]: The Last Roadside Attraction at the Edge of the Universe has been operating continuously since Year 1. Current cryptid count is undisclosed. The back lot is not part of the venue. The Goop Containment is under review.
          - paragraph [ref=e96]: This site is the public-facing layer of LDI's operational infrastructure. The Attraction is real. The Arcade is real. Bob is real in the ways that matter. We are less certain about the Chapel organ.
          - generic [ref=e97]:
            - link "Enter the Attraction →" [ref=e98] [cursor=pointer]:
              - /url: /attraction
            - link "Glasshouse Studio →" [ref=e99] [cursor=pointer]:
              - /url: /work
  - contentinfo [ref=e100]:
    - generic [ref=e101]:
      - generic [ref=e102]:
        - generic [ref=e103]: Lithium Dreams Industries
        - generic [ref=e104]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e105]:
        - link "Midway" [ref=e106] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e107] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e108] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e109] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e110] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e111] [cursor=pointer]:
          - /url: /about
      - generic [ref=e112]:
        - link "Operator Notes →" [ref=e113] [cursor=pointer]:
          - /url: /work
        - generic [ref=e114]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e117]:
    - button "Menu" [ref=e118]:
      - img [ref=e120]
      - generic: Menu
    - button "Inspect" [ref=e124]:
      - img [ref=e126]
      - generic: Inspect
    - button "Audit" [ref=e128]:
      - generic [ref=e129]:
        - img [ref=e130]
        - img [ref=e133]
      - generic: Audit
    - button "Settings" [ref=e136]:
      - img [ref=e138]
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
     |         ^ Error: /about has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```