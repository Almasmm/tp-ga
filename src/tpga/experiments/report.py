"""Tables, figures and documents of the paper from the raw results.

``python -m tpga.experiments.report --config experiments/paper.yaml`` regenerates everything in
``tables/``, ``figures/`` and the Markdown documents from ``raw/``, ``instances/``,
``reachability.json`` and ``environment.json``. Nothing is edited by hand.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from scipy import stats  # noqa: E402

from tpga.decoder import decode_trace  # noqa: E402
from tpga.experiments.config import GA_METHODS, Config  # noqa: E402
from tpga.model import TransportProblem  # noqa: E402

METHOD_ORDER = ["LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost"]
STOCHASTIC = ["RS", "GA-rand", "GA-cost"]
# Grey levels are distinct (luminance 0.15 ... 0.8) and every method also has its own marker and line style.
STYLE: dict[str, dict[str, Any]] = {
    "LP": {"color": "#000000", "marker": "s", "ls": (0, (1, 1.5)), "hatch": ""},
    "NWC": {"color": "#8c8c8c", "marker": "v", "ls": ":", "hatch": "xx"},
    "LCM": {"color": "#5e5e5e", "marker": "^", "ls": "-.", "hatch": "\\\\"},
    "VAM": {"color": "#b5b5b5", "marker": "D", "ls": (0, (5, 1)), "hatch": ".."},
    "RS": {"color": "#a3a3a3", "marker": "x", "ls": (0, (4, 1, 1, 1, 1, 1)), "hatch": "--"},
    "GA-rand": {"color": "#262626", "marker": "o", "ls": "-", "hatch": ""},
    "GA-cost": {"color": "#737373", "marker": "P", "ls": "--", "hatch": "//"},
}
LABELS = {
    "en": {
        "evals": "Decoder calls",
        "gap": "Gap to the LP optimum (%)",
        "median_gap": "Median gap to the LP optimum (%)",
        "arcs": "Number of arcs m·n",
        "time": "Wall-clock time per run (s)",
        "time_eval": "Time per decoder call (µs)",
        "population": "Population size",
        "mutation": "Mutation probability",
        "size": "Size",
        "lon": "Longitude (°)",
        "lat": "Latitude (°)",
        "volume": "Volume (thousand t)",
        "uniform": "uniform costs",
        "structured": "Euclidean costs",
        "random": "random start",
        "cost-aware": "cost-aware start",
        "step": "Step",
        "perm": "Permutation of arcs",
        "perm_key": (
            "dark: positive allocation; grey: visited, nothing left to allocate; white: not visited; "
            "a′, b′: remaining supply and demand"
        ),
        "supply": "a",
        "demand": "b",
        "region": "Region (supply)",
        "market": "Market (demand)",
        "fit": "fit",
    },
    "ru": {
        "evals": "Вызовы декодера",
        "gap": "Отклонение от оптимума ЛП (%)",
        "median_gap": "Медиана отклонения от оптимума ЛП (%)",
        "arcs": "Число дуг m·n",
        "time": "Время одного запуска (с)",
        "time_eval": "Время одного вызова декодера (мкс)",
        "population": "Размер популяции",
        "mutation": "Вероятность мутации",
        "size": "Размерность",
        "lon": "Долгота (°)",
        "lat": "Широта (°)",
        "volume": "Объём (тыс. т)",
        "uniform": "равномерные стоимости",
        "structured": "евклидовы стоимости",
        "random": "случайный старт",
        "cost-aware": "старт с учётом стоимости",
        "step": "Шаг",
        "perm": "Перестановка дуг",
        "perm_key": (
            "тёмные: положительное назначение; серые: пройдены без назначения; белые: не пройдены; "
            "a′, b′: остатки запасов и потребностей"
        ),
        "supply": "a",
        "demand": "b",
        "region": "Область (запас)",
        "market": "Рынок (спрос)",
        "fit": "аппроксимация",
    },
}


# --- loading ---------------------------------------------------------------------------------


def convergence_file(out: Path, name: str) -> Path | None:
    """The convergence CSV of a phase: plain while the runner appends to it, gzip-compressed when archived."""
    for suffix in (".csv", ".csv.gz"):
        p = out / "raw" / "convergence" / f"{name}{suffix}"
        if p.exists():
            return p
    return None


def load_runs(cfg: Config) -> pd.DataFrame:
    df = pd.read_csv(cfg.output / "raw" / "runs.csv")
    df["arcs"] = df["m"] * df["n"]
    df["optimal"] = df["optimal"].astype(str).str.lower().eq("true")
    return df


def size_key(size: str) -> int:
    m, n = (int(v) for v in size.split("x"))
    return m * n


def _fmt(v: Any, digits: int = 3) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "–"
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
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path.with_suffix(".csv"), index=False)
    cols = list(df.columns)
    lines = [f"# {title}", ""]
    if note:
        lines += [note, ""]
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("|" + "|".join("---" for _ in cols) + "|")
    for _, r in df.iterrows():
        lines.append("| " + " | ".join(_fmt(r[c]) for c in cols) + " |")
    path.with_suffix(".md").write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- base configuration selection ------------------------------------------------------------


def base_mask(df: pd.DataFrame, cfg: Config) -> pd.Series:
    """Rows of LP, classical methods, RS and the GA with the base configuration."""
    base_id = cfg.ga_base.config_id(cfg.budget, cfg.stagnation)
    return (
        df["method"].isin(["LP", "NWC", "LCM", "VAM"])
        | ((df["method"] == "RS") & (df["config"] == cfg.budget.rule_id))
        | (df["method"].isin(list(GA_METHODS)) & (df["config"] == base_id))
    )


def synthetic(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["suite"].isin(["uniform", "structured"])]


# --- tables ----------------------------------------------------------------------------------


def table_instances(cfg: Config, df: pd.DataFrame) -> pd.DataFrame:
    manifest = json.loads((cfg.output / "instances" / "manifest.json").read_text(encoding="utf-8"))
    rows = []
    lp = df[df["method"] == "LP"].set_index("instance")
    groups: dict[tuple[str, str], list[dict]] = {}
    for e in manifest["instances"]:
        key = (e["suite"] if e["suite"] != "applied" else e["dataset"], f"{e['m']}x{e['n']}")
        groups.setdefault(key, []).append(e)
    for (suite, size), items in groups.items():
        probs = [TransportProblem.from_json(cfg.output / "instances" / e["file"]) for e in items]
        z = [float(lp.loc[e["id"], "cost"]) for e in items if e["id"] in lp.index]
        rows.append(
            {
                "set": suite,
                "size": size,
                "instances": len(items),
                "arcs": items[0]["m"] * items[0]["n"],
                "balanced": sum(bool(e["balanced"]) for e in items),
                "total_supply_min": min(float(p.supply.sum()) for p in probs),
                "total_supply_max": max(float(p.supply.sum()) for p in probs),
                "cost_min": min(float(np.min(p.cost)) for p in probs),
                "cost_max": max(float(np.max(p.cost)) for p in probs),
                "z_star_median": float(np.median(z)) if z else math.nan,
            }
        )
    out = pd.DataFrame(rows)
    out["_k"] = out["size"].map(size_key)
    order = {"uniform": 0, "structured": 1}
    out["_s"] = out["set"].map(lambda s: order.get(s, 2))
    return out.sort_values(["_s", "_k"]).drop(columns=["_k", "_s"])


def gap_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (suite, size, method), g in df.groupby(["suite", "size", "method"]):
        per_inst = g.groupby("instance")["gap"].median()
        rows.append(
            {
                "suite": suite,
                "size": size,
                "method": method,
                "instances": g["instance"].nunique(),
                "runs": len(g),
                "gap_mean": g["gap"].mean(),
                "gap_median": g["gap"].median(),
                "gap_sd": g["gap"].std(ddof=1) if len(g) > 1 else math.nan,
                "gap_min": g["gap"].min(),
                "gap_max": g["gap"].max(),
                "median_of_instance_medians": per_inst.median(),
                "share_optimal": g["optimal"].mean(),
                "instances_with_optimal_run": int(g.groupby("instance")["optimal"].any().sum()),
                "time_median_s": g["time_s"].median(),
            }
        )
    out = pd.DataFrame(rows)
    out["_k"] = out["size"].map(size_key)
    out["_m"] = out["method"].map(METHOD_ORDER.index)
    return out.sort_values(["suite", "_k", "_m"]).drop(columns=["_k", "_m"])


def loglog_fit(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    lx, ly = np.log10(x), np.log10(y)
    fit = stats.linregress(lx, ly)
    tcrit = stats.t.ppf(0.975, len(x) - 2)
    return {
        "a": 10**fit.intercept,
        "b": fit.slope,
        "b_ci_low": fit.slope - tcrit * fit.stderr,
        "b_ci_high": fit.slope + tcrit * fit.stderr,
        "r2": fit.rvalue**2,
        "points": len(x),
        "arcs_min": float(np.min(x)),
        "arcs_max": float(np.max(x)),
    }


def time_tables(cfg: Config, df: pd.DataFrame, timing: pd.DataFrame | None) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Median times per size and method, and the log-log fits t = a (m n)^b on per-instance medians."""
    src = timing if timing is not None and len(timing) else df[df["suite"] == "uniform"]
    src = src.copy()
    src["us_per_eval"] = 1e6 * src["time_s"] / src["evals"]
    rows = []
    for (size, method), g in src.groupby(["size", "method"]):
        rows.append(
            {
                "size": size,
                "arcs": int(g["arcs"].iloc[0]),
                "method": method,
                "runs": len(g),
                "time_median_s": g["time_s"].median(),
                "time_q1_s": g["time_s"].quantile(0.25),
                "time_q3_s": g["time_s"].quantile(0.75),
                "evals_median": g["evals"].median() if method in STOCHASTIC else math.nan,
                "us_per_eval_median": g["us_per_eval"].median() if method in STOCHASTIC else math.nan,
                "best_eval_median": g["best_eval"].median() if method in STOCHASTIC else math.nan,
                "cpu_classes": ",".join(sorted({str(int(c)) for c in g["cpu_class"].dropna()})),
            }
        )
    t3 = pd.DataFrame(rows)
    t3["_m"] = t3["method"].map(METHOD_ORDER.index)
    t3 = t3.sort_values(["arcs", "_m"]).drop(columns="_m")
    fits = []
    for method, g in src.groupby("method"):
        per = g.groupby("instance").agg(arcs=("arcs", "first"), t=("time_s", "median"), u=("us_per_eval", "median"))
        if per["arcs"].nunique() < 3:
            continue
        fits.append({"method": method, "quantity": "time per run", **loglog_fit(per["arcs"].values, per["t"].values)})
        if method in STOCHASTIC:
            fits.append(
                {
                    "method": method,
                    "quantity": "time per decoder call",
                    **loglog_fit(per["arcs"].values, per["u"].values),
                }
            )
    return t3, pd.DataFrame(fits)


