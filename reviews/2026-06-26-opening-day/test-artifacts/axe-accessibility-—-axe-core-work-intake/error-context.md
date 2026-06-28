# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /work/intake
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /work/intake has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.49 (foreground color: #ffffff, background color: #c99d4c, font size: 7.8pt (10.4px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<span class=\"gh-logo-mark\" data-astro-cid-zyfjkaoe=\"\">LDI</span>", "impact": "serious", "none": [], "target": [".gh-logo-mark"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.18 (foreground color: #3d7fbd, background color: #fefefd, font size: 9.6pt (12.8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/work/intake\" class=\"active\" data-astro-cid-zyfjkaoe=\"\">Mission Intake</a>", "impact": "serious", "none": [], "target": ["a[href$=\"intake\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.26 (foreground color: #8a8f88, background color: #fefefd, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/attraction\" class=\"gh-nav-escape\" data-astro-cid-zyfjkaoe=\"\">← The Attraction</a>", "impact": "serious", "none": [], "target": [".gh-nav-escape"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.19 (foreground color: #9ba8b2, background color: #f5f3ee, font size: 7.2pt (9.6px), font weight: bold). Expected contrast ratio of 4.5:1", "html": "<div class=\"intake-eyebrow\" data-astro-cid-oh4brfd3=\"\">Mission Intake</div>", "impact": "serious", "none": [], "target": [".intake-eyebrow"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.81 (foreground color: #3d7fbd, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Track</span>", "impact": "serious", "none": [], "target": [".active.stepper-step[data-step=\"0\"] > .stepper-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.83 (foreground color: #b0b8b0, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Situation</span>", "impact": "serious", "none": [], "target": [".stepper-step[data-step=\"1\"] > .stepper-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.83 (foreground color: #b0b8b0, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Outcome</span>", "impact": "serious", "none": [], "target": [".stepper-step[data-step=\"2\"] > .stepper-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.83 (foreground color: #b0b8b0, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Systems</span>", "impact": "serious", "none": [], "target": [".stepper-step[data-step=\"3\"] > .stepper-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.83 (foreground color: #b0b8b0, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Scope</span>", "impact": "serious", "none": [], "target": [".stepper-step[data-step=\"4\"] > .stepper-label"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.83 (foreground color: #b0b8b0, background color: #f5f3ee, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"stepper-label\" data-astro-cid-oh4brfd3=\"\">Review</span>", "impact": "serious", "none": [], "target": [".stepper-step[data-step=\"5\"] > .stepper-label"]}, …], "tags": ["cat.color", "wcag2aa", "wcag143", "TTv5", "TT13.c", "EN-301-549", "EN-9.1.4.3", "ACT", "RGAAv4", "RGAA-3.2.1"]}]
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - navigation [ref=e2]:
    - link "LDI Work" [ref=e3] [cursor=pointer]:
      - /url: /work
      - generic [ref=e4]: LDI
      - generic [ref=e5]: Lithium Dreams Industries
    - generic [ref=e6]:
      - link "Overview" [ref=e7] [cursor=pointer]:
        - /url: /work
      - link "Mission Intake" [ref=e8] [cursor=pointer]:
        - /url: /work/intake
      - link "Case Files" [ref=e9] [cursor=pointer]:
        - /url: /work/case-files
      - link "About" [ref=e10] [cursor=pointer]:
        - /url: /about
    - link "← The Attraction" [ref=e11] [cursor=pointer]:
      - /url: /attraction
  - main [ref=e12]:
    - generic [ref=e13]:
      - generic [ref=e14]:
        - generic [ref=e15]: Mission Intake
        - heading "Brief an operator, not a chatbot." [level=1] [ref=e16]:
          - text: Brief an operator,
          - text: not a chatbot.
        - paragraph [ref=e17]:
          - text: A structured 6-step intake that replaces the vague discovery call.
          - text: No commitment — just clarity.
      - navigation "Wizard steps" [ref=e18]:
        - generic [ref=e19]:
          - generic [ref=e21]: "1"
          - generic [ref=e22]: Track
        - generic [ref=e24]:
          - generic [ref=e26]: "2"
          - generic [ref=e27]: Situation
        - generic [ref=e29]:
          - generic [ref=e31]: "3"
          - generic [ref=e32]: Outcome
        - generic [ref=e34]:
          - generic [ref=e36]: "4"
          - generic [ref=e37]: Systems
        - generic [ref=e39]:
          - generic [ref=e41]: "5"
          - generic [ref=e42]: Scope
        - generic [ref=e44]:
          - generic [ref=e46]: "6"
          - generic [ref=e47]: Review
      - generic [ref=e48]:
        - main [ref=e49]:
          - generic [ref=e51]:
            - generic [ref=e52]:
              - heading "Choose your track" [level=2] [ref=e53]
              - paragraph [ref=e54]: Select the service that most closely aligns with your primary objective. You can clarify in the brief.
            - generic [ref=e55]:
              - generic [ref=e56] [cursor=pointer]:
                - radio "Research OS Monitoring, synthesis, and knowledge systems."
                - img [ref=e58]
                - img [ref=e61]
                - generic [ref=e64]: Research OS
                - generic [ref=e65]: Monitoring, synthesis, and knowledge systems.
              - generic [ref=e66] [cursor=pointer]:
                - radio "Content Engine Plan, create, repurpose, and publish consistently."
                - img [ref=e68]
                - img [ref=e71]
                - generic [ref=e74]: Content Engine
                - generic [ref=e75]: Plan, create, repurpose, and publish consistently.
              - generic [ref=e76] [cursor=pointer]:
                - radio "Local Business Ops Streamline operations, client experience, and growth."
                - img [ref=e78]
                - img [ref=e81]
                - generic [ref=e84]: Local Business Ops
                - generic [ref=e85]: Streamline operations, client experience, and growth.
              - generic [ref=e86] [cursor=pointer]:
                - radio "Executive Assistant OS Delegate with confidence. Stay ahead proactively."
                - img [ref=e88]
                - img [ref=e91]
                - generic [ref=e94]: Executive Assistant OS
                - generic [ref=e95]: Delegate with confidence. Stay ahead proactively.
              - generic [ref=e96] [cursor=pointer]:
                - radio "Technical Advisory Solve technical challenges and build what matters."
                - img [ref=e98]
                - img [ref=e101]
                - generic [ref=e103]: Technical Advisory
                - generic [ref=e104]: Solve technical challenges and build what matters.
              - generic [ref=e105] [cursor=pointer]:
                - radio "Not Sure Yet Use the brief to identify the highest-value start."
                - img [ref=e107]
                - img [ref=e110]
                - generic [ref=e113]: Not Sure Yet
                - generic [ref=e114]: Use the brief to identify the highest-value start.
        - complementary [ref=e115]:
          - generic [ref=e116]:
            - generic [ref=e117]:
              - generic [ref=e118]:
                - generic [ref=e119]: Mission Brief
                - generic [ref=e120]: LDI-2026-0602
              - generic [ref=e121]:
                - img [ref=e122]
                - generic [ref=e126]: 17%
            - generic [ref=e127]: Step 1 of 6 — Track
            - generic [ref=e129]:
              - generic [ref=e130]: Service Track
              - generic [ref=e131]: Not selected
            - generic [ref=e133]:
              - generic [ref=e136]:
                - generic [ref=e137]: Situation
                - generic [ref=e138]: Not provided
              - generic [ref=e141]:
                - generic [ref=e142]: Outcome
                - generic [ref=e143]: Not provided
              - generic [ref=e146]:
                - generic [ref=e147]: Systems
                - generic [ref=e148]: Not provided
              - generic [ref=e151]:
                - generic [ref=e152]: Scope
                - generic [ref=e153]: Not provided
            - generic [ref=e155]:
              - generic [ref=e156]: Next Step
              - generic [ref=e157]: Current Situation
            - group [ref=e158]:
              - generic "JSON Output ▸" [ref=e159] [cursor=pointer]
      - generic [ref=e160]:
        - link "← Studio" [ref=e162] [cursor=pointer]:
          - /url: /work
        - generic [ref=e163]: Select a track to begin your mission brief.
        - button "Continue to Situation →" [ref=e165] [cursor=pointer]
  - contentinfo [ref=e166]:
    - generic [ref=e167]:
      - generic [ref=e168]: Lithium Dreams Industries
      - generic [ref=e169]: Operating Systems Design
      - link "About" [ref=e170] [cursor=pointer]:
        - /url: /about
      - link "Visit the Attraction →" [ref=e171] [cursor=pointer]:
        - /url: /attraction
  - generic [ref=e174]:
    - button "Menu" [ref=e175]:
      - img [ref=e177]
      - generic: Menu
    - button "Inspect" [ref=e181]:
      - img [ref=e183]
      - generic: Inspect
    - button "Audit" [ref=e185]:
      - img [ref=e187]
      - generic: Audit
    - button "Settings" [ref=e190]:
      - img [ref=e192]
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
     |         ^ Error: /work/intake has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```