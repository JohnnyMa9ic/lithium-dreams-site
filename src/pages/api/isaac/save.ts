import type { APIRoute } from 'astro';
import { env } from 'cloudflare:workers';

export const prerender = false;

/* Tyler's Isaac save — a single-user "reflection zone" so his marks grid
 * survives a Safari storage purge or a switch to a new device. Offline-first:
 * the app still saves to his phone instantly and works with no network; this
 * endpoint is only a background mirror.
 *
 * Auth is an obscurity soft-gate (one shared write token, one fixed KV key),
 * which is the right weight because the data is one kid's game-completion marks
 * — not sensitive. The token is embedded in the app's public JS by design; the
 * two copies must match. Upgrade path if this ever needs to be real: a
 * Cloudflare Access policy + per-user keys. */
const WRITE_TOKEN = '6bc7e34e028697ff6d8c6cd601e80d54fe1f94b53dfd4cf9';
const SAVE_KEY = 'save:tyler';
const MAX_BODY_BYTES = 262_144; // 256 KB — a full marks+run save is a few KB

function store(): KVNamespace | undefined {
  return (env as unknown as { ISAAC_SAVES?: KVNamespace }).ISAAC_SAVES;
}

function json(body: Record<string, unknown>, status: number): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
  });
}

function authed(request: Request): boolean {
  const h = request.headers.get('authorization') ?? '';
  const token = h.startsWith('Bearer ') ? h.slice(7) : '';
  return token === WRITE_TOKEN;
}

export const GET: APIRoute = async ({ request }) => {
  if (!authed(request)) return json({ ok: false, error: 'unauthorized' }, 401);
  const kv = store();
  if (!kv) return json({ ok: false, error: 'storage unavailable' }, 500);
  const raw = await kv.get(SAVE_KEY);
  if (!raw) return json({ ok: true, empty: true }, 200);
  // Stored value is already the JSON envelope we wrote — pass it straight back.
  return new Response(raw, {
    status: 200,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
  });
};

export const PUT: APIRoute = async ({ request }) => {
  if (!authed(request)) return json({ ok: false, error: 'unauthorized' }, 401);

  const contentLength = Number(request.headers.get('content-length') ?? 0);
  if (contentLength > MAX_BODY_BYTES) return json({ ok: false, error: 'too large' }, 413);

  let body: Record<string, unknown>;
  try {
    body = (await request.json()) as Record<string, unknown>;
  } catch {
    return json({ ok: false, error: 'invalid json' }, 400);
  }

  // Never let a malformed or empty payload overwrite weeks of grinding. The
  // write must carry a v:1 save with a real marks object; the client is also
  // careful never to push an all-empty save, but we enforce it here too.
  const save = body.save as { v?: unknown; marks?: unknown } | undefined;
  if (!save || save.v !== 1 || typeof save.marks !== 'object' || save.marks === null) {
    return json({ ok: false, error: 'no valid save' }, 422);
  }

  const savedAt = typeof body.savedAt === 'number' ? body.savedAt : Date.now();
  const device = typeof body.device === 'string' ? body.device.slice(0, 40) : null;
  const envelope = JSON.stringify({
    save,
    summary: body.summary ?? null,
    savedAt,
    device,
    serverAt: new Date().toISOString(),
  });

  const kv = store();
  if (!kv) return json({ ok: false, error: 'storage unavailable' }, 500);
  try {
    await kv.put(SAVE_KEY, envelope);
  } catch (err) {
    console.error('ISAAC_SAVES put failed', err);
    return json({ ok: false, error: 'write failed' }, 500);
  }
  return json({ ok: true, savedAt }, 200);
};