def holm(p: list[float]) -> list[float]:
    order = np.argsort(p)
    adj = np.empty(len(p))
    running = 0.0
    for rank, idx in enumerate(order):
        running = max(running, (len(p) - rank) * p[idx])
        adj[idx] = min(1.0, running)
    return adj.tolist()


def paired_test(x: np.ndarray, y: np.ndarray) -> dict[str, float]:
    """Wilcoxon signed-rank on paired values; effect sizes: matched-pairs rank-biserial r and Cliff's delta."""
    d = x - y
    nz = d[d != 0]
    if len(nz) == 0:
        p, w = 1.0, 0.0
        r = 0.0
    else:
        res = stats.wilcoxon(x, y, zero_method="wilcox")
        p, w = float(res.pvalue), float(res.statistic)
        ranks = stats.rankdata(np.abs(nz))
        r = float((ranks[nz > 0].sum() - ranks[nz < 0].sum()) / ranks.sum())
    gt = (x[:, None] > y[None, :]).sum()
    lt = (x[:, None] < y[None, :]).sum()
    return {
        "n": len(x),
        "nonzero_differences": len(nz),
        "W": w,
        "p": p,
        "rank_biserial_r": r,
        "cliffs_delta": float((gt - lt) / (len(x) * len(y))),
        "median_difference": float(np.median(d)),
    }


def comparison_tests(df: pd.DataFrame) -> pd.DataFrame:
    """Pairs of methods on per-instance median gaps, per size and pooled; Holm over the whole table."""
    pairs = [
        ("GA-rand", "NWC"),
        ("GA-rand", "LCM"),
        ("GA-rand", "VAM"),
        ("GA-rand", "RS"),
        ("GA-cost", "GA-rand"),
        ("GA-cost", "LCM"),
        ("GA-cost", "VAM"),
    ]
    med = df.groupby(["suite", "size", "instance", "method"])["gap"].median().unstack("method")
    rows = []
    groups: list[tuple[str, str, pd.DataFrame]] = [
        (suite, size, g) for (suite, size), g in med.groupby(level=["suite", "size"])
    ]
    groups.append(("all synthetic", "all", med))
    for suite, size, g in groups:
        for a, b in pairs:
            if a not in g or b not in g:
                continue
            sub = g[[a, b]].dropna()
            if len(sub) < 2:
                continue
            res = paired_test(sub[a].values, sub[b].values)
            rows.append({"suite": suite, "size": size, "method_a": a, "method_b": b, **res})
    out = pd.DataFrame(rows)
    if len(out):
        out["p_holm"] = holm(out["p"].tolist())
        # second family definition: the comparisons within one (set, size) group
        out["p_holm_within_size"] = np.nan
        for _, idx in out.groupby(["suite", "size"]).groups.items():
            out.loc[idx, "p_holm_within_size"] = holm(out.loc[idx, "p"].tolist())
    return out


