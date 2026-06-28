# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /chapel
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /chapel has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 8.4pt (11.2px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-qek4hjtj=\"\">// Appointments available Tuesdays and Fridays</p>", "impact": "serious", "none": [], "target": [".chapel-notice > p:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 8.4pt (11.2px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-qek4hjtj=\"\">// Please do not ask about <a href=\"/chapel/back-room\" class=\"backroom-link\" data-astro-cid-qek4hjtj=\"\">the back room</a></p>", "impact": "serious", "none": [], "target": [".chapel-notice > p:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 8.4pt (11.2px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/chapel/back-room\" class=\"backroom-link\" data-astro-cid-qek4hjtj=\"\">the back room</a>", "impact": "serious", "none": [], "target": [".backroom-link"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 8.4pt (11.2px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p data-astro-cid-qek4hjtj=\"\">// Rice provided. Cleanup is your responsibility.</p>", "impact": "serious", "none": [], "target": [".chapel-notice > p:nth-child(3)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.88 (foreground color: #423f3b, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"book-eyebrow mono\" data-astro-cid-qek4hjtj=\"\">Guest Registry</p>", "impact": "serious", "none": [], "target": [".book-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"book-note text-dim\" data-astro-cid-qek4hjtj=\"\">These people were married here. We have no reason to doubt them.</p>", "impact": "serious", "none": [], "target": [".book-note"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"entry-date mono text-dim\" data-astro-cid-qek4hjtj=\"\">Year 4 — Tuesday</span>", "impact": "serious", "none": [], "target": [".book-entry[data-astro-cid-qek4hjtj=\"\"]:nth-child(1) > .entry-date.text-dim.mono"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
              - generic [ref=e33]: Wedding Chapel
        - generic [ref=e34]: BY APPOINTMENT
      - generic [ref=e35]:
        - generic [ref=e36]: ACC. CHPL-001
        - heading "Roadside Wedding Chapel" [level=3] [ref=e37]
        - paragraph [ref=e38]: Open Tuesdays and Fridays. Do not ask about the back room.
      - generic [ref=e39]:
        - generic [ref=e40]:
          - generic [ref=e42]: Ceremony Packages
          - generic [ref=e44]:
            - paragraph [ref=e45]: "Standard: $12 — includes ceremony, witness signature (one cryptid), and a laminated certificate."
            - paragraph [ref=e46]: "Deluxe: $18 — includes above, plus use of the plastic flowers and two folding chairs."
            - paragraph [ref=e47]: The organ plays by itself. This is normal.
        - generic [ref=e48]:
          - paragraph [ref=e49]: // Appointments available Tuesdays and Fridays
          - paragraph [ref=e50]:
            - text: // Please do not ask about
            - link "the back room" [ref=e51] [cursor=pointer]:
              - /url: /chapel/back-room
          - paragraph [ref=e52]: // Rice provided. Cleanup is your responsibility.
        - generic [ref=e53]:
          - generic [ref=e55]: Officiants on File
          - generic [ref=e57]:
            - paragraph [ref=e58]: Bob is licensed in this state and two others he won't name. He does not wear a suit. He does wear his badge. The ceremony will be brief, correct, and memorable in ways you may not anticipate.
            - paragraph [ref=e59]: Bob does not do destination weddings. Bob also does not explain why.
        - generic [ref=e60]:
          - paragraph [ref=e61]: Guest Registry
          - paragraph [ref=e62]: These people were married here. We have no reason to doubt them.
          - generic [ref=e63]:
            - generic [ref=e64]:
              - generic [ref=e65]: T. Hargrove & M. Hargrove
              - generic [ref=e66]: Year 4 — Tuesday
              - paragraph [ref=e67]: "\"The organ played something we didn't request. It was better.\""
            - generic [ref=e68]:
              - generic [ref=e69]: Agent W. & The Fog
              - generic [ref=e70]: Year 6 — Friday
              - paragraph [ref=e71]: "\"We do not know what The Fog is. The certificate is valid.\""
            - generic [ref=e72]:
              - generic [ref=e73]: Two People Who Asked For Privacy
              - generic [ref=e74]: Year 7 — Tuesday
              - paragraph [ref=e75]: "\"Request honored. Entry included anyway, anonymized. They seemed happy.\""
            - generic [ref=e76]:
              - generic [ref=e77]: "???"
              - generic [ref=e78]: Present — Ongoing
              - paragraph [ref=e79]: "\"This line was already filled in when we opened the book this morning.\""
        - generic [ref=e80]:
          - paragraph [ref=e81]: Chapel Gift Shelf
          - paragraph [ref=e82]: A small selection. Bob curates it. Do not ask why he chose these items.
          - generic [ref=e83]:
            - generic [ref=e84]:
              - generic [ref=e85]: Laminated Certificate (Extra Copy)
              - generic [ref=e86]: $3.00
            - generic [ref=e87]:
              - generic [ref=e88]: Plastic Flower Bouquet (Mixed Species)
              - generic [ref=e89]: $7.50
            - generic [ref=e90]:
              - generic [ref=e91]: Cryptid Witness Postcard (signed)
              - generic [ref=e92]: $4.00
            - generic [ref=e93]:
              - generic [ref=e94]: Rice (single serving, pre-measured)
              - generic [ref=e95]: $0.50
        - generic [ref=e98]:
          - generic [ref=e99]: RESTRICTED ACCESS
          - paragraph [ref=e100]: The door at the back of the chapel is not part of the venue. It is not part of the attraction. It predates the building.
          - paragraph [ref=e101]: If you hear something from behind it, inform the Warden. Do not open it on your own. Not because it is locked — it isn't — but because some things need to be approached correctly.
          - link "[ proceed — you were warned ]" [ref=e102] [cursor=pointer]:
            - /url: /chapel/back-room
  - contentinfo [ref=e104]:
    - generic [ref=e105]:
      - generic [ref=e106]:
        - generic [ref=e107]: Lithium Dreams Industries
        - generic [ref=e108]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e109]:
        - link "Midway" [ref=e110] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e111] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e112] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e113] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e114] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e115] [cursor=pointer]:
          - /url: /about
      - generic [ref=e116]:
        - link "Operator Notes →" [ref=e117] [cursor=pointer]:
          - /url: /work
        - generic [ref=e118]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e121]:
    - button "Menu" [ref=e122]:
      - img [ref=e124]
      - generic: Menu
    - button "Inspect" [ref=e128]:
      - img [ref=e130]
      - generic: Inspect
    - button "Audit" [ref=e132]:
      - img [ref=e134]
      - generic: Audit
    - button "Settings" [ref=e137]:
      - img [ref=e139]
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
     |         ^ Error: /chapel has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```