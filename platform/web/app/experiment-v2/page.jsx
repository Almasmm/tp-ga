"use client";

import { useMemo, useState } from "react";
import { Download } from "lucide-react";
import { useSettings } from "../providers";
import { useApi } from "../lib/use-api";
import { num } from "../lib/format";
import { Field, Metric, PageHead, Panel, Segmented, Source, State } from "../components/ui";
import { ArtifactTable } from "../components/artifact-table";

const BASE = "/artifacts/v2/tables";
const SOURCE = "paper_artifacts_v2/tables";
const TABLE_TITLE = {
  T1_instances: ["T1. Наборы задач", "T1. Instance sets"],
  T2_gap: ["T2. Отклонение от оптимума", "T2. Gap to the optimum"],
  T3_time: ["T3. Время", "T3. Time"],
  T3_fits: ["T3b. Степенная аппроксимация времени", "T3b. Power-law fits"],
  T4_factorial: ["T4. Факторный план", "T4. Factorial plan"],
  T4_tests: ["T4b. Фридман, W Кендалла, попарные тесты", "T4b. Friedman, Kendall's W, post-hoc tests"],
  T5_methods_gap: ["T5. Сравнение методов (отклонение)", "T5. Method comparisons (gap)"],
  T5_methods_gap_norm: ["T5n. Сравнение методов (нормированное)", "T5n. Method comparisons (normalised)"],
  T6_initialisation: ["T6. Случайный и стоимостный старт", "T6. Random vs cost-aware start"],
  T7_stopping: ["T7. Правила остановки", "T7. Stopping rules"],
  T8_lp_scaling: ["T8. Точные методы на больших задачах", "T8. Exact solvers on large instances"],
  T8_lp_disagreement: ["T8b. Расхождения HiGHS и OR-Tools", "T8b. HiGHS vs OR-Tools disagreements"],
  A1_methods_pooled: ["П1. Сравнения по всем размерам (приложение)", "A1. Pooled comparisons (appendix)"],
};
const FIGURE_TITLE = {
  boxplot_gap: ["Отклонение по методам", "Gap by method"],
  boxplot_gap_norm: ["Нормированное отклонение по методам", "Normalised gap by method"],
  convergence: ["Сходимость", "Convergence"],
  time_scaling: ["Время от m·n", "Time against m·n"],
  factorial_heatmap: ["Факторный план", "Factorial plan"],
};
// v0.3.0 method names and their v0.4 counterparts; the stopping rule differs (see the note)
const PAIRS = [["NWC", "NWC"], ["LCM", "LCM"], ["VAM", "VAM"], ["RS", "RS"], ["GA-rand", "GA-rand-base"], ["GA-cost", "GA-cost-base"]];

