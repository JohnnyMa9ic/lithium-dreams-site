# Glasshouse Systems Studio
## Agent Framework Harness Specification

**Document ID:** GH-0003
**Prepared by:** Lithium Dreams Industries / Glasshouse Systems Studio
**Status:** Internal Technical Reference + Client-Facing Explainer

---

> *A harness is not artificial intelligence trying to replace a person. It is a system that does the repetitive, time-consuming work of assembling information and moving it to the right place — so the human can do the part only they can do.*

---

## 1. THE HARNESS CONCEPT

### Plain-Language Explainer (for client delivery)

You already have workflows in your business. Every day, certain things happen in a certain order: someone fills out your contact form, you check your email, you search for something, you sit down to write, you review what's on your calendar before the week starts. These workflows are real — they just mostly live in your head, and you do them manually, one step at a time.

A harness does the parts of those workflows that don't require your judgment.

Imagine you run a small consulting firm. Every morning, you spend 45 minutes reading newsletters, checking a few websites, scanning email, and compiling a mental picture of what's happening in your space before you start client work. You do this because it matters — but you're the one doing all the assembly work, not the thinking work.

A harness does the assembly. It reads the sources you've told it to read, compiles the information into a structured brief, and puts it in front of you — organized, summarized, ready for your attention. By the time you sit down, the 45 minutes of compilation has already happened. You spend 10 minutes reviewing and deciding. You move on.

The harness is not deciding what matters. You decided that when you configured it — you told it what sources to monitor, what topics to watch, what keywords to flag. It's executing your decisions, automatically, on a schedule, without you having to remember to start it.

That's what every Glasshouse harness does. The specifics differ — some compile research, some draft content, some route inquiries, some assemble briefings — but the principle is the same: structured, consistent execution of work that doesn't require a human to be present.

**What a harness is not:**
- It is not an autonomous agent making strategic decisions
- It is not a replacement for expertise, relationships, or judgment
- It is not something you install and forget (it requires configuration maintenance)
- It is not a product from a software company — it is a configured system built for your specific operation

**What a harness is:**
- A set of automated steps that run on a trigger (a time, an event, or a submission)
- A pipeline that takes input (a form, an email, a calendar, a list of sources) and produces output (a brief, a draft, a notification, an entry in your system)
- A human review checkpoint at each step where judgment is required
- An infrastructure layer that Glasshouse builds and maintains

---

## 2. THE FOUR HARNESS TYPES

---

### HARNESS A: The Research Harness
*For Research OS clients*

**What it monitors:**
The Research Harness reads from the client's configured Source Registry — a curated list of publications, websites, newsletters, RSS feeds, experts, and competitive entities that the client has determined are worth watching. Sources are grouped by topic; each topic has a configured relevance weight (what matters most gets more surface attention).

Standard monitoring scope:
- 10–30 sources (Source Registry entries with Active = true)
- 3–7 topic clusters
- 3–10 competitive entities (if Competitive Watch Room is included)
- Client-defined alert keywords (terms that trigger immediate notification, not just daily digest)

**How it summarizes:**
The harness runs on two schedules:

*Daily Brief (default: 6:30 AM)*
1. Perplexity API pulls recent content from each active source
2. Content is filtered by topic relevance (keyword matching + Claude relevance scoring)
3. Claude (Sonnet) generates a 300–500 word Signal Summary across all topics
4. 2–3 Priority Items are identified (highest relevance score + most recent)
5. New Notion page is created in the Daily Signal Brief database
6. If any content matches an Alert Keyword, an immediate notification is sent via email or Slack (before the full brief is complete)

*Weekly Deep Dive (default: Friday 4:00 PM)*
1. All brief pages from the current week are reviewed
2. Claude generates a "Week in Review" synthesis: patterns, anomalies, emerging signals
3. Competitive Watch entries are updated with weekly summaries
4. A "what to watch next week" section is generated from unresolved signals

**Where it delivers:**
- Primary: Notion (Daily Signal Brief database + Competitive Watch Dashboard)
- Optional: email delivery of brief (HTML formatted, links back to Notion)
- Optional: Slack message with brief summary and link to full Notion page
- Optional: SMS for Alert Keywords only (immediate, not digest)

**Human review checkpoint:**
The brief is always created before the client's day begins. The client's role is:
- Review the brief (not assemble it)
- Adjust Priority Items ranking if needed (AI flags, human ranks)
- Mark any items as "Action Required" (creates Synthesis entry)
- Quarterly: audit the Source Registry (remove dead sources, add new ones)

