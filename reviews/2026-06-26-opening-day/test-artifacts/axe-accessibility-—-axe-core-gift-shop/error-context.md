# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /gift-shop
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /gift-shop has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"back-link mono\" data-astro-cid-6gxwtk4r=\"\">← Back to Midway</a>", "impact": "serious", "none": [], "target": [".back-link"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"mono text-dim\" data-astro-cid-6gxwtk4r=\"\">// merchandise coming soon</p>", "impact": "serious", "none": [], "target": [".placeholder-shelf > p:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"mono text-dim\" data-astro-cid-6gxwtk4r=\"\">// field notes · stickers · patches · realm records</p>", "impact": "serious", "none": [], "target": [".placeholder-shelf > p:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"mono text-dim\" data-astro-cid-6gxwtk4r=\"\">// no refunds after portal exposure</p>", "impact": "serious", "none": [], "target": [".placeholder-shelf > p:nth-child(3)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-name\" data-astro-cid-pgtvljfo=\"\">Lithium Dreams Industries</span>", "impact": "serious", "none": [], "target": [".footer-name"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-tagline mono text-dim\" data-astro-cid-pgtvljfo=\"\">The Last Roadside Attraction</span>", "impact": "serious", "none": [], "target": [".footer-tagline"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".text-dim.mono[href$=\"attraction\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/museum\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Museum</a>", "impact": "serious", "none": [], "target": [".text-dim.mono[href$=\"museum\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/fortune\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Fortune</a>", "impact": "serious", "none": [], "target": [".text-dim.mono[href$=\"fortune\"]"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
    - generic [ref=e20]:
      - generic [ref=e21]:
        - link "← Back to Midway" [ref=e22] [cursor=pointer]:
          - /url: /attraction
        - generic [ref=e23]: OPEN
      - generic [ref=e24]:
        - generic [ref=e25]: ACC. GS-001
        - heading "Gift Shop" [level=3] [ref=e26]
        - paragraph [ref=e27]: Souvenirs, field notes, stickers, and objects we are legally allowed to sell.
      - generic [ref=e28]:
        - generic [ref=e29]:
          - generic [ref=e31]: Notice to Visitors
          - generic [ref=e33]:
            - paragraph [ref=e34]: The gift shop is open. The register is staffed by someone who has been here a very long time.
            - paragraph [ref=e35]: Please do not ask about the clearance bin in the back.
        - generic [ref=e36]:
          - paragraph [ref=e37]: // merchandise coming soon
          - paragraph [ref=e38]: // field notes · stickers · patches · realm records
          - paragraph [ref=e39]: // no refunds after portal exposure
  - contentinfo [ref=e40]:
    - generic [ref=e41]:
      - generic [ref=e42]:
        - generic [ref=e43]: Lithium Dreams Industries
        - generic [ref=e44]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e45]:
        - link "Midway" [ref=e46] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e47] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e48] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e49] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e50] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e51] [cursor=pointer]:
          - /url: /about
      - generic [ref=e52]:
        - link "Operator Notes →" [ref=e53] [cursor=pointer]:
          - /url: /work
        - generic [ref=e54]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e57]:
    - button "Menu" [ref=e58]:
      - img [ref=e60]
      - generic: Menu
    - button "Inspect" [ref=e64]:
      - img [ref=e66]
      - generic: Inspect
    - button "Audit" [ref=e68]:
      - img [ref=e70]
      - generic: Audit
    - button "Settings" [ref=e73]:
      - img [ref=e75]
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
     |         ^ Error: /gift-shop has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```