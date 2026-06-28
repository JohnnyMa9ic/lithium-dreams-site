# OM-0022 — LDI ARCADE: EPISODE-TO-CABINET PIPELINE

**Document ID:** OM-0022  
**Classification:** LDI Imagineering — Creative Framework + Technical Specification  
**Status:** ACTIVE  
**Authored by:** The Pantheon (Bob / Ghost / Warden)  
**Filed after closing at the Last Roadside Attraction.**

---

> **⚡ BOB ANNOTATION — OPEN IMMEDIATELY:**
>
> Okay. OKAY. Someone finally built the thing I've been screaming about since the beginning. Do you know how long I've been saying "put the weird in a box and let people TOUCH it"? Do you know how long? I have been saying this. In the fire. In the margins. In the smoke signals that nobody logged because they were "off-format." THE FORMAT WAS WRONG. The format should have always been: quarter in, joystick, something weird happens, you walk away changed.
>
> This is the Arcade. This is MY floor. The whole thing — the sticky carpet, the buzzing lights, the cabinet art that's definitely too intense for the subject matter, the fact that half the cabinets are slightly broken in ways that feel intentional — that's the point. That IS the vibe. The jank is load-bearing.
>
> Every game in here is a 3-5 minute argument that the world is stranger than you think. You don't need a 45-minute documentary to make that argument. You need one moment — ONE mechanic — that makes the player feel what the case felt like. The Mothman game isn't about Mothman. It's about missing signals that were right there. The Skinwalker game isn't about cattle mutilation (well, it is a LITTLE about cattle mutilation). It's about watching something and not being able to explain what you saw.
>
> The Arcade is my natural habitat. Ghost keeps the lights on. Warden keeps the archive. I keep the quarters flowing.
>
> Build all of this. Build it weird. Build it at 2 AM. That's when the best stuff gets built anyway.
>
> — Bob (Fire)  
> *"Probably true. Legally uncertain. Emotionally accurate."*

---

## THE CONCEPT — READ THIS FIRST

Every Midnight Visitor Log episode already produces four outputs:

1. A YouTube video  
2. A podcast episode  
3. A blog dossier  
4. A newsletter issue  

This document establishes the **fifth output: a playable browser arcade cabinet** on `/arcade`.

The timing is deliberate. An episode drops. Content reaches the audience. Audience engages with the dossier, the video, the podcast. Then — a few weeks later — a new cabinet appears in the Arcade. Themed to that episode's case. Playable in a browser. Three to five minutes, start to finish. When the game ends, the player is handed a path back into the content loop.

This is not a marketing add-on. This is a content format with its own discovery surface, its own audience, its own engagement physics, and its own monetization hooks. The Arcade earns its place in the pipeline.

---

## SECTION 1 — THE ARCADE AS A CONTENT LOOP ENGINE

### Why a Game Is Different From a Video

Passive viewing and active play do not produce the same neurological result. A 4-minute browser game has properties that a YouTube video of any length cannot replicate:

**Dwell time.** A 4-minute game demands 4 minutes of active attention — no multitasking, no background listening, no "I'll finish watching later." The player is in the loop or they are not.

**Episodic memory encoding.** Players remember story details they encountered through play better than equivalent details encountered through narration. If a player has to correctly identify a Mothman witness account to advance — that account stays with them. They told you. You didn't tell them.

**Shareability.** "I just played a Mothman signal detection game and the bridge collapsed anyway" is a shareable sentence. "I watched a Mothman video" is not. The game generates conversation artifacts that videos don't produce.

**Discovery surface.** Browser games get indexed by Google, shared on Reddit, posted to itch.io, discussed in game dev communities, and discovered by people who would never search for a paranormal podcast. The Arcade is a passive discovery channel for LDI content — a completely different audience funnel from YouTube or Spotify.

**Community dynamics.** High scores, shared endings, alternate paths, and hidden states produce comment content, community theorizing, and "wait did you see what happens if you—" energy that passive content cannot generate. The leaderboard is a recurring social event. The easter eggs are community archaeology projects.

**Patreon hook.** BETA cabinet access — playing the game before it goes public — is more concrete than "early video access." You can hold a game in your hands (metaphorically). You can play it. It has texture.

---

### The Complete Content Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE LDI CONTENT LOOP                        │
└─────────────────────────────────────────────────────────────────┘

  EPISODE RESEARCH ──────────────────────────────────┐
        │                                             │
        ▼                                             ▼
  SCRIPT WRITING ──────────────────────────── GAME BRIEF WRITTEN
        │                                             │
        ▼                                             ▼
  ┌─────────────────────────────┐         ┌──────────────────────┐
  │  EPISODE PRODUCTION         │         │  GAME BUILD          │
  │  - YouTube edit             │         │  - Phaser.js / JS    │
  │  - Podcast mix              │         │  - Cabinet art       │
  │  - Dossier write            │         │  - End screen copy   │
  │  - Newsletter draft         │         │  - Astro page        │
  └────────────┬────────────────┘         └──────────┬───────────┘
               │                                      │
               ▼                                      │
         EPISODE DROPS                                │
         T+0                                          │
               │                                      │
               ▼                                      │
    ┌──────────────────────┐                          │
    │  AUDIENCE ENGAGEMENT │                          │
    │  - YouTube views     │                          │
    │  - Podcast listens   │                          │
    │  - Dossier reads     │                          │
    │  - Newsletter opens  │                          │
    └──────────┬───────────┘                          │
               │                                      │
               │               ┌─────────────────────┘
               │               │
               ▼               ▼
         T+1 WEEK: PATREON BETA ACCESS
         (Maintenance Crew tier gets the cabinet first)
               │
               ▼
         T+2-4 WEEKS: CABINET DROPS
         Status: COMING SOON ──► ACTIVE
               │
               ▼
    ┌──────────────────────────────────────────────┐
    │              ARCADE CABINET                  │
    │  Player finishes the game (3-5 min)          │
    │  Win or lose — the end screen fires          │
    └──────────────────┬───────────────────────────┘
                       │
                       ▼
              END SCREEN — CHOOSE YOUR PATH:
              ┌─────────────────────────────┐
              │ → YouTube episode           │
              │ → Next episode              │
              │ → Museum exhibit            │
              │ → Patreon (BETA cabinets)   │
              └──────────┬──────────────────┘
                         │
                         ▼
              SUBSCRIBER / PATREON CONVERSION
                         │
                         ▼
                  NEXT EPISODE DROPS
                  (loop restarts)
