"use client";

import { useId } from "react";
import { METHOD_COLOR } from "../lib/format";

const W = 640;

function ticks(min, max, log) {
  if (log) {
    const out = [];
    for (let e = Math.floor(Math.log10(min)); e <= Math.ceil(Math.log10(max)); e += 1) out.push(10 ** e);
    return out.filter((v) => v >= min * 0.999 && v <= max * 1.001);
  }
  const span = max - min || 1;
  const step = 10 ** Math.floor(Math.log10(span / 4));
  const nice = [1, 2, 5, 10].map((k) => k * step).find((s) => span / s <= 6) ?? step * 10;
  const out = [];
  for (let v = Math.ceil(min / nice) * nice; v <= max + 1e-12; v += nice) out.push(+v.toPrecision(10));
  return out;
}

const fmtTick = (v) => {
  const a = Math.abs(v);
  if (a >= 1e6) return (v / 1e6).toPrecision(3).replace(/\.?0+$/, "") + "M";
  if (a >= 1e3) return (v / 1e3).toPrecision(3).replace(/\.?0+$/, "") + "k";
  return String(+v.toPrecision(3));
};

/**
 * Line chart. series: [{ key, label, color?, points: [[x, y]], band?: [[x, lo, hi]], dashed? }]
 * refs: [{ y, label, color }] horizontal reference lines.
 */
export function LineChart({ series, refs = [], xLog = false, yLog = false, xLabel, yLabel, height = 280, title }) {
  const id = useId();
  const pts = series.flatMap((s) => [...s.points, ...(s.band ?? []).flatMap(([x, lo, hi]) => [[x, lo], [x, hi]])]);
  const ys = [...pts.map((p) => p[1]), ...refs.map((r) => r.y)].filter((v) => Number.isFinite(v) && (!yLog || v > 0));
  const xs = pts.map((p) => p[0]).filter((v) => Number.isFinite(v) && (!xLog || v > 0));
  if (!xs.length || !ys.length) return null;
  const pad = { l: 56, r: 16, t: 12, b: 40 };
  let [x0, x1] = [Math.min(...xs), Math.max(...xs)];
  let [y0, y1] = [Math.min(...ys), Math.max(...ys)];
  if (x0 === x1) x1 = x0 + 1;
  if (y0 === y1) [y0, y1] = [y0 - 1, y1 + 1];
  if (!yLog) {
    const m = (y1 - y0) * 0.06;
    y0 -= m;
    y1 += m;
  }
  const fx = (v) => pad.l + ((xLog ? Math.log10(v) - Math.log10(x0) : v - x0) / (xLog ? Math.log10(x1) - Math.log10(x0) : x1 - x0)) * (W - pad.l - pad.r);
  const fy = (v) => height - pad.b - ((yLog ? Math.log10(v) - Math.log10(y0) : v - y0) / (yLog ? Math.log10(y1) - Math.log10(y0) : y1 - y0)) * (height - pad.t - pad.b);
  const path = (p) => p.filter(([x, y]) => Number.isFinite(y) && (!xLog || x > 0) && (!yLog || y > 0)).map(([x, y], i) => `${i ? "L" : "M"}${fx(x).toFixed(1)},${fy(y).toFixed(1)}`).join("");
  return (
    <figure style={{ margin: 0 }}>
      <svg className="chart" viewBox={`0 0 ${W} ${height}`} role="img" aria-labelledby={id}>
        <title id={id}>{title ?? yLabel}</title>
        <defs>
          <clipPath id={id + "c"}><rect x={pad.l} y={pad.t} width={W - pad.l - pad.r} height={height - pad.t - pad.b} /></clipPath>
        </defs>
        {ticks(y0, y1, yLog).map((v) => (
          <g key={"y" + v}>
            <line className="grid-line" x1={pad.l} x2={W - pad.r} y1={fy(v)} y2={fy(v)} />
            <text x={pad.l - 6} y={fy(v) + 4} textAnchor="end">{fmtTick(v)}</text>
          </g>
        ))}
        {ticks(x0, x1, xLog).map((v) => (
          <text key={"x" + v} x={fx(v)} y={height - pad.b + 16} textAnchor="middle">{fmtTick(v)}</text>
        ))}
        <line className="axis" x1={pad.l} x2={W - pad.r} y1={height - pad.b} y2={height - pad.b} stroke="var(--border-strong)" />
        <g clipPath={`url(#${id}c)`}>
          {refs.map((r) => (
            <line key={r.label} x1={pad.l} x2={W - pad.r} y1={fy(r.y)} y2={fy(r.y)} stroke={r.color ?? "var(--m-lp)"} strokeDasharray="5 4" strokeWidth={1.4} />
          ))}
          {series.map((s) =>
            s.band ? (
              <path
                key={s.key + "b"}
                d={path(s.band.map(([x, , hi]) => [x, hi])) + path([...s.band].reverse().map(([x, lo]) => [x, lo])).replace(/^M/, "L") + "Z"}
                fill={s.color ?? METHOD_COLOR[s.key]}
                opacity={0.14}
              />
            ) : null,
          )}
          {series.map((s) => (
            <path key={s.key} d={path(s.points)} fill="none" stroke={s.color ?? METHOD_COLOR[s.key]} strokeWidth={2} strokeDasharray={s.dashed ? "6 4" : undefined} strokeLinejoin="round" />
          ))}
        </g>
        {xLabel && <text x={(W + pad.l) / 2} y={height - 4} textAnchor="middle">{xLabel}</text>}
        {yLabel && <text transform={`translate(12 ${(height - pad.b) / 2}) rotate(-90)`} textAnchor="middle">{yLabel}</text>}
      </svg>
      <figcaption className="legend">
        {series.map((s) => (
          <span key={s.key}><i className="method-dot" style={{ background: s.color ?? METHOD_COLOR[s.key] }} />{s.label ?? s.key}</span>
        ))}
        {refs.map((r) => (
          <span key={r.label}><i className="method-dot" style={{ background: r.color ?? "var(--m-lp)" }} />{r.label}</span>
        ))}
      </figcaption>
    </figure>
  );
}

/** Horizontal bars: rows [{ key, label, value, color, highlight }] */
export function Bars({ rows, format = (v) => v, height = 22, max: forcedMax }) {
  const max = forcedMax ?? Math.max(...rows.map((r) => r.value), 1e-12);
  return (
    <div className="stack" style={{ gap: 6 }}>
      {rows.map((r) => (
        <div key={r.key} style={{ display: "grid", gridTemplateColumns: "minmax(90px, 160px) 1fr minmax(64px, auto)", gap: 8, alignItems: "center" }}>
          <span className="meta" style={{ color: "var(--text-secondary)" }}>{r.label}</span>
          <span style={{ height, background: "var(--surface-2)", borderRadius: 6, border: "1px solid var(--border)", overflow: "hidden" }}>
            <span style={{ display: "block", height: "100%", width: `${Math.max(1, (100 * r.value) / max)}%`, background: r.color ?? "var(--accent)", opacity: r.dim ? 0.35 : 1, outline: r.highlight ? "2px solid var(--text)" : "none", outlineOffset: -2 }} />
          </span>
          <span className="code-value" style={{ textAlign: "right" }}>{format(r.value)}</span>
        </div>
      ))}
    </div>
  );
}
