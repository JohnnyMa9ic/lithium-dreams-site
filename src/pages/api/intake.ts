import type { APIRoute } from 'astro';

export const prerender = false;

interface MissionBrief {
  reference?: string;
  track?: string;
  organization?: string;
  contact?: string;
  email?: string;
  [key: string]: unknown;
}

const MAX_BODY_BYTES = 32_768;

export const POST: APIRoute = async ({ request, locals }) => {
  const contentLength = Number(request.headers.get('content-length') ?? 0);
  if (contentLength > MAX_BODY_BYTES) {
    return json({ ok: false, error: 'Brief too large.' }, 413);
  }

  let brief: MissionBrief;
  try {
    brief = await request.json();
  } catch {
    return json({ ok: false, error: 'Invalid JSON body.' }, 400);
  }

  if (!brief.track || brief.track === 'Not selected') {
    return json({ ok: false, error: 'Select a track before submitting.' }, 422);
  }

  const kv = (locals as { runtime?: { env?: Record<string, KVNamespace> } })
    .runtime?.env?.MISSION_INTAKE;
  if (!kv) {
    // Fail loudly server-side — do not tell the visitor it worked if it didn't.
    console.error('MISSION_INTAKE KV binding missing');
    return json({ ok: false, error: 'Intake storage unavailable. Please email us directly.' }, 500);
  }

  const receivedAt = new Date().toISOString();
  const key = `${receivedAt}__${brief.reference ?? crypto.randomUUID()}`;
  await kv.put(key, JSON.stringify({ ...brief, receivedAt }));

  return json({ ok: true, reference: brief.reference ?? null });
};

function json(body: Record<string, unknown>, status: number): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json' },
  });
}