def factorial_tables(cfg: Config, df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    spec = cfg.phase("factorial")
    sizes = {f"{m}x{n}" for m, n in spec["sizes"]}
    pops, pms = [int(p) for p in spec["population"]], [float(v) for v in spec["mutation_rate"]]
    f = df[
        (df["suite"] == spec["suite"])
        & df["size"].isin(sizes)
        & df["method"].isin(list(GA_METHODS))
        & df["population"].isin(pops)
        & df["mutation_rate"].isin(pms)
        & np.isclose(df["crossover_rate"].fillna(-1), cfg.ga_base.crossover_rate)
    ]
    rows = []
    for (size, method, pop, pm), g in f.groupby(["size", "method", "population", "mutation_rate"]):
        rows.append(
            {
                "size": size,
                "initialization": GA_METHODS[method],
                "population": int(pop),
                "mutation_rate": pm,
                "runs": len(g),
                "gap_mean": g["gap"].mean(),
                "gap_median": g["gap"].median(),
                "gap_sd": g["gap"].std(ddof=1),
                "share_optimal": g["optimal"].mean(),
                "evals_median": g["evals"].median(),
                "time_median_s": g["time_s"].median(),
            }
        )
    t4 = pd.DataFrame(rows)
    if len(t4):
        t4["_k"] = t4["size"].map(size_key)
        t4 = t4.sort_values(["_k", "initialization", "population", "mutation_rate"]).drop(columns="_k")
    tests = []
    for (size, method), g in f.groupby(["size", "method"]):
        med = (
            g.groupby(["instance", "population", "mutation_rate"])["gap"]
            .median()
            .unstack(["population", "mutation_rate"])
        )
        med = med.dropna(axis=1)
        if med.shape[1] >= 3 and med.shape[0] >= 2:
            fr = stats.friedmanchisquare(*[med[c].values for c in med.columns])
            ranks = med.rank(axis=1).mean()
            best = ranks.idxmin()
            tests.append(
                {
                    "size": size,
                    "initialization": GA_METHODS[method],
                    "test": "Friedman over population x mutation",
                    "blocks": med.shape[0],
                    "treatments": med.shape[1],
                    "statistic": fr.statistic,
                    "p": fr.pvalue,
                    "best_mean_rank": f"P={best[0]} pm={best[1]}",
                    "best_rank": float(ranks.min()),
                }
            )
        for factor, levels in (("population", pops), ("mutation_rate", pms)):
            agg = g.groupby(["instance", factor])["gap"].median().unstack(factor).dropna(axis=1)
            if agg.shape[1] >= 3:
                fr = stats.friedmanchisquare(*[agg[c].values for c in agg.columns])
                tests.append(
                    {
                        "size": size,
                        "initialization": GA_METHODS[method],
                        "test": f"Friedman over {factor}",
                        "blocks": agg.shape[0],
                        "treatments": agg.shape[1],
                        "statistic": fr.statistic,
                        "p": fr.pvalue,
                        "best_mean_rank": f"{factor}={agg.rank(axis=1).mean().idxmin()}",
                        "best_rank": float(agg.rank(axis=1).mean().min()),
                    }
                )
                for x, y in combinations(levels, 2):
                    if x in agg and y in agg:
                        res = paired_test(agg[x].values, agg[y].values)
                        tests.append(
                            {
                                "size": size,
                                "initialization": GA_METHODS[method],
                                "test": f"Wilcoxon post-hoc {factor} {x} vs {y}",
                                "blocks": res["n"],
                                "treatments": 2,
                                "statistic": res["W"],
                                "p": res["p"],
                                "rank_biserial_r": res["rank_biserial_r"],
                                "cliffs_delta": res["cliffs_delta"],
                            }
                        )
    # initialization: random vs cost-aware, paired over (instance, population, mutation)
    for size, g in f.groupby("size"):
        med = (
            g.groupby(["instance", "population", "mutation_rate", "method"])["gap"].median().unstack("method").dropna()
        )
        if {"GA-rand", "GA-cost"} <= set(med.columns) and len(med) >= 2:
            res = paired_test(med["GA-cost"].values, med["GA-rand"].values)
            tests.append(
                {
                    "size": size,
                    "initialization": "cost-aware vs random",
                    "test": "Wilcoxon over (instance, population, mutation) cells",
                    "blocks": res["n"],
                    "treatments": 2,
                    "statistic": res["W"],
                    "p": res["p"],
                    "rank_biserial_r": res["rank_biserial_r"],
                    "cliffs_delta": res["cliffs_delta"],
                }
            )
    t4s = pd.DataFrame(tests)
    if len(t4s):
        post = t4s["test"].str.startswith("Wilcoxon post-hoc")
        t4s["p_holm"] = np.nan
        for _, idx in t4s[post].groupby(["size", "initialization"]).groups.items():
            t4s.loc[idx, "p_holm"] = holm(t4s.loc[idx, "p"].tolist())
    return t4, t4s


def stopping_table(cfg: Config, df: pd.DataFrame) -> pd.DataFrame:
    """Base GA configuration with and without the stagnation limit (phase ``stopping``)."""
    if "stopping" not in cfg.raw["phases"]:
        return pd.DataFrame()
    spec = cfg.phase("stopping")
    sizes = {f"{m}x{n}" for m, n in spec["sizes"]}
    with_id = cfg.ga_base.config_id(cfg.budget, cfg.stagnation)
    without_id = cfg.ga_base.config_id(cfg.budget, None)
    rows = []
    sub = df[(df["suite"] == spec["suite"]) & df["size"].isin(sizes) & df["method"].isin(spec["methods"])]
    for (size, method), g in sub.groupby(["size", "method"]):
        a, b = g[g["config"] == with_id], g[g["config"] == without_id]
        if not len(a) or not len(b):
            continue
        ma, mb = a.groupby("instance")["gap"].median(), b.groupby("instance")["gap"].median()
        common = ma.index.intersection(mb.index)
        test = paired_test(ma[common].values, mb[common].values) if len(common) >= 2 else {}
        for label, part in (("stagnation " + str(cfg.stagnation), a), ("budget only", b)):
            rows.append(
                {
                    "size": size,
                    "method": method,
                    "stopping": label,
                    "runs": len(part),
                    "gap_mean": part["gap"].mean(),
                    "gap_median": part["gap"].median(),
                    "share_optimal": part["optimal"].mean(),
                    "evals_median": part["evals"].median(),
                    "time_median_s": part["time_s"].median(),
                    "wilcoxon_p": test.get("p") if label == "budget only" else math.nan,
                    "rank_biserial_r": test.get("rank_biserial_r") if label == "budget only" else math.nan,
                }
            )
    out = pd.DataFrame(rows)
    if len(out):
        out["_k"] = out["size"].map(size_key)
        out = out.sort_values(["_k", "method", "stopping"], ascending=[True, True, False]).drop(columns="_k")
    return out


def applied_table(df: pd.DataFrame) -> pd.DataFrame:
    a = df[df["suite"] == "applied"]
    rows = []
    for inst, g in a.groupby("instance"):
        row: dict[str, Any] = {"instance": inst, "size": g["size"].iloc[0], "z_star": g["z_star"].dropna().iloc[0]}
        lp = g[g["method"] == "LP"]
        row["dummy_volume_LP"] = float(lp["dummy_volume"].iloc[0]) if len(lp) else math.nan
        for method in METHOD_ORDER[1:]:
            mg = g[g["method"] == method]
            if not len(mg):
                continue
            if method in STOCHASTIC:
                row[f"{method}_gap_mean"] = mg["gap"].mean()
                row[f"{method}_gap_min"] = mg["gap"].min()
                row[f"{method}_runs"] = len(mg)
            else:
                row[f"{method}_gap"] = float(mg["gap"].iloc[0])
        rows.append(row)
    return pd.DataFrame(rows)


# --- figures ---------------------------------------------------------------------------------


def setup_fonts() -> str:
    names = {f.name for f in font_manager.fontManager.ttflist}
    family = "Times New Roman" if "Times New Roman" in names else "serif"
    plt.rcParams.update(
        {
            "font.family": family,
            "font.size": 9,
            "axes.titlesize": 9,
            "axes.labelsize": 9,
            "legend.fontsize": 8,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "mathtext.fontset": "stix",
            "axes.spines.top": False,
            "axes.spines.right": False,
        }
    )
    return family


def save_fig(fig: plt.Figure, out: Path, lang: str, name: str) -> None:
    d = out / lang
    d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"{name}.png", dpi=600)
    fig.savefig(d / f"{name}.pdf")
    plt.close(fig)


