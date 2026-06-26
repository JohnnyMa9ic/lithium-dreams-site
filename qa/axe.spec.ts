import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import path from 'path';
import fs from 'fs';
import { ROUTES } from './routes';

const TODAY = new Date().toISOString().split('T')[0];
const REVIEW_DIR = path.join(process.cwd(), 'reviews', `${TODAY}-opening-day`);

test.beforeAll(() => {
  fs.mkdirSync(REVIEW_DIR, { recursive: true });
});

test.describe('accessibility — axe-core', () => {
  for (const route of ROUTES) {
    test(`${route.path}`, async ({ page }) => {
      await page.goto(route.path);
      await page.waitForLoadState('networkidle');

      const results = await new AxeBuilder({ page })
        .withTags(['wcag2a', 'wcag2aa'])
        .analyze();

      // Write full results to review dir
      const outFile = path.join(REVIEW_DIR, `axe-${route.name}.json`);
      fs.writeFileSync(outFile, JSON.stringify(results, null, 2));

      const critical = results.violations.filter(v => v.impact === 'critical' || v.impact === 'serious');
      expect(
        critical,
        `${route.path} has ${critical.length} critical/serious a11y violations:\n` +
          critical.map(v => `  [${v.impact}] ${v.id}: ${v.description}`).join('\n')
      ).toHaveLength(0);
    });
  }
});
