# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /attraction
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /attraction has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.69 (foreground color: #736d61, background color: #13100d, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"ticker-msg mono\" data-astro-cid-opfnnago=\"\">", "impact": "serious", "none": [], "target": [".ticker-msg.mono:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.88 (foreground color: #423f3b, background color: #0a0a0c, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"status-panel-eyebrow mono\" data-astro-cid-opfnnago=\"\">District Status</p>", "impact": "serious", "none": [], "target": [".status-panel-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Gift Shop</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(1) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Fortune Emporium</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(2) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Arcade</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(3) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Museum</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(4) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Wedding Chapel</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(5) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Garden</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(6) > .sname.mono"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 8.2pt (10.88px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"mono sname\" data-astro-cid-opfnnago=\"\">Employees Only</span>", "impact": "serious", "none": [], "target": [".status-item:nth-child(7) > .sname.mono"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
    - region "Midway district map" [ref=e20]:
      - generic [ref=e21]:
        - img "The Midway — a rain-slicked courtyard at night surrounded by neon signs for each district" [ref=e22]
        - link "Gift Shop" [ref=e23] [cursor=pointer]:
          - /url: /gift-shop
          - generic: Gift Shop
        - link "Bob's Fortune Emporium" [ref=e24] [cursor=pointer]:
          - /url: /fortune
          - generic: Fortune Emporium
        - link "Arcade" [ref=e25] [cursor=pointer]:
          - /url: /arcade
          - generic: Arcade
        - link "Museum" [ref=e26] [cursor=pointer]:
          - /url: /museum
          - generic: Museum
        - link "Snack Counter — coming soon" [ref=e27] [cursor=pointer]:
          - /url: "#"
          - generic: Snack Counter
        - link "LDI — Home" [ref=e28] [cursor=pointer]:
          - /url: /
          - generic: Home
        - link "Lost & Found — coming soon" [ref=e29] [cursor=pointer]:
          - /url: "#"
          - generic: Lost & Found
        - link "Wedding Chapel" [ref=e30] [cursor=pointer]:
          - /url: /chapel
          - generic: Wedding Chapel
        - link "Employees Only — Ghost's Workshop" [ref=e31] [cursor=pointer]:
          - /url: /workshop
          - generic: Employees Only
        - generic: YOU ARE HERE
    - generic "Midway announcements" [ref=e32]:
      - generic [ref=e33]: INTERCOM
      - generic [ref=e35]:
        - generic [ref=e36]: "Welcome to the Midway. Please keep your hands inside the lore. • Bob's Fortune Emporium is operational. Results not guaranteed. • The Museum of Ongoing Events is accepting new submissions. • Wedding Chapel: open Tuesdays and Fridays. Do not ask about the back room. • The Arcade cabinet in the corner is still technically running. We are aware. • Lost & Found hours: whenever someone remembers to open it. • The Warden would like to remind everyone that the cryptids are not decorative. •"
        - generic [ref=e37]: "Welcome to the Midway. Please keep your hands inside the lore. • Bob's Fortune Emporium is operational. Results not guaranteed. • The Museum of Ongoing Events is accepting new submissions. • Wedding Chapel: open Tuesdays and Fridays. Do not ask about the back room. • The Arcade cabinet in the corner is still technically running. We are aware. • Lost & Found hours: whenever someone remembers to open it. • The Warden would like to remind everyone that the cryptids are not decorative. •"
    - generic [ref=e38]:
      - generic [ref=e39]:
        - paragraph [ref=e40]: District Status
        - generic [ref=e41]:
          - generic [ref=e44]: Gift Shop
          - generic [ref=e47]: Fortune Emporium
          - generic [ref=e50]: Arcade
          - generic [ref=e53]: Museum
          - generic [ref=e56]: Wedding Chapel
          - generic [ref=e59]: Garden
          - generic [ref=e62]: Employees Only
          - generic [ref=e63]:
            - generic [ref=e65]: Snack Counter
            - generic [ref=e66]: soon
      - generic [ref=e67]:
        - generic [ref=e68]:
          - generic [ref=e69]: General Admission
          - generic [ref=e70]: $12
        - paragraph [ref=e71]: Access to all open Midway districts. Cryptid encounters not included but also not excluded.
        - generic [ref=e72]:
          - generic [ref=e73]: "Valid: one entry"
          - generic [ref=e74]: Non-refundable after threshold
        - generic [ref=e76]:
          - generic [ref=e77]: KEEP THIS PORTION
          - generic [ref=e78]: LDI ADMIT ONE
    - generic [ref=e79]:
      - paragraph [ref=e80]: District Directory
      - generic [ref=e81]:
        - link "Gift Shop OPEN Souvenirs, field notes, stickers, and objects we are legally allowed to sell. No refunds after portal exposure." [ref=e82] [cursor=pointer]:
          - /url: /gift-shop
          - generic [ref=e83]:
            - generic [ref=e84]: 🎪
            - generic [ref=e85]: Gift Shop
            - generic [ref=e86]: OPEN
          - generic [ref=e87]:
            - paragraph [ref=e88]: Souvenirs, field notes, stickers, and objects we are legally allowed to sell.
            - paragraph [ref=e89]: No refunds after portal exposure.
        - link "Arcade FLICKERING Project cabinets, experimental builds, and things that almost work. Please do not unplug the cabinet in the corner." [ref=e90] [cursor=pointer]:
          - /url: /arcade
          - generic [ref=e91]:
            - generic [ref=e92]: 🕹
            - generic [ref=e93]: Arcade
            - generic [ref=e94]: FLICKERING
          - generic [ref=e95]:
            - paragraph [ref=e96]: Project cabinets, experimental builds, and things that almost work.
            - paragraph [ref=e97]: Please do not unplug the cabinet in the corner.
        - link "Museum OPEN Curated case files, lore fragments, and a timeline we are still reconstructing. Please do not tap the glass." [ref=e98] [cursor=pointer]:
          - /url: /museum
          - generic [ref=e99]:
            - generic [ref=e100]: 🏺
            - generic [ref=e101]: Museum
            - generic [ref=e102]: OPEN
          - generic [ref=e103]:
            - paragraph [ref=e104]: Curated case files, lore fragments, and a timeline we are still reconstructing.
            - paragraph [ref=e105]: Please do not tap the glass.
        - link "Fortune Emporium UNSTABLE Bob's cabinet. Insert a question. Results are not guaranteed but are usually interesting. Temporarily sentient. Bob says this is probably fine." [ref=e106] [cursor=pointer]:
          - /url: /fortune
          - generic [ref=e107]:
            - generic [ref=e108]: 🔮
            - generic [ref=e109]: Fortune Emporium
            - generic [ref=e110]: UNSTABLE
          - generic [ref=e111]:
            - paragraph [ref=e112]: Bob's cabinet. Insert a question. Results are not guaranteed but are usually interesting.
            - paragraph [ref=e113]: Temporarily sentient. Bob says this is probably fine.
        - generic [ref=e114]:
          - generic [ref=e115]:
            - generic [ref=e116]: 🍿
            - generic [ref=e117]: Snack Counter
            - generic [ref=e118]: UNDER REPAIR
          - generic [ref=e119]:
            - paragraph [ref=e120]: Temporarily unmanned. The register is still running.
            - paragraph [ref=e121]: Maintenance has already been notified.
        - generic [ref=e122]:
          - generic [ref=e123]:
            - generic [ref=e124]: 📦
            - generic [ref=e125]: Lost & Found
            - generic [ref=e126]: OPEN
          - generic [ref=e127]:
            - paragraph [ref=e128]: Something has already been turned in on your behalf.
            - paragraph [ref=e129]: Extraterrestrial parking has moved behind the chapel.
        - link "Wedding Chapel BY APPOINTMENT Open Tuesdays and Fridays. Do not ask about the back room. Reflections may desynchronize during electrical storms." [ref=e130] [cursor=pointer]:
          - /url: /chapel
          - generic [ref=e131]:
            - generic [ref=e132]: ⛪
            - generic [ref=e133]: Wedding Chapel
            - generic [ref=e134]: BY APPOINTMENT
          - generic [ref=e135]:
            - paragraph [ref=e136]: Open Tuesdays and Fridays. Do not ask about the back room.
            - paragraph [ref=e137]: Reflections may desynchronize during electrical storms.
        - generic [ref=e138]:
          - generic [ref=e139]:
            - generic [ref=e140]: 🔒
            - generic [ref=e141]: Employees Only
            - generic [ref=e142]: RESTRICTED
          - generic [ref=e143]:
            - paragraph [ref=e144]: Authorized staff, maintenance personnel, cryptids with valid badges, and Bob.
            - paragraph [ref=e145]: Please do not feed the groundskeeper.
      - paragraph [ref=e146]: Additional districts are indicated by the arrows. The arrows are correct. Probably.
    - generic [ref=e147]:
      - paragraph [ref=e148]: Incident Log
      - generic [ref=e149]:
        - generic [ref=e150]:
          - generic [ref=e151]: Year 3 — Tuesday
          - paragraph [ref=e152]: The organ in the wedding chapel played something no one requested. Guests appreciated it. Warden says this was not unexpected.
        - generic [ref=e153]:
          - generic [ref=e154]: Year 6 — Friday
          - paragraph [ref=e155]: A visitor left a note in the Lost & Found. The note was addressed to the Midway. The Midway has been informed.
        - generic [ref=e156]:
          - generic [ref=e157]: Year 7 — Unknown
          - paragraph [ref=e158]: The Crossroads Incident. Museum is documenting. Details pending clearance.
        - generic [ref=e159]:
          - generic [ref=e160]: Present — Ongoing
          - paragraph [ref=e161]: You are here. The Midway has noted your arrival. Welcome. Please don't rush.
  - contentinfo [ref=e162]:
    - generic [ref=e163]:
      - generic [ref=e164]:
        - generic [ref=e165]: Lithium Dreams Industries
        - generic [ref=e166]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e167]:
        - link "Midway" [ref=e168] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e169] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e170] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e171] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e172] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e173] [cursor=pointer]:
          - /url: /about
      - generic [ref=e174]:
        - link "Operator Notes →" [ref=e175] [cursor=pointer]:
          - /url: /work
        - generic [ref=e176]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e179]:
    - button "Menu" [ref=e180]:
      - img [ref=e182]
      - generic: Menu
    - button "Inspect" [ref=e186]:
      - img [ref=e188]
      - generic: Inspect
    - button "Audit" [ref=e190]:
      - generic [ref=e191]:
        - img [ref=e192]
        - img [ref=e195]
      - generic: Audit
    - button "Settings" [ref=e198]:
      - img [ref=e200]
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
     |         ^ Error: /attraction has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```