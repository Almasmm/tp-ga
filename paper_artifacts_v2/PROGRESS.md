# Progress of the v0.4 main run

Written by `tpga-exp report` on 2026-11-18 12:59 from 2,952 run records. A phase is ready when every run of its task plan is recorded.

| Phase | Status |
|---|---|
| reference | ready (712 of 712 runs) |
| representation | ready (1,890 of 1,890 runs) |
| main | in progress (350 of 23,600 runs) |
| applied | not started (0 of 1,075 runs) |
| factorial | not started (0 of 24,000 runs) |
| stagnation | not started (0 of 1,800 runs) |
| legacy | not started (0 of 1,800 runs) |
| timing | not started (0 of 380 runs) |

## Where the results are

* Tables (CSV and Markdown): `paper_artifacts_v2/tables/`
* Figures for the article (600 dpi JPG and PDF, serif font): `paper_artifacts_v2/figures/final_en/`
* Figures with English and Russian labels (PNG, PDF): `paper_artifacts_v2/figures/en/`, `paper_artifacts_v2/figures/ru/`
* Raw records: `paper_artifacts_v2/raw/`; run log and errors: `paper_artifacts_v2/logs/`
* Source of every number of the article: `paper_artifacts_v2/MANUSCRIPT_MAP.md`

Numbers of a phase that is not ready are left out below; its tables exist but cover only the runs recorded so far.

## Main numbers of the finished phases

### reference: optimum and classical rules

Tables: T0_checks, T0_example1, T1_instances, T2_gap (LP, NWC, LCM, VAM).

| phase | records | failed_runs | plans_checked | plans_infeasible | plans_feasible_share | max_residual |
|---|---|---|---|---|---|---|
| main | 350 | 0 | 350 | 0 | 1.000 | 0 |
| reference | 712 | 0 | 712 | 0 | 1.000 | 0 |
| representation | 1890 | 0 | 0 | 0 | – | – |
| total | 2952 | 0 | 1062 | 0 | 1.000 | 0 |

Median gap, %, uniform set (`T2_gap.gap_median`):

| size | NWC | LCM | VAM |
|---|---|---|---|
| 5x5 | 97.739 | 12.261 | 1.067 |
| 10x10 | 210.668 | 30.088 | 8.377 |
| 20x20 | 550.556 | 50.665 | 22.725 |
| 30x30 | 699.735 | 49.214 | 25.623 |
| 50x50 | 1077.667 | 70.825 | 31.474 |
| 100x100 | 2007.940 | 85.213 | 43.123 |
| 200x200 | 3273.406 | 95.478 | 44.624 |

### representation: why the gap grows with the size (non-confirmatory)

Tables: representation; figure representation_neutrality.

| size | measure | operator | k | metric | median | q1 | q3 |
|---|---|---|---|---|---|---|---|
| 5x5 | locality | - | 1.000 | neutral_share | 0.556 | 0.538 | 0.562 |
| 5x5 | locality | - | 2.000 | neutral_share | 0.320 | 0.316 | 0.323 |
| 5x5 | locality | - | 5.000 | neutral_share | 0.075 | 0.074 | 0.079 |
| 5x5 | locality | - | 10.000 | neutral_share | 0.014 | 0.014 | 0.018 |
| 5x5 | locality | - | 20.000 | neutral_share | 0.002 | 0.001 | 0.003 |
| 5x5 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.037 | 0.035 | 0.038 |
| 5x5 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.564 | 0.554 | 0.572 |
| 5x5 | neutrality | swap_count:1 | - | neutral_share | 0.560 | 0.554 | 0.564 |
| 5x5 | neutrality | swap_count:10 | - | neutral_share | 0.011 | 0.009 | 0.014 |
| 5x5 | neutrality | swap_count:3 | - | neutral_share | 0.189 | 0.184 | 0.198 |
| 5x5 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.976 | 0.983 |
| 5x5 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.915 | 0.902 | 0.923 |
| 5x5 | neutrality | swap_fixed:1 | - | neutral_share | 0.550 | 0.537 | 0.559 |
| 5x5 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 |
| 5x5 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 0.999 | 1.000 |
| 5x5 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.989 | 0.988 | 0.992 |
| 5x5 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.548 | 0.543 | 0.557 |
| 5x5 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.552 | 0.540 | 0.569 |
| 5x5 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.325 | 0.313 | 0.334 |
| 5x5 | prefix | - | - | prefix_share | 0.890 | 0.880 | 0.920 |
| 10x10 | locality | - | 1.000 | neutral_share | 0.660 | 0.644 | 0.669 |
| 10x10 | locality | - | 2.000 | neutral_share | 0.442 | 0.436 | 0.453 |
| 10x10 | locality | - | 5.000 | neutral_share | 0.141 | 0.141 | 0.145 |
| 10x10 | locality | - | 10.000 | neutral_share | 0.021 | 0.017 | 0.023 |
| 10x10 | locality | - | 20.000 | neutral_share | 0 | 0 | 0.001 |
| 10x10 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.067 | 0.059 | 0.068 |
| 10x10 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.449 | 0.446 | 0.462 |
| 10x10 | neutrality | swap_count:1 | - | neutral_share | 0.669 | 0.666 | 0.677 |
| 10x10 | neutrality | swap_count:10 | - | neutral_share | 0.022 | 0.020 | 0.026 |
| 10x10 | neutrality | swap_count:3 | - | neutral_share | 0.301 | 0.295 | 0.309 |
| 10x10 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.985 | 0.982 | 0.987 |
| 10x10 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.931 | 0.925 | 0.936 |
| 10x10 | neutrality | swap_fixed:1 | - | neutral_share | 0.673 | 0.664 | 0.685 |
| 10x10 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.999 | 1.000 |
| 10x10 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.994 | 0.993 | 0.995 |
| 10x10 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.907 | 0.903 | 0.913 |
| 10x10 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.666 | 0.662 | 0.672 |
| 10x10 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.450 | 0.446 | 0.458 |
| 10x10 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.141 | 0.135 | 0.150 |
| 10x10 | prefix | - | - | prefix_share | 0.900 | 0.900 | 0.907 |
_80 more rows in the table file._
