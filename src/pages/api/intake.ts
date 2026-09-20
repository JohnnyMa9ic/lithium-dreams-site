import type { APIRoute } from 'astro';
import { env } from 'cloudflare:workers';

export const prerender = false;

interface MissionBrief {
  reference?: string;
  track?: string;
  organization?: string;
  contact?: string;
  email?: string;
  [key: string]: unknown;
}

interface IntakeEnv {
  MISSION_INTAKE?: KVNamespace;
  INTAKE_MAIL?: { send(message: unknown): Promise<void> };
  INTAKE_ADMIN_KEY?: string;
}

const MAX_BODY_BYTES = 32_768;

export const POST: APIRoute = async ({ request }) => {
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

  const intakeEnv = env as unknown as IntakeEnv;
  const kv = intakeEnv.MISSION_INTAKE;
  if (!kv) {
    // Fail loudly server-side — do not tell the visitor it worked if it didn't.
    console.error('MISSION_INTAKE KV binding missing');
    return json({ ok: false, error: 'Intake storage unavailable. Please email us directly.' }, 500);
  }

  const receivedAt = new Date().toISOString();
  const key = `${receivedAt}__${brief.reference ?? crypto.randomUUID()}`;
  try {
    await kv.put(key, JSON.stringify({ ...brief, receivedAt }));
  } catch (err) {
    console.error('MISSION_INTAKE KV write failed', err);
    return json({ ok: false, error: 'Could not store the brief. Please email us directly.' }, 500);
  }

  // Notify John by email via the zone's Email Routing send_email binding —
  // no secrets, no third party. The KV write above is the source of truth;
  // a notify failure must never fail the submission, so this only logs.
  await notifyOperator(intakeEnv, brief, key);

  return json({ ok: true, reference: brief.reference ?? null });
};

const NOTIFY_FROM = 'intake@lithium-dreams.com';
const NOTIFY_TO = 'john@lithium-dreams.com';

// User-supplied values that end up in MIME headers must not smuggle CRLFs.
function headerSafe(value: unknown): string {
  return String(value ?? '—').replace(/[\r\n]+/g, ' ').slice(0, 200);
}

async function notifyOperator(intakeEnv: IntakeEnv, brief: MissionBrief, key: string): Promise<void> {
  const mailer = intakeEnv.INTAKE_MAIL;
  if (!mailer) {
    console.warn('Intake notify skipped: INTAKE_MAIL send_email binding missing');
    return;
  }

  try {
    const { EmailMessage } = await import('cloudflare:email');
    const subject = headerSafe(`Mission brief: ${brief.track ?? 'no track'} — ${brief.organization ?? brief.contact ?? 'unnamed'}`);
    const body = [
      'New mission brief — lithium-dreams.com/work/intake',
      '',
      `Track:        ${brief.track ?? '—'}`,
      `Organization: ${brief.organization ?? '—'}`,
      `Contact:      ${brief.contact ?? '—'} <${brief.email ?? '—'}>`,
      `Reference:    ${brief.reference ?? '—'}`,
      `KV key:       ${key}`,
      '',
      'Full brief is stored in the MISSION_INTAKE KV namespace under that key.',
    ].join('\n');
    const raw = [
      `From: Glasshouse Intake <${NOTIFY_FROM}>`,
      `To: <${NOTIFY_TO}>`,
      `Subject: ${subject}`,
      `Message-ID: <${crypto.randomUUID()}@lithium-dreams.com>`,
      `Date: ${new Date().toUTCString()}`,
      'MIME-Version: 1.0',
      'Content-Type: text/plain; charset=utf-8',
      '',
      body,
    ].join('\r\n');
    await mailer.send(new EmailMessage(NOTIFY_FROM, NOTIFY_TO, raw));
  } catch (err) {
    console.error('Intake notify failed', err);
  }
}

// Operator backstop: GET /api/intake?key=<INTAKE_ADMIN_KEY> lists stored briefs.
// Answers 404 unless the key secret is configured AND matches — the endpoint
// is invisible without both.
export const GET: APIRoute = async ({ url }) => {
  const intakeEnv = env as unknown as IntakeEnv;
  const adminKey = intakeEnv.INTAKE_ADMIN_KEY;
  const given = url.searchParams.get('key') ?? '';
  if (!adminKey || !timingSafeEqual(given, adminKey)) {
    return new Response('Not found', { status: 404 });
  }

  const kv = intakeEnv.MISSION_INTAKE;
  if (!kv) {
    return json({ ok: false, error: 'MISSION_INTAKE KV binding missing' }, 500);
  }

  const listing = await kv.list({ limit: 100 });
  const briefs = await Promise.all(
    listing.keys.map(async (k) => {
      const raw = await kv.get(k.name);
      let value: unknown = raw;
      try {
        value = raw ? JSON.parse(raw) : null;
      } catch {
        /* leave raw */
      }
      return { key: k.name, value };
    }),
  );
  // Keys start with an ISO timestamp, so lexicographic order is chronological.
  briefs.sort((a, b) => (a.key < b.key ? 1 : -1));

  return json({ ok: true, count: briefs.length, complete: listing.list_complete, briefs }, 200);
};

function timingSafeEqual(a: string, b: string): boolean {
  const enc = new TextEncoder();
  const ab = enc.encode(a);
  const bb = enc.encode(b);
  if (ab.length !== bb.length) return false;
  let diff = 0;
  for (let i = 0; i < ab.length; i++) diff |= ab[i] ^ bb[i];
  return diff === 0;
}

function json(body: Record<string, unknown>, status: number): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'content-type': 'application/json' },
  });
}
