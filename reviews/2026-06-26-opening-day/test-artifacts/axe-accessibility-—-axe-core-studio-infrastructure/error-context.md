# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: axe.spec.ts >> accessibility — axe-core >> /studio/infrastructure
- Location: qa/axe.spec.ts:16:5

# Error details

```
Error: /studio/infrastructure has 1 critical/serious a11y violations:
  [serious] color-contrast: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds

expect(received).toHaveLength(expected)

Expected length: 0
Received length: 1
Received array:  [{"description": "Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds", "help": "Elements must meet minimum color contrast ratio thresholds", "helpUrl": "https://dequeuniversity.com/rules/axe/4.12/color-contrast?application=playwright", "id": "color-contrast", "impact": "serious", "nodes": [{"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 3.09 (foreground color: #786e59, background color: #2d220f, font size: 7.2pt (9.6px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"nav-logo-sub\" data-astro-cid-pgtvljfo=\"\">Industries</span>", "impact": "serious", "none": [], "target": [".nav-logo-sub"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.59 (foreground color: #363432, background color: #0a0a0c, font size: 7.0pt (9.28px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<a href=\"/about\" class=\"studio-back mono\" data-astro-cid-32dw5vra=\"\">← About</a>", "impact": "serious", "none": [], "target": [".studio-back"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">01</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"studio\"][data-astro-cid-32dw5vra=\"\"] > .link-num[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">The Story</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"studio\"][data-astro-cid-32dw5vra=\"\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 1.37 (foreground color: #2b2a28, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">02</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"field-notes\"][data-astro-cid-32dw5vra=\"\"] > .link-num[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 2.24 (foreground color: #4d4a44, background color: #0a0a0c, font size: 8.6pt (11.52px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-label\" data-astro-cid-32dw5vra=\"\">Field Notes</span>", "impact": "serious", "none": [], "target": [".studio-link[href$=\"field-notes\"][data-astro-cid-32dw5vra=\"\"] > .link-label[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
  Element has insufficient color contrast of 4.25 (foreground color: #79746a, background color: #0a0a0c, font size: 6.0pt (8px), font weight: normal). Expected contrast ratio of 4.5:1", "html": "<span class=\"link-num mono\" data-astro-cid-32dw5vra=\"\">03</span>", "impact": "serious", "none": [], "target": [".studio-link--active > .link-num[data-astro-cid-32dw5vra=\"\"]"]}, {"all": [], "any": [[Object]], "failureSummary": "Fix any of the following:
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
    - generic [ref=e23]:
      - paragraph [ref=e24]: LDI Studio · Operating Layer
      - heading "Infrastructure" [level=1] [ref=e25]
      - paragraph [ref=e26]: Three machines. Three agents. One handoff bus. This is how the work actually runs.
    - navigation "Studio section navigation" [ref=e27]:
      - link "← About" [ref=e28] [cursor=pointer]:
        - /url: /about
      - generic [ref=e29]:
        - link "01 The Story" [ref=e30] [cursor=pointer]:
          - /url: /studio
          - generic [ref=e31]: "01"
          - generic [ref=e32]: The Story
        - link "02 Field Notes" [ref=e33] [cursor=pointer]:
          - /url: /studio/field-notes
          - generic [ref=e34]: "02"
          - generic [ref=e35]: Field Notes
        - link "03 Infrastructure" [ref=e36] [cursor=pointer]:
          - /url: /studio/infrastructure
          - generic [ref=e37]: "03"
          - generic [ref=e38]: Infrastructure
    - generic [ref=e39]:
      - navigation "Breadcrumb" [ref=e40]:
        - list [ref=e41]:
          - listitem [ref=e42]:
            - link "Home" [ref=e43] [cursor=pointer]:
              - /url: /
            - generic [ref=e44]: /
          - listitem [ref=e45]:
            - link "About" [ref=e46] [cursor=pointer]:
              - /url: /about
            - generic [ref=e47]: /
          - listitem [ref=e48]:
            - link "Studio" [ref=e49] [cursor=pointer]:
              - /url: /studio
            - generic [ref=e50]: /
          - listitem [ref=e51]:
            - generic [ref=e52]: Infrastructure
      - generic [ref=e53]:
        - paragraph [ref=e54]: LDI runs on a three-machine, three-agent stack connected via Tailscale. This is not metaphor. The Attraction is the public face of a real operating infrastructure. The Workshop, the Signal Feeds, the back lot incident log — all of these correspond to actual running services.
        - paragraph [ref=e55]: "What follows is the honest version of the architecture: what the machines are, what the agents do, and how the handoff bus moves work between them. The Attraction's lore is the interpretive layer. This is the documentation layer."
      - generic [ref=e56]:
        - generic [ref=e57]:
          - generic [ref=e58]: "01"
          - heading "The Machines" [level=2] [ref=e59]
          - generic [ref=e60]: Tailscale mesh — always IPs, never hostnames
        - generic [ref=e61]:
          - generic [ref=e62]:
            - generic [ref=e63]:
              - generic [ref=e64]:
                - generic [ref=e65]: Mac Mini
                - generic [ref=e66]: primary
              - generic [ref=e67]: 100.73.149.45
            - generic [ref=e68]: Primary Orchestrator
            - paragraph [ref=e69]: The brain. Bob lives here. All agent sessions, vault access, handoff dispatch, and Claude Code sessions run from this machine. The Crossroads volume (3.5TB) and X9 Pro (1.8TB) are both mounted here.
            - generic [ref=e70]:
              - generic [ref=e71]: Services
              - list [ref=e72]:
                - listitem [ref=e73]: — Bob/Hermes gateway
                - listitem [ref=e74]: — Claude Code
                - listitem [ref=e75]: — Obsidian vault
                - listitem [ref=e76]: — Handoff bus (writer)
                - listitem [ref=e77]: — OneDrive (sole mount)
          - generic [ref=e78]:
            - generic [ref=e79]:
              - generic [ref=e80]:
                - generic [ref=e81]: Reliquary
                - generic [ref=e82]: standby
              - generic [ref=e83]: 100.116.54.62
            - generic [ref=e84]: Async Compute Node
            - paragraph [ref=e85]: Linux compute node for async workloads. Docker containers, long-running jobs, scheduled crons. The Crossroads and X9 Pro are accessible via SSHFS. No agent sessions or messaging — worker only.
            - generic [ref=e86]:
              - generic [ref=e87]: Services
              - list [ref=e88]:
                - listitem [ref=e89]: — Docker / cron jobs
                - listitem [ref=e90]: — Hermes worker
                - listitem [ref=e91]: — SSHFS (Crossroads + X9 Pro)
                - listitem [ref=e92]: — Handoff bus (reader)
          - generic [ref=e93]:
            - generic [ref=e94]:
              - generic [ref=e95]:
                - generic [ref=e96]: Victus
                - generic [ref=e97]: worker
              - generic [ref=e98]: 100.118.87.126
            - generic [ref=e99]: GPU / Windows Node
            - paragraph [ref=e100]: Windows machine with GPU. ComfyUI, 3D render jobs, image generation. Codex MCP available via WebSocket. All scripting is .ps1 — write file, SCP, execute. Never inline shell chains.
            - generic [ref=e101]:
              - generic [ref=e102]: Services
              - list [ref=e103]:
                - listitem [ref=e104]: — ComfyUI
                - listitem [ref=e105]: — Codex MCP (WebSocket)
                - listitem [ref=e106]: — GPU workloads
                - listitem [ref=e107]: — 3D fabrication prep
      - generic [ref=e108]:
        - generic [ref=e109]:
          - generic [ref=e110]: "02"
          - heading "The Agents" [level=2] [ref=e111]
          - generic [ref=e112]: Workers, not orchestrators — the Operator is the architect
        - generic [ref=e113]:
          - generic [ref=e114]:
            - generic [ref=e115]:
              - generic [ref=e117]: Bob
              - generic [ref=e119]: EMP-BOB-01
              - generic [ref=e120]: Quarterback / Orchestrator
              - generic [ref=e121]:
                - generic [ref=e122]: "Machine: Mac Mini"
                - generic [ref=e123]: "Status: On shift"
            - generic [ref=e124]:
              - paragraph [ref=e125]: Primary dispatch agent. Receives missions via the handoff bus, routes work to appropriate nodes, returns receipts. Runs on Hermes gateway with Nemotron Super as default model. Persona-hardened — does not spiral, does not apologize, gets things done.
              - generic [ref=e126]:
                - generic [ref=e127]: Capabilities
                - list [ref=e128]:
                  - listitem [ref=e129]: Mission dispatch
                  - listitem [ref=e130]: Multi-step research
                  - listitem [ref=e131]: Cross-machine routing
                  - listitem [ref=e132]: Receipt writing
                  - listitem [ref=e133]: Telegram interface (sole agent)
          - generic [ref=e134]:
            - generic [ref=e135]:
              - generic [ref=e137]: Ghost
              - generic [ref=e139]: SYS-GHOST-01
              - generic [ref=e140]: Infrastructure / Signal Routing
              - generic [ref=e141]:
                - generic [ref=e142]: "Machine: Mac Mini → all nodes"
                - generic [ref=e143]: "Status: Operational"
            - generic [ref=e144]:
              - paragraph [ref=e145]: Infrastructure maintenance agent. Keeps the gateway clean, signal paths correct, and the cold coffee undisturbed. Ghost operates at the systems layer and does not explain his work unless asked directly and twice.
              - generic [ref=e146]:
                - generic [ref=e147]: Capabilities
                - list [ref=e148]:
                  - listitem [ref=e149]: Gateway health
                  - listitem [ref=e150]: Signal path validation
                  - listitem [ref=e151]: Cross-node sync
                  - listitem [ref=e152]: Config maintenance
                  - listitem [ref=e153]: Cold coffee management
          - generic [ref=e154]:
            - generic [ref=e155]:
              - generic [ref=e157]: Warden
              - generic [ref=e159]: SEC-WARDEN-01
              - generic [ref=e160]: Boundary Patrol / Access Control
              - generic [ref=e161]:
                - generic [ref=e162]: "Machine: All sectors"
                - generic [ref=e163]: "Status: Active patrol"
            - generic [ref=e164]:
              - paragraph [ref=e165]: Monitors the boundary between the known operational envelope and whatever else is happening. Logs access events, classifies anomalies, and holds the full field notes record including the two open Y07 incidents. The Warden's logs are not public.
              - generic [ref=e166]:
                - generic [ref=e167]: Capabilities
                - list [ref=e168]:
                  - listitem [ref=e169]: Access logging
                  - listitem [ref=e170]: Anomaly classification
                  - listitem [ref=e171]: Boundary monitoring
                  - listitem [ref=e172]: Full field notes record
                  - listitem [ref=e173]: Back lot watch
      - generic [ref=e174]:
        - generic [ref=e175]:
          - generic [ref=e176]: "03"
          - heading "The Handoff Bus" [level=2] [ref=e177]
        - generic [ref=e178]:
          - paragraph [ref=e179]: Work moves between the Operator and Bob via a file-based handoff bus at /tmp/brainlab-context/handoff/. The Operator writes a mission brief to inbox-for-bob/. Bob's cron scans every 5 minutes, picks up the file, executes the mission, and drops a receipt in inbox-for-claude/. Both inboxes are committed to a shared git repo and pushed to GitHub so all machines see the same state.
          - generic [ref=e180]:
            - generic [ref=e181]:
              - generic [ref=e182]: Operator
              - generic [ref=e183]: writes mission brief
            - generic [ref=e184]:
              - generic [ref=e186]:
                - text: inbox-for-bob/
                - text: git push
              - generic [ref=e187]: →
            - generic [ref=e188]:
              - generic [ref=e189]: Bob
              - generic [ref=e190]: cron pickup → execute
            - generic [ref=e191]:
              - generic [ref=e192]: ←
              - generic [ref=e193]:
                - text: inbox-for-claude/
                - text: receipt
            - generic [ref=e195]:
              - generic [ref=e196]: Operator
              - generic [ref=e197]: reads receipt at session start
          - paragraph [ref=e198]: Mission briefs include a done_criteria field — a verifiable stop condition Bob checks after each iteration. Without it, Bob decides when he's done. This is how loops happen.
      - generic [ref=e199]:
        - paragraph [ref=e200]: On the Attraction
        - paragraph [ref=e201]: Ghost's Workshop is the public-facing version of this infrastructure. The signal feeds in the Workshop correspond to real service states. The access log on the Employees Only page uses real access event logic. The Warden's boundary patrol is the monitoring layer. The cryptid in the back lot is not yet classified.
      - generic [ref=e202]:
        - link "← Field Notes" [ref=e203] [cursor=pointer]:
          - /url: /studio/field-notes
        - link "Glasshouse Studio →" [ref=e204] [cursor=pointer]:
          - /url: /work
  - contentinfo [ref=e205]:
    - generic [ref=e206]:
      - generic [ref=e207]:
        - generic [ref=e208]: Lithium Dreams Industries
        - generic [ref=e209]: The Last Roadside Attraction
      - navigation "Footer navigation" [ref=e210]:
        - link "Midway" [ref=e211] [cursor=pointer]:
          - /url: /attraction
        - link "Museum" [ref=e212] [cursor=pointer]:
          - /url: /museum
        - link "Fortune" [ref=e213] [cursor=pointer]:
          - /url: /fortune
        - link "Chapel" [ref=e214] [cursor=pointer]:
          - /url: /chapel
        - link "Garden" [ref=e215] [cursor=pointer]:
          - /url: /deep-garden
        - link "About" [ref=e216] [cursor=pointer]:
          - /url: /about
      - generic [ref=e217]:
        - link "Operator Notes →" [ref=e218] [cursor=pointer]:
          - /url: /work
        - generic [ref=e219]: © Lithium Dreams Industries — Cryptid activity not the responsibility of management
  - generic [ref=e222]:
    - button "Menu" [ref=e223]:
      - img [ref=e225]
      - generic: Menu
    - button "Inspect" [ref=e229]:
      - img [ref=e231]
      - generic: Inspect
    - button "Audit" [ref=e233]:
      - img [ref=e235]
      - generic: Audit
    - button "Settings" [ref=e238]:
      - img [ref=e240]
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
     |         ^ Error: /studio/infrastructure has 1 critical/serious a11y violations:
  34 |     });
  35 |   }
  36 | });
  37 | 
```