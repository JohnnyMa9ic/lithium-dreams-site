# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /museum
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /museum has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 8.4pt (11.2px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"velvet-rope-notice mono text-dim\" data-astro-cid-qgnz24xd=\"\">— Please do not tap the glass. The glass is aware of you. —</div>", "impact": "serious", "none": [], "target": [".velvet-rope-notice"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"case-status mono text-dim\" data-astro-cid-qgnz24xd=\"\">// exhibit being prepared</div>", "impact": "serious", "none": [], "target": [".exhibit-case[data-astro-cid-qgnz24xd=\"\"]:nth-child(1) > .case-status.text-dim.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"case-status mono text-dim\" data-astro-cid-qgnz24xd=\"\">// access pending</div>", "impact": "serious", "none": [], "target": [".exhibit-case[data-astro-cid-qgnz24xd=\"\"]:nth-child(2) > .case-status.text-dim.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"case-status mono text-dim\" data-astro-cid-qgnz24xd=\"\">// exhibits rotating</div>", "impact": "serious", "none": [], "target": [".exhibit-case[data-astro-cid-qgnz24xd=\"\"]:nth-child(3) > .case-status.text-dim.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<div class=\"case-note mono\" data-astro-cid-qgnz24xd=\"\">", "impact": "serious", "none": [], "target": [".case-note"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.98 (foreground color: #782719, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"note-label\" data-astro-cid-qgnz24xd=\"\">CONTAINMENT STATUS:</span>", "impact": "serious", "none": [], "target": [".note-label:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.98 (foreground color: #782719, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"note-label\" data-astro-cid-qgnz24xd=\"\"> ORIGIN:</span>", "impact": "serious", "none": [], "target": [".note-label:nth-child(2)"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
    - generic [ref=e22]:
      - generic [ref=e23]:
        - navigation "Breadcrumb" [ref=e24]:
          - list [ref=e25]:
            - listitem [ref=e26]:
              - link "Home" [ref=e27] [cursor=pointer]:
                - /url: /
              - generic [ref=e28]: /
            - listitem [ref=e29]:
              - link "Midway" [ref=e30] [cursor=pointer]:
                - /url: /attraction
              - generic [ref=e31]: /
            - listitem [ref=e32]:
              - generic [ref=e33]: Museum
        - generic [ref=e34]: OPEN
      - generic [ref=e35]:
        - generic [ref=e36]: ACC. MUS-001
        - heading "Museum of Ongoing Events" [level=3] [ref=e37]
        - paragraph [ref=e38]: Curated case files, lore fragments, and a timeline we are still reconstructing.
      - generic [ref=e39]: — Please do not tap the glass. The glass is aware of you. —
      - generic [ref=e40]:
        - generic [ref=e41]:
          - generic [ref=e42]:
            - generic [ref=e43]: ACC. MUS-002
            - 'heading "Case File: Origin" [level=3] [ref=e44]'
            - paragraph [ref=e45]: Circumstances of founding — incomplete.
          - generic [ref=e46]: // exhibit being prepared
        - generic [ref=e47]:
          - generic [ref=e48]:
            - generic [ref=e49]: ACC. MUS-003
            - heading "The Crossroads Incident" [level=3] [ref=e50]
            - paragraph [ref=e51]: A record of what was left behind and why.
          - generic [ref=e52]: // access pending
        - generic [ref=e53]:
          - generic [ref=e54]:
            - generic [ref=e55]: ACC. MUS-004
            - heading "Field Reports" [level=3] [ref=e56]
            - paragraph [ref=e57]: Ongoing documentation from active operatives.
          - generic [ref=e58]: // exhibits rotating
        - generic [ref=e59]:
          - generic [ref=e60]:
            - generic [ref=e61]: ACC. MUS-005
            - heading "Goop Containment Note" [level=3] [ref=e62]
            - paragraph [ref=e63]: Greenish residue cataloged. Do not taste, touch, or compliment.
          - generic [ref=e64]:
            - text: "CONTAINMENT STATUS: Contained. ORIGIN: Unknown. TEXTURE: Consistent with itself."
            - text: "Warden note:"
            - emphasis [ref=e65]: It has not expanded. This is the best we can say.
          - generic [ref=e66]: // do not interact with exhibit
      - generic [ref=e67]:
        - paragraph [ref=e68]: Institutional History
        - paragraph [ref=e69]: A partial reconstruction. Some years are missing. The museum does not apologize for this.
        - generic [ref=e70]:
          - group [ref=e71]:
            - generic "▶ Year Zero — Founding Conditions" [ref=e72] [cursor=pointer]
          - group [ref=e73]:
            - generic "▶ Year 3 — First Expansions" [ref=e74] [cursor=pointer]
          - group [ref=e75]:
            - generic "▶ Year 7 — The Crossroads Incident" [ref=e76] [cursor=pointer]
          - group [ref=e77]:
            - generic "▶ Present — Ongoing Operations" [ref=e78] [cursor=pointer]
  - contentinfo [ref=e79]:
    - generic [ref=e80]:
      - generic [ref=e81]:
        - generic [ref=e82]: Lithium Dreams Industries
        - generic [ref=e83]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e84]:
        - link "Midway" [ref=e85] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e86] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e87] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e88] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e89] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e90] [cursor=pointer]:
          - /url: /about
      - generic [ref=e91]:
        - link "Operator Notes →" [ref=e92] [cursor=pointer]:
          - /url: /work
        - generic [ref=e93]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e96]:
    - button "Menu" [ref=e97]:
      - img [ref=e99]
      - generic: Menu
    - button "Inspect" [ref=e103]:
      - img [ref=e105]
      - generic: Inspect
    - button "Audit" [ref=e107]:
      - img [ref=e109]
      - generic: Audit
    - button "Settings" [ref=e112]:
      - img [ref=e114]
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
     |         ^ Error: /museum has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```