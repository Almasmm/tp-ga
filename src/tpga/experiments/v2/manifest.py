"""``run_manifest.json``: code version, configuration hash, software, machine and phase times (read only)."""

from __future__ import annotations

import hashlib
import json
import time
from importlib import metadata
from pathlib import Path
from typing import Any

from tpga.experiments import environment
from tpga.experiments.v2.config import ConfigV2
from tpga.experiments.v2.storage import write_atomic

PACKAGES = (
    "tpga",
    "numpy",
    "scipy",
    "numba",
    "llvmlite",
    "highspy",
    "ortools",
    "optuna",
    "rich",
    "psutil",
    "pandas",
    "pyarrow",
    "matplotlib",
    "pyyaml",
)


def versions() -> dict[str, str | None]:
    out: dict[str, str | None] = {}
    for p in PACKAGES:
        try:
            out[p] = metadata.version(p)
        except metadata.PackageNotFoundError:
            out[p] = None
    return out


def _sha(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def describe(cfg: ConfigV2) -> dict[str, Any]:
    info = environment.describe(cfg.root)
    info["packages"] = versions()
    try:
        import highspy

        info["highs_highspy"] = highspy.Highs().version()
    except Exception:  # noqa: BLE001
        info["highs_highspy"] = None
    info["highs_scipy"] = info.pop("highs", None)
    info["config"] = {"path": str(cfg.path), "sha256": cfg.sha256}
    info["tuned_parameters"] = {"path": str(cfg.tuned_path), "sha256": _sha(cfg.tuned_path)}
    info["instances_manifest_sha256"] = _sha(cfg.output / "instances" / "manifest.json")
    return info


def path(cfg: ConfigV2) -> Path:
    return cfg.output / "run_manifest.json"


def start(cfg: ConfigV2, phases: list[str]) -> dict[str, Any]:
    p = path(cfg)
    previous = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    snapshot = describe(cfg)
    snapshot["phases_requested"] = phases
    manifest = {
        "invocations": [*previous.get("invocations", []), snapshot],
        "phases": previous.get("phases", {}),
    }
    write_atomic(p, manifest)
    return manifest


def phase_done(
    cfg: ConfigV2, manifest: dict[str, Any], phase: str, started: float, counts: dict[str, int], interrupted: bool
) -> None:
    manifest["phases"].setdefault(phase, []).append(
        {
            "started": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(started)),
            "finished": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "wall_s": time.time() - started,
            "interrupted": interrupted,
            **counts,
        }
    )
    write_atomic(path(cfg), manifest)
