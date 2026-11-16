"use client";

import Link from "next/link";
import { ArrowRight, CheckCircle2, CircleDashed, FlaskConical } from "lucide-react";
import { useSettings } from "./providers";
import { useApi } from "./lib/use-api";
import { num, pct } from "./lib/format";
import { MethodLabel, PageHead, Panel, Source, State } from "./components/ui";

const RQ = {
  ru: [
    ["RQ1", "Насколько решения ГА отклоняются от точного оптимума (HiGHS) на сбалансированных задачах разной размерности?"],
    ["RQ2", "Как ГА соотносится с методами северо-западного угла, минимального элемента и аппроксимации Фогеля?"],
    ["RQ3", "Как время работы ГА растёт с размерностью по сравнению с точным методом?"],
    ["RQ4", "Как размер популяции, вероятность мутации и способ инициализации влияют на качество решения?"],
  ],
  en: [
    ["RQ1", "How far do GA solutions deviate from the exact optimum (HiGHS) on balanced instances of different size?"],
    ["RQ2", "How does the GA compare with the north-west corner, least-cost and Vogel methods?"],
    ["RQ3", "How does the GA's run time grow with size compared with the exact method?"],
    ["RQ4", "How do population size, mutation probability and initialization affect solution quality?"],
  ],
};

