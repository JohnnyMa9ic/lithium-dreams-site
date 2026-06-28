# Glasshouse Systems Studio
## Notion Template Framework

**Document ID:** GH-0002
**Prepared by:** Lithium Dreams Industries / Glasshouse Systems Studio
**Status:** Internal Reference + Client Delivery Guide

---

> *These are not templates in the generic sense. Each one is a configured workspace — built for a specific kind of thinking, designed to get out of the way.*

---

## Overview

Glasshouse delivers 16 core Notion templates across four system suites. Each template is designed as a standalone tool that also connects to the larger system it belongs to. A client receiving the Research OS gets all four Research OS templates pre-configured and linked; a client receiving only the Signal Stack Pilot Build gets the two or three templates that drive that system specifically.

Every template has three states:
1. **Empty (delivered)** — clean structure, ready for the client's data
2. **Seeded (in training)** — pre-populated with example entries so the client can see what good looks like
3. **Live (in operation)** — running with real data, with automation filling certain fields

---

## 1. RESEARCH OS SUITE

### Template R-01: Daily Signal Brief

**Primary Database Type:** Notion page (auto-generated daily), sourced from a filtered view of the Source Registry and Synthesis Workspace.

**What It Is:** A compiled daily reading digest — not a raw feed dump, but a curated, summarized view of what changed overnight that actually matters to this operator's work. The brief is delivered as a new Notion page each morning, created by the Research Harness at a configured time (default: 6:30 AM).

**Key Properties (Brief Page)**
| Property | Type | Notes |
|---|---|---|
| Brief Date | Date | Auto-set on creation |
| Priority Items | Text | 2–3 items that need attention today |
| Signal Summary | Text | AI-generated paragraph: what changed, what to watch |
| Sources Surfaced | Relation | Links to Source Registry entries |
| Topics Covered | Multi-select | Configured topic tags |
| Action Required | Checkbox | Did any item generate a task? |
| Synthesis Link | Relation | Links to any Synthesis Workspace entries created |
| Review Status | Select | Unread / In Review / Filed |

**Key Views**
- **This Week** — brief pages from the current week, newest first
- **Flagged for Action** — filtered to items where Action Required = true
- **By Topic** — grouped by topic tag; useful for weekly pattern review
- **Archive** — all briefs beyond 30 days, collapsed for storage

**Automation Opportunities**
- Research Harness creates a new brief page at configured time daily
- Perplexity API pulls source content; Claude generates summary paragraph
- If Action Required is checked, a task is created automatically in Synthesis Workspace
- Weekly digest: Friday brief auto-includes a "Week in Review" section summarizing the five days

**Who Fills It vs. What AI Fills**
- AI fills: Signal Summary, Sources Surfaced (from registry), Topics Covered, initial Priority Items (flagged by keyword relevance score)
- Human reviews: Priority Items ranking, Action Required checkbox, any downstream synthesis decisions

---

### Template R-02: Source Registry

**Primary Database Type:** Notion database (table view primary, gallery for source logos)

**What It Is:** The master list of information sources the operator has decided to monitor. This is the configuration layer for the Research OS — the Research Harness reads this registry to know what to pull. It's also a reference document: when a new publication or expert appears, it gets evaluated and either added or consciously excluded.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Source Name | Title | The publication, person, feed, or site |
| Source Type | Select | Newsletter / RSS / Social / Database / Podcast / Person |
| URL / Handle | URL or Text | Where to find it |
| Topic Tags | Multi-select | What subject matter this source covers |
| Reliability Score | Select | High / Medium / Watch / Probationary |
| Update Frequency | Select | Daily / Weekly / Irregular |
| Active | Checkbox | Is this source currently being monitored? |
| Added Date | Date | When it entered the registry |
| Last Surfaced | Date | Auto-updated when source appears in a brief |
| Notes | Text | Why this source, what to watch for |
| Category | Select | Competitive / Industry / Regulatory / Inspiration / Personal |

**Key Views**
- **Active Sources** — filtered to Active = true, sorted by last surfaced
- **By Topic** — grouped by topic tag; useful when configuring a new brief focus
- **Review Queue** — sources flagged as Probationary, awaiting reliability assessment
- **Inactive Archive** — sources deactivated, preserved for reference

**Automation Opportunities**
- When a source is added with Active = true, the Research Harness config updates automatically
- Last Surfaced updates automatically each time the source appears in a Daily Signal Brief
- Weekly: sources not surfaced in 30 days get flagged for human review (still active? still useful?)

