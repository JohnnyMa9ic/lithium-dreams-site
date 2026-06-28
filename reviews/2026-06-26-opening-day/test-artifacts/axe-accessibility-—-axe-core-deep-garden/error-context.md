# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /deep-garden
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /deep-garden has 1 critical/serious a11y violations:
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
    - complementary "Garden depth position" [ref=e20]:
      - link "Yasuragi" [ref=e21] [cursor=pointer]:
        - /url: "#yasuragi"
        - text: Yasuragi
      - link "Root Layer" [ref=e23] [cursor=pointer]:
        - /url: "#root-layer"
        - text: Root Layer
      - link "Deep Garden" [ref=e25] [cursor=pointer]:
        - /url: "#deep-garden"
        - text: Deep Garden
    - generic [ref=e30]:
      - generic [ref=e31]:
        - paragraph [ref=e32]: Warden Collection
        - heading "Yasuragi Garden" [level=1] [ref=e33]:
          - text: Yasuragi
          - text: Garden
        - paragraph [ref=e34]: A quiet place behind the noise.
        - paragraph [ref=e35]: Please walk slowly. The garden is listening.
        - generic [ref=e36]:
          - link "Walk the Lantern Path" [ref=e37] [cursor=pointer]:
            - /url: "#surface-garden"
          - link "Descend to the Deep Garden" [ref=e38] [cursor=pointer]:
            - /url: "#deep-garden"
      - complementary [ref=e39]:
        - paragraph [ref=e40]: Garden Status
        - strong [ref=e41]: Root System Active
        - generic [ref=e42]: Rainfall steady · Lanterns lit · Visitors calm
    - generic [ref=e44]:
      - generic [ref=e45]:
        - paragraph [ref=e46]: ACC. ROOT-001
        - heading "Visible Root System Restorative Zone" [level=2] [ref=e47]:
          - text: Visible Root System
          - text: Restorative Zone
        - paragraph [ref=e48]: Yasuragi Garden is the visible layer of the garden system — cultivated, tended, and accessible. This is where the attraction softens. Where noise drains off. Where ideas can rest long enough to become clear again.
        - paragraph [ref=e49]: Not every path needs to lead somewhere loud.
      - generic [ref=e50]:
        - article [ref=e51]:
          - generic [ref=e52]: "01"
          - heading "Bonsai Registry" [level=3] [ref=e53]
          - paragraph [ref=e54]: Atlas, Patient Zero, Lantern Keeper, and Quiet Signal remain under active care.
          - generic [ref=e55]: "Warden note: do not rush the small trees."
        - article [ref=e56]:
          - generic [ref=e57]: "02"
          - heading "Lantern Path" [level=3] [ref=e58]
          - paragraph [ref=e59]: Teal lanterns mark safe routes. Dim lanterns indicate slow zones. Flicker does not always mean danger.
          - generic [ref=e60]: "Current lantern status: all lit."
        - article [ref=e61]:
          - generic [ref=e62]: "03"
          - heading "Warden's Bench" [level=3] [ref=e63]
          - blockquote [ref=e64]: "\"Urgency is often just unprocessed fear wearing a watch.\""
        - article [ref=e65]:
          - generic [ref=e66]: "04"
          - heading "Greenhouse Notes" [level=3] [ref=e67]
          - paragraph [ref=e68]: Glass cleaned after storm activity. Rain chain repaired. Roots visible near west wall.
          - generic [ref=e69]: "Filed under: ordinary miracles."
        - article [ref=e70]:
          - generic [ref=e71]: "05"
          - heading "Stone Basin" [level=3] [ref=e72]
          - paragraph [ref=e73]: Touch water. Breathe. Begin again.
          - generic [ref=e74]: Water recirculating normally.
    - region "Garden descent from surface to deep" [ref=e75]:
      - generic [ref=e76]:
        - generic [ref=e85]:
          - paragraph [ref=e86]: Warden Collection
          - heading "Yasuragi Garden" [level=2] [ref=e87]:
            - text: Yasuragi
            - text: Garden
          - paragraph [ref=e88]: A quiet place behind the noise.
        - generic:
          - paragraph: Root Layer
          - heading "Below the visible garden is the part that remembers." [level=2]:
            - text: Below the visible garden
            - text: is the part that remembers.
          - paragraph: Some ideas are not dead. They are just underground.
        - generic:
          - paragraph: ACC. ROOT-002
          - heading "Deep Garden" [level=2]:
            - text: Deep
            - text: Garden
          - paragraph: Memory compost / dormant idea storage.
    - generic [ref=e90]:
      - generic [ref=e91]:
        - generic [ref=e92]:
          - paragraph [ref=e93]: ACC. ROOT-MAP-01
          - heading "Living Infrastructure Index" [level=2] [ref=e94]
        - paragraph [ref=e95]: "The visible attraction is not the whole structure. Beneath it runs a quieter network: roots, memory, patience, and living continuity."
      - img "Root network connecting Deep Garden to all attraction locations" [ref=e96]:
        - img [ref=e97]
        - generic [ref=e104]: Deep Garden
        - generic [ref=e105]: Midway
        - generic [ref=e106]: Museum
        - generic [ref=e107]: Bob's Fortune
        - generic [ref=e108]: Ghost's Workshop
        - generic [ref=e109]: Wedding Chapel
        - generic [ref=e110]: Cathedral
        - generic [ref=e111]: Crossroads
        - generic [ref=e112]: Corporate Glasshouse
      - paragraph [ref=e113]: Wiring carries signals. Roots carry memory.
    - generic [ref=e117]:
      - generic [ref=e118]:
        - paragraph [ref=e119]: ACC. ROOT-002
        - heading "Deep Garden" [level=1] [ref=e120]:
          - text: Deep
          - text: Garden
        - paragraph [ref=e121]: Memory compost / dormant idea storage.
        - paragraph [ref=e122]: Not every idea is supposed to bloom today.
      - complementary [ref=e123]:
        - paragraph [ref=e124]: Belowground Status
        - strong [ref=e125]: Dormant Systems Stable
        - generic [ref=e126]: Humidity 81% · Lanterns active · Cathedral boundary intact
    - generic [ref=e129]:
      - article [ref=e130]:
        - generic [ref=e131]: A
        - heading "Seed Archive" [level=3] [ref=e132]
        - paragraph [ref=e133]: Dream Crown, Archive Courtyard, Crossroads Atlas, Signal Herbarium, and Dormant Cabinet 7.
      - article [ref=e134]:
        - generic [ref=e135]: B
        - heading "Compost Notes" [level=3] [ref=e136]
        - paragraph [ref=e137]: Some ideas do not fail. They become soil.
      - article [ref=e138]:
        - generic [ref=e139]: C
        - heading "Dormant Ideas" [level=3] [ref=e140]
        - paragraph [ref=e141]: Not ready yet does not mean abandoned. Some roots grow in silence for years before finding light.
      - article [ref=e142]:
        - generic [ref=e143]: "!"
        - heading "Root Warnings" [level=3] [ref=e144]
        - paragraph [ref=e145]: Do not pull at active roots. Do not follow roots toward the Cathedral without escort. Do not confuse dormancy with abandonment.
      - article [ref=e146]:
        - generic [ref=e147]: W
        - heading "Warden's Field Notes" [level=3] [ref=e148]
        - paragraph [ref=e149]: The difference between delay and incubation is care.
      - article [ref=e150]:
        - generic [ref=e151]: "?"
        - heading "Things Not Ready Yet" [level=3] [ref=e152]
        - paragraph [ref=e153]: A holding shelf for ideas that still have heat but no shape. Come back when the season changes.
    - generic [ref=e155]:
      - generic [ref=e156]:
        - generic [ref=e157]:
          - paragraph [ref=e158]: Planting Station
          - heading "Plant an Idea" [level=2] [ref=e159]
        - paragraph [ref=e160]: Every idea is a seed. Not every seed should become a project immediately. Give it the right conditions and check back.
      - generic [ref=e161]:
        - generic [ref=e162]:
          - generic [ref=e163]:
            - text: Idea Name
            - textbox "Idea Name" [ref=e164]:
              - /placeholder: Give your idea a name...
          - generic [ref=e165]:
            - text: What sparked it?
            - textbox "What sparked it?" [ref=e166]:
              - /placeholder: What moment, observation, or question lit this idea?
          - generic [ref=e167]:
            - text: Why isn't it ready?
            - textbox "Why isn't it ready?" [ref=e168]:
              - /placeholder: What's missing, unclear, or unresolved right now?
          - generic [ref=e169]:
            - text: What might help it grow?
            - textbox "What might help it grow?" [ref=e170]:
              - /placeholder: What resources, connections, or conditions would support it?
          - generic [ref=e171]:
            - text: When should it be checked again?
            - combobox "When should it be checked again?" [ref=e172]:
              - option "Later" [selected]
              - option "7 days"
              - option "30 days"
              - option "Next season"
              - option "When Bob stops laughing"
          - generic [ref=e173]:
            - button "Clear" [ref=e174] [cursor=pointer]
            - button "Download Packet" [ref=e175] [cursor=pointer]
        - complementary [ref=e176]:
          - generic [ref=e177]:
            - paragraph [ref=e178]: Deep Garden Archive
            - heading "Seed of Potential" [level=3] [ref=e179]
            - generic [ref=e180]: ✦
            - generic [ref=e181]:
              - generic [ref=e182]:
                - term [ref=e183]: Idea
                - definition [ref=e184]: Your idea's name will appear here
              - generic [ref=e185]:
                - term [ref=e186]: Status
                - definition [ref=e187]: Dormant
              - generic [ref=e188]:
                - term [ref=e189]: Planted
                - definition [ref=e190]: Jun 26, 2026
              - generic [ref=e191]:
                - term [ref=e192]: Review
                - definition [ref=e193]: Later
            - paragraph [ref=e194]: "Warden Note: Let it rest."
    - generic [ref=e196]:
      - paragraph [ref=e197]: "Filed Under: Long-Term Care"
      - generic [ref=e198]:
        - blockquote [ref=e199]: Not every idea should become a task immediately.
        - blockquote [ref=e200]: Patience is structure in biological form.
        - blockquote [ref=e201]: A living system knows when not to act.
        - blockquote [ref=e202]: Clarity is often what remains after urgency leaves.
    - generic [ref=e204]:
      - paragraph [ref=e205]: Next Doorways
      - generic [ref=e206]:
        - link "Return to the Attraction" [ref=e207] [cursor=pointer]:
          - /url: /attraction
        - link "Visit the Museum File" [ref=e208] [cursor=pointer]:
          - /url: /museum
        - link "Access Ghost's Workshop" [ref=e209] [cursor=pointer]:
          - /url: /workshop
        - link "Return to the Crossroads" [ref=e210] [cursor=pointer]:
          - /url: /
        - link "Do Not Follow Roots Toward the Cathedral" [ref=e211] [cursor=pointer]:
          - /url: /cathedral
    - generic [ref=e212]:
      - strong [ref=e213]: Yasuragi / Deep Garden
      - generic [ref=e214]: Root Systems Stable
      - emphasis [ref=e215]: Somewhere above, the Midway is still making noise.
  - contentinfo [ref=e216]:
    - generic [ref=e217]:
      - generic [ref=e218]:
        - generic [ref=e219]: Lithium Dreams Industries
        - generic [ref=e220]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e221]:
        - link "Midway" [ref=e222] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e223] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e224] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e225] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e226] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e227] [cursor=pointer]:
          - /url: /about
      - generic [ref=e228]:
        - link "Operator Notes →" [ref=e229] [cursor=pointer]:
          - /url: /work
        - generic [ref=e230]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e233]:
    - button "Menu" [ref=e234]:
      - img [ref=e236]
      - generic: Menu
    - button "Inspect" [ref=e240]:
      - img [ref=e242]
      - generic: Inspect
    - button "Audit" [ref=e244]:
      - img [ref=e246]
      - generic: Audit
    - button "Settings" [ref=e249]:
      - img [ref=e251]
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
     |         ^ Error: /deep-garden has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```