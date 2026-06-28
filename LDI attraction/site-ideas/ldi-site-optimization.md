# OM-0020 — SITE OPTIMIZATION RECOMMENDATIONS
## Lithium Dreams Industries · Operations Memorandum
## Imagineering Division · Content Alive Assessment

```
╔══════════════════════════════════════════════════════════════════╗
║  DOCUMENT ID  : OM-0020                                          ║
║  CLASSIFICATION: IMAGINEERING OPS · INTERNAL USE ONLY           ║
║  STATUS       : ACTIVE                                           ║
║  FILED BY     : Operations, Imagineering Division                ║
║  DATE         : 2026-06-26                                       ║
║  SUBJECT      : lithium-dreams.com — Prioritized Optimization    ║
║  TAGLINE      : Filed after closing at the Last Roadside         ║
║                 Attraction.                                      ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## CONTENT ALIVE SCORE — BASELINE AUDIT

Rate: 1 (static/dead) → 5 (fully alive, dynamic, surprises returning visitors)

| Page | Score | Primary Deficit | Top Single Improvement |
|------|-------|----------------|------------------------|
| `/` | 3/5 | Hero feels like a poster, not a place | Rotating status message on the Attraction sign — different greeting each visit |
| `/attraction` | 3.5/5 | Incident Log exists but feels frozen | Add 2 new incident entries — the log should look like someone filed it recently |
| `/gift-shop` | 2.5/5 | Product grid feels like a placeholder | Add SOLD OUT badges on select items + a "BACKROOM INVENTORY" teaser |
| `/arcade` | 2/5 | High scores feel like a dev placeholder | Replace with lore-appropriate scores (see Tier 2) |
| `/museum` | 2/5 | "EXHIBIT BEING PREPARED" repeats multiple times | Replace with CLASSIFIED / INCOMING SPECIMEN teasers (see Tier 2) |
| `/fortune` | 4/5 | Archive link goes to `#` | Implement the Fortune Archive (see Tier 2) |
| `/chapel` | 3/5 | Guest registry feels thin | Add 2-3 stranger entries (see Tier 2) |
| `/chapel/back-room` | 3.5/5 | Exists, functions, but static | Add a "last visited" timestamp that changes |
| `/deep-garden` | 3/5 | Planting station form — unclear if it saves | Add a confirmation message in LDI voice |
| `/employees-only` | 2.5/5 | Access log is sparse | Populate with in-world entries (see Tier 2) |
| `/about` | 3/5 | Reads like a brand statement | Add a "Filed By" footer with an accession number — make it feel like a dossier page |
| `/work` | 4/5 | Clean Glasshouse aesthetic working well | Ensure case file count updates when new work is added |
| `/work/intake` | 4.5/5 | 6-step wizard is excellent | Add a "CASE RECEIVED" confirmation page in Glasshouse voice |
| `/work/case-files` | 3.5/5 | Grid is functional | Add a "CASE STATUS" filter (active / archived) |
| `/workshop` | 3/5 | Unclear what this page is for in the nav | Needs clearer purpose or a "RESTRICTED — CLEARANCE REQUIRED" teaser |
| `/broadcasts` | 0/5 | **404** | Implement per OM-0019 |
| `/broadcasts/midnight-visitor-log` | 0/5 | **404** | Implement per OM-0019 |
| `/shop` | 0/5 | **404** | Redirect to `/gift-shop` or implement |

---

## TIER 1 — CRITICAL FIXES
### Do First · These Are Broken

---

### T1-1 · /broadcasts — IMPLEMENT THE BROADCAST TOWER
**What:** Build `/broadcasts` and `/broadcasts/midnight-visitor-log/[slug]` as designed in OM-0019.
**Why:** The show is live. The website does not reflect it. Every episode that airs without a page on lithium-dreams.com is a missed indexing, SEO, and audience-routing opportunity.
**Implementation:** See OM-0019 in full. Astro Content Collections for episode data. YoutubeEmbed.astro + PodcastEmbed.astro components. Nav label: `THE LOG`.
**Priority:** Blocker-level. Fix before all other work.

---

### T1-2 · /broadcasts/midnight-visitor-log/[slug] — EPISODE PAGES
**What:** Individual episode pages per OM-0019 Section 2.
**Why:** These are the pages Google indexes, the pages fans share, the pages that build the archive.
**Implementation:** `src/pages/broadcasts/midnight-visitor-log/[...slug].astro` with Astro Content Collections. Frontmatter schema:

```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const episodes = defineCollection({
  type: 'content',
  schema: z.object({
    episodeNumber: z.number(),
    title: z.string(),
    caseSubject: z.string(),
    accessionNumber: z.string(),    // "MVL-EP001"
    publishDate: z.string(),        // ISO 8601
    youtubeId: z.string(),
    buzzsproutEpisodeId: z.string(),
    duration: z.string(),           // "PT45M30S"
    status: z.enum(['on-air', 'archived', 'field-recording']),
    tags: z.array(z.string()),
    witnessCount: z.number().optional(),
    theoriesDocumented: z.number().optional(),
    metaDescription: z.string().max(155),
    ogImagePath: z.string().optional(),
  }),
});

export const collections = { episodes };
```

