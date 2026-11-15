"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import {
  Activity, ArrowDownToLine, ArrowRight, Box, ChevronLeft, ChevronRight, CircleHelp, Database,
  FlaskConical, LayoutDashboard, List, LoaderCircle, MapPin, Package, Play, Search, Settings2, TriangleAlert,
  Truck, Warehouse,
} from "lucide-react";
import { Convergence, DistrictSummary, NetworkView, format } from "./visuals";
import Geography from "./geography";
import Benchmark from "./benchmark";

const DATASETS = {
  "kazakh-wheat": { title: "Экспорт пшеницы", first: "year-2024" },
  "astana-potato": { title: "Астана · тестовая сеть", first: "day-01" },
};
const tonnes = (kg) => format(kg / 1000, 1);

const WORKSPACES = [
  { id: "overview", label: "Обзор", icon: LayoutDashboard },
  { id: "plan", label: "План поставок", icon: List },
  { id: "experiment", label: "Эксперимент", icon: FlaskConical },
];
const EVENTS = {
  warehouse_outage: ["Отключение склада", "Один склад временно недоступен"],
  district_demand_plus_35_pct: ["Рост спроса", "Сарыарка · заявки +35%"],
  incoming_tariffs_plus_30_pct: ["Рост тарифов", "Есиль и Нура · тарифы +30%"],
  api_subset: ["Пилотная выборка", "8 складов · 40 точек"],
};
const PREFS = { theme: "aspan", density: "normal", scale: "100" };
const dayLabel = (date) => new Intl.DateTimeFormat("ru-KZ", { day: "numeric", month: "long", timeZone: "UTC" })
  .format(new Date(date + "T00:00:00Z"));

async function api(path, options) {
  const response = await fetch("/api" + path, options);
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(typeof data.detail === "string" ? data.detail : "Запрос не выполнен. Повторите попытку.");
  }
  return response.json();
}

function resolveNodes(network, scenario) {
  if (!scenario.warehouse_ids) return network;
  const select = (ids, list) => ids.map((id) => list.find((node) => node.id === id));
  return { warehouses: select(scenario.warehouse_ids, network.warehouses), stores: select(scenario.store_ids, network.stores) };
}

function Sidebar({ catalog, current, choose, dataset, setDataset }) {
  const days = catalog?.scenarios.filter((item) => item.event === "daily") ?? [];
  const stresses = catalog?.scenarios.filter((item) => item.parent && item.event !== "api_subset") ?? [];
  return (
    <aside className="sidebar" aria-label="Сценарии">
      <div className="sidebar-title"><span className="square-icon"><Database size={19} /></span>
        <div><h2>Рабочий контур</h2><p>Источник и сценарий</p></div>
      </div>
      <label className="day-field">Набор данных
        <select aria-label="Набор данных" value={dataset} onChange={(e) => setDataset(e.target.value)}>
          {Object.entries(DATASETS).map(([key, value]) => <option key={key} value={key}>{value.title}</option>)}
        </select>
      </label>
      <label className="day-field">Базовый период
        <select aria-label="Базовый период" value={current?.event === "daily" ? current.id : ""} disabled={!days.length}
          onChange={(e) => choose(e.target.value)}>
          <option value="" disabled>Выберите день</option>
          {days.map((d) => <option key={d.id} value={d.id}>{d.title ?? dayLabel(d.date) + " 2026"}</option>)}
        </select>
      </label>
      <div className="sidebar-group"><span>Проверка устойчивости</span>
        {stresses.map((item) => {
          const [name, description] = EVENTS[item.event] ?? ["Стресс-сценарий", ""];
          return <button key={item.id} className="scenario-option" aria-pressed={current?.id === item.id}
            onClick={() => choose(item.id)}>
            <i className="scenario-dot" /><span><b>{item.title ?? name}</b><small>{item.note ?? description}</small></span>
            <ChevronRight size={15} />
          </button>;
        })}
      </div>
      <div className="sidebar-foot"><Database size={17} /><div><b>{DATASETS[dataset].title}</b>
        <small>{dataset === "kazakh-wheat" ? "БНС · UN Comtrade" : "Модельный датасет"}</small></div></div>
    </aside>
  );
}

