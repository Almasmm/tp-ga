"""Neutrality of the swap move under the greedy decoder (Proposition 3 of the article).

For every instance of the v0.3.0 test set (uniform and structured) the script draws random permutations,
applies one random swap of two distinct positions u < v to each, and classifies the result:

* neutral        - the decoded plan is unchanged;
* moved_positive - at least one of the two swapped arcs carries flow in the plan of the parent;
* idle_forward   - both swapped arcs carry no flow and both endpoints of the arc at position v are still
                   open before step u (the second case of Proposition 3).

Proposition 3 states that every non-neutral swap is of the second or third kind; the script counts the
exceptions (expected 0). It also reports the bound 1 - C(N - r, 2) / C(N, 2) with r the number of positive
arcs of the parent plan.

Run from the repository root:

    python scripts/neutrality_check.py

Output: paper_artifacts_supplement/neutrality/neutrality_instances.csv and neutrality_summary.csv.
The decoder is the plain reference kernel of the library (tpga._kernels._decode_plan_py) when the library
can be imported; otherwise a line-by-line copy of it below is used (same arithmetic, eps = 0).

Second measurement (amendment 8.1 of docs/v0.4/PREREGISTRATION.md), on the same instances and sample sizes:

    python scripts/neutrality_check.py --operators paper_artifacts_v3/kselect/selected.json

For random parents it applies a whole mutation, as the GA does, and counts the offspring whose decoded plan
equals the plan of the parent: `swap_scaled` with the tuned strength 0.0837 (max(1, round(0.0837 (m + n)))
swaps) and the cycle mutation with the k chosen for GA-rand-cycle and GA-cost-cycle (tpga.cycle). For the
cycle mutation it also counts the pivots with theta = 0. Output:
paper_artifacts_v3/neutrality/operators_instances.csv and operators_summary.csv. This part needs the library.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261118
SAMPLES = {5: 2000, 10: 2000, 20: 2000, 30: 1000, 50: 500, 100: 200}


def decode_with_steps(perm: list[int], supply: list[float], demand: list[float], n: int) -> tuple[dict, list, list]:
    """Plan of the greedy decoder (dict arc -> amount) and the step at which every source and destination is
    exhausted (len(perm) if never). Same rule as tpga._kernels._decode_plan_py with eps = 0."""
    a = list(supply)
    b = list(demand)
    m = len(a)
    plan: dict[int, float] = {}
    ex_a = [len(perm)] * m
    ex_b = [len(perm)] * n
    active = sum(1 for x in a if x > 0)
    for t, k in enumerate(perm):
        if active == 0:
            break
        i, j = divmod(k, n)
        q = min(a[i], b[j])
        if q > 0:
            plan[k] = q
            a[i] -= q
            b[j] -= q
            if a[i] <= 0:
                active -= 1
                ex_a[i] = t
            if b[j] <= 0:
                ex_b[j] = t
    return plan, ex_a, ex_b


def plan_only(perm: list[int], supply: list[float], demand: list[float], n: int) -> dict:
    return decode_with_steps(perm, supply, demand, n)[0]


def check_against_library(instances: list[dict], rng: np.random.Generator) -> str:
    """Compare the copy above with the library's reference kernel on a few permutations."""
    try:
        sys.path.insert(0, str(ROOT / "src"))
        from tpga._kernels import _decode_plan_py  # type: ignore[attr-defined]
    except Exception as exc:  # noqa: BLE001 - numba missing: the copy is used
        return f"library kernel not importable ({type(exc).__name__}); copy used"
    for inst in instances[:20]:
        m, n = len(inst["supply"]), len(inst["demand"])
        perm = rng.permutation(m * n)
        args = (perm, np.array(inst["supply"], float), np.array(inst["demand"], float), n)
        try:
            ref = _decode_plan_py(*args, 0.0)  # v0.4: the tolerance eps is a parameter
        except TypeError:
            ref = _decode_plan_py(*args)  # v0.3.0: exact comparison with zero, the same as eps = 0
        own = plan_only(perm.tolist(), inst["supply"], inst["demand"], n)
        dense = np.zeros(m * n)
        for k, q in own.items():
            dense[k] = q
        if not np.array_equal(ref, dense):
            raise SystemExit("decoder copy differs from tpga._kernels._decode_plan_py")
    return "copy identical to tpga._kernels._decode_plan_py on 20 instances"


