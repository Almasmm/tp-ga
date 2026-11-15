"use client";

import dynamic from "next/dynamic";
import { useCallback, useMemo, useState } from "react";
import { Info, TriangleAlert } from "lucide-react";
import { useSettings } from "../providers";
import { api } from "../lib/api";
import { useAsync } from "../lib/use-async";
import { METHOD_NAME, num, pct } from "../lib/format";
import { MethodLabel, PageHead, Panel, Segmented, State } from "../components/ui";

const FlowMap = dynamic(() => import("./flow-map"), { ssr: false });
const PLAN_METHODS = ["LP", "VAM", "GA-rand", "GA-cost"];

function buildNodes(context, network, meta, problem, lang) {
  if (context === "wheat") {
    return {
      sources: network.warehouses.map((w, i) => ({ lat: w.lat, lon: w.lon, label: lang === "en" ? w.id : w.name, volume: problem.supply[i] })),
      targets: network.stores.map((s, j) => ({ lat: s.lat, lon: s.lon, label: lang === "en" ? s.id : s.name, volume: problem.demand[j] })),
    };
  }
  if (context === "astana") {
    return {
      sources: network.warehouses.map((w, i) => ({ x: w.x_km, y: w.y_km, label: w.id, volume: problem.supply[i] })),
      targets: network.stores.map((s, j) => ({ x: s.x_km, y: s.y_km, label: s.id, volume: problem.demand[j] })),
    };
  }
  const c = meta.coordinates;
  return {
    sources: c.sources.map(([x, y], i) => ({ x, y, label: `A${i + 1}`, volume: problem.supply[i] })),
    targets: c.destinations.map(([x, y], j) => ({ x, y, label: `B${j + 1}`, volume: problem.demand[j] })),
  };
}

const CONTEXTS = {
  wheat: { problem: { kind: "scenario", dataset_id: "kazakh-wheat", scenario_id: "year-2024" }, dataset: "kazakh-wheat", mode: "geo", unit: "kg" },
  astana: { problem: { kind: "scenario", dataset_id: "astana-potato", scenario_id: "day-01" }, dataset: "astana-potato", mode: "plane", unit: "kg" },
  synthetic: { problem: { kind: "generated", m: 12, n: 18, seed: 7, costs: "structured" }, dataset: null, mode: "plane", unit: "u" },
};

