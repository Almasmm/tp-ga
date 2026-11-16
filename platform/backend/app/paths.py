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


def paper_v2_dir() -> Path:
    return Path(os.environ.get("TPGA_ARTIFACTS_V2_DIR", REPO / "paper_artifacts_v2"))


def docs_v04_dir() -> Path:
    return Path(os.environ.get("TPGA_DOCS_V04_DIR", REPO / "docs" / "v0.4"))


def experiments_dir() -> Path:
    return Path(os.environ.get("TPGA_EXPERIMENTS_DIR", REPO / "experiments"))