---

### T1-3 · Fortune Archive — IMPLEMENT OR REDIRECT
**What:** The Fortune Archive link from `/fortune` currently goes to `#`. Build the page (see Tier 3 for full design) or, as an interim fix, redirect to `/fortune` with a message: "THE ARCHIVE IS BEING COLLATED. CHECK BACK."
**Why:** Dead links inside interactive features break immersion. The fortune oracle is one of the best interactive elements on the site — a broken archive link undercuts it.
**Interim fix (2 minutes):** Change `href="#"` to display an in-page modal or inline message.
**Full fix:** See T3-3 below.

---

### T1-4 · /shop — REDIRECT TO /gift-shop
**What:** `/shop` 404s. Implement a redirect.
**Why:** Users and external links may navigate to `/shop`. It should not 404.
**Implementation (Astro):**

```javascript
// astro.config.mjs
export default defineConfig({
  redirects: {
    '/shop': '/gift-shop',
  },
});
```

Or, in `_redirects` (Cloudflare Pages):
```
/shop  /gift-shop  301
```

**Time to implement:** 2 minutes. Do this immediately.

---

### T1-5 · ADD "THE LOG" TO NAVIGATION
**What:** Add nav item `THE LOG` linking to `/broadcasts`, second position in nav.
**Why:** No nav link to the show means every new visitor must find it by accident.
**Implementation:** See OM-0019 Section 6 for full nav upgrade spec including status badge.

---

## TIER 2 — QUICK WINS
### High Impact, Low Effort · One Session Each

---

### T2-1 · MUSEUM — Replace "EXHIBIT BEING PREPARED"

**What to do:** Replace every "EXHIBIT BEING PREPARED" placeholder with a differentiated teaser. Each should feel like a classified intake document, not a missing-image placeholder.

**Why it helps:** Multiple identical placeholders tell the visitor "this site is unfinished." Differentiated teasers tell the visitor "this place has secrets."

**Replacement copy patterns:**

```
┌────────────────────────────────────────┐
│  EXHIBIT [ACCESSION NUMBER]            │
│  SPECIMEN: [CRYPTID/SUBJECT NAME]      │
│  STATUS: ████ INCOMING                 │
│  ────────────────────────────────────  │
│  MATERIALS RECEIVED. CATALOGUING       │
│  IN PROGRESS. DO NOT DISTURB THE       │
│  COLLECTION UNTIL FURTHER NOTICE.      │
│                                        │
│  CLEARANCE REQUIRED FOR EARLY ACCESS.  │
└────────────────────────────────────────┘
```

Rotate through these status phrases instead of all saying the same thing:
- `INCOMING — CATALOGUING IN PROGRESS`
- `SPECIMEN ARRIVED — CONTAINMENT PENDING`
- `CLASSIFIED — CLEARANCE LEVEL 3 REQUIRED`
- `MATERIALS UNDER REVIEW — EXHIBIT DATE TBD`
- `FIELD EVIDENCE — AUTHENTICATION ONGOING`

**Implementation notes:** Find all placeholder blocks in the Museum page component. Replace static text with the appropriate teaser. No backend needed — these are static strings. Each exhibit slot should have a unique accession number (MUS-001, MUS-002, etc.) even before the exhibit is ready.

---

### T2-2 · ARCADE — Lore-Appropriate High Scores

**What to do:** Replace generic or placeholder high scores with in-world entries.

**Why it helps:** A leaderboard of random names or zeroes says "dev placeholder." A leaderboard of LDI employees and cryptid-themed handles says "this place has been running for decades."

**Recommended high score tables:**

```
COSMIC SELECTOR — TOP 10 PLAYERS
════════════════════════════════
RANK  INITIALS  SCORE
  1.  BOB       999,999  [SCORE INVALIDATED — MANAGEMENT DECISION]
  2.  GRY       847,440  UNVERIFIED
  3.  ???       600,000  [RECORD CORRUPTED — 1987 INCIDENT]
  4.  VLT       512,980
  5.  RMX       488,100
  6.  EMF       401,220
  7.  KAY       312,540
  8.  OWL       299,970
  9.  ___       250,010  [NAME REDACTED BY REQUEST]
 10.  NEW        10,000  ENTER YOUR INITIALS: _

NOTE FROM MANAGEMENT: Scores from the period
Oct 31–Nov 2, 1994 have been stricken from the
record pending investigation. We do not discuss
the 1994 incident.
```