export default function MapPage() {
  const { t, lang } = useSettings();
  const [context, setContext] = useState("wheat");
  const [method, setMethod] = useState("LP");
  const [tiles, setTiles] = useState(true);
  const [failedFor, setFailedFor] = useState(null);
  const [showCrossings, setShowCrossings] = useState(true);
  const onTilesFailed = useCallback(() => setFailedFor(context), [context]);
  const tilesFailed = failedFor === context && tiles;
  const rail = useAsync("rail", () => fetch("/maps/rail-crossings.json").then((r) => (r.ok ? r.json() : null)).catch(() => null));
  const crossings = rail.data;
  const loaded = useAsync(context, async () => {
    const ctx = CONTEXTS[context];
    const [plans, catalog] = await Promise.all([
      api("/plans", { method: "POST", body: { problem: ctx.problem, methods: PLAN_METHODS, params: { budget: 50000, seed: 0, population: 100 } } }),
      ctx.dataset ? api(`/scenarios?dataset_id=${ctx.dataset}`) : Promise.resolve(null),
    ]);
    return { plans, network: catalog?.network ?? null };
  });
  const data = loaded.data;
  const { status, error } = loaded;

  const view = useMemo(() => {
    if (!data || status !== "ok") return null;
    const { plans, network } = data;
    const res = plans.results[method];
    const nodes = buildNodes(context, network, plans.problem, plans.problem, lang);
    const flows = res.plan.map((c) => ({ from: c.row, to: c.col, quantity: c.quantity, unitCost: c.unit_cost ?? 0 }));
    return { res, nodes, flows, lp: plans.results.LP };
  }, [data, status, method, context, lang]);

  return (
    <>
      <PageHead kicker={t("navTools")} title={lang === "en" ? "Transportation problem on the map" : "Транспортная задача на карте"}
        actions={<Segmented label={lang === "en" ? "Context" : "Контекст"} value={context} onChange={setContext}
          options={[{ value: "wheat", label: t("wheat") }, { value: "astana", label: t("astana") }, { value: "synthetic", label: t("synthetic") }]} />}>
        {lang === "en"
          ? "Plans of the exact method, Vogel's method and the GA on the same instance; switch the plan to see where the cost difference comes from."
          : "Планы точного метода, метода Фогеля и ГА на одной задаче; переключайте план, чтобы увидеть, откуда берётся разница стоимости."}
      </PageHead>
      <div className="split" style={{ gridTemplateColumns: "minmax(0, 1fr) minmax(260px, 340px)" }}>
        <Panel className="map-panel" style={{ padding: 12 }}>
          <div className="row" style={{ marginBottom: 12, justifyContent: "space-between" }}>
            <Segmented label={t("plan")} value={method} onChange={setMethod} options={PLAN_METHODS.map((m) => ({ value: m, label: m }))} />
            {context === "wheat" && (
              <div className="row">
                <label className="check"><input type="checkbox" checked={showCrossings} onChange={(e) => setShowCrossings(e.target.checked)} />{t("rail")}</label>
                <label className="check"><input type="checkbox" checked={tiles} onChange={(e) => { setTiles(e.target.checked); setFailedFor(null); }} />OSM</label>
              </div>
            )}
            {context !== "wheat" && context === "astana" && <span className="badge warn">{t("modelNetwork")}</span>}
          </div>
          <div className="map-stage">
            <State status={status} error={error} onRetry={loaded.reload}>
              {view && (
                <FlowMap mode={CONTEXTS[context].mode} nodes={view.nodes} flows={view.flows} crossings={crossings}
                  showCrossings={context === "wheat" && showCrossings} tiles={context === "wheat" && tiles} unit={CONTEXTS[context].unit} onTilesFailed={onTilesFailed} />
              )}
            </State>
            {tilesFailed && (
              <div className="map-message notice" role="status"><TriangleAlert size={16} aria-hidden="true" />{t("tilesFailed")}</div>
            )}
            {view && (
              <div className="map-legend" aria-label={lang === "en" ? "Legend" : "Легенда"}>
                <div><b>{t("legendVolume")}</b></div>
                <div>{t("legendCost")}</div>
                <div className="ramp" aria-hidden="true" />
                <div className="row" style={{ justifyContent: "space-between" }}><span>min</span><span>max</span></div>
                <div style={{ marginTop: 6 }}>○ {lang === "en" ? "source (size: supply)" : "поставщик (размер — запас)"}</div>
                <div>● {lang === "en" ? "destination" : "потребитель"}</div>
              </div>
            )}
          </div>
          <p className="meta" style={{ marginTop: 10 }}>
            <Info size={13} aria-hidden="true" /> {context === "wheat" ? t("flowsNote") : context === "astana" ? t("modelNote") : lang === "en" ? "Random points on a 100 × 100 plane; costs are distance plus noise." : "Случайные точки на плоскости 100 × 100; стоимость — расстояние плюс шум."}
          </p>
        </Panel>
        <Panel title={METHOD_NAME[lang][method]}>
          {view && (
            <div className="stack">
              <div className="metric"><span className="value">{num(view.res.cost, 2, lang)}</span><span className="label">{t("cost")}</span></div>
              <div className="metric"><span className="value">{pct(view.res.gap_percent ?? 0, lang)}</span><span className="label">{t("differenceToLp")}</span></div>
              <div className="metric"><span className="value">{num(view.res.cost - view.lp.cost, 2, lang)}</span><span className="label">{lang === "en" ? "absolute difference" : "абсолютная разница"}</span></div>
              <div className="table-wrap">
                <table>
                  <thead><tr><th>{t("plan")}</th><th className="num">{t("cost")}</th><th className="num">Δ %</th></tr></thead>
                  <tbody>
                    {PLAN_METHODS.map((m) => (
                      <tr key={m}><td><MethodLabel code={m} short /></td><td className="num">{num(data.plans.results[m].cost, 2, lang)}</td><td className="num">{pct(data.plans.results[m].gap_percent ?? 0, lang)}</td></tr>
                    ))}
                  </tbody>
                </table>
              </div>
              <p className="meta">{lang === "en" ? `GA here: budget ${num(data.plans.params.budget, 0, lang)} decoder calls, seed 0 — a quick illustration, not the paper protocol.` : `ГА здесь: бюджет ${num(data.plans.params.budget, 0, lang)} вызовов декодера, seed 0 — быстрая иллюстрация, а не протокол статьи.`}</p>
            </div>
          )}
        </Panel>
      </div>
    </>
  );
}