**Who Fills It vs. What AI Fills**
- Human fills: all source additions (this is a deliberate curation decision)
- AI assists: suggests sources based on topic tags (optional, requires human approval before adding)
- AI fills: Last Surfaced (automated from brief creation)

---

### Template R-03: Synthesis Workspace

**Primary Database Type:** Notion database (board view primary, table for volume)

**What It Is:** Where raw information becomes decisions. Every brief can generate a synthesis entry — a place to pull a thread, think through implications, and convert a signal into an action or an artifact (a memo, a proposal, a decision).

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Title | Title | What's the question being worked? |
| Status | Select | Incoming / Active / Stalled / Complete / Archived |
| Source Briefs | Relation | Which Signal Briefs fed this thread |
| Topic | Multi-select | Same tags as Source Registry |
| Priority | Select | High / Medium / Low |
| Output Type | Select | Decision / Memo / Action / Watchlist / Discard |
| Insight | Text | The core takeaway (written by human) |
| Context | Text | Background, relevant history |
| Open Questions | Text | What would need to be true for this to matter more? |
| Action | Relation | Links to any tasks created |
| Date Opened | Date | Auto-set on creation |
| Date Closed | Date | Set when Status = Complete |

**Key Views**
- **Active Board** — Kanban by Status; the daily working view
- **High Priority** — filtered to Priority = High, all statuses
- **By Topic** — grouped by topic tag; useful for pattern recognition across time
- **Recent Outputs** — filtered to Output Type = Decision or Memo, sorted by date closed

**Automation Opportunities**
- When Action Required is checked in a Daily Signal Brief, a new Synthesis entry is created automatically (linked to the source brief, status = Incoming)
- When Status = Complete and Output Type = Decision, a summary is added to the Decision Log (if using Executive Assistant OS)

**Who Fills It vs. What AI Fills**
- Human fills: Insight, Open Questions, final Output Type assessment
- AI fills: initial Context paragraph (from source brief summary), links to related Source Registry entries
- AI assists: drafts an opening synthesis paragraph on creation; human rewrites or accepts

---

### Template R-04: Competitive Watch Dashboard

**Primary Database Type:** Notion database (gallery view primary for scannability, table for detail)

**What It Is:** A structured intelligence file on each tracked competitor or market player. Not a news feed — a living document that accumulates signal over time and allows pattern recognition across months.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Entity Name | Title | Company, person, or initiative |
| Category | Select | Direct Competitor / Adjacent / Aspirational / Threat / Partner |
| Watch Priority | Select | High / Medium / Monitor |
| Last Development | Date | When something notable last happened |
| Recent Signal | Text | AI-generated summary of recent activity (updated weekly) |
| Key Moves | Text | Notable actions, launches, hires, statements |
| Our Positioning vs. This | Text | Human-written differentiation notes |
| Sources | Relation | Source Registry entries that cover this entity |
| Alert Keywords | Text | Terms that trigger an immediate brief flag |
| Notes | Text | Contextual observations |

**Key Views**
- **Watch Room** — gallery view, sorted by Last Development; the default visual scan
- **High Priority** — filtered to Watch Priority = High
- **Recent Activity** — sorted by Last Development, descending
- **My Differentiation** — filtered to entries with Our Positioning vs. This filled

**Automation Opportunities**
- Weekly: Claude generates a new Recent Signal summary for each active entity from the past week's Daily Signal Briefs
- Alert: if an Alert Keyword appears in a Daily Signal Brief, the related entity is flagged immediately
- Quarterly: a "competitive landscape" report is compiled from all High Priority entries

**Who Fills It vs. What AI Fills**
- Human fills: Our Positioning vs. This (this is strategic, not operational), Watch Priority, Alert Keywords
- AI fills: Recent Signal summary (weekly), Last Development date (when new signal detected)

---

## 2. CONTENT ENGINE SUITE

### Template C-01: Content Calendar

**Primary Database Type:** Notion database (calendar view primary, board by status secondary)

