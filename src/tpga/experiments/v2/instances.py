"""Instance sets of v0.4 with SHA-256 manifest and the random-plan reference cost Z_rand (L7)."""

from __future__ import annotations

import hashlib
import json
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from tpga._kernels import Kernels
from tpga.decoder import decoder_eps
from tpga.experiments.instances import structured_instance, uniform_instance
from tpga.experiments.v2.config import ConfigV2
from tpga.model import TransportProblem

SET_ORDER = ("uniform", "structured", "skewed", "ties", "lp_scaling")
#: applied datasets (``datasets/<name>``) and the set name their instances get (amendment 4)
APPLIED = {"kazakh-wheat": "wheat", "astana-potato": "astana"}
TRAIN_OFFSET = 5_000_000


@dataclass(frozen=True)
class InstanceV2:
    id: str
    set: str
    m: int
    n: int
    path: Path
    seed: int
    z_rand: float | None
    split: str = "test"

    @property
    def size(self) -> str:
        return f"{self.m}x{self.n}"


def _balanced_demands(rng: np.random.Generator, total: int, n: int, weights: np.ndarray | None = None) -> np.ndarray:
    w = np.full(n, 1 / n) if weights is None else weights / weights.sum()
    return 1 + rng.multinomial(total - n, w)


def skewed_instance(m: int, n: int, seed: int, spec: dict[str, Any]) -> dict[str, Any]:
    """Strongly unequal volumes: supplies ``round(median * LogNormal(0, sigma))`` (at least 1) and demands
    split from the same total with log-normal weights; costs ``U[c_lo, c_hi]``."""
    rng = np.random.default_rng(seed)
    sigma, med = float(spec["lognormal_sigma"]), float(spec["supply_median"])
    a = np.maximum(1, np.rint(med * rng.lognormal(0.0, sigma, size=m))).astype(int)
    total = int(a.sum())
    if total < n:
        a[0] += n - total
        total = n
    b = _balanced_demands(rng, total, n, rng.lognormal(0.0, sigma, size=n))
    lo, hi = spec["cost"]
    c = rng.integers(int(lo), int(hi) + 1, size=(m, n))
    return {"supply": a.tolist(), "demand": b.tolist(), "cost": c.tolist()}


def ties_instance(m: int, n: int, seed: int, spec: dict[str, Any]) -> dict[str, Any]:
    """Many equal costs and frequent degeneracy: costs from {lo..hi}, small integer supplies."""
    rng = np.random.default_rng(seed)
    s_lo, s_hi = spec["supply"]
    a = rng.integers(int(s_lo), int(s_hi) + 1, size=m)
    total = int(a.sum())
    if total < n:
        a[0] += n - total
        total = n
    b = _balanced_demands(rng, total, n)
    lo, hi = spec["cost"]
    c = rng.integers(int(lo), int(hi) + 1, size=(m, n))
    return {"supply": a.tolist(), "demand": b.tolist(), "cost": c.tolist()}


def _uniform(m: int, n: int, seed: int, spec: dict[str, Any]) -> dict[str, Any]:
    lo, hi = spec["cost"]
    s_lo, s_hi = spec["supply"]
    return uniform_instance(m, n, seed, {"cost_low": lo, "cost_high": hi, "supply_low": s_lo, "supply_high": s_hi})


def _structured(m: int, n: int, seed: int, spec: dict[str, Any]) -> dict[str, Any]:
    s_lo, s_hi = spec["supply"]
    return structured_instance(
        m, n, seed, {"area": spec["area"], "noise": spec["noise"], "supply_low": s_lo, "supply_high": s_hi}
    )


GENERATORS = {
    "uniform": _uniform,
    "structured": _structured,
    "skewed": skewed_instance,
    "ties": ties_instance,
    "lp_scaling": _uniform,
}


def instance_seed(base: int, set_name: str, size_index: int, k: int, split: str = "test") -> int:
    return (
        base + (TRAIN_OFFSET if split == "train" else 0) + 100_000 * SET_ORDER.index(set_name) + 1000 * size_index + k
    )


def z_rand(problem: TransportProblem, samples: int, seed: int, tol: float) -> float:
    """Mean cost of ``samples`` decoded uniformly random permutations (random basic plans)."""
    p = problem.balanced()
    kern = Kernels("numba")
    rng = np.random.default_rng(seed)
    length = p.cost.size
    supply, demand = p.supply.astype(np.float64), p.demand.astype(np.float64)
    cost = np.ascontiguousarray(p.cost.ravel(), dtype=np.float64)
    out = np.empty(samples)
    for start in range(0, samples, 256):
        k = min(256, samples - start)
        part = np.empty(k)
        kern.random_batch_cost(
            rng.random((k, max(0, length - 1))), supply, demand, cost, p.shape[1], part, decoder_eps(p, tol)
        )
        out[start : start + k] = part
    return float(out.mean())


