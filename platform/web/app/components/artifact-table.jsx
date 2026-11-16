"use client";

// A CSV table of the experiment artifacts with per-column filters (read only).
import { useMemo, useState } from "react";
import { useSettings } from "../providers";
import { useApi } from "../lib/use-api";
import { num } from "../lib/format";
import { Field, Source, State } from "./ui";

const FILTER_COLUMNS = [
  "size", "method", "suite", "initialization", "population", "mutation_rate", "mutation", "set", "method_a", "method_b", "stop", "value", "range",
];

export function ArtifactTable({ base, source, name, lang }) {
  const { t } = useSettings();
  const table = useApi(`${base}/${name}`, { isEmpty: (d) => !d.rows.length });
  const [filters, setFilters] = useState({});
  const rows = useMemo(
    () => (table.data?.rows ?? []).filter((r) => Object.entries(filters).every(([k, v]) => v === "" || String(r[k]) === v)),
    [table.data, filters],
  );
  const columns = table.data?.columns ?? [];
  const filterable = FILTER_COLUMNS.filter((c) => columns.includes(c));
  return (
    <State status={table.status} error={table.error} onRetry={table.reload}>
      {table.data && (
        <>
          {filterable.length > 0 && (
            <div className="field-row" style={{ marginBottom: 12 }} aria-label={t("filters")}>
              {filterable.map((c) => {
                const values = [...new Set(table.data.rows.map((r) => String(r[c])))];
                return (
                  <Field key={c} label={c}>
                    <select value={filters[c] ?? ""} onChange={(e) => setFilters((f) => ({ ...f, [c]: e.target.value }))}>
                      <option value="">{t("all")}</option>
                      {values.map((v) => <option key={v} value={v}>{v}</option>)}
                    </select>
                  </Field>
                );
              })}
            </div>
          )}
          <div className="table-wrap" style={{ maxHeight: 520 }}>
            <table>
              <thead><tr>{columns.map((c) => <th key={c} className={typeof table.data.rows[0]?.[c] === "number" ? "num" : ""}>{c}</th>)}</tr></thead>
              <tbody>
                {rows.map((r, i) => (
                  <tr key={i}>{columns.map((c) => <td key={c} className={typeof r[c] === "number" ? "num" : ""}>{typeof r[c] === "number" ? num(r[c], 4, lang) : r[c] ?? "–"}</td>)}</tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="meta" style={{ marginTop: 8 }}>{rows.length} / {table.data.rows.length} · <Source>{`${source}/${name}.csv`}</Source></p>
        </>
      )}
    </State>
  );
}
