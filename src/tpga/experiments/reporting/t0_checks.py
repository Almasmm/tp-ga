"""T0: checks of the run (records, errors, feasibility) and the worked example of Section 2.2 of the article.

``checks`` summarises every phase: records, failed runs (``logs/errors.jsonl``), the largest constraint
residual of a final plan, plans that failed the independent check, and the wall time from the manifest.
``example1`` recomputes Table 1 of the article with the library: the instance, the permutation and the
expected plans are those printed in the article.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from tpga.basis import permutation_from_basis
from tpga.classical import least_cost, northwest_corner, vogel
from tpga.decoder import decode_trace
from tpga.exact import solve_lp_highspy
from tpga.experiments.v2.storage import read_jsonl
from tpga.model import TransportProblem

EXAMPLE = TransportProblem([70, 65, 40], [50, 50, 50, 25], [[10, 22, 30, 21], [20, 26, 4, 23], [9, 27, 14, 15]])
#: the random permutation of Example 1, as 1-based (i, j) pairs in the article
EXAMPLE_PERMUTATION = [(1, 1), (2, 4), (2, 3), (3, 2), (3, 4), (1, 4), (2, 2), (1, 3), (2, 1), (3, 3), (1, 2), (3, 1)]


def checks(output: Path, runs: pd.DataFrame) -> pd.DataFrame:
    errors = read_jsonl(output / "logs" / "errors.jsonl") if (output / "logs" / "errors.jsonl").exists() else []
    manifest = output / "run_manifest.json"
    phases_wall = {}
    if manifest.exists():
        for ph, entries in json.loads(manifest.read_text(encoding="utf-8")).get("phases", {}).items():
            phases_wall[ph] = sum(float(e.get("wall_s", 0.0)) for e in entries)
    rows: list[dict[str, Any]] = []
    names = {str(ph) for ph in runs["phase"]} if len(runs) else set()
    names |= {str(e["phase"]) for e in errors if e.get("phase")}
    for phase in sorted(names):
        part = runs[runs["phase"] == phase] if len(runs) else runs
        plans = part[part["feasible"].notna()] if "feasible" in part else part.iloc[0:0]
        rows.append(
            {
                "phase": phase,
                "records": len(part),
                "failed_runs": sum(1 for e in errors if e.get("phase") == phase),
                "plans_checked": len(plans),
                "plans_infeasible": int((plans["feasible"] != True).sum()) if len(plans) else 0,  # noqa: E712
                "max_residual": float(plans["max_residual"].max())
                if len(plans) and "max_residual" in plans
                else np.nan,
                "max_dummy_volume": float(plans["dummy_volume"].max())
                if len(plans) and "dummy_volume" in plans
                else np.nan,
                "wall_h": phases_wall.get(phase, np.nan) / 3600,
            }
        )
    if rows:
        total = {
            "phase": "total",
            **{
                k: sum(int(r[k]) for r in rows) for k in ("records", "failed_runs", "plans_checked", "plans_infeasible")
            },
        }
        total["max_residual"] = _nanmax([r["max_residual"] for r in rows])
        total["max_dummy_volume"] = _nanmax([r["max_dummy_volume"] for r in rows])
        total["wall_h"] = float(np.nansum([r["wall_h"] for r in rows]))
        rows.append(total)
    return pd.DataFrame(rows)


def _nanmax(values: list[float]) -> float:
    finite = [v for v in values if not np.isnan(v)]
    return max(finite) if finite else float("nan")


def _shipments(cells: list[tuple[int, int, float]]) -> str:
    return ", ".join(f"x{i + 1}{j + 1} = {q:g}" for i, j, q in cells)


def example1() -> pd.DataFrame:
    p = EXAMPLE
    n = p.shape[1]
    lp = solve_lp_highspy(p)
    z = float(lp.cost)
    rows = []
    for name, res in (("NWC", northwest_corner(p)), ("LCM", least_cost(p)), ("VAM", vogel(p))):
        cells = [(s["row"], s["col"], s["quantity"]) for s in res.steps if s["quantity"] > 0]
        rows.append((name, cells, float(res.cost)))
    perm = np.array([(i - 1) * n + (j - 1) for i, j in EXAMPLE_PERMUTATION])
    leaf = permutation_from_basis(p, np.round(lp.x))
    for name, order in (("Decoder, random permutation", perm), ("Decoder, leaf-elimination order", leaf)):
        steps = [s for s in decode_trace(p, order) if s["quantity"] > 0]
        cells = [(s["arc"] // n, s["arc"] % n, s["quantity"]) for s in steps]
        rows.append((name, cells, float(sum(p.cost[i, j] * q for i, j, q in cells))))
    x = np.round(lp.x)
    rows.append(("LP optimum (HiGHS)", [(i, j, float(x[i, j])) for i, j in zip(*np.nonzero(x), strict=True)], z))
    return pd.DataFrame(
        [
            {
                "method": name,
                "shipments_in_order": _shipments(cells),
                "positive": len(cells),
                "cost": cost,
                "gap": 100 * (cost - z) / z,
            }
            for name, cells, cost in rows
        ]
    )
