# Methods of the v0.4 experiment

What changed against v0.3.0 (`paper_artifacts/METHODS.md`) and how every number of v0.4 is produced. The
model, the greedy decoder and the GA loop are those of v0.3.0; with default parameters the library gives
bitwise the same runs (`tests/test_regression_v030.py` against `paper_artifacts/raw/runs.csv`).

## Changes in the library

| Item | v0.3.0 | v0.4 |
|---|---|---|
| Mutation | one swap with probability pm | `swap_fixed` (as before), `swap_count` (k swaps), `swap_per_position` (each position with probability q; Binomial(L, q) // 2 swaps), `swap_scaled` (round(s (m + n)) swaps) |
| Stopping | budget, 200 generations without improvement | budget only, or S generations, or S decoder calls without improvement |
| Decoder zero test | exact `> 0` | `> eps`, eps = tol max(1, max a, max b), tol = 1e-12; identical on integer data |
| Exact solver | SciPy `linprog` (HiGHS 1.12) | highspy (HiGHS 1.16) with solver, presolve, build and wrapper times; OR-Tools min-cost flow for timing and agreement |
| Comparator | RS | RS and simulated annealing (SA) on the same decoder |
| Reference cost | - | Z_rand: mean cost of 1000 decoded random permutations |

## Simulated annealing

State: a permutation, evaluated by the same decoder. Move: with probability p_ins an insertion (remove one
position and insert it elsewhere), otherwise a swap of two positions. Metropolis acceptance, geometric
cooling T_k = T0 alpha^k from T0 to T0 * final_ratio over the budget; T0 = -mean(positive deltas) / ln(p0)
from 100 pilot moves from the start (they count towards the budget), so that an average worsening move is
accepted with probability p0 = initial_acceptance. The best permutation found is returned. One decoder call
per move; the run stops when the budget is used. Start: a random permutation (SA-rand) or the Vogel order,
which decodes to the VAM plan (SA-cost).

## Common random numbers

Run r of every stochastic method on every instance uses seed 20261116 + r (one `numpy.random.Generator`,
PCG64, per run). Paired comparisons therefore compare methods on the same instances with the same seeds;
the per-instance median over seeds is the unit of every test.

## Normalised gap

gap_norm = (Z - Z*) / (Z_rand - Z*). 0 is the optimum, 1 is the expected cost of a random decoded
permutation. It makes instances with different cost scales comparable; the primary outcome stays the gap.

## Statistics (`src/tpga/experiments/reporting/stats.py`)

* **Wilcoxon signed-rank test** (two-sided), zero differences dropped. Exact distribution when n <= 50 and
  no ties among |d|, normal approximation otherwise (SciPy).
* **Matched-pairs rank-biserial correlation** r = (R+ - R-) / (R+ + R-), sign as method_a minus method_b
  (negative: method_a has the smaller gap).
* **Hodges-Lehmann shift**: median of the n (n + 1) / 2 Walsh averages (d_i + d_j) / 2, i <= j. 95 % CI:
  the Walsh averages at ranks C and N - C + 1, where C is the exact critical value of the signed-rank
  distribution (n <= 50); normal approximation for larger n.
* **Holm** correction within a family (section 5 of PREREGISTRATION.md).
* **Friedman test** with instances as blocks; **Kendall's W** = chi2 / (n (k - 1)). A family where every
  block is tied reports chi2 = 0, p = 1, W = 0.
* **Power-law fit** log10 t = log10 a + b log10(m n), least squares; 95 % CI of b from the t distribution
  with n - 2 degrees of freedom.
* p-values below 0.001 are printed as "< 0.001".

## Changes in the statistics against v0.3.0

* T4 (factorial) uses only rows of the factorial phase; v0.3.0 mixed in rows of other phases with the same
  configuration id.
* Random vs cost-aware start: one pair per instance (median over cells and seeds); v0.3.0 paired matched
  cells, which counts each instance many times.
* Method comparisons: families per (set, size), with HL shifts and CIs; the pooled rows moved to an
  appendix table.
* Time fits: over all sizes and over m n >= 2500, since small sizes are dominated by fixed costs.

## Runs and machine

* Quality phases: one process per logical processor, pinned to it (8 performance and 16 efficiency
  cores; the core class of each run is recorded). Results do not depend on the core: the budget is in
  decoder calls.
* Timing phase: performance cores only, no other phase running, no GPU.
* Raw records: `paper_artifacts_v2/raw/runs/*.jsonl`, convergence curves in `raw/curves/`, errors in
  `logs/errors.jsonl`; `run_manifest.json` holds the configuration hash, the tuning file hash, the git commit,
  the environment and the phases with their start and end times.
* GPU: not used (docs/v0.4/GPU.md).
