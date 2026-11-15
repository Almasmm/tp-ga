FROM python:3.12-slim
WORKDIR /srv
COPY pyproject.toml README.md /src/
COPY src /src/src
RUN pip install --no-cache-dir "/src[experiments]" fastapi "uvicorn[standard]" "sqlalchemy>=2.0" "alembic>=1.13"
COPY platform/backend/app ./app
COPY platform/backend/migrations ./migrations
COPY datasets ./datasets
ENV TPGA_DATASETS_DIR=/srv/datasets \
    TPGA_ARTIFACTS_DIR=/srv/paper_artifacts \
    TPGA_DB_PATH=/srv/data/runs.db
EXPOSE 8000
# 0.0.0.0 inside the container; docker-compose publishes the port on 127.0.0.1 only
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
