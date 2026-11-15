"use client";

import { useMemo, useState } from "react";
import { Download } from "lucide-react";
import { useSettings } from "../providers";
import { useApi } from "../lib/use-api";
import { METHODS, num } from "../lib/format";
import { Field, PageHead, Panel, Segmented, Source, State } from "../components/ui";
import { LineChart } from "../components/charts";

const TABLE_TITLE = {
  T1_instances: ["T1. Наборы задач", "T1. Instance sets"],
  T2_gap: ["T2. Отклонение от оптимума", "T2. Gap to the optimum"],
  T3_time: ["T3. Время", "T3. Time"],
  T3_time_fit: ["T3b. Степенная аппроксимация времени", "T3b. Power-law time fit"],
  T4_factorial: ["T4. Факторный план", "T4. Factorial plan"],
  T4_factorial_tests: ["T4b. Тесты факторного плана", "T4b. Factorial tests"],
  T5_tests: ["T5. Сравнение методов", "T5. Method comparison"],
  T6_applied: ["T6. Прикладные случаи", "T6. Applied cases"],
};
const FIGURE_TITLE = {
  F1_decoder: ["F1. Декодер на примере 3×4", "F1. Decoder on a 3×4 example"],
  F2_convergence: ["F2. Сходимость", "F2. Convergence"],
  F3_gap_boxplot: ["F3. Отклонение по размерностям", "F3. Gap by size"],
  F4_time_scaling: ["F4. Время от m·n", "F4. Time against m·n"],
  F5_factorial_heatmap: ["F5. Факторный план", "F5. Factorial plan"],
  F6_wheat_map: ["F6. Карта: пшеница", "F6. Map: wheat"],
};
const FILTER_COLUMNS = ["size", "method", "suite", "initialization", "population", "mutation_rate", "set"];

