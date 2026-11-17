"""T7: stopping rules - budget only (``main``), 0.1 B decoder calls without improvement (``stagnation``),
200 generations without improvement as in v0.3.0 (``legacy``); paired test budget vs each rule per size."""

from __future__ import annotations

import pandas as pd

from tpga.experiments.reporting import stats

RULES = {"main": "budget only", "stagnation": "0.1 B calls without improvement", "legacy": "200 generations"}


def table(runs: pd.DataFrame) -> pd.DataFrame:
    sub = runs[runs["phase"].isin(RULES)]
    have = set(sub[sub["phase"] != "main"][["set", "size", "method"]].itertuples(index=False, name=None))
    keep = [(s, z, m) in have for s, z, m in sub[["set", "size", "method"]].itertuples(index=False, name=None)]
    sub = sub[pd.Series(keep, index=sub.index, dtype=bool)]  # a Series: an empty list would select no columns
    rows = []
    for (set_, size, method), g in sub.groupby(["set", "size", "method"]):
        per = g.groupby(["instance", "phase"])["gap"].median().unstack("phase")
        for phase, label in RULES.items():
            part = g[g["phase"] == phase]
            if not len(part):
                continue
            row = {
                "set": set_,
                "size": size,
                "method": method,
                "stop": label,
                "runs": len(part),
                "gap_mean": part["gap"].mean(),
                "gap_median": part["gap"].median(),
                "evals_median": part["evals"].median(),
                "time_median_s": part["time_s"].median(),
                "stopped_early_share": float((part["stop_reason"] != "budget").mean()),
                "budget_used_median": float((part["evals"] / part["budget"]).median()),
                "best_found_median": float((part["best_eval"] / part["budget"]).median()),
            }
            if phase != "main" and "main" in per and phase in per:
                pair = per[["main", phase]].dropna()
                if len(pair) >= 2:
                    res = stats.paired(pair[phase].to_numpy(), pair["main"].to_numpy())
                    row.update(
                        p=res["p"],
                        p_text=stats.format_p(res["p"]),
                        hl_shift=res["hl_shift"],
                        hl_ci_low=res["hl_ci_low"],
                        hl_ci_high=res["hl_ci_high"],
                    )
            rows.append(row)
    return pd.DataFrame(rows)
