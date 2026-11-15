"use client";

import { useSettings } from "../providers";
import { num } from "../lib/format";

/**
 * Cost matrix with the shipments placed so far and the remaining supplies and demands.
 * plan: m x n quantities; current: [i, j] or null; rowNote/colNote: optional extra labels (VAM penalties).
 */
export function TransportMatrix({ cost, plan, supplyLeft, demandLeft, current, line, rowNote, colNote, caption }) {
  const { t, lang } = useSettings();
  const m = cost.length;
  const n = cost[0].length;
  return (
    <div className="table-wrap" style={{ border: 0, background: "transparent" }}>
      <table className="matrix" aria-label={caption ?? t("plan")}>
        {caption && <caption className="sr-only">{caption}</caption>}
        <thead>
          <tr>
            <th aria-hidden="true" />
            {Array.from({ length: n }, (_, j) => (
              <th key={j} scope="col" className="margin">B{j + 1}{colNote?.[j] != null && <span className="pen">Δ {num(colNote[j], 1, lang)}</span>}</th>
            ))}
            <th scope="col" className="margin">{t("supply")}</th>
          </tr>
        </thead>
        <tbody>
          {cost.map((row, i) => (
            <tr key={i}>
              <th scope="row" className="margin">A{i + 1}{rowNote?.[i] != null && <span className="pen">Δ {num(rowNote[i], 1, lang)}</span>}</th>
              {row.map((c, j) => {
                const q = plan?.[i]?.[j] ?? 0;
                const cur = current && current[0] === i && current[1] === j;
                const inLine = line && ((line.type === "row" && line.index === i) || (line.type === "col" && line.index === j));
                const cls = ["cell", q > 0 ? "filled" : "", cur ? "current" : "", inLine && !cur ? "chosen-line" : ""].join(" ");
                return (
                  <td key={j} className={cls} aria-label={`A${i + 1}→B${j + 1}: ${t("cost")} ${c}${q > 0 ? `, x = ${q}` : ""}`}>
                    <span className="c">{num(c, 2, lang)}</span>
                    {q > 0 && <span className="q">{num(q, 2, lang)}</span>}
                  </td>
                );
              })}
              <td className={"margin" + (supplyLeft?.[i] === 0 ? " zero" : "")}>{num(supplyLeft?.[i], 2, lang)}</td>
            </tr>
          ))}
          <tr>
            <th scope="row" className="margin">{t("demand")}</th>
            {Array.from({ length: n }, (_, j) => (
              <td key={j} className={"margin" + (demandLeft?.[j] === 0 ? " zero" : "")}>{num(demandLeft?.[j], 2, lang)}</td>
            ))}
            <td />
          </tr>
        </tbody>
      </table>
    </div>
  );
}

/** Plan of positive cells -> dense m x n matrix. */
export function denseFromCells(cells, m, n) {
  const x = Array.from({ length: m }, () => Array(n).fill(0));
  for (const c of cells) x[c.row][c.col] += c.quantity;
  return x;
}
