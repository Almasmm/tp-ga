"""Read-only access to the v0.4 experiment: ``paper_artifacts_v2/``, ``docs/v0.4/`` and the configuration.

Nothing here starts, stops or changes a run. Every file name comes from a fixed list or a strict pattern.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any

import yaml
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, PlainTextResponse

from .paths import docs_v04_dir, experiments_dir, paper_v2_dir
from .zipstream import zip_response

router = APIRouter(prefix="/artifacts/v2", tags=["Experiment v0.4"])

TABLE = re.compile(r"^[TA]\d[A-Za-z0-9_]*$")
FIGURE = re.compile(r"^[a-z][a-z0-9_]*$")
DOCS = {  # name -> (directory function, file name)
    "PREREGISTRATION": ("docs", "PREREGISTRATION.md"),
    "METHODS_v2": ("docs", "METHODS_v2.md"),
    "HEAVY_RUN": ("docs", "HEAVY_RUN.md"),
    "GPU": ("docs", "GPU.md"),
    "AUDIT": ("docs", "AUDIT.md"),
    "PILOT": ("artifacts", "pilot/PILOT.md"),
}
CONFIGS = {"paper-v2": "paper-v2.yaml", "tuned-v2": "tuned-v2.yaml"}


def _json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _num(v: str) -> Any:
    if v == "":
        return None
    try:
        f = float(v)
    except ValueError:
        return v
    if math.isnan(f):
        return None
    return int(f) if f.is_integer() and "." not in v and "e" not in v.lower() else f


def _doc_path(name: str) -> Path:
    where, file = DOCS[name]
    return (docs_v04_dir() if where == "docs" else paper_v2_dir()) / file


def _sha256(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


@router.get("")
def index() -> dict[str, Any]:
    root = paper_v2_dir()
    tables_dir, fig_dir = root / "tables", root / "figures"
    manifest = _json(root / "run_manifest.json")
    return {
        "available": root.is_dir(),
        "tables": sorted(p.stem for p in tables_dir.glob("*.csv") if TABLE.match(p.stem))
        if tables_dir.is_dir()
        else [],
        "figures": {
            lang: sorted({p.stem for p in (fig_dir / lang).glob("*.png")}) if (fig_dir / lang).is_dir() else []
            for lang in ("en", "ru")
        },
        "docs": sorted(name for name in DOCS if _doc_path(name).exists()),
        "report": _json(root / "report.json"),
        "phases": (manifest or {}).get("phases", {}),
        "invocations": len((manifest or {}).get("invocations", [])),
    }


@router.get("/tables/{name}")
def table(name: str) -> dict[str, Any]:
    if not TABLE.match(name):
        raise HTTPException(404, "Таблица не найдена")
    path = paper_v2_dir() / "tables" / f"{name}.csv"
    if not path.exists():
        raise HTTPException(404, "Таблица не найдена")
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        rows = [{k: _num(v) for k, v in r.items()} for r in reader]
        return {"name": name, "columns": reader.fieldnames or [], "rows": rows}


@router.get("/figures/{lang}/{name}.{ext}")
def figure(lang: str, name: str, ext: str) -> FileResponse:
    if lang not in ("en", "ru") or ext not in ("png", "pdf") or not FIGURE.match(name):
        raise HTTPException(404, "Рисунок не найден")
    path = paper_v2_dir() / "figures" / lang / f"{name}.{ext}"
    if not path.exists():
        raise HTTPException(404, "Рисунок не найден")
    return FileResponse(path, media_type="image/png" if ext == "png" else "application/pdf")


@router.get("/docs/{name}", response_class=PlainTextResponse)
def doc(name: str) -> str:
    if name not in DOCS or not _doc_path(name).exists():
        raise HTTPException(404, "Документ не найден")
    return _doc_path(name).read_text(encoding="utf-8")


@router.get("/manifest")
def manifest() -> dict[str, Any]:
    data = _json(paper_v2_dir() / "run_manifest.json")
    if data is None:
        raise HTTPException(404, "Прогон v0.4 ещё не запускался")
    return data


@router.get("/reproducibility")
def reproducibility() -> dict[str, Any]:
    """Hashes of the configuration and the frozen parameters, the tuning summary and the instance manifest."""
    configs = {}
    for name, file in CONFIGS.items():
        path = experiments_dir() / file
        configs[name] = {"file": f"experiments/{file}", "exists": path.exists(), "sha256": _sha256(path)}
    tuned_path = experiments_dir() / CONFIGS["tuned-v2"]
    tuned = None
    if tuned_path.exists():
        try:
            raw = yaml.safe_load(tuned_path.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError:
            raw = {}
        tuned = {k: raw.get(k) for k in ("frozen", "git_commit", "procedure", "parameters", "best_objective")}
        tuned["training_instances"] = len(raw.get("training_instances") or [])
    inst = _json(paper_v2_dir() / "instances" / "manifest.json")
    instances = None
    if inst:
        entries = list(inst.get("instances", {}).values())
        sets: dict[str, int] = {}
        for e in entries:
            sets[e["set"]] = sets.get(e["set"], 0) + 1
        instances = {"count": len(entries), "sets": sets}
    man = _json(paper_v2_dir() / "run_manifest.json")
    first = (man or {}).get("invocations", [{}])[0] if man else None
    return {
        "configs": configs,
        "tuned": tuned,
        "instances": instances,
        "run": {
            "invocations": len(man.get("invocations", [])) if man else 0,
            "first": {k: first.get(k) for k in ("git_commit", "packages", "config", "tuned_parameters")}
            if first
            else None,
        },
    }


@router.get("/config/{name}", response_class=PlainTextResponse)
def config(name: str) -> str:
    if name not in CONFIGS:
        raise HTTPException(404, "Файл не найден")
    path = experiments_dir() / CONFIGS[name]
    if not path.exists():
        raise HTTPException(404, "Файл не найден")
    return path.read_text(encoding="utf-8")


@router.get("/download")
def download() -> FileResponse:
    """Tables, figures, documents, report and manifests (raw records are left out: they can be large)."""
    root = paper_v2_dir()
    if not root.is_dir():
        raise HTTPException(404, "Артефакты v0.4 ещё не созданы")
    files: list[tuple[Path, Path]] = []
    for sub in ("tables", "figures", "pilot"):
        files += [
            (p, Path("paper_artifacts_v2") / p.relative_to(root))
            for p in sorted((root / sub).rglob("*"))
            if p.is_file()
        ]
    for file in ("report.json", "run_manifest.json", "instances/manifest.json"):
        if (root / file).exists():
            files.append((root / file, Path("paper_artifacts_v2") / file))
    for name in DOCS:
        path = _doc_path(name)
        if path.exists() and DOCS[name][0] == "docs":
            files.append((path, Path("docs/v0.4") / path.name))
    return zip_response(files, "paper_artifacts_v2.zip")