def fig_decoder(cfg: Config, out: Path, lang: str) -> dict[str, Any]:
    """F1: decoding of a fixed permutation on a 3x4 example, one panel per positive allocation."""
    p = TransportProblem([30, 45, 25], [20, 30, 25, 25], [[8, 6, 10, 9], [9, 12, 13, 7], [14, 9, 16, 5]])
    perm = np.random.default_rng(cfg.base_seed).permutation(12)
    steps = decode_trace(p, perm)
    L = LABELS[lang]
    alloc = [s for s in steps if s["quantity"] > 0]
    fig = plt.figure(figsize=(7.0, 3.9))
    ax0 = fig.add_axes((0.04, 0.83, 0.92, 0.12))
    ax0.set_xlim(0, 12)
    ax0.set_ylim(0, 1)
    ax0.axis("off")
    visited = {s["position"] for s in steps}
    for k, arc in enumerate(perm):
        used = any(s["position"] == k and s["quantity"] > 0 for s in steps)
        face = "#4d4d4d" if used else ("#e6e6e6" if k in visited else "white")
        ax0.add_patch(plt.Rectangle((k + 0.05, 0.1), 0.9, 0.8, fc=face, ec="black", lw=0.6))
        i, j = divmod(int(arc), 4)
        ax0.text(
            k + 0.5, 0.5, f"({i + 1},{j + 1})", ha="center", va="center", fontsize=7, color="white" if used else "black"
        )
    ax0.text(0, 1.15, L["perm"], fontsize=8, transform=ax0.transData)
    ax0.text(12, 1.15, L["perm_key"], fontsize=6.5, ha="right", transform=ax0.transData)
    grid = plt.matplotlib.gridspec.GridSpec(
        2, 3, left=0.04, right=0.98, bottom=0.03, top=0.76, wspace=0.18, hspace=0.25
    )
    plan = np.zeros((3, 4))
    for idx, s in enumerate(alloc[:6]):
        ax = fig.add_subplot(grid[idx // 3, idx % 3])
        plan[s["row"], s["col"]] = s["quantity"]
        ax.set_xlim(0, 5)
        ax.set_ylim(0, 4)
        ax.invert_yaxis()
        ax.axis("off")
        for i in range(3):
            for j in range(4):
                cur = (i, j) == (s["row"], s["col"])
                ax.add_patch(plt.Rectangle((j, i), 1, 1, fc="#bfbfbf" if cur else "white", ec="black", lw=0.5))
                ax.text(j + 0.15, i + 0.3, f"{p.cost[i, j]:g}", fontsize=5.5, color="#555555")
                if plan[i, j] > 0:
                    ax.text(j + 0.55, i + 0.68, f"{plan[i, j]:g}", fontsize=7.5, ha="center", fontweight="bold")
            ax.text(4.5, i + 0.6, f"{s['supply_left'][i]:g}", fontsize=7, ha="center")
        ax.text(4.5, -0.1, "a′", fontsize=7, ha="center", style="italic")
        ax.text(-0.1, 3.6, "b′", fontsize=7, ha="right", style="italic")
        for j in range(4):
            ax.text(j + 0.5, 3.6, f"{s['demand_left'][j]:g}", fontsize=7, ha="center")
        ax.text(
            0,
            -0.15,
            f"{L['step']} {s['position'] + 1}: x{s['row'] + 1}{s['col'] + 1} = {s['quantity']:g}",
            fontsize=7.5,
        )
    save_fig(fig, out, lang, "F1_decoder")
    return {
        "supply": p.supply.tolist(),
        "demand": p.demand.tolist(),
        "cost": p.cost.tolist(),
        "permutation": perm.tolist(),
    }


def fig_convergence(cfg: Config, out: Path, lang: str, df: pd.DataFrame) -> None:
    """F2: median and interquartile range of the gap against decoder calls, per size (uniform set)."""
    path = convergence_file(cfg.output, "main")
    if path is None:
        return
    cv = pd.read_csv(path)
    inst = df[["instance", "suite", "size"]].drop_duplicates().set_index("instance")
    cv = cv.join(inst, on="instance")
    cv = cv[cv["suite"] == "uniform"]
    base_rs = cfg.budget.rule_id
    base_ga = cfg.ga_base.config_id(cfg.budget, cfg.stagnation)
    cv = cv[((cv["method"] == "RS") & (cv["config"] == base_rs)) | ((cv["method"] != "RS") & (cv["config"] == base_ga))]
    sizes = sorted(cv["size"].unique(), key=size_key)
    L = LABELS[lang]
    cols = 3
    rows = math.ceil(len(sizes) / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(7.0, 2.2 * rows), squeeze=False, constrained_layout=True)
    classical = df[df["method"].isin(["NWC", "LCM", "VAM"]) & (df["suite"] == "uniform")]
    for ax, size in zip(axes.flat, sizes, strict=False):
        sub = cv[cv["size"] == size]
        grid = np.unique(sub["evals"].values)
        for method in STOCHASTIC:
            runs = sub[sub["method"] == method]
            if not len(runs):
                continue
            # carry the last value of each run forward onto the common grid (runs may stop early)
            wide = runs.pivot_table(index="evals", columns=["instance", "seed"], values="gap").reindex(grid).ffill()
            # start where every run has a value (after its initial population); earlier medians would
            # cover only the runs whose first individuals happened to be the best ones
            complete = wide.notna().all(axis=1)
            wide = wide.loc[complete.idxmax() :] if complete.any() else wide
            q = wide.quantile([0.25, 0.5, 0.75], axis=1).T
            st = STYLE[method]
            ax.plot(q.index, q[0.5], color=st["color"], ls=st["ls"], lw=1.2, label=method)
            ax.fill_between(q.index, q[0.25], q[0.75], color=st["color"], alpha=0.18, lw=0)
        for method in ("NWC", "LCM", "VAM"):
            g = classical[(classical["size"] == size) & (classical["method"] == method)]["gap"]
            if len(g):
                ax.axhline(g.median(), color=STYLE[method]["color"], ls=STYLE[method]["ls"], lw=0.9, label=method)
        ax.set_xscale("log")
        ax.set_yscale("symlog", linthresh=1.0)
        ax.set_ylim(bottom=0)
        ax.set_title(size.replace("x", "×"))
        ax.set_xlabel(L["evals"])
        ax.set_ylabel(L["median_gap"])
    for ax in list(axes.flat)[len(sizes) :]:
        ax.axis("off")
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=6, frameon=False)
    save_fig(fig, out, lang, "F2_convergence")


def fig_boxplot(out: Path, lang: str, base: pd.DataFrame) -> None:
    """F3: gap per run, by size and method (uniform set; deterministic methods: one value per instance)."""
    data = base[(base["suite"] == "uniform") & (base["method"] != "LP")]
    sizes = sorted(data["size"].unique(), key=size_key)
    methods = [m for m in METHOD_ORDER if m in set(data["method"]) and m != "LP"]
    L = LABELS[lang]
    fig, axes = plt.subplots(2, 3, figsize=(7.0, 4.6), constrained_layout=True)
    for ax, size in zip(axes.flat, sizes, strict=False):
        vals = [data[(data["size"] == size) & (data["method"] == m)]["gap"].values for m in methods]
        bp = ax.boxplot(vals, patch_artist=True, widths=0.6, showfliers=True, flierprops={"markersize": 2})
        for patch, m in zip(bp["boxes"], methods, strict=True):
            patch.set_facecolor(STYLE[m]["color"])
            patch.set_hatch(STYLE[m]["hatch"])
            patch.set_edgecolor("black")
            patch.set_linewidth(0.6)
        for med in bp["medians"]:
            med.set_color("black")
        ax.set_xticks(range(1, len(methods) + 1), methods, rotation=45, ha="right")
        ax.set_yscale("symlog", linthresh=1.0)
        ax.set_ylim(bottom=0)
        ax.set_title(size.replace("x", "×"))
        ax.set_ylabel(L["gap"])
    for ax in list(axes.flat)[len(sizes) :]:
        ax.axis("off")
    save_fig(fig, out, lang, "F3_gap_boxplot")


def fig_time(out: Path, lang: str, t3: pd.DataFrame, fits: pd.DataFrame) -> None:
    """F4: median time per run against m n, log-log, with the fitted power laws inside the observed range."""
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(3.6, 3.0), constrained_layout=True)
    for method in [m for m in METHOD_ORDER if m in set(t3["method"])]:
        g = t3[t3["method"] == method].sort_values("arcs")
        st = STYLE[method]
        ax.errorbar(
            g["arcs"],
            g["time_median_s"],
            yerr=[g["time_median_s"] - g["time_q1_s"], g["time_q3_s"] - g["time_median_s"]],
            color=st["color"],
            marker=st["marker"],
            ls="none",
            ms=4,
            capsize=2,
            lw=0.8,
            label=method,
            mec="black",
            mew=0.4,
        )
        f = fits[(fits["method"] == method) & (fits["quantity"] == "time per run")] if len(fits) else fits
        if len(f):
            r = f.iloc[0]
            xs = np.geomspace(r["arcs_min"], r["arcs_max"], 50)
            ax.plot(xs, r["a"] * xs ** r["b"], color=st["color"], ls=st["ls"], lw=0.9)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(L["arcs"])
    ax.set_ylabel(L["time"])
    ax.legend(frameon=False)
    save_fig(fig, out, lang, "F4_time_scaling")


