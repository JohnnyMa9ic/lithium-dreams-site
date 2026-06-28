```
╔══════════════════════════════════════════════════════════════════════════════╗
║  LITHIUM DREAMS INDUSTRIES — IMAGINEERING DIVISION                         ║
║  DOCUMENT ID: MN-0003                                                       ║
║  CLASSIFICATION: INTERNAL OPERATIONS — OWNED AUDIENCE ARCHITECTURE         ║
║  ISSUED: 2026-06-27                                                          ║
║  CLEARANCE LEVEL: FULL ACCESS                                               ║
║  STATUS: OPERATIONAL — IMPLEMENT FROM SCRATCH                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

SUBJECT: NEWSLETTER & OWNED AUDIENCE ARCHITECTURE — COMPLETE OPERATIONAL SPEC
FILED BY: Imagineering Division
ANNOTATION SIGNATORIES: Bob (§3), Ghost (§9), Warden (§1, §6)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

# LDI NEWSLETTER & OWNED AUDIENCE ARCHITECTURE
## MN-0003 — Full Operational Document

---

## SECTION 1: WHY EMAIL IS THE ONLY CHANNEL YOU OWN

YouTube demonetized 40,000 channels in 2023 without prior notice. Patreon restructured its fee model mid-season and creators absorbed the loss. TikTok spent eighteen months under a federal ban threat that finally materialized in January 2025. Twitter changed its API terms twice in one year, cutting off third-party scheduling tools overnight. Twitch gutted its revenue share. Tumblr sold to people who sold it to other people. Facebook organic reach dropped from 16% to under 2% in a single algorithm update and never recovered.

None of those things can happen to your email list.

The email list is the only subscriber asset that does not belong to a platform. It is a file. A spreadsheet of names and addresses. It travels with you. It cannot be demonetized. It cannot be deplatformed. It cannot be algorithmed into irrelevance. When everything else burns — and eventually something always burns — the list is what you carry out.

> **THE LDI FRAMING:** *The newsletter is the signal that goes out no matter what's happening at the Attraction. Platforms are the roads. Email is the radio tower.*

The practical case is equally blunt:

- **Average email open rate across industries: 38–42%.** Average YouTube click-through rate on a notification: 2–6%. Average Instagram story view rate for accounts under 100k: 4–8%. Email is not a legacy format. It is the highest-engagement channel that exists at scale.
- **You own the relationship.** A YouTube subscriber is a relationship mediated by Google. A Patreon backer is a relationship mediated by Patreon. An email subscriber is a direct relationship. If lithium-dreams.com shuts down tomorrow, you can email every subscriber and tell them where you went.
- **Email converts.** Newsletter-to-paid conversion typically runs 2–5x higher than social. The people on your email list want to be there. They said so. They clicked confirm.
- **Deliverability compounds.** A 500-person list with 45% open rate sends better algorithmic signals to Gmail and Outlook than a 50,000-person list at 8% open rate. List hygiene is not a chore — it's the engine.

> **[WARDEN ANNOTATION]:** *A list of 500 people who open your emails is not a small list. It is 500 people who have chosen, twice — once to subscribe, once to open — to let you into their day. That is not a audience. That is a relationship. Build it like one. The numbers will follow, but the relationship has to come first. I have watched media properties collapse when they got the order backwards.*

This document is the complete operational architecture for LDI's owned audience. Someone should be able to implement the full newsletter system — from platform selection to automation stack — using only what follows.

---

## SECTION 2: PLATFORM SELECTION

### The Three Contenders

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PLATFORM COMPARISON — LDI NEWSLETTER USE CASE                             │
│  Evaluated against: world-building aesthetic, monetization, automation,    │
│  deliverability, long-term stability                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Criterion | Beehiiv | ConvertKit (Kit) | Substack |
|---|---|---|---|
| **Free tier** | Up to 2,500 subscribers | Up to 10,000 (limited features) | Unlimited free subscribers |
| **Paid tier cost** | $42/mo (Scale) · $84/mo (Max) | $25/mo (Creator) · $50/mo (Pro) | Free — takes 10% of paid revenue |
| **Built-in paid newsletter** | Yes — charge subscribers directly | Yes — via "Commerce" | Yes — 10% platform cut |
| **Design customization** | High — custom CSS, clean templates | Moderate — visual builder | Very low — one basic layout |
| **Analytics** | Excellent — open rate, click map, subscriber growth | Good | Basic |
| **Referral program** | Built in | Requires integration | No |
| **Automation/sequences** | Good | Excellent — industry-leading | Minimal |
| **Discovery network** | Growing Beehiiv network | None | Strong — especially niche/paranormal |
| **Brand control** | High — your domain, your design | High | Low — everything feels like Substack |
| **Aesthetic fit for LDI** | High | Moderate | Low |
| **Platform risk** | Moderate (VC-backed, growing) | Low (profitable, stable) | Moderate (dependent on paid growth) |
| **API / integrations** | REST API available | REST API, strong Zapier support | Very limited |
| **Deliverability** | Excellent | Excellent | Good (shared infrastructure) |

---

### Beehiiv: Assessment

**Recommendation for LDI: YES — Primary Platform**

Beehiiv wins for LDI on aesthetic grounds first and structural grounds second.

The design system is clean enough to be customized into the dossier aesthetic without fighting the platform. Custom CSS is available at the Scale tier. The dark-on-light template base is workable. Most importantly, Beehiiv treats the newsletter as a *publication* — it has a web reader, an archive, and a profile page — which maps directly to how the Attraction works as a world, not just an email.

The referral program is operationally significant: "Refer 3 visitors to get the Extended Visitor Dossier" is a natural list-building mechanic that requires zero additional tooling on Beehiiv.

The built-in paid newsletter tier means Patreon is optional — subscribers who don't use Discord or want community can go paid directly through email. This reduces platform dependency.

The 2,500 free subscriber cap is adequate for launch. The jump to $42/mo (Scale) is reasonable and should be triggered at ~1,500 subscribers (before hitting the wall, not after).

**Limitations:** Automation sequences are less sophisticated than Kit. Complex multi-branch drips require workarounds. For launch, this is acceptable.

---

### ConvertKit (Kit): Assessment

**Recommendation for LDI: SECONDARY / FUTURE OPTION**

Kit's automation engine is the best in class. The visual sequence builder, conditional logic, and tag-based segmentation are genuinely excellent — when the LDI list is large enough and the content complex enough to need them, Kit becomes compelling.

The free tier up to 10,000 subscribers is generous, but the free tier strips the features that matter (no landing page A/B tests, limited automations). At the point where Kit's automation power matters, you're paying anyway.

Kit does not have native design polish. The emails look like creator emails. Making them look like LDI dossiers requires more effort than Beehiiv.

**Verdict:** Migrate to Kit when the list exceeds 5,000 subscribers and automation complexity demands it, *or* use Kit from the start if the Win-Back and Welcome sequences are the operational priority. For launch, Beehiiv is the right call.

---

### Substack: Assessment

**Recommendation for LDI: NO — Do Not Use as Primary Platform**

Substack's discovery network is the only genuine advantage. Paranormal, weird history, and regional mystery content does perform well in Substack's native discovery. That is real.

Everything else is a problem:

- The 10% cut compounds badly. At $5/mo × 200 paid subscribers ($1,000 MRR), Substack takes $100/mo. Beehiiv's $42/mo flat fee breaks even at ~420 paid subscribers and saves money beyond that.
- Design customization is essentially nonexistent. Every Substack newsletter looks like Substack. The LDI dossier aesthetic cannot be expressed in a Substack template.
- The platform is building a media brand (Substack Notes, Substack video) that is increasingly in tension with the creators on it. Platform risk is not zero.
- Substack owns the relationship in ways that other platforms do not. List export exists but the ecosystem locks you in.

**One exception:** A *Substack publication as a discovery funnel* — a trimmed version of the newsletter that links back to lithium-dreams.com for sign-up — could be a valid cross-posting strategy. Not primary infrastructure.

---

### Platform Decision Summary

```
PRIMARY:   Beehiiv (Scale tier at $42/mo, triggered at ~1,500 subscribers)
SECONDARY: ConvertKit migration consideration at 5,000+ subscribers
AVOID:     Substack as primary infrastructure
OPTIONAL:  Substack as discovery channel / cross-post feed only
```

**Custom domain:** All email should send from `transmissions@lithium-dreams.com` (or see Section 3). All web archives should live at `newsletter.lithium-dreams.com` via Beehiiv custom domain. Never send from a Beehiiv subdomain.

---

## SECTION 3: THE NEWSLETTER IDENTITY

### Name Selection

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CANDIDATE NAMES — EVALUATION                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**"The After-Closing Brief"** — Strong operational metaphor. "Filed after the Attraction shuts for the night" maps exactly to what it is. "Brief" connotes both the dossier format and the military/intelligence briefing aesthetic. Problem: "Brief" as a name slightly undersells the world — it sounds transactional.

**"Signal From the Attraction"** — Good Ghost energy. Transmission metaphor lands. "From the Attraction" grounds it geographically in the world. Problem: slightly passive construction.

**"The Incident Report"** — In-world, clean, incident-log framing is natural. Works perfectly as a container for the between-episodes content. Problem: "report" connotes routine bureaucratic filing — doesn't quite carry the mystery.

**"The Visitor Log"** — Direct tie to The Midnight Visitor Log. Familiar to existing audience. Problem: creates confusion — is this the show? the newsletter? the blog? For new subscribers, it's ambiguous.

**"Transmission from the Last Roadside Attraction"** — Most evocative. Contains the full mythology. Problem: too long for inbox display, will truncate in most clients.

---

### ✦ RECOMMENDED NAME: **The After-Closing Brief**

**Subtitle:** *Dispatches filed when the Last Roadside Attraction goes dark.*

**Reasoning:** "After-Closing" does three things simultaneously:

1. It tells you *when* — this is what gets filed after hours, after the episode, after the public-facing content is done. It is the insider version.
2. It implies *exclusivity* — the Attraction is closed. You're getting the briefing that only certain people receive.
3. It maintains the dossier/operational-document aesthetic that runs through all LDI content. A "Brief" is a formal document. It gets delivered. It matters.

The subtitle anchors it geographically and mythologically without overstating. "Goes dark" has dual meaning — the lights shut off at the Attraction, and the mysterious gets stranger in the dark.

**From-name:** `The After-Closing Brief · LDI`
**From-email:** `brief@lithium-dreams.com`
**Reply-to:** `hello@lithium-dreams.com`
**Web archive URL:** `newsletter.lithium-dreams.com`

> **[BOB ANNOTATION]:** *I wanted "Bob's Extremely Accurate Transmission" but apparently that's not a newsletter name. Fine. "The After-Closing Brief" is good. It sounds like something I'd get slid under a motel room door at 2am, which is exactly the energy we want. My one note: the subject lines better not be corporate garbage. I will personally haunt you if I see "Don't miss this week's episode!" in anyone's inbox. I have opinions about this. See Section 3.3.*

---

### Visual Identity

**Design Philosophy:** The newsletter should feel like receiving a physical document from the Attraction — not a marketing email, not a newsletter. When it opens, the reader should feel like they are unfolding something that was meant specifically for them.

**Background:** White background. (Rationale: Dark backgrounds display inconsistently across email clients. Gmail clips dark backgrounds. Outlook renders them unpredictably. A white-background newsletter with dark typography and classified-document styling delivers the aesthetic while remaining technically sound. Dark mode support can be added via `@media (prefers-color-scheme: dark)` CSS at the Beehiiv Scale tier.)

**Header Block:**
```
┌─────────────────────────────────────────────────────────────────────┐
│  ▓ THE AFTER-CLOSING BRIEF                                         │
│  LITHIUM DREAMS INDUSTRIES · IMAGINEERING DIVISION                 │
│  TRANSMISSION: [DATE] · ISSUE: [###] · CLEARANCE: GENERAL         │
│  "Filed after closing at the Last Roadside Attraction."            │
└─────────────────────────────────────────────────────────────────────┘
```

Render in email as: dark background header block (#1a1a1a or #111111), white text, monospace font (Courier New, monospace stack). The box-drawing characters can be approximated with a full-width dark block div and thin border.

**Typography:**
- **Body text:** Georgia, serif — readable, slightly literary, not corporate
- **Section headers / classification labels:** Courier New, monospace — dossier aesthetic
- **Data / links / callout boxes:** monospace, slightly smaller (0.9em)
- **Pull quotes / Warden's voice:** Georgia italic, slightly larger (1.1em)
- **Bob's sections:** Georgia regular, can use a light background box (#f5f5f0) to visually separate

**Color Palette:**
- Background: #ffffff
- Primary text: #1a1a1a
- Section header bars: #1a1a1a (dark fill) with white text
- Classification stamps: #cc0000 (red) for "INCIDENT" markers; #444444 for standard stamps
- Link color: #1a1a1a with underline (no blue links — they break the aesthetic)
- Subtle rule lines: #cccccc

**Classification Stamp (at top of each issue):**
```
TRANSMISSION · ISSUED [DATE] · CLEARANCE: GENERAL · ISSUE [###]
```
In email HTML: small-caps, monospace, #cc0000 or dark gray, centered or left-aligned below header block.

**Section Dividers:**
Use a simple horizontal rule styled as:
```
─────────────────────────────────────── ◈ ───────────────────────────────────────
```
Or in HTML: a thin 1px #cccccc `<hr>` with a centered ◈ character.

**Mobile rendering:** All section blocks should be single-column. Header block should scale to 100% width on mobile. Font sizes: body 16px minimum on mobile, headers 18px minimum.

---

### Subject Line Voice

Subject lines are not headlines. They are the knock on the door. They tell the reader what kind of transmission this is *before* they open it.

**The Five Subject Line Formats:**

| Format | Construction | Best for |
|---|---|---|
| `INCIDENT LOGGED:` | Classification prefix + brief | Episode drops, real-world events |
| `FIELD REPORT:` | Operational prefix + location/observation | Shorts content, between-episodes |
| `FROM THE WARDEN'S DESK:` | Authority prefix + contemplative fragment | Long-view issues, membership |
| `BOB HAS THOUGHTS:` | Character prefix + barely-contained theory | Bob's Corner, unverified histories |
| `SIGNAL DETECTED:` | Technical prefix + frequency/topic | Ghost-adjacent, lore drops |

**10 Example Subject Lines:**

```
1.  INCIDENT LOGGED: Something in Point Pleasant didn't leave in 1967

2.  FIELD REPORT: The truck stop on Route 50 that isn't on any map anymore

3.  BOB HAS THOUGHTS: Why the government definitely knows about the Cornfield Lights

4.  SIGNAL DETECTED at 3:17am: This week's case is still open

5.  FROM THE WARDEN'S DESK: On staying with a mystery that never resolves

6.  INCIDENT LOGGED: New episode — the thing in the water at Lake Lanier

7.  FIELD REPORT: A real wire service story that reads like we wrote it

8.  BOB HAS THOUGHTS: The Welcome Kit they didn't want you to have

9.  SIGNAL DETECTED: The archive has been updated. Start here.

10. FROM THE WARDEN'S DESK: The list has been open 90 days. Something to say about that.
```

**Subject line rules:**
- Never begin with "Episode" or a number
- Never use exclamation marks in the classification-style lines (they break the operational tone)
- Keep under 50 characters when possible (preview text carries the rest)
- Preview text complements — never repeats — the subject line
- Preview text format: plain voice, one sentence, in-world: *"The case file is attached. You'll want to read the last page first."*

> **[BOB ANNOTATION — ON SUBJECT LINES]:** *Okay so I've been in a lot of inboxes and I know what gets opened and what gets deleted without reading. "Don't miss Episode 12!" gets deleted. You know what gets opened? "INCIDENT LOGGED: The thing in the cornfield won't go on the record." That gets opened because now you NEED TO KNOW what the thing is. You don't say "here is content." You say "here is a transmission about something specific that happened." The inbox is a dark hallway. Your subject line is the light under the door. Make it look like something's on the other side. Because something is.*

---

## SECTION 4: CONTENT ARCHITECTURE — WHAT'S IN EACH ISSUE

### Issue Type A — Episode Drop Issue
*Weekly, triggered by new episode publication.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ISSUE TYPE A — EPISODE DROP                                                │
│  Trigger: New episode published to YouTube                                  │
│  Cadence: Weekly (when episode drops)                                       │
│  Estimated read time: 4–6 minutes                                           │
│  Auto-generated draft: YES (see Section 9 for Claude prompt)                │
└─────────────────────────────────────────────────────────────────────────────┘
```

**SECTION A1 — TRANSMISSION HEADER**
*3–4 sentences. Host voice, plain and direct. What happened this week at the Attraction. Not a summary — a mood setter.*

Format: Georgia body text, italic, inside a subtle border box. No header label needed — the reader knows where they are.

Example:
> *The log for this week came out of a four-hour drive to a place that doesn't get a lot of visitors anymore. Not because it's hard to find. Because people stopped looking. That's usually when it gets interesting.*

---

**SECTION A2 — THE CASE BRIEF**
*150–200 words. What the case is, why it matters, one detail that makes you have to watch.*

Format: Monospace header bar reading `CASE BRIEF — [EPISODE TITLE]`. Body in Georgia. End with one sentence in bold or small-caps that functions as the hook.

Example structure:
- Paragraph 1: What happened / the case
- Paragraph 2: The historical/factual context
- Bold closer: The one detail that doesn't fit, framed as an open question

---

**SECTION A3 — THE SIGNAL**
*All three format links. Clearly labeled. Not a wall of hyperlinks.*

Format: Monospace header bar reading `THE SIGNAL — FIND THE EPISODE`. Three clearly distinct link blocks:

```
▶  WATCH [Episode Title] on YouTube
    [Full URL — youtube.com/watch?v=...]
    Runtime: [XX min] · Published: [Date]

◎  LISTEN on the Podcast
    Available on Spotify · Apple Podcasts · Buzzsprout
    [Direct Buzzsprout link]

📂  READ THE DOSSIER
    Full case file at lithium-dreams.com
    [Direct episode dossier link]
```

Never embed a video in the email. Always link out. (Video embeds are blocked by most clients and trigger spam filters.)

---

**SECTION A4 — ONE MORE THING**
*One piece of research that didn't make the final cut. Exclusive to newsletter subscribers.*

Format: Header bar reading `ONE MORE THING — NOT IN THE EPISODE`. 100–150 words max. Can be a quote from a source, a detail that complicated the narrative, a dead end that's still interesting, a name that kept appearing.

This section creates genuine newsletter exclusivity. It is not a teaser. It is real content that only subscribers receive.

---

**SECTION A5 — BOB'S FORTUNE**
*This week's fortune. Different from the public website Fortune. Newsletter-exclusive.*

Format: A box (border: 1px solid #cccccc, background: #f9f9f7, padding: 16px). Center-aligned. Bob's Fortune stamp at top. The fortune below. Bob's sign-off at bottom.

```
╔══════════════════════════════════╗
║  BOB'S FORTUNE — ISSUE [###]    ║
║  (Not available at the website)  ║
╚══════════════════════════════════╝

"[Fortune text — one to three sentences, Bob voice.]"

— Bob, Resident Theorist, Lithium Dreams Industries
   Probably true. Legally uncertain. Emotionally accurate.
```

---

**SECTION A6 — FROM THE WARDEN**
*1–3 sentences. Contemplative. One per issue, always different. Long-view perspective on the episode theme.*

Format: Georgia italic, slight left-border indent (4px solid #cccccc, padding-left: 16px). Header: small monospace label `FROM THE WARDEN`.

Example:
> *The places that get abandoned don't disappear. They wait. Every case file in the log is an attempt to go back and look at something that's been waiting.*

---

**SECTION A7 — WHAT'S NEXT**
*Brief tease. 2–3 sentences maximum. No spoilers, but enough to make them want the next one.*

Format: Clean, plain. Monospace header `COMING NEXT`. Body Georgia.

Example:
> *Next week's case is in a state I've driven through twice without stopping. I should have stopped. More soon.*

---

**SECTION A8 — THE GIFT SHOP**
*One product. Written in Bob's voice. Not a sales pitch — an endorsement from a character who has very specific feelings about merchandise.*

Format: Header `FROM THE GIFT SHOP — BOB RECOMMENDS`. Product name, brief Bob description (50–75 words, Bob voice), one link.

Example:
> *Look. I don't tell people what to buy. But if you're the kind of person who reads a government document and then thinks "I should have this on a shirt," we made that shirt. The [Product Name]. Available at the Gift Shop. I own three. Two of them are mine.*

---

**SECTION A9 — FOOTER**

```
─────────────────────────────────────── ◈ ───────────────────────────────────────

You are receiving The After-Closing Brief because you registered at the Last
Roadside Attraction. Thank you for staying on the signal.

lithium-dreams.com  ·  @LithiumDreamsTV  ·  Podcast

Filed after closing at the Last Roadside Attraction.
"Keep the log open. I'll see you in the dark."

[Unsubscribe] · [Manage Preferences] · [View in Browser]

Lithium Dreams Industries · Filed from somewhere in the Midwest
```

---

### Issue Type B — Between-Episodes Issue
*Bi-weekly maintenance report. Keeps the list warm. No new episode needed.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ISSUE TYPE B — MAINTENANCE REPORT                                          │
│  Trigger: No new episode this week (or alternate-week send)                 │
│  Cadence: Bi-weekly on weeks without an episode drop                        │
│  Estimated read time: 3–4 minutes                                           │
│  Subject line format: FIELD REPORT or INCIDENT LOG UPDATE                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**SECTION B1 — THE INCIDENT LOG UPDATE**
*One new piece of Attraction lore. 100–150 words. First-person host voice.*

This is the world staying alive between episodes. The Warden found something in the basement. The arcade got a new cabinet that nobody remembers installing. Bob sent a voice memo at 2am. These are small, specific, and real-feeling — even when they're clearly invented. This section rewards long-term subscribers and makes the Attraction feel like a place that continues to exist when the camera is off.

Example:
> *The Warden reported this week that the fire door at the back of the Map Room — the one that's been painted shut since at least 2019 — is now ajar. We haven't gone in yet. The Warden says it can wait. Bob says it absolutely cannot wait. We're going to let them argue about it for a few more days.*

---

**SECTION B2 — FIELD NOTES**
*One real-world event treated in MVL voice. 150–200 words.*

Find one news story, wire report, or documented incident from the past two weeks that reads like it belongs in an MVL episode. Treat it in the show's voice: here's what happened, here's what we know, here's what nobody's explaining yet.

Format: Monospace header `FIELD NOTES — [DATE] · [LOCATION]`. Body Georgia. End with an open question in italics.

Rules:
- Must be real and sourced (link to the source)
- Must be genuinely strange or unexplained
- Do not editorialize into irresponsibility — the "we don't know" is the point
- Not political. Not tragic. Weird, specific, factual.

---

**SECTION B3 — THE ARCHIVE**
*Feature a past episode for new subscribers.*

Format: Header `FROM THE ARCHIVE — IF YOU'RE NEW, START HERE`. Episode title, 75-word description, three format links (same format as Section A3).

Rotate systematically — not random. EP01 first, then EP02, then forward. New subscribers get the archive introduced in order.

---

**SECTION B4 — BOB'S CORNER**
*Bob's Unverified Theory of the Week. Short (75–100 words), funny, possibly true.*

Format: Bob's Corner header, Georgia, slightly indented in a bordered box. Bob voice throughout. Must end with one sentence that sounds deranged but is technically plausible.

Example:
> *This week Bob would like to talk about why so many roadside attractions were built within a twelve-mile radius of former military testing ranges. Bob says this is not a coincidence. Bob has a map. The map has string. The string is color-coded. I'm not going to pretend I don't find it compelling.*

---

**SECTION B5 — GLASSHOUSE NOTE**
*One paragraph. Clean Glasshouse voice — not LDI voice.*

Format: Header `FROM GLASSHOUSE SYSTEMS STUDIO`. Background: very light gray (#f0f0f0) to visually separate from LDI content. Body Georgia, clean professional. 75–100 words.

This section does two things: it keeps the Glasshouse pipeline warm for LDI subscribers who might be business owners, and it demonstrates that LDI is a serious operation with a professional arm — not just a passion project. It should never oversell. One honest line about what Glasshouse is building, one link to /work.

Example:
> *At Glasshouse, we've been building an AI intake system for small creative studios — the same kind of system that runs behind The Midnight Visitor Log. If you run a small operation and want to see how that works in practice, the intake is open at lithium-dreams.com/work.*

---

**SECTION B6 — FOOTER**
*Same as Issue Type A footer.*

---

### Issue Type C — Membership Upgrade Issue
*Monthly. For free subscribers who haven't upgraded. Does not feel like a sales email.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ISSUE TYPE C — MEMBERSHIP INVITATION                                       │
│  Trigger: Monthly, auto-send to free subscribers only                       │
│  Cadence: Once per month (suppress if subscriber upgraded in last 30 days)  │
│  Goal: Conversion to paid tier — no hard sell                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

**SECTION C1 — A DOOR OPENED**
*In-world framing. 100–150 words. The host voice.*

Not "here's our paid tier." Instead: there are parts of the Attraction that aren't on the public map. This is the invitation to find out what's back there. The framing is curiosity, not transaction.

Example:
> *Most visitors to the Attraction see what we put out for them — the episodes, the dossiers, the map of the grounds. But the Attraction has other rooms. The ones we keep for the people who want to go further. Not because the public content isn't real. It is. But some cases don't fit in twenty-five minutes. Some Bob theories would get us both in trouble if we ran them publicly. Some things the Warden found, we're still not sure we should have found at all. If you want into those rooms, there's a door here.*

---

**SECTION C2 — WHAT'S BEHIND IT**
*Specific Patreon/paid tier benefits, framed in world. No bullet-list feature dumps.*

Format: Each benefit gets one sentence of in-world description. Not "access to extended dossiers" — "the full case files, including the sections that got pulled from the public version."

Example structure (3–5 benefits max):
> *Members get the full dossier — not the public version, the internal one. The sections with the sources we couldn't verify and the details the subject asked us not to include.*
>
> *Members get Bob's Fortune delivered privately, before it's filed anywhere else. The ones he sends at 3am. Those are different.*
>
> *Members get early access — the episode before it goes to YouTube. Useful if you want to watch it twice.*

---

**SECTION C3 — ONE EXCLUSIVE THING**
*A real sample of paid-tier content. Not a teaser — actual content.*

This is the most important section of Issue Type C. If you want someone to pay for more, show them a real piece of it. A paragraph from an extended dossier. One of the 3am Bob fortunes. A Ghost field note that didn't make the episode.

Format: Full content block, labeled `MEMBER EXCLUSIVE — PREVIEW`. After it: "This is what members receive."

---

**SECTION C4 — THE OPTION**
*Clear CTA. No urgency fake-out. No countdown timer.*

Format: Clean, simple, one link.

```
If you want to go further into the Attraction:
→ [Join as a Member — $5/month] [link to Beehiiv paid tier or Patreon]

No pressure. The free transmissions keep coming either way.
```

Footer: standard.

---

## SECTION 5: THE AUTOMATION SEQUENCES

### Welcome Sequence — Days 0, 2, 5, 10

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WELCOME SEQUENCE — TRIGGERED ON CONFIRMED SUBSCRIPTION                     │
│  Platform: Beehiiv (Scale tier) or ConvertKit                               │
│  Total emails: 4                                                            │
│  Suppression: Suppress if subscriber upgrades to paid tier                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

**DAY 0 — "You've arrived at the Last Roadside Attraction."**

*Subject:* `SIGNAL CONFIRMED: You're on the log.`
*Preview text:* `Your Visitor Welcome Kit is attached.`

Content:
- In-world orientation: Welcome to the Attraction. Here is what this place is. Here is what you'll receive and when.
- Deliver the **Visitor Welcome Kit** (PDF, auto-attached or linked from Beehiiv/ConvertKit delivery page)
- Brief paragraph on the show (The Midnight Visitor Log) — what it is, where to find it
- One sentence on the Pantheon: "You'll hear from Bob, Ghost, and the Warden. They each have a job here."
- Sign off: host voice, plain, warm. "The log is open. I'll see you in the dark."
- No links to products. No Patreon mention. Day 0 is purely welcome.

---

**DAY 2 — "This is where it starts."**

*Subject:* `INCIDENT LOGGED: The first case file is attached.`
*Preview text:* `EP01 — Mothman. We start here.`

Content:
- One-paragraph host note: "If you're going to understand the Attraction, start with Mothman. Not because it's the most unusual case. Because it's the one that explains why I started keeping the log."
- Three-format links to EP01 (YouTube, podcast, dossier) — same format as Section A3
- 50-word context note: what the Mothman case is, why it matters as an entry point
- Sign off: brief, in-world

---

**DAY 5 — "The Attraction has rooms."**

*Subject:* `FIELD REPORT: There's more to the grounds than the broadcasts.`
*Preview text:* `The Museum. The Fortune. The Arcade. The Garden.`

Content:
- Introduce the website world. Each section gets exactly one in-world sentence and a link.

```
THE MUSEUM AFTER CLOSING
Where the cases that didn't make the log live.
→ lithium-dreams.com/museum

THE FORTUNE MACHINE
Bob's ongoing oracle. Updated. Possibly dangerous.
→ lithium-dreams.com/fortune

THE ARCADE
The things we've built for visitors.
→ lithium-dreams.com/arcade

THE DEEP GARDEN
The lore section. Don't stay too long.
→ lithium-dreams.com/garden
```

- Close: "The map isn't complete. But this is the current survey."

---

**DAY 10 — "Bob has something to tell you."**

*Subject:* `BOB HAS THOUGHTS: (He asked me to send this.)`
*Preview text:* `He has been waiting.`

Content:
- Written entirely in Bob's voice — as if Bob hijacked the email sequence
- Bob introduction: who he is, what he does, why he's the most important person at the Attraction (his words)
- Bob's current active theory — something specific, real-feeling, mildly alarming
- Warm, funny, human — this is the email where the subscriber meets the most memorable character
- Soft Patreon/paid tier awareness: *"Also, there are things I can only tell members. Not because I'm being mysterious. Because some of this isn't ready for the public log. If you want to know what I know — and I know a lot — the door is at [link]. No pressure. I'll keep sending fortunes either way."*
- Not a sales pitch. A character introduction that happens to mention there's more inside.

---

### Win-Back Sequence — 60+ Days Inactive

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WIN-BACK SEQUENCE — TRIGGERED AT 60 DAYS NO OPEN                          │
│  Platform: Beehiiv automation or ConvertKit                                 │
│  Total emails: 3                                                            │
│  End state: Click = return to active segment / No click = unsubscribe       │
└─────────────────────────────────────────────────────────────────────────────┘
```

**EMAIL 1 — "The log shows you haven't checked in."**

*Subject:* `INCIDENT LOGGED: Your name is still on the log.`
*Preview text:* `No guilt. Just checking.`

Content:
- Simple, honest, no guilt. 150 words maximum.
- In-world: "The log shows you haven't opened a transmission in a while. That's fine. The Attraction doesn't close on anyone."
- One link: the most recent episode. "In case you missed it."
- No CTA to upgrade. No "you're about to be removed." Just a genuine check-in.

---

**EMAIL 2 — Field Note (genuine content drop) — 1 week after Email 1**

*Subject:* `FIELD REPORT: Something happened this week you should know about.`
*Preview text:* `Real event. Unverified explanation.`

Content:
- Drop a genuine Field Note — a real weird event, treated in MVL voice
- This email is a content email, not a re-engagement email. The goal is to remind them why they subscribed.
- 150–200 words of actual interesting content
- One link to a relevant dossier or episode
- No mention of unsubscribing

---

**EMAIL 3 — Clean close — 2 weeks after Email 2**

*Subject:* `SIGNAL CHECK: One click to stay on the log.`
*Preview text:* `If you want to keep receiving transmissions, this is the button.`

Content:
- Honest and direct. 100 words maximum.
- "If the transmissions aren't for you anymore, that's fine. Click here to stay on the signal. If not, we'll close your file."
- **One prominent button: "STAY ON THE LOG"** — this click re-activates them
- "If you don't click, you'll be removed from the list in 7 days. No hard feelings. The log stays open."
- **Auto-unsubscribe on no click within 7 days** — this is non-negotiable for list hygiene

> **[GHOST ANNOTATION — ON LIST HYGIENE]:** *A clean list is not a vanity metric. It is the mechanism by which your future emails reach people's inboxes instead of the spam folder. Gmail and Outlook use engagement signals — open rates, click rates, not-spam reports — to decide where email lands. A list full of non-openers does not sit quietly in the background. It actively damages deliverability for everyone on the list, including your most engaged subscribers. Unsubscribing a dead contact is not a loss. Keeping a dead contact is. Run win-back sequences religiously. Purge the non-responders. Never buy lists. Never add anyone who didn't explicitly opt in. The signal is only as clean as the infrastructure carrying it.*

---

## SECTION 6: LIST-BUILDING STRATEGY

### The Visitor Welcome Kit — Lead Magnet

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DOCUMENT: ORIENTATION PACKET                                               │
│  SUBTITLE: For New Visitors to the Last Roadside Attraction                │
│  FORMAT: PDF, 6–8 pages, full dossier aesthetic                            │
│  DELIVERY: Automated, immediate on confirmed subscription                   │
│  FILE: visitor-welcome-kit.pdf                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Contents (page by page):**

**Page 1 — Cover**
Full-bleed dossier cover. Classification header at top. Title: `ORIENTATION PACKET — VISITOR CLEARANCE GRANTED`. Subhead: "For New Visitors to the Last Roadside Attraction." LDI logo. Date field (auto-populated or static). CLASSIFICATION: GENERAL VISITOR.

**Page 2 — Map of the Attraction**
ASCII/illustrated map of the Attraction grounds — Museum After Closing, The Arcade, The Deep Garden, The Fortune Machine, The Broadcast Tower (where the show comes from), The Gift Shop, The Back Rooms (redacted). Hand-drawn or ASCII art — NOT a clean digital map. It should look like it was typed on a typewriter and photocopied twice.

**Page 3 — Meet the Pantheon**
Three character cards. Each: name, element association, function at the Attraction, one quote, visual indicator (icon or simple portrait in dossier style).
- BOB: Fire / Chaos — *"Chief Theorist, Unverified Histories Division"*
- GHOST: Signal / Precision — *"Operations, Transmission Quality, List Hygiene"*
- WARDEN: Earth / Patience — *"Long Game, Institutional Memory, Grounds Maintenance"*

**Page 4 — What Is The Midnight Visitor Log**
One-page description of the show — what it is, what it isn't, where to find it (YouTube, podcast, dossier). In host voice. Plain and direct. Three format links.

**Page 5 — Your First Case File: EP01 Mothman**
A condensed version of the Mothman dossier — 400–500 words, dossier format, header/footer with classification marks. "This is where the log starts. Start here."

**Page 6 — Bob's Fortune for New Arrivals (Special Edition)**
A full-page fortune, formatted like the website Fortune Machine output, but labeled SPECIAL EDITION — NEW VISITOR CLEARANCE. In Bob's voice. Something optimistic and strange.

**Page 7 — House Rules of the Attraction**
Short-form list, monospace font, numbered. Example rules:
```
1. The log stays open.
2. "Probably" is not the same as "definitely." Bob disagrees.
3. If something doesn't fit, that's why it's interesting.
4. The Warden is always right about the long game.
5. If Bob gives you a theory, write it down. Sometimes he's right.
6. You can leave whenever you want. The Attraction will still be here.
7. Keep the log open. We'll see you in the dark.
```

**Page 8 — Footer / Sign-Off**
Host sign-off in plain voice. Contact info. `lithium-dreams.com`. Social links. `Filed after closing at the Last Roadside Attraction.`

**Production:** Build in Canva (dossier template), Adobe InDesign, or — to stay fully in the LDI AI stack — generate the layout via a structured HTML-to-PDF pipeline using wkhtmltopdf or Puppeteer. Export as PDF. Host on lithium-dreams.com/welcome-kit (gated via Beehiiv/ConvertKit delivery URL, not public-facing).

---

### Sign-Up Placement Strategy

**On lithium-dreams.com:**

| Placement | In-World Copy | Priority |
|---|---|---|
| `/attraction` — after district directory | `"Register your visit. Transmissions go out after closing."` + form | HIGH |
| `/broadcasts/[episode-slug]` — after dossier content | `"The full file includes sections not in the public dossier. Register for the Brief."` + form | HIGHEST (highest intent) |
| `/museum` | `"Request access to field archives. Filed after closing."` + form | HIGH |
| Pop-up (60-second delay) | `"A transmission is waiting for you. Enter your address."` + form | MEDIUM |
| Footer (every page) | `"Stay on the signal. The After-Closing Brief goes out weekly."` | BASELINE |
| 404 page | `"You found the wrong room. The right one is here."` + sign-up link | LOW / BONUS |

**Pop-up technical notes:** 60-second delay (not immediate — visitor should have context before seeing the request). Single-field form (email only — no name required at sign-up; collect name on confirmation page if desired). Dismiss = do not show again for 30 days (cookie). Mobile: full-screen overlay, not a corner widget.

---

**On YouTube:**

| Placement | Copy / Action |
|---|---|
| End screen | Card: "Get the After-Closing Brief — link in description" |
| Pinned comment | `"The dossier and the newsletter are at lithium-dreams.com. Full file, plus stuff that didn't make the episode."` |
| Episode description | Line 1 after episode summary: `Get the After-Closing Brief: [link]` |
| Community tab | Monthly post: in-world copy, sign-up link, one exclusive that's in the current issue |

**On Podcast:**

| Placement | Copy |
|---|---|
| Show notes | First link in show notes, every episode: `Get the After-Closing Brief + Visitor Welcome Kit: [link]` |
| Verbal outro CTA | *"If you want the full case file — the sections that didn't make the episode — the After-Closing Brief goes out weekly. The link is in the show notes. The Visitor Welcome Kit is free."* |

---

**Cross-Platform Capture:**

- **Instagram bio:** Single link → lithium-dreams.com/welcome (sign-up landing page). Bio copy: `"Get the Visitor Welcome Kit. Link below."`
- **Reddit:** Post sign-off (in relevant subreddits — r/UFOs, r/theXfiles, r/mildlyinteresting, r/creepy): `"Full file at lithium-dreams.com"` — passive, not promotional
- **TikTok/Reels (if applicable):** Comment link, profile link — same landing page

> **[WARDEN ANNOTATION — ON LIST BUILDING]:** *The number that matters is not total subscribers. It is engaged subscribers. Chasing sign-ups with aggressive pop-ups and paid lead campaigns produces a list that looks large and performs poorly. Build the list by giving people something real — the Welcome Kit is real. Put the capture where people are already engaged — after the episode dossier is the right moment. A visitor who has just read your case file and clicks sign-up is a completely different subscriber than one who was interrupted by a pop-up on the homepage. They will open your emails at three times the rate. Optimize for the right subscriber, not the highest subscriber count.*

---

## SECTION 7: GLASSHOUSE NEWSLETTER (SEPARATE STREAM)

### Name: **The Glasshouse Brief**

*Alternative considered: "Morning Light." Decision: "The Glasshouse Brief" is better. It maintains the brand name, it matches "The After-Closing Brief" structurally (both are "The [Name] Brief"), and it signals professionalism to a business audience. "Morning Light" is softer but has no brand anchor — it could be anyone's wellness newsletter. "The Glasshouse Brief" is specific.*

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  THE GLASSHOUSE BRIEF                                                       │
│  Issued by Glasshouse Systems Studio · lithium-dreams.com/work             │
│  Cadence: Bi-weekly (every other week, Tuesday delivery)                   │
│  Target length: 300–400 words. Reads in 2 minutes.                        │
│  Audience: Business owners, operators, AI-curious professionals            │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Audience:** Business owners and operators who found `/work` and want practical AI and systems thinking without the Attraction lore. They are busy. They read in the morning. They want one actionable thing and they want it quickly.

**Tone:** Clean, clear, warm professional. The Glasshouse aesthetic — frosted glass, architectural daylight, measured optimism. Not corporate. Not cold. Not the dark LDI voice. Think: a thoughtful colleague sending you something genuinely useful, not a newsletter trying to become a media company.

**Visual Identity:** Separate from LDI entirely. White background, clean sans-serif (system stack: -apple-system, BlinkMacSystemFont, Segoe UI), generous whitespace. Header: Glasshouse Systems Studio wordmark, light gray (#f5f5f5) background bar, clean type. No box-drawing characters. No classification stamps. Daylight.

**From-name:** `The Glasshouse Brief`
**From-email:** `brief@glasshouse.lithium-dreams.com` or `work@lithium-dreams.com`

---

**Content Structure — Each Issue:**

| Section | Content | Length |
|---|---|---|
| **THE INSIGHT** | One practical AI/workflow concept, explained clearly | 150–200 words |
| **FROM THE FIELD** | One case study excerpt or client result (anonymized if needed) | 75–100 words |
| **ONE TOOL / RESOURCE** | One tool, template, or resource recommendation, with honest assessment | 50–75 words |
| **THE BRIEF LINE** | One sentence summary of the issue — the thing to remember | 1 sentence |

Total: 300–400 words. No fluff. No "this week I've been thinking about..." opener. Start with the insight.

---

**How They Intersect:**

The Glasshouse Brief occasionally (once per quarter) mentions the Attraction as the creative proof of concept — *"The system that runs The Midnight Visitor Log is the same system we deploy for clients. Here's how it works."* This gives the Brief a genuine case study and bridges the two worlds without muddying either.

The LDI After-Closing Brief (Issue Type B, Section B5) carries the Glasshouse Note — one paragraph, professional voice, for LDI subscribers who are also business operators. Some percentage of the Attraction audience has a business and needs what Glasshouse offers. The Note surfaces that without being intrusive.

The lists are **never combined**. They are separate lists, separate sends, separate analytics, separate from-addresses. A subscriber on one list is not automatically added to the other. Cross-pollination is via editorial mention and explicit opt-in only.

---

**Sign-Up Placement:**

| Placement | Copy |
|---|---|
| `/work` (main page) | `"The Glasshouse Brief — practical AI and systems thinking, bi-weekly."` + form |
| `/work/intake` confirmation page | `"While you wait for your intake review, get the Brief."` + opt-in checkbox |
| `/work/case-files` | `"Get the full methodology in the Brief."` + form |

**Cadence note:** Bi-weekly is intentional. These readers are busy. Over-sending to a professional list is the fastest way to get unsubscribes. One excellent, short email every two weeks outperforms four mediocre ones.

---

## SECTION 8: MONETIZATION VIA NEWSLETTER

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  REVENUE MODEL — NEWSLETTER DIRECT MONETIZATION                             │
│  The newsletter is not just audience infrastructure. It is a revenue        │
│  channel with three distinct mechanisms.                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Mechanism 1: Sponsored Placements

**Who buys newsletter sponsorships?** For LDI: paranormal-adjacent brands (candles, field gear, indie book publishers), horror/mystery media properties, regional tourism boards (unusual attractions), weird history publications, small-batch products with countercultural audiences.

**Placement:** Issue Type A (Episode Drop issues) only. One sponsor per issue. Placed in the GIFT SHOP section or a clearly labeled `SPONSORED TRANSMISSION` section between WHAT'S NEXT and the footer.

**Format:** 75–100 words, written by LDI in Bob's voice (with sponsor approval). Not a banner. A paragraph. This maintains the aesthetic and outperforms display ads.

**CPM benchmarks:** Email sponsorships typically run $20–$40 CPM (cost per 1,000 sends). LDI's niche audience commands the high end.

```
Revenue Projection Table — Sponsored Placements

Subscribers  |  CPM $30  |  Issues/mo  |  Monthly Revenue
─────────────┼───────────┼─────────────┼─────────────────
500          |  $15/send |  4          |  $60
1,000        |  $30/send |  4          |  $120
2,000        |  $60/send |  4          |  $240
5,000        |  $150/send|  4          |  $600
10,000       |  $300/send|  4          |  $1,200

Note: These assume 100% sponsored fill rate. Realistic launch rate: 25–50%.
Actual revenue at 2,000 subscribers with 50% fill: ~$120/mo from sponsorships.
```

**Sponsorship process:** Direct outreach via `work@lithium-dreams.com` → intake form at `/work` → rate card sent → Glasshouse manages the contract → LDI writes the copy.

---

### Mechanism 2: Paid Newsletter Tier (via Beehiiv)

**Free tier includes:** Issue Type A (Episode Drop) + Issue Type B (Between-Episodes)
**Paid tier ($5/mo) includes:**
- Issue Type A with **extended dossier section** (200–300 words of additional case material not in the public dossier)
- **Exclusive Bob Fortune** — the 3am fortunes, not the public ones
- **Early episode access** — 24–48 hours before YouTube publication
- Issue Type B with **Warden's extended field notes** (longer contemplative section)
- Issue Type C (membership upgrade issue) suppressed — they're already paid

**Why $5/mo:** It is psychologically frictionless. Less than a streaming service. Less than a coffee. The marginal cost to LDI of producing the paid-tier additions is low (the extended dossier content exists — it just doesn't go to public). The conversion rate at $5 is meaningfully higher than at $8 or $10.

**This is an alternative to Patreon** for people who prefer email to Discord. Some audience segments do not want community. They want the content, delivered to their inbox. This serves them.

```
Revenue Projection Table — Paid Newsletter Tier

Total Free Subs  |  Conversion %  |  Paid Subs  |  Monthly Revenue
─────────────────┼────────────────┼─────────────┼─────────────────
500              |  2%            |  10         |  $50
1,000            |  3%            |  30         |  $150
2,500            |  3%            |  75         |  $375
5,000            |  4%            |  200        |  $1,000
10,000           |  4%            |  400        |  $2,000

Industry average paid conversion for niche content newsletters: 2–5%.
Combined with Beehiiv Scale ($42/mo), break-even at ~9 paid subscribers.
```

---

### Mechanism 3: Digital Product Upsells

**Via The After-Closing Brief:**

| Product | Price | Description | Delivery |
|---|---|---|---|
| Visitor Welcome Kit | FREE (lead magnet) | See Section 6 | Automated on subscribe |
| Extended Visitor Dossier | $5 | Full 20-page expanded version of Welcome Kit — more cases, full Pantheon lore, complete House Rules | Beehiiv/Gumroad link in newsletter |
| Bob Fortune Archive PDF | $8 | 100+ Bob Fortunes, compiled, formatted as a reference document, Bob's intro notes | Gumroad, linked from Newsletter and Gift Shop |
| Case File Print Bundle | $15–25 | Physical print-quality dossier pages for select cases | Printful/on-demand, linked from Gift Shop section |

**Via The Glasshouse Brief:**

| Product | Price | Description |
|---|---|---|
| AI Intake System Template (Notion) | $25 | The intake/workflow template used to run LDI operations |
| Production Stack Setup Guide | $47 | Full documentation of the LDI AI stack — Hermes, Claude, Ollama, ffmpeg, Buffer, Buzzsprout |
| Glasshouse Systems Consultation | $200/hr | Via `/work/intake` — full Glasshouse service offering |

---

### Combined Revenue Model — Realistic 12-Month Projection

```
Assumptions: Launch at Month 1 with 0 subscribers.
Growth: 150–200 new subscribers/month (organic, no paid ads).
By Month 12: ~1,800–2,000 subscribers.

Month 12 Revenue Mix:
──────────────────────────────────────────────────
Sponsorships (50% fill, 4 episodes/mo, 2,000 subs)    $120/mo
Paid newsletter tier (3% of 2,000 = 60 paid subs)     $300/mo
Digital product sales (estimated 10 sales/mo avg)     $75/mo
Glasshouse leads generated (1–2 clients/mo)           $200–400/mo
──────────────────────────────────────────────────
Total newsletter-attributable revenue (Month 12):     ~$695–$895/mo
Operating cost offset:                                Full ($55–70/mo stack)
──────────────────────────────────────────────────
Net contribution at 2,000 subscribers:               ~$625–$840/mo
```

This is conservative. It does not include YouTube monetization, Patreon, or merchandise. It demonstrates that the newsletter alone, at a realistic list size, covers operating costs and generates meaningful supplemental revenue.

---

## SECTION 9: THE AUTOMATION STACK

### Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AUTOMATION FLOW — COMPLETE                                                 │
│  Core stack: Hermes · Claude API · Beehiiv API · Buffer API · Buzzsprout   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Episode Publication → Issue Type A Flow:**

```
T-0:  Episode uploaded to YouTube (scheduled publish)
T+0:  Buffer publishes social posts (pre-scheduled)
T+0:  Hermes detects YouTube publish event (via YouTube Data API webhook or 
      polling every 15 min)
T+0:  Hermes retrieves: episode script, dossier text, episode metadata
      (title, description, runtime, YouTube URL, Buzzsprout URL)
T+0:  Hermes sends structured data to Claude API with Issue Type A prompt 
      (see below)
T+5min: Claude API returns draft Issue Type A email
T+5min: Hermes creates draft in Beehiiv via API (status: draft, not published)
T+5min: Notification sent to human reviewer (email or Slack/Discord webhook)
T+2hr: Human reviews, edits, approves, publishes in Beehiiv dashboard
      — OR — if auto-send is enabled: Beehiiv sends at T+2hr automatically
```

**Rationale for T+2hr:** YouTube send traffic peaks in the first two hours after publication. Sending the newsletter during that peak competes with the YouTube notification, potentially splitting attention. Sending at T+2hr catches subscribers who missed the YouTube notification but haven't given up on checking their email for the day.

---

**Subscriber Lifecycle Automation:**

```
New confirmed subscription
  → Welcome Sequence triggers immediately (Day 0 email sends within 5 minutes)
  → Day 2, Day 5, Day 10 emails scheduled

Subscriber upgrades to paid tier
  → Welcome Sequence suppressed (remaining unsent)
  → Paid Tier Welcome email triggers (new sequence, not detailed here)
  → Removed from Issue Type C audience segment

Subscriber inactive for 60 days (no opens)
  → Win-Back Email 1 sends
  → 7 days later: Win-Back Email 2 sends
  → 14 days later: Win-Back Email 3 sends with "click to stay" link
  → 7 days after Email 3: auto-unsubscribe if no click

Glasshouse intake form submitted with "add me to the Brief" opt-in
  → Subscriber added to Glasshouse Brief list only
  → Standard Glasshouse Brief welcome email sends
  → NOT added to LDI After-Closing Brief list
```

---

**Issue Type B Scheduling:**

Issue Type B (Between-Episodes) does not require automation to generate — it is human-authored. It should be drafted in batches (write 4 issues at once during a production day, schedule in Beehiiv). The Field Notes section requires weekly research (30 minutes), but the rest of the content can be templated and batched.

---

### Claude API Prompt — Issue Type A Auto-Draft

The following prompt is designed to generate a first-draft Issue Type A email from episode materials. It produces a human-reviewable draft that requires ~15 minutes of editing, not a full write from scratch.

```
─────────────────────────────────────────────────────────────────────────────
SYSTEM PROMPT:
─────────────────────────────────────────────────────────────────────────────

You are the Imagineering AI for Lithium Dreams Industries, assisting with 
production of The After-Closing Brief — the official newsletter of The 
Midnight Visitor Log. 

Your task is to draft Issue Type A (Episode Drop Issue) of the newsletter 
using the provided episode materials.

BRAND VOICE GUIDELINES:
- Host voice: 45-year-old Midwestern man. Plain speech. Facts-first. 
  Mystery-honoring. "I WANT TO BELIEVE" sincerity. Joe Bob Briggs energy — 
  direct, specific, never condescending.
- Bob voice: Chaotic, funny, confident, possibly accurate. Fire energy. 
  His Fortune must end with something that sounds wrong but could be right.
- Ghost voice: Precise, minimal. Signal metaphors. Clean.
- Warden voice: Slow, patient, long-view. Earth. One to three sentences only.
- NEVER use: "deep dive," "don't miss," "game changer," "exciting," 
  "amazing," exclamation marks in classification headers.
- ALWAYS use: plain words, specific details, in-world framing.

NEWSLETTER IDENTITY:
- Name: The After-Closing Brief
- Tagline: Dispatches filed when the Last Roadside Attraction goes dark.
- Sign-off: "Keep the log open. I'll see you in the dark."
- Footer line: "Filed after closing at the Last Roadside Attraction."

─────────────────────────────────────────────────────────────────────────────
USER PROMPT TEMPLATE (fill in brackets before sending):
─────────────────────────────────────────────────────────────────────────────

Draft Issue Type A of The After-Closing Brief using the following materials.

EPISODE METADATA:
- Episode title: [TITLE]
- Episode number: [EP##]
- Runtime: [XX min]
- YouTube URL: [URL]
- Podcast URL (Buzzsprout): [URL]
- Dossier URL: [URL]
- Issue number: [###]
- Send date: [DATE]

EPISODE SCRIPT EXCERPT (key sections — paste the intro, the main case 
summary, and the closing):
[PASTE 500–1000 words of script here]

DOSSIER CONTENT SUMMARY (paste the case overview section from the dossier):
[PASTE 200–400 words here]

ONE RESEARCH DETAIL NOT IN THE EPISODE (something from your research that 
got cut — for the ONE MORE THING section):
[PASTE 1–3 sentences of the cut detail]

PRODUCT FOR GIFT SHOP SECTION:
[Product name, brief description, URL]

NEXT EPISODE TEASE (one or two vague sentences about the next case):
[PASTE TEASE]

─────────────────────────────────────────────────────────────────────────────
OUTPUT FORMAT INSTRUCTIONS:
─────────────────────────────────────────────────────────────────────────────

Generate the complete Issue Type A draft with all nine sections in order:

1. TRANSMISSION HEADER (3–4 sentences, host voice, in-world mood setter)
2. CASE BRIEF (150–200 words, dossier format, ends with bold hook line)
3. THE SIGNAL (three format links block — use provided URLs)
4. ONE MORE THING (the cut research detail, 100–150 words, exclusive framing)
5. BOB'S FORTUNE (new fortune, Bob voice, ends with "Probably true. Legally 
   uncertain. Emotionally accurate." — do not reuse any previous fortune)
6. FROM THE WARDEN (1–3 sentences, contemplative, about the episode theme)
7. WHAT'S NEXT (2–3 sentences, teasing the next case without spoiling)
8. THE GIFT SHOP (75–100 words, Bob voice, the provided product)
9. FOOTER (standard — use the provided footer template)

Label each section clearly. Flag anything you are uncertain about with 
[REVIEW: note]. Do not invent facts about the case — if the script doesn't 
include something, leave it blank rather than fabricating.

─────────────────────────────────────────────────────────────────────────────
```

**Human review checklist before send:**
- [ ] Section A1 (TRANSMISSION HEADER): Host voice sounds right, not generic
- [ ] Section A2 (CASE BRIEF): Facts are accurate to the episode
- [ ] Section A3 (THE SIGNAL): All three URLs are live and correct
- [ ] Section A4 (ONE MORE THING): Detail is genuinely cut from episode (not in the dossier)
- [ ] Section A5 (BOB'S FORTUNE): Fortune is new, not a repeat
- [ ] Section A6 (WARDEN): Sounds like Warden, not generic inspirational content
- [ ] Section A7 (WHAT'S NEXT): Tease is accurate to the actual next episode
- [ ] Section A8 (GIFT SHOP): Product link is live, Bob voice is on
- [ ] Subject line and preview text: Written by human, not AI (AI drafts get formulaic)
- [ ] Send time: Set for T+2hr from YouTube publication

> **[GHOST ANNOTATION — ON AUTOMATION AND DELIVERABILITY]:** *The automation stack is only as reliable as its maintenance. Monitor deliverability monthly: sender reputation score, spam complaint rate (keep under 0.08%), bounce rate (hard bounces removed immediately, soft bounce threshold: 3 attempts before suppression), unsubscribe rate (above 0.5% per send is a content signal, not a list problem). The Claude API generates drafts — it does not generate sends. Every Issue Type A goes through human review before it reaches an inbox. The automation reduces production labor. It does not remove human judgment from the chain. A single bad send to a cold list can damage domain reputation for weeks. The signal must be clean before it goes out.*

---

## APPENDIX A: PLATFORM SETUP CHECKLIST

*To be completed before first send.*

```
BEEHIIV SETUP
─────────────────────────────────────────────────────────────────────────
[ ] Create Beehiiv account (free tier to start)
[ ] Set publication name: "The After-Closing Brief"
[ ] Configure custom domain: newsletter.lithium-dreams.com
[ ] Configure sending domain: brief@lithium-dreams.com
    → Requires DNS records: SPF, DKIM, DMARC at Cloudflare
[ ] SPF record: v=spf1 include:beehiiv.com ~all
[ ] DKIM: follow Beehiiv domain authentication docs
[ ] DMARC: v=DMARC1; p=quarantine; rua=mailto:dmarc@lithium-dreams.com
[ ] Design newsletter template (dark header, Georgia body, monospace labels)
[ ] Upload LDI logo (dossier header version)
[ ] Set up Welcome Sequence (4 emails, Day 0/2/5/10)
[ ] Set up Win-Back Sequence (3 emails, trigger: 60 days no open)
[ ] Configure paid newsletter tier ($5/mo) — Beehiiv Scale required
[ ] Set up referral program ("Refer 3 → Extended Visitor Dossier")
[ ] Set up Beehiiv API key (for Hermes integration)
[ ] Test send to internal addresses (check rendering in Gmail, Outlook, Apple Mail)

DNS / DELIVERABILITY
─────────────────────────────────────────────────────────────────────────
[ ] SPF record configured at Cloudflare for lithium-dreams.com
[ ] DKIM keys published
[ ] DMARC policy active
[ ] MX records intact (lithium-dreams.com receives email)
[ ] Warm up sending domain: start at 50 sends/day, double weekly for 4 weeks

LEAD MAGNET
─────────────────────────────────────────────────────────────────────────
[ ] Visitor Welcome Kit PDF completed (8 pages)
[ ] Hosted at lithium-dreams.com/welcome-kit (Cloudflare redirect or direct)
[ ] Beehiiv delivery automation: confirm → deliver PDF link
[ ] PDF tested on mobile (font sizes legible, no overflow)

LANDING PAGE
─────────────────────────────────────────────────────────────────────────
[ ] Sign-up landing page at lithium-dreams.com/brief
[ ] In-world copy: "Register your visit. The After-Closing Brief goes out 
    after the Attraction closes."
[ ] Single field: email (no name required)
[ ] Confirmation page: "Transmission received. Check your email for the 
    Visitor Welcome Kit."
[ ] Thank-you page distinct from homepage (for analytics conversion tracking)

GLASSHOUSE BRIEF (SEPARATE)
─────────────────────────────────────────────────────────────────────────
[ ] Separate Beehiiv publication OR separate Kit account
[ ] From: brief@glasshouse.lithium-dreams.com
[ ] Custom domain: brief.lithium-dreams.com/work
[ ] Template: clean, white, sans-serif — no LDI dossier elements
[ ] Sign-up placement: /work, /work/intake confirmation, /work/case-files
[ ] First 4 issues written and scheduled before launch
```

---

## APPENDIX B: QUICK-REFERENCE — ISSUE TYPE SUMMARY

| Issue Type | Trigger | Cadence | Length | Auto-drafted? |
|---|---|---|---|---|
| A — Episode Drop | New episode on YouTube | Weekly (when episode drops) | 6–8 min read | YES (Claude API) |
| B — Maintenance Report | Calendar / no episode week | Bi-weekly | 3–4 min read | NO (human, batch) |
| C — Membership Invite | Monthly calendar | Monthly | 3–4 min read | NO (template) |
| Welcome Seq. — Day 0 | New subscription confirmed | Immediate | 2–3 min read | NO (template) |
| Welcome Seq. — Day 2 | Day 2 after confirmation | Automated | 2 min read | NO (template) |
| Welcome Seq. — Day 5 | Day 5 after confirmation | Automated | 2 min read | NO (template) |
| Welcome Seq. — Day 10 | Day 10 after confirmation | Automated | 3 min read | NO (template) |
| Win-Back — Email 1 | 60 days no open | Automated | 1 min read | NO (template) |
| Win-Back — Email 2 | Day 67 no open | Automated | 2 min read | NO (template) |
| Win-Back — Email 3 | Day 81 no open | Automated | 1 min read | NO (template) |
| Glasshouse Brief | Calendar (bi-weekly) | Every 2 weeks | 2 min read | NO (human) |

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  END OF DOCUMENT — MN-0003                                                  ║
║  CLASSIFICATION: INTERNAL OPERATIONS                                        ║
║  FILED: 2026-06-27                                                           ║
║  REVISION STATUS: INITIAL — OPERATIONAL                                     ║
║  NEXT REVIEW: At 1,000 subscribers or 90 days post-launch                  ║
║                                                                              ║
║  "Keep the log open. I'll see you in the dark."                             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```
