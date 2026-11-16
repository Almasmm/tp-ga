"""Empirical check that the decoder can reach an optimal basic solution returned by HiGHS.

For each random balanced integer instance the dual simplex gives an optimal vertex; the
permutation built from its support forest (:func:`tpga.basis.permutation_from_basis`) is decoded
and the decoded plan is compared with the vertex. This is an empirical check on the generated
instances, not a proof for every instance.
"""

from __future__ import annotations

import json
from typing import Any

import numpy as np

from tpga.basis import is_basic, permutation_from_basis, support
from tpga.decoder import decode_permutation
from tpga.exact import solve_lp_detailed
from tpga.experiments.config import Config
from tpga.model import TransportProblem


def random_instance(rng: np.random.Generator, spec: dict[str, Any]) -> TransportProblem:
    m = int(rng.integers(spec["min_size"], spec["max_size"] + 1))
    n = int(rng.integers(spec["min_size"], spec["max_size"] + 1))
    # small integer supplies make degenerate vertices frequent, which is the interesting case
    a = rng.integers(1, int(spec["max_supply"]) + 1, size=m)
    b = 1 + rng.multinomial(int(a.sum()) - n, np.full(n, 1 / n)) if a.sum() >= n else None
    if b is None:
        a[0] += n - int(a.sum())
        b = np.ones(n, dtype=int)
    c = rng.integers(1, int(spec["max_cost"]) + 1, size=(m, n))
    return TransportProblem(a, b, c)


def check(problem: TransportProblem, tol: float) -> dict[str, Any]:
    lp = solve_lp_detailed(problem, method="highs-ds")
    x = np.round(lp.x)
    integral = float(np.abs(lp.x - x).max()) <= 1e-6
    m, n = problem.shape
    basic = is_basic(x)
    perm = permutation_from_basis(problem, x) if basic else None
    out: dict[str, Any] = {
        "m": m,
        "n": n,
        "z_star": lp.cost,
        "support": len(support(x)),
        "degenerate": len(support(x)) < m + n - 1,
        "integral_vertex": integral,
        "basic": basic,
        "reproduced": False,
    }
    if perm is not None:
        y = decode_permutation(problem, perm)
        z = problem.total_cost(y)
        out["decoded_cost"] = z
        out["reproduced"] = bool(np.array_equal(y, x)) and abs(z - lp.cost) <= tol * max(1.0, abs(lp.cost))
    return out


def run(cfg: Config, spec: dict[str, Any]) -> dict[str, Any]:
    rng = np.random.default_rng(int(spec.get("seed", cfg.base_seed)))
    cases = [check(random_instance(rng, spec), cfg.tolerance) for _ in range(int(spec["instances"]))]
    failures = [c for c in cases if not c["reproduced"]]
    sizes = [c["m"] * c["n"] for c in cases]
    summary = {
        "description": (
            "Random balanced integer instances; HiGHS dual simplex (scipy linprog method='highs-ds') gives an "
            "optimal vertex; a permutation is built by removing leaves of the vertex's support forest and is "
            "decoded by the greedy decoder. 'reproduced' means the decoded plan equals the vertex exactly and "
            "its cost equals the LP optimum within the tolerance. Empirical check, not a proof."
        ),
        "generator": {k: spec[k] for k in ("min_size", "max_size", "max_supply", "max_cost")},
        "seed": int(spec.get("seed", cfg.base_seed)),
        "tolerance": cfg.tolerance,
        "instances": len(cases),
        "reproduced": len(cases) - len(failures),
        "not_reproduced": len(failures),
        "integral_vertices": sum(c["integral_vertex"] for c in cases),
        "basic_vertices": sum(c["basic"] for c in cases),
        "degenerate_vertices": sum(c["degenerate"] for c in cases),
        "degenerate_reproduced": sum(c["degenerate"] and c["reproduced"] for c in cases),
        "arcs_min": min(sizes),
        "arcs_max": max(sizes),
        "failures": failures,
        "cases": cases,
    }
    path = cfg.output / "reachability.json"
    path.write_text(json.dumps(summary, indent=1) + "\n", encoding="utf-8")
    return summary
