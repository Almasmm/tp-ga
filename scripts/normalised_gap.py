"""Normalised gap for the v0.3.0 results of the article.

gap_norm = (Z - Z*) / (Z_rand - Z*), where Z_rand is the mean cost of 1000 decoded uniformly random
permutations of the instance (the cost of an average basic plan reachable by the decoder). 0 is the
optimum, 1 the expected cost of a random decoded plan. The same definition is used in v0.4 (L7).

Run from the repository root:

    python scripts/normalised_gap.py

Input: paper_artifacts/instances/{uniform,structured}/*.json and paper_artifacts/raw/runs.csv (phase main).
Output: paper_artifacts_supplement/normalised_gap/zrand.csv, runs_gap_norm_summary.csv.
"""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SEED = 20261118
SAMPLES = 1000


def decode_cost(perm: list[int], supply: list[float], demand: list[float], cost: list[float], n: int) -> float:
    """Same rule as tpga._kernels._decode_cost_py with eps = 0."""
    a = list(supply)
    b = list(demand)
    active = sum(1 for x in a if x > 0)
    total = 0.0
    for k in perm:
        if active == 0:
            break
        i, j = divmod(k, n)
        q = min(a[i], b[j])
        if q > 0:
            total += cost[k] * q
            a[i] -= q
            b[j] -= q
            if a[i] <= 0:
                active -= 1
    return total


def main() -> None:
    inst_root = ROOT / "paper_artifacts" / "instances"
    out_dir = ROOT / "paper_artifacts_supplement" / "normalised_gap"
    out_dir.mkdir(parents=True, exist_ok=True)
    zrand_path = out_dir / "zrand.csv"
    zrand: dict[str, float] = {}
    if zrand_path.exists():  # resume
        for row in csv.DictReader(zrand_path.open(encoding="utf-8")):
            zrand[row["instance"]] = float(row["z_rand"])
    files = sorted((inst_root / "uniform").glob("*.json")) + sorted((inst_root / "structured").glob("*.json"))
    for f in files:
        if f.stem in zrand:
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        n = len(d["demand"])
        cost = [float(c) for row in d["cost"] for c in row]
        rng = np.random.default_rng([SEED, int.from_bytes(f.stem.encode(), "little") % (2**32)])
        vals = [
            decode_cost(rng.permutation(len(cost)).tolist(), d["supply"], d["demand"], cost, n) for _ in range(SAMPLES)
        ]
        zrand[f.stem] = statistics.fmean(vals)
        new = not zrand_path.exists()
        with zrand_path.open("a", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            if new:
                w.writerow(["instance", "z_rand", "samples", "seed"])
            w.writerow([f.stem, repr(zrand[f.stem]), SAMPLES, SEED])
        print(f.stem, round(zrand[f.stem], 1), flush=True)

    groups: dict[tuple[str, str, str], list[float]] = {}
    per_instance: dict[tuple[str, str, str, str], list[float]] = {}
    with (ROOT / "paper_artifacts" / "raw" / "runs.csv").open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["phase"] != "main" or r["method"] == "LP" or r["instance"] not in zrand:
                continue
            z, zs = float(r["cost"]), float(r["z_star"])
            g = (z - zs) / (zrand[r["instance"]] - zs)
            groups.setdefault((r["suite"], r["size"], r["method"]), []).append(g)
            per_instance.setdefault((r["suite"], r["size"], r["method"], r["instance"]), []).append(g)
    order = {"5x5": 0, "10x10": 1, "20x20": 2, "30x30": 3, "50x50": 4, "100x100": 5}
    rows = []
    for (suite, size, method), vals in sorted(groups.items(), key=lambda kv: (kv[0][0], order[kv[0][1]], kv[0][2])):
        inst_medians = [
            statistics.median(v) for (s, z, m, _), v in per_instance.items() if (s, z, m) == (suite, size, method)
        ]
        rows.append(
            {
                "suite": suite,
                "size": size,
                "method": method,
                "runs": len(vals),
                "gap_norm_median": statistics.median(vals),
                "gap_norm_max": max(vals),
                "gap_norm_instance_median_median": statistics.median(inst_medians),
            }
        )
    with (out_dir / "runs_gap_norm_summary.csv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(
            f"{r['suite']:10s} {r['size']:8s} {r['method']:8s} "
            f"median {r['gap_norm_median']:.4f}  max {r['gap_norm_max']:.4f}"
        )


if __name__ == "__main__":
    main()
