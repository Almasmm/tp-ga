# Second-review experiments

All results in this directory are exploratory. [Amendment 11](../../docs/v0.4/PREREGISTRATION.md)
sets the instances, parameters, comparisons and 120-minute limit. It was committed as `2926e69`
before the first calculation. No parameter was selected on a test instance.

| Block | Results |
|---|---|
| K1 | [Run-level costs and effort](tables/K1_runs.md), [instance medians](tables/K1_instances.md), [cell medians](tables/K1_cells.md), [cell pairs](tables/K1_pairs.md), [pooled pairs](tables/K1_pairs_pooled.md), [figure](figures/K1_fctp_population.pdf) |
| K2 | [Run-level costs and effort](tables/K2_runs.md), [instance medians](tables/K2_instances.md), [cell medians](tables/K2_cells.md), [pairs](tables/K2_pairs.md) |
| K3 | [OX counts by run and budget tenth](tables/K3_runs_by_tenth.md), [pooled counts and fractions](tables/K3_by_tenth.md), [figure](figures/K3_ox_novelty.pdf) |
| K4 | [Swap counts by run](tables/K4_runs.md), [counts and fractions by stage](tables/K4_by_stage.md) |
| K5 | [Start and final costs by run](tables/K5_runs.md), [gaps and improvement counts by cell](tables/K5_cells.md) |
| K6 | [Instance medians](tables/K6_instances.md), [cell medians and bootstrap intervals](tables/K6_cells.md), [100×100 values by instance](tables/K6_100x100_instances.md), [100×100 paired p-values](tables/K6_100x100_pairs.md), [figure](figures/K6_linear_medians.pdf) |
| K7 | [Bounds and proofs by instance](tables/K7_reference_instances.md), [bounds and proofs by cell](tables/K7_reference_cells.md), [run-level gaps and effort](tables/K7_runs.md), [methods by cell](tables/K7_methods_by_cell.md) |
| K8 | [Incumbents and gaps at the three deadlines](tables/K8_deadlines.md) |
| K9 | [All ten instances, source revision, SHA-256 and differences](tables/K9_public_instances.md) |
| K10 | [Files named in the review](tables/K10_required_files.md), [manuscript numbering](tables/K10_manuscript_map.md), [artifact sources and configurations](tables/K10_provenance.md), [historical revision mapping](tables/K10_recorded_revisions.md) |
| K11 | [The 100 archived records](tables/K11_runs.md), [counter totals](tables/K11_summary.md) |

Each linked table has a CSV with the same name. Each figure has a JPG. Blank cells indicate an
unavailable count, reference, deadline result or interval. Calculation times and evaluation units are
given in the run tables. Times for new heuristic runs reflect a shared machine. The one-core timing
block used a single process and one HiGHS thread.

In K1, A is one trajectory, B is a set of independent trajectories, C selects a parent from a population
and mutates it, and D adds OX. The suffix gives the number of initial plans. The article GA fills the final
partial generation for this comparison. ILS and Tabu come from the archived amendment 10 runs with
the same budget, instances and seeds. Their evaluation unit is one complete start plus neighbour evaluations.
Pairwise differences use percentage points. A cell of five pairs cannot provide a finite 95% interval
under the exact signed-rank inversion used here. The pooled table reports intervals across 40 instances.

K2 compares each re-encoding control with both the tuned and cycle variants under the same start.
K3 counts OX events before mutation. K4 may classify one swap in both cases, so each fraction has its
own denominator. K6 uses the archived linear runs, including the two sets of five 100×100 instances.
K7 uses the best feasible cost observed for each instance and retains the solver bound separately.

The original MIP timer starts after `passModel`, immediately before `run`. K8 starts the deadline timer before
model construction and reduces the solver time allowance by setup time. The first feasible incumbent is
taken from the HiGHS callback. A deadline without a feasible incumbent is left blank.

The K9 values are from Glover, Amini and Kochenberger (2005), Table 3, and Barr et al. (2021), Table 2.
For N504 the archived HiGHS incumbent and the CPLEX 9.0 value are both 57,130. The CPLEX 12.8 value in
Barr et al. is 56,883. The data establish the discrepancy of 247, but its cause is unknown.
[Table 3, Glover et al.](https://leeds-faculty.colorado.edu/glover/fred%20pubs/354%20-%20parametric%20ghost%20image%20fixed%20charge%20%28GIP%29.pdf)
[Table 2, Barr et al.](https://s2.smu.edu/~barr/pubs/2021ghost.pdf)

For K11, all 100 archived runs used 2,700 of 5,000 possible evaluations and made zero pivots. After the
initial population, 2,300 evaluations remained and a full generation required 2,695. The starting population
contained an optimal plan in 80 runs.

## Reproduce

Run from the repository root with the versions recorded in the source manifests and Python 3.14 for the
deadline runner. The command resumes from the experiment output and preserves its existing deadline.
For a fresh execution, use a separate working tree and an empty output directory.

```powershell
python -m tpga.experiments.v3.review2 K1
python -m tpga.experiments.v3.review2 K2
python -m tpga.experiments.v3.review2 K3
python -m tpga.experiments.v3.review2_report --replay-starts
python -m tpga.experiments.v3.review2 K8
python -m tpga.experiments.v3.review2_report
```

The first K1 attempt used unbound Numba kernels. A subsequent implementation passed uninitialized
scratch space to OX. All D rows from that implementation were discarded, including residual checks
that happened to pass. K1 was resumed on `a43fd7d`, retaining valid A, B, C and article-GA rows.
The errors are recorded in `errors.jsonl`. The shared deadline was left in place.



## Coverage and limitations

[Execution coverage](tables/K0_execution.md) and [elapsed time](tables/K0_timing.md) give the final
counts. Every planned block finished within the shared limit. In K5, the legacy convergence export
did not retain an initial-population observation for 22 runs. Their starting costs were reconstructed
with the constructor at the recorded v0.3 code revision, using the original instances and seeds.
The derived starts are kept in `raw/K5_starts.jsonl`.

K7 has a bound for every reported instance. The earlier 300-second setting was run on a subset,
and its availability is listed by cell. K8 has an observed feasible incumbent at every requested
deadline. The v0.4 time-scaling figure mentioned in the manuscript map was absent from the earlier
partial v0.4 archive. The map identifies the available v0.3 figure separately.
