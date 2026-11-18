# paper_artifacts_v2: data of the revised article (tp-ga v0.4)

Everything the revised article reports is in this directory. It is produced by one configuration,
`experiments/paper-v2.yaml`, and the frozen tuned parameters, `experiments/tuned-v2.yaml`. The plan and every
change made before the main run are in `docs/v0.4/PREREGISTRATION.md` (section 9 lists the amendments).

## Reproduce with one command

```
python scripts/run_main.py --config experiments/paper-v2.yaml --priority normal
```

`--priority` is `normal` (default) or `above_normal`; it replaces the `priority` of the configuration and
changes run times only. The stops and restarts of the published run and its priorities are in the run
record at the end of section 9 of `docs/v0.4/PREREGISTRATION.md`.

The command runs every phase in the order reference, representation, main, applied, factorial, stagnation,
legacy, timing, and writes the tables, the figures and `PROGRESS.md` after each phase. It can be started
again after an interruption: runs already recorded are not repeated. The tuned parameters are not computed
again; they are read from `experiments/tuned-v2.yaml`. The tables and figures alone are rebuilt from the raw
records with `tpga-exp report --config experiments/paper-v2.yaml`.

Set-up: Python 3.10 or newer, `pip install -e ".[runner]"` at the tag `v0.4.0-run`. The versions of the packages
and the machine of the published run are in `run_manifest.json`. Gaps and counts do not depend on the
machine; times do.

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
