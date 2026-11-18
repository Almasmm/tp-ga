# paper_artifacts_v3: cycle mutation, one linear protocol, fixed-charge problem

Results of the additional experiment v3. The plan was written before the code and the runs:
`docs/v0.4/PREREGISTRATION.md`, amendment 8, and the record of its rules after it. This experiment is not part
of the pre-registered v0.4 plan and does not replace it; `paper_artifacts_v2/` is not touched.

## Reproduce

```
pip install -e ".[runner]"
python -m tpga.experiments.v3 kselect   --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 pilot     --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 run       --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 run       --config experiments/paper-v3-fctp.yaml
python -m tpga.experiments.v3 benchmark --config experiments/paper-v3-fctp.yaml
python scripts/neutrality_check.py --operators paper_artifacts_v3/kselect/selected.json
python -m tpga.experiments.v3 report    --config experiments/paper-v3-cycle.yaml
python -m tpga.experiments.v3 report    --config experiments/paper-v3-fctp.yaml
```

Every command can be started again: finished runs are read from the raw files and are not repeated. Costs,
gaps and counts depend only on the seeds; run times depend on the machine and on the number of runs at once
and are not a timing result. The pilot decides the reduction of the 100x100 set from measured times, so on
another machine the plan of the linear run may contain 10 instances of 100x100 instead of 5.

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
| `neutrality/operators_instances.csv`, `operators_summary.csv` | offspring with an unchanged plan: `swap_scaled` and cycle mutation |
| `neutrality/neutrality_operators` | figure of that measurement |
| `run_manifest.json` | every command with its time, configuration hash, software and machine |

Tables are written as `.csv` and `.md`; figures as `.pdf` and `.jpg`.

## Definitions

* Linear problem: gap = 100 (Z - Z*) / Z*, Z* the LP optimum (HiGHS); normalised gap =
  (Z - Z*) / (Z_rand - Z*), Z_rand the mean cost of 1000 decoded random permutations.
* FCTP: gap = 100 (Z - Z_best) / Z_best, Z_best the proved MIP optimum, otherwise the best known value.
* Budget: 200 m n evaluations per run. One offspring of the cycle mutation is one decoder call; in GA-hybrid
  the decoding that starts a local-search step and every neighbour it evaluates are counted as well.
* Unit of every test: the instance (median over its 10 seeds).

## Limits of these results

* The parameters of all methods come from the tuning on the linear problem (`experiments/tuned-v2.yaml`);
  only k was chosen, on linear training instances. Nothing was tuned on FCTP.
* With the population of 2700 of GA-cost the budget gives few generations on the small FCTP sizes, so the
  local search of GA-hybrid is applied 0, 1, 2 and 6 times at 10x10, 15x15, 20x20 and 30x30.
* The instances up to 50x50 and the structured 20x20 are instances of the v0.4 plan; the 100x100 instances
  are new. The generated FCTP instances are synthetic; the external benchmark has three instances.