```
MOTHMAN SIGNAL — TOP 5 INTERCEPTORS
════════════════════════════════════
  1.  [SIGNAL ANALYST 7]   LEVEL 33
  2.  B.O.B.               LEVEL 31  [RESULTS DISPUTED]
  3.  NIGHTWING            LEVEL 28
  4.  RED EYE              LEVEL 22
  5.  CURIOUS              LEVEL 19

CURRENT SIGNAL STRENGTH: ████░░░░ 52%
NEXT TRANSMISSION: UNDISCLOSED
```

**Implementation notes:** Hard-coded in the arcade page component. Add a note from management in monospace at the bottom of each cabinet card. The 1994 incident is a lore seed — leave it unexplained for now.

---

### T2-3 · EMPLOYEES ONLY — Populate the Access Log

**What to do:** Add in-world access log entries.

**Why it helps:** An empty or minimal access log reads as unfinished. A log with 8-10 entries reads as a place with history.

**Recommended entries (add to the existing log format):**

```
ACCESS LOG — EMPLOYEES ONLY
════════════════════════════════════════════════════════
TIMESTAMP          EMPLOYEE ID    ACCESS POINT    NOTE
────────────────────────────────────────────────────────
1994-10-31 23:47   EMP-0003       BACK ENTRANCE   AUTHORIZED. DO NOT FOLLOW.
2003-07-14 02:13   EMP-0007       STORAGE B       AFTER-HOURS. LOGGED PER PROTOCOL 4.
2011-03-01 09:00   EMP-0012       MAIN FLOOR      REGULAR SHIFT BEGIN.
2019-08-22 11:34   EMP-0001       RESTRICTED ZN.  CLEARANCE: OMEGA. NO FURTHER NOTES.
2021-12-13 03:03   EMP-????       UNRECOGNIZED    BADGE NOT ON FILE. REVIEWED.
2023-05-07 17:59   EMP-0003       STORAGE B       AGAIN. THIRD TIME THIS MONTH.
2024-11-01 00:00   EMP-0000       [ALL POINTS]    SYSTEM RESET. VISITOR LOG PURGED.
2026-06-20 21:14   EMP-0019       BROADCAST TWR.  ROUTINE MAINTENANCE. SIGNAL NOMINAL.
────────────────────────────────────────────────────────
[VISITOR ACCESS DENIED — EMPLOYEES ONLY]
```

**Notes:**
- EMP-0003 is a recurring mystery — show up, never explain
- EMP-0001 with OMEGA clearance implies hierarchy never shown to visitors
- The unrecognized badge from 2021 is a long-form lore hook
- EMP-0000 on November 1 is the Attraction's "birthday" — keep this date significant

---

### T2-4 · DEEP GARDEN — Planting Station Confirmation

**What to do:** Add a form confirmation message in LDI voice after submission.

**Why it helps:** Without confirmation, users don't know if the form worked. A confirmation in LDI voice turns a functional necessity into a moment of delight.

**Confirmation message:**

```
┌────────────────────────────────────────────────────┐
│  PLANTING CONFIRMED                                │
│  ─────────────────────────────────────────────── │
│  Your specimen has been logged.                    │
│                                                    │
│  The Garden keeps its own records.                 │
│  We do not guarantee what grows.                   │
│  We do not guarantee it stays where you plant it.  │
│                                                    │
│  ACC. GARDEN-[TIMESTAMP]                           │
│  STATUS: PLANTED ·  ROOT DEPTH: UNKNOWN            │
│  ─────────────────────────────────────────────── │
│  [RETURN TO THE GARDEN]  [PLANT ANOTHER]           │
└────────────────────────────────────────────────────┘
```

If the form currently does save submissions (to a database, spreadsheet, or Airtable), surface an accession-style confirmation number using the submission timestamp: `GARDEN-20261126-0047`. If it does not save, it should — visitor submissions are community content.

**Implementation notes:** Add a success state to the existing form component. On submit: hide the form, show the confirmation block. The `[RETURN TO THE GARDEN]` button reloads the page; `[PLANT ANOTHER]` clears and re-shows the form.

---

### T2-5 · CHAPEL — Guest Registry Expansion

**What to do:** Add 3 additional guest registry entries, stranger than the existing ones.

**Why it helps:** The chapel is a strong atmospheric page. A thin guest registry breaks the illusion of a place that has been operating for decades.

**Suggested additions:**

```
ENTRY #0047 — Filed: unknown date
Name: [ILLEGIBLE]
Party: 1 (I think)
Occasion: Passage
Comment: The flowers were lovely. The flowers
were also watching me. I did not mind.
Officiant: Asked not to be named.
─────────────────────────────────────────────

ENTRY #0048 — Filed: March 1989
Name: CAROLYN W.
Party: 2
Occasion: Second ceremony (the first one didn't take)
Comment: We tried in Reno first. Something about
this place felt more permanent. It was.
─────────────────────────────────────────────

ENTRY #0049 — Filed: "recently"
Name: REDACTED
Party: Redacted
Occasion: [FORM FIELD LEFT BLANK]
Comment: I found what I was looking for.
I am leaving it here for someone else.
It is in the third pew on the left.
Status: ITEM NOT FOUND UPON INSPECTION.
─────────────────────────────────────────────

ENTRY #0050 — Filed: ongoing
Name: OPEN ENTRY
Party: Variable
Occasion: Anyone who needs it
Comment: The door is always open after 11pm.
You don't need an appointment.
─────────────────────────────────────────────
```

