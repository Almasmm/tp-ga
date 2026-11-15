"""Experiment configuration read from YAML; every parameter of the runs lives in the file."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

METHOD_CODES = ("LP", "NWC", "LCM", "VAM", "RS", "GA-rand", "GA-cost")
GA_METHODS = {"GA-rand": "random", "GA-cost": "cost-aware"}


@dataclass(frozen=True)
class GAParams:
    population: int
    crossover_rate: float
    mutation_rate: float
    tournament: int
    elite: int

    def config_id(self, budget: Budget, stagnation: int | None) -> str:
        stop = "none" if stagnation is None else str(stagnation)
        return (
            f"P{self.population}-pc{self.crossover_rate:g}-pm{self.mutation_rate:g}-t{self.tournament}"
            f"-e{self.elite}-{budget.rule_id}-S{stop}"
        )


@dataclass(frozen=True)
class Budget:
    """Decoder-call budget ``clamp(factor * m * n, minimum, maximum)``."""

    factor: int
    minimum: int
    maximum: int

    def of(self, m: int, n: int) -> int:
        return int(min(self.maximum, max(self.minimum, self.factor * m * n)))

    @property
    def rule_id(self) -> str:
        return f"B{self.factor}mn-{self.minimum}-{self.maximum}"


@dataclass(frozen=True)
class Config:
    raw: dict[str, Any]
    path: Path

    @classmethod
    def load(cls, path: str | Path) -> Config:
        p = Path(path).resolve()
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("configuration must be a mapping")
        for key in ("output", "base_seed", "runs", "budget", "stagnation", "ga_base", "instances", "phases"):
            if key not in data:
                raise ValueError(f"configuration is missing {key!r}")
        return cls(data, p)

    @property
    def root(self) -> Path:
        """Directory against which relative paths in the file are resolved (the repository root).

        The optional key ``root`` sets it; otherwise it is the parent of ``experiments/``."""
        if "root" in self.raw:
            return Path(self.raw["root"]).resolve()
        return self.path.parent.parent if self.path.parent.name == "experiments" else self.path.parent

    @property
    def output(self) -> Path:
        out = Path(self.raw["output"])
        return out if out.is_absolute() else self.root / out

    @property
    def base_seed(self) -> int:
        return int(self.raw["base_seed"])

    @property
    def runs(self) -> int:
        return int(self.raw["runs"])

    @property
    def tolerance(self) -> float:
        return float(self.raw.get("tolerance", 1e-9))

    @property
    def lp_repeats(self) -> int:
        return int(self.raw.get("lp_repeats", 5))

    @property
    def budget(self) -> Budget:
        b = self.raw["budget"]
        return Budget(int(b["factor"]), int(b["min"]), int(b["max"]))

    @property
    def stagnation(self) -> int:
        return int(self.raw["stagnation"])

    @property
    def convergence_points(self) -> int:
        return int(self.raw.get("convergence_points", 100))

    @property
    def ga_base(self) -> GAParams:
        g = self.raw["ga_base"]
        return GAParams(
            int(g["population"]),
            float(g["crossover_rate"]),
            float(g["mutation_rate"]),
            int(g["tournament"]),
            int(g["elite"]),
        )

    def seeds(self, runs: int | None = None) -> list[int]:
        return [self.base_seed + r for r in range(self.runs if runs is None else runs)]

    def phase(self, name: str) -> dict[str, Any]:
        phases = self.raw["phases"]
        if name not in phases:
            raise ValueError(f"unknown phase {name!r}")
        return dict(phases[name])
