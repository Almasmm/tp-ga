"""Locations of data on disk; each can be overridden by an environment variable (tests, containers)."""

import os
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def datasets_dir() -> Path:
    return Path(os.environ.get("TPGA_DATASETS_DIR", REPO / "datasets"))


def paper_dir() -> Path:
    return Path(os.environ.get("TPGA_ARTIFACTS_DIR", REPO / "paper_artifacts"))


def db_path() -> Path:
    return Path(os.environ.get("TPGA_DB_PATH", REPO / "platform" / "data" / "runs.db"))
