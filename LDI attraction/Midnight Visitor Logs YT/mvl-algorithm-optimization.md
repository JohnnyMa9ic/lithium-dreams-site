# MIDNIGHT VISITOR LOG
## YouTube & Social Algorithm Optimization Framework
### Lithium Dreams Industries · Signal Engine Division
#### Document ID: OM-0016 · Revision 2037.1

> *"Ghost's domain: the data. Bob's domain: what the data doesn't say. Both are required."*

---

## SECTION 1: YOUTUBE ALGORITHM — WHAT ACTUALLY MATTERS

For a headless AI-native channel, the algorithm signal hierarchy is:

| Signal | Priority | Target Benchmark | Notes |
|--------|----------|-----------------|-------|
| **Click-Through Rate (CTR)** | Critical | >4% healthy; <2% = thumbnail/title problem | Measured: Impressions → Clicks |
| **Absolute Watch Time (minutes)** | Critical | Maximize total minutes, not just % | Longer videos with high retention > short videos |
| **Average View Duration %** | High | >50% AVD triggers algorithmic boost | Chapter markers improve this significantly |
| **Session Starts** | High | Driven by: search traffic, social shares, newsletter | External traffic that opens YouTube = highest value |
| **Return Viewer Rate** | Medium-High | Tracked as "Returning viewers" in Studio | Subscriber notifications boost this |
| **Cards & End Screen CTR** | Medium | Target >1% card CTR | Place at 20%, 50%, and final 20% |
| **Comments / Likes / Shares** | Medium | Engagement matters, but secondary to watch time | Pinned comment from host boosts comment rate |

**The headless channel's key vulnerability:** AI voiceover scripts often have lower information density than human-delivered scripts, causing mid-video drop-off. The fix is tight scripting, chapter markers, and B-roll variety — not shorter videos.

---

## SECTION 2: TERMINAL-CONNECTABLE ANALYTICS RETRIEVAL

### YouTube Data API v3 Setup

```bash
# Install Google API client
pip install google-api-python-client google-auth-oauthlib google-auth-httplib2

# Authenticate (one-time, saves credentials.json)
# Download OAuth2 credentials from Google Cloud Console
# Enable: YouTube Data API v3 + YouTube Analytics API v2 + YouTube Reporting API
```

### Pull Core Video Metrics (Python)

```python
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
import json, csv
from datetime import date, timedelta

def get_channel_analytics(channel_id, start_date, end_date):
    """Retrieve core video performance metrics for a date range."""
    creds = Credentials.from_authorized_user_file('credentials.json')
    yt_analytics = build('youtubeAnalytics', 'v2', credentials=creds)

    response = yt_analytics.reports().query(
        ids=f'channel=={channel_id}',
        startDate=start_date,
        endDate=end_date,
        metrics='views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained,likes,comments,shares',
        dimensions='video',
        sort='-estimatedMinutesWatched',
        maxResults=25
    ).execute()

    return response

# Get last 30 days
end = date.today().isoformat()
start = (date.today() - timedelta(days=30)).isoformat()
results = get_channel_analytics('CHANNEL_ID', start, end)

# Save to CSV
with open('analytics_report.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(results['columnHeaders'])
    writer.writerows(results['rows'])

print(f"Saved {len(results['rows'])} videos to analytics_report.csv")
```

### Pull Audience Retention Curve (per video)

```python
def get_retention_curve(video_id):
    """Pull audience retention data for a specific video."""
    response = yt_analytics.reports().query(
        ids='channel==CHANNEL_ID',
        startDate='2020-01-01',
        endDate=date.today().isoformat(),
        metrics='audienceWatchRatio,relativeRetentionPerformance',
        dimensions='elapsedVideoTimeRatio',
        filters=f'video=={video_id}'
    ).execute()
    return response

# Usage:
curve = get_retention_curve('VIDEO_ID_HERE')
# Plot with matplotlib to identify drop-off points
# Drop-off at >30% of video = intro problem
# Drop-off at 50% = mid-video pacing issue
# Spike at end = end card working
```

### Pull Impressions & CTR (Reporting API — not Analytics API)

**Important:** `impressionBasedCtr` is NOT available in YouTube Analytics API v2. It requires the YouTube Reporting API (bulk, async delivery):

```python
def schedule_ctr_report(channel_id):
    """Schedule an impressions/CTR report via YouTube Reporting API."""
    yt_reporting = build('youtubereporting', 'v1', credentials=creds)

    # Create report job (runs daily, delivered to Google Cloud Storage)
    job = yt_reporting.jobs().create(
        body={
            'reportTypeId': 'channel_basic_a2',  # includes impressionBasedCtr
            'name': f'MVL CTR Report {date.today().isoformat()}'
        }
    ).execute()

    print(f"Report job created: {job['id']}")
    # Download available reports after 24-48 hours
    return job['id']
```

**Alternative — Studio scrape for impressions CTR:**
YouTube Studio does not expose impressions CTR via API. Pull manually from Studio → Analytics → Reach tab weekly, or use a browser automation script (Playwright/Puppeteer) with local browser authenticated session.

