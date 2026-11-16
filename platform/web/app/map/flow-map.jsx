"use client";

import { useEffect, useRef, useState } from "react";
import { useSettings } from "../providers";
import { num } from "../lib/format";

const RAMP = ["#0072B2", "#56B4E9", "#E69F00", "#D55E00"];

function rampColor(t) {
  const x = Math.max(0, Math.min(0.9999, t)) * (RAMP.length - 1);
  const i = Math.floor(x);
  const f = x - i;
  const a = RAMP[i].match(/\w\w/g).map((h) => parseInt(h, 16));
  const b = RAMP[i + 1].match(/\w\w/g).map((h) => parseInt(h, 16));
  return "#" + a.map((v, k) => Math.round(v + (b[k] - v) * f).toString(16).padStart(2, "0")).join("");
}

function tip(text) {
  const el = document.createElement("span");
  el.textContent = text;
  return el;
}

/**
 * Leaflet map of a plan.
 * mode "geo": nodes have lat/lon, background is the Natural Earth outline, OSM tiles are optional.
 * mode "plane": nodes have x/y (km or abstract units) on L.CRS.Simple.
 */
export default function FlowMap({ mode, nodes, flows, crossings, showCrossings, tiles, unit, onTilesFailed }) {
  const { lang } = useSettings();
  const el = useRef(null);
  const ref = useRef(null);
  const [ready, setReady] = useState(false);

  useEffect(() => {
    let map;
    let cancelled = false;
    import("leaflet").then(async (mod) => {
      const L = mod.default ?? mod;
      if (cancelled || !el.current) return;
      map = L.map(el.current, {
        crs: mode === "plane" ? L.CRS.Simple : L.CRS.EPSG3857,
        zoomControl: true,
        attributionControl: true,
        scrollWheelZoom: false,
        minZoom: mode === "plane" ? -5 : 2,
        zoomSnap: 0.25,
      });
      map.attributionControl.setPrefix(false);
      if (mode === "geo") {
        const world = await fetch("/maps/eurasia.json").then((r) => (r.ok ? r.json() : null)).catch(() => null);
        if (world && !cancelled) {
          L.geoJSON(world, {
            interactive: false,
            style: (f) => ({ color: f.properties.id === "KAZ" ? "#6F8FB8" : "#B7C4D6", weight: f.properties.id === "KAZ" ? 1.4 : 0.8, fillColor: f.properties.id === "KAZ" ? "#E3EBF6" : "#F1F4F8", fillOpacity: 1 }),
          }).addTo(map);
          map.attributionControl.addAttribution('<a href="https://www.naturalearthdata.com/about/terms-of-use/" target="_blank" rel="noreferrer">Natural Earth</a>');
        }
      }
      ref.current = { L, map, layer: L.layerGroup().addTo(map), tiles: null };
      setReady(true);
    });
    return () => {
      cancelled = true;
      map?.remove();
      ref.current = null;
      setReady(false);
    };
  }, [mode]);

  // optional OSM base map; a run of tile errors removes it and reports the failure
  useEffect(() => {
    if (!ready || mode !== "geo") return undefined;
    const { L, map } = ref.current;
    if (!tiles) return undefined;
    let errors = 0;
    const layer = L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 12,
      opacity: 0.55,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noreferrer">OpenStreetMap</a>',
    });
    layer.on("tileerror", () => {
      errors += 1;
      if (errors === 3) {
        map.removeLayer(layer);
        onTilesFailed?.();
      }
    });
    layer.addTo(map).bringToBack();
    return () => map.hasLayer(layer) && map.removeLayer(layer);
  }, [ready, mode, tiles, onTilesFailed]);

  useEffect(() => {
    if (!ready) return;
    const { L, map, layer } = ref.current;
    layer.clearLayers();
    const pos = (node) => (mode === "geo" ? [node.lat, node.lon] : [node.y, node.x]);
    const all = [...nodes.sources, ...nodes.targets].map(pos);
    if (all.length) map.fitBounds(L.latLngBounds(all), { padding: [30, 30] });
    if (showCrossings && crossings) {
      for (const f of crossings.features) {
        const pts = f.geometry.coordinates.map(([lon, lat]) => [lat, lon]);
        L.polyline(pts, { color: "#ffffff", weight: 8, opacity: 0.9, interactive: false }).addTo(layer);
        L.polyline(pts, { color: "#0B2552", weight: 4 }).bindTooltip(tip(f.properties.stations.join(" — ")), { className: "tp-tip" }).addTo(layer);
      }
    }
    const qmax = Math.max(...flows.map((f) => f.quantity), 1e-12);
    const cmin = Math.min(...flows.map((f) => f.unitCost));
    const cmax = Math.max(...flows.map((f) => f.unitCost));
    for (const f of [...flows].sort((a, b) => a.quantity - b.quantity)) {
      const a = nodes.sources[f.from];
      const b = nodes.targets[f.to];
      if (!a || !b) continue;
      L.polyline([pos(a), pos(b)], {
        color: rampColor(cmax > cmin ? (f.unitCost - cmin) / (cmax - cmin) : 0.5),
        weight: 1 + 7 * Math.sqrt(f.quantity / qmax),
        opacity: 0.85,
        lineCap: "round",
      })
        .bindTooltip(tip(`${a.label} → ${b.label}: ${num(f.quantity, 2, lang)} ${unit} · ${num(f.unitCost, 3, lang)}/${unit}`), { sticky: true, className: "tp-tip" })
        .addTo(layer);
    }
    const smax = Math.max(...nodes.sources.map((s) => s.volume), 1e-12);
    nodes.sources.forEach((s) => {
      L.circleMarker(pos(s), { radius: 4 + 8 * Math.sqrt(s.volume / smax), color: "#0F1A2E", weight: 1.2, fillColor: "#ffffff", fillOpacity: 1 })
        .bindTooltip(tip(`${s.label}: ${num(s.volume, 2, lang)} ${unit}`), { className: "tp-tip" })
        .addTo(layer);
    });
    nodes.targets.forEach((d) => {
      L.circleMarker(pos(d), { radius: nodes.targets.length > 60 ? 3 : 6, color: "#ffffff", weight: 1.2, fillColor: "#0F1A2E", fillOpacity: 1 })
        .bindTooltip(tip(`${d.label}: ${num(d.volume, 2, lang)} ${unit}`), { className: "tp-tip" })
        .addTo(layer);
    });
  }, [ready, mode, nodes, flows, crossings, showCrossings, unit, lang]);

  return <div ref={el} className="map-canvas" role="region" aria-label={lang === "en" ? "Map of the shipment plan" : "Карта плана перевозок"} />;
}
