// Site-wide configuration values that are safe to keep in source.

// Cloudflare Web Analytics site token. Empty string = no beacon rendered.
// LEAVE THIS EMPTY: the zone already has Web Analytics with "Automatic setup"
// (dash → Analytics → Web Analytics → lithium-dreams.com, created 2026-06,
// verified collecting 2026-09-20 — 39 views/29 visits in 24h). Cloudflare
// injects the beacon at the edge; pasting a token here would DOUBLE-COUNT
// every page view. Only fill this if automatic setup is ever turned off.
export const CF_ANALYTICS_TOKEN = '';
