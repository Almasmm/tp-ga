"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Download, Play, Save, Square, Trash2 } from "lucide-react";
import { useSettings } from "../providers";
import { api, downloadBlob, subscribe } from "../lib/api";
import { METHODS, METHOD_COLOR, num, pct, sec } from "../lib/format";
import { useApi } from "../lib/use-api";
import { ConfirmDialog, Field, MethodLabel, PageHead, Panel, Progress, Segmented, State } from "../components/ui";
import { Bars, LineChart } from "../components/charts";

const DEFAULT_PARAMS = { population: 100, mutation_rate: 0.2, crossover_rate: 0.9, tournament: 3, elite: 2, budget: 100000, stagnation: 200, seed: 0 };

function problemFrom(src) {
  if (src.kind === "generated") return { kind: "generated", m: src.m, n: src.n, seed: src.seed, costs: src.costs };
  if (src.kind === "scenario") return { kind: "scenario", dataset_id: src.dataset_id, scenario_id: src.scenario_id };
  return { kind: "paper", instance_id: src.instance_id };
}

function toCsv(job) {
  const lines = ["method,cost,gap_percent,time_s,evaluations,best_evaluation,stop_reason,dummy_volume"];
  for (const [m, r] of Object.entries(job.result.results)) {
    lines.push([m, r.cost, r.gap_percent ?? "", r.time_s, r.evaluations ?? "", r.best_evaluation ?? "", r.stop_reason ?? "", r.dummy_volume].join(","));
  }
  return lines.join("\n") + "\n";
}

