import { test } from '@playwright/test';
import path from 'path';
import fs from 'fs';
import { ROUTES } from './routes';
import { VIEWPORTS } from './viewports';

const TODAY = new Date().toISOString().split('T')[0];
const REVIEW_DIR = path.join(process.cwd(), 'reviews', `${TODAY}-opening-day`);
const SCREENSHOT_DIR = path.join(REVIEW_DIR, 'screenshots');

test.beforeAll(() => {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
});

for (const viewport of VIEWPORTS) {
  test.describe(`${viewport.name} (${viewport.width}×${viewport.height})`, () => {
    test.use({ viewport: { width: viewport.width, height: viewport.height } });

    for (const route of ROUTES) {
      test(`${route.path}`, async ({ page }) => {
        await page.goto(route.path);
        await page.waitForLoadState('networkidle');
        const filename = `${route.name}--${viewport.name}.png`;
        await page.screenshot({
          path: path.join(SCREENSHOT_DIR, filename),
          fullPage: true,
        });
      });
    }
  });
}
