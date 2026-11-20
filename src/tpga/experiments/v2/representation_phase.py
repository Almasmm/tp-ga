"""Phase ``representation`` (non-confirmatory, amendment 3): tasks and their execution.

One task per instance with random parents, and one per instance, tuned GA and seed with the populations of
that GA run at fractions of the budget. A task returns a short run record (stored with the other runs, so
an interrupted phase resumes like any other) and long-format rows stored in ``raw/representation``.
"""

from __future__ import annotations

import time
import zlib
from typing import Any

import numpy as np

from tpga.analysis import representation as rep
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.instances import InstanceV2, select
from tpga.experiments.v2.tasks import _base, method_params, stochastic_tasks

PHASE = "representation"
STORE = "representation"


def operators(cfg: ConfigV2) -> list[list[Any]]:
    """[label, mode, strength]: every mutation setting of the factorial plan and the tuned GA settings."""
    out = [
        [f"{mode}:{level:g}", mode, float(level)]
        for mode, levels in cfg.phase("factorial")["mutation"].items()
        for level in levels
    ]
    for name in ("GA-rand-tuned", "GA-cost-tuned"):
        _, p, _ = method_params(cfg, name)
        mode = p["mutation_mode"]
        strength = p["mutation_rate"] if mode == "swap_fixed" else p["mutation_strength"]
        out.append([f"{name} ({mode}:{float(strength):.3g})", mode, float(strength)])
    return out


def tasks(cfg: ConfigV2, items: list[InstanceV2]) -> list[dict[str, Any]]:
    spec = cfg.phase(PHASE)
    chosen = select(items, spec["sets"])
    common = {
        "kind": "representation",
        "operators": operators(cfg),
        "random_parents": int(spec["random_parents"]),
        "snapshots": [float(f) for f in spec["snapshots"]],
        "crossover_pairs": int(spec["crossover_pairs"]),
        "base_seed": int(cfg.raw["base_seed"]),
    }
    out = [
        {
            **_base(cfg, PHASE, inst),
            **common,
            "part": "random",
            "method": "random-parents",
            "config": f"R{common['random_parents']}",
        }
        for inst in chosen
    ]
    limit = {str(k): int(v) for k, v in (spec.get("ga_instances_by_size") or {}).items()}
    ga_items = [i for i in chosen if int(i.id.split("-")[1]) < limit.get(i.size, 10**9)]
    for t in stochastic_tasks(
        cfg, PHASE, ga_items, list(spec["ga_methods"]), "budget", cfg.seeds(int(spec["ga_seeds"]))
    ):
        out.append({**t, **common, "part": "ga"})
    return out


def _rng(task: dict[str, Any], salt: int) -> np.random.Generator:
    seed = int(task["seed"]) if task.get("seed") is not None else 0
    return np.random.default_rng([task["base_seed"], zlib.crc32(task["instance"].encode()), seed, salt])


def execute(task: dict[str, Any], problem: Any) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    from tpga.experiments.v2.methods import ga_config  # local: methods imports this module

    t0 = time.perf_counter()
    dec = rep.Decoder(problem, float(task["decoder_tol"]))
    z = float(task["z_star"])
    base = {k: task.get(k) for k in ("set", "size", "m", "n", "instance", "seed")}
    base["mn"] = int(task["m"]) * int(task["n"])
    rows: list[dict[str, Any]] = []

    def add(
        source: str,
        snapshot: float | None,
        measure: str,
        operator: str | None,
        values: dict[str, float],
        k: float | None = None,
    ) -> None:
        for metric, value in values.items():
            rows.append(
                {
                    **base,
                    "source": source,
                    "snapshot": snapshot,
                    "measure": measure,
                    "operator": operator,
                    "k": k,
                    "metric": metric,
                    "value": value,
                }
            )

    def mutation_rows(source: str, snapshot: float | None, parents: np.ndarray, costs: np.ndarray, salt: int) -> None:
        rng = _rng(task, salt)
        for label, mode, strength in task["operators"]:
            add(source, snapshot, "neutrality", label, rep.neutrality(dec, parents, costs, mode, strength, rng))

    def locality_rows(source: str, snapshot: float | None, parents: np.ndarray, costs: np.ndarray, salt: int) -> None:
        for r in rep.locality(dec, parents, costs, z, _rng(task, salt)):
            k = r.pop("k")
            add(source, snapshot, "locality", None, r, None if np.isnan(k) else k)

    extra: dict[str, Any] = {}
    if task["part"] == "random":
        parents = rep.random_parents(dec, int(task["random_parents"]), _rng(task, 1))
        costs = dec.costs(parents)
        add("random", None, "prefix", None, rep.prefix_rows(dec, parents))
        mutation_rows("random", None, parents, costs, 2)
        locality_rows("random", None, parents, costs, 3)
    else:
        from tpga.ga import run_ga

        snaps = rep.Snapshots(int(task["budget"]), tuple(task["snapshots"]))
        result = run_ga(problem, ga_config(task), population_hook=snaps)
        pops = {**snaps.kept, 1.0: snaps.final()}
        src = task["method"]
        add(src, 1.0, "prefix", None, rep.prefix_rows(dec, pops[1.0]))
        for i, f in enumerate(sorted(pops)):
            costs = dec.costs(pops[f])
            mutation_rows(src, f, pops[f], costs, 10 + i)
            if f == 0.5:
                locality_rows(src, f, pops[f], costs, 20)
                add(
                    src,
                    f,
                    "heritability",
                    "OX1",
                    rep.heritability(dec, pops[f], int(task["crossover_pairs"]), _rng(task, 30)),
                )
        extra = {"evals": result.evaluations, "ga_cost": result.cost, "ga_time_s": result.runtime_s}
    record = {k: task.get(k) for k in ("phase", "set", "instance", "method", "config", "seed", "size", "m", "n")}
    record.update(time_s=time.perf_counter() - t0, rows=len(rows), rows_store=STORE, z_star=z, **extra)
    return record, rows