**Implementation notes:** Hard-code into the registry component. Use a consistent date format that implies some entries have no date ("Filed: unknown date") — this is more interesting than a blank field.

---

### T2-6 · THE CATHEDRAL PAGE — Does It Exist?

**What to do:** Audit whether `/cathedral` exists. If not: create a minimal placeholder.

**Why it helps:** The "DO NOT FOLLOW ROOTS TOWARD THE CATHEDRAL" link on `/deep-garden` is one of the best mysterious moments on the site. If it 404s, it deflates the moment. If it resolves to something — even something minimal — it rewards the curious.

**Recommended minimum `/cathedral` page:**

```
┌────────────────────────────────────────────────────┐
│                                                    │
│                                                    │
│         YOU WERE TOLD NOT TO FOLLOW.               │
│                                                    │
│                                                    │
│  ACC. CAT-000                                      │
│  STATUS: RESTRICTED                                │
│  ──────────────────────────────────────────────  │
│  This area is not open to visitors.               │
│                                                    │
│  If you are reading this, you followed the roots. │
│                                                    │
│  The Cathedral has noted your arrival.             │
│                                                    │
│  [RETURN TO THE GARDEN]                            │
│                                                    │
└────────────────────────────────────────────────────┘
```

Dark background. No header. No footer. No nav. Possibly a subtle heartbeat or low breathing sound that autoplay cannot trigger (user must click). The page feels like a mistake — intentionally.

**Implementation:** `src/pages/cathedral.astro` — no layout wrapper, standalone page. Add a `<meta name="robots" content="noindex">` tag so it doesn't appear in search results (the discovery should be earned, not Googled).

---

## TIER 3 — MAKE IT FEEL MORE ALIVE
### Medium Effort, High Reward · "Living Site" Features

---

### T3-1 · ROTATING DYNAMIC CONTENT SYSTEM

**What:** A lightweight system for rotating content on multiple pages. No database needed — use JSON files in `public/data/` and client-side fetch, or Astro's `import.meta.glob` for build-time rotation.

**Targets:**
- Homepage: Rotating Attraction status message (different greeting per day of week or per hour)
- Marquee ticker: Rotating messages (50+ messages, cycling daily)
- Employees Only: Rotating safety bulletin

**Rotating Marquee Messages (add to ticker pool):**

```javascript
// public/data/marquee-messages.json
[
  "WELCOME TO THE LAST ROADSIDE ATTRACTION · MIND THE GAP BETWEEN THE WORLD AND THE NEXT",
  "TONIGHT'S FORECAST: UNUSUAL · TOMORROW'S FORECAST: SEE TONIGHT'S",
  "THE GIFT SHOP DOES NOT ACCEPT RETURNS ON ITEMS THAT HAVE ALREADY CHANGED HANDS",
  "ARCADE HIGH SCORES HAVE BEEN FROZEN PENDING INVESTIGATION OF THE 1994 INCIDENT",
  "THE GARDEN IS CLOSED AFTER 10PM · THE GARDEN DOES NOT ACKNOWLEDGE THIS POLICY",
  "MANAGEMENT REMINDS STAFF: DO NOT MAKE EYE CONTACT WITH EXHIBIT 7B",
  "SIGNAL: ACTIVE · THE LOG IS OPEN · KEEP WATCHING",
  "THE CHAPEL IS AVAILABLE FOR EVENTS · THE CHAPEL IS ALSO AVAILABLE FOR NON-EVENTS",
  "ALL FORTUNES DISPENSED BY BOB ARE FINAL · BOB DOES NOT ISSUE REFUNDS · BOB DOES NOT HAVE FEELINGS ABOUT THIS",
  "THERE IS NO CATHEDRAL · THERE HAS NEVER BEEN A CATHEDRAL · PLEASE STOP ASKING",
  "THE MUSEUM IS CURRENTLY ACCEPTING NEW SPECIMENS · DELIVERY HOURS: AFTER DARK ONLY",
  "EMPLOYEE OF THE MONTH: [REDACTED] · REASON FOR AWARD: [REDACTED] · PLEASE DO NOT DISCUSS THIS WITH [REDACTED]",
  "THE BROADCAST TOWER IS OPERATIONAL · SOMEONE IS ALWAYS RECORDING",
  "DO NOT FOLLOW THE ROOTS · THIS IS A REMINDER, NOT A SUGGESTION",
  "NEXT ATTRACTION: IN THE DARK, BEHIND YOU",
]
```

