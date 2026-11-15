import { CircleHelp, Network, TrendingDown } from "lucide-react";

export const format = (value, digits = 0) => new Intl.NumberFormat("ru-KZ", {
  maximumFractionDigits: digits,
}).format(value);
export const DISTRICT_COLORS = ["#5286e5", "#7359c7", "#0c8a8c", "#1e9e77", "#bd782a", "#596db2"];

export function NetworkView({ network, nodes, plan, district, onDistrict }) {
  const labels = network.districts;
  const colors = Object.fromEntries(labels.map((item, i) => [item.id, DISTRICT_COLORS[i]]));
  const x = (point) => 320 + point.x_km * 23;
  const y = (point) => 162 - point.y_km * 13;
  const relevant = plan.shipments.filter((row) => !district || nodes.stores[row.store].district === district);
  const lines = [...relevant].sort((a, b) => b.kg - a.kg).slice(0, district ? 22 : 30);

  return (
    <section className="panel network-panel">
      <div className="panel-head">
        <div><h2>Схема поставок</h2><p>Условная география · крупнейшие потоки</p></div>
        <span className="square-icon"><Network size={18} /></span>
      </div>
      <div className="network-wrap">
        <svg viewBox="0 0 640 324" role="img" aria-label="Схема складов, точек и потоков поставок">
          <defs>
            <pattern id="grid" width="22" height="22" patternUnits="userSpaceOnUse">
              <circle cx="1" cy="1" r="0.9" fill="#d7e2f0" />
            </pattern>
          </defs>
          <rect width="640" height="324" rx="14" fill="url(#grid)" />
          {labels.map((label) => {
            const points = nodes.stores.filter((store) => store.district === label.id);
            if (!points.length) return null;
            const center = points.reduce((a, p) => [a[0] + x(p), a[1] + y(p)], [0, 0]);
            return <ellipse key={label.id} cx={center[0] / points.length} cy={center[1] / points.length}
              rx="55" ry="34" fill={colors[label.id]} opacity={district && district !== label.id ? .04 : .10} />;
          })}
          {lines.map((line) => {
            const from = nodes.warehouses[line.warehouse], to = nodes.stores[line.store];
            const a = x(from), b = y(from), c = x(to), d = y(to);
            return <path key={line.warehouse + ":" + line.store}
              d={["M", a, b, "Q", (a + c) / 2, Math.min(b, d) - 12, c, d].join(" ")}
              fill="none" stroke={colors[to.district]} strokeWidth={Math.min(3, .7 + line.kg / 260)} opacity=".32" />;
          })}
          {nodes.stores.map((node, i) => <circle key={node.id} cx={x(node)} cy={y(node)}
            r={plan.stores[i].deficit_kg > .01 ? 3.3 : 2.2}
            fill={plan.stores[i].deficit_kg > .01 ? "#d77238" : colors[node.district]}
            opacity={district && district !== node.district ? .12 : .88}><title>{node.id}</title></circle>)}
          {nodes.warehouses.map((node, i) => <rect key={node.id} x={x(node) - 4} y={y(node) - 4} width="8"
            height="8" rx="2" fill={plan.warehouses[i].supply_kg ? "#143b79" : "#f0a66e"}
            stroke="white" strokeWidth="1.25"><title>{node.id}</title></rect>)}
        </svg>
      </div>
      <div className="network-legend">
        <span><i className="warehouse-mark" /> Склад</span><span><i className="store-mark" /> Торговая точка</span>
        <span><i className="deficit-mark" /> Есть дефицит</span>
      </div>
      <div className="district-chips" aria-label="Фильтр схемы по районам">
        {labels.map((d) => <button key={d.id} type="button" aria-pressed={district === d.id}
          onClick={() => onDistrict(district === d.id ? "" : d.id)}>
          <i style={{ background: colors[d.id] }} />{d.name}
        </button>)}
      </div>
    </section>
  );
}

export function DistrictSummary({ districts, nodes, plan, district, onDistrict }) {
  const totals = districts.map((d, i) => {
    const districtPlan = plan.stores.filter((_, j) => nodes.stores[j].district === d.id);
    const demand = districtPlan.reduce((s, p) => s + p.demand_kg, 0);
    const delivered = districtPlan.reduce((s, p) => s + p.received_kg, 0);
    return { ...d, demand, delivered, color: DISTRICT_COLORS[i] };
  });
  return (
    <section className="panel district-panel">
      <div className="panel-head"><div><h2>Покрытие по районам</h2><p>Поставка / заявка, кг</p></div></div>
      <div className="district-list">
        {totals.map((d) => {
          const ratio = d.demand ? d.delivered / d.demand : 0;
          return <button key={d.id} aria-pressed={district === d.id}
            onClick={() => onDistrict(district === d.id ? "" : d.id)} className="district-row">
            <span><b>{d.name}</b><span className="code-value">{format(d.delivered)} <small>/ {format(d.demand)}</small></span></span>
            <span className="progress" aria-hidden="true">
              <i style={{ width: Math.min(100, ratio * 100) + "%", background: d.color }} />
            </span>
          </button>;
        })}
      </div>
      <p className="panel-note"><CircleHelp size={15} /> Нажмите на район, чтобы выделить его на схеме.</p>
    </section>
  );
}

export function Convergence({ history, before, optimum }) {
  const values = [...history, ...before, optimum], min = Math.min(...values), max = Math.max(...values);
  const lo = min - (max - min || 1) * .07, hi = max + (max - min || 1) * .07;
  const x = (i) => 112 + i / Math.max(1, history.length - 1) * 520;
  const y = (v) => 186 - (v - lo) / (hi - lo) * 151;
  const axis = new Intl.NumberFormat("ru-KZ", { notation: "compact", maximumFractionDigits: 2 });
  const path = (series) => series.map((v, i) => [x(i), y(v)].join(",")).join(" ");
  return (
    <section className="panel convergence">
      <div className="panel-head"><div><h2>Сходимость алгоритма</h2><p>Лучшая стоимость к каждому поколению, ₸</p></div>
        <span className="square-icon"><TrendingDown size={18} /></span></div>
      <svg viewBox="0 0 660 232" role="img" aria-label="Стоимость по поколениям и линия точного оптимума">
        {[0, 1, 2, 3].map((i) => {
          const value = min + (max - min) * i / 3;
          return <g key={i}>
            <line x1="112" x2="632" y1={y(value)} y2={y(value)} stroke="#e1e7f0" />
            {max !== min || !i ? <text x="101" y={y(value) + 4} textAnchor="end">{axis.format(value)}</text> : null}
          </g>;
        })}
        <line x1="112" x2="632" y1={y(optimum)} y2={y(optimum)} stroke="#0c8a8c" strokeWidth="2" strokeDasharray="5 5" />
        <polyline points={path(before)} fill="none" stroke="#a2683d" strokeWidth="2" strokeLinejoin="round" />
        <polyline points={path(history)} fill="none" stroke="#1f5fd1" strokeWidth="3" strokeLinejoin="round" />
        <text x="112" y="213" textAnchor="middle">0</text>
        <text x="632" y="213" textAnchor="end">{history.length - 1}</text>
      </svg>
      <div className="network-legend"><span><i className="before-mark" /> ГА до</span><span><i className="store-mark" /> ГА после</span>
        <span><i className="exact-mark" /> Точный оптимум</span></div>
    </section>
  );
}