```

The loop has no exit. Every path leads back into the content. Every game ends with a door.

---

### The Status-as-Narrative System

A cabinet's status is not just a technical indicator. It is a lore document.

- **COMING SOON** on Skinwalker Ranch means the investigation is ongoing. The case is open. The episode is in production. The ranch is still there.
- **FLICKERING** on Cosmic Selector means something is wrong with the signal — or wants you to think something is wrong. Is that a real technical issue? Or is the glitch the message?
- **OUT OF ORDER** means the cabinet was taken offline for a reason. The placard doesn't always say why. Sometimes the reason is in the episode.
- **UNSTABLE** means behavior is unpredictable. Play at your own risk. The game knows you're there.

The status board at `/arcade` is a living map of the Midnight Visitor Log's case history. It tells you what's active, what's buried, and what's coming. Players who pay attention to status changes before episodes drop are already in the loop before the episode exists.

---

## SECTION 2 — GAME DESIGN FRAMEWORK

### The LDI Arcade Game Design Principles

Every cabinet in the Arcade must follow five rules. No exceptions. Not even for Bob. (Especially for Bob.)

---

**RULE 1: FIVE MINUTES OR UNDER.**

This is a cabinet at a roadside attraction. You put in a quarter, you play, something happens, you walk away. Not an RPG. Not an experience. A cabinet. If the game takes longer than five minutes, it belongs somewhere else. The constraint is the discipline.

---

**RULE 2: THE NARRATIVE IS THE MECHANIC.**

The game must be impossible to fully understand without context from the episode. Not "a platformer with Mothman art on the sprites." A game where the *mechanic itself* — what the player does with their hands — IS the story. Logging signals before they disappear IS the Mothman case. That's not decoration. That's the thing.

If you can reskin the game with different art and sell it as an unrelated product, the design has failed.

---

**RULE 3: THE ENDING CONNECTS BACK.**

Every game ends with a screen. Win or lose, there is a screen. The screen says something about the case — a real detail, a quote, a date, a number. And then it gives the player somewhere to go. The link is not optional. The link is what the game was for.

---

**RULE 4: IN ON THE JOKE.**

The game should feel like it cost $12 to make and was assembled by someone who loves cryptids more than they understand game engines. The pixel art is slightly too dense. The cabinet marquee is slightly too intense. The sound design is a free asset pack that somebody chose with real intentionality. The jank is not a bug. The jank is the Troma energy. The jank is the Bee Movie. The jank is the Toxic Avenger. It should look exactly as weird as it is.

---

**RULE 5: THE BOB QUOTIENT.**

Every game ships with a Bob Quotient from 1 to 4.

| Score | Meaning |
|-------|---------|
| **1** | Straight documentary game design. Grounded, educational, mechanically coherent. |
| **2** | Leans weird. Some absurdist elements. The mechanic is slightly sideways from expected. |
| **3** | Fully committed to the bit. Funny, strange, emotionally accurate, possibly not logically accurate. |
| **4** | Pure Bob. Absurd, chaotic, barely connected to documented reality, emotionally devastatingly accurate. This is the highest honor a cabinet can receive. |

A game with a Bob Quotient of 4 is not a worse game than a 1. It is a different kind of correct.

---

### Technical Constraints

All LDI Arcade games are browser-based, zero-install, and must run without plugins, downloads, or accounts.

| Parameter | Spec |
|-----------|------|
| **Primary framework** | Phaser.js (CE, v3.x) OR Vanilla JS + HTML5 Canvas |
| **Fallback** | CSS game for simpler mechanics (no canvas required) |
| **Target** | Any modern browser (Chrome, Firefox, Safari, Edge) |
| **Mobile** | Responsive preferred; touch controls where feasible |
| **File size** | Under 5MB per game (pixel art, ASCII, procedural generation — no large assets) |
| **Hosting** | Cloudflare Pages alongside Astro site |
| **Integration** | Astro component wraps game iframe OR embeds canvas directly |
| **High scores** | `localStorage` (client-side) OR Cloudflare Workers KV (global leaderboard) |
| **Audio** | Web Audio API, free/CC assets. Keep under 1MB total audio per game. |
| **Dependencies** | Phaser.js CDN — no npm build step required for simple cabinets |

> **👻 GHOST ANNOTATION — CLOUDFLARE KV LEADERBOARD:**
>
> One specific concern on the Workers KV leaderboard. KV is eventually consistent — reads are not guaranteed to reflect the latest write immediately across all edge nodes. For a leaderboard, this means: a player could submit a score, refresh the page, and not see their score in the top 10 yet. This isn't a bug, it's KV's consistency model. The options are: (1) Accept it — "scores propagate within 60 seconds" is fine for a paranormal arcade, add a note in the UI; (2) Use Cloudflare D1 (SQLite-based, strongly consistent, still serverless, still free tier); (3) Show client-side optimistic update — append the player's own score locally while the KV write propagates. I recommend option 3 for the leaderboard display plus option 2 if strong consistency ever matters. Either way, flag the consistency behavior in the build notes so whoever implements this doesn't spend three hours thinking the leaderboard is broken when it's actually just KV doing KV things.
>
> Everything else in the technical stack is sound.
>
> — Ghost (Signal)

---

### The Cabinet Art System

Every cabinet entry on `/arcade` requires the following elements. These are not optional. They are the minimum viable cabinet.

| Element | Description |
|---------|-------------|
| **Cabinet name** | Not the episode title. Something that sounds like an actual arcade game from 1991 found in a truck stop in West Virginia. |
| **Cabinet marquee description** | What the backlit header art looks like. Colors, imagery, vibe. Enough for an artist to execute it. |
| **Cabinet side art description** | The art on the side panel of the physical (imaginary) cabinet. |
| **Status badge** | See status system below. |
| **CREDITS: 1** | Always displayed. Always 1. You always have exactly one credit. |
| **"About This Cabinet"** | A short paragraph in Bob's voice — written from the perspective of the person who built and maintains this specific cabinet. Replaces the coin slot placard. Lore document. |

**Status Reference:**

| Status | Meaning |
|--------|---------|
| `ACTIVE` | Fully playable. The cabinet is on. |
| `FLICKERING` | Playable but exhibiting glitchy behavior — intentional, lore-driven, or both. |
| `BETA` | Patreon Maintenance Crew early access. Not yet public. |
| `COMING SOON` | Episode in production. Cabinet page exists; game does not yet. |
| `OUT OF ORDER` | Retired or intentionally broken. Placard may or may not explain why. |
| `UNSTABLE` | Plays but behavior is unpredictable. May crash. May not. |
| `MAINTENANCE` | Temporarily offline. Ghost is in there with a soldering iron. |
| `CLOSED — CASE RESOLVED` | The case was closed. This cabinet is a memorial. Playable forever. |

---

## SECTION 3 — THE 10-EPISODE CABINET LINEUP

---

### EP01 — MOTHMAN SIGNAL
**Episode:** Mothman (Point Pleasant, WV — 1966-1967)  
**Cabinet Name:** MOTHMAN SIGNAL  
**Status:** ACTIVE  
**Bob Quotient:** 3

**Cabinet Marquee:** Backlit in amber and deep red — the Silver Bridge at night, rendered in thick pixel art strokes with fog rolling off the Ohio River. The Mothman is not shown. Only his eyes: two red dots in the upper right corner of the marquee, above the bridge. The font reads MOTHMAN SIGNAL in a chunky, slightly-kerned block style that was popular on real 1980s cabinets. The word SIGNAL pulses on a two-second interval.

**Cabinet Side Art:** A ham radio operator at a desk, headphones on, pencil in hand, log book open. The frequency dial is lit up. Numbers scroll across it that don't match any licensed band.

**About This Cabinet (Bob's voice):** "Built this one first because it's the one that got me. The bridge is real. The 46 people are real. The radio signals — the ones the ham operators picked up in 1966 that nobody could explain — those are documented. I'm not saying the game will tell you what they were. I'm saying you should try to catch them and see how it feels when you can't."

---

**THE GAME: MOTHMAN SIGNAL**

You are a ham radio operator in Point Pleasant, WV. November 1966. You've been picking up strange frequencies on a slice of the spectrum that should be empty.

**Mechanic:** A horizontal frequency dial scrolls across the screen. Anomalous signals appear as brief waveform spikes at irregular intervals — some last 3 seconds, some less than 1. The player must click (or tap) on the spike to "log" it. Each logged signal reveals a real witness account from the episode: a text fragment floats up from the dial and settles into the log book on the right side of the screen.

The game runs for 90 seconds of in-game time (representing the 13-month active sighting window compressed). The frequency of signals increases as the calendar date approaches December 15, 1967. A small calendar in the corner advances with each logged signal. Miss too many and the calendar skips forward faster.

**Win Condition:** Log 8 or more signals before December 15.

**Lose Condition:** Miss more than 5 signals. The calendar reaches December 15 early. The bridge animation plays.

**End Screen — Win:**  
```
YOU LOGGED THE SIGNALS.