function Metric({ icon: Icon, title, value, unit, note, warning, digits = 0 }) {
  return (
    <section className={"metric panel" + (warning ? " warning" : "")}>
      <div className="metric-title"><span>{title}</span><span className="square-icon"><Icon size={17} /></span></div>
      <div className="metric-value">{format(value, digits)} <small>{unit}</small></div>
      <p>{note}</p>
    </section>
  );
}

const PLAN_VIEWS = {
  shipments: { name: "Отгрузки", headings: ["Склад", "Торговая точка", "Район", "Объём, кг", "Тариф, ₸/кг", "Стоимость, ₸"] },
  stores: { name: "Дефицит", headings: ["Торговая точка", "Район", "Заявка, кг", "Поставка, кг", "Дефицит, кг"] },
  warehouses: { name: "Склады", headings: ["Склад", "Район", "Запас, кг", "Отгружено, кг", "Остаток, кг"] },
};

function downloadCsv(name, headings, rows) {
  const csv = (line) => line.map((cell) => '"' + String(cell).replaceAll('"', '""') + '"').join(";");
  const blob = new Blob(["\ufeff" + [csv(headings), ...rows.map((row) => csv(row.cells))].join("\r\n")], {
    type: "text/csv;charset=utf-8",
  });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = name + ".csv";
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function PlanTable({ result, nodes, districts, scenarioId, wheat }) {
  const [view, setView] = useState("shipments");
  const [algorithm, setAlgorithm] = useState("lp");
  const [query, setQuery] = useState("");
  const [district, setDistrict] = useState("");
  const [page, setPage] = useState(0);
  const plan = result[algorithm] ?? result.lp;
  const labels = Object.fromEntries(districts.map((d) => [d.id, d.name]));
  const headings = wheat ? {
    shipments: ["Регион", "Рынок", "Город на карте", "Объём, т", "Тариф, ₸/т", "Стоимость, ₸"],
    stores: ["Рынок", "Город на карте", "Объём, т", "Поставка, т", "Дефицит, т"],
    warehouses: ["Регион", "Город на карте", "Доступно, т", "Отгружено, т", "Остаток, т"],
  }[view] : PLAN_VIEWS[view].headings;
  const filterOptions = wheat && view === "warehouses" ? nodes.warehouses : districts;
  const entries = useMemo(() => {
    const mass = (kg) => wheat ? kg / 1000 : kg;
    if (view === "stores") {
      return plan.stores.map((item, index) => ({ item, node: nodes.stores[index] }))
        .filter(({ item }) => item.deficit_kg > .01)
        .sort((a, b) => b.item.deficit_kg - a.item.deficit_kg)
        .map(({ item, node }) => ({
          id: node.id, district: node.district,
          cells: [node.name ?? node.id, node.city ?? labels[node.district], mass(item.demand_kg), mass(item.received_kg), mass(item.deficit_kg)],
        }));
    }
    if (view === "warehouses") {
      return plan.warehouses.map((item, index) => {
        const node = nodes.warehouses[index];
        return { id: node.id, district: node.district, cells: [node.name ?? node.id, node.city ?? labels[node.district], mass(item.supply_kg), mass(item.shipped_kg), mass(item.unused_kg)] };
      });
    }
    return [...plan.shipments].sort((a, b) => b.kg - a.kg).map((item) => {
      const store = nodes.stores[item.store], warehouse = nodes.warehouses[item.warehouse];
      return { id: warehouse.id + ":" + store.id, district: store.district,
        cells: [warehouse.name ?? warehouse.id, store.name ?? store.id, store.city ?? labels[store.district], mass(item.kg), wheat ? item.tariff * 1000 : item.tariff, item.cost_kzt] };
    });
  }, [plan, nodes, view, districts, wheat]);
  const search = query.trim().toLowerCase();
  const filtered = entries.filter((row) => (!district || district === row.district) &&
    (!search || row.cells.slice(0, view === "shipments" ? 3 : 2).some((value) => value.toLowerCase().includes(search))));
  const size = 12, pages = Math.max(1, Math.ceil(filtered.length / size)), current = Math.min(page, pages - 1);
  const change = (setter, value) => { setter(value); setPage(0); };
  return (
    <section className="panel plan-panel">
      <div className="panel-head"><div><h2>Ведомость поставок</h2><p>Объёмы, тарифы и остатки по выбранному сценарию</p></div>
        <button className="secondary" disabled={!filtered.length} onClick={() => downloadCsv(scenarioId + "-" + view, headings, filtered)}>
          <ArrowDownToLine size={17} /> CSV
        </button>
      </div>
      <div className="table-actions">
        <div className="segment" aria-label="Раздел ведомости">
          {Object.entries(PLAN_VIEWS).map(([id, item]) => <button key={id} aria-pressed={view === id}
            onClick={() => { change(setView, id); setDistrict(""); }}>{wheat && id === "warehouses" ? "Регионы" : item.name}</button>)}
        </div>
        <div className="filters">
          {result.ga && <select value={algorithm} onChange={(e) => change(setAlgorithm, e.target.value)} aria-label="Алгоритм плана">
            <option value="lp">Точный план</option><option value="ga_before">ГА до</option><option value="ga">ГА после</option>
          </select>}
          <label className="search"><Search size={16} /><input placeholder={wheat ? "Рынок или город" : "Поиск по коду"} aria-label="Поиск по ведомости"
            value={query} onChange={(e) => change(setQuery, e.target.value)} /></label>
          <select value={district} onChange={(e) => change(setDistrict, e.target.value)} aria-label="Район">
            <option value="">{wheat ? "Все направления" : "Все районы"}</option>{filterOptions.map((d) => <option key={d.id} value={d.id}>{d.name}</option>)}
          </select>
        </div>
      </div>
      <div className="table-scroll">
        <table>
          <thead><tr>{headings.map((label) => <th key={label}>{label}</th>)}</tr></thead>
          <tbody>{filtered.slice(current * size, (current + 1) * size).map((row) => <tr key={row.id}>
            {row.cells.map((value, index) => <td key={index} className={(typeof value === "number" || value.startsWith("W-") || value.startsWith("S-") ? "code-value" : "") +
              (view === "stores" && index === 4 ? " deficit-text" : "")}>
              {typeof value === "number" ? format(value, 2) : value}</td>)}
          </tr>)}</tbody>
        </table>
        {!filtered.length && <p className="empty-table">{view === "stores" && !entries.length ? "По этому плану дефицита нет." : "По фильтрам ничего не найдено."}</p>}
      </div>
      <div className="pagination">
        <span>{filtered.length ? format(current * size + 1) + "–" + format(Math.min((current + 1) * size, filtered.length)) + " из " + format(filtered.length) : "0 строк"}</span>
        <div><button className="icon-button" aria-label="Предыдущая страница" disabled={!current} onClick={() => setPage(current - 1)}><ChevronLeft size={18} /></button>
          <button className="icon-button" aria-label="Следующая страница" disabled={current >= pages - 1} onClick={() => setPage(current + 1)}><ChevronRight size={18} /></button></div>
      </div>
    </section>
  );
}

function Experiment({ result, config, setConfig, busy, error, run, goPlan, wheat }) {
  const ga = result.ga, before = result.ga_before, lp = result.lp;
  const fields = [
    ["population", "Популяция", 8, 80], ["generations", "Поколения", 5, 150], ["seed", "Seed", 0, 4294967295],
  ];
  const scale = wheat ? 1000 : 1, unit = wheat ? "т" : "кг";
  const comparison = [
    ["Стоимость, ₸", lp.cost_kzt, before?.cost_kzt, ga?.cost_kzt, 2],
    ["Поставлено, " + unit, lp.delivered_kg / scale, before?.delivered_kg / scale, ga?.delivered_kg / scale, wheat ? 1 : 0],
    ["Дефицит, " + unit, lp.deficit_kg / scale, before?.deficit_kg / scale, ga?.deficit_kg / scale, wheat ? 1 : 0],
    ["Время, с", lp.runtime_s, before?.runtime_s, ga?.runtime_s, 3],
  ];
  return <>
    <section className="panel experiment-controls">
      <div className="panel-head"><div><h2>Новый прогон</h2>
        <p>Обе версии ГА используют один бюджет. HiGHS задаёт точный эталон для тех же входных данных.</p></div>
        <span className="square-icon"><FlaskConical size={19} /></span>
      </div>
      <form onSubmit={(e) => { e.preventDefault(); run(); }}>
        {fields.map(([id, label, min, max]) => <label key={id}>{label}
          <input type="number" min={min} max={max} step="1" required disabled={busy} value={config[id]}
            onChange={(e) => setConfig({ ...config, [id]: e.target.value })} />
        </label>)}
        <button className="primary" type="submit" disabled={busy}>
          {busy ? <LoaderCircle size={17} className="spin" /> : <Play size={17} />} {busy ? "Идёт расчёт…" : "Сравнить алгоритмы"}
        </button>
      </form>
      {error && <p className="error-text" role="alert">{error}</p>}
    </section>
    {ga ? <div className="overview-grid">
      <Convergence history={ga.history} before={before.history} optimum={lp.cost_kzt} />
      <section className="panel comparison">
        <div className="panel-head"><div><h2>Сравнение решений</h2><p>Случайный старт и старт с учётом затрат</p></div></div>
        <div className="comparison-gap"><span>Отклонение от оптимума</span>
          <strong>{ga.gap_percent == null ? "—" : format(before.gap_percent, 2) + "% → " + format(ga.gap_percent, 2) + "%"}</strong>
        </div>
        <div className="table-scroll"><table>
          <thead><tr><th>Метрика</th><th>HiGHS</th><th>ГА до</th><th>ГА после</th></tr></thead>
          <tbody>{comparison.map(([name, a, b, c, digits]) => <tr key={name}><td>{name}</td>
            <td className="code-value">{format(a, digits)}</td><td className="code-value">{format(b, digits)}</td>
            <td className="code-value">{format(c, digits)}</td></tr>)}</tbody>
        </table></div>
        <p className="panel-note">Seed {ga.seed} · {format(ga.evaluations)} оценок</p>
        <button className="text-button" onClick={goPlan}>Смотреть планы <ArrowRight size={16} /></button>
      </section>
    </div> : <section className="panel experiment-empty" aria-live="polite">
      <span className="square-icon">{busy ? <LoaderCircle className="spin" size={20} /> : <Activity size={20} />}</span>
      <div><h2>{busy ? "Идёт сравнение" : "Сравнение готово к запуску"}</h2>
        <p>{busy ? "Выполняются оба прогона ГА на выбранном сценарии." : "После расчёта здесь появятся метрики обоих решений и график сходимости."}</p></div>
    </section>}
  </>;
}

function Markets({ nodes, plan, market, selectMarket }) {
  const highest = Math.max(...plan.stores.map((row) => row.demand_kg), 1);
  return <section className="panel markets">
    <div className="panel-head"><div><h2>Рынки назначения</h2><p>Поставка / объём сценария, т</p></div>
      <span className="square-icon"><Truck size={18} /></span></div>
    <div className="market-list">
      {nodes.stores.map((node, i) => {
        const item = plan.stores[i];
        return <button key={node.id} className="market-row" aria-pressed={market === node.id}
          onClick={() => selectMarket(market === node.id ? "" : node.id)}>
          <span className="market-top"><b>{node.name}</b><span className="market-code">{node.id}</span></span>
          <span className="market-quantities code-value">{tonnes(item.received_kg)} <small>/ {tonnes(item.demand_kg)}</small></span>
          <span className="market-track" style={{ width: (item.demand_kg ? Math.max(4, 100 * item.demand_kg / highest) : 0) + "%" }}>
            <i style={{ width: (item.demand_kg ? 100 * item.received_kg / item.demand_kg : 0) + "%" }} />
          </span>
        </button>;
      })}
    </div>
  </section>;
}

function Evidence({ catalog, wheat }) {
  return <details className="panel evidence">
    <summary>Источники и допущения модели</summary>
    <p>{wheat
      ? "Экспорт по странам взят из торговой статистики. Доступный объём распределён по долям урожая областей. Тарифы оценены по расстоянию между городами, фактические тарифы и маршруты перевозчиков не использовались."
      : "Склады, точки, объёмы и тарифы смоделированы. Данные акимата использованы для масштаба сети по районам."}</p>
    <ul>{catalog.sources.map((source) => <li key={source.url}><a href={source.url} target="_blank" rel="noreferrer">
      {source.title ?? new URL(source.url).hostname}</a></li>)}</ul>
  </details>;
}

export default function Dashboard() {
  const [dataset, setDataset] = useState("kazakh-wheat");
  const [catalogState, setCatalog] = useState(null);
  const [benchmark, setBenchmark] = useState(null);
  const catalog = catalogState?.key === dataset ? catalogState.data : null;
  const wheat = dataset === "kazakh-wheat";
  const query = "?dataset_id=" + dataset;
  const [catalogError, setCatalogError] = useState("");
  const [retry, setRetry] = useState(0);
  const [id, setId] = useState(DATASETS["kazakh-wheat"].first);
  const [tab, setTab] = useState("overview");
  const [district, setDistrict] = useState("");
  const [prefs, setPrefs] = useState(PREFS);
  const [result, setResult] = useState(null);
  const [loadError, setLoadError] = useState("");
  const [busy, setBusy] = useState(false);
  const [experimentError, setExperimentError] = useState("");
  const [config, setConfig] = useState({ population: 32, generations: 60, seed: 42 });
  const experiment = useRef(null);
  const scenario = catalog?.scenarios.find((item) => item.id === id);
  const nodes = useMemo(() => scenario && resolveNodes(catalog.network, scenario), [catalog, scenario]);
  const current = result?.scenario_id === id && result.key === dataset ? result : null;
  const lp = current?.lp;

  useEffect(() => {
    try {
      const stored = JSON.parse(localStorage.getItem("tpga-ui") || "{}");
      setPrefs({
        theme: ["aspan", "astana"].includes(stored.theme) ? stored.theme : PREFS.theme,
        density: ["compact", "normal", "relaxed"].includes(stored.density) ? stored.density : PREFS.density,
        scale: ["93.3", "100", "113.3"].includes(stored.scale) ? stored.scale : PREFS.scale,
      });
    } catch { /* Preferences can be unavailable in private storage contexts. */ }
  }, []);

  useEffect(() => {
    const controller = new AbortController();
    setCatalogError("");
    setBenchmark(null);
    api("/scenarios" + query, { signal: controller.signal })
      .then((data) => { if (!controller.signal.aborted) setCatalog({ key: dataset, data }); })
      .catch((error) => { if (!controller.signal.aborted) setCatalogError(error.message); });
    api("/scenarios/benchmark" + query, { signal: controller.signal })
      .then((data) => { if (!controller.signal.aborted) setBenchmark({ key: dataset, data }); })
      .catch(() => {});
    return () => controller.abort();
  }, [dataset, query, retry]);

  useEffect(() => {
    const controller = new AbortController();
    setLoadError("");
    setResult(null);
    api("/scenarios/" + id + "/plan" + query, {
      method: "POST", headers: { "Content-Type": "application/json" }, body: "{}", signal: controller.signal,
    }).then((data) => { if (!controller.signal.aborted) setResult({ ...data, key: dataset }); }).catch((error) => {
      if (!controller.signal.aborted) setLoadError(error.message);
    });
    return () => controller.abort();
  }, [dataset, id, query, retry]);

  function choose(next) {
    if (next === id) return;
    experiment.current?.abort();
    setBusy(false);
    setExperimentError("");
    setDistrict("");
    setId(next);
  }

  function chooseDataset(next) {
    if (next === dataset) return;
    choose(DATASETS[next].first);
    setDataset(next);
  }

  function preference(name, value) {
    const updated = { ...prefs, [name]: value };
    setPrefs(updated);
    try { localStorage.setItem("tpga-ui", JSON.stringify(updated)); } catch { /* Keep session settings. */ }
  }

  async function run() {
    if (busy) return;
    const controller = new AbortController();
    experiment.current = controller;
    setBusy(true);
    setExperimentError("");
    try {
      const payload = Object.fromEntries(Object.entries(config).map(([key, value]) => [key, Number(value)]));
      const data = await api("/scenarios/" + id + "/plan" + query, {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...payload, compare: true }), signal: controller.signal,
      });
      if (!controller.signal.aborted) setResult({ ...data, key: dataset });
    } catch (error) {
      if (!controller.signal.aborted) setExperimentError(error.message);
    } finally {
      if (experiment.current === controller) { experiment.current = null; setBusy(false); }
    }
  }

  return (
    <div className="shell export-shell" data-theme={prefs.theme} data-density={prefs.density} data-scale={prefs.scale}>
      <header className="topbar">
        <div className="brand"><span className="brand-logo"><Box size={21} /></span><span><b>tp-ga</b><small>Контур поставок</small></span></div>
        <nav className="main-nav" aria-label="Рабочие разделы">
          {WORKSPACES.map(({ id: value, label, icon: Icon }) => <button key={value}
            aria-current={tab === value ? "page" : undefined} onClick={() => setTab(value)}><Icon size={17} />{label}</button>)}
        </nav>
        <details className="settings">
          <summary aria-label="Настройки интерфейса"><Settings2 size={19} /><span>Настройки</span></summary>
          <div className="settings-menu">
            <label>Тема<select aria-label="Тема" value={prefs.theme} onChange={(e) => preference("theme", e.target.value)}>
              <option value="aspan">Aspan</option><option value="astana">Astana</option></select></label>
            <label>Строки таблиц<select aria-label="Строки таблиц" value={prefs.density} onChange={(e) => preference("density", e.target.value)}>
              <option value="compact">Компактные</option><option value="normal">Обычные</option><option value="relaxed">Просторные</option>
            </select></label>
            <label>Масштаб текста<select aria-label="Масштаб текста" value={prefs.scale} onChange={(e) => preference("scale", e.target.value)}>
              <option value="93.3">93,3%</option><option value="100">100%</option><option value="113.3">113,3%</option>
            </select></label>
          </div>
        </details>
      </header>
      <div className="workspace">
        <Sidebar catalog={catalog} current={scenario} choose={choose} dataset={dataset} setDataset={chooseDataset} />
        <main className="main">
          <div className="page-head export-head">
            <div><div className="eyebrow"><MapPin size={15} /> {wheat ? "Казахстан · внешняя торговля" : "Астана · модель поставок"}</div>
              <h1>{tab === "plan" ? "План поставок" : tab === "experiment" ? "Сравнение алгоритмов" : DATASETS[dataset].title}</h1>
              <p>{scenario ? scenario.title ?? (EVENTS[scenario.event]?.[0] ?? "Дневной сценарий") + " · " + dayLabel(scenario.date) :
                "Выберите сценарий поставок"}</p></div>
            {scenario && <span className="pill"><Database size={14} /> {scenario.warehouse_count} × {scenario.store_count}<span className="pill-divider" />
              {catalog.display.badge ?? "Модельные данные"}</span>}
          </div>
          {catalogError || loadError ? <section className="panel status-panel" role="alert">
            <TriangleAlert size={22} /><div><h2>Данные не загрузились</h2><p>{catalogError || loadError}</p></div>
            <button className="secondary" onClick={() => setRetry(retry + 1)}>Повторить</button>
          </section> : !lp || !nodes ? <section className="panel status-panel" role="status">
            <LoaderCircle className="spin" size={22} /><div><h2>Рассчитываем точный план</h2><p>Подготавливаем ведомость и сводку по районам.</p></div>
          </section> : <>
            <div className="metrics">
              <Metric icon={Package} title={wheat ? "Объём сценария" : "Спрос"} value={scenario.demand_kg / (wheat ? 1000 : 1)}
                unit={wheat ? "т" : "кг"} digits={wheat ? 1 : 0} note={format(scenario.store_count) + (wheat ? " экспортных рынков" : " торговых точек")} />
              <Metric icon={Truck} title="К поставке" value={lp.delivered_kg / (wheat ? 1000 : 1)} unit={wheat ? "т" : "кг"} digits={wheat ? 1 : 0}
                note={scenario.demand_kg ? format(100 * lp.delivered_kg / scenario.demand_kg, 1) + "% заявленного объёма" : "Нет заявок"} />
              <Metric icon={TriangleAlert} title="Дефицит" value={lp.deficit_kg / (wheat ? 1000 : 1)} unit={wheat ? "т" : "кг"} digits={wheat ? 1 : 0} warning={lp.deficit_kg > .01}
                note={lp.deficit_kg > .01 ? format(lp.stores.filter((item) => item.deficit_kg > .01).length) + " точек с непокрытой заявкой" : "Все заявки покрыты"} />
              <Metric icon={Warehouse} title={wheat ? "Расчётный минимум" : "Точная стоимость"} value={lp.cost_kzt / (wheat ? 1e9 : 1)}
                unit={wheat ? "млрд ₸" : "₸"} digits={wheat ? 2 : 0} note={format(lp.shipments.length) + " направлений с отгрузкой"} />
            </div>
            {tab === "overview" && <>
              {wheat ? <div className="export-grid">
                <Geography nodes={nodes} plan={lp} market={district} selectMarket={setDistrict} />
                <Markets nodes={nodes} plan={lp} market={district} selectMarket={setDistrict} />
              </div> : <div className="overview-grid">
                <NetworkView network={catalog.network} nodes={nodes} plan={lp} district={district} onDistrict={setDistrict} />
                <DistrictSummary districts={catalog.network.districts} nodes={nodes} plan={lp} district={district} onDistrict={setDistrict} />
              </div>}
              <section className="panel insight"><span className="square-icon"><CircleHelp size={19} /></span>
                <div><h2>{lp.deficit_kg > .01 ? "План покрывает часть объёма" : wheat ? "План покрывает весь объём сценария" : "Запаса хватает на все заявки"}</h2>
                  <p>{scenario.note ?? (lp.deficit_kg > .01 ? "Откройте вкладку «Дефицит» в ведомости, чтобы увидеть недопоставку по точкам." :
                    "В ведомости можно проверить объёмы отгрузок, тарифы и остатки по складам.")}</p></div>
                <button className="secondary" onClick={() => setTab("plan")}>Открыть ведомость <ArrowRight size={16} /></button>
              </section>
              <Evidence catalog={catalog} wheat={wheat} />
            </>}
            {tab === "plan" && <PlanTable key={id} result={current} nodes={nodes} districts={catalog.network.districts} scenarioId={id} wheat={wheat} />}
            {tab === "experiment" && <>
              <Benchmark report={benchmark?.key === dataset ? benchmark.data : null} scenarios={catalog.scenarios} choose={choose} dataset={dataset} />
              <Experiment result={current} config={config} setConfig={setConfig} busy={busy}
                error={experimentError} run={run} goPlan={() => setTab("plan")} wheat={wheat} />
            </>}
          </>}
          <footer><span>tp-ga · {wheat ? "Казахстан" : "Астана"}</span><span>{scenario && format(scenario.direction_count) + " направлений в задаче"}</span></footer>
        </main>
      </div>
    </div>
  );
}