**What It Is:** The master production schedule for all content. Not a wish list — a live production tracker where every entry has a status, an owner, a due date, and a publish target. The Content Engine Harness reads this calendar to know what to draft, repurpose, and schedule.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Title | Title | Working title of the content piece |
| Content Type | Select | Podcast / Video / Newsletter / LinkedIn / Short-form / Email / Thread |
| Platform | Multi-select | Where it publishes |
| Status | Select | Idea / Briefed / In Draft / In Review / Scheduled / Published / Archived |
| Publish Date | Date | When it goes live |
| Due Date | Date | When the draft is due for review |
| Owner | Person | Who is responsible |
| Brief | Text | What this piece is about, what it needs to accomplish |
| Draft Link | URL | Link to the working draft (Notion page or external doc) |
| Atoms Generated | Relation | Links to Content Atom Library entries from this piece |
| Keywords / Tags | Multi-select | SEO or thematic tags |
| AI-Assisted | Checkbox | Was AI used in production? |
| Performance Notes | Text | Post-publish observations |

**Key Views**
- **This Month** — calendar view, filtered to current month
- **Production Pipeline** — board by Status; the daily working view for the content team
- **Platform View** — filtered and grouped by Platform
- **Needs Review** — filtered to Status = In Review; the editor's queue
- **Published Archive** — filtered to Status = Published, sorted descending

**Automation Opportunities**
- When Status changes to "Briefed," Content Engine Harness generates a first draft and sets Status to "In Draft"
- When Status changes to "Scheduled," Buffer API integration triggers scheduling
- Atoms: when Status = Published, a workflow prompts extraction of atoms into the Content Atom Library

**Who Fills It vs. What AI Fills**
- Human fills: Title (working), Content Type, Platform, Publish Date, Brief, performance notes
- AI fills: Draft Link (creates the draft page), suggests Keywords, generates atoms on publish

---

### Template C-02: Content Atom Library

**Primary Database Type:** Notion database (gallery view primary)

**What It Is:** The reusable idea inventory of the content operation. Every long-form piece contains 8–20 atoms — a quote, a hook, a framework, a statistic, a story beat, a question — that can be repurposed across platforms without starting from scratch. This library makes repurposing systematic rather than aspirational.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Atom Title | Title | Short descriptor of the idea |
| Atom Type | Select | Quote / Hook / Stat / Framework / Story Beat / Question / Argument / Example |
| Source Content | Relation | Links to Content Calendar entry it came from |
| Atom Text | Text | The actual text or idea, verbatim or paraphrased |
| Platform Fit | Multi-select | Where this atom works: LinkedIn / Twitter / Email / Podcast Intro / etc. |
| Status | Select | Unused / In Use / Retired |
| Used In | Relation | Links to Content Calendar entries where this atom was deployed |
| Date Created | Date | Auto-set on creation |
| Tags | Multi-select | Topic or theme tags |

**Key Views**
- **Unused Atoms** — filtered to Status = Unused; the default repurposing queue
- **By Type** — grouped by Atom Type; useful for finding the right kind of element
- **By Platform Fit** — filtered by platform; useful when writing for a specific channel
- **By Source** — grouped by Source Content; shows all atoms from one piece

**Automation Opportunities**
- When a Content Calendar entry is marked Published, Content Engine Harness processes the piece and creates 8–15 atom entries automatically (Claude-generated, human-reviewed)
- When an atom is used in a new piece, Status updates to "In Use" and Used In is updated

**Who Fills It vs. What AI Fills**
- AI fills: Atom Text extraction, Platform Fit suggestions, initial Atom Type classification
- Human reviews: all AI-generated atoms before Status is set to "Unused" (ready to use)
- Human fills: any manually identified atoms the AI missed

---

### Template C-03: Brand Voice Reference

**Primary Database Type:** Notion page (not a database — a reference document with embedded tables)

**What It Is:** The written specification of how this brand communicates. Not a mood board. Not a brand manifesto. A working reference that anyone producing content — human or AI — can open and use to calibrate. This is the most important document in the Content Engine. Everything downstream reads from it.

**Document Structure**
1. **Voice in One Sentence** — the shortest possible description of how this brand sounds
2. **The Tone Spectrum** — a 2×2 or 1-to-5 scale showing where the voice lives (formal ↔ casual, direct ↔ expansive, warm ↔ cool)
3. **We Sound Like** — 3–5 annotated examples of writing that captures the voice well, with notes on why they work
4. **We Don't Sound Like** — 3–5 examples of writing the brand avoids, with notes on why
5. **Vocabulary** — words and phrases the brand uses; words and phrases it avoids (the "never-say list")
6. **Sentence Architecture** — characteristic rhythm, length, structural patterns
7. **Platform Modifiers** — how the core voice adjusts for LinkedIn vs. email vs. podcast vs. short-form
8. **The Claude System Prompt** — the exact prompt used to configure Claude to write in this voice