def fig_heatmap(out: Path, lang: str, t4: pd.DataFrame) -> None:
    """F5: mean gap of the factorial plan, population x mutation, per size and initialization."""
    if not len(t4):
        return
    L = LABELS[lang]
    sizes = sorted(t4["size"].unique(), key=size_key)
    inits = ["random", "cost-aware"]
    fig, axes = plt.subplots(len(sizes), 2, figsize=(6.4, 2.6 * len(sizes)), squeeze=False, constrained_layout=True)
    for r, size in enumerate(sizes):
        for c, init in enumerate(inits):
            ax = axes[r, c]
            g = t4[(t4["size"] == size) & (t4["initialization"] == init)]
            mat = g.pivot(index="population", columns="mutation_rate", values="gap_mean")
            im = ax.imshow(mat.values, cmap="Greys", aspect="auto")
            vmin, vmax = np.nanmin(mat.values), np.nanmax(mat.values)
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    v = mat.values[i, j]
                    ax.text(
                        j,
                        i,
                        f"{v:.2f}",
                        ha="center",
                        va="center",
                        fontsize=7,
                        color="white" if (v - vmin) > 0.55 * (vmax - vmin) else "black",
                    )
            ax.set_xticks(range(mat.shape[1]), [f"{v:g}" for v in mat.columns])
            ax.set_yticks(range(mat.shape[0]), [str(v) for v in mat.index])
            ax.set_xlabel(L["mutation"])
            ax.set_ylabel(L["population"])
            ax.set_title(f"{size.replace('x', '×')}, {L[init]}")
            fig.colorbar(im, ax=ax, label=L["gap"], shrink=0.85)
    save_fig(fig, out, lang, "F5_factorial_heatmap")


def fig_wheat_map(cfg: Config, out: Path, lang: str) -> dict[str, Any] | None:
    """F6: LP plan of the 2024 wheat scenario; straight lines are modelled flows, not rail routes."""
    ds = cfg.root / "datasets" / "kazakh-wheat"
    world = cfg.root / "platform" / "web" / "public" / "maps" / "eurasia.json"
    inst = cfg.output / "instances" / "applied" / "kazakh-wheat" / "year-2024.json"
    if not (ds.exists() and inst.exists()):
        return None
    from tpga.exact import solve_lp

    net = json.loads((ds / "network.json").read_text(encoding="utf-8"))
    p = TransportProblem.from_json(inst)
    x, z = solve_lp(p)
    L = LABELS[lang]
    fig, ax = plt.subplots(figsize=(7.0, 4.4), constrained_layout=True)
    if world.exists():
        for feat in json.loads(world.read_text(encoding="utf-8"))["features"]:
            geom = feat["geometry"]
            polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
            for poly in polys:
                ring = np.asarray(poly[0])
                ax.fill(ring[:, 0], ring[:, 1], fc="#f2f2f2", ec="#9e9e9e", lw=0.4)
    src, dst = net["warehouses"], net["stores"]
    vmax = float(np.max(x))
    for i, s in enumerate(src):
        for j, d in enumerate(dst):
            if x[i, j] > 0:
                ax.plot(
                    [s["lon"], d["lon"]],
                    [s["lat"], d["lat"]],
                    color="#333333",
                    lw=0.4 + 3.6 * x[i, j] / vmax,
                    alpha=0.75,
                    solid_capstyle="round",
                )
    ax.scatter(
        [s["lon"] for s in src],
        [s["lat"] for s in src],
        s=[8 + 60 * v / float(np.max(p.supply)) for v in p.supply],
        c="white",
        edgecolors="black",
        lw=0.6,
        zorder=3,
        label=L["region"],
    )
    ax.scatter(
        [d["lon"] for d in dst], [d["lat"] for d in dst], s=40, marker="s", c="black", zorder=3, label=L["market"]
    )
    for d in dst:
        ax.annotate(
            d["id"] if lang == "en" else d["name"],
            (d["lon"], d["lat"]),
            xytext=(4, -9),
            textcoords="offset points",
            fontsize=7,
        )
    lons = [v["lon"] for v in src + dst]
    lats = [v["lat"] for v in src + dst]
    ax.set_xlim(min(lons) - 3, max(lons) + 3)
    ax.set_ylim(min(lats) - 2, max(lats) + 2)
    ax.set_aspect(1 / math.cos(math.radians(np.mean(lats))))
    ax.set_xlabel(L["lon"])
    ax.set_ylabel(L["lat"])
    ax.legend(frameon=True, loc="lower left")
    save_fig(fig, out, lang, "F6_wheat_map")
    return {"instance": "kazakh-wheat/year-2024", "lp_cost": z, "flows": int((x > 0).sum())}


# --- documents -------------------------------------------------------------------------------


