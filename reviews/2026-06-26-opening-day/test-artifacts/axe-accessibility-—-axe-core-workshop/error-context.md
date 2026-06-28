# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /workshop
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /workshop has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"workshop-sub mono text-dim\" data-astro-cid-s3j2uayv=\"\">Operational infrastructure. Precision. Routing. Not decorative.</p>", "impact": "serious", "none": [], "target": [".workshop-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.73 (foreground color: #1e3e48, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"log-eyebrow mono\" data-astro-cid-s3j2uayv=\"\">Maintenance Log</p>", "impact": "serious", "none": [], "target": [".log-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.87 (foreground color: #2c6170, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"entry-date mono\" data-astro-cid-s3j2uayv=\"\">Y10 — Day 203</span>", "impact": "serious", "none": [], "target": [".log-entry:nth-child(1) > .entry-date.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"entry-body mono\" data-astro-cid-s3j2uayv=\"\">Hermes gateway restarted after upstream congestion. 3 queued missions delivered on next tick.</p>", "impact": "serious", "none": [], "target": [".log-entry:nth-child(1) > .entry-body"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.87 (foreground color: #2c6170, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"entry-date mono\" data-astro-cid-s3j2uayv=\"\">Y10 — Day 198</span>", "impact": "serious", "none": [], "target": [".log-entry:nth-child(2) > .entry-date.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.11 (foreground color: #635f57, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"entry-body mono\" data-astro-cid-s3j2uayv=\"\">Signal routing paths rebuilt. Previous paths were technically working. Ghost disagreed.</p>", "impact": "serious", "none": [], "target": [".log-entry:nth-child(2) > .entry-body"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.87 (foreground color: #2c6170, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"entry-date mono\" data-astro-cid-s3j2uayv=\"\">Y10 — Day 191</span>", "impact": "serious", "none": [], "target": [".log-entry:nth-child(3) > .entry-date.mono"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
              - generic [ref=e33]: Ghost's Workshop
        - generic [ref=e34]: STAFF ONLY
      - heading "Ghost's Workshop" [level=1] [ref=e35]
      - paragraph [ref=e36]: Operational infrastructure. Precision. Routing. Not decorative.
      - generic [ref=e37]:
        - generic [ref=e39]: SYSTEM STATUS
        - generic [ref=e44]:
          - paragraph [ref=e45]: Hermes gateway — active
          - paragraph [ref=e46]: Signal routing — active
          - paragraph [ref=e47]: BrainLab infrastructure — active
          - paragraph [ref=e48]: Bob engine — active
          - paragraph [ref=e49]
          - paragraph [ref=e50]: The cold coffee on the rack is Ghost's. Do not touch it.
      - generic [ref=e51]:
        - paragraph [ref=e52]: Maintenance Log
        - generic [ref=e53]:
          - generic [ref=e54]:
            - generic [ref=e55]: Y10 — Day 203
            - paragraph [ref=e56]: Hermes gateway restarted after upstream congestion. 3 queued missions delivered on next tick.
          - generic [ref=e57]:
            - generic [ref=e58]: Y10 — Day 198
            - paragraph [ref=e59]: Signal routing paths rebuilt. Previous paths were technically working. Ghost disagreed.
          - generic [ref=e60]:
            - generic [ref=e61]: Y10 — Day 191
            - paragraph [ref=e62]: Installed badge reader at sector boundary. Badge reader immediately flagged itself. Conflict resolved.
          - generic [ref=e63]:
            - generic [ref=e64]: Y10 — Day 184
            - paragraph [ref=e65]: Bob requested a new joke module. Two approved. Sarcasm density increased by 4%.
          - generic [ref=e66]:
            - generic [ref=e67]: Y10 — Day 177
            - paragraph [ref=e68]: Cold coffee on rack replaced. Ghost put the old one back. This is a known issue. Do not escalate.
      - generic [ref=e69]:
        - paragraph [ref=e70]: Signal Feeds
        - generic [ref=e71]:
          - generic [ref=e72]:
            - generic [ref=e74]: Hermes
            - generic [ref=e76]: online
            - paragraph [ref=e77]: Gateway active. Queue nominal.
          - generic [ref=e78]:
            - generic [ref=e80]: Warden
            - generic [ref=e82]: active
            - paragraph [ref=e83]: Signal steady. Boundary patrol running.
          - generic [ref=e84]:
            - generic [ref=e86]: Reliquary
            - generic [ref=e88]: standby
            - paragraph [ref=e89]: Compute node idle. Awaiting dispatch.
          - generic [ref=e90]:
            - generic [ref=e92]: Cryptid Watch
            - generic [ref=e94]: elevated
            - paragraph [ref=e95]: Back lot activity above baseline. Within normal range.
      - generic [ref=e96]:
        - generic [ref=e98]: BADGE READER — SECTOR 7
        - generic [ref=e100]:
          - paragraph [ref=e101]: Authorized personnel only beyond this point.
          - paragraph [ref=e102]: Credential verification required. Ghost is watching.
          - link "ENTER WORKSHOP →" [ref=e103] [cursor=pointer]:
            - /url: https://cc.lithium-dreams.com/app/
            - generic [ref=e104]: ENTER WORKSHOP
            - generic [ref=e105]: →
          - paragraph [ref=e106]: Access is logged. Unauthorized entry triggers the Warden.
  - contentinfo [ref=e107]:
    - generic [ref=e108]:
      - generic [ref=e109]:
        - generic [ref=e110]: Lithium Dreams Industries
        - generic [ref=e111]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e112]:
        - link "Midway" [ref=e113] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e114] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e115] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e116] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e117] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e118] [cursor=pointer]:
          - /url: /about
      - generic [ref=e119]:
        - link "Operator Notes →" [ref=e120] [cursor=pointer]:
          - /url: /work
        - generic [ref=e121]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e124]:
    - button "Menu" [ref=e125]:
      - img [ref=e127]
      - generic: Menu
    - button "Inspect" [ref=e131]:
      - img [ref=e133]
      - generic: Inspect
    - button "Audit" [ref=e135]:
      - img [ref=e137]
      - generic: Audit
    - button "Settings" [ref=e140]:
      - img [ref=e142]
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
     |         ^ Error: /workshop has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```