**Key Properties (as a document)**
- No database structure — this is a reference page, not a database
- Updated quarterly or when voice drift is detected
- Version history preserved (Notion page history)

**Automation Opportunities**
- Claude system prompt is extracted from this document and loaded into the Content Engine Harness
- When the Brand Voice Reference is updated, the harness is manually reconfigured (requires a Glasshouse session or human builder)

**Who Fills It vs. What AI Fills**
- Human fills: everything in sections 1–7
- Glasshouse facilitates: voice calibration session; the reference is built collaboratively during onboarding
- AI fills: the Claude System Prompt (Glasshouse derives it from the sections above)

---

### Template C-04: Platform Publishing Checklist

**Primary Database Type:** Notion page (checklist template, duplicated per publish event)

**What It Is:** A per-piece, per-platform launch checklist. Every time a piece is ready to publish, a copy of this checklist is created and linked to the Content Calendar entry. Nothing goes out until the checklist is complete.

**Checklist Structure (example: Podcast Episode)**
- [ ] Episode audio exported at correct specs (mp3, 192kbps, normalized to -16 LUFS)
- [ ] Show notes written and formatted (intro hook, timestamps, links, CTA)
- [ ] Episode title finalized (no placeholder title)
- [ ] Thumbnail created and at correct dimensions
- [ ] Buzzsprout upload complete (audio + metadata + show notes)
- [ ] Publish date and time set in Buzzsprout
- [ ] LinkedIn post drafted and reviewed (links to episode)
- [ ] Newsletter section drafted (if this episode is featured this week)
- [ ] Atoms extracted and added to Content Atom Library
- [ ] Content Calendar status updated to Scheduled

**Platform variants maintained:** Podcast / YouTube / Newsletter / LinkedIn / Email Announcement / Short-form clip series

**Automation Opportunities**
- When Content Calendar Status changes to "Scheduled," a new checklist page is created automatically and linked to the entry
- Completion of checklist triggers Status change to "Published" (if auto-complete is enabled)

**Who Fills It vs. What AI Fills**
- Human checks: all checklist items (the checklist is a human accountability tool, not an automation)
- AI assists: can pre-fill some metadata fields (show notes structure, social caption draft) as a starting point

---

## 3. LOCAL BUSINESS OPS SUITE

### Template L-01: Lead Intake Tracker

**Primary Database Type:** Notion database (board by status primary, table for detail)

**What It Is:** The CRM layer of the Local Business Ops system. Every inbound inquiry — whether from a contact form, email, phone call, or referral — becomes an entry here. This is the system that The Front Door harness writes to automatically.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Lead Name | Title | Contact name or company name |
| Contact Info | Text | Email, phone — what was captured |
| Source | Select | Website Form / Referral / Email / Phone / Social / Event |
| Lead Type | Select | Configured per business — e.g., New Client / Vendor / Partnership |
| Status | Select | New / Contacted / Qualified / Proposal Sent / Won / Lost / Hold |
| Assigned To | Person | Who owns this lead |
| Date Received | Date | Auto-set on intake |
| Last Contact Date | Date | Updated on each touchpoint |
| Next Follow-Up | Date | When to reach out next |
| Lead Score | Select | Hot / Warm / Cold (AI-assigned, human-adjusted) |
| Intake Notes | Text | What they said / what they need |
| AI Qualification Summary | Text | Claude-generated summary of inquiry + fit assessment |
| Budget / Timeline | Text | If captured in intake |
| Follow-Up Sequence | Select | Which follow-up sequence applies |

**Key Views**
- **Active Board** — board by Status; the default working view
- **My Leads** — filtered to Assigned To = current user
- **Hot Leads** — filtered to Lead Score = Hot
- **Follow-Up Due Today** — filtered to Next Follow-Up = today
- **Won / Lost Review** — filtered to Status = Won or Lost; for pipeline analysis

**Automation Opportunities**
- The Front Door harness creates a new entry automatically on form submission
- Claude generates AI Qualification Summary and initial Lead Score
- Follow-Up Sequence trigger: when Lead Score is set, the corresponding email sequence is activated
- Next Follow-Up alert: Notion automation flags entries where Next Follow-Up is overdue

**Who Fills It vs. What AI Fills**
- AI fills: Date Received, AI Qualification Summary, initial Lead Score, Source (from intake form)
- Human reviews: Lead Score (adjusts as needed), Assigned To, Follow-Up Sequence selection, all active contact decisions