function KeyResults({ t2, fits, lang }) {
  const rows = t2.rows.filter((r) => r.suite === "uniform");
  const sizes = [...new Set(rows.map((r) => r.size))].sort((a, b) => a.split("x")[0] * a.split("x")[1] - b.split("x")[0] * b.split("x")[1]);
  const methods = ["GA-rand", "GA-cost", "RS", "NWC", "LCM", "VAM"].filter((m) => rows.some((r) => r.method === m));
  const get = (size, m) => rows.find((r) => r.size === size && r.method === m);
  return (
    <>
      <div className="table-wrap">
        <table>
          <caption className="sr-only">{lang === "en" ? "Mean gap to the LP optimum, uniform set" : "Среднее отклонение от оптимума ЛП, равномерный набор"}</caption>
          <thead>
            <tr><th>{lang === "en" ? "Size" : "Размерность"}</th>{methods.map((m) => <th key={m} className="num"><MethodLabel code={m} short /></th>)}</tr>
          </thead>
          <tbody>
            {sizes.map((s) => (
              <tr key={s}><td className="code-value">{s.replace("x", "×")}</td>{methods.map((m) => <td key={m} className="num">{pct(get(s, m)?.gap_mean, lang)}</td>)}</tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="meta" style={{ marginTop: 8 }}>
        {lang === "en" ? "Mean gap (%) over all runs of the base configuration. " : "Среднее отклонение (%) по всем запускам базовой конфигурации. "}
        <Source>paper_artifacts/tables/T2_gap.csv</Source>
      </p>
      {fits?.rows?.length > 0 && (
        <div className="grid grid-3" style={{ marginTop: 12 }}>
          {fits.rows.filter((f) => f.quantity === "time per run").map((f) => (
            <div key={f.method} className="metric">
              <span className="value">b = {num(f.b, 2, lang)}</span>
              <span className="label"><MethodLabel code={f.method} short /> · t ≈ a·(m·n)^b, 95 % [{num(f.b_ci_low, 2, lang)}; {num(f.b_ci_high, 2, lang)}]</span>
              <Source>tables/T3_time_fit.csv</Source>
            </div>
          ))}
        </div>
      )}
    </>
  );
}

export default function OverviewPage() {
  const { t, lang } = useSettings();
  const index = useApi("/artifacts");
  const t2 = useApi(index.data?.tables?.includes("T2_gap") ? "/artifacts/tables/T2_gap" : null);
  const fits = useApi(index.data?.tables?.includes("T3_time_fit") ? "/artifacts/tables/T3_time_fit" : null);
  const env = index.data?.environment;
  const reach = index.data?.reachability;
  const phases = env?.phases ?? {};

  return (
    <>
      <PageHead kicker="Astana IT University" title={lang === "en" ? "Transportation problem and the genetic algorithm" : "Транспортная задача и генетический алгоритм"}
        actions={<Link className="button" href="/experiment"><FlaskConical size={16} aria-hidden="true" />{t("experiment")}<ArrowRight size={16} aria-hidden="true" /></Link>}>
        {lang === "en"
          ? "A permutation-encoded GA with a greedy decoder for the balanced transportation problem, measured against the exact LP optimum and the classical starting-plan methods. The exact method solves this problem; the study measures the GA's gap, run time and parameter effects."
          : "ГА с перестановочным кодированием и жадным декодером для сбалансированной транспортной задачи в сравнении с точным оптимумом ЛП и классическими методами опорного плана. Точный метод решает эту задачу; исследование измеряет отклонение ГА, время и влияние параметров."}
      </PageHead>
      <div className="stack">
        <Panel title={t("rq")}>
          <div className="grid grid-4">
            {RQ[lang].map(([code, text]) => (
              <div key={code} className="panel" style={{ padding: 16 }}>
                <span className="badge">{code}</span>
                <p className="list-text" style={{ marginTop: 8, marginBottom: 0 }}>{text}</p>
              </div>
            ))}
          </div>
        </Panel>
        <State status={index.status} error={index.error} onRetry={index.reload} empty={t("noArtifacts")} emptyHint={t("noArtifactsHint")}>
          <div className="grid split-side">
            <Panel title={t("keyResults")}>
              <State status={t2.status === "loading" && !index.data?.tables?.includes("T2_gap") ? "empty" : t2.status} error={t2.error} onRetry={t2.reload}
                empty={lang === "en" ? "Tables are not generated yet" : "Таблицы ещё не построены"} emptyHint="python -m tpga.experiments.report --config experiments/paper.yaml">
                {t2.data && <KeyResults t2={t2.data} fits={fits.data} lang={lang} />}
              </State>
              {reach && (
                <p className="list-text" style={{ marginTop: 12 }}>
                  {lang === "en" ? "Reachability: the decoder reproduced " : "Достижимость: декодер воспроизвёл "}
                  <span className="code-value">{reach.reproduced}</span> {lang === "en" ? "of" : "из"} <span className="code-value">{reach.instances}</span>
                  {lang === "en" ? " HiGHS optimal vertices (empirical check). " : " оптимальных вершин HiGHS (эмпирическая проверка). "}
                  <Source>reachability.json</Source>
                </p>
              )}
            </Panel>
            <Panel title={t("lastExperiment")}>
              <ul className="list">
                {Object.entries(phases).map(([name, entries]) => {
                  const total = entries.reduce((a, e) => a + e.wall_s, 0);
                  const errors = entries.reduce((a, e) => a + e.errors, 0);
                  return (
                    <li key={name} className="list-item" style={{ minHeight: "calc(var(--row-h) - 12px)" }}>
                      {errors ? <CircleDashed size={16} aria-hidden="true" color="var(--danger)" /> : <CheckCircle2 size={16} aria-hidden="true" color="var(--success)" />}
                      <span style={{ flex: 1 }}>{name}</span>
                      <span className="code-value">{num(total / 60, 1, lang)} min</span>
                    </li>
                  );
                })}
              </ul>
              {env && (
                <dl className="stack" style={{ gap: 6, marginTop: 12 }}>
                  <div><dt className="meta">{t("codeVersion")}</dt><dd className="code-value" style={{ margin: 0, wordBreak: "break-all" }}>{env.git_commit ?? "–"}{env.git_dirty ? " (dirty)" : ""}</dd></div>
                  <div><dt className="meta">CPU</dt><dd style={{ margin: 0 }}>{env.cpu}</dd></div>
                  <div><dt className="meta">Python · NumPy · SciPy · numba</dt><dd className="code-value" style={{ margin: 0 }}>{env.python} · {env.packages?.numpy} · {env.packages?.scipy} · {env.packages?.numba}</dd></div>
                  <div><dt className="meta">HiGHS</dt><dd className="code-value" style={{ margin: 0 }}>{env.highs}</dd></div>
                  <div><dt className="meta">{lang === "en" ? "Power scheme" : "План питания"}</dt><dd style={{ margin: 0 }}>{env.power_scheme}</dd></div>
                </dl>
              )}
              <Source>environment.json</Source>
            </Panel>
          </div>
        </State>
      </div>
    </>
  );
}
