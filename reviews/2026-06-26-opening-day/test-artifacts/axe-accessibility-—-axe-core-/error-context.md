# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: / has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-name\" data-astro-cid-pgtvljfo=\"\">Lithium Dreams Industries</span>", "impact": "serious", "none": [], "target": [".footer-name"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"footer-tagline mono text-dim\" data-astro-cid-pgtvljfo=\"\">The Last Roadside Attraction</span>", "impact": "serious", "none": [], "target": [".footer-tagline"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"attraction\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/museum\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Museum</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"museum\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/fortune\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Fortune</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"fortune\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/chapel\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Chapel</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"chapel\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/deep-garden\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">Garden</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"deep-garden\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"mono text-dim\" data-astro-cid-pgtvljfo=\"\">About</a>", "impact": "serious", "none": [], "target": [".mono.text-dim[href$=\"about\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/work\" class=\"footer-corp mono text-dim\" data-astro-cid-pgtvljfo=\"\">Operator Notes →</a>", "impact": "serious", "none": [], "target": [".footer-corp"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
      - generic "District shortcuts":
        - link "Gift Shop" [ref=e22] [cursor=pointer]:
          - /url: /gift-shop
          - generic: Gift Shop
        - link "Arcade" [ref=e23] [cursor=pointer]:
          - /url: /arcade
          - generic: Arcade
        - link "Museum" [ref=e24] [cursor=pointer]:
          - /url: /museum
          - generic: Museum
        - link "Bob's Fortune Emporium" [ref=e25] [cursor=pointer]:
          - /url: /fortune
          - generic: Fortune
        - link "Wedding Chapel" [ref=e26] [cursor=pointer]:
          - /url: /chapel
          - generic: Wedding Chapel
        - link "Employees Only" [ref=e27] [cursor=pointer]:
          - /url: /workshop
          - generic: Employees Only
        - link "Lost & Found — coming soon" [ref=e28] [cursor=pointer]:
          - /url: "#"
          - generic: Lost & Found
      - generic [ref=e29]:
        - generic [ref=e30]:
          - paragraph [ref=e31]:
            - text: Lithium Dreams
            - text: Industries
          - paragraph [ref=e32]: The Last Roadside Attraction
        - list "Districts" [ref=e33]:
          - listitem [ref=e34]: Cryptids.
          - listitem [ref=e35]: Arcade.
          - listitem [ref=e36]: Gift Shop.
          - listitem [ref=e37]: Weddings Tuesdays & Fridays.
        - separator [ref=e38]
        - paragraph [ref=e39]:
          - text: Words is welcome.
          - text: Curiosity is required.
          - text: Coffee is terrible.
        - link "Enter the Attraction →" [ref=e41] [cursor=pointer]:
          - /url: /attraction
        - paragraph [ref=e42]: Mind the puddles.
      - generic [ref=e43]:
        - generic [ref=e44]: Maintenance has already been notified.
        - generic [ref=e45]: Extraterrestrial parking has moved behind the chapel.
        - generic [ref=e46]: Please remain on the path.
  - contentinfo [ref=e47]:
    - generic [ref=e48]:
      - generic [ref=e49]:
        - generic [ref=e50]: Lithium Dreams Industries
        - generic [ref=e51]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e52]:
        - link "Midway" [ref=e53] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e54] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e55] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e56] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e57] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e58] [cursor=pointer]:
          - /url: /about
      - generic [ref=e59]:
        - link "Operator Notes →" [ref=e60] [cursor=pointer]:
          - /url: /work
        - generic [ref=e61]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e64]:
    - button "Menu" [ref=e65]:
      - img [ref=e67]
      - generic: Menu
    - button "Inspect" [ref=e71]:
      - img [ref=e73]
      - generic: Inspect
    - button "Audit" [ref=e75]:
      - generic [ref=e76]:
        - img [ref=e77]
        - img [ref=e80]
      - generic: Audit
    - button "Settings" [ref=e83]:
      - img [ref=e85]
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
     |         ^ Error: / has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```