---

### Template L-02: Follow-Up Sequence Manager

**Primary Database Type:** Notion database (table view primary)

**What It Is:** The library of follow-up sequences — each sequence is a defined series of touchpoints (emails, calls, messages) that runs when a lead reaches a certain status. The Intake & Follow-Up Harness reads this database to know what to send and when.

**Key Properties (Sequence Library)**
| Property | Type | Notes |
|---|---|---|
| Sequence Name | Title | E.g., "New Inquiry — Service Inquiry," "Referral Welcome" |
| Trigger | Select | Which lead status or event activates this sequence |
| Total Steps | Number | How many touches |
| Duration | Number | Over how many days |
| Status | Select | Active / Draft / Retired |
| Last Edited | Date | Auto-updated |

**Key Properties (Sequence Steps — sub-database or inline)**
| Property | Type | Notes |
|---|---|---|
| Step Number | Number | 1, 2, 3... |
| Day | Number | Days after trigger (Day 1, Day 3, Day 7...) |
| Channel | Select | Email / Phone / SMS / LinkedIn |
| Template | Text | The message template with [variables] |
| Personalization Variables | Text | What Claude fills in (name, inquiry summary, etc.) |
| Goal | Text | What this step is trying to accomplish |
| AI-Generated | Checkbox | Is the actual message generated by AI from template? |

**Key Views**
- **Active Sequences** — filtered to Status = Active
- **By Trigger** — grouped by Trigger type
- **Step Drill-Down** — expanded view of all steps for a selected sequence

**Automation Opportunities**
- When a lead's Follow-Up Sequence is set in the Intake Tracker, the harness activates the sequence automatically
- Each step fires on its configured day; Claude personalizes the message using the template + lead data
- Human approval gate: all AI-drafted emails are queued for review before send (configurable — some clients turn this off for steps 3+)

**Who Fills It vs. What AI Fills**
- Human fills: Sequence structure, step timing, template text, goals
- AI fills: personalized message content from templates; sends on schedule
- Glasshouse builds: initial sequence library during onboarding; client edits templates over time

---

### Template L-03: Client Onboarding Checklist

**Primary Database Type:** Notion database (board by phase primary)

**What It Is:** A per-client onboarding tracker. When a lead converts to a client, a new entry is created here with a structured checklist of everything that needs to happen before work can start. This is the handoff point from The Front Door to The Delivery Rail.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Client Name | Title | New client name |
| Onboarding Phase | Select | Contract / Kickoff / Setup / Access / Active |
| Start Date | Date | When the engagement began |
| Target Ready Date | Date | When onboarding should be complete |
| Assigned To | Person | Internal owner |
| Contract Signed | Checkbox | |
| Invoice Sent | Checkbox | |
| Kickoff Scheduled | Checkbox | |
| Welcome Email Sent | Checkbox | |
| Access / Credentials Shared | Checkbox | |
| Notion Workspace Created | Checkbox | (if applicable) |
| Onboarding Call Complete | Checkbox | |
| First Deliverable Due | Date | |
| Notes | Text | Anything unusual about this onboarding |

**Key Views**
- **Active Onboardings** — filtered to Phase ≠ Active (i.e., still in onboarding)
- **Overdue** — filtered to Target Ready Date past and Phase ≠ Active
- **Recently Completed** — filtered to Phase = Active, sorted by Start Date descending

**Automation Opportunities**
- When a Lead in the Intake Tracker moves to "Won," a new Onboarding entry is created automatically
- Welcome email sequence triggers on creation (via Delivery Rail harness)
- Checklist completion triggers Phase change to Active and creates a new entry in the Service Delivery Tracker

**Who Fills It vs. What AI Fills**
- Human checks: all checklist items (intentional — onboarding is a relationship moment)
- AI sends: Welcome Email sequence (Claude-drafted, human-configured)
- Automation handles: creation of the entry, linking to the originating Lead record

---

### Template L-04: Service Delivery Tracker

**Primary Database Type:** Notion database (board by phase primary, Gantt/timeline for complex projects)

**What It Is:** The operational record of active client engagements. Not a project management app — a status system. Where is each client in their service relationship? What's next? What's overdue?

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Client Name | Title | Linked to onboarding record |
| Service Type | Select | Configured per business |
| Current Phase | Select | Phases configured per service type |
| Start Date | Date | |
| Renewal / End Date | Date | |
| Owner | Person | |
| Status | Select | On Track / Needs Attention / At Risk / Complete |
| Last Touchpoint | Date | Updated on each client interaction |
| Next Scheduled Action | Text | What happens next |
| Next Action Date | Date | |
| Revenue | Number | Monthly or project value |
| Notes | Text | |
| Satisfaction Signal | Select | Strong / Neutral / Concern (human judgment) |

