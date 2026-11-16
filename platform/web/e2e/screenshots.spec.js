// Screenshots for docs/screenshots: every page at 1440 and 390 px in both themes.
// Runs only with SCREENSHOTS=1 (npm run test:e2e -- e2e/screenshots.spec.js).
import { test } from "@playwright/test";

const PAGES = ["", "map", "decoder", "classical", "ga", "lab", "experiment", "methods"];
const OUT = "../../docs/screenshots";

test.skip(process.env.SCREENSHOTS !== "1", "set SCREENSHOTS=1 to write screenshots");
test.setTimeout(300_000);

for (const width of [1440, 390]) {
  for (const theme of ["aspan", "astana"]) {
    for (const lang of width === 1440 ? ["ru", "en"] : ["ru"]) {
      test(`${width}px ${theme} ${lang}`, async ({ page }) => {
        await page.setViewportSize({ width, height: width === 1440 ? 900 : 844 });
        await page.goto("/");
        await page.evaluate(
          ([t, l]) => window.localStorage.setItem("tpga-settings", JSON.stringify({ theme: t, lang: l })),
          [theme, lang],
        );
        for (const p of PAGES) {
          await page.goto("/" + p);
          await page.waitForLoadState("networkidle");
          await page.waitForTimeout(p === "map" ? 2500 : 600);
          // teaching pages: advance a few steps so that the picture shows the process, not an empty table
          const steps = { decoder: 5, classical: 3, ga: 12 }[p];
          if (steps) {
            const label = lang === "en" ? "Step" : "Шаг";
            const button = page.getByRole("button", { name: label, exact: true });
            await button.evaluate((el) => el.scrollIntoView({ block: "center" }));
            for (let k = 0; k < steps; k += 1) await button.click();
            await page.evaluate(() => window.scrollTo(0, 0));
            await page.waitForTimeout(400);
          }
          const name = `${p || "overview"}-${theme}-${width}${lang === "en" ? "-en" : ""}.png`;
          await page.screenshot({ path: `${OUT}/${name}`, fullPage: true });
        }
      });
    }
  }
}
