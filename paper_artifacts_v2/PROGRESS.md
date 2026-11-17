# Progress of the v0.4 main run

Written by `tpga-exp report` on 2026-11-18 01:11 from 712 run records. A phase is ready when every run of its task plan is recorded.

| Phase | Status |
|---|---|
| reference | ready (712 of 712 runs) |
| representation | not started (0 of 1,890 runs) |
| main | not started (0 of 23,600 runs) |
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
| reference | 712 | 0 | 712 | 0 | 1.000 | 0 |
| total | 712 | 0 | 712 | 0 | 1.000 | 0 |

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