**Key Views**
- **Active Clients** — filtered to Status ≠ Complete; default working view
- **Needs Attention** — filtered to Status = Needs Attention or At Risk
- **Renewals This Quarter** — filtered to Renewal/End Date within 90 days
- **Revenue Dashboard** — sum of Revenue field across active clients

**Automation Opportunities**
- 30-day renewal alert: when Renewal Date is within 30 days, entry is flagged automatically
- Last Touchpoint overdue: if no touchpoint in 14 days (configurable), entry moves to "Needs Attention"
- Monthly: a client health digest is compiled from all active entries

**Who Fills It vs. What AI Fills**
- Human fills: Satisfaction Signal, Next Scheduled Action, Status (this is judgment work)
- Automation fills: Last Touchpoint (when a follow-up email is sent by the harness)
- AI assists: drafts client status summary paragraphs for reporting

---

## 4. EXECUTIVE ASSISTANT OS SUITE

### Template E-01: Weekly Mission Brief

**Primary Database Type:** Notion page (auto-generated weekly), archived as database entries

**What It Is:** A compiled weekly context document — delivered before Monday begins. Not a to-do list. Not a calendar print. A briefing: here is what this week is, here is what you need to walk into it knowing, here is what was left unresolved from last week.

**Brief Structure (each weekly page)**
1. **Week Overview** — what kind of week is this? (heavy external / internal focus / travel / deadline-heavy)
2. **Key Commitments** — major calendar items with context, not just titles
3. **Open Decisions** — items from the Decision Log awaiting resolution
4. **Incoming This Week** — flagged emails and requests that need a response
5. **Horizon Watch** — anything due or expiring in the next 30 days worth flagging now
6. **Last Week's Unfinished Business** — carried items from the prior brief
7. **This Week's Intention** — a single sentence the executive writes (the only human-authored section)

**Key Properties (Brief Archive Database)**
| Property | Type | Notes |
|---|---|---|
| Week Of | Date | Monday of the week |
| Week Type | Select | External Heavy / Internal / Travel / Deadline / Normal |
| Open Decisions Count | Number | How many decisions were flagged |
| Items Resolved | Number | How many from the prior brief were closed |
| Brief Status | Select | Draft / Delivered / Reviewed |
| Executive Rating | Select | 1–5 (usefulness score, tracked for harness calibration) |

**Automation Opportunities**
- Operator Briefing Harness generates full brief from Gmail API + Google Calendar API + Decision Log + prior week's brief every Sunday evening
- Open Decisions count auto-populated from Decision Log
- Brief delivered to Notion (and optionally emailed) at configured time

