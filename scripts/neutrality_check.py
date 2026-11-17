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
"""

from __future__ import annotations

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


if __name__ == "__main__":
    main()
