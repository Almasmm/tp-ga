"use client";

import { useMemo, useState } from "react";
import { Play } from "lucide-react";
import { useSettings } from "../providers";
import { api } from "../lib/api";
import { num, pct } from "../lib/format";
import { useStepper } from "../lib/use-stepper";
import { useAsync } from "../lib/use-async";
import { Field, Metric, PageHead, Panel, Segmented, State } from "../components/ui";
import { LineChart } from "../components/charts";
import { StepperControls } from "../components/stepper-controls";
import { MiniMap } from "../components/mini-map";
import { TransportMatrix, denseFromCells } from "../components/matrix";

function Genes({ perm, n, segment, mutated, label }) {
  return (
    <div>
      <div className="meta" style={{ marginBottom: 4 }}>{label}</div>
      <div className="perm">
        {perm.map((arc, pos) => {
          const inSeg = segment && pos >= segment[0] && pos <= segment[1];
          const mut = mutated && mutated.includes(pos);
          return <span key={pos} className={"gene " + (mut ? "mutated" : inSeg ? "segment" : "")}>({Math.floor(arc / n) + 1},{(arc % n) + 1})</span>;
        })}
      </div>
    </div>
  );
}

const NONE = [];

export default function GAPage() {
  const { t, lang } = useSettings();
  const [form, setForm] = useState({ example: "3x4", population: 12, generations: 40, mutation_rate: 0.2, crossover_rate: 0.9, seed: 1, initialization: "random" });
  const [submitted, setSubmitted] = useState(form);
  const set = (patch) => setForm((f) => ({ ...f, ...patch }));
  const result = useAsync(JSON.stringify(submitted), async () => {
    const ex = (await api("/trace/examples"))[submitted.example];
    const params = { ...submitted };
    delete params.example;
    return api("/trace/ga", { method: "POST", body: { problem: { kind: "matrix", supply: ex.supply, demand: ex.demand, cost: ex.cost }, ...params } });
  });
  const run = () => (JSON.stringify(form) === JSON.stringify(submitted) ? result.reload() : setSubmitted(form));
  const trace = result.data;
  const { status, error } = result;

  const gens = trace?.generations ?? NONE;
  const stepper = useStepper(Math.max(0, gens.length - 1), trace);
  const k = stepper.k;
  const cur = gens[k];
  const prev = gens[k - 1];
  const detail = cur?.offspring;
  const n = trace?.n ?? 1;
  const curve = useMemo(() => gens.slice(0, k + 1).map((g) => [g.generation, g.best_cost]), [gens, k]);
  const elites = new Set(detail?.elite ?? []);
  const candA = new Set(detail?.tournament_a.candidates ?? []);
  const candB = new Set(detail?.tournament_b.candidates ?? []);

  return (
    <>
      <PageHead kicker={t("navLearn")} title={t("ga")}>
        {lang === "en"
          ? "Generation by generation on a small instance: tournament selection, OX1 crossover, swap mutation and elitism. The same seed reproduces the run."
          : "Поколение за поколением на малой задаче: турнирный отбор, OX1-кроссовер, мутация-обмен и элитизм. Тот же seed воспроизводит запуск."}
      </PageHead>
      <div className="split">
        <Panel title={lang === "en" ? "Parameters" : "Параметры"} as="form" onSubmit={(e) => { e.preventDefault(); run(); }}>
          <div className="stack">
            <Segmented label={t("example")} value={form.example} onChange={(v) => set({ example: v })}
              options={[{ value: "3x4", label: "3 × 4" }, { value: "4x5", label: "4 × 5" }]} />
            <div className="field-row">
              <Field label={t("population")}><input type="number" min={4} max={60} value={form.population} onChange={(e) => set({ population: Number(e.target.value) })} /></Field>
              <Field label={t("generations")}><input type="number" min={1} max={300} value={form.generations} onChange={(e) => set({ generations: Number(e.target.value) })} /></Field>
              <Field label={t("mutation")}><input type="number" min={0} max={1} step={0.01} value={form.mutation_rate} onChange={(e) => set({ mutation_rate: Number(e.target.value) })} /></Field>
              <Field label={t("crossover")}><input type="number" min={0} max={1} step={0.05} value={form.crossover_rate} onChange={(e) => set({ crossover_rate: Number(e.target.value) })} /></Field>
              <Field label={t("seed")}><input type="number" min={0} value={form.seed} onChange={(e) => set({ seed: Number(e.target.value) })} /></Field>
            </div>
            <Field label={t("initialization")}>
              <Segmented label={t("initialization")} value={form.initialization} onChange={(v) => set({ initialization: v })}
                options={[{ value: "random", label: t("random") }, { value: "cost-aware", label: t("costAware") }]} />
            </Field>
            <button type="submit" disabled={status === "loading"}><Play size={16} aria-hidden="true" />{t("run")}</button>
          </div>
        </Panel>
        <State status={status} error={error} onRetry={result.reload}>
          {cur && (
            <div className="stack">
              <Panel title={`${t("generation")} ${cur.generation}`} actions={<StepperControls stepper={stepper} total={gens.length - 1} />}>
                <div className="grid grid-4">
                  <Metric label={lang === "en" ? "best cost" : "лучшая стоимость"} value={num(cur.best_cost, 2, lang)} />
                  <Metric label={t("optimum")} value={num(trace.lp_cost, 2, lang)} />
                  <Metric label={t("gap")} value={pct((100 * (cur.best_cost - trace.lp_cost)) / trace.lp_cost, lang)} />
                  <Metric label={lang === "en" ? "diversity" : "разнообразие"} value={num(cur.diversity, 3, lang)} />
                </div>
                <div style={{ marginTop: 16 }}>
                  <LineChart series={[{ key: "GA-rand", label: lang === "en" ? "best cost" : "лучшая стоимость", points: curve }]}
                    refs={[{ y: trace.lp_cost, label: t("optimum") }]} xLabel={t("generation")} yLabel={t("cost")} height={220} />
                </div>
              </Panel>
              {detail && prev && (
                <Panel title={lang === "en" ? "How the first offspring of this generation was made" : "Как получен первый потомок этого поколения"}
                  subtitle={lang === "en" ? "Population of the previous generation; candidates of the two tournaments are marked" : "Популяция предыдущего поколения; отмечены участники двух турниров"}>
                  <div className="stack">
                    <div className="perm" aria-label={t("population")}>
                      {prev.population_costs.map((c, idx) => {
                        const mark = idx === detail.tournament_a.winner || idx === detail.tournament_b.winner ? "current" : candA.has(idx) || candB.has(idx) ? "used" : elites.has(idx) ? "segment" : "";
                        return <span key={idx} className={"gene " + mark} title={`#${idx}`}>{num(c, 0, lang)}</span>;
                      })}
                    </div>
                    <p className="meta">
                      {lang === "en" ? "Blue: tournament winners; light blue: other candidates; amber: elite copied unchanged." : "Синий — победители турниров; голубой — остальные участники; янтарный — элита, копируется без изменений."}
                    </p>
                    <Genes perm={detail.parent_a} n={n} segment={detail.crossover.cut} label={lang === "en" ? "Parent A (segment kept by OX1)" : "Родитель A (сегмент сохраняет OX1)"} />
                    <Genes perm={detail.parent_b} n={n} label={lang === "en" ? "Parent B (fills the rest in its order)" : "Родитель B (заполняет остальное в своём порядке)"} />
                    <Genes perm={detail.after_crossover} n={n} segment={detail.crossover.cut} label={detail.crossover.applied ? (lang === "en" ? "After crossover" : "После кроссовера") : (lang === "en" ? "No crossover: copy of A" : "Без кроссовера: копия A")} />
                    <Genes perm={detail.child} n={n} segment={detail.crossover.cut} mutated={detail.mutation.positions} label={detail.mutation.applied ? (lang === "en" ? "After swap mutation (pink)" : "После мутации-обмена (розовым)") : (lang === "en" ? "No mutation" : "Без мутации")} />
                    <span className="meta">{t("cost")}: <span className="code-value">{num(detail.child_cost, 2, lang)}</span></span>
                  </div>
                </Panel>
              )}
              <div className="grid grid-2">
                <Panel title={lang === "en" ? "Best plan" : "Лучший план"}>
                  <TransportMatrix cost={trace.problem.cost} plan={denseFromCells(cur.best_plan, trace.m, trace.n)} supplyLeft={trace.problem.supply} demandLeft={trace.problem.demand} />
                </Panel>
                <Panel title={lang === "en" ? "Best plan as flows" : "Лучший план: потоки"}>
                  <MiniMap m={trace.m} n={trace.n} cells={cur.best_plan} supply={trace.problem.supply} demand={trace.problem.demand} />
                </Panel>
              </div>
            </div>
          )}
        </State>
      </div>
    </>
  );
}