def numbers(
    cfg: Config,
    df: pd.DataFrame,
    t2: pd.DataFrame,
    t3: pd.DataFrame,
    fits: pd.DataFrame,
    t5: pd.DataFrame,
    t4: pd.DataFrame,
    reach: dict | None,
    env: dict,
    t2b: pd.DataFrame | None = None,
) -> str:
    lines = [
        "# Numbers for the paper",
        "",
        "Every value below is computed by `python -m tpga.experiments.report` from the files named in the",
        "*Source* column. Queries are pandas expressions on the CSV file given; `gap` is",
        "`100 * (z - z*) / z*` with z* the HiGHS optimum of the same instance.",
        "",
        "| Quantity | Value | Definition | Source |",
        "|---|---|---|---|",
    ]

    def add(name: str, value: Any, definition: str, source: str) -> None:
        lines.append(f"| {name} | {_fmt(value, 4)} | {definition} | {source} |")

    base = df[base_mask(df, cfg)]
    add(
        "Runs in raw/runs.csv", len(df), "rows (one per run; LP and classical methods one per instance)", "raw/runs.csv"
    )
    for method in METHOD_ORDER:
        add(
            f"Rows of {method}",
            int((df["method"] == method).sum()),
            "rows with this method",
            f"raw/runs.csv: method == '{method}'",
        )
    add(
        "Infeasible plans",
        int((~df["feasible"].astype(str).str.lower().eq("true")).sum()),
        "rows whose plan failed the independent check",
        "raw/runs.csv: feasible != True",
    )
    for _, r in t2.iterrows():
        if r["suite"] not in ("uniform", "structured"):
            continue
        q = f"suite == '{r['suite']}' and size == '{r['size']}' and method == '{r['method']}' (base config)"
        add(
            f"Mean gap {r['method']} {r['size']} {r['suite']}",
            r["gap_mean"],
            "mean of gap over runs, %",
            f"tables/T2_gap.csv; raw/runs.csv: {q}",
        )
        add(
            f"Median gap {r['method']} {r['size']} {r['suite']}",
            r["gap_median"],
            "median of gap over runs, %",
            f"tables/T2_gap.csv; raw/runs.csv: {q}",
        )
        add(
            f"Share optimal {r['method']} {r['size']} {r['suite']}",
            r["share_optimal"],
            "share of runs with |z - z*| <= 1e-9 max(1, |z*|)",
            f"tables/T2_gap.csv; raw/runs.csv: {q}",
        )
    for _, r in fits.iterrows():
        add(
            f"Exponent b, {r['method']}, {r['quantity']}",
            r["b"],
            f"slope of log10 t on log10(m n), 95% CI [{_fmt(r['b_ci_low'])}, {_fmt(r['b_ci_high'])}], "
            f"{int(r['points'])} instances, m n in [{int(r['arcs_min'])}, {int(r['arcs_max'])}]",
            "tables/T3_time_fit.csv",
        )
    for _, r in t3.iterrows():
        add(
            f"Median time {r['method']} {r['size']}",
            r["time_median_s"],
            "median wall-clock per run, s",
            "tables/T3_time.csv",
        )
    for _, r in t5.iterrows():
        add(
            f"Wilcoxon {r['method_a']} vs {r['method_b']} ({r['suite']}, {r['size']})",
            r["p_holm"],
            f"Holm-adjusted p on per-instance median gaps; n = {int(r['n'])}, "
            f"r = {_fmt(r['rank_biserial_r'])}, Cliff's delta = {_fmt(r['cliffs_delta'])}",
            "tables/T5_tests.csv",
        )
    if len(t4):
        for _, r in t4.iterrows():
            add(
                f"RQ4 mean gap {r['size']} {r['initialization']} P={int(r['population'])} pm={r['mutation_rate']:g}",
                r["gap_mean"],
                "mean gap over 10 instances x runs, %",
                "tables/T4_factorial.csv",
            )
    if t2b is not None and len(t2b):
        for _, r in t2b.iterrows():
            add(
                f"Stopping {r['stopping']} {r['method']} {r['size']}: mean gap",
                r["gap_mean"],
                f"mean gap over runs, %; median decoder calls {_fmt(r['evals_median'])}",
                "tables/T2b_stopping.csv",
            )
    if reach:
        add(
            "Reachability instances",
            reach["instances"],
            "random integer instances checked",
            "reachability.json: instances",
        )
        add(
            "Reachability reproduced",
            reach["reproduced"],
            "decoded plan equals the HiGHS vertex and its cost equals z*",
            "reachability.json: reproduced",
        )
        add(
            "Reachability degenerate vertices",
            reach["degenerate_vertices"],
            "vertices with fewer than m + n - 1 positive cells",
            "reachability.json: degenerate_vertices",
        )
    for name, entries in env.get("phases", {}).items():
        add(
            f"Wall time of phase {name}",
            sum(e["wall_s"] for e in entries) / 3600,
            "hours, sum over invocations",
            "environment.json: phases",
        )
    add(
        "Base-configuration rows",
        len(base),
        "rows used for RQ1-RQ3",
        "raw/runs.csv with the base configuration filter in report.base_mask",
    )
    return "\n".join(lines) + "\n"