function Compare({ lang, value }) {
  const v3 = useApi("/artifacts/tables/T2_gap");
  const v4 = useApi(`${BASE}/T2_gap`);
  const col = value === "gap_norm" ? "gap_norm_median" : "gap_median";
  const rows = useMemo(() => {
    if (!v3.data || !v4.data) return [];
    const old = new Map(v3.data.rows.filter((r) => r.suite === "uniform").map((r) => [`${r.size}|${r.method}`, r]));
    const sizes = [...new Set(v4.data.rows.filter((r) => r.set === "uniform").map((r) => r.size))];
    const out = [];
    for (const size of sizes) {
      for (const [a, b] of PAIRS) {
        const n = v4.data.rows.find((r) => r.set === "uniform" && r.size === size && r.method === b);
        const o = old.get(`${size}|${a}`);
        if (n || o) out.push({ size, method: b, v3: value === "gap" ? o?.gap_median : undefined, v4: n?.[col] });
      }
    }
    return out;
  }, [v3.data, v4.data, col, value]);
  const en = lang === "en";
  return (
    <Panel title={en ? "v0.3.0 and v0.4 side by side (uniform set, median)" : "v0.3.0 и v0.4 рядом (набор uniform, медиана)"}
      subtitle={en
        ? "Not the same experiment: v0.3.0 stopped the GA after 200 generations without improvement and used other instances; v0.4 uses the budget only. The normalised gap exists only in v0.4."
        : "Это разные эксперименты: в v0.3.0 ГА останавливался после 200 поколений без улучшения и задачи были другими; в v0.4 — только по бюджету. Нормированное отклонение есть только в v0.4."}>
      <State status={v4.status === "ok" ? v3.status : v4.status} error={v4.error ?? v3.error} onRetry={() => { v3.reload(); v4.reload(); }}
        empty={en ? "No v0.4 table yet" : "Таблицы v0.4 ещё нет"}>
        {rows.length === 0 ? (
          <State status="empty" empty={en ? "Nothing to compare yet" : "Пока нечего сравнивать"} />
        ) : (
          <div className="table-wrap" style={{ maxHeight: 420 }}>
            <table>
              <thead><tr><th>{en ? "size" : "размер"}</th><th>{en ? "method (v0.4)" : "метод (v0.4)"}</th><th className="num">v0.3.0</th><th className="num">v0.4</th></tr></thead>
              <tbody>
                {rows.map((r) => (
                  <tr key={`${r.size}|${r.method}`}>
                    <td>{r.size}</td><td>{r.method}</td>
                    <td className="num">{num(r.v3, 3, lang)}</td><td className="num">{num(r.v4, 3, lang)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </State>
      <Source>paper_artifacts/tables/T2_gap.csv · paper_artifacts_v2/tables/T2_gap.csv</Source>
    </Panel>
  );
}

export default function ExperimentV2Page() {
  const { t, lang } = useSettings();
  const en = lang === "en";
  const L = en ? 1 : 0;
  const index = useApi("/artifacts/v2");
  const [value, setValue] = useState("gap");
  const [table, setTable] = useState("T2_gap");
  const [figLang, setFigLang] = useState(lang);
  const tables = index.data?.tables ?? [];
  const figures = (index.data?.figures?.[figLang] ?? []).filter((f) => !f.startsWith("boxplot_") || f === `boxplot_${value}`);
  const phases = Object.entries(index.data?.phases ?? {});
  const t5 = value === "gap" ? "T5_methods_gap" : "T5_methods_gap_norm";
  const valueSwitch = (
    <Segmented label={en ? "Measure" : "Показатель"} value={value} onChange={setValue}
      options={[{ value: "gap", label: en ? "gap, %" : "отклонение, %" }, { value: "gap_norm", label: en ? "normalised" : "нормированное" }]} />
  );

  return (
    <>
      <PageHead kicker={t("navResearch")} title={t("experimentV2")}
        actions={index.data?.available && <a className="button" href="/api/artifacts/v2/download" download><Download size={16} aria-hidden="true" />{t("download")}</a>}>
        {en
          ? "Read-only view of paper_artifacts_v2/: the revised experiment with tuned GA and SA, a budget-only stop, per-size statistics and the normalised gap."
          : "Только чтение paper_artifacts_v2/: пересмотренный эксперимент с настроенными ГА и имитацией отжига, остановкой по бюджету, статистикой по каждому размеру и нормированным отклонением."}
      </PageHead>
      <State status={index.status} error={index.error} onRetry={index.reload}>
        {index.data && !index.data.available ? (
          <Panel><State status="empty" empty={en ? "The v0.4 experiment has not been run yet" : "Эксперимент v0.4 ещё не запускался"}
            emptyHint="tpga-exp run --config experiments/paper-v2.yaml" /></Panel>
        ) : (
          <div className="stack">
            <div className="grid grid-3">
              <Metric label={en ? "runs in the report" : "запусков в отчёте"} value={num(index.data?.report?.runs ?? 0, 0, lang)} source="report.json" />
              <Metric label={en ? "phases finished" : "фаз завершено"} value={`${phases.length} / 6`} source="run_manifest.json" />
              <Metric label={en ? "run invocations" : "запусков команды"} value={num(index.data?.invocations ?? 0, 0, lang)} source="run_manifest.json" />
            </div>
            {tables.length === 0 ? (
              <Panel><State status="empty" empty={en ? "Tables are not generated yet" : "Таблицы ещё не построены"} emptyHint="tpga-exp report --config experiments/paper-v2.yaml" /></Panel>
            ) : (
              <>
                {tables.includes(t5) && (
                  <Panel title={TABLE_TITLE[t5][L]} actions={valueSwitch}
                    subtitle={en
                      ? "Per (set, size): Wilcoxon on per-instance medians, Holm within the family, Hodges–Lehmann shift with 95 % CI"
                      : "Для каждого (набора, размера): Уилкоксон по медианам задач, поправка Холма внутри семейства, сдвиг Ходжеса–Лемана с 95 % ДИ"}>
                    <ArtifactTable key={t5} base={BASE} source={SOURCE} name={t5} lang={lang} />
                  </Panel>
                )}
                <Panel title={t("tables")} actions={
                  <Field label={<span className="sr-only">{t("tables")}</span>}>
                    <select aria-label={t("tables")} value={table} onChange={(e) => setTable(e.target.value)}>
                      {tables.map((n) => <option key={n} value={n}>{TABLE_TITLE[n]?.[L] ?? n}</option>)}
                    </select>
                  </Field>}>
                  <ArtifactTable key={table} base={BASE} source={SOURCE} name={table} lang={lang} />
                </Panel>
              </>
            )}
            <Compare lang={lang} value={value} />
            <Panel title={t("figures")} actions={<>
              {valueSwitch}
              <Segmented label={t("language")} value={figLang} onChange={setFigLang} options={[{ value: "en", label: "EN" }, { value: "ru", label: "RU" }]} />
            </>}>
              {figures.length === 0 ? (
                <State status="empty" empty={en ? "Figures are not generated yet" : "Рисунки ещё не построены"} />
              ) : (
                <div className="grid grid-2">
                  {figures.map((f) => (
                    <figure key={f} className="figure-card panel" style={{ margin: 0 }}>
                      {/* eslint-disable-next-line @next/next/no-img-element */}
                      <img src={`/api/artifacts/v2/figures/${figLang}/${f}.png`} alt={FIGURE_TITLE[f]?.[figLang === "en" ? 1 : 0] ?? f} loading="lazy" />
                      <figcaption className="row" style={{ justifyContent: "space-between", marginTop: 8 }}>
                        <span className="list-text">{FIGURE_TITLE[f]?.[L] ?? f}</span>
                        <span className="row">
                          <a href={`/api/artifacts/v2/figures/${figLang}/${f}.png`} download>PNG</a>
                          <a href={`/api/artifacts/v2/figures/${figLang}/${f}.pdf`} download>PDF</a>
                        </span>
                      </figcaption>
                    </figure>
                  ))}
                </div>
              )}
            </Panel>
          </div>
        )}
      </State>
    </>
  );
}
