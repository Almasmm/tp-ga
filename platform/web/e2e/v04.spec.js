// v0.4 pages: experiment v0.4, run monitor, reproducibility. API answers are stubbed where the
// content depends on a run that may not exist on the test machine.
import { expect, test } from "@playwright/test";

test.beforeEach(async ({ page }) => {
  page.on("pageerror", (error) => {
    throw error;
  });
});

const T5 = (value) => ({
  name: value,
  columns: ["set", "size", "method_a", "method_b", "n", "p_holm_text", "hl_shift"],
  rows: [{ set: "uniform", size: "20x20", method_a: "GA-rand-base", method_b: "VAM", n: 10, p_holm_text: "0.020", hl_shift: value.endsWith("norm") ? 0.4 : 12.5 }],
});

test("experiment v0.4 shows tables and switches between gap and normalised gap", async ({ page }) => {
  await page.route("**/api/artifacts/v2", (r) =>
    r.fulfill({ json: { available: true, tables: ["T2_gap", "T5_methods_gap", "T5_methods_gap_norm"], figures: { en: [], ru: [] }, docs: [], report: { runs: 42 }, phases: { reference: [{}] }, invocations: 1 } }));
  await page.route("**/api/artifacts/v2/tables/T5_methods_gap", (r) => r.fulfill({ json: T5("T5_methods_gap") }));
  await page.route("**/api/artifacts/v2/tables/T5_methods_gap_norm", (r) => r.fulfill({ json: T5("T5_methods_gap_norm") }));
  await page.route("**/api/artifacts/v2/tables/T2_gap", (r) =>
    r.fulfill({ json: { name: "T2_gap", columns: ["set", "size", "method", "gap_median", "gap_norm_median"], rows: [{ set: "uniform", size: "20x20", method: "VAM", gap_median: 2.5, gap_norm_median: 0.05 }] } }));
  await page.goto("/experiment-v2");
  await expect(page.getByRole("heading", { level: 1, name: "Эксперимент v0.4" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "T5. Сравнение методов (отклонение)" })).toBeVisible();
  await expect(page.getByText("12,5").first()).toBeVisible();
  await page.getByRole("button", { name: "нормированное" }).first().click();
  await expect(page.getByRole("heading", { name: "T5n. Сравнение методов (нормированное)" })).toBeVisible();
  await expect(page.getByText("0,4").first()).toBeVisible();
  await expect(page.getByRole("heading", { name: /v0\.3\.0 и v0\.4 рядом/ })).toBeVisible();
});

test("experiment v0.4 explains how to start when nothing has run", async ({ page }) => {
  await page.route("**/api/artifacts/v2", (r) => r.fulfill({ json: { available: false, tables: [], figures: { en: [], ru: [] }, docs: [], phases: {}, invocations: 0 } }));
  await page.goto("/experiment-v2");
  await expect(page.getByText("Эксперимент v0.4 ещё не запускался")).toBeVisible();
  await expect(page.getByText("tpga-exp run --config experiments/paper-v2.yaml")).toBeVisible();
});

const STATE = {
  phase: "main",
  message: "",
  overall: { done: 120, total: 1000, elapsed_s: 3600 },
  phase_progress: { done: 20, total: 400, rate_per_min: 12.5, eta_s: 7200, elapsed_s: 100 },
  workers: [{ cpu: 0, method: "GA-rand-tuned", set: "uniform", size: "50x50", instance: "uniform-50x50-03", seed: 20261117, evals: 250000, budget: 500000, best_gap: 3.2, running_s: 42 }],
  recent: [{ method: "RS", instance: "uniform-20x20-01", seed: 20261116, gap: 40.1, gap_norm: 0.5, stop_reason: "budget", time_s: 1.2 }],
  methods: {},
  system: { cpu_percent: [100, 90], ram_free_gb: 40, ram_total_gb: 64, disk_free_gb: 500, temperature: null },
  counts: { errors: 0 },
};

test("run monitor shows the state written by the runner and warns when it is old", async ({ page }) => {
  let stale = false;
  await page.route("**/api/monitor/state", (r) => r.fulfill({ json: { available: true, age_s: stale ? 600 : 2, stale, state: STATE } }));
  await page.goto("/monitor");
  await expect(page.getByRole("heading", { level: 1, name: "Монитор прогона" })).toBeVisible();
  await expect(page.getByRole("cell", { name: "uniform-50x50-03" })).toBeVisible();
  await expect(page.getByRole("cell", { name: "50 %" })).toBeVisible();
  await expect(page.getByText("120 / 1 000")).toBeVisible();
  await expect(page.getByRole("alert")).toHaveCount(0);
  stale = true;
  await expect(page.getByRole("alert")).toContainText("прогон, вероятно, остановлен", { timeout: 10_000 });
  // the page has no control that could change the run
  await expect(page.getByRole("button", { name: /Запустить|Остановить|Отменить/ })).toHaveCount(0);
});

test("run monitor without a run", async ({ page }) => {
  await page.route("**/api/monitor/state", (r) => r.fulfill({ json: { available: false } }));
  await page.goto("/monitor");
  await expect(page.getByText("Ни один прогон не пишет своё состояние")).toBeVisible();
});

test("reproducibility lists the configuration hash from the real API", async ({ page }) => {
  await page.goto("/reproducibility");
  await expect(page.getByRole("heading", { level: 1, name: "Воспроизводимость" })).toBeVisible();
  const row = page.getByRole("row").filter({ hasText: "experiments/paper-v2.yaml" });
  await expect(row).toBeVisible();
  await expect(row.locator("td").nth(1)).toHaveText(/^[0-9a-f]{64}$/);
});

test.describe("phone width", () => {
  test.use({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  for (const path of ["/experiment-v2", "/monitor", "/reproducibility"]) {
    test(`page ${path} fits 390 px`, async ({ page }) => {
      await page.route("**/api/monitor/state", (r) => r.fulfill({ json: { available: true, age_s: 1, stale: false, state: STATE } }));
      await page.goto(path);
      await page.waitForLoadState("networkidle");
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      expect(overflow).toBeLessThanOrEqual(1);
    });
  }
});