function TableView({ name, lang }) {
  const { t } = useSettings();
  const table = useApi(`/artifacts/tables/${name}`, { isEmpty: (d) => !d.rows.length });
  const [filters, setFilters] = useState({});
  const rows = useMemo(
    () => (table.data?.rows ?? []).filter((r) => Object.entries(filters).every(([k, v]) => v === "" || String(r[k]) === v)),
    [table.data, filters],
  );
  const columns = table.data?.columns ?? [];
  const filterable = FILTER_COLUMNS.filter((c) => columns.includes(c));
  return (
    <State status={table.status} error={table.error} onRetry={table.reload}>
      {table.data && (
        <>
          {filterable.length > 0 && (
            <div className="field-row" style={{ marginBottom: 12 }} aria-label={t("filters")}>
              {filterable.map((c) => {
                const values = [...new Set(table.data.rows.map((r) => String(r[c])))];
                return (
                  <Field key={c} label={c}>
                    <select value={filters[c] ?? ""} onChange={(e) => setFilters((f) => ({ ...f, [c]: e.target.value }))}>
                      <option value="">{t("all")}</option>
                      {values.map((v) => <option key={v} value={v}>{v}</option>)}
                    </select>
                  </Field>
                );
              })}
            </div>
          )}
          <div className="table-wrap" style={{ maxHeight: 520 }}>
            <table>
              <thead><tr>{columns.map((c) => <th key={c} className={typeof table.data.rows[0]?.[c] === "number" ? "num" : ""}>{c}</th>)}</tr></thead>
              <tbody>
                {rows.map((r, i) => (
                  <tr key={i}>{columns.map((c) => <td key={c} className={typeof r[c] === "number" ? "num" : ""}>{typeof r[c] === "number" ? num(r[c], 4, lang) : r[c] ?? "–"}</td>)}</tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="meta" style={{ marginTop: 8 }}>{rows.length} / {table.data.rows.length} · <Source>{`paper_artifacts/tables/${name}.csv`}</Source></p>
        </>
      )}
    </State>
  );
}

function Convergence({ lang, sizes }) {
  const { t } = useSettings();
  const [size, setSize] = useState(sizes.at(-1));
  const data = useApi(size ? `/artifacts/convergence?size=${size}` : null);
  const series = data.data
    ? Object.entries(data.data.methods).map(([m, v]) => ({
        key: m,
        points: v.evals.map((e, i) => [e, Math.max(1e-3, v.median[i])]),
        band: v.evals.map((e, i) => [e, Math.max(1e-3, v.q1[i]), Math.max(1e-3, v.q3[i])]),
      }))
    : [];
  return (
    <Panel title={lang === "en" ? "Convergence (median and interquartile range)" : "Сходимость (медиана и межквартильный размах)"}
      actions={<Segmented label={t("size")} value={size} onChange={setSize} options={sizes.map((s) => ({ value: s, label: s.replace("x", "×") }))} />}>
      <State status={data.status} error={data.error} onRetry={data.reload}>
        {series.length > 0 && <LineChart series={series} xLog yLog xLabel={t("evaluations")} yLabel={lang === "en" ? "gap, % (log)" : "отклонение, % (лог.)"} height={300} />}
      </State>
      <Source>raw/convergence/main.csv</Source>
    </Panel>
  );
}

export default function ExperimentPage() {
  const { t, lang } = useSettings();
  const index = useApi("/artifacts");
  const [table, setTable] = useState("T2_gap");
  const [figLang, setFigLang] = useState(lang);
  const tables = index.data?.tables ?? [];
  const figures = index.data?.figures?.[figLang] ?? [];
  const sizes = ["5x5", "10x10", "20x20", "30x30", "50x50", "100x100"];
  const L = lang === "en" ? 1 : 0;

  return (
    <>
      <PageHead kicker={t("navResearch")} title={t("experiment")}
        actions={<a className="button" href="/api/artifacts/download" download><Download size={16} aria-hidden="true" />{t("download")}</a>}>
        {lang === "en"
          ? "Read-only view of paper_artifacts/: tables T1–T6 and figures F1–F6 exactly as generated from the raw runs."
          : "Только чтение paper_artifacts/: таблицы T1–T6 и рисунки F1–F6 в том виде, в каком они построены из сырых запусков."}
      </PageHead>
      <State status={index.status} error={index.error} onRetry={index.reload} empty={t("noArtifacts")} emptyHint={t("noArtifactsHint")}>
        <div className="stack">
          {tables.length === 0 ? (
            <Panel><State status="empty" empty={lang === "en" ? "Tables are not generated yet" : "Таблицы ещё не построены"} emptyHint="python -m tpga.experiments.report --config experiments/paper.yaml" /></Panel>
          ) : (
            <Panel title={t("tables")} actions={
              <Field label={<span className="sr-only">{t("tables")}</span>}>
                <select aria-label={t("tables")} value={table} onChange={(e) => setTable(e.target.value)}>
                  {tables.map((n) => <option key={n} value={n}>{TABLE_TITLE[n]?.[L] ?? n}</option>)}
                </select>
              </Field>}>
              <TableView key={table} name={table} lang={lang} />
            </Panel>
          )}
          {tables.includes("T5_tests") && (
            <Panel title={t("tests")} subtitle={lang === "en" ? "Wilcoxon signed-rank on per-instance median gaps, Holm correction" : "Критерий Уилкоксона по медианным отклонениям задач, поправка Холма"}>
              <TableView name="T5_tests" lang={lang} />
            </Panel>
          )}
          {index.data?.has_runs && <Convergence lang={lang} sizes={sizes} />}
          <Panel title={t("figures")} actions={<Segmented label={t("language")} value={figLang} onChange={setFigLang} options={[{ value: "en", label: "EN" }, { value: "ru", label: "RU" }]} />}>
            {figures.length === 0 ? (
              <State status="empty" empty={lang === "en" ? "Figures are not generated yet" : "Рисунки ещё не построены"} />
            ) : (
              <div className="grid grid-2">
                {figures.map((f) => (
                  <figure key={f} className="figure-card panel" style={{ margin: 0 }}>
                    {/* the PNG is produced by the report script; plain img keeps the original pixels */}
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={`/api/artifacts/figures/${figLang}/${f}.png`} alt={FIGURE_TITLE[f]?.[figLang === "en" ? 1 : 0] ?? f} loading="lazy" />
                    <figcaption className="row" style={{ justifyContent: "space-between", marginTop: 8 }}>
                      <span className="list-text">{FIGURE_TITLE[f]?.[L] ?? f}</span>
                      <span className="row">
                        <a href={`/api/artifacts/figures/${figLang}/${f}.png`} download>PNG</a>
                        <a href={`/api/artifacts/figures/${figLang}/${f}.pdf`} download>PDF</a>
                      </span>
                    </figcaption>
                  </figure>
                ))}
              </div>
            )}
          </Panel>
          <p className="meta">{METHODS.join(" · ")}</p>
        </div>
      </State>
    </>
  );
}
