"use client";

import { useSettings } from "../providers";
import { num } from "../lib/format";

/** Bipartite sketch: sources on the left, destinations on the right, line width proportional to volume. */
export function MiniMap({ m, n, cells, supply, demand }) {
  const { t, lang } = useSettings();
  const H = Math.max(m, n) * 36 + 24;
  const W = 360;
  const ys = (k, total) => 18 + (k + 0.5) * ((H - 36) / total);
  const max = Math.max(...cells.map((c) => c.quantity), 1);
  return (
    <svg className="chart" viewBox={`0 0 ${W} ${H}`} role="img" aria-label={t("plan")}>
      {cells.map((c) => (
        <line key={`${c.row}-${c.col}`} x1={70} y1={ys(c.row, m)} x2={W - 70} y2={ys(c.col, n)} stroke="var(--accent)" strokeOpacity={0.75} strokeWidth={1 + (6 * c.quantity) / max} strokeLinecap="round">
          <title>{`A${c.row + 1} → B${c.col + 1}: ${num(c.quantity, 2, lang)}`}</title>
        </line>
      ))}
      {Array.from({ length: m }, (_, i) => (
        <g key={"a" + i}>
          <circle cx={70} cy={ys(i, m)} r={9} fill="var(--surface)" stroke="var(--text)" strokeWidth={1.4} />
          <text x={52} y={ys(i, m) + 4} textAnchor="end">A{i + 1}{supply ? ` ${num(supply[i], 0, lang)}` : ""}</text>
        </g>
      ))}
      {Array.from({ length: n }, (_, j) => (
        <g key={"b" + j}>
          <rect x={W - 79} y={ys(j, n) - 9} width={18} height={18} rx={4} fill="var(--text)" />
          <text x={W - 52} y={ys(j, n) + 4}>B{j + 1}{demand ? ` ${num(demand[j], 0, lang)}` : ""}</text>
        </g>
      ))}
    </svg>
  );
}
