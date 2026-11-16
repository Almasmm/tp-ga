# Artifacts of the computational experiment

Configuration: `experiments\paper.yaml`. Machine and software: `environment.json` (one snapshot per invocation
of the runner in `invocations`).

| Invocation started | Phases | Code version | Power scheme |
|---|---|---|---|
| 2026-11-16T01:09:32+05:00 | reachability, main, factorial, applied, stopping | `0a7a31573b` | GUID схемы питания: 381b4222-f694-41f0-9685-ff5bb260df2e  (Сбалансированная) |
| 2026-11-16T04:59:30+05:00 | timing | `eb61ad105b` | GUID схемы питания: 381b4222-f694-41f0-9685-ff5bb260df2e  (Сбалансированная) |

## Reproduce

```bash
python -m venv .venv && .venv/Scripts/activate      # Linux: source .venv/bin/activate
pip install -e ".[dev]"
python -m tpga.experiments.run --config experiments/paper.yaml       # all phases, resumable
python -m tpga.experiments.report --config experiments/paper.yaml    # tables, figures, documents
```

`--pilot` runs a short pilot and writes `pilot/estimate.json`; `--phase NAME` runs one phase.

## Wall time of the recorded run

| Phase | Hours | Errors |
|---|---|---|
| reachability | 0.00 | 0 |
| main | 1.32 | 0 |
| factorial | 0.22 | 0 |
| applied | 0.95 | 0 |
| stopping | 1.30 | 0 |
| timing | 0.06 | 0 |

Rows in `raw/runs.csv`: 28012.

## Contents

* `instances/` — every instance as JSON; `instances/manifest.json` gives seed, SHA-256 and provenance.
* `raw/runs.csv` — one row per run (LP and classical methods: one row per instance); `raw/timing.csv`
  — RQ3 timing phase on performance cores; `raw/convergence/*.csv.gz` (+ `.parquet`) — best cost at
  log-spaced decoder-call counts (the runner appends to plain `.csv`; archived gzip-compressed).
* `reachability.json` — decoder reproduction of HiGHS vertices.
* `tables/` — T1 instance sets, T2 gap, T3 time and fits, T4 factorial plan (+ tests), T5 method
  comparison tests, T6 applied cases; CSV and Markdown.
* `figures/en`, `figures/ru` — F1 decoder example, F2 convergence, F3 gap boxplots, F4 time scaling,
  F5 factorial heat map, F6 wheat map; PNG (600 dpi) and PDF, Times New Roman.
* `METHODS.md`, `LIMITATIONS.md`, `NUMBERS.md` — method description, limitations, every number with its source.
