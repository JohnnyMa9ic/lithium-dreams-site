# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /cathedral
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /cathedral has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.23 (foreground color: #25515e, background color: #0b0d10, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"cath-eyebrow mono\" data-astro-cid-jqtd44xh=\"\">Sector — Unclassified</p>", "impact": "serious", "none": [], "target": [".cath-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.25 (foreground color: #2f6b7c, background color: #0b0d10, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"cath-warning mono\" data-astro-cid-jqtd44xh=\"\">You were told not to follow the roots.</p>", "impact": "serious", "none": [], "target": [".cath-warning"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.65 (foreground color: #6e6b63, background color: #0b0d10, font size: 9.8pt (13.12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-jqtd44xh=\"\">This sector does not appear on the official venue map. The Warden has flagged this location for containment review since Y07. The organ plays music that has not been scheduled.</p>", "impact": "serious", "none": [], "target": [".cath-body > p:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.65 (foreground color: #6e6b63, background color: #0b0d10, font size: 9.8pt (13.12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-jqtd44xh=\"\">No incidents have been formally recorded here. This is because incidents that originate here are reclassified before they reach the log. The Warden knows. The Warden is not elaborating at this time.</p>", "impact": "serious", "none": [], "target": ["p:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.23 (foreground color: #25515e, background color: #0b0d10, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-jqtd44xh=\"\">You should not have followed the roots.</p>", "impact": "serious", "none": [], "target": [".cath-body > p:nth-child(3)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.56 (foreground color: #1c3841, background color: #0b0d10, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"cath-status mono\" data-astro-cid-jqtd44xh=\"\">Status: [REDACTED]</span>", "impact": "serious", "none": [], "target": [".cath-status"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.9 (foreground color: #42413e, background color: #0b0d10, font size: 7.4pt (9.92px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/deep-garden\" class=\"cath-back mono\" data-astro-cid-jqtd44xh=\"\">← Return to the Garden</a>", "impact": "serious", "none": [], "target": [".cath-back"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-name\" data-astro-cid-pgtvljfo=\"\">Lithium Dreams Industries</span>", "impact": "serious", "none": [], "target": [".footer-name"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-tagline mono text-dim\" data-astro-cid-pgtvljfo=\"\">The Last Roadside Attraction</span>", "impact": "serious", "none": [], "target": [".footer-tagline"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
      - paragraph [ref=e22]: Sector — Unclassified
      - heading "The Cathedral" [level=1] [ref=e23]
      - paragraph [ref=e24]: You were told not to follow the roots.
      - generic [ref=e25]:
        - paragraph [ref=e26]: This sector does not appear on the official venue map. The Warden has flagged this location for containment review since Y07. The organ plays music that has not been scheduled.
        - paragraph [ref=e27]: No incidents have been formally recorded here. This is because incidents that originate here are reclassified before they reach the log. The Warden knows. The Warden is not elaborating at this time.
        - paragraph [ref=e28]: You should not have followed the roots.
      - generic [ref=e29]:
        - generic [ref=e30]: "Status: [REDACTED]"
        - link "← Return to the Garden" [ref=e31] [cursor=pointer]:
          - /url: /deep-garden
  - contentinfo [ref=e32]:
    - generic [ref=e33]:
      - generic [ref=e34]:
        - generic [ref=e35]: Lithium Dreams Industries
        - generic [ref=e36]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e37]:
        - link "Midway" [ref=e38] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e39] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e40] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e41] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e42] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e43] [cursor=pointer]:
          - /url: /about
      - generic [ref=e44]:
        - link "Operator Notes →" [ref=e45] [cursor=pointer]:
          - /url: /work
        - generic [ref=e46]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e49]:
    - button "Menu" [ref=e50]:
      - img [ref=e52]
      - generic: Menu
    - button "Inspect" [ref=e56]:
      - img [ref=e58]
      - generic: Inspect
    - button "Audit" [ref=e60]:
      - img [ref=e62]
      - generic: Audit
    - button "Settings" [ref=e65]:
      - img [ref=e67]
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
     |         ^ Error: /cathedral has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```