"""Check the paths cited by the manuscript in the paper ZIP."""

from __future__ import annotations

import argparse
import re
from zipfile import ZipFile

REQUIRED_FILES = (
    "scripts/normalised_gap.py",
    "scripts/neutrality_check.py",
    "tests/test_proposition3.py",
    "paper_artifacts/tables/T4_factorial.csv",
    "paper_artifacts/tables/T5_tests.csv",
    "docs/v0.4/PREREGISTRATION.md",
)
REQUIRED_DIRS = ("paper_artifacts_v2/", "paper_artifacts_v3/", "paper_artifacts_v3/review2/")
SESSION = re.compile(rb"the agent.s session|assistant.s session|session of (the agent|the assistant)", re.IGNORECASE)


def check(path: str) -> None:
    with ZipFile(path) as archive:
        if damaged := archive.testzip():
            raise ValueError(f"invalid ZIP entry: {damaged}")
        files = {member.filename.partition("/")[2]: member for member in archive.infolist() if not member.is_dir()}
        missing = [name for name in REQUIRED_FILES if name not in files]
        missing.extend(directory for directory in REQUIRED_DIRS if not any(p.startswith(directory) for p in files))
        if missing:
            raise ValueError(f"missing manuscript sources: {missing}")
        if any("AGENT_PROMPT" in name.upper() for name in files):
            raise ValueError("service prompt found")
        for name, member in files.items():
            if name.endswith((".md", ".txt", ".rst")) and SESSION.search(archive.read(member)):
                raise ValueError(f"session reference found in {name}")
        print(f"{path}: {len(files)} files, required paths present, text check passed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    check(parser.parse_args().archive)
