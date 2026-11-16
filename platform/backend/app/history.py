"""History of runs started from the interface, stored in SQLite and migrated with Alembic."""

from __future__ import annotations

import datetime as dt
import json
import threading
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import JSON, DateTime, Integer, String, create_engine, select
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from .paths import db_path

router = APIRouter(prefix="/history", tags=["Run history"])
MIGRATIONS = Path(__file__).resolve().parents[1] / "migrations"


class Base(DeclarativeBase):
    pass


class Run(Base):
    __tablename__ = "runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True))
    title: Mapped[str] = mapped_column(String(200))
    job_id: Mapped[str | None] = mapped_column(String(32), nullable=True)
    problem: Mapped[dict] = mapped_column(JSON)
    methods: Mapped[list] = mapped_column(JSON)
    params: Mapped[dict] = mapped_column(JSON)
    results: Mapped[dict] = mapped_column(JSON)
    notes: Mapped[str | None] = mapped_column(String(2000), nullable=True)


_engine: Engine | None = None
_engine_path: Path | None = None
_lock = threading.Lock()


def migrate(path: Path) -> None:
    """Bring the database at ``path`` to the latest Alembic revision."""
    from alembic import command
    from alembic.config import Config

    cfg = Config()
    cfg.set_main_option("script_location", str(MIGRATIONS))
    cfg.set_main_option("sqlalchemy.url", f"sqlite:///{path.as_posix()}")
    command.upgrade(cfg, "head")


def engine() -> Engine:
    global _engine, _engine_path
    path = db_path()
    with _lock:
        if _engine is None or _engine_path != path:
            path.parent.mkdir(parents=True, exist_ok=True)
            migrate(path)
            _engine = create_engine(f"sqlite:///{path.as_posix()}")
            _engine_path = path
    return _engine


class SaveRequest(BaseModel):
    job_id: str = Field(..., pattern=r"^[0-9a-f]{12}$")
    title: str = Field("", max_length=200)
    notes: str | None = Field(None, max_length=2000)


def _public(r: Run, full: bool = False) -> dict[str, Any]:
    out: dict[str, Any] = {
        "id": r.id,
        "created_at": r.created_at.isoformat(),
        "title": r.title,
        "job_id": r.job_id,
        "problem": r.problem,
        "methods": r.methods,
        "params": r.params,
        "summary": {
            k: {f: v.get(f) for f in ("cost", "gap_percent", "time_s", "evaluations")}
            for k, v in (r.results.get("results") or {}).items()
        },
        "notes": r.notes,
    }
    if full:
        out["results"] = r.results
    return out


@router.get("")
def list_runs(limit: int = 100) -> list[dict[str, Any]]:
    with Session(engine()) as s:
        rows = s.scalars(select(Run).order_by(Run.id.desc()).limit(max(1, min(limit, 500))))
        return [_public(r) for r in rows]


@router.post("", status_code=201)
def save_run(req: SaveRequest) -> dict[str, Any]:
    from .jobs import manager

    job = manager.get(req.job_id)
    if job.status != "done" or job.result is None:
        raise HTTPException(409, "Сохранить можно только завершённый расчёт")
    m, n = job.result["problem"]["m"], job.result["problem"]["n"]
    run = Run(
        created_at=dt.datetime.now(dt.UTC),
        title=req.title or f"{m}×{n}: {', '.join(job.request['methods'])}",
        job_id=job.id,
        problem=job.request["problem"],
        methods=job.request["methods"],
        params=job.result["params"],
        results=json.loads(json.dumps(job.result)),
        notes=req.notes,
    )
    with Session(engine()) as s:
        s.add(run)
        s.commit()
        s.refresh(run)
        return _public(run)


@router.get("/{run_id}")
def get_run(run_id: int) -> dict[str, Any]:
    with Session(engine()) as s:
        run = s.get(Run, run_id)
        if run is None:
            raise HTTPException(404, "Запуск не найден")
        return _public(run, full=True)


@router.delete("/{run_id}", status_code=204)
def delete_run(run_id: int) -> None:
    with Session(engine()) as s:
        run = s.get(Run, run_id)
        if run is None:
            raise HTTPException(404, "Запуск не найден")
        s.delete(run)
        s.commit()