**Implementation:** The marquee ticker already exists. Pass it an array of messages from a JSON file. Use the current timestamp or day-of-week to select a deterministic rotation (so all visitors see the same message at the same time — it feels like a broadcast, not randomized spam).

```javascript
// Deterministic rotation — same message for everyone at the same hour
const hourOfWeek = Math.floor(Date.now() / (1000 * 60 * 60)) % messages.length;
const currentMessage = messages[hourOfWeek];
```

---

### T3-2 · ATTRACTION INCIDENT LOG — ONGOING FORMAT

The Incident Log on `/attraction` is a timeline. Design it to be maintainable as the lore grows.

**Format spec:**

```
INCIDENT LOG — LITHIUM DREAMS INDUSTRIES
Filed after closing at the Last Roadside Attraction.
════════════════════════════════════════════════════

[DATE] — [INCIDENT TYPE] — ACC. INC-[###]
[One to three sentences. Cold, institutional voice. End with an observation that raises more questions than it answers.]

────────────────────────────────────────────────────
```

**Data structure:** Move incidents to a JSON or YAML file:

```yaml
# src/data/incidents.yaml
- date: "1967-03-15"
  type: "FIRST CONTACT — CLASSIFIED"
  accession: "INC-001"
  body: "Site selected. Surveyor's notes indicate the ground was already warm. No geological explanation on file."
  status: "ARCHIVED"

- date: "1987-11-02"
  type: "STRUCTURAL — RESOLVED"
  accession: "INC-014"
  body: "East wing experienced unexplained tonal resonance for 72 hours. All clocks in the facility ran backward during this period. Clocks have since been replaced. The resonance has not been replaced."
  status: "ARCHIVED"

- date: "1994-10-31"
  type: "THE 1994 INCIDENT — RESTRICTED"
  accession: "INC-033"
  body: "[CLEARANCE LEVEL OMEGA REQUIRED TO VIEW THIS ENTRY]"
  status: "RESTRICTED"
```

**Adding new incidents:** The team writes a new entry in the YAML file and redeploys. The page renders them chronologically. Mark recent incidents with `STATUS: ACTIVE` to make the log feel current.

---

### T3-3 · FORTUNE ARCHIVE — ASK BOB'S COMPLETE CATALOGUE

**What:** A `/fortune/archive` page listing all fortunes that Bob has ever dispensed, archived by number.

**URL:** `/fortune/archive`

**Page header:**
```
BOB'S FORTUNE EMPORIUM — COMPLETE ARCHIVE
ACC. FORT-ARCH-001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FORTUNES DISPENSED: [COUNT]
LAST UPDATED: [DATE]
DISCLAIMER: Bob's fortunes are accurate. Bob's
fortunes are not always accurate in the way you
expect. Bob is not responsible for what you do
with the information.
```

**50+ Fortune Seed List (use as the initial archive):**

```
FORT-001  The door you are afraid to open is the one that was already open.
FORT-002  Something is watching you read this. It means well.
FORT-003  The next time you hear a sound you cannot explain, write it down. You will need it later.
FORT-004  You are not lost. The map is lost. You are exactly where you are.
FORT-005  The thing you are waiting for has already arrived. You called it by a different name.
FORT-006  Do not make a promise in a place like this. The walls remember.
FORT-007  The road that ends at the water has not ended.
FORT-008  Someone you know is thinking of you right now. They are thinking of the version of you that was six years ago. This is not a bad thing.
FORT-009  The signal you have been trying to receive is not broken. You are not the intended recipient.
FORT-010  The photograph you took will show something you did not see. Don't look at it alone.
FORT-011  You have been here before. It was different then. So were you.
FORT-012  The thing in the corner of the room is a chair. Probably.
FORT-013  A door will open on its own tonight. This is expected. Do not mention it to anyone.
FORT-014  The number you are thinking of is not significant. The number you are not thinking of is.
FORT-015  Your future is bright. Bright in the way that something is bright just before it is dark.
FORT-016  An animal you do not expect to see will cross your path. It is looking for the same thing you are. It will find it first.
FORT-017  The voice on the radio was speaking to you specifically. You were right to be unsettled.
FORT-018  There is a field you have never visited that remembers you.
FORT-019  The pattern you have been noticing is not a coincidence. The coincidences are the pattern.
FORT-020  Someone will leave a door open for you. They will not remember doing it.
FORT-021  The longest route is the correct one.
FORT-022  You have already made the right decision. You made it before you knew there was a decision to make.
FORT-023  The light at the end of the road is a gas station. The gas station has been closed since 1991. Keep driving.
FORT-024  Do not read the sign on the way back. It will say something different.
FORT-025  You will recognize it when you see it. You may not want to.
FORT-026  The answer is yes. The question is the part that will take time.
FORT-027  Something you lost is not gone. It has been reassigned.
FORT-028  Trust the dog. The dog knows.
FORT-029  The person who handed you something today was thanking you for something you have not done yet.
FORT-030  The last thing you expected to happen today has not happened yet.
FORT-031  A phone will ring in an empty room. Do not answer it. The call is for someone else.
FORT-032  The bridge is fine. The bridge has always been fine. The feeling is not about the bridge.
FORT-033  You are going to sleep well tonight. This has been arranged.
FORT-034  Whatever you are building, finish it. The unfinished things accumulate.
FORT-035  Write your name somewhere unusual before the year is out. This is not a threat.
FORT-036  The map has a gap where you are standing. This is consistent with all previous maps of this area.
FORT-037  Something followed you home. It is harmless. It is also very patient.
FORT-038  The sound you heard was not the house settling. Houses do not settle like that.
FORT-039  If you have been counting, you have miscounted. Start again.
FORT-040  The person who told you "it's fine" was half right.
FORT-041  You will see an animal tonight that does not blink. Note the time.
FORT-042  The thing growing in the garden was not planted. Let it grow.
FORT-043  You are being followed by good luck. Good luck has been having a rough year.
FORT-044  The door at the end of the hallway goes somewhere. It has always gone somewhere.
FORT-045  Your question has been received. Bob is processing. Please do not ask again tonight.
FORT-046  The shadow you saw was not yours. You do not need to know whose it was.
FORT-047  Tomorrow will feel like it has happened before. This is normal. This location has a tendency to do that.
FORT-048  The signal is strong tonight. Someone is listening.
FORT-049  There is one fortune in this archive that is specifically about you. You will not know which one.
FORT-050  Keep the log open. I'll see you in the dark.
```