def methods_md(cfg: Config, f1: dict[str, Any]) -> str:
    g, b = cfg.ga_base, cfg.budget
    fac = cfg.phase("factorial")
    return f"""# Methods

## Model

Balanced classical transportation problem: minimise sum_ij c_ij x_ij subject to sum_j x_ij = a_i,
sum_i x_ij = b_j, x_ij >= 0. An unbalanced instance gets a zero-cost dummy source or destination
before any method runs; the volume on it is reported in the `dummy_volume` column.

## Greedy decoder

A chromosome is a permutation of the m*n arcs; arc k is (k // n, k mod n).

```
decode(perm):
    a' := a; b' := b; x := 0
    for k in perm:
        if every a'_i = 0: stop
        (i, j) := (k // n, k mod n)
        q := min(a'_i, b'_j)
        if q > 0: x_ij := q; a'_i -= q; b'_j -= q
    return x
```

For a balanced problem with nonnegative data every permutation decodes to a feasible plan; with
integer data the plan is integral. Each positive allocation exhausts a row or a column, so a plan has
at most m + n - 1 positive cells and its support is acyclic (a basic solution); the tests check both
on random instances up to 50x50. Visiting arcs in row-major order gives the north-west corner rule;
visiting them by increasing cost (ties by arc index) gives the least-cost method with that tie rule;
the Vogel order of the cost-aware start gives Vogel's plan (all three checked by tests).

## Genetic algorithm

```
GA(P, pc, pm, t, e, B, S):
    pop := P permutations (random, or cost-aware start); evaluate all (P decoder calls)
    while evaluations + (P - e) <= B and fewer than S generations without improvement:
        new := the e best individuals, with their stored fitness (no decoder call)
        repeat P - e times:
            p1 := tournament of t distinct individuals; p2 := another tournament
            child := OX1(p1, p2) with probability pc, otherwise a copy of p1
            with probability pm swap two distinct random positions of child
            evaluate child (one decoder call)
        pop := new
    return the best individual found
```

* Tournament: t individuals drawn without replacement, the cheapest wins (first drawn on ties).
* OX1 variant: cut points i < j; positions i..j come from p1; the other positions are filled from
  left to right with the genes of p2 in p2's order.
* Mutation: one swap of two distinct positions with probability pm per offspring.
* Base configuration: P = {g.population}, pc = {g.crossover_rate}, pm = {g.mutation_rate},
  t = {g.tournament}, e = {g.elite}.
* Budget: B = clamp({b.factor} * m * n, {b.minimum}, {b.maximum}) decoder calls;
  stagnation S = {cfg.stagnation} generations.
* Random numbers: numpy.random.Generator (PCG64) seeded with seed = {cfg.base_seed} + r for run r = 0..{cfg.runs - 1}.
  All uniforms of a generation are drawn at once; the compiled (numba) and plain-Python kernels give
  identical runs (tested).

### Cost-aware start (GA-cost)

The initial population contains the Vogel order (decodes to the VAM plan), the arcs sorted by cost
(decodes to the LCM plan), permutations sorted by cost plus Gaussian noise with standard deviations
0.05, 0.15 and 0.35 times the standard deviation of the costs, and every fourth further individual a
uniformly random permutation. Because elitism keeps the best individual, **GA-cost is never worse
than the better of LCM and VAM by construction**. The comparison with the classical methods (RQ2)
is therefore made with GA-rand; GA-cost is reported separately.

## Random search (RS)

B uniformly random permutations (Fisher-Yates driven by the same generator), decoded by the same
decoder; the cheapest is kept. RS always uses the full budget B, while the GA may stop earlier by
stagnation, so RS receives at least as many decoder calls as the GA.

## Exact and classical methods

* LP: scipy.optimize.linprog(method="highs"), HiGHS {_highs()}, sparse equality constraints,
  primal and dual feasibility tolerance 1e-9; status 0 required. Time: median of {cfg.lp_repeats} solver calls.
* NWC, LCM, VAM: tpga.classical; tie and degeneracy rules are stated in the module docstring.
  Time: median of {cfg.lp_repeats} calls.

## Factorial plan (RQ4)

Sizes {fac["sizes"]} (uniform set, 10 instances each), population {fac["population"]} x mutation
probability {fac["mutation_rate"]} x start {fac["initialization"]}, {cfg.runs} runs per cell, the same
budget rule and stagnation limit; other parameters as in the base configuration.

## Stopping-rule check

The pilot showed that on large instances the stagnation limit often ends a run long before the
budget is used. As a sensitivity check (not a research question), the base configuration was also
run on the uniform 50×50 and 100×100 instances with the stagnation limit removed (budget only),
with the same seeds; table T2b compares the two stopping rules.

## Timing (RQ3)

The quality phases run one process per logical processor, pinned to it; the processor has
performance and efficiency cores, and each row records the core class. The run times used for RQ3
come from a separate timing phase on performance cores only, with no other phase running; LP times
are medians of {cfg.lp_repeats} solver calls in the same phase.

## Metrics and checks

* gap = 100 (z - z*) / z*; a run is optimal when |z - z*| <= 1e-9 max(1, |z*|).
* Every final plan is re-checked by tpga.verify.check_plan (plain loops, relative tolerance 1e-9);
  an infeasible plan or a cost below z* aborts the task as an experiment error.
* Convergence: the GA records each improvement of the best cost with the decoder call at which it
  happened; the stored curves sample this step function at {cfg.convergence_points} log-spaced budget points.

## Statistics

* Method comparison: Wilcoxon signed-rank test on per-instance median gaps (pairs listed in T5),
  effect sizes: matched-pairs rank-biserial r and Cliff's delta. Two Holm corrections are reported:
  `p_holm` over all rows of T5 and `p_holm_within_size` over the comparisons of one (set, size) group.
  With 10 instances per size the exact two-sided Wilcoxon p-value cannot be below 2/1024 = 0.00195,
  so under the first correction no per-size comparison can fall below 0.05 even when all 10
  differences have the same sign; the pooled rows (80 instances) do not have this floor.
* RQ4: Friedman test over the 16 (population, mutation) cells with instances as blocks, and over
  each factor separately; post-hoc pairwise Wilcoxon tests with Holm correction within each
  (size, start) group; random vs cost-aware start by a Wilcoxon test over matched cells.
* RQ3: least-squares fit of log10 t = log10 a + b log10(m n) on per-instance median times; 95%
  confidence interval of b from the t distribution. No extrapolation outside the observed range.

## Decoder example (F1)

Instance: supply {f1["supply"]}, demand {f1["demand"]}, cost {f1["cost"]};
permutation {f1["permutation"]} (numpy Generator seeded with {cfg.base_seed}).
"""


def _highs() -> str:
    from tpga.experiments.environment import _highs_version

    return _highs_version() or "version unknown"


def limitations_md(cfg: Config, df: pd.DataFrame, env: dict, reach: dict | None) -> str:
    timing_note = (
        "The quality phases ran one pinned process per logical processor on a CPU with performance and "
        "efficiency cores, so their wall-clock times mix two core types (the `cpu_class` column records "
        "which). RQ3 uses the separate timing phase, which ran only on performance cores."
    )
    power = env.get("power_scheme") or "not recorded"
    ac = env.get("on_ac_power")
    items = [
        "**Exact methods solve this problem.** The classical transportation problem is a linear program; "
        "HiGHS returns the optimum in every case here. The GA is studied as a heuristic whose gap and run "
        "time are measured, not as a competitor that could beat the exact method.",
        "**Reachability is empirical.** The reproduction of HiGHS vertices by the decoder was checked on "
        f"{reach['instances'] if reach else 'the generated'} random instances; it is not a theorem for every "
        "instance or for optimal faces "
        "with several vertices.",
        "**Budget sets the run time.** The GA budget grows with m n, so the exponent of the GA's time per run "
        "partly reflects the budget rule; T3 also reports time per decoder call.",
        timing_note,
        f"**Power settings.** Recorded power scheme: `{power}`; on AC power: {ac}. The scheme could not be "
        "changed by the agent (system setting); see environment.json.",
        "**Synthetic sets.** Uniform costs U[1, 100] and Euclidean costs with noise; supplies U[20, 100]. "
        "Conclusions may not transfer to other cost structures or to much larger instances.",
        "**Applied cases are illustrations.** Wheat: supplies and demands come from public statistics "
        "(BNS 2024 harvest table, UN Comtrade/WITS HS 1001), but the supplies are model export quotas "
        "and the costs are a distance formula, not observed rail tariffs. Astana: a modelled network. "
        "They are not used for statistical tests.",
        "**Rail pilot excluded.** `datasets/kazakh-wheat/rail-pilot` has no waybills or paid amounts yet; "
        "no savings can be computed and it is not part of the paper.",
        "**No textbook examples with page references** are stored in the repository; the classical methods "
        "are tested on hand-worked small cases and on random instances against HiGHS.",
        "**Statistical power per size.** Each size has 10 instances. The exact Wilcoxon p-value then has a "
        "floor of 0.00195, and after Holm over all rows of T5 no per-size comparison is significant at 0.05 "
        "even with the same sign on all 10 instances (r = ±1). T5 therefore also gives Holm within each "
        "(set, size) group, and pooled rows over all 80 synthetic instances.",
        "**Stopping rule matters.** The stagnation limit of 200 generations ends many large runs long before "
        "the budget (T2b); results of the base configuration describe the GA with this rule, not the GA's "
        "best attainable quality at the budget.",
        "**LP time at small sizes.** For small instances the measured LP time is dominated by the fixed cost of "
        "the scipy.optimize.linprog call (model set-up and checks), so the fitted exponent of the LP time does "
        "not describe the asymptotic complexity of HiGHS.",
        "**Factorial grid boundary.** In RQ4 the best cells lie at the edge of the grid (largest population and "
        "mutation probability), so the grid does not bracket the best parameter values; the effect directions "
        "hold only inside the tested ranges.",
        "**Timing runs reproduce the quality runs.** The timing phase repeats five seeds of the base GA "
        "configuration on performance cores; its costs are identical to the corresponding rows of raw/runs.csv, "
        "which is checked by the report (NUMBERS.md).",
        "**Single machine.** All runs on one laptop; times are not comparable across machines.",
        "**Wheat source links.** The dataset manifest stores the BNS and Comtrade URLs and table positions; "
        "the downloaded source files themselves are not archived in the repository.",
    ]
    return "# Limitations\n\n" + "\n".join(f"{k}. {t}" for k, t in enumerate(items, 1)) + "\n"


