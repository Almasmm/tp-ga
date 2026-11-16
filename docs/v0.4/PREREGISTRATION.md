# Pre-registration of the v0.4 experiment

Written and committed **before** the main run. The commit that adds this file also adds the frozen tuning
result `experiments/tuned-v2.yaml`; the main run uses exactly these files and `experiments/paper-v2.yaml`
(its SHA-256 is recorded in `paper_artifacts_v2/run_manifest.json`). Any change after this commit is listed
in section 9 with its date and reason, before the run it affects. The progress monitor shows running
counts, errors and the gaps of finished runs; nothing in sections 1-8 is changed after the main run has
started, whatever the monitor shows.

## 1. Research questions

* **RQ1 (quality).** How far from the LP optimum are the GA's plans for a fixed budget of decoder calls,
  and is the GA better than random search (RS) and simulated annealing (SA) with the same budget, decoder
  and start?
* **RQ2 (classical heuristics).** Is the GA with a random start (GA-rand) better than the north-west corner
  rule (NWC), the least-cost method (LCM) and Vogel's approximation (VAM)? GA-cost starts from the VAM and
  LCM permutations and keeps the best by elitism, so it cannot be worse than them; it is reported, not
  tested against them.
* **RQ3 (time).** How do the run times of HiGHS, OR-Tools min-cost flow, the GA and SA grow with m n
  inside the tested range?
* **RQ4 (parameters).** How do population size, mutation operator and strength, and the start
  (random or cost-aware) affect the gap under a fixed budget?

## 2. Instances

Test instances: `experiments/paper-v2.yaml`, section `instances` — uniform (5x5 to 200x200), structured
(20x20 to 100x100), skewed (20x20, 50x50), ties (20x20, 50x50), 10 instances per set and size; lp_scaling
(100x100 to 1000x1000) for the exact solvers only. Generators and seeds are fixed in the configuration;
every file has its SHA-256 in `paper_artifacts_v2/instances/manifest.json`. Tuning used separate training
instances (seed offset 5 000 000), listed in `experiments/tuned-v2.yaml`.

## 3. Methods and budgets

LP (HiGHS via highspy, the reference optimum), LP-ortools (timing and agreement check only), NWC, LCM,
VAM, RS, GA-rand-base, GA-cost-base (the v0.3.0 base parameters, budget-only stop), GA-rand-tuned,
GA-cost-tuned, SA-rand-tuned, SA-cost-tuned. Every stochastic method gets the same budget
B = min(200 m n, cap) decoder calls, the same decoder and the same seeds: run r uses seed
20261116 + r for every method and instance (common random numbers), r = 0..29. The cap is fixed in
section 9 before the main run, from the pilot. All tuned methods had the same tuning effort
(TPE, 40 trials, the same training instances and seeds, the same objective).

Frozen result (`experiments/tuned-v2.yaml`, written 2026-11-16 23:55 +05:00 after 13 min of tuning on
8 training instances, uniform 20x20 and 50x50, 3 seeds each). The file records commit 16af15b, the commit
checked out when it was written; the tuning ran on bdf61c6, and the two differ in `src/` only by the
version string.

| Method | Parameters | Training mean gap, % |
|---|---|---|
| GA-rand | P 179, pc 0.948, t 3, e 3, swap_scaled s 0.0592 | 37.62 |
| GA-cost | P 348, pc 0.713, t 5, e 2, swap_scaled s 0.1329 | 7.71 |
| SA-rand | p_ins 0.593, p0 0.0676, final_ratio 9.12e-4 | 48.14 |
| SA-cost | p_ins 0.982, p0 0.0688, final_ratio 6.74e-5 | 15.86 |

Both SA results have p0 close to the lower end of its range [0.05, 0.95]; the range is not changed
after seeing this (it is stated here so that the reader can judge it).

## 4. Outcomes

