import { defineConfig } from '@playwright/test';

const TODAY = new Date().toISOString().split('T')[0];

export default defineConfig({
  testDir: './qa',
  use: {
    browserName: 'chromium',
    baseURL: 'http://localhost:4321',
  },
  reporter: [
    ['line'],
    ['html', { outputFolder: `reviews/${TODAY}-opening-day/playwright-report`, open: 'never' }],
  ],
  outputDir: `reviews/${TODAY}-opening-day/test-artifacts`,
  workers: 2,
  timeout: 30000,
  webServer: {
    command: 'npm run dev',
    port: 4321,
    reuseExistingServer: true,
    timeout: 30000,
  },
});
