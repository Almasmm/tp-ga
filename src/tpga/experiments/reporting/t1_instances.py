"""T1: instance sets (from ``instances/manifest.json``) with the LP optimum and Z_rand."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from tpga.experiments.reporting.common import sort_frame


def table(output: Path, runs: pd.DataFrame) -> pd.DataFrame:
    path = output / "instances" / "manifest.json"
    if not path.exists():
        return pd.DataFrame()
    entries = pd.DataFrame(json.loads(path.read_text(encoding="utf-8"))["instances"].values())
    entries["size"] = entries["m"].astype(str) + "x" + entries["n"].astype(str)
    lp = (
        runs[(runs["phase"] == "reference") & (runs["method"] == "LP")].set_index("instance")["cost"]
        if len(runs)
        else pd.Series(dtype=float)
    )
    entries["z_star"] = entries["id"].map(lp)
    rows = []
    for (set_, size), g in entries.groupby(["set", "size"]):
        rows.append(
            {
                "set": set_,
                "size": size,
                "instances": len(g),
                "arcs": int(g["m"].iloc[0] * g["n"].iloc[0]),
                "z_star_median": g["z_star"].median(),
                "z_rand_median": g["z_rand"].median(),
                "generator": g["generator"].iloc[0],
            }
        )
    return sort_frame(pd.DataFrame(rows), ["set", "size"])