* Primary: gap = 100 (Z - Z*) / Z*, Z* = LP optimum.
* Secondary: normalised gap (Z - Z*) / (Z_rand - Z*), Z_rand = mean cost of 1000 decoded random
  permutations of the instance; share of runs that reach the optimum; run time; decoder calls used.
* Unit of analysis for every test: the instance (median over the 30 seeds of a method), so a test with
  10 instances has 10 pairs.

## 5. Confirmatory comparisons (RQ1, RQ2)

For each (set, size) separately, two-sided Wilcoxon signed-rank tests on per-instance median gaps:

| # | method_a | method_b | question |
|---|---|---|---|
| 1 | GA-rand-base | NWC | RQ2 |
| 2 | GA-rand-base | LCM | RQ2 |
| 3 | GA-rand-base | VAM | RQ2 |
| 4 | GA-rand-base | RS | RQ1 |
| 5 | GA-rand-tuned | VAM | RQ2 |
| 6 | GA-rand-tuned | GA-rand-base | RQ1 (effect of tuning) |
| 7 | GA-cost-tuned | VAM | reported, see RQ2 |
| 8 | SA-rand-tuned | VAM | RQ1 |
| 9 | SA-rand-tuned | GA-rand-tuned | RQ1 |
| 10 | SA-cost-tuned | GA-cost-tuned | RQ1 |

* Family for the Holm correction: the 10 comparisons of one (set, size). alpha = 0.05.
* Exact p-values when there are no ties among |differences| and n <= 50, normal approximation otherwise.
  With 10 instances the smallest exact two-sided p is 2/1024 = 0.00195; after Holm over 10 comparisons
  a comparison can still reach p_holm < 0.05 when all 10 differences have the same sign.
* Effect sizes reported for every row: matched-pairs rank-biserial r, wins/losses/ties, and the
  Hodges-Lehmann estimate of the shift (percentage points) with its exact 95 % CI (Walsh averages).
* The same tests on the normalised gap are reported as secondary.
* Comparisons pooled over sizes are reported only in an appendix table and are not used for conclusions.

## 6. RQ3 and RQ4

* RQ3: phase `timing`, performance cores only, nothing else running; per-instance median of 3 runs
  (GA, SA) or 5 solver calls (LP). Fit log10 t = log10 a + b log10(m n) by least squares, once over all
  sizes and once over m n >= 2500, with a 95 % CI of b. No extrapolation outside the tested sizes.
* RQ4: phase `factorial`, uniform 20x20 and 50x50, population {20, 50, 100, 200, 400} x 12 mutation
  settings (4 operators x 3 strengths) x start {random, cost-aware}, 30 seeds, budget-only stop. Per
  (size, start): Friedman test over all cells with instances as blocks, Friedman tests per factor
  (median over the other factor), Kendall's W, post-hoc Wilcoxon tests with Holm within each factor.
  Random vs cost-aware: one pair per instance (median over cells and seeds), Wilcoxon, HL shift.

## 7. Additional, not confirmatory

* Stopping rules on uniform 20x20, 50x50, 100x100: budget only vs stagnation (0.1 B decoder calls without
  improvement) vs 200 generations without improvement (the v0.3.0 rule), paired by instance.
* Agreement of HiGHS and OR-Tools optima on every timing instance (expected: no disagreement).

## 8. Data handling

* Every run is written once (key: phase, set, instance, method, configuration, seed); interrupted runs are
  repeated from the start, so no partial run enters the data.
* No run is excluded. A run that fails (exception, infeasible plan, cost below the optimum) is written to
  `logs/errors.jsonl` and reported with its count; it is not replaced by another seed. A failed key has no
  record, so resuming the run repeats it with the same seed (deterministic: it fails again unless the
  cause was external, such as running out of memory); every error stays in the log.
* Tables and figures are produced only by `tpga-exp report` from the raw records.
* v0.3.0 results (`paper_artifacts/`) are not changed; the comparison with them is a separate document.

## 9. Amendments before the main run

| Date | Change | Reason |
|---|---|---|
| (to be filled at the decision point) | budget cap and any reduction chosen from the pilot | run time |
