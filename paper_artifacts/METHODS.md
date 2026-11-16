# Methods

## Model

Balanced classical transportation problem: minimise sum_ij c_ij x_ij subject to sum_j x_ij = a_i,
sum_i x_ij = b_j, x_ij >= 0. An unbalanced instance gets a zero-cost dummy source or destination
before any method runs; the volume on it is reported in the `dummy_volume` column.

## Greedy decoder

A chromosome is a permutation of the m*n arcs; arc k is (k // n, k mod n).

```
decode(perm):
    a' := a; b' := b; x := 0
    for k in perm:
        if every a'_i = 0: stop
        (i, j) := (k // n, k mod n)
        q := min(a'_i, b'_j)
        if q > 0: x_ij := q; a'_i -= q; b'_j -= q
    return x
```

For a balanced problem with nonnegative data every permutation decodes to a feasible plan; with
integer data the plan is integral. Each positive allocation exhausts a row or a column, so a plan has
at most m + n - 1 positive cells and its support is acyclic (a basic solution); the tests check both
on random instances up to 50x50. Visiting arcs in row-major order gives the north-west corner rule;
visiting them by increasing cost (ties by arc index) gives the least-cost method with that tie rule;
the Vogel order of the cost-aware start gives Vogel's plan (all three checked by tests).

## Genetic algorithm

```
GA(P, pc, pm, t, e, B, S):
    pop := P permutations (random, or cost-aware start); evaluate all (P decoder calls)
    while evaluations + (P - e) <= B and fewer than S generations without improvement:
        new := the e best individuals, with their stored fitness (no decoder call)
        repeat P - e times:
            p1 := tournament of t distinct individuals; p2 := another tournament
            child := OX1(p1, p2) with probability pc, otherwise a copy of p1
            with probability pm swap two distinct random positions of child
            evaluate child (one decoder call)
        pop := new
    return the best individual found
```

* Tournament: t individuals drawn without replacement, the cheapest wins (first drawn on ties).
* OX1 variant: cut points i < j; positions i..j come from p1; the other positions are filled from
  left to right with the genes of p2 in p2's order.
* Mutation: one swap of two distinct positions with probability pm per offspring.
* Base configuration: P = 100, pc = 0.9, pm = 0.2,
  t = 3, e = 2.
* Budget: B = clamp(200 * m * n, 20000, 2000000) decoder calls;
  stagnation S = 200 generations.
* Random numbers: numpy.random.Generator (PCG64) seeded with seed = 20261116 + r for run r = 0..29.
  All uniforms of a generation are drawn at once; the compiled (numba) and plain-Python kernels give
  identical runs (tested).

### Cost-aware start (GA-cost)

The initial population contains the Vogel order (decodes to the VAM plan), the arcs sorted by cost
(decodes to the LCM plan), permutations sorted by cost plus Gaussian noise with standard deviations
0.05, 0.15 and 0.35 times the standard deviation of the costs, and every fourth further individual a
uniformly random permutation. Because elitism keeps the best individual, **GA-cost is never worse
than the better of LCM and VAM by construction**. The comparison with the classical methods (RQ2)
is therefore made with GA-rand; GA-cost is reported separately.

## Random search (RS)

B uniformly random permutations (Fisher-Yates driven by the same generator), decoded by the same
decoder; the cheapest is kept. RS always uses the full budget B, while the GA may stop earlier by
stagnation, so RS receives at least as many decoder calls as the GA.

## Exact and classical methods

* LP: scipy.optimize.linprog(method="highs"), HiGHS 1.12.0 (bundled with SciPy), sparse equality constraints,
  primal and dual feasibility tolerance 1e-9; status 0 required. Time: median of 5 solver calls.
* NWC, LCM, VAM: tpga.classical; tie and degeneracy rules are stated in the module docstring.
  Time: median of 5 calls.

## Factorial plan (RQ4)

Sizes [[20, 20], [50, 50]] (uniform set, 10 instances each), population [20, 50, 100, 200] x mutation
probability [0.01, 0.05, 0.1, 0.2] x start ['random', 'cost-aware'], 30 runs per cell, the same
budget rule and stagnation limit; other parameters as in the base configuration.

## Stopping-rule check

The pilot showed that on large instances the stagnation limit often ends a run long before the
budget is used. As a sensitivity check (not a research question), the base configuration was also
run on the uniform 50×50 and 100×100 instances with the stagnation limit removed (budget only),
with the same seeds; table T2b compares the two stopping rules.

## Timing (RQ3)

The quality phases run one process per logical processor, pinned to it; the processor has
performance and efficiency cores, and each row records the core class. The run times used for RQ3
come from a separate timing phase on performance cores only, with no other phase running; LP times
are medians of 5 solver calls in the same phase.

## Metrics and checks

* gap = 100 (z - z*) / z*; a run is optimal when |z - z*| <= 1e-9 max(1, |z*|).
* Every final plan is re-checked by tpga.verify.check_plan (plain loops, relative tolerance 1e-9);
  an infeasible plan or a cost below z* aborts the task as an experiment error.
* Convergence: the GA records each improvement of the best cost with the decoder call at which it
  happened; the stored curves sample this step function at 100 log-spaced budget points.

## Statistics

* Method comparison: Wilcoxon signed-rank test on per-instance median gaps (pairs listed in T5),
  effect sizes: matched-pairs rank-biserial r and Cliff's delta. Two Holm corrections are reported:
  `p_holm` over all rows of T5 and `p_holm_within_size` over the comparisons of one (set, size) group.
  With 10 instances per size the exact two-sided Wilcoxon p-value cannot be below 2/1024 = 0.00195,
  so under the first correction no per-size comparison can fall below 0.05 even when all 10
  differences have the same sign; the pooled rows (80 instances) do not have this floor.
* RQ4: Friedman test over the 16 (population, mutation) cells with instances as blocks, and over
  each factor separately; post-hoc pairwise Wilcoxon tests with Holm correction within each
  (size, start) group; random vs cost-aware start by a Wilcoxon test over matched cells.
* RQ3: least-squares fit of log10 t = log10 a + b log10(m n) on per-instance median times; 95%
  confidence interval of b from the t distribution. No extrapolation outside the observed range.

## Decoder example (F1)

Instance: supply [30.0, 45.0, 25.0], demand [20.0, 30.0, 25.0, 25.0], cost [[8.0, 6.0, 10.0, 9.0], [9.0, 12.0, 13.0, 7.0], [14.0, 9.0, 16.0, 5.0]];
permutation [3, 10, 6, 2, 7, 9, 0, 11, 5, 4, 1, 8] (numpy Generator seeded with 20261116).
