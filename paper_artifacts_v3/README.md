# paper_artifacts_v3: cycle mutation, one linear protocol, fixed-charge problem

Results of the additional experiment v3. The plan was written before the code and the runs:
`docs/v0.4/PREREGISTRATION.md`, amendment 8, and the record of its rules after it. This experiment is not part
of the pre-registered v0.4 plan and does not replace it; `paper_artifacts_v2/` is not touched.

Amendment 9 extends it **after the results of amendment 8 were seen**: the 100x100 set with all 10 instances
(9.1), a grid on FCTP training instances (9.2), the MIP solver with the time of the GA (9.3) and FCTP sizes
50x50 and 70x70 (9.4). Its rules were also written before its runs; its results are marked below.

## Reproduce

```
pip install -e ".[runner]"
python -m tpga.experiments.v3 kselect   --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 pilot     --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 run       --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 extend    --config experiments/paper-v3-cycle.yaml      # amendment 9.1
python -m tpga.experiments.v3 run       --config experiments/paper-v3-fctp.yaml
python -m tpga.experiments.v3 benchmark --config experiments/paper-v3-fctp.yaml
python -m tpga.experiments.v3 tune      --config experiments/paper-v3-fctp-ext.yaml   # amendment 9.2
python -m tpga.experiments.v3 run       --config experiments/paper-v3-fctp-ext.yaml   # amendment 9.2-9.4
python scripts/neutrality_check.py --operators paper_artifacts_v3/kselect/selected.json
python -m tpga.experiments.v3 report    --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 report    --config experiments/paper-v3-fctp.yaml
python -m tpga.experiments.v3 report    --config experiments/paper-v3-fctp-ext.yaml
```

Every command can be started again: finished runs are read from the raw files and are not repeated. Costs,
gaps and counts depend only on the seeds; run times depend on the machine and on the number of runs at once
and are not a timing result. The pilot decides the reduction of the 100x100 set from measured times, so on
another machine the plan of the linear run may contain 10 instances of 100x100 at once; `extend` then has
nothing to run. Two parts depend on the machine by design: a MIP run that stops at its time limit, and the
limits of amendment 9.3, which are the recorded run times of the GA.

## Contents

| Path | What |
|---|---|
| `kselect/kselect.csv`, `kselect/selected.json` | grid of k on the training instances and the chosen k (8.2) |
| `kselect/records.jsonl`, `kselect/instances/` | raw runs and training instances of the choice of k |
| `linear/pilot.json` | pilot times, estimate and the decision of the reduction rule (8.3) |
| `linear/instances/` | instances with seeds, SHA-256, Z* and Z_rand (`manifest.json`) |
| `linear/raw/runs.jsonl` | one record per run of the linear protocol |
| `linear/tables/T1_gap` | gap, normalised gap, run time by set, size and method |
| `linear/tables/T2_tests` | paired comparisons: wins/ties/losses, Wilcoxon, Holm, rank-biserial r |
| `linear/tables/T2_tests_extension` | 9.1: the 100x100 tests on the first 5, the added 5 and all 10 instances |
| `linear/extension.json` | 9.1: marker that the plan was completed to every instance |
| `linear/tables/T3_by_size` | medians by method and size (gap, normalised gap, time) |
| `linear/tables/T4_cycle_counters` | pivots and pivots with theta = 0 inside the GA runs |
| `linear/figures/linear_gap_norm` | normalised gap by size |
| `fctp/instances/` | generated fixed-charge instances (`manifest.json` with seeds) |
| `fctp/raw/mip.jsonl`, `fctp/raw/runs.jsonl` | MIP reference and one record per run |
| `fctp/tables/F1_mip_instances`, `F1_mip_summary` | MIP status, value, bound, gap, time; best known value |
| `fctp/tables/F2_gap` | gap of every method by size and rho |
| `fctp/tables/F3_tests`, `F3_cells` | paired comparisons on all instances and per rho; counts per cell |
| `fctp/benchmark/source/` | the three MIPLIB 2017 instances as downloaded (`*.mps.gz`) |
| `fctp/benchmark/instances/`, `fctp/raw/benchmark*.jsonl` | converted instances and runs of the benchmark |
| `fctp/tables/B1_benchmark_reference`, `B2_benchmark_gap` | external benchmark (8.5) |
| `fctp/figures/fctp_gap` | gap by size for each rho |
| `fctp/tune/` | 9.2: training instances, their MIP records, the runs of the grid, `grid.csv`, `selected.json` |
| `fctp/raw/runs_ft.jsonl` | 9.2: runs of GA-cost-cycle-ft and GA-hybrid-ft on the 40 instances |
| `fctp/large/instances/`, `fctp/raw/large_mip.jsonl`, `large.jsonl` | 9.4: instances 50x50 and 70x70, MIP and runs |
| `fctp/raw/mip_time.jsonl` | 9.3: MIP runs with the time of the GA as the limit |
| `fctp/tables/E1_tuning` | 9.2: mean training gap of the 48 configurations and the two chosen ones |
| `fctp/tables/E2_gap_tuned`, `E3_tests_tuned` | 9.2: gap and paired comparisons of the chosen variants |
| `fctp/tables/E4_mip_equal_time` | 9.3: MIP plan at the time of the GA, at 10 times it and at 60 s against the GA |
| `fctp/tables/E5_large_mip`, `E6_large_gap`, `E7_large_tests` | 9.4: MIP reference, gaps and tests at 50x50 and 70x70 |
| `fctp/figures/fctp_gap_sizes` | 9.2-9.4: gap by size from 10x10 to 70x70 |
| `neutrality/operators_instances.csv`, `operators_summary.csv` | offspring with an unchanged plan: `swap_scaled` and cycle mutation |
| `neutrality/neutrality_operators` | figure of that measurement |
| `run_manifest.json` | every command with its time, configuration hash, software and machine |

