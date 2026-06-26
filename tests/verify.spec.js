// Verification loop — lithium-dreams-site
// Run against dev server (npm run dev) or preview (npm run preview)
// Definition of done: all pages HTTP 200, no JS errors, content visible at desktop + mobile

import { test, expect } from '@playwright/test';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BASE_URL = process.env.BASE_URL || 'http://localhost:4321';
const SCREENSHOT_DIR = path.join(__dirname, '../test-results/screenshots');

const PAGES = [
  { name: 'index', path: '/' },
  { name: 'attraction', path: '/attraction' },
  { name: 'arcade', path: '/arcade' },
  { name: 'museum', path: '/museum' },
  { name: 'workshop', path: '/workshop' },
  { name: 'fortune', path: '/fortune' },
  { name: 'gift-shop', path: '/gift-shop' },
  { name: 'crossroads', path: '/crossroads' },
  { name: 'employees-only', path: '/employees-only' },
  { name: 'work', path: '/work' },
  { name: 'work-intake', path: '/work/intake' },
  { name: 'work-case-files', path: '/work/case-files' },
];

test.beforeAll(() => {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
});

for (const pg of PAGES) {
  test.describe(pg.name, () => {
    test('desktop 1280px — HTTP 200, no JS errors', async ({ page }) => {
      await page.setViewportSize({ width: 1280, height: 800 });
      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const res = await page.goto(`${BASE_URL}${pg.path}`, { waitUntil: 'networkidle' });
      await page.screenshot({
        path: path.join(SCREENSHOT_DIR, `desktop-${pg.name}.png`),
        fullPage: true,
      });

      expect(res.status(), `${pg.path} returned non-200`).toBe(200);
      expect(errors, `JS errors on ${pg.path}`).toHaveLength(0);
    });

    test('mobile 375px — HTTP 200, no JS errors', async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 812 });
      const errors = [];
      page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
      page.on('pageerror', err => errors.push(err.message));

      const res = await page.goto(`${BASE_URL}${pg.path}`, { waitUntil: 'networkidle' });
      await page.screenshot({
        path: path.join(SCREENSHOT_DIR, `mobile-${pg.name}.png`),
        fullPage: true,
      });

      expect(res.status(), `${pg.path} returned non-200`).toBe(200);
      expect(errors, `JS errors on ${pg.path}`).toHaveLength(0);
    });
  });
}
