"""Report modules of v0.4 on small synthetic record sets whose correct answers are known in advance."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tpga.experiments.reporting import (
    build,
    stats,
    t2_gap,
    t3_time,
    t4_factorial,
    t5_methods,
    t6_initialisation,
    t7_stopping,
    t8_lp_scaling,
)
from tpga.experiments.reporting.common import load_runs
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.methods import key_of
from tpga.experiments.v2.storage import PartWriter


def rec(
    phase: str,
    set_: str,
    size: str,
    inst: str,
    method: str,
    gap: float,
    seed: int | None = 0,
    config: str = "-",
    **extra: object,
) -> dict[str, object]:
    m, n = (int(v) for v in size.split("x"))
    r: dict[str, object] = {
        "phase": phase,
        "set": set_,
        "size": size,
        "m": m,
        "n": n,
        "instance": inst,
        "method": method,
        "config": config,
        "seed": seed,
        "gap": gap,
        "gap_norm": gap / 100.0,
        "optimal": gap == 0,
        "time_s": 1.0,
        "evals": 100,
        "budget": 100,
        "best_eval": 50,
        "stop_reason": "budget",
        "cpu_class": 1,
        "cost": 100 + gap,
    }
    r.update(extra)
    return r


def frame(rows: list[dict[str, object]]) -> pd.DataFrame:
    for r in rows:
        r["key"] = key_of(r)
    df = pd.DataFrame(rows)
    df["arcs"] = df["m"] * df["n"]
    return df


# --- statistics ----------------------------------------------------------------------------------------------


def test_format_p_and_holm() -> None:
    assert stats.format_p(0.0004) == "< 0.001"
    assert stats.format_p(0.0123) == "0.012"
    assert stats.holm([0.01, 0.04, 0.03]) == pytest.approx([0.03, 0.06, 0.06])


def test_hodges_lehmann_exact_ci() -> None:
    est, lo, hi, method = stats.hodges_lehmann(np.arange(1, 11, dtype=float))
    assert (est, lo, hi) == (5.5, 3.0, 8.0)
    assert method.startswith("exact")


def test_paired_constant_shift() -> None:
    y = np.arange(10, dtype=float) * 3
    res = stats.paired(y - 2.0 - np.arange(10) * 0.01, y)
    assert res["wins_x"] == 10 and res["wins_y"] == 0
    assert res["p"] == pytest.approx(2 / 1024)  # exact two-sided, all ten differences negative
    assert res["rank_biserial_r"] == pytest.approx(-1.0)
    assert -2.1 < res["hl_shift"] < -2.0


def test_friedman_kendall_w() -> None:
    m = np.tile(np.arange(4, dtype=float), (6, 1))
    fr = stats.friedman(m)
    assert fr["kendall_w"] == pytest.approx(1.0)
    assert fr["blocks"] == 6 and fr["treatments"] == 4


def test_loglog_fit_recovers_exponent() -> None:
    x = np.array([25, 100, 400, 2500, 10000, 40000], dtype=float)
    f = stats.loglog_fit(x, 1e-6 * x**1.5)
    assert f["b"] == pytest.approx(1.5) and f["a"] == pytest.approx(1e-6) and f["r2"] == pytest.approx(1.0)


# --- tables --------------------------------------------------------------------------------------------------


def test_t4_uses_the_factorial_phase_only() -> None:
    """The v0.3.0 T4 mixed in rows of other phases; here a main-phase row with the same id must not count."""
    cfg = "P20-pc0.9-t3-e2-swap_count:3-random-budget"
    rows = [
        rec("factorial", "uniform", "20x20", f"i{i}", "GA-rand", 1.0, seed=s, config=cfg)
        for i in range(3)
        for s in range(2)
    ]
    rows += [rec("main", "uniform", "20x20", "i0", "GA-rand", 99.0, seed=s, config=cfg) for s in range(5)]
    t = t4_factorial.table(frame(rows))
    assert len(t) == 1
    assert t["runs"].iloc[0] == 6
    assert t["gap_mean"].iloc[0] == pytest.approx(1.0)


def test_t4_friedman_and_posthoc() -> None:
    rows = []
    for i in range(8):
        for pop, base in ((20, 3.0), (50, 2.0), (100, 1.0)):
            for mut in ("swap_count:1", "swap_count:3", "swap_count:10"):
                cfg = f"P{pop}-pc0.9-t3-e2-{mut}-random-budget"
                rows.append(rec("factorial", "uniform", "20x20", f"i{i}", "GA-rand", base * (1 + 0.05 * i), config=cfg))
    cells = t4_factorial.table(frame(rows))
    by_pop = cells.groupby("population")["mean_rank"].mean()
    assert by_pop[100] == pytest.approx(2.0) and by_pop[20] == pytest.approx(8.0)  # 3 tied cells per population
    tests = t4_factorial.tests(frame(rows))
    pop = tests[tests["test"] == "Friedman, population"].iloc[0]
    assert pop["kendall_w"] == pytest.approx(1.0)
    post = tests[tests["test"].str.startswith("Wilcoxon population")]
    assert len(post) == 3
    assert set(post["p_text"]) == {"0.023"}  # exact 2/256 = 0.0078 for n=8, times 3 after Holm
    mut = tests[tests["test"] == "Friedman, mutation"].iloc[0]
    assert mut["p"] == 1.0 and mut["kendall_w"] == 0.0  # every block tied: no evidence of an effect


def test_t6_one_pair_per_instance() -> None:
    rows = []
    for i in range(10):
        for cell in ("swap_count:1", "swap_count:3"):
            for s in range(3):
                for init, g in (("random", 5.0 + i), ("cost-aware", 4.0 + i)):
                    cfg = f"P20-pc0.9-t3-e2-{cell}-{init}-budget"
                    rows.append(rec("factorial", "uniform", "20x20", f"i{i}", "GA", g, seed=s, config=cfg))
    t = t6_initialisation.table(frame(rows))
    assert t["pairs"].iloc[0] == 10
    assert t["hl_shift"].iloc[0] == pytest.approx(-1.0)
    assert t["ties"].iloc[0] == 0 and t["wins_x"].iloc[0] == 10
    # random / cost-aware per instance: (5 + i) / (4 + i), median over i = 0..9 at i = 4.5
    assert t["ratio_median"].iloc[0] == pytest.approx(float(np.median([(5 + i) / (4 + i) for i in range(10)])))
    assert t["reduction_pp_median"].iloc[0] == pytest.approx(1.0)
    assert t["cells_cost_aware_lower_share"].iloc[0] == 1.0


def test_t5_per_size_families_with_holm() -> None:
    rows = []
    for size in ("20x20", "50x50"):
        for i in range(10):
            rows.append(rec("reference", "uniform", size, f"{size}-{i}", "VAM", 10.0 + i, seed=None))
            rows.append(rec("reference", "uniform", size, f"{size}-{i}", "NWC", 50.0 + i, seed=None))
            for s in range(3):
                rows.append(rec("main", "uniform", size, f"{size}-{i}", "GA-rand-base", 5.0 + i + 0.1 * i * i, seed=s))
    df = frame(rows)
    t = t5_methods.table(df)
    assert set(t["size"]) == {"20x20", "50x50"}
    vam = t[(t["method_b"] == "VAM") & (t["size"] == "20x20")].iloc[0]
    assert vam["n"] == 10 and vam["wins_x"] == 8  # 5 + i + 0.1 i^2 < 10 + i for i < sqrt(50), i = 0..7
    fam = t[t["size"] == "20x20"]
    assert fam["p_holm"].min() >= fam["p"].min()
    pooled = t5_methods.appendix_pooled(df)
    assert set(pooled["size"]) == {"all sizes"} and pooled["n"].max() == 20


def test_t2_excludes_lp_scaling_and_counts_runs() -> None:
    rows = [rec("main", "uniform", "20x20", "a", "RS", 3.0, seed=s) for s in range(4)]
    rows += [rec("timing", "lp_scaling", "100x100", "b", "LP", 0.0, seed=None)]
    t = t2_gap.table(frame(rows))
    assert list(t["method"]) == ["RS"] and t["runs"].iloc[0] == 4


def test_t3_fits_two_ranges() -> None:
    rows = []
    for side in (5, 10, 20, 50, 100, 200):
        for i in range(2):
            rows.append(
                rec(
                    "timing",
                    "uniform",
                    f"{side}x{side}",
                    f"{side}-{i}",
                    "LP",
                    0.0,
                    seed=None,
                    time_s=2e-6 * (side * side) ** 1.2,
                )
            )
    fits = t3_time.fits(frame(rows))
    per_run = fits[fits["measure"] == "time per run"]
    assert set(per_run["range"]) == {"all sizes", "m n >= 2500"}
    assert per_run["b"].to_numpy() == pytest.approx([1.2, 1.2])
    per_call = fits[fits["measure"] == "time per decoder call"]  # evals = 100 in every record
    assert per_call["b"].to_numpy() == pytest.approx([1.2, 1.2])


def test_t7_pairs_budget_with_stagnation() -> None:
    rows = []
    for i in range(6):
        rows.append(rec("main", "uniform", "20x20", f"i{i}", "GA-rand-base", 1.0 + i))
        rows.append(rec("stagnation", "uniform", "20x20", f"i{i}", "GA-rand-base", 3.0 + i))
    t = t7_stopping.table(frame(rows))
    stag = t[t["stop"].str.startswith("0.1")].iloc[0]
    assert stag["hl_shift"] == pytest.approx(2.0)
    assert stag["stopped_early_share"] == 0.0 and stag["budget_used_median"] == 1.0
    assert stag["best_found_median"] == 0.5


def test_t8_detects_disagreement() -> None:
    rows = [
        rec("timing", "lp_scaling", "100x100", "x", "LP", 0.0, seed=None, cost=10.0, build_s=0.1),
        rec("timing", "lp_scaling", "100x100", "x", "LP-ortools", 0.0, seed=None, cost=11.0, build_s=0.1),
        rec("timing", "lp_scaling", "100x100", "y", "LP", 0.0, seed=None, cost=10.0, build_s=0.1),
        rec("timing", "lp_scaling", "100x100", "y", "LP-ortools", 0.0, seed=None, cost=10.0, build_s=0.1),
    ]
    df = frame(rows)
    assert list(t8_lp_scaling.agreement(df)["instance"]) == ["x"]
    assert len(t8_lp_scaling.table(df)) == 2


# --- end to end ----------------------------------------------------------------------------------------------


def test_generate_on_partial_and_full_records(tmp_path: Path) -> None:
    cfg = ConfigV2({"output": str(tmp_path / "out")}, tmp_path / "cfg.yaml")
    empty = build.generate(cfg)
    assert empty["runs"] == 0
    assert "has not been run" in (tmp_path / "out" / "tables" / "T5_methods_gap.md").read_text(encoding="utf-8")

    rows = []
    for i in range(4):
        rows.append(rec("reference", "uniform", "20x20", f"i{i}", "VAM", 10.0 + i, seed=None))
        for s in range(2):
            rows.append(rec("main", "uniform", "20x20", f"i{i}", "GA-rand-base", 2.0 + i, seed=s))
    writer = PartWriter(tmp_path / "out" / "raw" / "runs", "runs")
    writer.add(rows)
    writer.flush()
    assert len(load_runs(tmp_path / "out")) == len(rows)
    res = build.generate(cfg)
    assert res["tables"]["T2_gap"] == 2
    assert res["phases"] == {"main": 8, "reference": 4}
    assert any(f.endswith("boxplot_gap.pdf") for f in res["figures"])
    assert json.loads((tmp_path / "out" / "report.json").read_text(encoding="utf-8"))["runs"] == 12


def test_generate_builds_every_figure(tmp_path: Path) -> None:
    """Timing, factorial and convergence records produce the time, heatmap and convergence figures."""
    rows: list[dict[str, object]] = []
    for side in (20, 50, 100):
        size = f"{side}x{side}"
        for i in range(3):
            inst = f"u{size}-{i}"
            rows.append(rec("reference", "uniform", size, inst, "VAM", 10.0 + i, seed=None))
            rows.append(
                rec(
                    "timing",
                    "uniform",
                    size,
                    inst,
                    "LP",
                    0.0,
                    seed=None,
                    time_s=1e-6 * side**3,
                    presolve_s=0.01,
                    build_s=0.02,
                    wrapper_s=0.03,
                )
            )
            for s in range(2):
                rows.append(rec("main", "uniform", size, inst, "GA-rand-tuned", 2.0 + i, seed=s))
                rows.append(rec("timing", "uniform", size, inst, "GA-rand-tuned", 1.0, seed=s, time_s=1e-5 * side**2))
    for i in range(3):
        for pop in (20, 50):
            for mut in ("swap_count:1", "swap_count:3"):
                for init in ("random", "cost-aware"):
                    rows.append(
                        rec(
                            "factorial",
                            "uniform",
                            "20x20",
                            f"f{i}",
                            "GA",
                            1.0 + i + pop / 100,
                            config=f"P{pop}-pc0.9-t3-e2-{mut}-{init}-budget",
                        )
                    )
    for r in rows:
        r["key"] = key_of(r)
    curves = [
        {"key": r["key"], "evals": e, "best_cost": 100.0, "gap": 10.0 / e}
        for r in rows
        if r["phase"] == "main"
        for e in (1, 10, 100)
    ]
    out = tmp_path / "out"
    w = PartWriter(out / "raw" / "runs", "runs")
    w.add(rows)
    w.flush()
    c = PartWriter(out / "raw" / "curves", "curves")
    c.add(curves)
    c.flush()
    res = build.generate(ConfigV2({"output": str(out)}, tmp_path / "cfg.yaml"))
    names = {Path(f).stem for f in res["figures"]}
    assert {"boxplot_gap", "boxplot_gap_norm", "convergence", "time_scaling", "factorial_heatmap"} <= names
    assert res["tables"]["T3_fits"] >= 2 and res["tables"]["T4_tests"] > 0
    t3 = (out / "tables" / "T3_time.csv").read_text(encoding="utf-8")
    assert "presolve_median_s" in t3 and "\r" not in t3


def test_example1_reproduces_the_article() -> None:
    from tpga.experiments.reporting import t0_checks

    t = t0_checks.example1().set_index("method")
    assert t["cost"].to_dict() == {
        "NWC": 2445.0,
        "LCM": 2345.0,
        "VAM": 2310.0,
        "Decoder, random permutation": 2835.0,
        "Decoder, leaf-elimination order": 2220.0,
        "LP optimum (HiGHS)": 2220.0,
    }
    assert t.loc["NWC", "gap"] == pytest.approx(10.135, abs=1e-3)
    assert (t["positive"] == 6).all()  # m + n - 1: no plan is degenerate
    assert t.loc["Decoder, random permutation", "shipments_in_order"].startswith("x11 = 50, x24 = 25, x23 = 40")


def test_checks_counts_records_failures_and_residuals(tmp_path: Path) -> None:
    from tpga.experiments.reporting import t0_checks

    (tmp_path / "logs").mkdir()
    (tmp_path / "logs" / "errors.jsonl").write_text('{"phase": "main", "error": "x"}\n', encoding="utf-8")
    rows = [
        rec("main", "uniform", "5x5", "a", "RS", 1.0, seed=s, feasible=True, max_residual=1e-12 * s, dummy_volume=0.0)
        for s in range(3)
    ]
    rows.append(rec("representation", "uniform", "5x5", "a", "random-parents", 0.0, seed=None))
    t = t0_checks.checks(tmp_path, frame(rows)).set_index("phase")
    assert t.loc["main", "records"] == 3 and t.loc["main", "failed_runs"] == 1
    assert t.loc["main", "plans_infeasible"] == 0 and t.loc["main", "max_residual"] == pytest.approx(2e-12)
    assert t.loc["total", "records"] == 4 and t.loc["representation", "plans_checked"] == 0
