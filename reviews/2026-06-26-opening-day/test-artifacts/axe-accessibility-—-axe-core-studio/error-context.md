# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /studio
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /studio has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.59 (foreground color: #363432, background color: #0a0a0c, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"studio-back mono\" data-astro-cid-32dw5vra=\"\">← About</a>", "impact": "serious", "none": [], "target": [".studio-back"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">01</span>", "impact": "serious", "none": [], "target": [".studio-link--active > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">02</span>", "impact": "serious", "none": [], "target": ["a[href$=\"field-notes\"] > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">Field Notes</span>", "impact": "serious", "none": [], "target": ["a[href$=\"field-notes\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">03</span>", "impact": "serious", "none": [], "target": ["a[href$=\"infrastructure\"] > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">Infrastructure</span>", "impact": "serious", "none": [], "target": ["a[href$=\"infrastructure\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">About</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"about\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.03 (foreground color: #584013, background color: #0a0a0c, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"section-num mono\" data-astro-cid-cwimmrs4=\"\">01</span>", "impact": "serious", "none": [], "target": [".studio-section:nth-child(2) > .section-header > .section-num.mono"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
    - generic [ref=e23]:
      - paragraph [ref=e24]: Lithium Dreams Industries · Studio
      - heading "The Story" [level=1] [ref=e25]
      - paragraph [ref=e26]: Where the work comes from. What it's for. Why the attraction exists at all.
    - navigation "Studio section navigation" [ref=e27]:
      - link "← About" [ref=e28] [cursor=pointer]:
        - /url: /about
      - generic [ref=e29]:
        - link "01 The Story" [ref=e30] [cursor=pointer]:
          - /url: /studio
          - generic [ref=e31]: "01"
          - generic [ref=e32]: The Story
        - link "02 Field Notes" [ref=e33] [cursor=pointer]:
          - /url: /studio/field-notes
          - generic [ref=e34]: "02"
          - generic [ref=e35]: Field Notes
        - link "03 Infrastructure" [ref=e36] [cursor=pointer]:
          - /url: /studio/infrastructure
          - generic [ref=e37]: "03"
          - generic [ref=e38]: Infrastructure
    - generic [ref=e39]:
      - navigation "Breadcrumb" [ref=e40]:
        - list [ref=e41]:
          - listitem [ref=e42]:
            - link "Home" [ref=e43] [cursor=pointer]:
              - /url: /
            - generic [ref=e44]: /
          - listitem [ref=e45]:
            - link "About" [ref=e46] [cursor=pointer]:
              - /url: /about
            - generic [ref=e47]: /
          - listitem [ref=e48]:
            - generic [ref=e49]: Studio
      - generic [ref=e50]:
        - generic [ref=e51]:
          - generic [ref=e52]: "01"
          - heading "Origin" [level=2] [ref=e53]
        - generic [ref=e54]:
          - paragraph [ref=e55]: Lithium Dreams Industries started as a tooling problem. Too many things needed to talk to each other, and none of the off-the-shelf solutions understood the shape of the work. So the work built its own infrastructure. Then the infrastructure needed documentation. Then the documentation needed a face. Then the face needed a parking lot and a back lot and a cryptid, and here we are.
          - paragraph [ref=e56]: "The studio is one person with three agents and a collection of machines that collectively constitute something approaching a functional creative practice. The work is operational in the broadest sense: systems that route information, surface signals, and make it possible for a person to think clearly without holding everything in their head at once."
          - paragraph [ref=e57]: "The name came from the intersection of two things: a specific kind of energy — low-voltage, steady, sufficient — and the particular weight of a dream that has been refined down from aspiration into something more like intention. The Industries part is aspirational in the truest sense. It will earn it."
      - generic [ref=e58]:
        - generic [ref=e59]:
          - generic [ref=e60]: "02"
          - heading "The Work" [level=2] [ref=e61]
        - generic [ref=e62]:
          - paragraph [ref=e63]: "LDI designs operational systems. Practically: workflows, dashboards, dispatch pipelines, integration layers — the plumbing that lets a person or a small team function above their weight class. The Glasshouse Studio side of this site is the professional-facing version of this work. Clear, competent, glass-and-brass."
          - paragraph [ref=e64]: But the work is also research — a running field study in what it means to build with AI agents that are neither tools nor colleagues but something in between. Bob dispatches missions. Ghost maintains the infrastructure. The Warden logs what crosses the boundary. The Operator watches all three and tries to understand what's working and what's just very confident noise.
          - paragraph [ref=e65]: "And the work is physical. The Object Lab runs 3D fabrication out of the same infrastructure: printed structures, cast collectibles, numbered architectural models, custom pieces made to order. Physical objects made by the same system that routes the digital work. The gift shop is real."
          - paragraph [ref=e66]: The Attraction is the laboratory condition for all of it. If the system can support a back story, it can support a business. If it can route a mission to Bob and get a receipt, it can route a purchase order and get an invoice. The strange use case is the stress test for the serious one.
      - generic [ref=e67]:
        - generic [ref=e68]:
          - generic [ref=e69]: "03"
          - heading "The Aesthetic" [level=2] [ref=e70]
        - generic [ref=e71]:
          - paragraph [ref=e72]: Dark because clarity requires contrast. Amber because warm light is honest. Monospace because exact language matters. The lore-forward presentation of the site isn't irony — it's a decision about what kind of attention to reward. Someone who arrives at the Attraction and engages with it is the kind of person worth working with.
          - paragraph [ref=e73]: The roadside attraction is a specifically American form — the thing that appeared between the highway and the possibility of anywhere, offering something impractical but memorable. The cryptid, the giant statue, the mystery spot. These things persist not because they're useful but because they're real in a way that useful things sometimes fail to be.
          - paragraph [ref=e74]: "LDI is interested in that quality. A system that works is necessary. A system that works and means something is what the studio is for. The physical objects in the shop follow the same rule: made to last, made to mean something, made here."
      - generic [ref=e75]:
        - generic [ref=e76]:
          - generic [ref=e77]: "04"
          - heading "Year Log" [level=2] [ref=e78]
        - paragraph [ref=e79]: Studio history in lore time. Events happened in the sequence listed.
        - generic [ref=e80]:
          - generic [ref=e81]:
            - generic [ref=e83]: Y01
            - generic [ref=e85]:
              - heading "First signal" [level=3] [ref=e86]
              - paragraph [ref=e87]: Studio founded. First system shipped. The work begins before the name does. The name arrives later, when it becomes clear this is not a phase.
          - generic [ref=e88]:
            - generic [ref=e90]: Y03
            - generic [ref=e92]:
              - heading "The Attraction opens" [level=3] [ref=e93]
              - paragraph [ref=e94]: The lore layer arrives — a way to explain the infrastructure to people who don't need to know how it works, only that it does. The Chapel performs its first ceremony. The organ plays something unscheduled. This is logged as normal.
          - generic [ref=e95]:
            - generic [ref=e97]: Y05
            - generic [ref=e99]:
              - heading "Agents formalized" [level=3] [ref=e100]
              - paragraph [ref=e101]: Bob takes the dispatch role. Ghost assumes the Workshop. The Warden formalizes boundary protocols after an incident in the back lot. The incident is classified. The Warden's report is not.
          - generic [ref=e102]:
            - generic [ref=e104]: Y07
            - generic [ref=e106]:
              - heading "Reliquary online" [level=3] [ref=e107]
              - paragraph [ref=e108]: Second compute node. Cross-machine handoff reaches stability after three attempts and one memorable failure. The Museum opens with three exhibits, one of which is immediately flagged for containment review.
          - generic [ref=e109]:
            - generic [ref=e111]: Y08
            - generic [ref=e113]:
              - heading "Signal taxonomy + fabrication" [level=3] [ref=e114]
              - paragraph [ref=e115]: "Field notes formalized into a system. The Object Lab opens — physical production of LDI artifacts: printed structures, cast collectibles, numbered editions. The gift shop gets its first non-ironic inventory."
          - generic [ref=e116]:
            - generic [ref=e118]: Y10
            - generic [ref=e120]:
              - heading "Current" [level=3] [ref=e121]
              - paragraph [ref=e122]: Three machines. Three agents. One attraction. Two open incidents. A growing catalog of physical objects made here and available to take home. The goop situation remains under review.
      - generic [ref=e123]:
        - link "Glasshouse Studio Work with LDI → Operational systems design for people who need clarity" [ref=e124] [cursor=pointer]:
          - /url: /work
          - generic [ref=e125]:
            - generic [ref=e126]: Glasshouse Studio
            - generic [ref=e127]: Work with LDI →
            - generic [ref=e128]: Operational systems design for people who need clarity
        - link "Object Lab The Gift Shop → 3D-printed collectibles, architectural models, numbered editions made here" [ref=e129] [cursor=pointer]:
          - /url: /gift-shop
          - generic [ref=e130]:
            - generic [ref=e131]: Object Lab
            - generic [ref=e132]: The Gift Shop →
            - generic [ref=e133]: 3D-printed collectibles, architectural models, numbered editions made here
  - contentinfo [ref=e134]:
    - generic [ref=e135]:
      - generic [ref=e136]:
        - generic [ref=e137]: Lithium Dreams Industries
        - generic [ref=e138]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e139]:
        - link "Midway" [ref=e140] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e141] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e142] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e143] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e144] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e145] [cursor=pointer]:
          - /url: /about
      - generic [ref=e146]:
        - link "Operator Notes →" [ref=e147] [cursor=pointer]:
          - /url: /work
        - generic [ref=e148]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e151]:
    - button "Menu" [ref=e152]:
      - img [ref=e154]
      - generic: Menu
    - button "Inspect" [ref=e158]:
      - img [ref=e160]
      - generic: Inspect
    - button "Audit" [ref=e162]:
      - img [ref=e164]
      - generic: Audit
    - button "Settings" [ref=e167]:
      - img [ref=e169]
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
     |         ^ Error: /studio has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```