**Who Fills It vs. What AI Fills**
- AI fills: sections 1–6 in full
- Human fills: section 7 (This Week's Intention) — this is the only required human input
- Human reviews: the whole brief before the week begins; corrections are noted for harness calibration

---

### Template E-02: Decision Log

**Primary Database Type:** Notion database (table view primary, board by domain secondary)

**What It Is:** The institutional memory of consequential decisions. Every significant choice — a hire, a pricing change, a strategic pivot, a vendor selection, a boundary set — lives here with its reasoning intact. When something is revisited six months later, the log is the answer to "why did we do this?"

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Decision Title | Title | What was decided, as a statement |
| Decision Date | Date | When it was made |
| Domain | Select | Configured per org: Finance / People / Product / Operations / Relationships / Strategy |
| Status | Select | Active / Revisit / Reversed / Superseded |
| Made By | Person | Who made the call |
| Decision Summary | Text | What was decided, in plain language |
| Context | Text | What was happening that made this decision necessary |
| Alternatives Considered | Text | What other paths were on the table |
| Reasoning | Text | Why this path over the others |
| Risks Noted | Text | What could go wrong; what was accepted |
| Revisit Date | Date | When to check if this decision still stands |
| Outcome | Text | (filled in later) — what actually happened |
| Source Meeting | Relation | Links to a meeting brief if applicable |

**Key Views**
- **Active Decisions** — filtered to Status = Active; the live decision landscape
- **Revisit Queue** — filtered to Revisit Date within 30 days
- **By Domain** — grouped by domain; useful for domain-specific reviews
- **Reversed / Superseded** — the decisions that changed; important historical record

**Automation Opportunities**
- When Revisit Date is within 7 days, entry is flagged in the Weekly Mission Brief
- When a meeting brief marks a decision as made, AI drafts a Decision Log entry from the meeting notes (human confirms before saving)

**Who Fills It vs. What AI Fills**
- Human fills: Decision Summary, Reasoning, Alternatives Considered — the judgment fields
- AI assists: drafts initial entry from meeting notes or email thread (human reviews and edits)
- Human fills: Outcome (in retrospect — this cannot be automated)

---

### Template E-03: Stakeholder Map

**Primary Database Type:** Notion database (gallery view primary for relationship overview)

**What It Is:** A relationship intelligence file. Not a contact directory — a strategic map of the people who matter to the executive's work: clients, investors, partners, advisors, vendors, and key relationships inside the organization.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Name | Title | Person or organization |
| Relationship Type | Select | Client / Investor / Partner / Advisor / Vendor / Internal / Prospect |
| Priority | Select | Strategic / Active / Maintain / Watch |
| Last Contact | Date | Updated on each touchpoint |
| Next Planned Contact | Date | When to reach out next |
| Contact Cadence | Select | Weekly / Monthly / Quarterly / As Needed |
| What They Care About | Text | What matters to this person in their context |
| Our Current Relationship | Text | Where things stand right now |
| History With Us | Text | Notable interactions, agreements, tensions |
| Preferred Contact Channel | Select | Email / Phone / In Person / Text |
| Overdue | Formula | Calculated: is Last Contact past the cadence threshold? |
| Notes | Text | Anything the executive should remember |

**Key Views**
- **Priority Map** — gallery view grouped by Priority; the default scanning view
- **Overdue Outreach** — filtered to Overdue formula = true
- **By Relationship Type** — filtered by type; used when preparing for a specific kind of meeting
- **Strategic Relationships** — filtered to Priority = Strategic; the inner circle

**Automation Opportunities**
- When Last Contact exceeds the Contact Cadence threshold, an outreach reminder is added to the Weekly Mission Brief
- When a meeting brief is completed with a stakeholder, Last Contact updates automatically
- AI drafts outreach messages from the "What They Care About" field + relationship history (human sends)

**Who Fills It vs. What AI Fills**
- Human fills: What They Care About, Our Current Relationship, History (these require judgment)
- Human maintains: all relationship decisions remain human
- AI assists: outreach draft from existing data (human reviews, always)
- Automation handles: Overdue calculation, reminder insertion into Weekly Brief

---

### Template E-04: Horizon Planner

**Primary Database Type:** Notion database (timeline view primary, board by time horizon secondary)

**What It Is:** The 30/60/90 day view of what's coming — not tasks, not calendar events, but horizons: the things the executive needs to be thinking about before they become urgent. Contracts expiring. Hiring decisions approaching. Renewals. Commitments made months ago that land soon. Strategic windows.

**Key Properties**
| Property | Type | Notes |
|---|---|---|
| Item Title | Title | What it is |
| Category | Select | Configured per exec: Finance / Relationships / Decisions / Commitments / Deadlines / Opportunities |
| Horizon | Select | This Month / 30–60 Days / 60–90 Days / Beyond 90 |
| Due / Target Date | Date | When it lands |
| Status | Select | On Track / Needs Prep / Needs Decision / At Risk / Complete |
| Owner | Person | Who is responsible for the preparation |
| Dependencies | Text | What needs to happen before this can be addressed |
| Linked Decisions | Relation | Decision Log entries connected to this horizon item |
| Notes | Text | Context, stakes, what preparation is needed |

**Key Views**
- **Timeline** — Notion timeline view, sorted by Due Date; the visual planning view
- **This Month** — filtered to Horizon = This Month
- **Needs Prep / Decision** — filtered to Status = Needs Prep or Needs Decision; action queue
- **Beyond 90** — early warning items; reviewed monthly

**Automation Opportunities**
- Items in "Beyond 90" automatically advance to "60–90 Days" then "30–60 Days" as time passes (Horizon field updates based on date proximity to Due Date)
- Items approaching "This Month" are flagged in the Weekly Mission Brief
- When linked Decision Log entries are created, the horizon item is automatically linked

**Who Fills It vs. What AI Fills**
- Human fills: all new horizon items (the executive or their EA adds these)
- AI populates: items surfaced from email analysis (contract renewals, calendar commitments far out) — flagged for human review before added
- Automation handles: Horizon field advancement as dates approach

---

## 5. THE TEMPLATE DELIVERY MODEL

### Notion Workspace Setup Process

Every Glasshouse client gets a purpose-built Notion workspace — not a template dump. The setup process has four phases:

**Phase 1: Architecture (Week 1)**
- New Notion workspace created under client's account (or within their existing workspace as a top-level space)
- System architecture established: which template suites, which databases, how they connect
- All databases configured with the client's specific properties (e.g., Lead Types, Service Types, Domain tags are all configured to the client's actual business, not generic placeholders)
- Linking structure established (how the Content Calendar relates to the Atom Library; how the Lead Tracker relates to the Onboarding Checklist)

