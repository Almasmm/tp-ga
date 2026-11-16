"use client";

import { useMemo, useState } from "react";
import { useSettings } from "../providers";
import { api } from "../lib/api";
import { METHOD_COLOR, METHOD_NAME, num, pct } from "../lib/format";
import { useStepper } from "../lib/use-stepper";
import { useAsync } from "../lib/use-async";
import { MethodLabel, PageHead, Panel, Segmented, State } from "../components/ui";
import { TransportMatrix } from "../components/matrix";
import { StepperControls } from "../components/stepper-controls";
import { Bars } from "../components/charts";

const CODES = ["NWC", "LCM", "VAM"];
const RULES = {
  ru: {
    NWC: "Начинаем с левой верхней клетки. Назначаем min(запас, потребность); если строка исчерпана — вниз, иначе вправо.",
    LCM: "Клетки по возрастанию стоимости (равные — по номеру дуги). Пропускаем клетки с исчерпанной строкой или столбцом.",
    VAM: "Штраф строки или столбца — разность двух наименьших стоимостей среди активных клеток. Берём линию с наибольшим штрафом и в ней самую дешёвую клетку.",
  },
  en: {
    NWC: "Start at the top-left cell, allocate min(supply, demand); move down if the row is exhausted, otherwise right.",
    LCM: "Visit cells by increasing cost (ties by arc index); skip cells whose row or column is exhausted.",
    VAM: "The penalty of a row or column is the difference of its two smallest active costs. Take the line with the largest penalty and its cheapest cell.",
  },
};

const NONE = [];

export default function ClassicalPage() {
  const { t, lang } = useSettings();
  const [example, setExample] = useState("3x4");
  const [method, setMethod] = useState("VAM");
  const loaded = useAsync(example, async () => {
    const e = (await api("/trace/examples"))[example];
    const problem = { kind: "matrix", supply: e.supply, demand: e.demand, cost: e.cost };
    const all = await Promise.all(CODES.map((code) => api("/trace/classical", { method: "POST", body: { problem, method: code } })));
    return Object.fromEntries(all.map((r) => [r.method, r]));
  });
  const traces = loaded.data;
  const { status, error } = loaded;

  const trace = traces?.[method];
  const steps = trace?.steps ?? NONE;
  const stepper = useStepper(steps.length, `${example}-${method}-${traces ? 1 : 0}`);
  const k = stepper.k;
  const view = useMemo(() => {
    if (!trace) return null;
    const { cost, supply, demand } = trace.problem;
    const plan = cost.map((r) => r.map(() => 0));
    for (const s of steps.slice(0, k)) plan[s.row][s.col] += s.quantity;
    const last = k ? steps[k - 1] : null;
    return {
      cost,
      plan,
      supplyLeft: last ? last.supply_left : supply,
      demandLeft: last ? last.demand_left : demand,
      current: last ? [last.row, last.col] : null,
      last,
      line: last && (last.line === "row" ? { type: "row", index: last.row } : last.line === "col" ? { type: "col", index: last.col } : null),
    };
  }, [trace, steps, k]);

  return (
    <>
      <PageHead kicker={t("navLearn")} title={t("classical")}
        actions={<Segmented label={t("example")} value={example} onChange={setExample}
          options={[{ value: "3x4", label: "3 × 4" }, { value: "4x5", label: "4 × 5" }]} />}>
        {lang === "en"
          ? "Three classical rules for an initial basic plan, step by step on the same instance, with their cost against the LP optimum."
          : "Три классических правила построения опорного плана — по шагам на той же задаче, со стоимостью относительно оптимума ЛП."}
      </PageHead>
      <State status={status} error={error} onRetry={loaded.reload}>
        {view && (
          <div className="stack">
            <Segmented label={t("methodsLabel")} value={method} onChange={setMethod}
              options={CODES.map((c) => ({ value: c, label: METHOD_NAME[lang][c] }))} />
            <div className="split split-side">
              <Panel title={METHOD_NAME[lang][method]} subtitle={RULES[lang][method]} actions={<StepperControls stepper={stepper} total={steps.length} />}>
                <TransportMatrix cost={view.cost} plan={view.plan} supplyLeft={view.supplyLeft} demandLeft={view.demandLeft}
                  current={view.current} line={view.line}
                  rowNote={method === "VAM" ? view.last?.row_penalty : undefined}
                  colNote={method === "VAM" ? view.last?.col_penalty : undefined} />
                {method === "VAM" && view.last && (
                  <p className="meta" aria-live="polite" style={{ marginTop: 12 }}>
                    {t("penalties")}: Δ — {t("rowPenalty")} / {t("colPenalty")}.{" "}
                    {view.last.line === "single"
                      ? lang === "en" ? "One line left: cheapest cell." : "Осталась одна линия: самая дешёвая клетка."
                      : `${view.last.line === "row" ? "A" + (view.last.row + 1) : "B" + (view.last.col + 1)} → A${view.last.row + 1}B${view.last.col + 1}, x = ${num(view.last.quantity, 2, lang)}`}
                  </p>
                )}
              </Panel>
              <Panel title={t("totalCost")} subtitle={`${t("optimum")}: ${num(trace.lp_cost, 2, lang)}`}>
                <Bars
                  rows={[...CODES.map((c) => ({ key: c, label: <MethodLabel code={c} short />, value: traces[c].cost, color: METHOD_COLOR[c], highlight: c === method })),
                    { key: "LP", label: <MethodLabel code="LP" short />, value: trace.lp_cost, color: METHOD_COLOR.LP }]}
                  format={(v) => num(v, 2, lang)}
                />
                <div className="table-wrap" style={{ marginTop: 16 }}>
                  <table>
                    <thead><tr><th>{t("methodsLabel")}</th><th className="num">{t("cost")}</th><th className="num">{t("gap")}</th></tr></thead>
                    <tbody>
                      {CODES.map((c) => (
                        <tr key={c}><td><MethodLabel code={c} short /></td><td className="num">{num(traces[c].cost, 2, lang)}</td><td className="num">{pct(traces[c].gap_percent, lang)}</td></tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </Panel>
            </div>
          </div>
        )}
      </State>
    </>
  );
}
