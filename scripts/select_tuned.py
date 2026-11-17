"""Final tuned parameters by amendment 5 (PREREGISTRATION.md, section 9).

For every tuned method: the completed trial with the lowest mean training gap among round 1
(``paper_artifacts_v2/tuning/round1/<method>.jsonl``) and round 2 (``paper_artifacts_v2/tuning/<method>.jsonl``);
on an exact tie the round-2 trial. No other rule. Rewrites ``experiments/tuned-v2.yaml`` (written by the
round-2 ``tpga-exp tune``) with the chosen parameters and, under ``selection``, the round and trial of every
method and the best training gap of each round.

    python scripts/select_tuned.py --config experiments/paper-v2.yaml
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
from typing import Any

import yaml

from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.tune import TUNED, near_bounds

ROUNDS = {1: "round1", 2: ""}  # sub-directory of <output>/tuning


def trials(path: Path) -> list[dict[str, Any]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return [r for r in rows if r.get("mean_gap") is not None]


def select(tuning: Path, expected: int) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for name in TUNED:
        best: dict[int, dict[str, Any]] = {}
        for rnd, sub in ROUNDS.items():
            rows = trials(tuning / sub / f"{name}.jsonl")
            if len(rows) != expected:
                raise SystemExit(f"{name}, round {rnd}: {len(rows)} completed trials, expected {expected}")
            best[rnd] = min(rows, key=lambda r: (r["mean_gap"], r["trial"]))
        rnd = 2 if best[2]["mean_gap"] <= best[1]["mean_gap"] else 1  # exact tie: round 2
        out[name] = {
            "round": rnd,
            "trial": int(best[rnd]["trial"]),
            "mean_gap": float(best[rnd]["mean_gap"]),
            "runs": int(best[rnd]["runs"]),
            "params": best[rnd]["params"],
            "best_mean_gap_by_round": {f"round{r}": float(b["mean_gap"]) for r, b in best.items()},
            "best_trial_by_round": {f"round{r}": int(b["trial"]) for r, b in best.items()},
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = ConfigV2.load(args.config)
    spec = cfg.raw["tuning"]
    chosen = select(cfg.output / "tuning", int(spec["trials"]))
    frozen = yaml.safe_load(cfg.tuned_path.read_text(encoding="utf-8"))
    round1 = yaml.safe_load((cfg.tuned_path.parent / "tuned-v2-round1.yaml").read_text(encoding="utf-8"))
    frozen["frozen"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    frozen["rule"] = (
        "amendment 5: per method, the trial with the lowest mean training gap among all completed trials of "
        "round 1 and round 2; exact tie: round 2"
    )
    frozen["parameters"] = {k: v["params"] for k, v in chosen.items()}
    frozen["best_objective"] = {k: v["mean_gap"] for k, v in chosen.items()}
    frozen["selection"] = {k: {f: v[f] for f in v if f != "params"} for k, v in chosen.items()}
    frozen["space_by_round"] = {"round1": round1["space"], "round2": spec["space"]}
    # near the bounds of the range the trial was sampled from, and of the final (round-2) range
    frozen["near_bounds"] = {
        k: {
            "own_round_range": near_bounds(TUNED[k][0], v["params"], frozen["space_by_round"][f"round{v['round']}"]),
            "round2_range": near_bounds(TUNED[k][0], v["params"], spec["space"]),
        }
        for k, v in chosen.items()
    }
    text = yaml.safe_dump(frozen, sort_keys=False, allow_unicode=True)
    cfg.tuned_path.write_text(text, encoding="utf-8", newline="\n")
    for k, v in chosen.items():
        by = v["best_mean_gap_by_round"]
        print(
            f"{k}: round {v['round']}, trial {v['trial']}, mean gap {v['mean_gap']:.3f} % "
            f"(round 1 best {by['round1']:.3f}, round 2 best {by['round2']:.3f})  {v['params']}"
        )
        for where, items in frozen["near_bounds"][k].items():
            for b in items:
                print(f"    near the {b['side']} bound {b['bound']:g} of {b['parameter']} ({where}): {b['value']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
