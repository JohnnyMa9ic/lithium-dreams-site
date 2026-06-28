# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /arcade
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /arcade has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.72 (foreground color: #434341, background color: #1a1c1f, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"cabinet-num mono\" data-astro-cid-lwl5rxwe=\"\">01</span>", "impact": "serious", "none": [], "target": [".cabinet--active.cabinet-card:nth-child(1) > .cabinet-top > .cabinet-num"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.15 (foreground color: #6c6a63, background color: #1a1c1f, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"cabinet-copy\" data-astro-cid-lwl5rxwe=\"\">Insert coin. Save the world. Choose your destiny.</p>", "impact": "serious", "none": [], "target": [".cabinet--active.cabinet-card:nth-child(1) > .cabinet-copy"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.67 (foreground color: #286a56, background color: #1a1c1f, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"cabinet-label mono\" data-astro-cid-lwl5rxwe=\"\">active</span>", "impact": "serious", "none": [], "target": [".cabinet--active.cabinet-card:nth-child(1) > .cabinet-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.72 (foreground color: #434341, background color: #1a1c1f, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"cabinet-num mono\" data-astro-cid-lwl5rxwe=\"\">02</span>", "impact": "serious", "none": [], "target": [".cabinet--flickering > .cabinet-top > .cabinet-num"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.15 (foreground color: #6c6a63, background color: #1a1c1f, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"cabinet-copy\" data-astro-cid-lwl5rxwe=\"\">Absolutely required. Lore integrity depends on it.</p>", "impact": "serious", "none": [], "target": [".cabinet--flickering > .cabinet-copy"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.69 (foreground color: #966e20, background color: #1a1c1f, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"cabinet-label mono\" data-astro-cid-lwl5rxwe=\"\">flickering</span>", "impact": "serious", "none": [], "target": [".cabinet--flickering > .cabinet-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.15 (foreground color: #6c6a63, background color: #1a1c1f, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"cabinet-copy\" data-astro-cid-lwl5rxwe=\"\">Two cryptids enter. One leaves confused.</p>", "impact": "serious", "none": [], "target": [".cabinet--out-of-order > .cabinet-copy"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
    - link "Signal detected" [ref=e21]:
      - /url: /workshop
    - generic [ref=e23]:
      - generic [ref=e24]:
        - navigation "Breadcrumb" [ref=e25]:
          - list [ref=e26]:
            - listitem [ref=e27]:
              - link "Home" [ref=e28] [cursor=pointer]:
                - /url: /
              - generic [ref=e29]: /
            - listitem [ref=e30]:
              - link "Midway" [ref=e31] [cursor=pointer]:
                - /url: /attraction
              - generic [ref=e32]: /
            - listitem [ref=e33]:
              - generic [ref=e34]: Arcade
        - generic [ref=e35]: FLICKERING
      - generic [ref=e36]:
        - generic [ref=e37]: ACC. ARC-001
        - heading "Arcade" [level=3] [ref=e38]
        - paragraph [ref=e39]: Project cabinets, experimental builds, and things that almost work.
      - generic [ref=e40]:
        - generic [ref=e42]: ARCADE DIRECTORY
        - generic [ref=e47]:
          - paragraph [ref=e48]: "> Cabinet index loaded. 8 units registered."
          - paragraph [ref=e49]: "> Please do not unplug the cabinet in the corner."
          - paragraph [ref=e50]: "> Jersey Devil Joust is out of order. It is also still running. Management is aware."
      - generic [ref=e51]:
        - generic [ref=e52]:
          - generic [ref=e54]: "01"
          - heading "Cosmic Selector" [level=3] [ref=e56]
          - paragraph [ref=e57]: Insert coin. Save the world. Choose your destiny.
          - generic [ref=e58]: active
        - generic [ref=e59]:
          - generic [ref=e61]: "02"
          - heading "Gopher Guts" [level=3] [ref=e63]
          - paragraph [ref=e64]: Absolutely required. Lore integrity depends on it.
          - generic [ref=e65]: flickering
        - generic [ref=e66]:
          - generic [ref=e68]: "03"
          - heading "Jersey Devil Joust" [level=3] [ref=e70]
          - paragraph [ref=e71]: Two cryptids enter. One leaves confused.
          - generic [ref=e72]: out of order / still running
          - link "Signal detected" [ref=e73]:
            - /url: /workshop
        - generic [ref=e74]:
          - generic [ref=e76]: "04"
          - heading "Mothman Signal" [level=3] [ref=e78]
          - paragraph [ref=e79]: Every warning is also a broadcast.
          - generic [ref=e80]: active
        - generic [ref=e81]:
          - generic [ref=e83]: "05"
          - heading "Alien Abduction" [level=3] [ref=e85]
          - paragraph [ref=e86]: No refunds for missing time.
          - generic [ref=e87]: beta
        - generic [ref=e88]:
          - generic [ref=e90]: "06"
          - heading "No-Clip Racing" [level=3] [ref=e92]
          - paragraph [ref=e93]: Reality optional. Seatbelt recommended.
          - generic [ref=e94]: unstable
        - generic [ref=e95]:
          - generic [ref=e97]: "07"
          - heading "Bigfoot Brawl" [level=3] [ref=e99]
          - paragraph [ref=e100]: Temporarily offline. Bigfoot is consulting legal.
          - generic [ref=e101]: maintenance
        - generic [ref=e102]:
          - generic [ref=e104]: "08"
          - heading "Cryptid Crush" [level=3] [ref=e106]
          - paragraph [ref=e107]: Hearts in pixel art. Pre-registration now open.
          - generic [ref=e108]: coming soon
      - generic [ref=e109]:
        - paragraph [ref=e110]: All-Time High Scores
        - paragraph [ref=e111]: Scores are estimated. The machine remembers differently than management.
        - table [ref=e112]:
          - rowgroup [ref=e113]:
            - row "Rank Handle Score Cabinet" [ref=e114]:
              - columnheader "Rank" [ref=e115]
              - columnheader "Handle" [ref=e116]
              - columnheader "Score" [ref=e117]
              - columnheader "Cabinet" [ref=e118]
          - rowgroup [ref=e119]:
            - row "01 WARDEN 9,847,200 Mothman Signal" [ref=e120]:
              - cell "01" [ref=e121]
              - cell "WARDEN" [ref=e122]
              - cell "9,847,200" [ref=e123]
              - cell "Mothman Signal" [ref=e124]
            - row "02 GHOST 7,102,400 No-Clip Racing" [ref=e125]:
              - cell "02" [ref=e126]
              - cell "GHOST" [ref=e127]
              - cell "7,102,400" [ref=e128]
              - cell "No-Clip Racing" [ref=e129]
            - row "03 B0B 6,330,050 Gopher Guts" [ref=e130]:
              - cell "03" [ref=e131]
              - cell "B0B" [ref=e132]
              - cell "6,330,050" [ref=e133]
              - cell "Gopher Guts" [ref=e134]
            - row "04 ??? 4,999,999 Cosmic Selector" [ref=e135]:
              - cell "04" [ref=e136]
              - cell "???" [ref=e137]
              - cell "4,999,999" [ref=e138]
              - cell "Cosmic Selector" [ref=e139]
            - row "05 VISITOR 112 Jersey Devil Joust" [ref=e140]:
              - cell "05" [ref=e141]
              - cell "VISITOR" [ref=e142]
              - cell "112" [ref=e143]
              - cell "Jersey Devil Joust" [ref=e144]
  - contentinfo [ref=e145]:
    - generic [ref=e146]:
      - generic [ref=e147]:
        - generic [ref=e148]: Lithium Dreams Industries
        - generic [ref=e149]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e150]:
        - link "Midway" [ref=e151] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e152] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e153] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e154] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e155] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e156] [cursor=pointer]:
          - /url: /about
      - generic [ref=e157]:
        - link "Operator Notes →" [ref=e158] [cursor=pointer]:
          - /url: /work
        - generic [ref=e159]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e162]:
    - button "Menu" [ref=e163]:
      - img [ref=e165]
      - generic: Menu
    - button "Inspect" [ref=e169]:
      - img [ref=e171]
      - generic: Inspect
    - button "Audit" [ref=e173]:
      - img [ref=e175]
      - generic: Audit
    - button "Settings" [ref=e178]:
      - img [ref=e180]
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
     |         ^ Error: /arcade has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```