"""Figures of the v0.4 report, each in English and Russian (PNG 600 dpi and PDF without a timestamp)."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib import font_manager  # noqa: E402

from tpga.experiments.reporting.common import size_key  # noqa: E402

LABELS = {
    "en": {
        "gap": "Gap to the LP optimum, %",
        "gap_norm": "Normalised gap (Z - Z*) / (Z_rand - Z*)",
        "evals": "Decoder calls",
        "arcs": "Number of arcs m n",
        "time": "Time, s",
        "size": "Instance size",
        "population": "Population size",
        "mutation": "Mutation",
    },
    "ru": {
        "gap": "Отклонение от оптимума ЛП, %",
        "gap_norm": "Нормированное отклонение (Z - Z*) / (Z_rand - Z*)",
        "evals": "Вызовы декодера",
        "arcs": "Число дуг m n",
        "time": "Время, с",
        "size": "Размер задачи",
        "population": "Размер популяции",
        "mutation": "Мутация",
    },
}
LANGS = ("en", "ru")


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


def save(fig: plt.Figure, out: Path, lang: str, name: str) -> list[str]:
    d = out / lang
    d.mkdir(parents=True, exist_ok=True)
    fig.savefig(d / f"{name}.png", dpi=600)
    fig.savefig(d / f"{name}.pdf", metadata={"CreationDate": None})
    plt.close(fig)
    return [f"{lang}/{name}.png", f"{lang}/{name}.pdf"]


def boxplot(runs: pd.DataFrame, out: Path, value: str = "gap") -> list[str]:
    """F2 / F2n: per-instance median gap by method, uniform set, one panel per size."""
    df = runs[
        runs["phase"].isin(["reference", "main"])
        & (runs["set"] == "uniform")
        & (runs["method"] != "LP")
        & (runs["method"] != "LP-ortools")
    ]
    if not len(df):
        return []
    med = df.groupby(["size", "instance", "method"])[value].median().reset_index()
    sizes = sorted(med["size"].unique(), key=size_key)
    methods = [
        m
        for m in [
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
        if m in set(med["method"])
    ]
    files: list[str] = []
    for lang in LANGS:
        fig, axes = plt.subplots(1, len(sizes), figsize=(1.6 * len(sizes) + 1, 3.2), sharey=False, squeeze=False)
        for ax, size in zip(axes[0], sizes, strict=True):
            sub = med[med["size"] == size]
            data = [sub[sub["method"] == m][value].to_numpy() for m in methods]
            ax.boxplot(data, widths=0.6, showfliers=True, flierprops={"markersize": 2})
            ax.set_xticks(range(1, len(methods) + 1), methods, rotation=90, fontsize=6)
            ax.set_title(size)
        axes[0][0].set_ylabel(LABELS[lang][value])
        fig.tight_layout()
        files += save(fig, out, lang, f"boxplot_{value}")
    return files


def convergence(curves: pd.DataFrame, runs: pd.DataFrame, out: Path) -> list[str]:
    """F3: median best gap against decoder calls (convergence rows of the ``main`` phase)."""
    if not len(curves):
        return []
    keys = runs[runs["phase"] == "main"][["key", "method", "size"]]
    c = curves.merge(keys, on="key")
    if not len(c):
        return []
    sizes = sorted(c["size"].unique(), key=size_key)
    files: list[str] = []
    for lang in LANGS:
        fig, axes = plt.subplots(1, len(sizes), figsize=(2.6 * len(sizes), 2.8), squeeze=False)
        for ax, size in zip(axes[0], sizes, strict=True):
            sub = c[c["size"] == size]
            for method, g in sub.groupby("method"):
                line = g.groupby("evals")["gap"].median()
                ax.plot(line.index, line.to_numpy(), label=method, lw=1)
            ax.set_xscale("log")
            ax.set_title(size)
            ax.set_xlabel(LABELS[lang]["evals"])
        axes[0][0].set_ylabel(LABELS[lang]["gap"])
        axes[0][-1].legend(fontsize=6)
        fig.tight_layout()
        files += save(fig, out, lang, "convergence")
    return files


def time_scaling(runs: pd.DataFrame, fits: pd.DataFrame, out: Path) -> list[str]:
    """F4: time against m n on log-log axes with the fitted lines of both ranges."""
    t = runs[runs["phase"] == "timing"]
    if not len(t):
        return []
    per = t.groupby(["method", "instance"]).agg(arcs=("arcs", "first"), t=("time_s", "median")).reset_index()
    files: list[str] = []
    for lang in LANGS:
        fig, ax = plt.subplots(figsize=(4.5, 3.2))
        for method, g in per.groupby("method"):
            pts = ax.loglog(g["arcs"], g["t"], "o", ms=2.5, label=method)[0]
            for _, f in fits[fits["method"] == method].iterrows() if len(fits) else []:
                xs = np.geomspace(f["x_min"], f["x_max"], 20)
                ax.loglog(
                    xs, f["a"] * xs ** f["b"], "-" if f["range"] == "all sizes" else "--", color=pts.get_color(), lw=0.8
                )
        ax.set_xlabel(LABELS[lang]["arcs"])
        ax.set_ylabel(LABELS[lang]["time"])
        ax.legend(fontsize=6)
        fig.tight_layout()
        files += save(fig, out, lang, "time_scaling")
    return files


def factorial_heatmap(t4: pd.DataFrame, out: Path) -> list[str]:
    """F5: median gap per (population, mutation) cell, one panel per size and start."""
    if not len(t4):
        return []
    panels = sorted(
        {(s, i) for s, i in t4[["size", "initialization"]].itertuples(index=False)},
        key=lambda p: (size_key(p[0]), p[1]),
    )
    files: list[str] = []
    for lang in LANGS:
        fig, axes = plt.subplots(1, len(panels), figsize=(3.2 * len(panels), 3.2), squeeze=False)
        for ax, (size, init) in zip(axes[0], panels, strict=True):
            sub = t4[(t4["size"] == size) & (t4["initialization"] == init)]
            grid = sub.pivot_table(index="mutation", columns="population", values="gap_median")
            im = ax.imshow(grid.to_numpy(), aspect="auto", cmap="viridis")
            ax.set_xticks(range(grid.shape[1]), [str(c) for c in grid.columns])
            ax.set_yticks(range(grid.shape[0]), list(grid.index), fontsize=6)
            ax.set_xlabel(LABELS[lang]["population"])
            ax.set_title(f"{size}, {init}")
            fig.colorbar(im, ax=ax, shrink=0.8)
        axes[0][0].set_ylabel(LABELS[lang]["mutation"])
        fig.tight_layout()
        files += save(fig, out, lang, "factorial_heatmap")
    return files