def readme_md(cfg: Config, env: dict, df: pd.DataFrame) -> str:
    phases = env.get("phases", {})
    timing = "\n".join(
        f"| {name} | {sum(e['wall_s'] for e in v) / 3600:.2f} | {sum(e['errors'] for e in v)} |"
        for name, v in phases.items()
    )
    rows = [
        f"| {i.get('recorded_at')} | {', '.join(i.get('phases_run', [])) or '–'} "
        f"| `{(i.get('git_commit') or '–')[:10]}` | {i.get('power_scheme') or '–'} |"
        for i in env.get("invocations", [])
    ]
    invocations = "\n".join(rows) or "| – | – | – | – |"
    return f"""# Artifacts of the computational experiment

Configuration: `{env.get("config")}`. Machine and software: `environment.json` (one snapshot per invocation
of the runner in `invocations`).

| Invocation started | Phases | Code version | Power scheme |
|---|---|---|---|
{invocations}

## Reproduce

```bash
python -m venv .venv && .venv/Scripts/activate      # Linux: source .venv/bin/activate
pip install -e ".[dev]"
python -m tpga.experiments.run --config experiments/paper.yaml       # all phases, resumable
python -m tpga.experiments.report --config experiments/paper.yaml    # tables, figures, documents
```

`--pilot` runs a short pilot and writes `pilot/estimate.json`; `--phase NAME` runs one phase.

## Wall time of the recorded run

| Phase | Hours | Errors |
|---|---|---|
{timing}

Rows in `raw/runs.csv`: {len(df)}.

## Contents

* `instances/` — every instance as JSON; `instances/manifest.json` gives seed, SHA-256 and provenance.
* `raw/runs.csv` — one row per run (LP and classical methods: one row per instance); `raw/timing.csv`
  — RQ3 timing phase on performance cores; `raw/convergence/*.csv.gz` (+ `.parquet`) — best cost at
  log-spaced decoder-call counts (the runner appends to plain `.csv`; archived gzip-compressed).
* `reachability.json` — decoder reproduction of HiGHS vertices.
* `tables/` — T1 instance sets, T2 gap, T3 time and fits, T4 factorial plan (+ tests), T5 method
  comparison tests, T6 applied cases; CSV and Markdown.
* `figures/en`, `figures/ru` — F1 decoder example, F2 convergence, F3 gap boxplots, F4 time scaling,
  F5 factorial heat map, F6 wheat map; PNG (600 dpi) and PDF, Times New Roman.
* `METHODS.md`, `LIMITATIONS.md`, `NUMBERS.md` — method description, limitations, every number with its source.
"""


def generate(cfg: Config) -> dict[str, Any]:
    out = cfg.output
    df = load_runs(cfg)
    timing_path = out / "raw" / "timing.csv"
    timing = pd.read_csv(timing_path) if timing_path.exists() else None
    if timing is not None:
        timing["arcs"] = timing["m"] * timing["n"]
    env = (
        json.loads((out / "environment.json").read_text(encoding="utf-8"))
        if (out / "environment.json").exists()
        else {}
    )
    reach_path = out / "reachability.json"
    reach = json.loads(reach_path.read_text(encoding="utf-8")) if reach_path.exists() else None
    base = df[base_mask(df, cfg)]
    tables = out / "tables"
    t1 = table_instances(cfg, df)
    write_table(t1, tables / "T1_instances", "T1. Instance sets")
    t2 = gap_summary(base)
    write_table(
        t2,
        tables / "T2_gap",
        "T2. Gap to the HiGHS optimum by set, size and method",
        "Base configuration. Deterministic methods: one run per instance. gap in %.",
    )
    t3, fits = time_tables(cfg, base, timing[base_mask(timing, cfg)] if timing is not None else None)
    write_table(
        t3,
        tables / "T3_time",
        "T3. Wall-clock time per run",
        "Timing phase on performance cores (raw/timing.csv) when present.",
    )
    write_table(fits, tables / "T3_time_fit", "T3b. Fits t = a (m n)^b on per-instance median times")
    t4, t4s = factorial_tables(cfg, df)
    write_table(t4, tables / "T4_factorial", "T4. Factorial plan (RQ4): gap by population, mutation and start")
    write_table(t4s, tables / "T4_factorial_tests", "T4b. Tests of the factorial plan")
    t5 = comparison_tests(synthetic(base))
    write_table(
        t5,
        tables / "T5_tests",
        "T5. Paired comparison of methods on per-instance median gaps",
        "Wilcoxon signed-rank, Holm correction over all rows. "
        "GA-cost is not worse than LCM and VAM by construction (its start contains both plans).",
    )
    t6 = applied_table(base)
    write_table(t6, tables / "T6_applied", "T6. Applied cases (illustration)")
    t2b = stopping_table(cfg, df)
    if len(t2b):
        write_table(
            t2b,
            tables / "T2b_stopping",
            "T2b. Sensitivity to the stopping rule: stagnation limit vs. budget only",
            "Same instances, seeds and parameters; the only difference is the stagnation limit. "
            "Wilcoxon on per-instance median gaps (with limit vs. without).",
        )
    family = setup_fonts()
    figs = out / "figures"
    f1: dict[str, Any] = {}
    for lang in ("en", "ru"):
        f1 = fig_decoder(cfg, figs, lang)
        fig_convergence(cfg, figs, lang, df)
        fig_boxplot(figs, lang, base)
        fig_time(figs, lang, t3, fits)
        fig_heatmap(figs, lang, t4)
        fig_wheat_map(cfg, figs, lang)
    for name in ("main", "applied", "stopping"):
        src = convergence_file(out, name)
        if src is not None:
            pd.read_csv(src).to_parquet(out / "raw" / "convergence" / f"{name}.parquet", index=False)
    text = numbers(cfg, df, t2, t3, fits, t5, t4, reach, env, t2b)
    if timing is not None and len(timing):
        keys = ["instance", "method", "config", "seed"]
        ga = timing[timing["method"].isin(list(GA_METHODS))]
        both = ga.merge(df[[*keys, "cost"]], on=keys, suffixes=("_timing", "_runs"))
        same = int((both["cost_timing"] == both["cost_runs"]).sum())
        text += (
            f"| Timing runs with the same cost as in raw/runs.csv | {same} of {len(both)} "
            f"| GA runs of the timing phase matched by instance, method, configuration and seed; equality of cost "
            f"| raw/timing.csv joined with raw/runs.csv |\n"
        )
    (out / "NUMBERS.md").write_text(text, encoding="utf-8")
    (out / "METHODS.md").write_text(methods_md(cfg, f1), encoding="utf-8")
    (out / "LIMITATIONS.md").write_text(limitations_md(cfg, df, env, reach), encoding="utf-8")
    (out / "README.md").write_text(readme_md(cfg, env, df), encoding="utf-8")
    summary = {"rows": len(df), "font": family, "tables": sorted(p.name for p in tables.glob("*.csv"))}
    (out / "report.json").write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m tpga.experiments.report", description=__doc__)
    ap.add_argument("--config", required=True)
    args = ap.parse_args(argv)
    print(json.dumps(generate(Config.load(args.config)), indent=1))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
