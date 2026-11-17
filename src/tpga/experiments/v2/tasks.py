"""Task lists of the v0.4 phases, built from the configuration and the frozen tuning result."""

from __future__ import annotations

from itertools import product
from typing import Any

from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.instances import InstanceV2, select

GA_DEFAULTS = {"crossover_rate": 0.9, "tournament": 3, "elite": 2, "mutation_rate": 0.2, "mutation_mode": "swap_fixed"}


def ga_config_id(p: dict[str, Any], init: str, stop: str) -> str:
    mode = p.get("mutation_mode", "swap_fixed")
    strength = p.get("mutation_rate") if mode == "swap_fixed" else p.get("mutation_strength")
    return (
        f"P{int(p['population'])}-pc{float(p['crossover_rate']):g}-t{int(p['tournament'])}-e{int(p['elite'])}"
        f"-{mode}:{float(strength or 0):g}-{init}-{stop}"
    )


def sa_config_id(p: dict[str, Any], init: str, stop: str) -> str:
    return (
        f"ins{float(p['insertion_probability']):.3g}-acc{float(p['initial_acceptance']):.3g}"
        f"-fr{float(p['final_ratio']):.3g}-{init}-{stop}"
    )


def stop_spec(spec: Any, budget: int) -> tuple[dict[str, Any], str]:
    """Stop rule of a phase -> (fields for the run, short label for the config id)."""
    if spec in (None, "budget"):
        return {}, "budget"
    if "stagnation_evaluations_fraction" in spec:
        s = max(1, int(round(float(spec["stagnation_evaluations_fraction"]) * budget)))
        return {"stagnation_evaluations": s}, f"stagE{float(spec['stagnation_evaluations_fraction']):g}"
    if "stagnation_generations" in spec:
        return {
            "stagnation_generations": int(spec["stagnation_generations"])
        }, f"stagG{int(spec['stagnation_generations'])}"
    raise ValueError(f"unknown stop rule {spec!r}")


def method_params(cfg: ConfigV2, name: str) -> tuple[str, dict[str, Any], str | None]:
    """(kind, parameters, initialization) of a configured method; tuned methods read the frozen file."""
    spec = cfg.method(name)
    kind = spec["kind"]
    params = dict(spec.get("params", {}))
    if "tuned" in spec:
        tuned = cfg.tuned()
        if spec["tuned"] not in tuned:
            raise RuntimeError(f"no frozen tuning result for {spec['tuned']} in {cfg.tuned_path}; run tpga-exp tune")
        params = dict(tuned[spec["tuned"]])
    if kind == "ga":
        params = {**GA_DEFAULTS, **params}
    return kind, params, spec.get("initialization")


def _base(cfg: ConfigV2, phase: str, inst: InstanceV2) -> dict[str, Any]:
    return {
        "phase": phase,
        "set": inst.set,
        "instance": inst.id,
        "size": inst.size,
        "m": inst.m,
        "n": inst.n,
        "path": str(inst.path),
        "z_rand": inst.z_rand,
        "tolerance": cfg.tolerance,
        "decoder_tol": cfg.decoder_tol,
        "seed": None,
    }


def reference_tasks(
    cfg: ConfigV2, phase: str, items: list[InstanceV2], methods: list[str], repeats: int | None = None
) -> list[dict[str, Any]]:
    tasks = []
    for inst in items:
        for name in methods:
            spec = cfg.method(name)
            t = {
                **_base(cfg, phase, inst),
                "method": name,
                "kind": spec["kind"],
                "config": spec.get("solver", "-"),
                "solver": spec.get("solver"),
                "repeats": repeats or int(cfg.raw.get("lp_repeats", 5)),
            }
            tasks.append(t)
    return tasks