**Phase 2: Seeding (Week 1–2)**
- Each template is populated with 5–10 example entries that reflect the client's actual context
- Example: the Source Registry is seeded with the client's actual publications, not "Example Newsletter 1"
- Example: the Follow-Up Sequence Manager is seeded with sequences that match the client's actual service types
- This seeding work is done collaboratively — Glasshouse builds the structure; the client provides the real content

**Phase 3: Harness Connection (Week 2–3)**
- Automation pipelines are configured and tested
- API connections established (with credentials held by the client or by Glasshouse depending on tier)
- Trigger/action flows tested with real data
- First automated brief or intake is run end-to-end before handoff

**Phase 4: Handoff & Training (Week 3–4)**
- Two training sessions (recorded, stored in the client's Notion workspace)
- Written SOP for each template: what it's for, how to use it, what to do when something looks wrong
- "First 30 days" guide: specific prompts for the first month of operation
- Glasshouse contact protocol: how to reach Glasshouse if something breaks or needs adjustment

---

### Onboarding Sequence

The client experience from signed contract to live system:

| Day | What Happens |
|---|---|
| Day 0 | Contract signed → automated onboarding email sent → Glasshouse workspace session scheduled |
| Day 1–3 | Pre-session questionnaire completed by client (context, existing tools, current workflows) |
| Day 5 | Architecture session (90 minutes, recorded) — Glasshouse builds the workspace structure live |
| Day 7 | Client reviews seeded workspace; sends feedback on property configurations |
| Day 10 | Harness configuration begins; client provides API credentials (via secure form) |
| Day 14 | First automated run (test brief, test intake, or test draft — depending on system) |
| Day 17 | Adjustments from test run applied |
| Day 21 | Training Session 1: how to use the templates day-to-day |
| Day 24 | Live operation begins |
| Day 28 | Training Session 2: troubleshooting, advanced configuration, editing sequences |
| Day 30 | 30-day check-in call; support window closes (or transitions to retainer) |

---

### Training Assets

Every client receives the following, stored inside their Notion workspace:

- **Workspace Tour** (recorded walkthrough, 20–30 minutes): John walks through every template, every view, every automation trigger
- **Template Quick Reference** (one page per template): what it's for, how to add to it, what the AI fills vs. what the human fills
- **"When Something Looks Wrong" Guide**: common failure modes, how to tell if an automation broke, when to contact Glasshouse vs. fix it yourself
- **The Brand Voice Calibration Guide** (Content Engine clients): how to refine the Brand Voice Reference and update the Claude system prompt
- **The Harness Health Check** (all harness clients): a monthly 15-minute checklist to confirm the harness is still running correctly

---

### Ongoing Maintenance

**What the client maintains:**
- Their actual content: entries, leads, decisions, briefs (the system is only as good as what's in it)
- Their Brand Voice Reference (kept current as the brand evolves)
- Their Source Registry (kept current as their information environment changes)
- Their Sequence templates (the message content — they know their clients better than Glasshouse does)

**What Glasshouse maintains (under retainer):**
- The Hermes orchestration layer
- API connections and credential rotation
- Harness health monitoring
- Template updates as Glasshouse's methodology evolves
- System architecture expansions when the client's needs change

**What Notion maintains:**
- The platform itself (Glasshouse does not warrant Notion uptime)

**The Support Protocol:**
- All Pilot Build clients: 30-day email support window post-launch
- All OS clients: ongoing priority support channel (Slack or email) under retainer
- Embedded clients: direct line to John; same-day response during business hours

---

*Document ID: GH-0002 | Glasshouse Systems Studio | Lithium Dreams Industries*
*For internal use and client delivery reference*
