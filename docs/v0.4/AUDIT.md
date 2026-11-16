# Audit before v0.4

Baseline: `main` at `b9586e2`, tag `v0.3.0-paper`. The results of the article were computed with commit
`0a7a315` (quality phases) and `eb61ad1` (timing phase); both are ancestors of the tag and the code paths
that produce results are unchanged up to the tag (see `REPORT.md`, item 9 of the open questions).

## 1. What the v0.4 task asks for and what already exists

| Item | Exists in v0.3.0? | Where | What changes in v0.4 |
|---|---|---|---|
| L1 mutation modes | Only one swap with probability p_m per offspring | `_kernels._next_generation_py` (uniform columns `2t+3 … 2t+5`), `GAConfig.mutation_rate` | Add `mutation_mode` (`swap_fixed`, `swap_count`, `swap_per_position`, `swap_scaled`) and `mutation_strength`. Extra random numbers are drawn **only** for the new modes, after the uniforms of the generation, so `swap_fixed` consumes the generator exactly as before. |
| L2 stagnation in decoder calls | Stagnation in generations only | `ga.run_ga` | Add `GAConfig.stagnation_evaluations`; record `generations_since_improvement` and `evaluations_since_improvement` in `GAResult`. |
| L3 HiGHS timing | Wall time of the `scipy.optimize.linprog` call only | `exact.solve_lp_detailed` | New `exact.solve_lp_highspy`: HiGHS run time from `Highs.getRunTime()`, presolve time from a separate `presolve()` call, model-build time and wrapper time measured apart. `linprog` path kept. |
| L4 OR-Tools | No | – | New `tpga.network_simplex` (OR-Tools `SimpleMinCostFlow`, Apache-2.0). OR-Tools 9.15 installs on Python 3.14. Integer data only (the solver works with integers). |
| L5 single Vogel implementation | Two implementations with identical rules | `initialization.vogel_order`, `classical.vogel` | `vogel_order` takes `vogel(p).order`; the old function is kept in the tests as the reference. |
| L6 simulated annealing | No | – | New `tpga.sa` with swap and insertion moves, geometric cooling, T0 from a pilot sample of moves, decoder-call budget and the same `improvements` record; numba kernel. |
| L7 normalised gap | No | – | `Z_rand` = mean cost of 1000 decoded random permutations per instance, fixed seed; `gap_norm = (Z − Z*) / (Z_rand − Z*)` in every v0.4 run record. |
| L8 tolerance in the decoder's early exit | Exact comparison `a[i] == 0` | `_kernels._decode_cost_py`, `_decode_plan_py`, `decoder._decode_valid_permutation`, `decoder.decode_trace` | Residual counts as zero when `≤ tol·max(1, max a, max b)`, `tol = 1e-12`. Integer data: unchanged (regression test). |
| L9 decoder docstring | Says the decoder makes no claim about reachability | `decoder.decode_permutation` | Refer to Proposition 2 of the article and `tests/test_properties.py::test_permutation_from_the_optimal_basis_decodes_to_the_optimum`, `paper_artifacts/reachability.json`. |
| L10 FCTP | No | – | Stage 2, after the main run. |
| Report split | One file, 1 344 lines | `experiments/report.py` | Kept **frozen** for v0.3.0 so that `python -m tpga.experiments.report --config experiments/paper.yaml` still regenerates the v0.3.0 artifacts byte for byte. v0.4 reports live in a new package `tpga.experiments.reporting` (one module per table or figure, a statistics module, tests on synthetic runs). |
| Statistics fixes | Initialisation test pooled 160 cells over the same 10 instances; no Kendall W; no Hodges–Lehmann; pooled "all synthetic" row in T5 | `report.factorial_tables`, `report.comparison_tests` | Implemented in the new package only (v0.3.0 tables stay as published). |
| Resumable storage | Append-only CSV, one row per run, flushed per row | `run.Appender`, `run.execute_tasks` | v0.4: JSON Lines parts written to a temporary file and renamed; keys (phase, set, instance, method, config, seed). The v0.3.0 runner is kept for its config. |
| Ctrl+C | Not handled: an interruption leaves the CSV usable (rows are complete) but the pool is killed abruptly | `run.execute_tasks` | v0.4 runner: workers ignore SIGINT, the main process stops submitting, waits for running tasks up to a grace period, flushes, exits; resume skips finished keys. |
| Run manifest | `environment.json` (one snapshot per invocation) | `environment.describe`, `run.main` | v0.4 `run_manifest.json` adds config hash, package versions incl. highspy/ortools/optuna, phase times. |
| Live monitor | Log line once a minute | `run.execute_tasks` | `rich` terminal monitor, `--plain` mode, state file for the web page, JSONL log. |
| `doctor`, `pilot` | Pilot exists (`run.pilot`, `estimate_plan`); no doctor | `run.py` | New `tpga-exp` CLI (`doctor`, `pilot`, `run`, `tune`, `report`). |
| Priority | Not set | – | `--priority above_normal` via `psutil` (no admin rights needed). |
| CPU pinning | Yes, `SetProcessAffinityMask`, core class recorded | `environment.pin_to_cpu`, `worker.init_worker` | Reused. |
| GPU | No | – | Prototype and measurement (`docs/v0.4/GPU.md`). `numba.cuda` is not available in numba 0.68 on this machine and CuPy is not installed; see GPU.md. |