---

## SECTION 3: KEYWORD RESEARCH — TERMINAL TOOLS

### YouTube Autocomplete (No API key required)

```python
import requests, json

def youtube_autocomplete(query):
    """Pull YouTube search autocomplete suggestions."""
    url = "https://suggestqueries.google.com/complete/search"
    params = {
        "client": "firefox",
        "ds": "yt",
        "q": query
    }
    response = requests.get(url, params=params)
    suggestions = json.loads(response.text)[1]
    return suggestions

# Example
queries = youtube_autocomplete("mothman")
for q in queries:
    print(q)

# Output example:
# mothman documentary
# mothman sightings 2024
# mothman point pleasant
# mothman chicago
# mothman prophecies
```

### Google Trends — YouTube-Specific (pytrends)

```python
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)  # CDT = UTC-5

# YouTube-specific search interest (gprop='youtube')
pytrends.build_payload(
    ['mothman', 'cryptids', 'paranormal documentary'],
    cat=0,
    timeframe='today 12-m',
    geo='US',
    gprop='youtube'  # YouTube search interest, not web
)

interest = pytrends.interest_over_time()
related = pytrends.related_queries()

print(interest.tail(10))
print(related['mothman']['top'])
```

### Automated Keyword Report (weekly)

```bash
#!/bin/bash
# Run every Monday morning via cron
# cron: 0 8 * * 1 /home/user/workspace/scripts/keyword-report.sh

python3 /home/user/workspace/scripts/keyword-research.py \
  --topics "cryptids,paranormal,fringe history,mothman,roadside america" \
  --output /home/user/workspace/reports/keyword-report-$(date +%Y-%W).md

echo "Keyword report generated: $(date)"
```

---

## SECTION 4: TITLE & THUMBNAIL OPTIMIZATION SYSTEM

### Title Formula Bank (for MVL subject matter)

```
CURIOSITY GAP FORMULAS:
"[SUBJECT]: The [THING] Nobody Talks About"
"Why [LOCATION] Was Never the Same After [YEAR]"
"What Actually Happened in [LOCATION] in [YEAR]"
"The [SUBJECT] Case File: [HOOK DETAIL]"
"[NUMBER] People Saw It. Nobody Believed Them."
"Filed After Closing: The [SUBJECT] Incident"

MVL-SPECIFIC FORMULAS:
"Visitor Log [###]: [Subject]"
"The [LOCATION] Incident | Midnight Visitor Log"
"[SUBJECT] — A Case File | Midnight Visitor Log"
```

### Thumbnail Generation Pipeline (automated)

```python
import openai, subprocess
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def generate_thumbnail(episode_subject, thumbnail_text, style_prompt):
    """Generate and composite a MVL thumbnail."""

    # Step 1: Generate base image via DALL-E 3
    client = openai.OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"""
        Atmospheric, cinematic still image for a paranormal documentary thumbnail.
        Subject: {episode_subject}
        Style: dark roadside Americana, neon signs, 1960s Midwest, dramatic lighting,
        film grain, slightly desaturated, ominous but beautiful.
        NO text in the image. Pure atmospheric visual.
        {style_prompt}
        """,
        size="1792x1024",  # YouTube thumbnail aspect ratio (16:9)
        quality="hd"
    )

    # Step 2: Download base image
    img_url = response.data[0].url
    img_data = requests.get(img_url).content
    img = Image.open(BytesIO(img_data))

    # Step 3: Composite text overlay via Pillow
    draw = ImageDraw.Draw(img)
    # Load Impact font (or substitute)
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Impact.ttf", 90)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/msttcorefonts/Impact.ttf", 45)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Draw text with stroke (outline) for readability
    # Thumbnail text (max 7 words)
    draw.text((50, 850), thumbnail_text, font=font_large,
              fill="white", stroke_width=4, stroke_fill="black")

    # LDI brand badge (bottom right)
    draw.text((1600, 920), "MIDNIGHT VISITOR LOG", font=font_small,
              fill="#D4A017", stroke_width=2, stroke_fill="black")  # Amber brand color

    # Save variants
    img.save(f"ep-thumb-{episode_subject.replace(' ', '-').lower()}.jpg",
             quality=95, optimize=True)
    print(f"Thumbnail generated: ep-thumb-{episode_subject}.jpg")

# Usage:
generate_thumbnail(
    "The Mothman",
    "They all saw the same thing.",
    "Stormy West Virginia night, silhouette of a bridge in fog"
)
```

---

## SECTION 5: PUBLISH SCHEDULE OPTIMIZATION

### Optimal Publish Times (based on paranormal/fringe content audience behavior)

| Day | Time (CDT) | Rationale |
|-----|-----------|-----------|
| **Tuesday 8 PM** | Primary | Peak evening viewing; not competing with Mon/Fri news cycles |
| **Wednesday 7 PM** | Secondary | Mid-week engagement; strong for podcast drops |
| **Saturday 10 AM** | Alternate | Weekend discovery; good for long-form |

