"use client";

import { useMemo, useState } from "react";
import { Shuffle } from "lucide-react";
import { useSettings } from "../providers";
import { api } from "../lib/api";
import { num, pct } from "../lib/format";
import { useStepper } from "../lib/use-stepper";
import { useApi } from "../lib/use-api";
import { useAsync } from "../lib/use-async";
import { Metric, PageHead, Panel, Segmented, State } from "../components/ui";
import { TransportMatrix } from "../components/matrix";
import { StepperControls } from "../components/stepper-controls";

const NONE = [];

export default function DecoderPage() {
  const { t, lang } = useSettings();
  const [example, setExample] = useState("3x4");
  const [seed, setSeed] = useState(0);
  const examples = useApi("/trace/examples");
  const ex = examples.data?.[example];
  const result = useAsync(ex ? `${example}-${seed}` : null, () =>
    api("/trace/decoder", { method: "POST", body: { problem: { kind: "matrix", supply: ex.supply, demand: ex.demand, cost: ex.cost }, seed } }),
  );
  const trace = result.data;
  const status = examples.status === "error" ? "error" : result.status === "idle" ? "loading" : result.status;
  const error = examples.error ?? result.error;

  const steps = trace?.steps ?? NONE;
  const stepper = useStepper(steps.length, `${example}-${seed}-${trace ? 1 : 0}`);
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
      partial: steps.slice(0, k).reduce((acc, s) => acc + s.quantity * cost[s.row][s.col], 0),
    };
  }, [trace, steps, k]);

  return (
    <>
      <PageHead kicker={t("navLearn")} title={lang === "en" ? "How the decoder works" : "Как работает декодер"}
        actions={<>
          <Segmented label={t("example")} value={example} onChange={setExample}
            options={[{ value: "3x4", label: "3 × 4" }, { value: "4x5", label: "4 × 5" }]} />
          <button className="secondary" onClick={() => setSeed((s) => s + 1)}><Shuffle size={16} aria-hidden="true" />{t("newPermutation")}</button>
        </>}>
        {lang === "en"
          ? "A chromosome is a permutation of all arcs. The greedy decoder turns it into a shipment plan, one arc at a time."
          : "Хромосома — перестановка всех дуг. Жадный декодер превращает её в план перевозок, дуга за дугой."}
      </PageHead>
      <State status={status} error={error} onRetry={() => (examples.status === "error" ? examples.reload() : result.reload())}>
        {view && (
          <div className="stack">
            <Panel title={t("permutation")} subtitle={lang === "en" ? "Arc (i, j) is source Ai to destination Bj; seed " + seed : "Дуга (i, j) — из Ai в Bj; seed " + seed}>
              <div className="perm" aria-label={t("permutation")}>
                {trace.permutation.map((arc, pos) => {
                  const n = trace.problem.cost[0].length;
                  const s = steps[pos];
                  const cls = pos === k - 1 ? "current" : pos < k ? (s?.quantity > 0 ? "used" : "done") : "";
                  return <span key={pos} className={"gene " + cls}>({Math.floor(arc / n) + 1},{(arc % n) + 1})</span>;
                })}
              </div>
            </Panel>
            <div className="split split-side">
              <Panel title={t("plan")} actions={<StepperControls stepper={stepper} total={steps.length} />}>
                <TransportMatrix cost={view.cost} plan={view.plan} supplyLeft={view.supplyLeft} demandLeft={view.demandLeft} current={view.current} />
                <p className="meta" aria-live="polite" style={{ marginTop: 12 }}>
                  {view.last
                    ? `A${view.last.row + 1}→B${view.last.col + 1}: x = min(${t("remainingSupply")}, ${t("remainingDemand")}) = ${num(view.last.quantity, 2, lang)} — ${view.last.quantity > 0 ? t("allocated") : t("skipped")}`
                    : t("stepOf", { a: 0, b: steps.length })}
                </p>
              </Panel>
              <div className="stack">
                <Panel title={t("totalCost")}>
                  <div className="grid grid-2">
                    <Metric label={lang === "en" ? "so far" : "на текущем шаге"} value={num(view.partial, 2, lang)} />
                    <Metric label={t("optimum")} value={num(trace.lp_cost, 2, lang)} />
                    <Metric label={lang === "en" ? "plan of this permutation" : "план этой перестановки"} value={num(trace.cost, 2, lang)} />
                    <Metric label={t("gap")} value={pct(trace.gap_percent, lang)} />
                  </div>
                </Panel>
                <Panel title={t("whyFeasible")}>
                  <p className="list-text" style={{ color: "var(--text-secondary)" }}>{t("whyFeasibleText")}</p>
                </Panel>
              </div>
            </div>
          </div>
        )}
      </State>
    </>
  );
}