The harness does not send anything external without human review. Its output is internal to the client's Notion workspace (plus optional notification). There is no external-facing automation in this harness.

**Technical Stack:**
| Component | Tool | Role |
|---|---|---|
| Source content retrieval | Perplexity API | Pulls recent content from monitored sources |
| Relevance scoring + summarization | Claude API (Sonnet) | Generates summaries, scores relevance, identifies priorities |
| Delivery + storage | Notion API | Creates brief pages, updates Competitive Watch entries |
| Scheduling | Hermes (internal LDI orchestration) | Triggers the pipeline at configured times |
| Alerts | Email (SMTP) + optional Slack webhook | Sends immediate notifications on keyword matches |

---

### HARNESS B: The Content Engine Harness
*For Content Engine clients*

**Inputs:**
The Content Engine Harness reads two primary inputs:
1. The client's Content Calendar — specifically, entries with Status = "Briefed" (ready for AI to draft)
2. The client's Brand Voice Reference — the source of truth for how the brand sounds

When the harness detects a Calendar entry in "Briefed" status, it activates the drafting pipeline for that entry.

**What it produces:**

*On a new "Briefed" entry (trigger: status change detected)*
1. Claude reads the Brief field from the Content Calendar entry
2. Claude reads the Brand Voice Reference (loaded as system prompt)
3. Claude generates a first draft of the content piece (article, newsletter, script, social post — depending on Content Type)
4. Draft is written into a new Notion page, linked to the Calendar entry
5. Calendar Status changes to "In Draft"
6. Optional: DALL-E 3 generates 3 thumbnail concepts (for video/visual content) based on the brief + brand visual direction
7. ElevenLabs generates a voiceover read of the draft intro paragraph (optional — for podcast/audio clients)

*On a "Published" entry (trigger: status change detected)*
1. Claude processes the published piece for Content Atom extraction
2. 8–15 atoms are generated (quotes, hooks, frameworks, arguments, statistics)
3. Each atom is classified by type and Platform Fit
4. Atoms are written to the Content Atom Library with Status = "Unused" and linked to the source Calendar entry
5. Platform-specific repurpose drafts are generated (LinkedIn post, Twitter thread, email summary, newsletter blurb)
6. Repurposed content is staged in the Calendar as new "In Draft" entries linked to the source piece

*Weekly publishing schedule (for clients using Buffer integration)*
1. All Calendar entries with Status = "Scheduled" are reviewed
2. Buffer API scheduling is verified (posts are queued at the right times)
3. A weekly content slate summary is generated and sent to the client (what goes out when)

**Review gates:**
The Content Engine Harness does not publish anything. Every output passes through a human review step:

| Output | Review Gate |
|---|---|
| First draft | Human edits in Notion before Status moves to "In Review" |
| DALL-E thumbnails | Human selects from 3 options |
| Content atoms | Human reviews all atoms before Status = "Unused" |
| Repurposed content | Human reviews each piece; approves or discards |
| Buffer scheduling | Human confirms schedule in Buffer before posts go live |

The harness produces; the human approves. Nothing external is touched without a human decision.

**Output routing:**
- Notion: all drafts, atoms, and repurposed content live here until approved
- Buffer API: receives approved scheduled posts (after human confirmation)
- Email: newsletter content formatted and sent via configured provider (after human confirmation)
- Website CMS: supported via Webflow or WordPress API (custom integration, billed separately)
- ElevenLabs: audio files saved to Notion or delivered via link

**Technical Stack:**
| Component | Tool | Role |
|---|---|---|
| Draft generation + atom extraction | Claude API (Sonnet) | Primary content generation, brand-voice-configured |
| Image generation | DALL-E 3 | Thumbnail concepts from brief + brand direction |
| Voice generation | ElevenLabs | Intro voiceover, optional audio preview |
| Video processing | ffmpeg | Audio/video file handling for podcast/video clients |
| Social scheduling | Buffer API | Queues approved posts |
| Content delivery | Notion API | Manages all draft and published content storage |
| Scheduling | Hermes | Triggers pipeline on status changes and schedule |

---

### HARNESS C: The Intake & Follow-Up Harness
*For Local Business Ops clients*

**Trigger:**
The Intake & Follow-Up Harness activates on one of two events:
1. A form submission (Tally or Typeform intake form submits to the Cloudflare Worker)
2. An email received matching configured patterns (new inquiry keywords in subject line, or sent to a configured intake address)

