"""Estimated wall time of the plan after each reduction of amendment 7, in the fixed order a-f.

No runs: uses the measurements of the last pilot (``paper_artifacts_v2/pilot/estimate.json``). Prints the
estimate of the configuration as it is and after each step applied on top of the previous ones, and marks
the first step at which the total is within the target. The configuration file is not changed.

    python scripts/plan_variants.py --config experiments/paper-v2.yaml --target 14
"""

from __future__ import annotations

import argparse
import copy
from typing import Any

from tpga.experiments.v2 import pilot
from tpga.experiments.v2.config import ConfigV2


def steps(raw: dict[str, Any]) -> list[tuple[str, Any]]:
    ph = raw["phases"]

    def a() -> None:
        ph["timing"]["stochastic_max_arcs"] = 10000

    def b() -> None:
        ph["factorial"]["runs"] = 10

    def c() -> None:
        ph["stagnation"]["runs"] = 10

    def d() -> None:
        ph["main"]["skip_methods_by_size"] = {"200x200": ["GA-rand-base", "GA-cost-base"]}

    def e() -> None:
        ph["main"]["runs_by_size"] = {"50x50": 20, "100x100": 20, "200x200": 10}

    def f() -> None:
        ph["applied"]["runs_by_set"] = {"astana": 5}

    return [
        ("a) timing: GA and SA up to 100x100 only", a),
        ("b) factorial: 10 seeds", b),
        ("c) stagnation: 10 seeds", c),
        ("d) main 200x200: without the base GA configurations", d),
        ("e) main, 50x50 and larger: 20 seeds (200x200 keeps 10)", e),
        ("f) applied, Astana: 5 runs", f),
    ]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True)
    ap.add_argument("--target", type=float, default=14.0)
    args = ap.parse_args()
    cfg = ConfigV2.load(args.config)
    raw = copy.deepcopy(cfg.raw)

    def show(label: str) -> float:
        est = pilot.reestimate(ConfigV2(copy.deepcopy(raw), cfg.path))
        parts = "  ".join(f"{k} {v['wall_h']:.2f}" for k, v in est["phases"].items())
        print(f"{est['total_wall_h']:7.2f} h  {label}\n           {parts}")
        return float(est["total_wall_h"])

    total = show("configuration as it is")
    for label, apply in steps(raw):
        if total <= args.target:
            print(f"within {args.target:g} h: no further reduction")
            break
        apply()
        total = show(label)
    else:
        print(f"within {args.target:g} h" if total <= args.target else f"STILL ABOVE {args.target:g} h after step f")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