def stochastic_tasks(
    cfg: ConfigV2,
    phase: str,
    items: list[InstanceV2],
    methods: list[str],
    stop: Any,
    seeds: list[int],
    curve: bool = False,
    params_override: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    tasks = []
    for inst in items:
        budget = cfg.budget(inst.m, inst.n)
        stop_fields, stop_label = stop_spec(stop, budget)
        for name in methods:
            if params_override and name in params_override:
                kind, params, init = "ga", {**GA_DEFAULTS, **params_override[name]}, params_override[name]["init"]
            else:
                kind, params, init = method_params(cfg, name)
            if kind == "rs":
                cid = f"B{budget}"
            elif kind == "ga":
                cid = ga_config_id(params, str(init), stop_label)
            else:
                cid = sa_config_id(params, str(init), stop_label)
            for seed in seeds:
                tasks.append(
                    {
                        **_base(cfg, phase, inst),
                        "method": name,
                        "kind": kind,
                        "config": cid,
                        "params": params,
                        "initialization": init,
                        "stop": stop_fields,
                        "budget": budget,
                        "seed": seed,
                        "curve_points": int(cfg.raw.get("convergence_points", 100)) if curve else 0,
                    }
                )
    return tasks


def factorial_tasks(cfg: ConfigV2, items: list[InstanceV2]) -> list[dict[str, Any]]:
    spec = cfg.phase("factorial")
    chosen = select(items, spec["sets"])
    overrides: dict[str, dict[str, Any]] = {}
    for pop, (mode, levels), init in product(spec["population"], spec["mutation"].items(), spec["initialization"]):
        for level in levels:
            p = {**spec["fixed"], "population": pop, "mutation_mode": mode, "init": init}
            if mode == "swap_fixed":
                p["mutation_rate"] = level
            else:
                p["mutation_strength"] = level
            name = f"GA-{'rand' if init == 'random' else 'cost'}"
            overrides[f"{name}|{pop}|{mode}|{level}"] = p
    tasks = []
    for label, p in overrides.items():
        method = label.split("|")[0]
        for t in stochastic_tasks(cfg, "factorial", chosen, [label], "budget", cfg.seeds(), params_override={label: p}):
            t["method"] = method
            tasks.append(t)
    return tasks


def phase_tasks(cfg: ConfigV2, phase: str, items: list[InstanceV2]) -> list[dict[str, Any]]:
    """Tasks of a phase (reference tasks need no optimum; the others get ``z_star`` filled in later)."""
    spec = cfg.phase(phase)
    if phase == "reference":
        return reference_tasks(cfg, phase, select(items, spec["sets"]), list(cfg.raw["reference_methods"]))
    if phase == "factorial":
        return factorial_tasks(cfg, items)
    if phase == "representation":
        from tpga.experiments.v2.representation_phase import tasks as representation_tasks

        return representation_tasks(cfg, items)
    if phase == "timing":
        chosen = select(items, spec["sets"], int(spec["instances"]))
        lp_only = set(spec.get("lp_methods_only_on", []))
        lp_methods = [m for m in spec["methods"] if cfg.method(m)["kind"] == "lp"]
        other = [m for m in spec["methods"] if m not in lp_methods]
        tasks = reference_tasks(cfg, phase, chosen, lp_methods)
        tasks += stochastic_tasks(
            cfg, phase, [i for i in chosen if i.set not in lp_only], other, "budget", cfg.seeds(int(spec["runs"]))
        )
        return tasks
    # runs_by_size: {"200x200": 10} runs seeds r = 0..9 at that size (the first ones of the common seeds)
    by_size = {str(k): int(v) for k, v in (spec.get("runs_by_size") or {}).items()}
    default = int(spec.get("runs", cfg.runs))  # a phase may set its own number of runs (applied: 10)
    chosen = select(items, spec["sets"])
    tasks = []
    for runs in sorted({by_size.get(i.size, default) for i in chosen}):
        group = [i for i in chosen if by_size.get(i.size, default) == runs]
        tasks += stochastic_tasks(
            cfg, phase, group, list(spec["methods"]), spec.get("stop"), cfg.seeds(runs), curve=(phase == "main")
        )
    return tasks