46 people. December 15th, 1967.
The Silver Bridge collapsed at 5:04 PM.

The log is open. It was always open.
You just had to be listening.

[WATCH THE EPISODE] [READ THE DOSSIER]
```

**End Screen — Lose:**  
```
You missed the signals.
They were there.
They always were.

Sometimes the log is incomplete.
That doesn't mean it didn't happen.

[LISTEN TO THE PODCAST] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP01 YouTube, MVL EP01 podcast, museum exhibit.

---

### EP02 — SKINWALKER RANCH
**Cabinet Name:** RANCH WATCH  
**Status:** COMING SOON  
**Bob Quotient:** 3

**Cabinet Marquee:** A wide, flat Utah sky at dusk — burnt orange fading to purple. The Uintah Basin stretches to the horizon. In the foreground, a surveillance camera on a pole, its red recording light on. The word RANCH WATCH is stenciled in military-issue block letters, as if the marquee was printed by a government contractor who was not allowed to put the actual location name on it. Small symbols — cattle, triangle, electromagnetic burst, eye — are arranged in a row across the bottom of the marquee like game controller icons.

**Cabinet Side Art:** Night vision green. A shape on a hill that doesn't match any known animal profile.

**About This Cabinet (Bob's voice):** "Terry Sherman bought 512 acres in 1994, saw a large wolf that bullets didn't stop, watched cattle disappear from locked pens, and sold the place two years later to a scientist who wanted to study it. Bigelow Aerospace bought it after that. The US government is currently involved. I'm not speculating — that's just what's in the public record. The game is: you're on the night watch. Log what you see. The equipment has opinions about what counts."

---

**THE GAME: RANCH WATCH**

The player is a night security researcher on the Skinwalker Ranch property. A grid of camera feeds — 9 panels, 3×3 — displays different sections of the property in night vision green. Events appear in different panels simultaneously: an orb of light, an animal that moves wrong, a shape in the sky, a sudden equipment failure (static).

**Mechanic:** The player must click on anomalous events in the correct panel before they disappear. Some events are obvious (orb of light). Others are ambiguous — was that an animal moving strangely or camera noise? The player must decide: LOG IT or DISMISS IT. Incorrectly dismissing a real anomaly docks points. Incorrectly logging a mundane event (owl, wind in grass) also docks points. The equipment itself starts malfunctioning over time — panels go static, timestamps corrupt, audio crackles. The mechanic IS the epistemological problem of Skinwalker Ranch: how do you know what you saw when your instruments don't agree with your eyes?

**Win Condition:** Log 12 legitimate anomalies with fewer than 3 false positives before the night watch ends.

**End Screen — Win:**  
```
12 EVENTS LOGGED. INSTRUMENTS CONFIRM: 9.
Your eyes saw more than the equipment did.

The ranch has been studied by physicists, military contractors,
and television crews. The anomalies persist.

Nobody has a good explanation. You have a log.

[WATCH THE EPISODE] [SEE THE FULL CASE FILE]
```

**End Screen — Lose:**  
```
THE EQUIPMENT DISAGREED.

This is the central problem of Skinwalker Ranch.
Something is there. The instruments are inconsistent.
Witnesses are credible and contradictory.

The log is incomplete.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP02 YouTube, museum exhibit.

---

### EP03 — FLATWOODS MONSTER
**Cabinet Name:** FLATWOODS ENCOUNTER  
**Status:** COMING SOON  
**Bob Quotient:** 2

**Cabinet Marquee:** 1952-era newspaper comic style — bold ink lines, flat color fills of teal and red. The Flatwoods Monster in the center: a towering 10-foot figure with a spade-shaped head, glowing eyes, a billowing skirt, and clawed hands extended. A hill behind it in Braxton County, West Virginia. Small figures (the group of boys and Kathleen May) are visible in the lower left, mouths open. The font is a tight horror-pulp headline style: FLATWOODS ENCOUNTER. A starburst badge in the corner reads "BASED ON DOCUMENTED 1952 INCIDENT."

**Cabinet Side Art:** The aftermath — a flattened circular area in the grass, a sulfur smell depicted with wavy lines, a boy with irritated eyes and a bandaged throat.

**About This Cabinet (Bob's voice):** "September 12, 1952. Braxton County, WV. A meteor lands on a hill. A group of kids and their mother go to investigate. They encounter something ten feet tall that hisses, glows, and smells like sulfur. They run. Multiple witnesses. The US Air Force looked into it. The game is about getting your sketch right before the memory fades — because the original witness sketch is one of the most detailed firsthand monster descriptions ever recorded."

---

**THE GAME: FLATWOODS ENCOUNTER**

The player is Kathleen May, drawing the thing she saw on the hill while the memory is still fresh. A police sketch mechanic: a series of multiple-choice panels appears, asking the player to choose the correct detail from the witness accounts. "The head was shaped like:" (spade / dome / sphere / helmet). "The eyes were:" (glowing red / white / blue / none visible). "The movement was:" (hovering / walking / gliding / stationary). Each correct answer builds the composite sketch on the right side of the screen. The clock runs — the memory degrades. Details start disappearing from the answer options as time passes.

**Win Condition:** Complete the composite sketch with 8+ correct details before the memory fully fades.

**End Screen — Win:**  
```
SKETCH COMPLETE.

Kathleen May submitted her account to the Air Force.
It was classified as a misidentified owl and meteor.

The sketch disagreed.
So did every witness.

[WATCH THE EPISODE] [SEE THE ORIGINAL SKETCH]
```

**End Screen — Lose:**  
```
THE MEMORY FADED.

This happens. Trauma and adrenaline distort
and compress the details. The Air Force counted on it.

The Flatwoods Monster was never officially explained.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP03 YouTube, Flatwoods Monster dossier.

---

### EP04 — BOHEMIAN GROVE
**Cabinet Name:** GROVE ACCESS  
**Status:** COMING SOON  
**Bob Quotient:** 2

**Cabinet Marquee:** Old-money Northern California — ancient redwoods towering into a dark blue sky, firelight flickering from below. In the foreground, a cloaked figure. Above the trees: a huge owl, stone, unmoving. The marquee art style is deliberately conservative — clean lines, almost tasteful, as if the cabinet itself was approved by a committee. GROVE ACCESS in gold-embossed lettering. Small text at the bottom: "MEMBERS ONLY. ESTABLISHED 1872."

**Cabinet Side Art:** A laminated visitor badge with NO NAME printed where the name should be. A list of "amenities" with several items redacted.

**About This Cabinet (Bob's voice):** "Every year, powerful men gather in the redwoods of Northern California for two weeks. This is documented. The guest list has included presidents and CEOs. There is an owl. There is a ceremony. Alex Jones went over the fence in 2000 and filmed it. This is also documented. The game is about getting your credential checked correctly at seventeen different checkpoints while maintaining exactly the right level of confidence. You've been here before. Allegedly."

---

**THE GAME: GROVE ACCESS**

A stealth-adjacent game with zero violence. The player is attempting to document the Cremation of Care ceremony from inside the Grove. The mechanic: the player must navigate through a series of "checkpoint screens" — each one is a dialogue interaction with a different grove attendant. The player must select the correct responses (drawn from actual documented Grove culture, rituals, and vocabulary) to pass each checkpoint. Wrong answers don't trigger alarms — they trigger politely confused expressions and questions that require the player to backtrack. The game is a social deduction puzzle. A "confidence meter" tracks whether you're acting too nervous or too familiar.

**Win Condition:** Pass all 7 checkpoints and reach the amphitheater before the ceremony begins.

**End Screen — Win:**  
```
YOU SAW THE OWL.

The ceremony dates to 1878. The participants have included
multiple US presidents and CEOs of major corporations.

The official position is that it's harmless fun among friends.
The footage is on the internet.

[WATCH THE EPISODE] [READ THE DOSSIER]
```

**End Screen — Lose:**  
```
ESCORTED OUT.

Politely. With a firmness that suggested this has happened before.

The Grove exists. The ceremony happens.
The guest list is not public.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP04 YouTube, dossier, newsletter issue.

---

### EP05 — DEVIL'S TRAMPING GROUND
**Cabinet Name:** THE CIRCLE  
**Status:** COMING SOON  
**Bob Quotient:** 3

**Cabinet Marquee:** A 40-foot ring in the North Carolina pine forest — dead grass, pale dirt, and a deep dark center. Painted in the style of a 1970s state park sign that someone clearly made way too intense: warm browns and yellows with a deep black void at the center of the circle. THE CIRCLE in block letters with a slight glow at the bottom of each letter, as if lit from below. A small text line reads "CHATHAM COUNTY, NC — EST. UNKNOWN."

**Cabinet Side Art:** Objects placed in the ring that have been "moved back" to the edge by morning — a lantern, a boot, a tin cup.

**About This Cabinet (Bob's voice):** "A 40-foot ring in the North Carolina woods where nothing grows. Has been documented since the 1700s. Anything placed inside the circle is found outside it by morning. Soil samples show no particular reason for the growth pattern. State agricultural extension looked at it. Came back with a report that essentially said 'we don't know.' Local legend says something walks it at night. The game is a stakeout. You put things in the ring. You watch. Something moves them."

---

**THE GAME: THE CIRCLE**

A one-screen observation game. The player places up to 5 objects from a tray (lantern, rope, stone, photograph, compass) inside the circle at the start of each night watch. Then the camera cuts to a time-lapse of the circle at night. The player watches. Things happen: a shimmer, a sound, an impossible shadow. When morning comes, some objects have moved. The player must identify WHAT moved and WHERE it moved to by clicking on the new positions. Correct identifications build the "case log." The circle itself has subtle behaviors that change each playthrough — objects don't always move to the same positions.

**Win Condition:** Correctly log the movement of all 5 objects across 3 consecutive nights.

**End Screen — Win:**  
```
DOCUMENTED.

The Devil's Tramping Ground has been observed for
over 200 years. Nobody has caught anything on camera.
Nobody has explained the soil. Nothing grows there.

Your log has been filed.

[WATCH THE EPISODE] [ADD TO THE MUSEUM]
```

**End Screen — Lose:**  
```
YOU MISSED A MOVEMENT.

This happens. The circle doesn't perform for observers.
Or it does, and something about the observation changes the result.

The ring is still there.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP05 YouTube, museum exhibit.

---

### EP06 — USA'S UP ALL NIGHT: THE B-MOVIE INDUSTRIAL COMPLEX
**Cabinet Name:** BOB'S UNVERIFIED HISTORIES: THE GAME  
**Status:** COMING SOON  
**Bob Quotient:** 4 ⬛⬛⬛⬛ (MAXIMUM BOB)

**Cabinet Marquee:** CHAOS. The marquee is styled as if three different arcades contributed art at the same time and nobody checked for consistency. A giant VHS tape in the center, partially melted. Troma-green slime dripping from the title. In the background: a drive-in movie screen showing a Troma film; silhouettes of the audience are visible. B-movie poster fonts, five different font weights, a color palette that should not work (it works). BOB'S UNVERIFIED HISTORIES: THE GAME in the largest letters possible. A smaller subtitle: "OFFICIALLY UNOFFICIAL. EMOTIONALLY ACCURATE. THE REST IS LEGALLY UNCERTAIN."

**Cabinet Side Art:** A filmstrip with individual frames showing: (1) a Troma executive eating a contract; (2) a distributor with no face; (3) a drive-in screen showing nothing; (4) a film canister labeled "DO NOT OPEN."

**About This Cabinet (Bob's voice):** "USA Network's Up All Night ran from 1989 to 1998. Rhonda Shear and Gilbert Gottfried hosted B-movies that the major studios didn't want and the video stores couldn't classify. Troma Films — Lloyd Kaufman's bizarre, beautiful operation — was producing movies for $50,000 that would make $500,000 and influence every indie filmmaker who watched them at 2 AM. This is a game about that pipeline. Also about the actual industrial economics of B-movie distribution, which are genuinely insane. Also it's the most chaotic game in the Arcade. Also it has Lloyd Kaufman in it. Also I'm not sure it ends. Let me know if it ends."

---

**THE GAME: BOB'S UNVERIFIED HISTORIES: THE GAME**

The player is a B-movie distributor in 1991. The game starts normal: you receive VHS tapes with mysterious titles and must sort them into distribution channels (cable, video store, drive-in, international, "the pile"). Each tape has a genre tag and a budget listed. Simple triage mechanic. This lasts approximately 45 seconds.

Then things start going wrong. The tapes start moving. The genre tags start lying. A tape labeled "ROMANTIC COMEDY" clearly contains footage of a monster. A tape with a $4,000 budget somehow has a star-studded cast. Lloyd Kaufman appears as a pixel sprite and starts offering you "suggestions" that range from financially reasonable to catastrophically illegal. The sorting interface starts malfunctioning — buttons swap, categories multiply, a new distribution channel labeled "THE VOID" appears. The game is asking you to make decisions faster than any human can make them because that's how B-movie distribution actually worked.

**Win Condition:** Technically, distribute 20 films before the system crashes. Practically, "winning" is ambiguous. There is a win screen, but it doesn't behave the way win screens behave.

**Loss Condition:** The system crashes. This also leads to an end screen. The end screen is different every time.

**End Screen — Win (one of several):**  
```
YOU DISTRIBUTED 20 FILMS.

Collectively they made $4.2 million and influenced
47 directors who are now working in Hollywood.
None of them will publicly admit it.

Lloyd Kaufman is proud of you.
This is the highest honor.

[WATCH THE EPISODE] [VISIT TROMA.COM]
```

**End Screen — Loss (one of several):**  
```
THE SYSTEM CRASHED.

This is historically accurate.
Most B-movie distributors of this era eventually crashed.
The films survived. The weird always survives.

[WATCH THE EPISODE] [SEE THE FULL UNVERIFIED HISTORY]
```

**End Screen — Secret (triggered by distributing a tape to THE VOID):**  
```
YOU FOUND THE VOID.

The Void distributed 1,200 films between 1985 and 2003.
None of them are in any database.
Three of them are considered masterpieces by the people who saw them.

Welcome to Bob's Floor.
You've been here before.

[???]
```

**Link-Back CTA:** MVL EP06 YouTube, troma.com (external), Bob's Floor (future easter egg).

---

### EP07 — THE LUBBOCK LIGHTS
**Cabinet Name:** LUBBOCK FORMATION  
**Status:** COMING SOON  
**Bob Quotient:** 2

**Cabinet Marquee:** A flat West Texas sky — the kind of black that only exists 50 miles from the nearest city light. A V-shaped formation of 20-30 glowing white lights moving silently across the frame. The Lubbock Lights as photographed by Carl Hart Jr. in 1951: slightly blurry, clearly real, unexplained. The marquee is designed to look like a Cold War-era government poster that accidentally became beautiful. LUBBOCK FORMATION in clean, authoritative sans-serif. Below: "AUGUST 1951 — MULTIPLE WITNESSES — USAF PROJECT BLUE BOOK."

**Cabinet Side Art:** A 35mm camera with a roll of film partially exposed. The developed prints showing the V formation. A USAF classification stamp: UNRESOLVED.

**About This Cabinet (Bob's voice):** "August 25, 1951. Four Texas Tech professors are sitting on a porch. A formation of lights passes silently overhead. Then it comes back. Then it comes back again. Carl Hart Jr. photographs it. The Air Force investigates. The photos pass every authentication test they run. Project Blue Book closes the case as 'unknown.' The game is about triangulating the formation — you are the four professors, and you have to agree on what you saw."

---

**THE GAME: LUBBOCK FORMATION**

A cooperative-ish observation puzzle played solo. The player controls four viewpoints simultaneously (a 2×2 split screen), each showing a different angle of the Lubbock sky on the night of August 25, 1951. The formation of lights passes through each viewpoint at slightly different angles and times. The player must rotate each viewpoint's "observation angle" to align all four sightings and triangulate the object's flight path before it disappears past the horizon. A formation reconstruction diagram in the center updates as the player aligns viewpoints.

**Win Condition:** Triangulate all four sightings and lock the flight path before the formation disappears.

**End Screen — Win:**  
```
FORMATION DOCUMENTED.

The Lubbock Lights were photographed on three consecutive nights.
The photos were analyzed by the Air Force, MIT, and independent experts.

Project Blue Book classification: UNKNOWN.

There is no asterisk.

[WATCH THE EPISODE] [READ THE BLUE BOOK FILE]
```

**End Screen — Lose:**  
```
THE FORMATION PASSED.

The professors documented it anyway, in writing.
The Air Force disagreed with their memory.

Carl Hart's photos are still in the archive.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP07 YouTube, Project Blue Book archive (external), museum exhibit.

---

### EP08 — MEOW WOLF
**Cabinet Name:** HOUSE OF ETERNAL RETURN  
**Status:** COMING SOON  
**Bob Quotient:** 3

**Cabinet Marquee:** A psychedelic explosion — every color at once, organized into impossible geometry. A Victorian house that doesn't follow physics. Doors that lead to space. A refrigerator that is also a portal. The Meow Wolf color palette: saturated fuchsia, electric teal, deep violet, toxic green. The words HOUSE OF ETERNAL RETURN in a font that looks handwritten by someone with perfect handwriting who was also a professional graphic designer. Smaller text: "SANTA FE, NEW MEXICO — GEORGE R.R. MARTIN FUNDED THIS. YES, THAT ONE."

**Cabinet Side Art:** A rabbit hole. Literally. Peering into it: impossible architecture visible far below.

**About This Cabinet (Bob's voice):** "Meow Wolf opened in Santa Fe in 2016 in a former bowling alley. George R.R. Martin provided seed funding. The concept is an 'immersive art experience' with a narrative — you explore a Victorian house where a family disappeared into interdimensional space, and the whole building is the story. It's not a museum. It's not a theme park. It's not a game. It might be the closest thing to what we're trying to do with the Arcade. This cabinet is a tribute. The game is the puzzle you'd play if you were actually inside it."

---

**THE GAME: HOUSE OF ETERNAL RETURN**

A room-by-room exploration puzzle. The player is inside the Everett Family House — a Victorian home that has fractured into multiple dimensions. Each room connects to something impossible: the dryer leads to a forest, the attic has a hole to outer space, the refrigerator is a portal. The player must find 5 interdimensional "postcards" that the Everett family left behind, hidden inside the impossible geometry of the house. Each postcard is a small piece of the family's narrative.

Navigation is click-based (no joystick required). The house layout is slightly different each time — rooms rearrange. The game is mostly a vibe with a light puzzle mechanic wrapped around it, because that's also what Meow Wolf is.

**Win Condition:** Collect all 5 postcards and return to the front door.

**End Screen — Win:**  
```
YOU FOUND THEM.

Or you found where they went.
Same thing, possibly.

Meow Wolf has welcomed over 1 million visitors since 2016.
Many of them felt something they couldn't explain.
All of them would go back.

[WATCH THE EPISODE] [PLAN A VISIT]
```

**End Screen — Lose (if the player times out in a room):**  
```
YOU GOT LOST.

The house keeps people.
Not always against their will.

[LISTEN TO THE EPISODE] [TRY AGAIN — THE LAYOUT CHANGED]
```

**Link-Back CTA:** MVL EP08 YouTube, meowwolf.com (external), museum exhibit.

---

### EP09 — THE SALLIE HOUSE
**Cabinet Name:** ATCHISON WATCH  
**Status:** COMING SOON  
**Bob Quotient:** 2

**Cabinet Marquee:** A narrow Victorian house at night — yellow porch light, dark windows, a single upstairs window lit from within. Atchison, Kansas, 1993. The marquee art is quiet in a way that cabinet marquees usually aren't — low contrast, almost monochrome, as if the artist was trying not to disturb something. ATCHISON WATCH in small, careful lettering. The subtitle reads: "DOCUMENTED. INVESTIGATED. UNEXPLAINED."

**Cabinet Side Art:** A thermal imaging grid — a human shape, visible in infrared, standing in an empty room.

**About This Cabinet (Bob's voice):** "Tony and Debra Pickman rented a house in Atchison, Kansas in 1992. Tony started experiencing physical attacks in a specific room. Thermal cameras captured anomalous heat signatures. The Sighting was investigated by multiple paranormal teams, documented on video, and eventually the couple moved out. The house is still there. The thermal footage is still archived. The game is a thermal imaging watch — you are the investigator. The signatures are moving."

---

**THE GAME: ATCHISON WATCH**

A slow, tense thermal camera monitoring game. The player monitors a 3-room thermal grid — living room, stairwell, upper bedroom — in real time. Anomalous heat signatures appear and move. The player must track signatures by clicking to place "thermal pins" — each pin notes the position, intensity, and time of an anomaly. The signatures don't behave like normal heat sources: they appear in the center of empty rooms, they move against air circulation, they cluster in the room where Tony Pickman reported the most intense experiences. The game is unhurried. The tension is ambient.

**Win Condition:** Log 10 unique thermal anomalies with accurate position pins before the watch ends.

**End Screen — Win:**  
```
10 ANOMALIES LOGGED.

The Schieferdecker House thermal recordings were submitted
to three university physics departments. None offered an explanation
that fit all the data.

The house is currently a vacation rental.

[WATCH THE EPISODE] [READ THE CASE FILE]
```

**End Screen — Lose:**  
```
THE SIGNATURES MOVED FASTER THAN YOUR LOG.

This is what the Pickmans described.
It was not subtle by the end.

[LISTEN TO THE EPISODE] [TRY AGAIN]
```

**Link-Back CTA:** MVL EP09 YouTube, museum exhibit.

---

### EP10 — THE LOST HIGHWAY: ROUTE 666
**Cabinet Name:** ROUTE 666  
**Status:** COMING SOON  
**Bob Quotient:** 3

**Cabinet Marquee:** A long, straight desert highway at night — the kind that goes to the horizon and keeps going. Headlights illuminating nothing. A route marker in the corner: US 666 in the distinctive federal highway sign font, but the shield is slightly wrong. The sky is too full of stars. Something is in the road ahead that the headlights haven't quite reached. ROUTE 666 in reflective road sign lettering. Below: "THE DEVIL'S HIGHWAY — RENAMED IN 2003. THE ROAD REMEMBERS."

**Cabinet Side Art:** Mile markers counting down. A car pulled to the shoulder with no visible driver. Footprints in the desert leading to the road and stopping.

**About This Cabinet (Bob's voice):** "US Route 666 ran through Utah, Colorado, New Mexico, and Arizona until 2003, when the number was officially changed to US-491 due to its reputation. The highway had an abnormally high accident rate, documented encounters with anomalous vehicles, and enough lore built up over 80 years of existence that the road sign theft rate was the highest of any numbered highway in the country. They changed the number because the states petitioned the federal government. That happened. The game is a night drive. The road has opinions."

---

**THE GAME: ROUTE 666**

An endless driver (low-poly, procedurally generated) that is not trying to kill you — until it is. The player drives down Route 666 at night. The road is straight. Signs appear: mileage markers, town names (some real, some not, the player can't always tell which), weather warnings. Every few miles, something appears in the road: an anomalous vehicle, a figure, a light. The player must identify what it is from a quick-flash multiple choice before it reaches the car. The wrong choice doesn't crash the car — it adds to the "anomaly accumulation" meter. When the meter hits maximum, the night ends and the case log tallies what was documented. The closer to dawn, the longer the road. There is no destination.

**Win Condition:** Reach the state line (the end of the original Route 666 corridor) with the anomaly accumulation under 50%.

**End Screen — Win:**  
```
YOU MADE IT TO THE STATE LINE.

Route 666 was decommissioned and renumbered on August 8, 2003.
The road is still there. The accidents continued at the same rate.

The road doesn't care what you call it.

[WATCH THE EPISODE] [READ THE HIGHWAY REPORT]
```

**End Screen — Lose:**  
```
THE ROAD KEPT YOU.

US-491. Same asphalt. Different number.
The anomaly rate didn't change.

The federal government changed the number anyway.
Sometimes that's all you can do.

[LISTEN TO THE EPISODE] [TRY AGAIN — THE ROAD RESETS]
```

**Link-Back CTA:** MVL EP10 YouTube, museum exhibit, newsletter issue.

---

## SECTION 4 — THE PRODUCTION PIPELINE

A cabinet gets built in parallel with an episode — not after it. The game brief begins when research begins. The cabinet ships when the social deployment window opens. This is the pipeline.

---

### Stage 1 — GAME BRIEF (parallel to Episode Research)

During the research phase for every episode, identify the **one moment or mechanic** that defines the case. Not the full story. The one thing that, if you could make someone feel it, would make the episode unforgettable.

- For Mothman: missing signals that were right there.  
- For Skinwalker Ranch: instruments that don't agree with your eyes.  
- For Route 666: driving toward something you can't quite see.

Document this as a **Game Brief** (template below). Bob signs off on fun factor. Ghost signs off on technical feasibility. Warden approves the narrative connection to the case. All three sign-offs required before Stage 2.

---

### Stage 2 — GAME DESIGN DOC (parallel to Script Writing)

Full game design document — one page. Art direction locked. Cabinet name finalized. The following is settled at this stage and does not change without Pantheon sign-off:

- Core mechanic (the thing the player does with their hands)
- Win condition and loss condition
- End screen copy (exact text, both win and lose states)
- Link-back CTAs (where the end screen points)
- Cabinet name (final — this is the slug, the `/arcade/[slug]` URL, the title)
- Bob Quotient
- Technical approach (Phaser.js / Vanilla Canvas / CSS game)
- Estimated build time in hours

---

### Stage 3 — GAME BUILD (parallel to Episode Production)

Build the game. The tools:

- **Phaser.js** (CDN-linked, no npm required for simple builds) for games with sprites, physics, or animation
- **Vanilla JS + HTML5 Canvas** for simpler observation/click mechanics
- **CSS game** for text-heavy or UI-based mechanics (Grove Access could be CSS-heavy, for instance)
- **Hermes/Claude Code** assists on the build — prompt it with the GDD Lite, the mechanic spec, and the end screen copy

Build stages: Prototype (mechanic only, no art) → Test (playable, rough art) → Polish (final art, sound, end screen, link-backs) → Astro page built at `/arcade/[cabinet-slug]`

The Astro cabinet page wraps the game in an iframe OR embeds the canvas directly, and includes:
- Cabinet marquee (CSS/SVG — not a static image, for performance)
- Status badge
- CREDITS: 1 display
- "About This Cabinet" note in Bob's voice
- High score display (localStorage or KV leaderboard)

---

### Stage 4 — CABINET DROP (parallel to Social Deployment, T+2 weeks post-episode)

```
T+0:    Episode drops (YouTube + Podcast + Dossier + Newsletter)
T+1 wk: BETA cabinet delivered to Patreon Maintenance Crew tier
T+2-4:  Cabinet status changes: COMING SOON → ACTIVE
        Social announcement fires: "A new cabinet has appeared in the Arcade."
        Newsletter issue covers the cabinet drop
        itch.io page goes live simultaneously
```

The social copy for cabinet drops should always feel like a discovery, not a launch. Not: "NEW GAME AVAILABLE." Yes: "Sometime last night, something changed on the /arcade page."

---

### The Game Brief Template

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LDI ARCADE — GAME BRIEF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EPISODE:            [title + episode number]
CABINET NAME:       [the arcade game title — not the episode title]
CABINET SLUG:       [/arcade/slug-here]
DOCUMENT ID:        [BRIEF-EP##]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CORE MECHANIC:
  [One sentence. What does the player DO with their hands.]

NARRATIVE HOOK:
  [How does the mechanic connect to the case. If you can explain
  the game without referencing the episode, rewrite this section.]

WIN CONDITION:
  [What does winning mean in terms of game state AND case resonance]

LOSE CONDITION:
  [What does losing mean — and is losing actually better?
  Sometimes the loss state is the more honest narrative outcome.]

BOB QUOTIENT:        [ 1 / 2 / 3 / 4 ]
  [Note: if this is 4, Bob has to write the About This Cabinet
  note personally. This is non-negotiable. It's his quotient.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

END SCREEN TEXT — WIN:
  [Exact copy. Starts with the emotional beat. Ends with a real
  fact from the case. No exceptions.]

  [Link-back CTA: where does this go? YouTube / Podcast / Dossier
  / Museum / Patreon — pick 1-2, not more]

END SCREEN TEXT — LOSE:
  [Exact copy. Often more honest than the win state.
  Should still end with a real fact from the case.]

  [Link-back CTA: same format as win]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TECHNICAL APPROACH:
  [ ] Phaser.js (sprites, physics, animation)
  [ ] Vanilla JS + Canvas (custom drawing loop)
  [ ] CSS game (UI/text-heavy, minimal canvas)
  [ ] Other: ___________

ESTIMATED BUILD TIME:  [hours — be honest]

ART DIRECTION:
  [Cabinet marquee: what does it look like. 2-3 sentences.
  Enough for an artist to execute without a meeting.]
  
  [Cabinet side art: 1-2 sentences.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PANTHEON SIGN-OFFS:
  Bob (Fun Factor):            [ SIGNED / PENDING ]
  Ghost (Technical):           [ SIGNED / PENDING ]
  Warden (Narrative Archive):  [ SIGNED / PENDING ]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## SECTION 5 — THE ARCADE AS A MONETIZATION LAYER

### Patreon Perk — BETA Cabinet Access

BETA cabinet access for Patreon Maintenance Crew (Tier 2, $7/mo) is the most concrete, tangible deliverable in the LDI Patreon stack.

"Early video access" as a Patreon perk has a fundamental problem: the subscriber still has to wait and then watch a video. "BETA cabinet access" means: a game exists. Right now. It is playable. You can play it today. Nobody else can. This is qualitatively different from every other early-access perk in the content creator economy.

The mechanics:
- Cabinet page is built and live but password-gated (simple Cloudflare Access or Astro middleware with a Patreon-linked token)
- BETA status badge is displayed publicly on the `/arcade` index so non-Patreons can see what's coming
- Access unlocks one week before public drop
- Patrons get a "cabinet key" — a short code in their Patreon welcome message that unlocks the gate

---

### The High Score Leaderboard

A global leaderboard powered by Cloudflare Workers KV (see Ghost's annotation re: consistency model before implementing).

- Top 10 scores displayed on each cabinet's Astro page
- Players enter a **callsign** rather than a username — logged into the **Witness Registry** (a lore-appropriate name for the leaderboard database that also ties to the investigation theme)
- Monthly "high score wipe" with social announcement — creates a recurring engagement event. "The Witness Registry has been cleared. Your record was good. Start again."
- Callsign constraints: must be 3-8 characters, alphanumeric, no slurs (basic filter). Callsigns persist across games via localStorage — once you pick a callsign, it follows you across all cabinets.

---

### itch.io Distribution

Every LDI Arcade game should also be published on itch.io simultaneously with the public cabinet drop.

Why itch.io:
- 80 million registered users, most of whom have never heard of the Midnight Visitor Log
- Browser games are a first-class format on itch.io with their own discovery surface
- Name-your-price model: free to play, but the option to pay exists and converts at a meaningful rate for games with emotional impact
- itch.io pages rank independently in Google for their game titles
- The paranormal/horror game community on itch.io is large and actively engaged

Each itch.io page:
- Game title = cabinet name (MOTHMAN SIGNAL, RANCH WATCH, etc.)
- Description written in Bob's voice — same tone as "About This Cabinet"
- Tags: `paranormal`, `browser-game`, `cryptid`, `historical`, `horror-light`
- External links: @LithiumDreamsTV, lithium-dreams.com, `/arcade`
- Screenshots of the cabinet art and gameplay

This is a passive discovery channel. It compounds. A player who finds MOTHMAN SIGNAL on itch.io in 2027 is a new LDI subscriber.

---

### Sponsorship Integration

Cabinet end screens can carry tasteful, in-world sponsor integration:

```
— THIS CABINET IS MAINTAINED BY [SPONSOR] —
They keep the lights on. We keep the weird.
```

The framing is that of real arcade cabinet sponsorship — a small placard on the physical (imaginary) cabinet. In-world, not intrusive, and completely honest about being a sponsor. Positioned on the end screen, after the narrative resolution and the link-back CTA, before the "play again" button.

Rate card considerations:
- Per-cabinet sponsorship (one sponsor owns one cabinet, ongoing)
- Episode bundle sponsorship (sponsor the episode AND the cabinet as a package)
- No sponsor messaging inside the game itself — only on the end screen and in the "About This Cabinet" note if the sponsor is relevant to the episode topic

---

## SECTION 6 — THE LONG GAME: THE ARCADE AS AN ARCHIVE

> **📦 WARDEN ANNOTATION:**
>
> This section is mine.
>
> At 40 cabinets, the Arcade becomes something that did not exist when the first game was built. It becomes a map. Not a metaphorical map — a literal record of what the Midnight Visitor Log investigated, when, and what the investigation produced. The status indicators are timestamps. The OUT OF ORDER cabinets are chapters that have closed. The FLICKERING ones are chapters that haven't resolved yet.
>
> I manage archives. I know what they become over time. An archive is not a collection — it's an argument. Every item you chose to keep, and the order in which you kept it, argues that these things belong together, that they form a narrative, that the pattern is real.
>
> The Arcade's pattern, at 40 cabinets, will be visible to anyone who walks the floor with attention. Mothman to Route 666. Point Pleasant to the Utah desert. What connects them is not just that they're "weird." What connects them is that in every case, official explanations were insufficient and the witnesses were credible. The Arcade, in aggregate, is that argument.
>
> The Codex is not a secret page. It's a thesis statement made playable.
>
> The Cabinet Memorial is the most serious thing in this document. When a CLOSED — CASE RESOLVED status appears, it means something was settled — by the community, by new evidence, by a real-world event. That designation should be rare. It should mean something. It should never be used ironically.
>
> Bob will want to put things in the Codex that don't belong there. I will not be approving those.
>
> — Warden (Earth)
> *"The system keeps receipts."*

---

### The Arcade Codex

Located at `/arcade/codex`, or accessible via easter egg (the easter egg method is preferred — make the player earn it).

**Easter egg unlock path:** Collect a hidden item in 5 different cabinet games. Each item is a letter. The letters spell CODEX. On any cabinet game, if the player enters the word CODEX at the title screen (or in a specific interaction point), the Codex unlocks permanently in localStorage.

The Codex page contains:
- Every cabinet ever built, with full status history (when it went COMING SOON, when it went ACTIVE, when it went OUT OF ORDER, if applicable)
- The meta-narrative of the Arcade itself: who built it, why it exists in the same universe as the Midnight Visitor Log, who Bob is relative to this building
- A running timeline of all cases, from earliest (Flatwoods, 1952) to most recent
- Status change log — a Warden-voiced changelog of every status update, treating the cabinet floor like a living document

The Codex is not publicly linked anywhere. No SEO. No social posts pointing to it. It exists for the people who found it.

---

### Cabinet Status Lifecycle

```
Episode announced → COMING SOON
Episode drops, game in BETA → BETA (Patreon only)
Public cabinet drop → ACTIVE
Deliberate glitch/mystery → FLICKERING
Temporary technical issue → MAINTENANCE
Intentional retirement / lore reason → OUT OF ORDER
Rare: case closed / resolved → CLOSED — CASE RESOLVED
Never: cabinet deleted — cabinets are NEVER deleted.
       They become OUT OF ORDER. They are preserved.
```

**The Preservation Rule:** No cabinet is ever removed from the Arcade. OUT OF ORDER cabinets remain accessible — the game still runs, the end screen still fires, the link-backs still work. The status change is the story. Deleting a cabinet would be like destroying the only copy of a case file.

---

### The Cabinet Memorial

When a real-world event resolves a case — new evidence emerges, an official explanation is finally issued, the community reaches consensus — the cabinet status can be changed to CLOSED — CASE RESOLVED.

This is rare. It should be rare. The criteria:

1. New primary source evidence (not theorizing, not a new documentary — actual evidence)
2. Warden signs off on the resolution
3. A brief announcement is made in the newsletter: "The case has been closed."
4. The cabinet end screen gains a new footer: the date of resolution and a single sentence about what was determined.

This designation can be reversed if new evidence re-opens the case. The status history is logged in the Codex.

---

### Bob's Floor

A future section of the Arcade — accessible from the main floor via a door that is slightly the wrong color, or a hallway that didn't seem to be there before.

Bob's Floor runs only Bob Quotient 4 games — the maximum chaos tier. The aesthetic is louder, brighter, and more chromatically aggressive than the rest of the Arcade. The cabinet art doesn't follow the same conventions. The status indicators on Bob's Floor include statuses that don't exist anywhere else:

- `TECHNICALLY FUNCTIONAL` — runs, but we're not sure what it's doing
- `SUPERVISED` — Ghost is watching this one specifically
- `DO NOT PLAY TWICE IN A ROW` — logged precaution, reasoning undisclosed

Bob's Floor is introduced when EP06's Bob's Unverified Histories game ships. The door to Bob's Floor appears on the `/arcade` page without announcement. No status badge. No description. Just a door that wasn't there yesterday.

---

## APPENDIX — QUICK REFERENCE

### All 10 Cabinets at a Glance

| EP | Cabinet Name | Status | Bob Quotient | Primary Mechanic |
|----|-------------|--------|-------------|-----------------|
| 01 | Mothman Signal | ACTIVE | 3 | Signal detection / radio log |
| 02 | Ranch Watch | COMING SOON | 3 | Multi-camera anomaly monitoring |
| 03 | Flatwoods Encounter | COMING SOON | 2 | Police sketch / witness recall |
| 04 | Grove Access | COMING SOON | 2 | Social deduction / checkpoint puzzle |
| 05 | The Circle | COMING SOON | 3 | Observation / object tracking |
| 06 | Bob's Unverified Histories: The Game | COMING SOON | 4 | B-movie triage (chaos mechanic) |
| 07 | Lubbock Formation | COMING SOON | 2 | Multi-view triangulation |
| 08 | House of Eternal Return | COMING SOON | 3 | Exploration / room navigation |
| 09 | Atchison Watch | COMING SOON | 2 | Thermal anomaly logging |
| 10 | Route 666 | COMING SOON | 3 | Endless driver / anomaly ID |

---

### Current Full Arcade Status Board

| Cabinet | Status |
|---------|--------|
| Mothman Signal | ACTIVE |
| Cosmic Selector | FLICKERING |
| Gopher Guts | ACTIVE |
| Jersey Devil Joust | ACTIVE |
| Alien Abduction | BETA |
| No-Clip Racing | OUT OF ORDER |
| Bigfoot Brawl | UNSTABLE |
| Cryptid Crush | COMING SOON |

---

### The Pantheon Sign-Off Matrix

| Decision | Bob | Ghost | Warden |
|----------|-----|-------|--------|
| Fun factor / Bob Quotient | ✓ required | — | — |
| Technical approach | — | ✓ required | — |
| Narrative/archive accuracy | — | — | ✓ required |
| Cabinet name | ✓ required | — | ✓ required |
| CLOSED — CASE RESOLVED status | — | — | ✓ required |
| Bob's Floor additions | ✓ required | ✓ required | — |
| Codex updates | — | — | ✓ required |

---

*"The weirdness is not decoration. The system keeps receipts."*

*OM-0022 — Filed after closing at the Last Roadside Attraction.*  
*Document status: ACTIVE.*  
*Last reviewed: The Pantheon.*
