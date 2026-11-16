"""Loading the raw records and writing tables (shared by the table and figure modules)."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from tpga.experiments.v2.methods import key_of
from tpga.experiments.v2.storage import read_parts

SET_ORDER = ["uniform", "structured", "skewed", "ties", "lp_scaling"]
METHOD_ORDER = [
    "LP",
    "LP-ortools",
    "NWC",
    "LCM",
    "VAM",
    "RS",
    "GA-rand-base",
    "GA-cost-base",
    "GA-rand-tuned",
    "GA-cost-tuned",
    "SA-rand-tuned",
    "SA-cost-tuned",
]
STOCHASTIC = ["RS", "GA-rand-base", "GA-cost-base", "GA-rand-tuned", "GA-cost-tuned", "SA-rand-tuned", "SA-cost-tuned"]


def load_runs(output: Path) -> pd.DataFrame:
    rows = list(read_parts(output / "raw" / "runs", "runs"))
    by_key: dict[str, dict[str, Any]] = {}
    for r in rows:  # a key is written once by the runner; keep the last copy if a part was ever duplicated
        r["key"] = key_of(r)
        by_key[r["key"]] = r
    df = pd.DataFrame(list(by_key.values()))
    if len(df):
        df["arcs"] = df["m"] * df["n"]
    return df


def load_curves(output: Path) -> pd.DataFrame:
    return pd.DataFrame(list(read_parts(output / "raw" / "curves", "curves")))


def size_key(size: str) -> int:
    m, n = (int(v) for v in size.split("x"))
    return m * n


def sort_frame(df: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    if not len(df):
        return df
    keys = []
    out = df.copy()
    for col in by:
        if col == "size":
            out["_size"] = out["size"].map(size_key)
            keys.append("_size")
        elif col == "set":
            out["_set"] = out["set"].map(lambda s: SET_ORDER.index(s) if s in SET_ORDER else 99)
            keys.append("_set")
        elif col == "method":
            out["_method"] = out["method"].map(lambda s: METHOD_ORDER.index(s) if s in METHOD_ORDER else 99)
            keys.append("_method")
        else:
            keys.append(col)
    return out.sort_values(keys).drop(columns=[c for c in ("_size", "_set", "_method") if c in out])


def fmt(v: Any, digits: int = 3) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "–"
    if isinstance(v, (bool, np.bool_)):
        return str(bool(v))
    if isinstance(v, (int, np.integer)):
        return str(int(v))
    if isinstance(v, (float, np.floating)):
        if v == 0:
            return "0"
        if abs(v) >= 1e5 or abs(v) < 1e-3:
            return f"{v:.{digits}e}"
        return f"{v:.{digits}f}"
    return str(v)


def write_table(df: pd.DataFrame, path: Path, title: str, note: str = "") -> None:
    """CSV plus Markdown with the same rows; ``note`` states the source filter and the method."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # pandas writes os.linesep by default; LF keeps the files identical on every system
    df.to_csv(path.with_suffix(".csv"), index=False, lineterminator="\n")
    cols = list(df.columns)
    lines = [f"# {title}", ""]
    if note:
        lines += [note, ""]
    if cols:
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("|" + "|".join("---" for _ in cols) + "|")
        for _, r in df.iterrows():
            lines.append("| " + " | ".join(fmt(r[c]) for c in cols) + " |")
    else:
        lines.append("_No rows: the phase has not been run._")
    path.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def per_instance(df: pd.DataFrame, value: str = "gap") -> pd.DataFrame:
    """Median over seeds per (set, size, instance, method): the unit of every paired test."""
    return df.groupby(["set", "size", "instance", "method"])[value].median().reset_index()
