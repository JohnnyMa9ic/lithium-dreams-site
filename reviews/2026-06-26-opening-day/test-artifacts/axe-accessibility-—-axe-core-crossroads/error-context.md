# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /crossroads
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /crossroads has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"back-link mono\" data-astro-cid-lyw3zhkl=\"\">← Back to Midway</a>", "impact": "serious", "none": [], "target": [".back-link"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.69 (foreground color: #8a8780, background color: #2c3038, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"maintenance-tag tag--soon tag-size--md\" data-astro-cid-qv3dslcb=\"\">COMING SOON</span>", "impact": "serious", "none": [], "target": [".maintenance-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"crossroads-sub mono text-dim\" data-astro-cid-lyw3zhkl=\"\">Where everything connects. Quiet, by design.</p>", "impact": "serious", "none": [], "target": [".crossroads-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.61 (foreground color: #77736b, background color: #1a1c1f, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono text-dim\" style=\"font-size: 0.75rem; display: block; margin-top: 0.5em;\" data-astro-cid-lyw3zhkl=\"\">Do not attempt to access the Crossroads by walking directly through the back wall of the Arcade. This has not worked for anyone.</span>", "impact": "serious", "none": [], "target": [".notice-body > .text-dim.mono[data-astro-cid-lyw3zhkl=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
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
        - generic [ref=e23]: COMING SOON
      - generic [ref=e24]:
        - heading "The Crossroads" [level=1] [ref=e25]
        - paragraph [ref=e26]: Where everything connects. Quiet, by design.
      - generic [ref=e27]:
        - generic [ref=e28]: ACC. LDI-DEEP-001
        - heading "The Crossroads" [level=3] [ref=e29]
        - paragraph [ref=e30]: Deeper Lore Hub — Access Pending
        - paragraph [ref=e31]: This is the space that came after the Cathedral.
        - paragraph [ref=e32]: Breathing room. Roots instead of recursion.
        - paragraph [ref=e33]
        - paragraph [ref=e34]: The Pantheon chose this place deliberately.
        - paragraph [ref=e35]: Creativity needs somewhere it can put its hands in the dirt.
      - generic [ref=e36]:
        - generic [ref=e38]: ATTENTION
        - generic [ref=e40]:
          - strong [ref=e41]: "Status: Not yet open to the public."
          - text: The Crossroads is being prepared. Signage is going up. The fog machine is calibrated. The groundskeeper has been briefed.
          - generic [ref=e42]: Do not attempt to access the Crossroads by walking directly through the back wall of the Arcade. This has not worked for anyone.
  - contentinfo [ref=e43]:
    - generic [ref=e44]:
      - generic [ref=e45]:
        - generic [ref=e46]: Lithium Dreams Industries
        - generic [ref=e47]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e48]:
        - link "Midway" [ref=e49] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e50] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e51] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e52] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e53] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e54] [cursor=pointer]:
          - /url: /about
      - generic [ref=e55]:
        - link "Operator Notes →" [ref=e56] [cursor=pointer]:
          - /url: /work
        - generic [ref=e57]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e60]:
    - button "Menu" [ref=e61]:
      - img [ref=e63]
      - generic: Menu
    - button "Inspect" [ref=e67]:
      - img [ref=e69]
      - generic: Inspect
    - button "Audit" [ref=e71]:
      - img [ref=e73]
      - generic: Audit
    - button "Settings" [ref=e76]:
      - img [ref=e78]
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
     |         ^ Error: /crossroads has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```