Tables are written as `.csv` and `.md`; figures as `.pdf` and `.jpg`.

## Definitions

* Linear problem: gap = 100 (Z - Z*) / Z*, Z* the LP optimum (HiGHS); normalised gap =
  (Z - Z*) / (Z_rand - Z*), Z_rand the mean cost of 1000 decoded random permutations.
* FCTP: gap = 100 (Z - Z_best) / Z_best, Z_best the proved MIP optimum, otherwise the best known value.
  The tables `F*` use the runs of amendment 8; the tables `E*` also count the runs and MIP plans of
  amendment 9, so a gap on an instance without a proved optimum can differ between the two.
* Budget: 200 m n evaluations per run. One offspring of the cycle mutation is one decoder call; in GA-hybrid
  the decoding that starts a local-search step and every neighbour it evaluates are counted as well.
* Unit of every test: the instance (median over its 10 seeds).

## What amendment 9 gave

* 100x100 with 10 instances: all five comparisons of the linear protocol pass the Holm correction at that
  size; the five added instances alone repeat the directions of the first five.
* A grid on FCTP training instances (population, pivots, local-search period) does not improve GA-cost-cycle
  on the 40 test instances (19 wins, 3 ties, 18 losses, p = 0.72), and a local search applied 20 to 110 times
  per run does not help either (11, 11, 18, p = 0.72).
* With the run time of the GA as its limit (0.07 to 1.8 s) the MIP solver is worse than the median
  GA-cost-cycle run on 38 of the 40 instances up to 30x30 and equal on 2; with ten times that limit it is
  better on 34.
* At 50x50 and 70x70 the MIP solver with 60 s is better than every GA variant on all 20 instances
  (GA gap 6.6 to 11.9 % to the MIP plan), and better than GA-cost-cycle on 19 of 20 with the time of the GA.

## Limits of these results

* Amendment 9 was written after the results of amendment 8 were seen. The test at 100x100 on ten instances
  includes the five that had been seen; `T2_tests_extension` gives the three sets separately.
* The parameters of all methods come from the tuning on the linear problem (`experiments/tuned-v2.yaml`);
  only k was chosen, on linear training instances. On FCTP only the population, k and the local-search
  period of the cost-aware variant were put on a grid of 48 configurations (amendment 9.2); the other methods
  were not tuned on FCTP, and the grid gave no significant change.
* With the population of 2700 of GA-cost the budget gives few generations on the small FCTP sizes, so the
  local search of GA-hybrid is applied 0, 1, 2 and 6 times at 10x10, 15x15, 20x20 and 30x30. GA-hybrid-ft
  applies it 20 to 200 times per run (mean by size) and is not better.
* No heuristic run is below a MIP plan on any FCTP instance. The GA is ahead of the MIP solver only at the
  same short time up to 30x30; the comparison by time is from one machine with 20 runs at once and is not
  tested.
* Inside the GA runs 1.6 to 75 % of the pivots have theta = 0 (`T4_cycle_counters`); no operator was changed
  to address this.
* The instances up to 50x50 and the structured 20x20 are instances of the v0.4 plan; the 100x100 instances
  are new. The generated FCTP instances are synthetic; the external benchmark has three instances.