**Avoid:** Monday (low intent), Friday (lost in weekend noise), Sunday (peak competition from major channels)

### The Two-Platform Release Pattern

```
TUESDAY 8 PM CDT
→ YouTube video goes live (scheduled in Studio)
→ Podcast episode goes live (Buzzsprout scheduled publish)

WEDNESDAY 8 AM CDT
→ Blog post goes live (Ghost CMS scheduled)
→ Newsletter sent (The Visitor Log dispatch)

WEDNESDAY 12 PM CDT
→ Social clip #1 (cold open clip, ~60 sec, Instagram Reels / TikTok / YouTube Shorts)

THURSDAY 7 PM CDT
→ Social clip #2 (witness account reading, ~90 sec, same platforms)

FRIDAY 12 PM CDT
→ "Filed this week" social post (static image with key fact from episode)
```

---

## SECTION 6: AUTOMATED PERFORMANCE REVIEW

Run this review after every episode, 7 days post-publish.

### Weekly Analytics Pull Script

```bash
#!/bin/bash
# 7-day post-publish performance review
# Run: bash mvl-analytics-review.sh VIDEO_ID EPISODE_NUM

VIDEO_ID=$1
EP_NUM=$2
REPORT_FILE="reports/mvl-ep${EP_NUM}-7day-review.md"

echo "# MVL Episode ${EP_NUM} — 7-Day Performance Review" > $REPORT_FILE
echo "Generated: $(date)" >> $REPORT_FILE
echo "" >> $REPORT_FILE

python3 scripts/pull-video-metrics.py --video_id $VIDEO_ID \
  --days 7 --output $REPORT_FILE

python3 scripts/pull-retention-curve.py --video_id $VIDEO_ID \
  --output reports/mvl-ep${EP_NUM}-retention.png

echo "Review complete: $REPORT_FILE"
```

### Performance Scorecard (fill after each 7-day review)

```
═══════════════════════════════════════════════════════
  MVL EPISODE PERFORMANCE SCORECARD
  Episode: MVL-EP[###] — [TITLE]
  Review date: [7 days post-publish]
═══════════════════════════════════════════════════════

  REACH
  Views (7d):            _______  [Target: >500]
  Impressions:           _______  [Check Studio manually]
  CTR:                   _______% [Target: >4%]
  Traffic source (top):  _______

  ENGAGEMENT
  Avg View Duration:     _______  [Target: >50% of runtime]
  Avg View %:            _______% 
  Likes:                 _______
  Comments:              _______
  Shares:                _______

  AUDIENCE
  Subscribers gained:    _______
  Return viewer %:       _______%

  PODCAST (7d)
  Downloads:             _______
  Completion rate:       _______%

  BLOG (7d)
  Page views:            _______
  Avg time on page:      _______

  THUMBNAIL
  Which variant ran:     [A / B / C]
  CTR notes:             _______

  LEARNINGS (3 max)
  1.
  2.
  3.

  NEXT EPISODE ADJUSTMENTS:
═══════════════════════════════════════════════════════
```

---

## SECTION 7: SOCIAL PLATFORM OPTIMIZATION

### Platform Matrix

| Platform | Content Type | MVL Lane | Post Frequency |
|----------|-------------|---------|---------------|
| **YouTube** | Long-form (15-25 min) + Shorts (60s clips) | Primary broadcast | 1/week |
| **Instagram** | Reels (60-90s), static atmospheric stills | Clip highlights + dossier aesthetics | 3-4/week |
| **TikTok** | Short clips (30-90s), trending audio | Clips, reaction to own content | 3-4/week |
| **X / Twitter** | Thread (episode summary), single fact drops | Drive-In Totals style facts | Daily |
| **Threads** | Atmospheric stills + short copy | Brand building | 2-3/week |
| **YouTube Shorts** | 60s clips from episodes | Algorithm discovery | 2/week |

### Social Copy Templates (auto-generated from episode)

**X / Twitter thread format:**
```
THREAD: The [SUBJECT] Case File
Filed: MVL-EP[###]

1/ [PLAIN DROP — the flat Midwest fact that makes people stop scrolling]

2/ [The detail that deepens it]

3/ [The witness account — one sentence of the best quote]

4/ [The productive question]

5/ Full case file → [YouTube link]
Podcast → [Spotify/Apple link]
Filed in the log: [Blog link]

#MidnightVisitorLog #LithiumDreams #[SubjectTag]
```

**Instagram Reel caption:**
```
Case file MVL-EP[###].

[2-3 sentences of episode hook in host voice]

Full log now streaming. Link in bio.

Filed after closing at the Last Roadside Attraction.
#MidnightVisitorLog #[SubjectTag] #FringeHistory #WeirdAmericana #LithiumDreams
```

---

*OM-0016 · YouTube & Social Algorithm Optimization Framework*
*The Midnight Visitor Log · Lithium Dreams Industries · Signal Engine Division*
*June 2026*
