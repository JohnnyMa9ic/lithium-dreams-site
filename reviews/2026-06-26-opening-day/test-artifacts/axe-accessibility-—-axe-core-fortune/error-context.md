# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /fortune
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /fortune has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"emporium-sub mono text-dim\" data-astro-cid-4cephfxv=\"\">Temporarily sentient. Results vary. Bob is not liable.</p>", "impact": "serious", "none": [], "target": [".emporium-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-4cephfxv=\"\">One question at a time. Bob is not a search engine.</li>", "impact": "serious", "none": [], "target": [".rules-list > li:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-4cephfxv=\"\">The fortune is final. Disputes go to the Lost &amp; Found.</li>", "impact": "serious", "none": [], "target": [".rules-list > li:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-4cephfxv=\"\">Do not tap the cabinet. It is aware of you.</li>", "impact": "serious", "none": [], "target": [".rules-list > li:nth-child(3)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-4cephfxv=\"\">Bob's sarcasm module is a feature, not a flaw. Management has been informed.</li>", "impact": "serious", "none": [], "target": ["li:nth-child(4)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.28 (foreground color: #4e3d20, background color: #b5893e, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"fortune-number\" data-astro-cid-sy4fch57=\"\">#09</span>", "impact": "serious", "none": [], "target": [".fortune-number"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.03 (foreground color: #e5dac0, background color: #e3d6ba, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono text-dim\" style=\"font-size:0.6rem;\" data-astro-cid-sy4fch57=\"\">BOB'S FORTUNE EMPORIUM — EST. PROBABLY</span>", "impact": "serious", "none": [], "target": [".fortune-footer[data-astro-cid-sy4fch57=\"\"] > span[data-astro-cid-sy4fch57=\"\"]"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
              - generic [ref=e33]: Bob's Fortune Emporium
        - generic [ref=e34]: UNSTABLE
      - generic [ref=e35]:
        - heading "Bob's Fortune Emporium" [level=1] [ref=e36]:
          - text: Bob's Fortune
          - text: Emporium
        - paragraph [ref=e37]: Temporarily sentient. Results vary. Bob is not liable.
      - generic [ref=e38]:
        - generic [ref=e40]: Machine Status
        - generic [ref=e42]:
          - paragraph [ref=e43]: The cabinet is operational. The cabinet is also having a moment. Please insert your question and pull the lever.
          - paragraph [ref=e44]: Bob says this is probably fine.
      - generic [ref=e45]:
        - paragraph [ref=e46]: House Rules
        - list [ref=e47]:
          - listitem [ref=e48]: One question at a time. Bob is not a search engine.
          - listitem [ref=e49]: The fortune is final. Disputes go to the Lost & Found.
          - listitem [ref=e50]: Do not tap the cabinet. It is aware of you.
          - listitem [ref=e51]: Bob's sarcasm module is a feature, not a flaw. Management has been informed.
      - generic [ref=e53]:
        - generic [ref=e54]:
          - generic [ref=e55]: FORTUNE
          - generic [ref=e56]: "#09"
        - paragraph [ref=e58]: Bob says the answer is probably behind the snack counter. Bob is not allowed behind the snack counter.
        - generic [ref=e59]: BOB'S FORTUNE EMPORIUM — EST. PROBABLY
      - paragraph [ref=e60]: — Lever mechanism under maintenance. Fortune dispensed automatically. —
      - generic [ref=e61]:
        - generic [ref=e62]:
          - paragraph [ref=e63]: Ask Bob
          - paragraph [ref=e64]: Bob will probably make fun of it. That's part of the service.
          - generic [ref=e65]:
            - textbox "Type your question here..." [ref=e66]
            - button "Submit Question" [ref=e67] [cursor=pointer]
        - generic [ref=e69]:
          - generic [ref=e70]:
            - paragraph [ref=e71]: Recent Fortunes
            - generic [ref=e72]:
              - paragraph [ref=e73]: "\"Your next idea is better than your last one.\""
              - paragraph [ref=e74]: "\"Something you lost is not lost. It is waiting.\""
              - paragraph [ref=e75]: "\"The fog is not hiding anything. The fog is just the fog.\""
            - link "Fortune Archive →" [ref=e76] [cursor=pointer]:
              - /url: "#"
          - generic [ref=e77]:
            - paragraph [ref=e78]: Service Notes
            - paragraph [ref=e79]: // Replaced jaw servo. Again.
            - paragraph [ref=e80]: // Lubricated gears (10W-30, per spec).
            - paragraph [ref=e81]: // Bob insisted on new jokes. Two approved.
            - paragraph [ref=e82]: "// Sarcasm module: operational. As expected."
  - contentinfo [ref=e83]:
    - generic [ref=e84]:
      - generic [ref=e85]:
        - generic [ref=e86]: Lithium Dreams Industries
        - generic [ref=e87]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e88]:
        - link "Midway" [ref=e89] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e90] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e91] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e92] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e93] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e94] [cursor=pointer]:
          - /url: /about
      - generic [ref=e95]:
        - link "Operator Notes →" [ref=e96] [cursor=pointer]:
          - /url: /work
        - generic [ref=e97]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e100]:
    - button "Menu" [ref=e101]:
      - img [ref=e103]
      - generic: Menu
    - button "Inspect" [ref=e107]:
      - img [ref=e109]
      - generic: Inspect
    - button "Audit" [ref=e111]:
      - generic [ref=e112]:
        - img [ref=e113]
        - img [ref=e116]
      - generic: Audit
    - button "Settings" [ref=e119]:
      - img [ref=e121]
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
     |         ^ Error: /fortune has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```