**Pipeline:**

*Step 1: Intake (immediate, within 60 seconds of trigger)*
- Cloudflare Worker receives the form payload (JSON)
- Required fields are validated; missing fields trigger a "we need a bit more information" auto-response
- Claude generates an AI Qualification Summary: what did this person say, what are they asking for, how does it match our service criteria?
- Claude assigns initial Lead Score (Hot / Warm / Cold) based on configured qualification rubric
- New entry is created in the Lead Intake Tracker (Notion) with all captured fields + AI summary
- Internal notification sent (Slack or email): "New lead received — [Name] — [Score]"

*Step 2: Routing (within 2 minutes)*
- Based on Lead Score and Lead Type, the harness selects the appropriate Follow-Up Sequence
- The sequence is activated with Day 1 = today
- Lead is assigned to the configured team member (based on routing rules: geography, service type, team member capacity)
- If Lead Score = Hot: immediate priority notification sent to assigned team member

*Step 3: Follow-Up Sequence Execution*
- Day 1: Claude drafts a personalized initial response using the Follow-Up Sequence template + lead data
- If auto-send is enabled: email sends immediately
- If human-in-the-loop is enabled: email is queued for human review; sends when approved (15-minute window before it sends anyway, configurable)
- Day 3, 7, 14 (or configured schedule): subsequent sequence steps execute on the same review/send logic
- If lead responds at any step: sequence pauses; notification sent to assigned team member; the human takes over

