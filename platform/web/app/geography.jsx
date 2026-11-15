"use client";

import { useEffect, useRef, useState } from "react";
import { ArrowUpRight, Focus, Layers3, MapPin, Route, TrainFront } from "lucide-react";
import { format } from "./visuals";

const BOUNDS = [[34.6, 45.8], [57.2, 92.6]];
const MARKET_COLOR = "#ac671f";
const ROUTE_COLOR = "#12636d";
const REGION_COLOR = "#1f5984";

function textElement(text, className) {
  const element = document.createElement("span");
  element.textContent = text;
  if (className) element.className = className;
  return element;
}

function curve(a, b) {
  const middle = [(a.lat + b.lat) / 2 + Math.min(3.0, Math.abs(a.lon - b.lon) * .11), (a.lon + b.lon) / 2];
  return Array.from({ length: 25 }, (_, index) => {
    const t = index / 24, u = 1 - t;
    return [u * u * a.lat + 2 * t * u * middle[0] + t * t * b.lat, u * u * a.lon + 2 * t * u * middle[1] + t * t * b.lon];
  });
}

export default function Geography({ nodes, plan, market, selectMarket }) {
  const element = useRef(null);
  const map = useRef(null);
  const [ready, setReady] = useState(false);
  const [error, setError] = useState(false);
  const [expanded, setExpanded] = useState(false);
  const [rail, setRail] = useState(true);
  const [crossings, setCrossings] = useState(null);
  const [crossingId, setCrossingId] = useState("");
  const active = crossings?.features.find(({ properties }) => properties.id === crossingId);
  const selected = market && nodes.stores.find((node) => node.id === market);
  const shipments = plan.shipments.filter((row) => !market || nodes.stores[row.store].id === market);
  const displayed = [...shipments].sort((a, b) => b.kg - a.kg).slice(0, expanded ? shipments.length : 10);

  useEffect(() => {
    const controller = new AbortController();
    let instance;
    Promise.all([
      import("leaflet"),
      fetch("/maps/rail-crossings.json", { signal: controller.signal })
        .then((response) => response.ok ? response.json() : null).catch(() => null),
      fetch("/maps/eurasia.json", { signal: controller.signal }).then((response) => {
        if (!response.ok) throw new Error("map data");
        return response.json();
      }),
    ]).then(([module, railData, countries]) => {
      if (controller.signal.aborted) return;
      const L = module.default ?? module;
      instance = L.map(element.current, { zoomControl: false, attributionControl: false, scrollWheelZoom: false, minZoom: 2, maxZoom: 11, zoomSnap: .25 });
      L.control.zoom({ position: "topright", zoomInTitle: "Приблизить", zoomOutTitle: "Отдалить" }).addTo(instance);
      L.geoJSON(countries, {
        interactive: false,
        style: (feature) => ({
          color: feature.properties.id === "KAZ" ? "#74998d" : "#cad6d6",
          weight: feature.properties.id === "KAZ" ? 1.6 : .85,
          fillColor: feature.properties.id === "KAZ" ? "#d9e8d9" : "#eff0e9",
          fillOpacity: 1,
        }),
      }).addTo(instance);
      const labels = [
        [48.5, 66.5, "КАЗАХСТАН"], [54.9, 76, "РОССИЯ"], [44.7, 94.1, "КИТАЙ"], [37, 56, "ИРАН"],
      ];
      for (const [lat, lon, name] of labels) {
        L.marker([lat, lon], {
          interactive: false, keyboard: false, zIndexOffset: -100,
          icon: L.divIcon({ className: "map-country-name" + (name === "КАЗАХСТАН" ? "" : " neighbor-label"),
            html: name, iconSize: [140, 20], iconAnchor: [70, 10] }),
        }).addTo(instance);
      }
      map.current = { instance, L, overlay: L.layerGroup().addTo(instance) };
      instance.fitBounds(BOUNDS, { padding: [16, 18] });
      setCrossings(railData);
      setReady(true);
    }).catch(() => {
      if (!controller.signal.aborted) setError(true);
    });
    return () => {
      controller.abort();
      instance?.remove();
      map.current = null;
    };
  }, []);

  useEffect(() => {
    if (!ready || !map.current) return;
    const { L, overlay } = map.current;
    overlay.clearLayers();
    if (rail) {
      for (const feature of crossings?.features ?? []) {
        const { id, stations } = feature.properties;
        const points = feature.geometry.coordinates.map(([lon, lat]) => [lat, lon]);
        const center = points[Math.floor(points.length / 2)];
        const jump = () => {
          setCrossingId(id);
          map.current.instance.fitBounds(L.latLngBounds(points), { padding: [40, 55], maxZoom: 11 });
        };
        L.polyline(points, { color: "#fff", weight: 8, opacity: .9, interactive: false }).addTo(overlay);
        L.polyline(points, { color: "#176059", weight: 4 })
          .bindTooltip(textElement(stations.join(" — "))).on("click", jump).addTo(overlay);
        if (id === crossingId) {
          [points[0], points.at(-1)].forEach((point, i) => {
            L.circleMarker(point, { radius: 5, fillColor: "#176059", color: "#fff", weight: 2, fillOpacity: 1 })
              .bindTooltip(textElement(stations[i]), { permanent: true, direction: i ? "bottom" : "top",
                offset: [0, i ? 7 : -7], className: "map-label" }).addTo(overlay);
          });
        } else {
          L.marker(center, {
            title: stations.join(" — "),
            icon: L.divIcon({ className: "rail-dot", html: "↔", iconSize: [24, 24], iconAnchor: [12, 12] }),
          }).bindTooltip(textElement(stations.join(" — "))).on("click", jump).addTo(overlay);
        }
      }
      return;
    }
    const maximum = Math.max(...plan.shipments.map((row) => row.kg), 1);
    for (const row of displayed) {
      const origin = nodes.warehouses[row.warehouse], target = nodes.stores[row.store];
      L.polyline(curve(origin, target), {
        color: ROUTE_COLOR, weight: 1.1 + 7 * Math.sqrt(row.kg / maximum),
        opacity: .64, lineCap: "round", dashArray: "5 7",
      }).bindTooltip(textElement(origin.city + " → " + target.city + " · " + format(row.kg / 1000, 1) + " т"), { sticky: true })
        .on("click", () => selectMarket(target.id)).addTo(overlay);
    }
    nodes.warehouses.forEach((node, i) => {
      const data = plan.warehouses[i];
      L.circleMarker([node.lat, node.lon], { radius: data.shipped_kg ? 4.2 : 3.1, color: "#fff", weight: 1.5,
        fillColor: REGION_COLOR, fillOpacity: data.shipped_kg ? 1 : .4 })
        .bindTooltip(textElement(node.city + " · " + format(data.shipped_kg / 1000, 1) + " т отгружено")).addTo(overlay);
    });
    nodes.stores.forEach((node, i) => {
      const data = plan.stores[i], active = !market || market === node.id;
      const marker = L.circleMarker([node.lat, node.lon], {
        radius: market === node.id ? 7.5 : 5.5, color: "#fff", weight: 2,
        fillColor: data.deficit_kg > .01 ? "#ab431c" : MARKET_COLOR, fillOpacity: active ? 1 : .42,
      }).bindTooltip(textElement(node.city + " · " + format(data.received_kg / 1000, 1) + " т"), { direction: "top" });
      if (i < 3 || market === node.id) {
        marker.unbindTooltip().bindTooltip(textElement(node.city), {
          direction: i === 1 ? "bottom" : "top", permanent: true, offset: [0, i === 1 ? 6 : -6], className: "map-label",
        });
      }
      marker.on("click", () => selectMarket(market === node.id ? "" : node.id)).addTo(overlay);
    });
  }, [ready, nodes, plan, market, expanded, selectMarket, rail, crossings, crossingId]); // displayed is derived from these inputs.

  const reset = () => {
    setCrossingId("");
    map.current?.instance.fitBounds(BOUNDS, { padding: [16, 18] });
  };
  const choose = (feature) => {
    setCrossingId(feature.properties.id);
    const { L, instance } = map.current;
    instance.fitBounds(L.latLngBounds(feature.geometry.coordinates.map(([lon, lat]) => [lat, lon])),
      { padding: [40, 55], maxZoom: 11 });
  };

  return <section className="panel geographic">
    <div className="map-heading">
      <div><span className="map-kicker"><MapPin size={14} /> География поставок</span>
        <h2>{rail ? "Железнодорожные переходы" : "Экспортные направления"}</h2>
        <p>{rail ? "Участки между пограничными станциями" :
          selected ? selected.name + " · " + selected.city : "Регионы Казахстана и рынки назначения"}</p>
      </div>
      <button className="secondary map-reset" onClick={reset}
        disabled={!ready} aria-label="Сбросить масштаб карты"><Focus size={17} /><span>Вся сеть</span></button>
    </div>
    <div className="geo-mode-switch" role="group" aria-label="Слой карты">
      <button type="button" aria-pressed={rail} onClick={() => { setRail(true); reset(); }}>
        <TrainFront size={15} /> Ж/д переходы</button>
      <button type="button" aria-pressed={!rail} onClick={() => { setRail(false); reset(); }}>
        <Route size={15} /> План модели</button>
    </div>
    <div className="geo-stage">
      <div ref={element} className="geo-map" aria-label="Карта экспортных направлений" />
      {!ready && <p className="map-status" role="status">{error ? "Карта недоступна. Обновите страницу." : "Загружаем границы стран…"}</p>}
      {ready && <div className="map-overlay"><Layers3 size={15} /><span>{rail ?
        (active ? active.properties.stations.join(" — ") : crossings ? crossings.features.length + " перехода" : "Слой недоступен") :
        displayed.length + " из " + shipments.length + " направлений"}</span></div>}
      <div className="map-attribution"><a href="https://www.naturalearthdata.com/about/terms-of-use/" target="_blank" rel="noreferrer">Natural Earth</a>
        {rail && crossings && <> · <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noreferrer">© OpenStreetMap contributors</a></>}
      </div>
    </div>
    {rail ? <>
      <div className="rail-crossings" aria-label="Переходы на карте">
        {crossings?.features.map((feature) => {
          const info = feature.properties;
          return <button key={info.id} type="button" aria-pressed={crossingId === info.id} onClick={() => choose(feature)}>
            <TrainFront size={16} /><span><strong>{info.stations.join(" — ")}</strong><small>{info.country}</small></span>
          </button>;
        })}
      </div>
      <p className="map-note">Линии проходят по путям OpenStreetMap. Полные маршруты вагонов по накладным пока не загружены.</p>
      {active && <p className="rail-source">
        <a href={active.properties.source} target="_blank" rel="noreferrer">Источник по переходу <ArrowUpRight size={13} /></a>
        {active.properties.shipment && <a href={active.properties.shipment} target="_blank" rel="noreferrer">
          Отправки пшеницы через этот переход <ArrowUpRight size={13} /></a>}
      </p>}
      <details className="rail-evidence">
        <summary>Фактические отправки, тарифы и экономия</summary>
        <p>КТЖ сообщили о восьми составах и свыше 15 тыс. тонн пшеницы во Вьетнам в мае–июле 2025 года через Достык и Алтынколь. Отправление: Азат, Акколь и Кокшетау; конечный пункт: Хайфон.</p>
        <p><strong>Экономия пока не рассчитана.</strong> В открытой публикации нет сумм по накладным и ставок на альтернативные маршруты. Стоимость в сценариях рассчитана по модели.</p>
        <div className="rail-source">
          <a href="https://ktzh-gp.kz/en/media/news/news_main_section_ru/25333/" target="_blank" rel="noreferrer">Публикация КТЖ об отправках <ArrowUpRight size={13} /></a>
          <a href="https://ktzh-gp.kz/ru/activity/tariff-policy/cargo-transportation/" target="_blank" rel="noreferrer">Прейскуранты КТЖ <ArrowUpRight size={13} /></a>
        </div>
      </details>
    </> : <>
    <div className="map-footer">
      <div className="map-key"><span><i className="origin-key" /> Регион</span>
        <span><i className="market-key" /> Рынок</span><span><i className="route-key" /> Поток по модели</span></div>
      <button className="secondary map-mode" aria-pressed={expanded} onClick={() => setExpanded(!expanded)}>
        <Route size={15} />{expanded ? "Крупнейшие" : "Все потоки"}
      </button>
    </div>
    <p className="map-note">Пунктир показывает расчётные потоки. Он не повторяет железнодорожные пути.</p>
    </>}
  </section>;
}

