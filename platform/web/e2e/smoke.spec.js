// Smoke scenarios: every page renders, a calculation runs, the theme switch persists, phones work.
import { expect, test } from "@playwright/test";

const PAGES = [
  ["/", "Транспортная задача и генетический алгоритм"],
  ["/map", "Транспортная задача на карте"],
  ["/decoder", "Как работает декодер"],
  ["/classical", "Классические методы"],
  ["/ga", "Генетический алгоритм"],
  ["/lab", "Лаборатория"],
  ["/experiment", "Эксперимент статьи"],
  ["/methods", "Методика и воспроизводимость"],
];

test.beforeEach(async ({ page }) => {
  page.on("pageerror", (error) => {
    throw error;
  });
});

for (const [path, heading] of PAGES) {
  test(`page ${path} renders without errors`, async ({ page }) => {
    const errors = [];
    page.on("console", (m) => m.type() === "error" && errors.push(m.text()));
    await page.goto(path);
    await expect(page.getByRole("heading", { level: 1, name: heading })).toBeVisible();
    await expect(page.getByRole("navigation")).toBeVisible();
    await page.waitForLoadState("networkidle");
    expect(errors.filter((e) => !/tile\.openstreetmap|Failed to load resource.*404/.test(e))).toEqual([]);
  });
}

test("decoder steps through the permutation", async ({ page }) => {
  await page.goto("/decoder");
  await expect(page.getByText("Шаг 0 из 12").first()).toBeVisible();
  await page.getByRole("button", { name: "Шаг", exact: true }).click();
  await expect(page.getByText("Шаг 1 из 12").first()).toBeVisible();
  await page.getByRole("button", { name: "Назад" }).click();
  await expect(page.getByText("Шаг 0 из 12").first()).toBeVisible();
});

test("a calculation runs in the laboratory and reports every method", async ({ page }) => {
  await page.goto("/lab");
  await page.getByLabel("m", { exact: true }).fill("6");
  await page.getByLabel("n", { exact: true }).fill("7");
  await page.getByLabel("Бюджет (вызовы декодера)").fill("3000");
  await page.getByRole("button", { name: "Запустить" }).click();
  const results = page.getByRole("table").filter({ hasText: "Отклонение от оптимума" });
  await expect(results).toBeVisible({ timeout: 60_000 });
  for (const code of ["LP", "VAM", "LCM", "GA-rand", "GA-cost"]) await expect(results.getByText(code, { exact: true })).toBeVisible();
  await page.getByRole("button", { name: "Сохранить в историю" }).click();
  await expect(page.getByRole("button", { name: "Сохранено" })).toBeVisible();
});

test("cancelling a long calculation asks for confirmation", async ({ page }) => {
  await page.goto("/lab");
  await page.getByLabel("m", { exact: true }).fill("150");
  await page.getByLabel("n", { exact: true }).fill("150");
  await page.getByLabel("Бюджет (вызовы декодера)").fill("2000000");
  await page.getByLabel("Случайный поиск").check();
  await page.getByRole("button", { name: "Запустить" }).click();
  await page.getByRole("button", { name: "Отменить" }).click();
  const dialog = page.getByRole("alertdialog");
  await expect(dialog).toBeVisible();
  await dialog.getByRole("button", { name: "Остановить" }).click();
  await expect(page.getByText("Расчёт отменён.")).toBeVisible({ timeout: 60_000 });
});

test("theme and language switches persist", async ({ page }) => {
  await page.goto("/decoder");
  await page.getByRole("button", { name: "Настройки" }).click();
  await page.getByRole("dialog").getByRole("button", { name: "Astana" }).click();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "astana");
  await page.getByRole("dialog").getByRole("button", { name: "Закрыть" }).click();
  await page.getByRole("button", { name: "Язык" }).click();
  await expect(page.getByRole("heading", { level: 1, name: "How the decoder works" })).toBeVisible();
  await page.reload();
  await expect(page.locator("html")).toHaveAttribute("data-theme", "astana");
  await expect(page.getByRole("heading", { level: 1, name: "How the decoder works" })).toBeVisible();
  await page.evaluate(() => window.localStorage.clear());
});

test.describe("phone width", () => {
  test.use({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  for (const [path] of PAGES) {
    test(`page ${path} fits 390 px`, async ({ page }) => {
      await page.goto(path);
      await page.waitForLoadState("networkidle");
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      expect(overflow).toBeLessThanOrEqual(1);
    });
  }
  test("menu opens and navigates", async ({ page }) => {
    await page.goto("/");
    await page.getByRole("button", { name: "Меню" }).first().click();
    await page.getByRole("link", { name: "Декодер" }).click();
    await expect(page.getByRole("heading", { level: 1, name: "Как работает декодер" })).toBeVisible();
  });
});
