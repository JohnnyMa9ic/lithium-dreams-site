# Opening Day Review — YYYY-MM-DD

## Summary

| Check | Status | Notes |
|---|---|---|
| Route availability | — | All 20 routes return 200? |
| Broken links | — | Any 404 hrefs found? |
| Desktop screenshots | — | Review /screenshots/ folder |
| Mobile screenshots | — | Review /screenshots/ folder |
| Axe a11y (critical) | — | Zero critical/serious violations? |
| Lighthouse performance | — | Score ≥ 80? |
| Lighthouse accessibility | — | Score ≥ 90? |

## Route Check

Run: `npm run review:routes`

Paste output or note any failures here.

## Screenshots

Run: `npm run review:screenshots`

Screenshots saved to: `reviews/YYYY-MM-DD-opening-day/screenshots/`

Pages to spot-check manually:

| Page | Desktop | Mobile | Notes |
|---|---|---|---|
| home | [ ] | [ ] | |
| attraction | [ ] | [ ] | |
| deep-garden | [ ] | [ ] | Verify scroll descent renders |
| arcade | [ ] | [ ] | Leaderboard overflow on mobile? |
| work | [ ] | [ ] | |
| gift-shop | [ ] | [ ] | |

## Accessibility

Run: `npm run review:axe`

Full JSON reports saved to: `reviews/YYYY-MM-DD-opening-day/axe-*.json`

Violations (copy from output):

## Lighthouse

Run: `npm run review:lighthouse`

| Page | Performance | Accessibility | Best Practices | SEO |
|---|---|---|---|---|
| home | | | | |
| work | | | | |
| deep-garden | | | | |

## Issues Found

### Critical (blocks launch)

### High (fix before launch)

### Low (nice to have)

## Sign-off

- [ ] All routes return 200
- [ ] No critical a11y violations
- [ ] Desktop layout reviewed for all 20 pages
- [ ] Mobile layout reviewed for all 20 pages
- [ ] Lighthouse performance ≥ 80 on key pages
