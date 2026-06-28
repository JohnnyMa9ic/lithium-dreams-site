# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /studio/field-notes
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /studio/field-notes has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.59 (foreground color: #363432, background color: #0a0a0c, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"studio-back mono\" data-astro-cid-32dw5vra=\"\">← About</a>", "impact": "serious", "none": [], "target": [".studio-back"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">01</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"studio\"][data-astro-cid-32dw5vra=\"\"] > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">The Story</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"studio\"][data-astro-cid-32dw5vra=\"\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">02</span>", "impact": "serious", "none": [], "target": [".studio-link--active > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">03</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"infrastructure\"][data-astro-cid-32dw5vra=\"\"] > .link-num.mono[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">Infrastructure</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"infrastructure\"][data-astro-cid-32dw5vra=\"\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">About</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"about\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/studio\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Studio</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"studio\"][data-astro-cid-ezvlwyc3=\"\"]"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
      - paragraph [ref=e23]: LDI Studio · Signal Taxonomy
      - heading "Field Notes" [level=1] [ref=e24]
      - paragraph [ref=e25]: The observation system. Twelve symbols, four categories. Used to classify signals before they become something else.
    - navigation "Studio section navigation" [ref=e26]:
      - link "← About" [ref=e27] [cursor=pointer]:
        - /url: /about
      - generic [ref=e28]:
        - link "01 The Story" [ref=e29] [cursor=pointer]:
          - /url: /studio
          - generic [ref=e30]: "01"
          - generic [ref=e31]: The Story
        - link "02 Field Notes" [ref=e32] [cursor=pointer]:
          - /url: /studio/field-notes
          - generic [ref=e33]: "02"
          - generic [ref=e34]: Field Notes
        - link "03 Infrastructure" [ref=e35] [cursor=pointer]:
          - /url: /studio/infrastructure
          - generic [ref=e36]: "03"
          - generic [ref=e37]: Infrastructure
    - generic [ref=e38]:
      - navigation "Breadcrumb" [ref=e39]:
        - list [ref=e40]:
          - listitem [ref=e41]:
            - link "Home" [ref=e42] [cursor=pointer]:
              - /url: /
            - generic [ref=e43]: /
          - listitem [ref=e44]:
            - link "About" [ref=e45] [cursor=pointer]:
              - /url: /about
            - generic [ref=e46]: /
          - listitem [ref=e47]:
            - link "Studio" [ref=e48] [cursor=pointer]:
              - /url: /studio
            - generic [ref=e49]: /
          - listitem [ref=e50]:
            - generic [ref=e51]: Field Notes
      - generic [ref=e52]:
        - paragraph [ref=e53]: Field notes are how the Operator tracks signals — observations that don't fit an existing category, events that need to be held somewhere before they can be understood. The symbols below are the full taxonomy. They appear in the physical notebooks, in system logs, and in the margins of things that are still being figured out.
        - paragraph [ref=e54]: "Each symbol is a compression of a question: what kind of thing is this, and what does it require of me right now?"
      - generic [ref=e55]:
        - generic [ref=e56]:
          - generic [ref=e58]: Observation
          - generic [ref=e60]:
            - generic [ref=e61]:
              - img [ref=e63]
              - generic [ref=e66]:
                - generic [ref=e67]:
                  - generic [ref=e68]: Open Signal
                  - generic [ref=e69]: OS
                - paragraph [ref=e70]: Event logged. Status unresolved. Awaiting classification or follow-up.
            - generic [ref=e71]:
              - img [ref=e73]
              - generic [ref=e75]:
                - generic [ref=e76]:
                  - generic [ref=e77]: Closed Signal
                  - generic [ref=e78]: CS
                - paragraph [ref=e79]: Event resolved. Filed. No further action required unless re-triggered.
            - generic [ref=e80]:
              - img [ref=e82]
              - generic [ref=e84]:
                - generic [ref=e85]:
                  - generic [ref=e86]: Dormant
                  - generic [ref=e87]: DR
                - paragraph [ref=e88]: Signal present but inactive. Monitoring continues at reduced frequency.
        - generic [ref=e89]:
          - generic [ref=e91]: Dynamic
          - generic [ref=e93]:
            - generic [ref=e94]:
              - img [ref=e96]
              - generic [ref=e98]:
                - generic [ref=e99]:
                  - generic [ref=e100]: Elevated
                  - generic [ref=e101]: EL
                - paragraph [ref=e102]: Activity above baseline. Not anomalous — pattern recognized, intensity increased.
            - generic [ref=e103]:
              - img [ref=e105]
              - generic [ref=e107]:
                - generic [ref=e108]:
                  - generic [ref=e109]: Ambient
                  - generic [ref=e110]: AM
                - paragraph [ref=e111]: Persistent background condition. Not an event — an environment. Log once, review periodically.
            - generic [ref=e112]:
              - img [ref=e114]
              - generic [ref=e117]:
                - generic [ref=e118]:
                  - generic [ref=e119]: Loop
                  - generic [ref=e120]: LP
                - paragraph [ref=e121]: Recursive or cyclical behavior detected. May resolve naturally. Monitor for runaway state.
        - generic [ref=e122]:
          - generic [ref=e124]: Classification
          - generic [ref=e126]:
            - generic [ref=e127]:
              - img [ref=e129]
              - generic [ref=e132]:
                - generic [ref=e133]:
                  - generic [ref=e134]: Convergence
                  - generic [ref=e135]: CV
                - paragraph [ref=e136]: Two or more independent signals overlapping. May be coincidence. May not be.
            - generic [ref=e137]:
              - img [ref=e139]
              - generic [ref=e141]:
                - generic [ref=e142]:
                  - generic [ref=e143]: "Null"
                  - generic [ref=e144]: NL
                - paragraph [ref=e145]: Expected signal absent. The absence is the signal. Investigate what should be present.
            - generic [ref=e146]:
              - img [ref=e148]
              - generic [ref=e151]:
                - generic [ref=e152]:
                  - generic [ref=e153]: Threshold
                  - generic [ref=e154]: TH
                - paragraph [ref=e155]: Boundary condition reached. Proceed with awareness. This is the edge of the known map.
        - generic [ref=e156]:
          - generic [ref=e158]: Caution
          - generic [ref=e160]:
            - generic [ref=e161]:
              - img [ref=e163]
              - generic [ref=e166]:
                - generic [ref=e167]:
                  - generic [ref=e168]: Anomaly
                  - generic [ref=e169]: AN
                - paragraph [ref=e170]: Deviation outside expected range. Not necessarily dangerous — but it requires a name before it gets one.
            - generic [ref=e171]:
              - img [ref=e173]
              - generic [ref=e176]:
                - generic [ref=e177]:
                  - generic [ref=e178]: Bifurcation
                  - generic [ref=e179]: BF
                - paragraph [ref=e180]: Multiple valid interpretations. Both branches are logged. Resolution pending additional observation.
            - generic [ref=e181]:
              - img [ref=e183]
              - generic [ref=e187]:
                - generic [ref=e188]:
                  - generic [ref=e189]: Redacted
                  - generic [ref=e190]: RD
                - paragraph [ref=e191]: Entry exists. Content classified or removed from active record. The Warden has the full log.
      - generic [ref=e192]:
        - generic [ref=e193]:
          - paragraph [ref=e194]: Usage
          - paragraph [ref=e195]: Symbols are applied at first classification and updated as new information arrives. A signal that opens as OS may close as CS, or reclassify as AN depending on subsequent observations. RD entries are not modified after classification — the Warden maintains the full record separately.
        - generic [ref=e196]:
          - paragraph [ref=e197]: On the back lot
          - paragraph [ref=e198]: The back lot has generated entries in every category. The two open incidents from Y07 are currently logged as BF — both interpretations remain active. The Warden has additional context. The Warden is not sharing it at this time.
      - generic [ref=e199]:
        - link "← The Story" [ref=e200] [cursor=pointer]:
          - /url: /studio
        - link "Infrastructure →" [ref=e201] [cursor=pointer]:
          - /url: /studio/infrastructure
  - contentinfo [ref=e202]:
    - generic [ref=e203]:
      - generic [ref=e204]:
        - generic [ref=e205]: Lithium Dreams Industries
        - generic [ref=e206]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e207]:
        - link "Midway" [ref=e208] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e209] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e210] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e211] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e212] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e213] [cursor=pointer]:
          - /url: /about
      - generic [ref=e214]:
        - link "Operator Notes →" [ref=e215] [cursor=pointer]:
          - /url: /work
        - generic [ref=e216]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e219]:
    - button "Menu" [ref=e220]:
      - img [ref=e222]
      - generic: Menu
    - button "Inspect" [ref=e226]:
      - img [ref=e228]
      - generic: Inspect
    - button "Audit" [ref=e230]:
      - img [ref=e232]
      - generic: Audit
    - button "Settings" [ref=e235]:
      - img [ref=e237]
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
     |         ^ Error: /studio/field-notes has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```