## 2. Risks for reproducing v0.3.0

1. **Kernel signatures.** L1 and L8 change `_next_generation`, `_decode_cost`, `_decode_plan`. Every default must
   reproduce v0.3.0: `swap_fixed` uses the same uniform columns and draws no extra numbers; the tolerance only
   changes the outcome when a residual is in `(0, tol·scale]`, impossible with integer data.
   *Guard:* `tests/test_regression_v030.py` re-runs one instance per size of `experiments/paper.yaml` with 3
   seeds for GA-rand, GA-cost and RS and compares `cost`, `evaluations`, `best_eval` and `stop_reason` with
   `paper_artifacts/raw/runs.csv`.
2. **Vogel order (L5).** GA-cost starts from it; a different tie rule would change every GA-cost run.
   *Guard:* old implementation kept as a test reference and compared on random instances, plus the
   regression test above.
3. **Floating-point data (L8).** The applied datasets have non-integer costs and volumes. A decoded plan could
   differ in the last bits where a residual of order 1e-12·scale used to stay active. The article's applied
   cases are illustrations; the regression test covers the synthetic integer sets only, as required.
4. **Frozen v0.3.0 code paths.** `experiments/report.py`, `experiments/run.py`, `experiments/paper.yaml` and
   `paper_artifacts/` are not modified; `paper_artifacts_v2/` is separate.
5. **Dependencies.** New optional dependencies (`highspy`, `ortools`, `optuna`, `rich`, `psutil`) go into a
   `v2` extra; the base install of v0.3.0 is unchanged.

## 3. Web platform

**Pages** (8): overview, map, decoder, classical methods, GA, laboratory, paper experiment (v0.3.0),
methodology. **API**: `/health`, `/version`, `/solve`, `/scenarios*`, `/jobs*` (+SSE), `/trace/*`,
`/plans`, `/artifacts*`, `/history*`. **Tests**: 23 API tests, 22 Playwright scenarios; CI green on `b9586e2`.

Known problems and security notes (local single-user server bound to 127.0.0.1, no authentication):

| # | Problem | Severity | Action in v0.4 |
|---|---|---|---|
| W1 | `POST /solve` (legacy) accepts `population ≤ 1000` and `generations ≤ 5000` without a decoder-call cap; a request can block a worker thread for a long time. | Medium (DoS of the local server) | Cap `population × generations` (decoder calls) and return 422 above the cap; keep the endpoint's behaviour for the previous limits. |
| W2 | `POST /plans` runs LP, classical methods and a GA synchronously in a request thread; with 200×200 and budget 200 000 it blocks for seconds. | Low | Run it in the thread pool with a time budget check; keep sync API. |
| W3 | `GET /artifacts/download` builds the whole zip in memory. | Low | Stream from a temporary file. |
| W4 | Artifact endpoints are hard-wired to `paper_artifacts/`; no v0.4 data. | Feature | Add `/artifacts/v2/*` reading `paper_artifacts_v2/` (read only). |
| W5 | No monitor of a running experiment. | Feature | `/monitor/state` reads the runner's state file (read only); no control endpoints. |
| W6 | Job events list grows without bound for long jobs (progress every 0.1 s). | Low | Keep only the last N progress events per job, all non-progress events. |
| W7 | `/experiment` page hard-codes the six v0.3.0 sizes. | Low | Sizes from the data. |
| W8 | CORS, path validation, Markdown rendering (no raw HTML), loopback binding: checked, no change needed. | – | – |

## 4. Other findings

* `experiments/report.py` mixes loading, statistics, tables, figures and documents; the T4 phase filter bug
  (fixed in `d02dbbb`) would have been caught by a test on a synthetic `runs.csv` with a known answer —
  the new package is tested that way.
* `run.estimate_plan` assumes time depends on size and method only and ignores the stagnation stop; the v0.4
  pilot measures time per decoder call and multiplies by the budget (the main v0.4 mode stops by budget only).

## 5. Status of the web items after the v0.4 changes

| # | Status |
|---|---|
| W1 | Fixed: `/solve` returns 422 when population x (generations + 1) > 1 000 000 decoder calls (GA only). |
| W2 | Checked, not changed: `/plans` is a plain `def` endpoint, so FastAPI already runs it in its thread pool; the GA budget is capped at 200 000 decoder calls. |
| W3 | Fixed: both downloads write the zip to a temporary file, stream it and delete it. |
| W4 | Added: `/artifacts/v2`, `/tables`, `/figures`, `/docs`, `/manifest`, `/reproducibility`, `/config`, `/download` (raw records left out of the zip). |
| W5 | Added: `/monitor/state` (read only, with the age of the file and a stale flag after 60 s). |
| W6 | Fixed: events carry a sequence number; at most 500 progress events per job are kept, other events always. |
| W7 | Fixed: the convergence sizes come from T2 of the artifacts. |
