"""Configuration of the v0.4 experiment (``experiments/paper-v2.yaml``)."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REQUIRED = ("output", "base_seed", "instance_seed_base", "runs", "budget", "instances", "methods", "phases")


@dataclass(frozen=True)
class ConfigV2:
    raw: dict[str, Any]
    path: Path

    @classmethod
    def load(cls, path: str | Path) -> ConfigV2:
        p = Path(path).resolve()
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("configuration must be a mapping")
        missing = [k for k in REQUIRED if k not in data]
        if missing:
            raise ValueError(f"configuration is missing {missing}")
        return cls(data, p)

    @property
    def root(self) -> Path:
        if "root" in self.raw:
            return Path(self.raw["root"]).resolve()
        return self.path.parent.parent if self.path.parent.name == "experiments" else self.path.parent

    def resolve(self, value: str | Path) -> Path:
        p = Path(value)
        return p if p.is_absolute() else self.root / p

    @property
    def output(self) -> Path:
        return self.resolve(self.raw["output"])

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.path.read_bytes()).hexdigest()

    @property
    def runs(self) -> int:
        return int(self.raw["runs"])

    def seeds(self, runs: int | None = None) -> list[int]:
        return [int(self.raw["base_seed"]) + r for r in range(self.runs if runs is None else runs)]

    def budget(self, m: int, n: int) -> int:
        b = self.raw["budget"]
        return int(min(int(b["cap"]), int(b["factor"]) * m * n))

    @property
    def tolerance(self) -> float:
        return float(self.raw.get("tolerance", 1e-9))

    @property
    def decoder_tol(self) -> float:
        return float(self.raw.get("decoder_tol", 1e-12))

    def method(self, name: str) -> dict[str, Any]:
        if name not in self.raw["methods"]:
            raise ValueError(f"unknown method {name!r}")
        return dict(self.raw["methods"][name])

    def phase(self, name: str) -> dict[str, Any]:
        if name not in self.raw["phases"]:
            raise ValueError(f"unknown phase {name!r}")
        return dict(self.raw["phases"][name])

    @property
    def tuned_path(self) -> Path:
        return self.resolve(self.raw.get("tuned_parameters", "experiments/tuned-v2.yaml"))

    def tuned(self) -> dict[str, Any]:
        """Frozen tuning result; empty when tuning has not been run yet."""
        if not self.tuned_path.exists():
            return {}
        data = yaml.safe_load(self.tuned_path.read_text(encoding="utf-8")) or {}
        return dict(data.get("parameters", {}))