**Archive layout:** Grid of fortune cards, numbered. Each card shows the accession number (FORT-001) and the fortune text. A "GET YOUR FORTUNE" button links back to `/fortune`. Bob's signature or seal at the bottom.

**Implementation notes:** Store fortunes in `src/data/fortunes.json`. The oracle at `/fortune` draws from the same array (ensuring archive and oracle are always in sync). Add a "Today's Fortune" highlight at the top of the archive that shows fortune #[day of year % 50].

---

### T3-4 · THE SIGNAL FROM THE CATHEDRAL — OCCASIONAL INTERFERENCE

**What:** A subtle CSS/JS glitch effect that appears on select pages, randomly, suggesting something is interfering with the signal. Not disruptive — atmospheric.

**Trigger rules:** Fires once per session, on one of: homepage, /museum, /deep-garden, /attraction. Probability: 15% on each page load. Not on /work (Glasshouse aesthetic must remain clean).

**Effect options (use one at a time — restraint is key):**

Option A — Brief scan line:
```css
@keyframes scanline {
  0% { transform: translateY(-100%); opacity: 0.03; }
  100% { transform: translateY(100vh); opacity: 0.03; }
}
.cathedral-interference::after {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(255,255,255,0.015) 2px,
    rgba(255,255,255,0.015) 4px
  );
  pointer-events: none;
  animation: scanline 8s linear;
  z-index: 9999;
}
```

Option B — Text glitch on a random heading:
A random `<h2>` on the page briefly displays scrambled characters then returns to normal. Duration: 800ms. This feels like a transmission error.

Option C — Status bar flash:
The bottom marquee ticker briefly shows: `SIGNAL FROM THE CATHEDRAL — [UNINTELLIGIBLE] — SIGNAL LOST` before returning to normal.

**Implementation:** Small vanilla JS snippet that fires probabilistically on page load. Respect `prefers-reduced-motion: reduce`.

---

### T3-5 · ROTATING EMPLOYEE SAFETY BULLETINS

**What:** The Employees Only page shows a rotating safety bulletin. Changes weekly.

**Sample bulletins:**

```
SAFETY BULLETIN #44 — WEEK OF [DATE]
────────────────────────────────────────
Do not leave food unattended in Storage B.
This is the fourth bulletin on this subject.
We have counted the incidents. Storage B is
aware of this bulletin.

SAFETY BULLETIN #45 — WEEK OF [DATE]
────────────────────────────────────────
The wiring in the East Wing has been assessed.
Assessment results are: satisfactory, with
exceptions. The exceptions are not being
disclosed at this time. Use the East Wing
as normal.

SAFETY BULLETIN #46 — WEEK OF [DATE]
────────────────────────────────────────
Reminder: The buddy system is in effect for
all after-hours visits to the Garden.
The buddy does not need to be human.
The buddy does need to agree to accompany you.
```

---

## TIER 4 — BIG SWINGS
### High Effort, High Reward · Planned for Future Phases

---

### T4-1 · THE WITNESS REGISTRY — Community Submission Hub

**What:** A curated community submission page where fan/audience field reports get posted in LDI's in-world format.

**Page URL:** `/broadcasts/witness-registry`