**Human checkpoint — when the agent hands off to a human:**
The harness is designed to hold the line through the early touches, not replace the human relationship. The handoff happens when:
- The lead responds (any response — now it's a real conversation)
- The lead books a call or meeting (automation creates the calendar event; human shows up)
- The Lead Score changes to Hot based on response signals
- 14 days have passed with no response (harness stops; human decides whether to follow up manually)

After handoff, the human manages the relationship. The harness continues to log touchpoints in the Intake Tracker as the human updates fields.

**Output:**
| Output | Destination |
|---|---|
| New lead record | Notion Lead Intake Tracker |
| AI Qualification Summary | Notion (field in lead record) |
| Internal notification | Email or Slack |
| Personalized follow-up emails | Client email (via Gmail API or SMTP) |
| Calendar event (when lead books) | Google Calendar API |
| Sequence status updates | Notion Lead Intake Tracker |

**Technical Stack:**
| Component | Tool | Role |
|---|---|---|
| Intake endpoint | Cloudflare Worker | Receives form payload, initiates pipeline |
| Qualification + summarization | Claude API (Sonnet) | Qualification summary, lead scoring, message drafting |
| CRM storage | Notion API | Lead records, sequence status, touchpoint logging |
| Email delivery | Gmail API (or SMTP) | Sends follow-up sequence emails |
| Calendar | Google Calendar API | Creates appointments when leads book |
| Notifications | Slack webhook or email | Internal team alerts |
| Scheduling | Hermes | Sequences follow-up step triggers |

---

### HARNESS D: The Operator Briefing Harness
*For Executive Assistant OS clients*

**Daily Mode (default: 6:00 AM)**

The morning briefing pipeline runs seven days a week (configurable — many clients set Monday–Friday only):

*Step 1: Calendar Pull*
- Google Calendar API retrieves today's events
- Claude interprets each event: what is this, what context matters going into it, is there any prep required?
- "Key Commitments" section of the brief is generated

*Step 2: Email Surface Scan*
- Gmail API retrieves emails received since the last brief
- Claude scans for: items requiring a decision, items waiting on the executive, items from Stakeholder Map priority contacts, flagged keywords
- "Incoming This Week" section is populated with surfaced items (not the emails themselves — a structured summary)
- Urgent items are separated from the digest

*Step 3: Decision Log Review*
- Notion API retrieves Decision Log entries where Revisit Date is within 7 days
- These are surfaced in the "Open Decisions" section

*Step 4: Horizon Planner Pull*
- Notion API retrieves Horizon Planner entries where Due Date is within 30 days and Status = "Needs Prep" or "Needs Decision"
- These are surfaced in the "Horizon Watch" section

*Step 5: Brief Assembly + Delivery*
- Claude assembles all sections into the Weekly Mission Brief format
- A new Notion page is created in the Brief Archive database
- Brief is delivered to Notion and optionally emailed to the executive at configured time
- One-sentence summary sent via Slack or SMS if configured ("This week: 3 key meetings, 2 open decisions, 1 renewal approaching")

**Weekly Mode (default: Sunday 7:00 PM)**

The weekly briefing is the same pipeline but with expanded scope:
- Full week of calendar events (not just today)
- Full week of email reviewed (not just recent)
- Prior week's brief reviewed: which items were resolved, which were not
- Horizon Planner advanced: items approaching the "This Month" window
- 30/60/90 Horizon updated with any new surfaced items from the week's email and calendar

**Alert Mode (trigger: keyword match)**

A parallel, always-on monitoring layer runs against incoming email and calendar changes:
- Configured alert keywords (names, topics, trigger phrases set during onboarding)
- When a match is detected, an immediate notification is sent — not part of the daily brief cycle
- Examples: "contract," "emergency," a specific client name, "deadline," "legal," "urgent"
- Alert notification includes: source (email or calendar), what matched, the relevant excerpt, a link

**Output:**
| Output | Destination |
|---|---|
| Daily briefing page | Notion (Brief Archive database) |
| Optional email brief | Executive's inbox (HTML formatted) |
| Optional Slack summary | Configured Slack channel or DM |
| Alert notifications | Email + optional SMS (via Twilio) |
| Decision Log entries (drafted) | Notion Decision Log (pending human review) |
| Horizon Planner updates | Notion Horizon Planner database |

**Technical Stack:**
| Component | Tool | Role |
|---|---|---|
| Email reading | Gmail API | Reads and surfaces relevant email |
| Calendar reading | Google Calendar API | Reads events and interprets context |
| Briefing assembly + summarization | Claude API (Sonnet) | Generates all brief sections |
| Knowledge base | Notion API | Creates brief pages, reads Decision Log and Horizon Planner |
| Orchestration | Hermes | Manages all pipeline triggers and step sequencing |
| Notifications | Email / Slack webhook / Twilio (optional) | Delivers alerts and briefs |

---

## 3. THE HANDOFF MODEL

### What the Client Gets

At the conclusion of every harness deployment, the client receives:

1. **Credentials & Access Document** — a secure-shared document listing every API connection in the harness, which account it connects to, and the client-side credential management instructions
2. **Harness Architecture Diagram** — a visual map of the harness: triggers, steps, decision points, outputs. One page, readable without technical background
3. **Notion Workspace** — fully configured, seeded, and live (per GH-0002)
4. **SOP Library** — written operating procedures for each harness component: what it does, how to adjust its configuration, when to contact Glasshouse
5. **Training Recordings** — two sessions recorded and stored inside the Notion workspace
6. **"First 30 Days" Guide** — specific prompts and exercises for the first month of operation
7. **The Harness Health Check** — a monthly 15-minute checklist the client runs to confirm the harness is operating correctly

### What John Maintains

The Hermes layer is not handed off. Glasshouse retains operational control of:

- The Hermes orchestration configuration (the scheduling, trigger logic, and step sequencing)
- API key rotation and credential security for the LDI-managed stack components
- Monitoring of harness health (automated pings confirm each pipeline ran successfully)
- Updates to Claude prompts when model behavior changes or outputs drift from expected quality
- Recovery when a pipeline fails (diagnosis, fix, and a brief explanation of what happened)

This is by design. The harness is powerful precisely because it is professionally maintained. A client managing their own Hermes configuration is like a business managing their own server — possible, but not the reason they hired Glasshouse.

### What the Client Maintains

The client is the owner of their data and their decisions. Their ongoing responsibilities:

- **Content and records** — the entries in their Notion workspace. The harness moves and processes data; the client owns the data itself
- **Brand Voice Reference** — updated when the brand evolves (Glasshouse can facilitate a voice recalibration session)
- **Source Registry** — kept current as information sources change; Glasshouse provides a quarterly audit prompt
- **Follow-Up Sequence templates** — the message content (the harness executes the sequence; the client decides what it says)
- **Human review checkpoints** — approvals, edits, decisions. These are not automated
- **API accounts** — the client maintains their own Google, Buffer, ElevenLabs, and other third-party accounts. Glasshouse configures the connections; the client owns the accounts and the associated costs

### The Monitoring Protocol

Glasshouse monitors the health of every live harness under an active retainer:

**Automated Monitoring (continuous)**
- Each harness pipeline sends a confirmation ping to a Glasshouse monitoring endpoint on completion
- If a pipeline fails or does not confirm within its expected window, an alert is triggered
- Ghost (the LDI infrastructure agent) handles first-line detection and logs the failure for John's review

**Human Review (daily)**
- John reviews the monitoring log as part of his own morning briefing
- Failures are triaged: infrastructure issue, API change, data issue, or configuration drift
- Client is notified when a failure affected their operation (with explanation + resolution timeline)

**Proactive Maintenance (quarterly)**
- Glasshouse reviews each live harness against current API documentation for any breaking changes
- Claude prompt outputs are reviewed for quality drift (models update; prompts sometimes need adjustment)
- A brief "harness health report" is shared with the client: what's working well, what was adjusted, any recommended changes

---

## 4. PRICING & PACKAGING

### One-Time Setup Fee vs. Monthly Maintenance

Every harness deployment involves two cost components:

**Setup Fee (one-time)**
Covers: harness architecture, API configuration, testing, Notion workspace build, documentation, training sessions.

| Harness | Setup Fee Range |
|---|---|
| Research Harness | $2,800 – $4,200 |
| Content Engine Harness | $3,500 – $5,500 |
| Intake & Follow-Up Harness | $3,000 – $4,800 |
| Operator Briefing Harness | $3,200 – $4,500 |
| Multi-harness discount (2+) | 15% off additional harnesses |

*Setup fees are included in the Pilot Build and Operating System tier pricing — they are not additional.*

**Monthly Maintenance (optional after Pilot Build; included in OS and Embedded tiers)**
Covers: Hermes orchestration, pipeline monitoring, API maintenance, prompt calibration, health checks, support access.

| Harness | Monthly Maintenance |
|---|---|
| Research Harness | $380 – $520/month |
| Content Engine Harness | $480 – $680/month |
| Intake & Follow-Up Harness | $350 – $480/month |
| Operator Briefing Harness | $420 – $580/month |
| Multi-harness (2+) | 20% off additional harnesses |

*Clients who do not subscribe to monthly maintenance retain their harness but are responsible for their own infrastructure maintenance. Glasshouse will not have visibility into failures. Recommended only for clients with an internal technical resource.*

**API Costs (client's responsibility)**
All third-party API costs are the client's. Glasshouse provides a cost estimate at scoping:

| Tool | Estimated Monthly Cost (typical usage) |
|---|---|
| Claude API (Sonnet) | $15 – $80/month (usage-dependent) |
| Perplexity API | $20 – $60/month |
| ElevenLabs | $11 – $99/month (plan-dependent) |
| DALL-E 3 | $5 – $30/month |
| Buffer | $18 – $99/month (plan-dependent) |
| Twilio (SMS alerts) | $5 – $20/month |

Total third-party API costs for a typical single-harness client: **$50 – $200/month**. This is not a Glasshouse charge — it is the cost of the tools the harness uses.

### When a Client Outgrows the Harness

Harnesses are designed to scale within their configuration — adding more sources to monitor, more sequence steps, more content types — without rebuild costs. True outgrowth happens when:

- The client's operation has expanded into a new service area that requires a different harness configuration
- The volume of processing has increased beyond the current API tier limits
- The client needs harness types not included in their current deployment
- The client's technical sophistication has grown and they want a more complex orchestration architecture

Glasshouse handles outgrowth as a scoping conversation, not an upgrade form. The trajectory is clear: Pilot Build → Operating System → Embedded Studio. At each tier, the harness architecture expands. The Embedded tier includes unlimited harness reconfiguration within the retainer scope.

### The Upgrade Path

| Current | Trigger | Next |
|---|---|---|
| Orientation (Tier I) | Ready to build | Pilot Build (Tier II) |
| Pilot Build (Tier II) | System is working; need more | Operating System (Tier III) |
| Pilot Build without maintenance | Harness breaks or drifts | Add maintenance retainer |
| Operating System (Tier III) | Glasshouse needs to be embedded, not visiting | Embedded Studio (Tier IV) |
| Embedded Studio (Tier IV) | — | Annual renegotiation; scope expansion |

---

## 5. REAL-WORLD IMPLICATIONS BY CUSTOMER SEGMENT

### Solo Operator (independent consultant, coach, freelancer)

A solo operator's primary problem is time — specifically, the time they spend on operational work that doesn't directly serve clients. For a solo consultant, the Research Harness replaces 45 minutes of manual reading with a 10-minute review. The Content Engine Harness means their newsletter doesn't fall behind when a client project gets heavy. The Operator Briefing Harness means Monday morning is a briefing, not a scramble. Over the course of a month, the harness stack returns 15–25 hours of cognitive overhead. The solo operator doesn't hire an assistant — they build a system. They don't become a technologist — they configure once and let the system run.

### Local Small Business (5–20 employees, not tech-savvy)

For a local business — a contractor, a salon, a specialty retailer, a medical practice — the harness is largely invisible. The owner doesn't interact with the technology; they interact with the outputs: a lead that came in through the website was already responded to before the owner checked their phone, a follow-up email went out on schedule without anyone on the team remembering to send it, the weekly digest of what happened with leads and clients was waiting in their inbox on Monday. The technology stays in the back. What changes is that the business responds faster, follows up consistently, and loses fewer opportunities — without adding headcount. The Local Business Ops harness is, in practice, a reliable part-time employee who never forgets, never calls in sick, and never confuses a "Warm" lead with a "Hot" one.

### Content Creator (podcast, YouTube, newsletter)

For the content creator, the harness is the difference between a content operation and a content habit. Without systems, production is heroic — exhausting bursts of creative output followed by gaps. With the Content Engine Harness, the creator records a podcast, the system produces show notes, social captions, email newsletter copy, a LinkedIn post, and a short-form clip strategy — all from one recording session. The creator's job is to create the source material and approve what goes out. The machine handles the multiplication. A creator who was publishing one piece per week and losing all the derivative value from it finds themselves, three months in, maintaining a consistent presence across four platforms — without working more hours.

### Mid-Size Company with a Real Operations Team

At this scale, the harness is less about replacing manual work and more about creating consistency. The operations team already does what the harness does — but they do it inconsistently, depending on who's working that day and how much else is happening. The Intake & Follow-Up Harness means every lead gets the same quality of initial response, regardless of which team member is on intake. The Operator Briefing Harness means the VP's Monday morning context is always current, not dependent on whether an EA had time to compile it. The Research Harness means the strategy team's competitive intelligence isn't dependent on whoever remembered to search last week. The harness doesn't replace the team — it gives the team a reliable baseline to operate from.

### Executive Who Wants to Think Better, Not Just Work Faster

This is the most specific use case, and in some ways the most valuable. The executive's leverage is in the quality of their thinking and their decisions. Everything that pulls attention away from thinking — assembling context, tracking open loops, remembering what was decided and why, maintaining relationships on a cadence — is a tax on the executive's most valuable function. The Operator Briefing Harness is not a productivity tool for the executive — it's a thinking support infrastructure. When Monday morning begins with a compiled briefing instead of 45 minutes of inbox archaeology, when a decision from eight months ago is retrievable in seconds from the Decision Log, when a relationship that should have been tended surfaces automatically in the weekly brief — the executive isn't faster. They're clearer. And clarity at the top of an organization propagates. That is the Glasshouse proposition at its highest level: not doing things faster, but thinking from a better position.

---

## APPENDIX: HARNESS ARCHITECTURE SUMMARY

| Harness | Primary Trigger | Primary Output | Human Gate | Core Tools |
|---|---|---|---|---|
| Research | Scheduled time (daily) | Signal Brief in Notion | Review + action triage | Perplexity, Claude, Notion, Hermes |
| Content Engine | Status change in Notion | First draft + atoms in Notion | Approval before publish | Claude, DALL-E 3, ElevenLabs, Buffer, ffmpeg |
| Intake & Follow-Up | Form submission / email | Lead record + follow-up sequence | Response approval / handoff decision | Cloudflare Worker, Claude, Notion, Gmail, Calendar |
| Operator Briefing | Scheduled time (daily + weekly) | Mission Brief in Notion | Review + "This Week's Intention" | Gmail, Calendar, Claude, Notion, Hermes |

**The Pantheon Layer (internal LDI, Embedded tier only)**

At Tier IV (Embedded Studio), the LDI Pantheon is available for complex orchestration:
- **Bob (Quarterback)** — orchestrates multi-harness pipelines; routes decisions to the correct harness based on input type and context
- **Ghost (Infrastructure/Signal Routing)** — manages the underlying infrastructure, monitoring, and inter-harness communication
- **Warden (Boundary Patrol/Access)** — enforces access controls; ensures the right data reaches the right harness and that client data boundaries are maintained

The Pantheon is not a product — it is Glasshouse's internal operating layer. Embedded clients benefit from it without managing it.

---

*Document ID: GH-0003 | Glasshouse Systems Studio | Lithium Dreams Industries*
*For internal use and client-facing technical reference*
*Technical implementation: contact John directly*
