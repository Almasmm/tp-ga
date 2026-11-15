// End-to-end tests of the interface against a running API.
// Locally: start scripts/dev.ps1 first, then `npm run test:e2e`.
// CI (E2E_START=1): Playwright starts uvicorn on :8000 and `next start` on :3000 itself.
import { defineConfig, devices } from "@playwright/test";

const base = process.env.E2E_BASE_URL || "http://127.0.0.1:3000";
const start = process.env.E2E_START === "1";

const config = defineConfig({
  testDir: "./e2e",
  timeout: 90_000,
  expect: { timeout: 20_000 },
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  reporter: [["list"], ["html", { open: "never" }]],
  use: { baseURL: base, trace: "retain-on-failure", locale: "ru-RU" },
  projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"], viewport: { width: 1440, height: 900 } } }],
  webServer: start
    ? [
        {
          command: "python -m uvicorn app.main:app --host 127.0.0.1 --port 8000",
          cwd: "../backend",
          url: "http://127.0.0.1:8000/health",
          timeout: 120_000,
          reuseExistingServer: false,
        },
        {
          command: "npm run start -- --hostname 127.0.0.1 --port 3000",
          url: base,
          timeout: 120_000,
          reuseExistingServer: false,
        },
      ]
    : undefined,
});

export default config;