**Submission flow:**
1. Fan submits a field report via a form (linked from `/broadcasts` CTA)
2. The team reviews submissions offline
3. Approved submissions are formatted in LDI dossier style and posted to the page
4. Each submission gets an accession number: WIT-[###]

**Submission form fields:**
- Witness name (or handle/alias — submissions do not require real names)
- Date of incident
- Location (general — city/state or region, not address)
- Type of incident (select: sighting / sound / electromagnetic / disappearance / other)
- Report body (textarea, 500 chars max)
- Would you like to be contacted? (yes/no — email optional)

**Posted format:**
```
WIT-0023 — [DATE FILED]
WITNESS: [NAME/HANDLE]
LOCATION: [REGION]
INCIDENT TYPE: [TYPE]
────────────────────────
[Report body, formatted in LDI voice. Light editorial only — preserve the original report's character.]
STATUS: RECEIVED AND FILED
────────────────────────
```

**Implementation options:**
- Simple: Google Form for collection, manually post to a JSON file after review
- Advanced: Airtable form → Airtable base → Cloudflare Pages Function pulls approved records via API and renders dynamically
- Backend-light: Netlify Forms or Cloudflare Pages Forms for collection; manual JSON curation pipeline for posting

---

### T4-2 · MUSEUM — MOTHMAN AS THE FIRST FULL EXHIBIT

**What:** Build out the first real Museum exhibit: Mothman (connects directly to Episode 1 of The Midnight Visitor Log).

**URL:** `/museum/mothman` — accessible from museum index

**Exhibit structure:**
```
MUS-001 — THE MOTHMAN
ACC. MUS-001
STATUS: ACTIVE · OPEN FOR VIEWING
────────────────────────────────────────

[SPECIMEN PHOTOGRAPH OR ILLUSTRATION]

CLASSIFICATION: Cryptid · Avian-Humanoid
FIRST DOCUMENTED SIGHTING: November 12, 1966
LOCATION: Point Pleasant, West Virginia
HEIGHT: Estimated 6-7ft
WINGSPAN: 10-15ft (disputed)
THREAT ASSESSMENT: [REDACTED]

────────────────────────────────────────
FIELD NOTES

[Long-form exhibit text in LDI dossier voice. 400-600 words. Cover: the 1966-67 sighting wave, the Silver Bridge collapse, the Keel hypothesis, the electromagnetic interference correlation, the connection to Episode 1 of The Midnight Visitor Log.]

────────────────────────────────────────
RELATED TRANSMISSIONS
→ MVL-EP001: The Mothman Signal [link]

INCIDENT TAGS: #pointpleasant #mothman
#electromagnetic #eyewitness #bridge

────────────────────────────────────────
[← MUSEUM INDEX]  [NEXT EXHIBIT: PENDING →]
```

**Cross-linking:** The museum exhibit links to the MVL episode, and the episode page links to the museum exhibit. These two content types reinforce each other and increase time-on-site.

---

### T4-3 · EMPLOYEES ONLY — REAL AUTHENTICATION

**What:** Make `/employees-only` actually restricted. Two options:

**Option A — Cloudflare Access (recommended for LDI):**
Cloudflare Access can restrict a path to specific email addresses or Google accounts. Free tier covers this use case. The aesthetic of "you must authenticate to enter" is very on-brand.

Implementation: In Cloudflare Zero Trust dashboard, add an Access Policy for `lithium-dreams.com/employees-only` → Allow only specific email addresses or a Google Workspace domain. The login page can be customized with LDI branding.

**Option B — Simple password gate:**
A client-side password prompt (not secure against determined visitors, but adds friction and aesthetics):

```javascript
// On page load:
const pass = sessionStorage.getItem('ldi-clearance');
if (pass !== 'OMEGA1994') {
  document.getElementById('access-gate').style.display = 'flex';
  document.getElementById('page-content').style.display = 'none';
}
```

Password displayed: a badge-style prompt that looks like a keycard reader. Wrong password response: "ACCESS DENIED — BADGE NOT RECOGNIZED — INCIDENT LOGGED." Right password: "CLEARANCE CONFIRMED — WELCOME, EMPLOYEE — REMEMBER: WHAT HAPPENS HERE IS FILED."

**Option C — No authentication, just the illusion:**
Keep the page publicly accessible but surround it with enough in-world friction that casual visitors feel like they've found something. The current approach; deepen it with the access log entries from T2-3.

**Recommendation:** Start with Option C (access log), move to Option B (password gate) once content is deeper, consider Option A (Cloudflare Access) if the team wants a private backstage area.

---

### T4-4 · ARCADE GAMES — BROWSER PLAYABLE CABINETS

**What:** Turn at least one of the listed arcade cabinets into an actual playable browser game.

**Priority target: COSMIC SELECTOR**

A simple game could be built in a single Astro page using vanilla canvas or a minimal JS game library:

**Concept:** A slot-machine style game where you pull for a "cosmic reading." Three columns spin and align on symbols: cryptids, locations, omens. Your reading is determined by the combination. 50-100 unique readings, all in LDI voice. Adjacent to the Fortune oracle in spirit, but with an interaction mechanic.

**Alternative simpler build: MOTHMAN SIGNAL**

A one-button game: a signal strength meter fluctuates randomly. Your goal is to press the button at the exact moment the signal peaks. The "score" is your signal quality percentage. High scores stored in `localStorage`. Three rounds per play.

**Tech:** Vanilla JS + Canvas. No dependencies. Built as a standalone Astro page. Load the game only when the player clicks the cabinet — don't load game assets on the arcade index page.

**Time estimate:** MOTHMAN SIGNAL (simple mechanic): 4-6 hours. COSMIC SELECTOR (slot + readings): 8-12 hours.

---

## CROSS-CUTTING RECOMMENDATIONS

### The Accession Number System — Formalize It

Currently accession numbers appear on some pages but not consistently. Make them a design system standard:

| Section | Format | Example |
|---------|--------|---------|
| Broadcasts hub | BRD-### | ACC. BRD-001 |
| Episodes | MVL-EP### | ACC. MVL-EP001 |
| Museum exhibits | MUS-### | ACC. MUS-001 |
| Incidents | INC-### | ACC. INC-033 |
| Fortunes | FORT-### | ACC. FORT-049 |
| Garden submissions | GARDEN-[timestamp] | ACC. GARDEN-20261126-0047 |
| Witness reports | WIT-### | ACC. WIT-0023 |
| Cathedral | CAT-### | ACC. CAT-000 |
| Chapel entries | CHAP-### | ACC. CHAP-0050 |
| Pages/documents | Various | ACC. BRD-001 |

Every page should have an accession number in the footer or header (small, monospace, muted). This unifies the aesthetic across all sections and makes everything feel catalogued.

### The Status Badge System — Apply Everywhere

| Badge | Color | Use When |
|-------|-------|----------|
| OPEN | Green pulse | Active, operational |
| ACTIVE | Solid green | Live, broadcasting |
| UNSTABLE | Amber pulse | Something weird is happening |
| FLICKERING | Amber/white alternating | Intermittent, unreliable |
| RESTRICTED | Red static | Access limited |
| UNDER REPAIR | Yellow, no pulse | Intentionally offline |
| INCOMING | Blue | New exhibit/content arriving |
| ARCHIVED | Gray, no animation | Historical, read-only |
| DORMANT | Dark gray | Inactive but not gone |
| CLASSIFIED | Red, no pulse | Content hidden intentionally |

Apply a status badge to every page in the nav, every exhibit in the museum, every episode in the archive, every cabinet in the arcade. The site should feel like everything has been assessed and logged.

### /work vs. LDI — The Dual Aesthetic Contract

The Glasshouse Systems Studio at `/work` maintains a clean, light, professional aesthetic distinct from the dark LDI experience. This is a strength — it serves two different audiences (potential clients vs. fans/community). 

**Rules to preserve this:**
- No LDI marquee ticker on `/work` pages
- No LDI Radio widget on `/work` pages (or render it minimal/hidden)
- No status badges on `/work` pages (they belong to the Attraction)
- The back-link from `/work` to the main LDI site should be subtle ("← LDI MAIN") not a full nav toggle
- The `/work/intake` wizard should stay in Glasshouse voice — institutional but clean, not dark and cryptid-themed

The dual aesthetic is part of the brand story: LDI is the Attraction; Glasshouse Systems Studio is the business. They coexist but do not bleed into each other.

---

## IMPLEMENTATION PRIORITY MATRIX

```
PRIORITY  EFFORT    DOCUMENT
────────────────────────────────────────────────────────────
T1-1      HIGH      /broadcasts hub (OM-0019)
T1-2      HIGH      Episode pages (OM-0019)
T1-3      LOW       Fortune Archive link → interim fix
T1-4      1 min     /shop redirect
T1-5      LOW       Nav: add THE LOG

T2-1      LOW       Museum placeholders
T2-2      LOW       Arcade high scores
T2-3      LOW       Employees Only log
T2-4      LOW       Deep Garden confirmation
T2-5      LOW       Chapel guest registry
T2-6      LOW       /cathedral page

T3-1      MED       Rotating marquee messages
T3-2      MED       Incident Log format + YAML
T3-3      MED       Fortune Archive (50 fortunes)
T3-4      MED       Cathedral interference glitch
T3-5      LOW       Employee safety bulletins

T4-1      HIGH      Witness Registry
T4-2      HIGH      Mothman Museum exhibit
T4-3      MED-HIGH  Employees Only auth
T4-4      HIGH      Arcade browser games
```

---

```
╔══════════════════════════════════════════════════════════╗
║  OM-0020 · END OF DOCUMENT                               ║
║  Filed after closing at the Last Roadside Attraction.    ║
║  Keep the log open. I'll see you in the dark.            ║
╚══════════════════════════════════════════════════════════╝
```
