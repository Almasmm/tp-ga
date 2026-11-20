# v0.4 experiment archive

This snapshot contains 2,952 run records from 18 November 2026. The reference and representation phases
are complete. The main phase has 350 of 23,600 runs, and the remaining phases have yet to run. Tables that
use the main phase cover the runs available in this snapshot. See [PROGRESS.md](PROGRESS.md) for phase counts.

## Run or resume the experiment

```
python scripts/run_main.py --config experiments/paper-v2.yaml --priority normal
```

`--priority` overrides the process priority in the configuration. The default is `normal`. Section 9 of the
[preregistration](../docs/v0.4/PREREGISTRATION.md) records the interruptions, restarts and priorities.

The command runs every phase in the order reference, representation, main, applied, factorial, stagnation,
legacy, timing, and writes the tables, the figures and `PROGRESS.md` after each phase. It can be started
again after an interruption: runs already recorded are not repeated. The tuned parameters are not computed
again; they are read from `experiments/tuned-v2.yaml`. The tables and figures alone are rebuilt from the raw
records with `tpga-exp report --config experiments/paper-v2.yaml`.

Use Python 3.10 or newer and install the runner with `pip install -e ".[runner]"`. The archived code
revisions, Python and package versions, and machine details are in `run_manifest.json`.

## What is where

| Path | Content |
|---|---|
| `PROGRESS.md` | Which phases are finished and their main numbers (rewritten by every report) |
| `MANUSCRIPT_MAP.md` | For every number of the article: the table, row and column it comes from |
| `tables/` | Tables T0-T10, A1 and `representation`, each as CSV and Markdown |
| `figures/final_en/` | Figures for the article: 600 dpi JPG and PDF, serif font |
| `figures/en/`, `figures/ru/` | The same figures with English and Russian labels (PNG 600 dpi, PDF) |
| `raw/runs/` | One record per run (JSON lines in parts): method, instance, seed, cost, gap, time, checks |
| `raw/curves/` | Convergence points of the runs of the phase `main` |
| `raw/representation/` | Rows of the phase `representation` |
| `instances/` | Test instances and `manifest.json` (SHA-256, LP optimum is in `raw/runs`, Z_rand) |
| `instances_train/` | Training instances used only by the tuning |
| `tuning/` | Tuning trials: `round1/`, round 2 (`*.jsonl`, `optuna-journal.log`), earlier attempts |
| `pilot/` | `PILOT.md` and `estimate.json`: measured times and the estimate of the plan |
| `logs/` | Run log (`run-*.jsonl`), errors (`errors.jsonl`), console output, `main-run.log` |
| `run_manifest.json` | Code version, configuration hash, package versions, machine, time of every phase |
| `report.json` | Files and row counts of the last report |
| `reachability.json` | Check of Proposition 2 on 1,000 instances (Section 3.1) |

## Tables

| Table | Content | Phases |
|---|---|---|
| T0_checks | Records, failed runs, feasibility of every final plan (a check; expected share 1) | all |
| T0_example1 | Example 1 of Section 2.2, recomputed | - |
| T1_instances | Instance sets | reference |
| T2_gap | Per set, size and method: mean, median, standard deviation, minimum, maximum of the gap, share of runs at the optimum, time, decoder call of the best plan | reference, main |
| T3_time, T3_fits | Run time on performance cores and power-law fits | timing |
| T4_factorial, T4_tests | Factorial plan, Friedman and post-hoc tests | factorial |
| T5_methods_gap, T5_methods_gap_norm | Paired comparisons per (set, size): wins / ties / losses, Wilcoxon p with Holm correction, rank-biserial r, Hodges-Lehmann shift with 95 % CI | reference, main |
| T6_initialisation | Random against cost-aware start | factorial |
| T7_stopping | Stopping rules | main, stagnation, legacy |
| T8_lp_scaling, T8_lp_disagreement | Exact solvers up to 1000x1000 | timing |
| T10_applied_instances, T10_applied_summary | Illustrative cases (wheat, Astana) | reference, applied |
| A1_methods_pooled | Comparisons pooled over sizes (appendix) | reference, main |
| representation | Decoder prefix, neutrality, locality, heritability | representation |

Unit of every test: the median over the seeds of one instance (10 instances per set and size), never single
runs. The Holm correction is applied within one (set, size).
