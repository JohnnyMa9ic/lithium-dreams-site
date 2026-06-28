# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /employees-only
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /employees-only has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Home</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href=\"/\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.63 (foreground color: #58544e, background color: #0a0a0c, font size: 7.8pt (10.4px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"breadcrumb-link mono\" data-astro-cid-ezvlwyc3=\"\">Midway</a>", "impact": "serious", "none": [], "target": [".breadcrumb-link[href$=\"attraction\"][data-astro-cid-ezvlwyc3=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.71 (foreground color: #c23b22, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"maintenance-tag tag--restricted tag-size--md\" data-astro-cid-qv3dslcb=\"\">RESTRICTED</span>", "impact": "serious", "none": [], "target": [".maintenance-tag"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.63 (foreground color: #6e6961, background color: #0a0a0c, font size: 9.0pt (12px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<p class=\"emp-sub mono text-dim\" data-astro-cid-nbnw27wf=\"\">Badge access required. Smile at the camera. It notices everything.</p>", "impact": "serious", "none": [], "target": [".emp-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.65 (foreground color: #3a3835, background color: #0e0e10, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"poster-eyebrow mono\" data-astro-cid-nbnw27wf=\"\">POSTED BY: MANAGEMENT</span>", "impact": "serious", "none": [], "target": [".poster-eyebrow:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.65 (foreground color: #3a3835, background color: #0e0e10, font size: 6.6pt (8.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"poster-eyebrow mono\" data-astro-cid-nbnw27wf=\"\">DATE: ONGOING</span>", "impact": "serious", "none": [], "target": [".poster-eyebrow:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.27 (foreground color: #7b766c, background color: #0e0e10, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-nbnw27wf=\"\">If the lights flicker, do not panic. If the lights go out entirely, panic quietly and in an orderly fashion.</li>", "impact": "serious", "none": [], "target": [".safety-rules > li:nth-child(1)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.27 (foreground color: #7b766c, background color: #0e0e10, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-nbnw27wf=\"\">Do not feed the cryptids in the back lot. They have a schedule. Your generosity disrupts it.</li>", "impact": "serious", "none": [], "target": [".safety-rules > li:nth-child(2)"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.27 (foreground color: #7b766c, background color: #0e0e10, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<li data-astro-cid-nbnw27wf=\"\">The badge reader reads mood as well as magnetic stripe. Keep both professional.</li>", "impact": "serious", "none": [], "target": [".safety-rules > li:nth-child(3)"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
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
              - generic [ref=e34]: Employees Only
        - generic [ref=e35]: RESTRICTED
      - generic [ref=e36]:
        - heading "Employees Only" [level=1] [ref=e37]
        - paragraph [ref=e38]: Badge access required. Smile at the camera. It notices everything.
      - generic [ref=e39]:
        - generic [ref=e40]:
          - generic [ref=e41]: "POSTED BY: MANAGEMENT"
          - generic [ref=e42]: "DATE: ONGOING"
        - heading "Employee Safety Bulletin" [level=2] [ref=e43]
        - list [ref=e44]:
          - listitem [ref=e45]: If the lights flicker, do not panic. If the lights go out entirely, panic quietly and in an orderly fashion.
          - listitem [ref=e46]: Do not feed the cryptids in the back lot. They have a schedule. Your generosity disrupts it.
          - listitem [ref=e47]: The badge reader reads mood as well as magnetic stripe. Keep both professional.
          - listitem [ref=e48]: If you find a door that was not there yesterday, report it. Do not enter it. Note its size, texture, and whether it smells of cedar.
          - listitem [ref=e49]: Bob is a coworker, not a resource. Treat him accordingly. Bob says this is not a joke.
        - paragraph [ref=e50]: — LDI Employee Relations — This notice supersedes all prior safety notices —
      - generic [ref=e51]:
        - generic [ref=e53]: Badge Reader Status
        - generic [ref=e55]:
          - paragraph [ref=e56]: Badge reader operational. System is logging all entries, denials, and hesitations. Hesitation counts as an attempt.
          - paragraph [ref=e57]: If your access is PENDING, it is being evaluated. This may take longer than expected. This is intentional.
      - generic [ref=e58]:
        - paragraph [ref=e59]: Today's Access Log
        - table [ref=e61]:
          - rowgroup [ref=e62]:
            - row "Time ID Name Status Note" [ref=e63]:
              - columnheader "Time" [ref=e64]
              - columnheader "ID" [ref=e65]
              - columnheader "Name" [ref=e66]
              - columnheader "Status" [ref=e67]
              - columnheader "Note" [ref=e68]
          - rowgroup [ref=e69]:
            - row "08:14 EMP-008 Warden GRANTED Routine entry" [ref=e70]:
              - cell "08:14" [ref=e71]
              - cell "EMP-008" [ref=e72]
              - cell "Warden" [ref=e73]
              - cell "GRANTED" [ref=e74]
              - cell "Routine entry" [ref=e75]
            - row "08:47 EMP-??? Unknown DENIED Badge not recognized" [ref=e76]:
              - cell "08:47" [ref=e77]
              - cell "EMP-???" [ref=e78]
              - cell "Unknown" [ref=e79]
              - cell "DENIED" [ref=e80]
              - cell "Badge not recognized" [ref=e81]
            - row "09:02 EMP-??? Unknown DENIED Badge still not recognized" [ref=e82]:
              - cell "09:02" [ref=e83]
              - cell "EMP-???" [ref=e84]
              - cell "Unknown" [ref=e85]
              - cell "DENIED" [ref=e86]
              - cell "Badge still not recognized" [ref=e87]
            - row "09:03 EMP-??? Unknown DENIED Stop trying" [ref=e88]:
              - cell "09:03" [ref=e89]
              - cell "EMP-???" [ref=e90]
              - cell "Unknown" [ref=e91]
              - cell "DENIED" [ref=e92]
              - cell "Stop trying" [ref=e93]
            - row "10:30 SYS-01 Ghost GRANTED Remote access — Workshop relay" [ref=e94]:
              - cell "10:30" [ref=e95]
              - cell "SYS-01" [ref=e96]
              - cell "Ghost" [ref=e97]
              - cell "GRANTED" [ref=e98]
              - cell "Remote access — Workshop relay" [ref=e99]
            - row "11:15 EMP-??? Unknown DENIED Different badge. Same result." [ref=e100]:
              - cell "11:15" [ref=e101]
              - cell "EMP-???" [ref=e102]
              - cell "Unknown" [ref=e103]
              - cell "DENIED" [ref=e104]
              - cell "Different badge. Same result." [ref=e105]
            - row "13:48 EMP-001 Warden GRANTED Second entry — forgot something" [ref=e106]:
              - cell "13:48" [ref=e107]
              - cell "EMP-001" [ref=e108]
              - cell "Warden" [ref=e109]
              - cell "GRANTED" [ref=e110]
              - cell "Second entry — forgot something" [ref=e111]
            - row "NOW VIS-000 YOU PENDING Evaluating" [ref=e112]:
              - cell "NOW" [ref=e113]
              - cell "VIS-000" [ref=e114]
              - cell "YOU" [ref=e115]
              - cell "PENDING" [ref=e116]
              - cell "Evaluating" [ref=e117]
      - generic [ref=e118]:
        - generic [ref=e119]: EMPLOYEES ONLY
        - img [ref=e121]
        - paragraph [ref=e125]: Authorized staff, maintenance personnel, cryptids with valid badges, and Bob.
        - link "← Return to Midway" [ref=e126] [cursor=pointer]:
          - /url: /
  - contentinfo [ref=e127]:
    - generic [ref=e128]:
      - generic [ref=e129]:
        - generic [ref=e130]: Lithium Dreams Industries
        - generic [ref=e131]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e132]:
        - link "Midway" [ref=e133] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e134] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e135] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e136] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e137] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e138] [cursor=pointer]:
          - /url: /about
      - generic [ref=e139]:
        - link "Operator Notes →" [ref=e140] [cursor=pointer]:
          - /url: /work
        - generic [ref=e141]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e144]:
    - button "Menu" [ref=e145]:
      - img [ref=e147]
      - generic: Menu
    - button "Inspect" [ref=e151]:
      - img [ref=e153]
      - generic: Inspect
    - button "Audit" [ref=e155]:
      - img [ref=e157]
      - generic: Audit
    - button "Settings" [ref=e160]:
      - img [ref=e162]
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
     |         ^ Error: /employees-only has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```