def zrand_seed(instance_id: str, base: int) -> int:
    return base + zlib.crc32(instance_id.encode("utf-8"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(
    cfg: ConfigV2, split: str = "test", sets: list[str] | None = None, per_size: int | None = None
) -> list[InstanceV2]:
    """Generate (or verify) instances and update ``instances/manifest.json`` (``split`` test or train)."""
    root = cfg.output / ("instances" if split == "test" else "instances_train")
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {"instances": {}}
    entries: dict[str, Any] = manifest["instances"]
    base = int(cfg.raw["instance_seed_base"])
    samples = int(cfg.raw.get("zrand_samples", 1000))
    out: list[InstanceV2] = []
    spec_all = cfg.raw["instances"]
    for set_name in sets or [s for s in SET_ORDER if s in spec_all]:
        spec = spec_all[set_name]
        for size_index, (m, n) in enumerate(spec["sizes"]):
            for k in range(int(per_size or spec["per_size"])):
                seed = instance_seed(base, set_name, size_index, k, split)
                prefix = {"uniform": "u", "structured": "s", "skewed": "k", "ties": "t", "lp_scaling": "l"}[set_name]
                iid = f"{prefix}{m}x{n}-{k:02d}" + ("-train" if split == "train" else "")
                path = root / set_name / f"{iid}.json"
                data = GENERATORS[set_name](int(m), int(n), seed, spec)
                text = json.dumps(data, separators=(",", ":")) + "\n"
                if not path.exists() or path.read_bytes() != text.encode("utf-8"):
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(text, encoding="utf-8", newline="\n")
                digest = _sha(path)
                entry = entries.get(iid)
                if entry is None or entry.get("sha256") != digest or "z_rand" not in entry:
                    zr = None
                    if set_name != "lp_scaling":
                        zr = z_rand(TransportProblem.from_dict(data), samples, zrand_seed(iid, base), cfg.decoder_tol)
                    entry = {
                        "id": iid,
                        "set": set_name,
                        "m": int(m),
                        "n": int(n),
                        "seed": seed,
                        "split": split,
                        "file": path.relative_to(root).as_posix(),
                        "sha256": digest,
                        "z_rand": zr,
                        "z_rand_samples": samples if zr is not None else None,
                        "z_rand_seed": zrand_seed(iid, base) if zr is not None else None,
                        "generator": f"tpga.experiments.v2.instances.{GENERATORS[set_name].__name__}",
                    }
                    entries[iid] = entry
                out.append(InstanceV2(iid, set_name, int(m), int(n), path, seed, entry["z_rand"], split))
    if split == "test" and sets is None and "applied" in spec_all:
        out += _applied(cfg, root, entries, spec_all["applied"], samples, base)
    root.mkdir(parents=True, exist_ok=True)
    tmp = manifest_path.with_suffix(".tmp")
    tmp.write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8", newline="\n")
    tmp.replace(manifest_path)
    return out


def _applied(
    cfg: ConfigV2, root: Path, entries: dict[str, Any], spec: dict[str, Any], samples: int, base: int
) -> list[InstanceV2]:
    """Scenarios of the applied datasets, copied byte for byte from ``datasets/`` (illustration only)."""
    out = []
    for dataset in spec["datasets"]:
        set_name = APPLIED[dataset]
        src_root = cfg.root / "datasets" / dataset
        info = json.loads((src_root / "manifest.json").read_text(encoding="utf-8"))
        scenarios = [s for s in info["scenarios"] if s.get("event") not in spec.get("exclude_events", [])]
        for k, sc in enumerate(scenarios):
            iid = f"{set_name}-{k:02d}-{sc['id']}"
            src = src_root / sc["file"]
            path = root / set_name / f"{iid}.json"
            data = src.read_bytes()
            if not path.exists() or path.read_bytes() != data:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
            digest = _sha(path)
            problem = TransportProblem.from_json(path)
            m, n = problem.shape
            entry = entries.get(iid)
            if entry is None or entry.get("sha256") != digest or "z_rand" not in entry:
                entry = {
                    "id": iid,
                    "set": set_name,
                    "m": int(m),
                    "n": int(n),
                    "seed": None,
                    "split": "test",
                    "file": path.relative_to(root).as_posix(),
                    "sha256": digest,
                    "source_file": src.relative_to(cfg.root).as_posix(),
                    "dataset": dataset,
                    "scenario": sc["id"],
                    "event": sc.get("event"),
                    "balanced": bool(problem.is_balanced),
                    "data_kind": info.get("data_kind"),
                    "z_rand": z_rand(problem, samples, zrand_seed(iid, base), cfg.decoder_tol),
                    "z_rand_samples": samples,
                    "z_rand_seed": zrand_seed(iid, base),
                    "generator": None,
                }
                entries[iid] = entry
            out.append(InstanceV2(iid, set_name, int(m), int(n), path, 0, entry["z_rand"], "test"))
    return out


def select(items: list[InstanceV2], spec: Any, count: int | None = None) -> list[InstanceV2]:
    """Instances of a phase: ``spec`` is a list of set names (all sizes) or ``{set: [[m, n], ...] | "all"}``."""
    if isinstance(spec, list):
        chosen = [i for i in items if i.set in spec]
    else:
        chosen = []
        for set_name, sizes in spec.items():
            wanted = None if sizes == "all" else {tuple(s) for s in sizes}
            chosen += [i for i in items if i.set == set_name and (wanted is None or (i.m, i.n) in wanted)]
    if count is not None:
        chosen = [i for i in chosen if int(i.id.split("-")[1]) < count]
    return chosen
