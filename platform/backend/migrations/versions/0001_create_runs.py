"""Create the runs table.

Revision ID: 0001
Revises:
Create Date: 2026-11-16
"""

import sqlalchemy as sa
from alembic import op

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "runs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("job_id", sa.String(32), nullable=True),
        sa.Column("problem", sa.JSON, nullable=False),
        sa.Column("methods", sa.JSON, nullable=False),
        sa.Column("params", sa.JSON, nullable=False),
        sa.Column("results", sa.JSON, nullable=False),
    )
    op.create_index("ix_runs_created_at", "runs", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_runs_created_at", table_name="runs")
    op.drop_table("runs")
