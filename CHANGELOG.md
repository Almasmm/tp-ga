# Changelog

All notable changes are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/)
and the project uses [Semantic Versioning](https://semver.org/).

## [0.4.1-paper] — 2026-11-20

The same code and data as `v0.4.0-paper`, released again after the repository was enabled in Zenodo, which
archives only the releases published after that.

### Changed
- Version `0.4.1-paper` in `CITATION.cff` and `.zenodo.json`; release notes `docs/releases/v0.4.1-paper.md`.

## [0.4.0-paper] — 2026-11-20

Code and data of the article at the tag `v0.4.0-paper`. The package version stays `0.4.0.dev0`: the main run
of the v0.4 experiment is not finished and its raw records are not part of this tag.

### Added
- Cycle mutation: random simplex pivots on the decoded basic plan (`tpga.cycle`, `GAXConfig`, `run_ga_x`),
  with a second rule that draws the entering arc among the arcs with theta > 0
  (`entering="nondegenerate"`), and counters of pivots, pivots with theta = 0 and unchanged offspring.
- Fixed-charge transportation problem (`tpga.fctp`): generators (uniform and with a few large suppliers),
  true cost, MIP model for HiGHS, Balinski plan.
- Local searches over basis pivots for the fixed-charge problem (`tpga.localsearch`): tabu search
  (`run_tabu`) and iterated local search (`run_ils`), with a separate counter of neighbour evaluations.
- Experiment v0.4 (`tpga.experiments.v2`, `experiments/paper-v2.yaml`): preregistration with amendments
  (`docs/v0.4/PREREGISTRATION.md`), tuning, pilot, resumable runner with a memory reserve and a process
  priority option; its quick version with artifacts in `paper_artifacts_quick/`.
- Additional experiment v3 (`tpga.experiments.v3`, amendments 8 to 10) with artifacts in
  `paper_artifacts_v3/`: one protocol for the linear problem up to 100x100, the fixed-charge problem with a
  MIP reference, MIPLIB and public instances, rivals, timing on one processor, effect sizes with intervals.
- Paired tests report the Hodges-Lehmann shift with its interval and the rank-biserial correlation.
- `.zenodo.json` and the workflow `paper-release.yml` (GitHub Release with one archive of the tracked paper
  artifacts for tags `vX.Y.Z-paper`).

## [0.3.1-paper] — 2026-11-18

Paper materials only; the library is unchanged (package version 0.3.0).

### Added
- `scripts/neutrality_check.py` and `paper_artifacts_supplement/neutrality/`: check of Proposition 3 on the
  80 test instances (no exception).
- `scripts/normalised_gap.py` and `paper_artifacts_supplement/normalised_gap/`: `Z_rand` and the normalised
  gap of the v0.3.0 runs.
- `tests/test_proposition3.py`: property test of Proposition 3 on random and degenerate instances.
- `scripts/watch_tuning.py`: read-only view of the v0.4 tuning.
- README section "Paper materials".

## [0.3.0] — 2026-11-16

### Added
- Cost-aware initial population (`tpga.initialization`): Vogel order, least-cost order, cost-sorted
  orders with noise and random permutations (work of 2026-11-09, first committed in this release).
- Datasets `kazakh-wheat` (public 2024 volumes, modelled tariffs, five scenarios) and `astana-potato`
  (modelled city network, 33 full instances and an 8×40 API sample), with generators and benchmarks.
- `rail-pilot`: template and `scripts/compare_rail.py` for comparing paid rail shipments with
  optimised plans once waybills are available; `scripts/build_rail_crossings.py` for the map layer.
- Compiled kernels (`tpga._kernels`, numba): decoder, OX1, swap mutation, tournament and random
  search written once in Python and compiled; the plain versions are the test reference.
- `run_ga`: decoder-call budget (`max_evaluations`), stagnation stop, progress/cancel callback,
  exact improvement record; `run_random_search` (RS control).
- Classical methods with step traces (`tpga.classical`: NWC, LCM, VAM), basis tools
  (`tpga.basis`), independent plan check (`tpga.verify`), detailed LP report
  (`tpga.exact.solve_lp_detailed`), GA trace for teaching (`tpga.ga_trace`), decoder trace.
- Experiment package `tpga.experiments` (YAML configuration `experiments/paper.yaml`, resumable
  runner, pinned workers with recorded core class, reachability check, report with tables T1–T6,
  figures F1–F6 in English and Russian, NUMBERS/METHODS/LIMITATIONS documents) and its artifacts in
  `paper_artifacts/`.
- Platform API: jobs with SSE progress and cancellation, traces, plans for the map, read-only
  artifacts, run history in SQLite with Alembic migrations, `/version`; CORS for the local front end,
  JSON access logs.
- Web interface rebuilt: design system (Aspan/Astana), eight pages, Russian and English, ESLint,
  Playwright smoke tests; `scripts/dev.ps1`.
- Tests: hypothesis properties up to 50×50, bitwise kernel checks, experiment pipeline, API v2.

### Changed
- GA elites keep their stored fitness instead of being decoded again; `evaluations` now counts
  real decoder calls (for P individuals, G generations and e elites: P + G (P − e)). Seeded runs
  differ from 0.2.0 because the random numbers are drawn per generation in one block.
- `solve_lp` uses sparse constraints and checks the solver status.
- CI: Python 3.10–3.14 on Ubuntu and Windows, web job (lint, build, Playwright).
- Packaging metadata: SPDX licence string (setuptools ≥ 77); pytest `pythonpath` so that
  `tests/test_compare_rail.py` runs under plain `pytest` as in CI.
- Platform: `/health` unchanged; default ports 8000 (API) and 3000 (interface).

### Removed
- The previous single-page dashboard components of the web interface (replaced by the new pages).

## [0.2.0] — 2026-10-10

### Added
- Web platform API (`platform/backend`, FastAPI): `GET /health`, `POST /solve` with LP and GA; GA responses include
  the LP optimum and the gap. Dockerfile and docker-compose.
- CI job **Platform API tests**; the package build now depends on it.

### Changed
- The repository is now the single code repository of the project and is named `tp-ga`.
- GitHub Actions updated by Dependabot: `actions/checkout` v7, `actions/setup-python` v7, `actions/upload-artifact` v6.

## [0.1.0] — 2026-10-09

### Added
- `TransportProblem`: classical model, validation, balancing with a dummy source or destination, JSON input/output.
- `decode_permutation`: greedy decoder from a permutation of the m·n arcs to a feasible plan.
- `run_ga`: permutation GA (order crossover, swap mutation, tournament selection, elitism) with a run record.
- `solve_lp`: exact optimum by linear programming (SciPy HiGHS) as the reference result.
- `tpga` command-line tool (`solve`, `generate`) and matplotlib plots of convergence and shipment plans.
- Test suite (pytest), lint and format (ruff), type checking (mypy), CI and release workflows.
