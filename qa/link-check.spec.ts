import { test, expect } from '@playwright/test';
import { ROUTES } from './routes';

test.describe('route availability', () => {
  for (const route of ROUTES) {
    test(`GET ${route.path} → 200`, async ({ request }) => {
      const response = await request.get(route.path);
      expect(response.status(), `${route.path} returned ${response.status()}`).toBe(200);
    });
  }
});

test.describe('no broken internal links', () => {
  for (const route of ROUTES) {
    test(`${route.path} — no 404 hrefs`, async ({ page }) => {
      await page.goto(route.path);
      await page.waitForLoadState('networkidle');

      const links = await page.$$eval('a[href]', anchors =>
        anchors
          .map(a => (a as HTMLAnchorElement).href)
          .filter(href => href.startsWith(location.origin))
          .filter((href, i, arr) => arr.indexOf(href) === i)
      );

      const broken: string[] = [];
      for (const link of links) {
        const r = await page.request.get(link);
        if (r.status() === 404) broken.push(link);
      }

      expect(broken, `Broken links on ${route.path}: ${broken.join(', ')}`).toHaveLength(0);
    });
  }
});
