"""Read-only access to the experiment artifacts in ``paper_artifacts/``."""

from __future__ import annotations

import csv
import io
import json
import math
import re
import zipfile
from functools import lru_cache
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse, PlainTextResponse, StreamingResponse

from .paths import paper_dir

router = APIRouter(prefix="/artifacts", tags=["Experiment artifacts"])

TABLE = re.compile(r"^T\d[A-Za-z0-9_]*$")
FIGURE = re.compile(r"^F\d[A-Za-z0-9_]*$")
DOCS = {"METHODS", "LIMITATIONS", "NUMBERS", "README"}


def _root() -> Path:
    root = paper_dir()
    if not root.is_dir():
        raise HTTPException(404, "Артефакты эксперимента ещё не созданы")
    return root


def _json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


@router.get("")
def index() -> dict[str, Any]:
    root = _root()
    tables = sorted(p.stem for p in (root / "tables").glob("T*.csv")) if (root / "tables").is_dir() else []
    figures = {lang: sorted({p.stem for p in (root / "figures" / lang).glob("F*.png")}) for lang in ("en", "ru")}
    reach = _json(root / "reachability.json")
    if reach:
        reach = {k: v for k, v in reach.items() if k not in ("cases", "failures")}
    return {
        "tables": tables,
        "figures": figures,
        "docs": sorted(d for d in DOCS if (root / f"{d}.md").exists()),
        "environment": _json(root / "environment.json"),
        "reachability": reach,
        "report": _json(root / "report.json"),
        "has_runs": (root / "raw" / "runs.csv").exists(),
    }


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


@router.get("/tables/{name}")
def table(name: str) -> dict[str, Any]:
    if not TABLE.match(name):
        raise HTTPException(404, "Таблица не найдена")
    path = _root() / "tables" / f"{name}.csv"
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
    path = _root() / "figures" / lang / f"{name}.{ext}"
    if not path.exists():
        raise HTTPException(404, "Рисунок не найден")
    return FileResponse(path, media_type="image/png" if ext == "png" else "application/pdf")


@router.get("/docs/{name}", response_class=PlainTextResponse)
def doc(name: str) -> str:
    if name not in DOCS:
        raise HTTPException(404, "Документ не найден")
    path = _root() / f"{name}.md"
    if not path.exists():
        raise HTTPException(404, "Документ не найден")
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=8)
def _curves(path: str, mtime: float) -> dict[tuple[str, str], dict[str, list]]:
    """Median and quartiles of the gap at each budget point, per (size, method), uniform set."""
    import pandas as pd

    cv = pd.read_csv(path)
    runs = pd.read_csv(Path(path).parents[1] / "runs.csv", usecols=["instance", "suite", "size"]).drop_duplicates()
    cv = cv.merge(runs, on="instance")
    out: dict[tuple[str, str], dict[str, list]] = {}
    for (suite, size, method), g in cv.groupby(["suite", "size", "method"]):
        grid = sorted(g["evals"].unique())
        wide = g.pivot_table(index="evals", columns=["instance", "seed"], values="gap").reindex(grid).ffill()
        q = wide.quantile([0.25, 0.5, 0.75], axis=1).T
        out[(f"{suite}/{size}", method)] = {
            "evals": [int(v) for v in q.index],
            "q1": q[0.25].round(6).tolist(),
            "median": q[0.5].round(6).tolist(),
            "q3": q[0.75].round(6).tolist(),
        }
    return out


@router.get("/convergence")
def convergence(size: str = Query(..., pattern=r"^\d+x\d+$"), suite: str = Query("uniform", pattern=r"^[a-z]+$")):
    path = _root() / "raw" / "convergence" / "main.csv"
    if not path.exists():
        raise HTTPException(404, "Кривые сходимости ещё не записаны")
    curves = _curves(str(path), path.stat().st_mtime)
    data = {method: v for (key, method), v in curves.items() if key == f"{suite}/{size}"}
    if not data:
        raise HTTPException(404, "Нет кривых для этой размерности")
    return {"suite": suite, "size": size, "methods": data}


@router.get("/instances")
def instances(suite: str | None = Query(None, pattern=r"^[a-z]+$")) -> list[dict[str, Any]]:
    manifest = _json(_root() / "instances" / "manifest.json") or {"instances": []}
    keep = ("id", "suite", "m", "n", "seed", "sha256", "balanced", "dataset")
    return [{k: e.get(k) for k in keep} for e in manifest["instances"] if suite is None or e["suite"] == suite]


@router.get("/download")
def download() -> StreamingResponse:
    """Zip of tables, figures, documents, instances and raw results."""
    root = _root()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            if path.is_file() and "pilot" not in path.relative_to(root).parts:
                zf.write(path, Path("paper_artifacts") / path.relative_to(root))
    buf.seek(0)
    headers = {"Content-Disposition": 'attachment; filename="paper_artifacts.zip"'}
    return StreamingResponse(buf, media_type="application/zip", headers=headers)
