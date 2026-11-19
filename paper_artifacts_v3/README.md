# paper_artifacts_v3: cycle mutation, one linear protocol, fixed-charge problem

Results of the additional experiment v3. The plan was written before the code and the runs:
`docs/v0.4/PREREGISTRATION.md`, amendment 8, and the record of its rules after it. This experiment is not part
of the pre-registered v0.4 plan and does not replace it; `paper_artifacts_v2/` is not touched.

Amendment 9 extends it **after the results of amendment 8 were seen**: the 100x100 set with all 10 instances
(9.1), a grid on FCTP training instances (9.2), the MIP solver with the time of the GA (9.3) and FCTP sizes
50x50 and 70x70 (9.4). Its rules were also written before its runs; its results are marked below.

Amendment 10 answers a review, again **after the results of amendments 8 and 9 were seen**, so all of its
results are exploratory: two local searches over basis pivots as rivals on FCTP (tabu search and iterated
local search), the MIP solver with all threads and 300 s, new FCTP instance classes and a public set, times
with one run at a time, the share of pivots with theta > 0 and a second rule for the entering arc, effect
sizes with intervals, a second normalisation and three figures. Everything it wrote is in `review/`. All of
its runs had a limit of 90 minutes with reduction rules written before them; the record of amendment 10 in
`docs/v0.4/PREREGISTRATION.md` says what each rule gave.

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
# amendment 10, in this order (the time rules read the time used by the commands before)
python -m tpga.experiments.v3 pilot      --config experiments/paper-v3-review.yaml
python -m tpga.experiments.v3 tune       --config experiments/paper-v3-review.yaml
python -m tpga.experiments.v3 rivals     --config experiments/paper-v3-review.yaml
python -m tpga.experiments.v3 generator  --config experiments/paper-v3-review.yaml
python -m tpga.experiments.v3 degenerate --config experiments/paper-v3-review.yaml
python -m tpga.experiments.v3 public     --config experiments/paper-v3-review.yaml   # downloads ten files
python -m tpga.experiments.v3 timing     --config experiments/paper-v3-review.yaml   # nothing else running
python -m tpga.experiments.v3 mipdefault --config experiments/paper-v3-review.yaml   # nothing else running
python -m tpga.experiments.v3 report     --config experiments/paper-v3-review.yaml   # after the three reports above
```

The commands of amendment 10 share a limit of 90 minutes (`review/budget.json`). On a slower machine the
rules keep fewer instances; on this one `mipdefault` ran 40 of its 60 instances.
`mipdefault --minutes 105` continues the same order beyond the limit and completes them. The ten public
instances are downloaded from a fixed commit of https://github.com/Tybirk/RL-FCTP and checked against the
SHA-256 values of the configuration; that repository states no licence, so the files are not stored here.

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
| `review/budget.json`, `review/tables/R0_rules` | 10.0: time of every run command and what its reduction rule gave |
| `review/pilot.json`, `review/pilot/`, `review/raw/pilot.jsonl` | 10.0: pilot times and instances |
| `review/tune/`, `review/tables/R1_tuning` | 10.1: grids of Tabu and ILS on the training instances, chosen configurations |
| `review/raw/rivals.jsonl` | 10.1: Tabu and ILS on the 60 FCTP instances |
| `review/tables/R2_gap`, `R2_z_best_lowered` | 10.1: gap of every method by size and rho with a bootstrap interval; instances whose best known value became smaller |
| `review/tables/R3_tests` | 10.1: GA-cost-cycle against Tabu and ILS (all instances, by rho, by size) |
| `review/raw/mip_default.jsonl`, `review/mip_default.json` | 10.2: MIP with all threads and 300 s; order, instances run and not run |
| `review/tables/R4_mip_instances`, `R4_mip_summary` | 10.2: status, gap and time of the MIP in both settings |
| `review/generator/`, `review/raw/gen_mip.jsonl`, `gen.jsonl` | 10.3 b: instances of the new classes, their MIP reference and runs |
| `review/tables/R5_generator_gap`, `R5_generator_tests` | 10.3 b: gap by class, rho and size; tests by class and rho |
| `review/raw/public_mip.jsonl`, `public.jsonl`, `review/tables/R6_public` | 10.3 a: the ten public instances against the published values |
| `review/raw/timing.jsonl`, `timing_mip.jsonl`, `review/timing.json`, `review/tables/R7_timing` | 10.4: times with one run at a time on one processor |
| `review/raw/linear.jsonl` | 10.5: runs with the pivots of every generation (phase `trace`) and with the second rule (phase `nd`) |
| `review/tables/R8_theta_share`, `review/figures/theta_share` | 10.5 a: share of pivots with theta > 0 along the budget |
| `review/tables/R9_entering_rule`, `R9_entering_tests` | 10.5 b: the two rules for the entering arc |
| `review/tables/S1_pairs` | 10.6: every paired comparison of v3 with rank-biserial r and the Hodges-Lehmann shift with its interval |
| `review/tables/S2_bootstrap_linear` | 10.6: linear problem, median gap by cell with a bootstrap interval |
| `review/tables/S3_normalisation` | 10.6: normalisation by Z_rand - Z* and by Z_NWC - Z*, ranks of the methods |
| `review/figures/linear_gap_sizes`, `fctp_gap_rivals` | 10.7: the two summary figures |
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
* Tables `R*` (amendment 10): Z_best is the proved optimum, otherwise the smallest cost over every MIP run
  and every heuristic run on disk; it is smaller than the value of the tables `F*` and `E*` on 22 instances
  (`R2_z_best_lowered`). Tabu and ILS start from the Balinski plan and count one evaluation for it and one
  for every neighbour whose cost they compute; the sum is the same budget 200 m n.
* Intervals: the Hodges-Lehmann shift has the interval of the Walsh averages (exact up to 50 pairs); the
  median gap of a cell has a percentile bootstrap interval over its instances (10 000 resamples).

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

## What amendment 10 gave

Exploratory. Numbers are from the tables named; the record of amendment 10 has more.

* Rivals on FCTP (`R2_gap`, `R3_tests`). With the same budget ILS and Tabu are better than GA-cost-cycle:
  against Tabu the GA wins on 6 instances, ties on 3 and loses on 51 of 60 (p_Holm = 1.9e-9, shift 3.4
  points, 95 % interval 2.4 to 4.3); against ILS 2, 3 and 55 (p_Holm = 1.3e-10, shift 4.7, interval 3.4 to
  5.7). From 20x20 up the GA loses to both on every instance. Median gap by size from 10x10 to 70x70:
  GA-cost-cycle 0.96 to 11.3 %, Tabu 0.82 to 4.0 %, ILS 0 to 1.8 %.
* MIP in its usual setting (`R4_mip_summary`). With all threads and 300 s the solver proves the optimum on
  the 30 instances up to 20x20 (as with one thread and 60 s) and on 3 of the 4 instances run at 30x30, where
  one thread and 60 s proved none; at 50x50 and 70x70 it proves none (gap at the limit 1.9 to 5.0 %). 20 of
  the 60 instances were not run (time rule).
* Instance classes (`R5_generator_gap`, `R5_generator_tests`). In the 8 groups of class and rho the GA is
  worse than Tabu and ILS (p_Holm at most 0.002). In 5 of the 18 new cells the GA is behind the Balinski
  plan, the start of the two local searches.
* Public set (`R6_public`). Ten instances of the subset of Sun et al. used by Glover et al. (2005). Our MIP
  optimum equals the published CPLEX value on the 8 instances it proves; the median ILS run is at 0 % on
  these 8 and within 0.06 % on the two 50x50; GA-cost-cycle is within 0.62 %. The fixed charges of this set
  are small: the Balinski plan alone is within 0.54 %.
* Time on one processor (`R7_timing`). GA-cost-cycle 0.055 s at 10x10 and 26 s at 70x70; Tabu 0.008 and
  0.48 s; ILS 0.006 and 0.43 s. With 20 runs at once the same runs took 1.1 to 1.7 times longer.
* Degenerate pivots (`R8_theta_share`, `R9_*`). The share of pivots with theta > 0 falls in the first tenths
  of the budget and then stays level: about 0.65 to 0.76 at 20x20, 0.41 to 0.47 at 50x50 and 0.27 to 0.31
  at 100x100. Choosing the entering arc among those with theta > 0 helps GA-cost-cycle (34 wins, 16 ties, 10
  losses; at 50x50 4.3 against 7.3 %) and hurts GA-rand-cycle (10, 15, 35; at 50x50 21.2 against 11.9 %),
  and makes a run 2.1 to 3.9 times longer. 100x100 was not compared (time rule).
* Statistics (`S1_pairs`, `S3_normalisation`). 128 paired comparisons with effect sizes and intervals. The
  order of the methods by median is the same with both normalisations in all 7 cells.

## Limits of these results

* Amendment 10 was written after the results of amendments 8 and 9 were seen; none of its tests is
  confirmatory. Tabu and ILS are our own implementations (one-pivot neighbourhood); the tabu search is not a
  reproduction of Sun et al. (1998), whose full text we could not read.
* From 30x30 up only 10 of the 30 instances have a MIP run with 300 s. On these the best known value comes
  from that run on 9 of 10; on the other 20 it comes from the MIP with 60 s or from a heuristic run (ILS on
  13), so the gaps of every method are measured against a weaker value there.
* The statement below that no heuristic run is below a MIP plan holds for the methods of amendments 8 and 9
  only: from 30x30 up, 80 of the 300 ILS runs (on 21 of the 30 instances) and 9 Tabu runs (on 7 instances)
  are below the plan of the MIP with one thread and 60 s.
* Times: one machine. The times of `R7_timing` were measured with one run at a time; all other times with 20
  runs at once.

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