def main() -> None:
    root = ROOT / "paper_artifacts" / "instances"
    files = sorted((root / "uniform").glob("*.json")) + sorted((root / "structured").glob("*.json"))
    instances = []
    for f in files:
        d = json.loads(f.read_text(encoding="utf-8"))
        d["id"] = f.stem
        d["set"] = f.parent.name
        instances.append(d)
    rng = np.random.default_rng(SEED)
    # its own generator: the results below are the same whether or not the library can be imported
    note = check_against_library(instances, np.random.default_rng(SEED + 1))
    out_dir = ROOT / "paper_artifacts_supplement" / "neutrality"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for inst in instances:
        m, n = len(inst["supply"]), len(inst["demand"])
        big_n = m * n
        samples = SAMPLES.get(m, 500)
        neutral = moved_pos = idle_fwd = exceptions = 0
        r_values = []
        for _ in range(samples):
            perm = rng.permutation(big_n).tolist()
            plan, ex_a, ex_b = decode_with_steps(perm, inst["supply"], inst["demand"], n)
            r_values.append(len(plan))
            u, v = sorted(rng.choice(big_n, size=2, replace=False).tolist())
            child = list(perm)
            child[u], child[v] = child[v], child[u]
            same = plan_only(child, inst["supply"], inst["demand"], n) == plan
            pos = perm[u] in plan or perm[v] in plan
            iv, jv = divmod(perm[v], n)
            fwd = (not pos) and ex_a[iv] >= u and ex_b[jv] >= u
            neutral += same
            moved_pos += pos
            idle_fwd += fwd
            if not same and not (pos or fwd):
                exceptions += 1
        r_mean = statistics.mean(r_values)
        r = round(r_mean)
        bound = 1 - math.comb(big_n - r, 2) / math.comb(big_n, 2)
        rows.append(
            {
                "set": inst["set"],
                "instance": inst["id"],
                "m": m,
                "n": n,
                "samples": samples,
                "positive_arcs_mean": round(r_mean, 3),
                "neutral_share": neutral / samples,
                "moved_positive_share": moved_pos / samples,
                "idle_forward_share": idle_fwd / samples,
                "exceptions": exceptions,
                "bound_moved_positive": bound,
            }
        )
    with (out_dir / "neutrality_instances.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    summary = []
    for key in sorted({(r["set"], r["m"], r["n"]) for r in rows}, key=lambda x: (x[0], x[1])):
        grp = [r for r in rows if (r["set"], r["m"], r["n"]) == key]
        summary.append(
            {
                "set": key[0],
                "size": f"{key[1]}x{key[2]}",
                "instances": len(grp),
                "neutral_share_median": statistics.median(r["neutral_share"] for r in grp),
                "moved_positive_share_median": statistics.median(r["moved_positive_share"] for r in grp),
                "idle_forward_share_median": statistics.median(r["idle_forward_share"] for r in grp),
                "bound_moved_positive_median": statistics.median(r["bound_moved_positive"] for r in grp),
                "exceptions_total": sum(r["exceptions"] for r in grp),
            }
        )
    with (out_dir / "neutrality_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)
    print(note)
    for s in summary:
        print(
            f"{s['set']:10s} {s['size']:8s} neutral {s['neutral_share_median']:.3f}  "
            f"moved positive {s['moved_positive_share_median']:.3f} (bound {s['bound_moved_positive_median']:.3f})  "
            f"idle forward {s['idle_forward_share_median']:.3f}  exceptions {s['exceptions_total']}"
        )


SWAP_SCALED_STRENGTH = 0.08371937516446804  # GA-rand of experiments/tuned-v2.yaml


def load_instances() -> list[dict]:
    root = ROOT / "paper_artifacts" / "instances"
    out = []
    for f in sorted((root / "uniform").glob("*.json")) + sorted((root / "structured").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        d["id"] = f.stem
        d["set"] = f.parent.name
        out.append(d)
    return out


def operators(selected_path: Path) -> None:
    """Share of offspring with the plan of the parent: swap_scaled against the cycle mutation."""
    sys.path.insert(0, str(ROOT / "src"))
    from tpga._kernels import Kernels
    from tpga.cycle import GAXConfig, cycle_mutation
    from tpga.model import TransportProblem

    chosen = json.loads(selected_path.read_text(encoding="utf-8"))["selected"]
    kern = Kernels("numba")
    base = dict(population=2, crossover_rate=1.0, tournament=1, elite=0, max_evaluations=2)
    ops: dict[str, GAXConfig] = {
        f"swap_scaled:{SWAP_SCALED_STRENGTH:.4f}": GAXConfig(
            mutation_mode="swap_scaled", mutation_strength=SWAP_SCALED_STRENGTH, **base
        )
    }
    for sel in chosen.values():
        ops.setdefault(
            f"cycle k={sel['k']}",
            GAXConfig(mutation_mode=sel["mode"], mutation_strength=float(sel["strength"]), **base),
        )
    used_by = {name: [v for v, sel in chosen.items() if f"cycle k={sel['k']}" == name] for name in ops}
    rng = np.random.default_rng(SEED + 2)
    out_dir = ROOT / "paper_artifacts_v3" / "neutrality"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for inst in load_instances():
        p = TransportProblem(inst["supply"], inst["demand"], inst["cost"])
        m, n = p.shape
        big_n = m * n
        samples = SAMPLES.get(m, 500)
        supply, demand = p.supply.copy(), p.demand.copy()
        for name, cfg in ops.items():
            moves = cfg.moves(m, n)
            unchanged = pivots = zero = unchanged_all_zero = 0
            for _ in range(samples):
                parent = rng.permutation(big_n)
                plan = kern.decode_plan(parent, supply, demand, n)
                if name.startswith("swap"):
                    child = parent.copy()
                    for _s in range(moves):
                        u, v = rng.choice(big_n, size=2, replace=False)
                        child[u], child[v] = child[v], child[u]
                    same = bool(np.array_equal(kern.decode_plan(child, supply, demand, n), plan))
                else:
                    move = cycle_mutation(p, parent, moves, rng=rng)
                    same = bool(np.array_equal(kern.decode_plan(move.permutation, supply, demand, n), plan))
                    pivots += move.pivots
                    zero += move.zero_pivots
                    unchanged_all_zero += same and move.zero_pivots == move.pivots
                unchanged += same
            rows.append(
                {
                    "set": inst["set"],
                    "instance": inst["id"],
                    "m": m,
                    "n": n,
                    "operator": name,
                    "used_by": "; ".join(used_by[name]) or "GA-rand-tuned",
                    "moves_per_offspring": moves,
                    "samples": samples,
                    "unchanged": unchanged,
                    "unchanged_share": unchanged / samples,
                    "pivots": pivots,
                    "pivots_theta_zero": zero,
                    "unchanged_with_all_theta_zero": unchanged_all_zero,
                }
            )
    with (out_dir / "operators_instances.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    summary = []
    keys = sorted({(r["set"], r["m"], r["n"]) for r in rows}, key=lambda x: (x[0] != "uniform", x[1]))
    for key in keys:
        for name in ops:
            grp = [r for r in rows if (r["set"], r["m"], r["n"]) == key and r["operator"] == name]
            pivots = sum(r["pivots"] for r in grp)
            summary.append(
                {
                    "set": key[0],
                    "size": f"{key[1]}x{key[2]}",
                    "operator": name,
                    "used_by": grp[0]["used_by"],
                    "moves_per_offspring": grp[0]["moves_per_offspring"],
                    "instances": len(grp),
                    "samples": sum(r["samples"] for r in grp),
                    "unchanged": sum(r["unchanged"] for r in grp),
                    "unchanged_share_median": statistics.median(r["unchanged_share"] for r in grp),
                    "unchanged_share_min": min(r["unchanged_share"] for r in grp),
                    "unchanged_share_max": max(r["unchanged_share"] for r in grp),
                    "pivots": pivots,
                    "pivots_theta_zero": sum(r["pivots_theta_zero"] for r in grp),
                    "share_pivots_theta_zero": sum(r["pivots_theta_zero"] for r in grp) / pivots if pivots else "",
                    "unchanged_with_all_theta_zero": sum(r["unchanged_with_all_theta_zero"] for r in grp),
                }
            )
    with (out_dir / "operators_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(summary[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(summary)
    for s in summary:
        print(
            f"{s['set']:10s} {s['size']:8s} {s['operator']:28s} unchanged {s['unchanged_share_median']:.4f}  "
            f"pivots {s['pivots']}  theta = 0: {s['pivots_theta_zero']}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--operators",
        metavar="SELECTED_JSON",
        help="second measurement: unchanged plans under swap_scaled and the cycle mutation with the chosen k",
    )
    arguments = parser.parse_args()
    if arguments.operators:
        operators(Path(arguments.operators))
    else:
        main()