export default function LabPage() {
  const { t, lang } = useSettings();
  const [src, setSrc] = useState({ kind: "generated", m: 20, n: 20, seed: 1, costs: "uniform", dataset_id: "kazakh-wheat", scenario_id: "year-2024", instance_id: "" });
  const [methods, setMethods] = useState(["VAM", "LCM", "GA-rand", "GA-cost"]);
  const [params, setParams] = useState(DEFAULT_PARAMS);
  const [job, setJob] = useState(null);
  const [live, setLive] = useState({});
  const [phase, setPhase] = useState("idle");
  const [error, setError] = useState(null);
  const [confirm, setConfirm] = useState(false);
  const [saved, setSaved] = useState(null);
  const close = useRef(null);
  const scenarios = useApi(src.kind === "scenario" ? `/scenarios?dataset_id=${src.dataset_id}` : null);
  const paper = useApi(src.kind === "paper" ? "/artifacts/instances" : null, { isEmpty: (d) => !d.length });
  const history = useApi("/history");

  useEffect(() => () => close.current?.(), []);
  const setP = (patch) => setParams((p) => ({ ...p, ...patch }));
  const toggle = (m) => setMethods((list) => (list.includes(m) ? list.filter((x) => x !== m) : [...list, m]));

  const start = async () => {
    setError(null);
    setSaved(null);
    setLive({});
    setPhase("running");
    try {
      const created = await api("/jobs", { method: "POST", body: { problem: problemFrom(src), methods: methods.filter((m) => m !== "LP"), params } });
      setJob(created);
      close.current = subscribe(created.id, {
        method_started: (e) => setLive((l) => ({ ...l, [e.method]: { ...(l[e.method] ?? {}), running: true, curve: [] } })),
        progress: (e) => setLive((l) => {
          const cur = l[e.method] ?? { curve: [] };
          return { ...l, [e.method]: { ...cur, ...e, curve: [...cur.curve, [Math.max(1, e.evaluations), e.gap ?? e.best_cost]] } };
        }),
        method_done: (e) => setLive((l) => ({ ...l, [e.method]: { ...(l[e.method] ?? {}), running: false, done: e.result } })),
        done: async () => { setJob(await api(`/jobs/${created.id}`)); setPhase("done"); },
        cancelled: () => setPhase("cancelled"),
        error: (e) => { setError({ message: e.message }); setPhase("error"); },
        closed: () => setPhase((p) => (p === "running" ? "error" : p)),
      });
    } catch (e) {
      setError(e);
      setPhase("error");
    }
  };
  const cancel = useCallback(async () => {
    setConfirm(false);
    if (job) await api(`/jobs/${job.id}`, { method: "DELETE" }).catch(() => null);
  }, [job]);
  const save = async () => {
    const r = await api("/history", { method: "POST", body: { job_id: job.id } }).catch((e) => { setError(e); return null; });
    if (r) { setSaved(r.id); history.reload(); }
  };

  const results = job?.result?.results;
  const curves = Object.entries(live).filter(([m, v]) => ["GA-rand", "GA-cost", "RS"].includes(m) && v.curve?.length > 1);

  return (
    <>
      <PageHead kicker={t("navTools")} title={t("lab")}>
        {lang === "en"
          ? "Choose a problem, methods and parameters; the local back end runs them in a process pool and streams the progress."
          : "Выберите задачу, методы и параметры; локальный бэкенд считает их в пуле процессов и передаёт прогресс."}
      </PageHead>
      <div className="three-pane">
        <Panel title={lang === "en" ? "Problem" : "Задача"}>
          <div className="stack">
            <Segmented label={lang === "en" ? "Source" : "Источник"} value={src.kind} onChange={(v) => setSrc((s) => ({ ...s, kind: v }))}
              options={[{ value: "generated", label: lang === "en" ? "generate" : "генерация" }, { value: "scenario", label: lang === "en" ? "dataset" : "датасет" }, { value: "paper", label: lang === "en" ? "paper set" : "из статьи" }]} />
            {src.kind === "generated" && (
              <div className="field-row">
                <Field label="m"><input type="number" min={1} max={200} value={src.m} onChange={(e) => setSrc((s) => ({ ...s, m: Number(e.target.value) }))} /></Field>
                <Field label="n"><input type="number" min={1} max={200} value={src.n} onChange={(e) => setSrc((s) => ({ ...s, n: Number(e.target.value) }))} /></Field>
                <Field label={t("seed")}><input type="number" min={0} value={src.seed} onChange={(e) => setSrc((s) => ({ ...s, seed: Number(e.target.value) }))} /></Field>
                <Field label={lang === "en" ? "Costs" : "Стоимости"}>
                  <select value={src.costs} onChange={(e) => setSrc((s) => ({ ...s, costs: e.target.value }))}>
                    <option value="uniform">U[1, 100]</option>
                    <option value="structured">{lang === "en" ? "Euclidean + noise" : "евклидовы + шум"}</option>
                  </select>
                </Field>
              </div>
            )}
            {src.kind === "scenario" && (
              <>
                <Field label={lang === "en" ? "Dataset" : "Набор"}>
                  <select value={src.dataset_id} onChange={(e) => setSrc((s) => ({ ...s, dataset_id: e.target.value, scenario_id: e.target.value === "kazakh-wheat" ? "year-2024" : "day-01" }))}>
                    <option value="kazakh-wheat">{t("wheat")}</option>
                    <option value="astana-potato">{t("astana")} · {t("modelNetwork")}</option>
                  </select>
                </Field>
                <State status={scenarios.status} error={scenarios.error} onRetry={scenarios.reload}>
                  <Field label={lang === "en" ? "Scenario" : "Сценарий"}>
                    <select value={src.scenario_id} onChange={(e) => setSrc((s) => ({ ...s, scenario_id: e.target.value }))}>
                      {scenarios.data?.scenarios.map((s) => <option key={s.id} value={s.id}>{s.title ?? s.id} · {s.warehouse_count}×{s.store_count}</option>)}
                    </select>
                  </Field>
                </State>
              </>
            )}
            {src.kind === "paper" && (
              <State status={paper.status} error={paper.error} onRetry={paper.reload} empty={t("noArtifacts")} emptyHint={t("noArtifactsHint")}>
                <ul className="list" style={{ maxHeight: 360, overflow: "auto" }}>
                  {paper.data?.filter((i) => i.suite !== "applied").map((i) => (
                    <li key={i.id}>
                      <button type="button" className="list-item" aria-pressed={src.instance_id === i.id} onClick={() => setSrc((s) => ({ ...s, instance_id: i.id }))}>
                        <span className="code-value" style={{ flex: 1 }}>{i.id}</span><span className="meta">{i.m}×{i.n}</span>
                      </button>
                    </li>
                  ))}
                </ul>
              </State>
            )}
          </div>
        </Panel>
        <Panel title={lang === "en" ? "Methods and parameters" : "Методы и параметры"}>
          <div className="stack">
            <fieldset style={{ border: 0, padding: 0, margin: 0 }}>
              <legend className="meta">{lang === "en" ? "LP is always solved as the reference" : "ЛП решается всегда — это эталон"}</legend>
              {METHODS.filter((m) => m !== "LP").map((m) => (
                <label key={m} className="check"><input type="checkbox" checked={methods.includes(m)} onChange={() => toggle(m)} /><MethodLabel code={m} /></label>
              ))}
            </fieldset>
            <div className="field-row">
              <Field label={t("population")}><input type="number" min={4} max={500} value={params.population} onChange={(e) => setP({ population: Number(e.target.value) })} /></Field>
              <Field label={t("mutation")}><input type="number" min={0} max={1} step={0.01} value={params.mutation_rate} onChange={(e) => setP({ mutation_rate: Number(e.target.value) })} /></Field>
              <Field label={t("crossover")}><input type="number" min={0} max={1} step={0.05} value={params.crossover_rate} onChange={(e) => setP({ crossover_rate: Number(e.target.value) })} /></Field>
              <Field label={lang === "en" ? "Budget (decoder calls)" : "Бюджет (вызовы декодера)"}><input type="number" min={100} max={2000000} step={1000} value={params.budget} onChange={(e) => setP({ budget: Number(e.target.value) })} /></Field>
              <Field label={lang === "en" ? "Stagnation (generations)" : "Стагнация (поколений)"}><input type="number" min={1} value={params.stagnation} onChange={(e) => setP({ stagnation: Number(e.target.value) })} /></Field>
              <Field label={t("seed")}><input type="number" min={0} value={params.seed} onChange={(e) => setP({ seed: Number(e.target.value) })} /></Field>
            </div>
            {phase === "running" ? (
              <button className="danger" onClick={() => setConfirm(true)}><Square size={16} aria-hidden="true" />{t("cancel")}</button>
            ) : (
              <button onClick={start} disabled={!methods.length || (src.kind === "paper" && !src.instance_id)}><Play size={16} aria-hidden="true" />{t("run")}</button>
            )}
          </div>
        </Panel>
        <div className="stack">
          <Panel title={lang === "en" ? "Progress and results" : "Прогресс и результаты"}
            actions={job?.result && <>
              <button className="secondary" onClick={save} disabled={!!saved}><Save size={16} aria-hidden="true" />{saved ? t("saved") : t("save")}</button>
              <button className="secondary" onClick={() => downloadBlob(`tpga-${job.id}.csv`, toCsv(job), "text/csv")}><Download size={16} aria-hidden="true" />{t("exportCsv")}</button>
              <button className="secondary" onClick={() => downloadBlob(`tpga-${job.id}.json`, JSON.stringify(job, null, 1), "application/json")}><Download size={16} aria-hidden="true" />{t("exportJson")}</button>
            </>}>
            {phase === "idle" && <State status="empty" empty={lang === "en" ? "Run a calculation to see results" : "Запустите расчёт, чтобы увидеть результаты"} />}
            {phase === "error" && <State status="error" error={error} onRetry={start} />}
            {phase === "cancelled" && <div className="notice info" role="status">{lang === "en" ? "The calculation was cancelled." : "Расчёт отменён."}</div>}
            {(phase === "running" || phase === "done") && (
              <div className="stack">
                {["LP", ...methods].map((m) => {
                  const l = live[m];
                  const budget = params.budget;
                  const frac = l?.done ? 1 : l?.evaluations ? l.evaluations / budget : l?.running ? 0.02 : 0;
                  return (
                    <div key={m}>
                      <div className="row" style={{ justifyContent: "space-between" }}>
                        <MethodLabel code={m} />
                        <span className="code-value">{l?.done ? `${num(l.done.cost, 2, lang)} · ${pct(l.done.gap_percent, lang)}` : l?.best_cost != null ? `${num(l.best_cost, 2, lang)} · ${pct(l.gap, lang)}` : ""}</span>
                      </div>
                      <Progress value={frac} label={m} />
                    </div>
                  );
                })}
                {curves.length > 0 && (
                  <LineChart series={curves.map(([m, v]) => ({ key: m, points: v.curve.filter((p) => p[1] > 0) }))} xLog yLog
                    xLabel={t("evaluations")} yLabel={lang === "en" ? "gap, %" : "отклонение, %"} height={240} />
                )}
              </div>
            )}
          </Panel>
          {results && (
            <Panel title={t("plan")} subtitle={`${job.result.problem.m} × ${job.result.problem.n} · ${t("optimum")} ${num(job.result.lp_optimum, 2, lang)}`}>
              <Bars rows={Object.entries(results).map(([m, r]) => ({ key: m, label: <MethodLabel code={m} short />, value: r.cost, color: METHOD_COLOR[m] }))} format={(v) => num(v, 2, lang)} />
              <div className="table-wrap" style={{ marginTop: 16 }}>
                <table>
                  <thead><tr><th>{t("methodsLabel")}</th><th className="num">{t("cost")}</th><th className="num">{t("gap")}</th><th className="num">{t("time")}</th><th className="num">{t("evaluations")}</th><th>stop</th></tr></thead>
                  <tbody>
                    {Object.entries(results).map(([m, r]) => (
                      <tr key={m}><td><MethodLabel code={m} short /></td><td className="num">{num(r.cost, 2, lang)}</td><td className="num">{pct(r.gap_percent, lang)}</td><td className="num">{sec(r.time_s, lang)}</td><td className="num">{r.evaluations ? num(r.evaluations, 0, lang) : "–"}</td><td className="code-value">{r.stop_reason ?? ""}</td></tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </Panel>
          )}
          <Panel title={t("history")}>
            <State status={history.status} error={history.error} onRetry={history.reload}>
              {history.data?.length ? (
                <ul className="list">
                  {history.data.map((h) => (
                    <li key={h.id} className="list-item">
                      <span style={{ flex: 1 }}>{h.title}<br /><span className="meta">{new Date(h.created_at).toLocaleString(lang === "en" ? "en-GB" : "ru-RU")}</span></span>
                      <span className="code-value">{Object.entries(h.summary).map(([m, s]) => `${m} ${pct(s.gap_percent, lang)}`).join(" · ")}</span>
                      <button className="ghost icon" aria-label={lang === "en" ? "Delete" : "Удалить"} onClick={() => api(`/history/${h.id}`, { method: "DELETE" }).then(history.reload)}><Trash2 size={16} aria-hidden="true" /></button>
                    </li>
                  ))}
                </ul>
              ) : (
                <State status="empty" />
              )}
            </State>
          </Panel>
        </div>
      </div>
      <ConfirmDialog open={confirm} title={t("cancelConfirm")} text={t("cancelConfirmText")} confirm={t("stop")} cancel={t("keepRunning")} onConfirm={cancel} onCancel={() => setConfirm(false)} />
    </>
  );
}
