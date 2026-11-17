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

Each amendment is dated and was committed before the run it affects. Sections 1-8 above are read together
with these amendments; where they differ, the amendment applies.

### Amendment 1 (2026-11-17): budget and number of runs

* Chosen: option A. B = 200 m n decoder calls at every size (the cap of 8 000 000 equals 200 m n at
  200x200, so no cap is active). In the main phase the uniform 200x200 instances run with 10 seeds
  (r = 0..9, the first ten of the common seeds) instead of 30; every other size and phase keeps 30.
* Reason: run time. The pilot estimated 43.9 h for the full plan, 23.8 h with option A and 20.2 h with
  option B (cap 2 000 000, 30 seeds everywhere). Option A keeps the same budget per arc at every size, so
  the growth of the gap with size is not confounded with a smaller budget per arc; the unit of every test
  is the per-instance median, so the 200x200 tests still have 10 pairs.
* Effect on section 3: "r = 0..29" becomes "r = 0..9" for the main phase at uniform 200x200.

### Amendment 2 (2026-11-17): tuning repeated with a range that does not bind

* Reason: both SA results of the first tuning had `initial_acceptance` near the lower bound 0.05 of its range
  (0.0676 and 0.0688). A comparator tuned against a bound is disadvantaged. Forty TPE trials are also few
  for the conditional nine-dimensional GA space.
* Changes, identical for all four tuned methods (equal tuning effort):
  * `initial_acceptance`: range [0.001, 0.95], sampled on a log scale (was [0.05, 0.95], linear);
  * trials per method: 100 (was 40);
  * training instances: uniform 20x20 and 50x50 (4 each, as before) plus uniform 100x100 (2), 3 seeds,
    seed offset 5 000 000 as before; the run stops if a training instance file has the SHA-256 of a test
    instance (`paper_artifacts_v2/instances/manifest.json`);
  * all other ranges and scales unchanged.
* Bound rule, fixed before the tuning is run: after the tuning, every parameter of every method is checked
  (for the GA: population, crossover rate, tournament size, elite count and the strength of the chosen
  mutation operator). A value within 5 % of the width of its range from a bound, measured on the scale on
  which it is sampled, makes that bound widen once: by a factor of 10 for a range that spans more than a
  factor of 10 (sampled on a log scale), otherwise by half the width of the range; never beyond the domain
  of the parameter (probabilities in [0, 1], acceptance probability below 1, tournament >= 2, elite >= 1,
  population >= 2, swap count >= 1). A bound that is already at the limit of its domain is not widened and
  is reported. If any bound is widened, the tuning of all four methods is repeated once with the widened
  ranges and both results are recorded here; the second result is the one used. No further widening.
* The first result is kept as `experiments/tuned-v2-superseded.yaml` (frozen 2026-11-16 23:55 +05:00):

| Method | Parameters | Training mean gap, % |
|---|---|---|
| GA-rand | P 179, pc 0.948, t 3, e 3, swap_scaled s 0.0592 | 37.62 |
| GA-cost | P 348, pc 0.713, t 5, e 2, swap_scaled s 0.1329 | 7.71 |
| SA-rand | p_ins 0.593, p0 0.0676, final_ratio 9.12e-4 | 48.14 |
| SA-cost | p_ins 0.982, p0 0.0688, final_ratio 6.74e-5 | 15.86 |

  These training gaps were measured on 20x20 and 50x50 only and are not comparable with those of the
  repeated tuning, which includes 100x100.
* Parallel trials (added 2026-11-17, before the repeated tuning was run to the end): the trials are evaluated
  in batches of 5 at a time (Optuna ask/tell; `TPESampler(seed=20261201, constant_liar=True)`, so that the
  trials of a batch are proposed with the others treated as running). A batch is told to the sampler in trial
  order after all its runs have finished, so the result depends on the seed only; a test checks that two
  tuning runs give the same parameters. The number of trials, the training instances, the seeds, the search
  space and the selection rule (best mean training gap) are unchanged. Reason: run time (about 90 s per trial
  when trials run one at a time, about 30 s per trial in batches of 5). A first, sequential run of the
  repeated tuning was stopped after 14 GA-rand trials when this change was made; its trials were discarded
  and are not used.
* Result of the repeated tuning, round 1 (2026-11-17, 3 h 48 min; `experiments/tuned-v2-round1.yaml`, trial
  logs in `paper_artifacts_v2/tuning/round1/`; no training instance has the SHA-256 of a test instance):

| Method | Parameters | Training mean gap, % | Within 5 % of a bound |
|---|---|---|---|
| GA-rand | P 143, pc 0.977, t 5, e 1, swap_scaled s 0.0837 | 46.14 | elite = 1 (lower), pc (upper) |
| GA-cost | P 399, pc 0.952, t 7, e 4, swap_scaled s 0.1053 | 9.90 | population (upper), tournament (upper) |
| SA-rand | p_ins 0.246, p0 0.0341, final_ratio 0.0677 | 86.48 | final_ratio (upper) |
| SA-cost | p_ins 0.915, p0 0.00138, final_ratio 1.23e-5 | 14.58 | p0 (lower), final_ratio (lower) |

* Widening by the rule above (once): population [20, 400] -> [20, 4000] (log range, factor 10); tournament
  [2, 7] -> [2, 9] (half the width, 2.5, rounded down for an integer); initial_acceptance [0.001, 0.95] ->
  [0.0001, 0.95]; final_ratio [1e-5, 0.1] -> [1e-6, 0.99] (the factor 10 would give 1.0, outside the domain
  0 < final_ratio < 1; 0.99 is used). Not widened, already at the limit of the domain: elite >= 1 and
  crossover rate <= 1. Round 2 tunes all four methods again with these ranges, otherwise unchanged; its
  result is `experiments/tuned-v2.yaml` and is the one used. No further widening.
* Round 2, first start (2026-11-17, 13:13 +05:00) stopped after 10 GA-rand trials (two batches of 5; the last
  trial was written at 13:22). Cause, from the Windows system log: at 13:23:47 the computer was restarted from
  the Start menu by the user account (event 1074, StartMenuExperienceHost, "Other (Unplanned)"), followed by a
  second restart by winlogon at 13:25:36 (event 1074, reason code 0x500ff). The tuning ran as a child process of
  the agent's session and ended with it. There was no sleep (no Kernel-Power 42 / Power-Troubleshooter event)
  and no memory exhaustion (no Resource-Exhaustion event); the worst case of round 2, population 4000 on
  100x100, peaks at 1054 MiB per process (measured), so 24 processes need about 25 GiB with 33 GiB free.
  The 10 trials are kept in `paper_artifacts_v2/tuning/round2-attempt1/` and are not used.
* Round 2 restarted from the beginning (2026-11-17), with the same trials (100 per method, batches of 5), the
  same training instances, seeds and ranges. Changes to the procedure, none of which changes what is tuned or
  how a trial is scored: (a) the Optuna study is stored on disk (JournalStorage,
  `paper_artifacts_v2/tuning/optuna-journal.log`), so a crash loses at most the batch in flight; (b) batch k is
  proposed by `TPESampler(seed=20261201 + k, constant_liar=True)` (before: one sampler seeded once), so a run
  resumed from the journal proposes the same trials as an uninterrupted run (tested); (c) the tuning process
  asks Windows not to sleep while it runs (`SetThreadExecutionState`, no setting changed) and runs as a
  separate process, independent of the agent's session; (d) the number of worker processes is reduced if the
  worst case (150 MiB + 24 bytes per individual and arc) would not fit in free memory less 4 GiB; the number of
  workers does not change any result.
* Round 2 stopped a second time (2026-11-17, between 21:11 and 21:16 +05:00) with GA-rand complete (100 trials)
  and GA-cost at 15 trials; batch 3 of GA-cost (trials 15-19, populations 417 to 3995) was asked but not
  finished. The process ended without a traceback and without a Windows error event. Most likely cause:
  the commit limit of Windows (RAM plus page file, 94.4 GB) was used up, which makes allocations fail even
  with free RAM. At the time, the audio service process `DAX3API.exe` held 35.9 GB of private memory, the
  tuning view held 1.5 GB (it imported NumPy without `OPENBLAS_NUM_THREADS=1`, so OpenBLAS committed its
  buffers), and batch 3 starts with 24 runs on 100x100 that need about 12 GB; at 21:15:50 another program's
  service ended unexpectedly. The earlier memory check of the tuning used the free RAM at start only.
* Change (2026-11-17, before the resume): a run starts only while its memory is free. Memory per run is an upper
  bound of the measured peak private bytes (GA: 150 MiB + 24 bytes per individual and arc; checked at 100x100
  and 200x200 up to population 4000); the memory a batch may use is the smaller of the free RAM and the free
  commit at the start of the batch, less 4 GiB, and a run also waits while the memory free at that moment would
  not cover it. Runs are admitted in the same order as before and the results are collected in that order, so
  every trial value is unchanged; only the number of runs at once can be smaller. The resume continues from the
  journal: GA-rand is kept, batch 3 of GA-cost is marked failed and asked again with the same parameters (the
  sampler of a batch is seeded by its index), and the round continues with the same trials, instances, seeds and
  ranges.

### Amendment 3 (2026-11-17): phase `representation` (non-confirmatory; added to section 7)

* Purpose: explain why the gap grows with the size. A plan has at most m + n - 1 positive cells out of m n,
  so most swaps exchange two arcs that carry no flow in either order. A check outside the project (uniform
  costs in [1, 100], random permutations) gave 0.70, 0.81, 0.90 and 0.94 for the share of single swaps that
  leave the decoded cost unchanged at 10x10, 20x20, 50x50 and 100x100. The phase measures this with the
  project's decoder, operators and instances (`src/tpga/analysis/representation.py`).
* Instances: uniform 5x5 to 200x200 and structured, skewed and ties at 50x50, 10 instances each.
* Per instance: (1) decoder prefix — positive cells and the number of positions read before all supply is
  used, absolute and as a share of m n — for 1000 random permutations and for the final populations of
  GA-rand-tuned and GA-cost-tuned (seeds r = 0..9); (2) neutrality — share of mutation offspring whose decoded
  cost equals the parent's, for every mutation operator and strength of the factorial plan and the tuned
  settings, with parents (a) the 1000 random permutations and (b) the GA populations at 10 %, 50 % and 100 %
  of the budget; the share is also reported among offspring with at least one swap; (3) locality — for
  k = 1, 2, 5, 10, 20 random swaps: median |dZ| / Z*, the neutral share and the Spearman correlation between
  k and |dZ|; (4) heritability of the order crossover — for 200 random parent pairs from the population at
  50 % of the budget, the share of the child's positive cells that are positive in at least one parent.
* Output: `paper_artifacts_v2/tables/representation.csv` and one figure (neutral share against m n per
  operator, log x axis). No test; no conclusion of sections 5-6 depends on this phase.

### Amendment 4 (2026-11-17): phase `applied` (illustration; added to section 7)

* Reason: the article reports two illustrative cases (Section 3.7); every number of the revised article is
  to come from v0.4, so the cases are run again under the v0.4 protocol.
* Instances: the scenarios of `datasets/kazakh-wheat` (5, set `wheat`, 15x7) and `datasets/astana-potato`
  (33, set `astana`, 24x324; the 8x40 API sample is left out, as in v0.3.0), copied byte for byte with their
  SHA-256 into `paper_artifacts_v2/instances/`. Unbalanced scenarios get a zero-cost dummy node, as for every
  method. The data are modelled (see the dataset READMEs); costs are not observed freight tariffs.
* Methods: LP, NWC, LCM, VAM (reference phase) and RS, GA-rand-tuned, GA-cost-tuned, SA-rand-tuned,
  SA-cost-tuned with 10 runs (r = 0..9) and B = 200 m n of the scenario as given (budget-only stop).
* Output: `T10_applied_instances` (per scenario: mean over runs) and `T10_applied_summary` (median and range
  over the scenarios of a set; number of scenarios better than VAM; median time). No test; the cases are not
  pooled with the synthetic sets and enter no conclusion of sections 5-6.

### Amendment 5 (2026-11-17, 20:55 +05:00, during round 2): final parameters are the best of rounds 1 and 2

* Rule: the final parameters of each tuned method are those of the trial with the lowest mean training gap
  among all completed trials of round 1 and round 2 of amendment 2. The same rule for all four methods.
  On an exact tie the round-2 trial is taken. `experiments/tuned-v2.yaml` records, for every method, the
  round and the trial number the parameters come from and the best training gap of each round.
* Candidates: round 1 (`paper_artifacts_v2/tuning/round1/`, 100 trials per method) and round 2
  (`paper_artifacts_v2/tuning/`, 100 trials per method, the restarted run). The 10 trials of the first start
  of round 2 (`round2-attempt1/`) are not candidates, as stated under amendment 2. The superseded first
  tuning (`experiments/tuned-v2-superseded.yaml`) is not a candidate: it used other training instances.
* Why the rounds can be compared: both use the same 10 training instances (uniform 20x20 x 4, 50x50 x 4,
  100x100 x 2, seed offset 5 000 000), the same 3 seeds, the same budget-only stop and the same objective;
  every trial is the mean gap of the same 30 runs. Round 2 only searches a wider range.
* Reason: round 2 searches a wider range, but 100 TPE trials in a wider space need not find a point as good
  as the best point of round 1, which also lies inside the round-2 range. Using a worse training result only
  because it came later would disadvantage a method for no reason related to its quality.
* Selection uses training data only; no test instance has been run with tuned parameters. The best of 200
  trials has a slightly optimistic training gap compared with the best of 100; this concerns the training
  gap only, not the test results, and applies equally to all four methods.
* Disclosed state when this rule was written: round 2 had finished 95 of 100 GA-rand trials (best training
  gap 56.47 % against 46.14 % in round 1); GA-cost, SA-rand and SA-cost of round 2 had not started.
  Replaces the sentence "the second result is the one used" of amendment 2.

### Amendment 6 (2026-11-17): runs start only while their memory is free (procedure, no change of results)

* Reason: with the tuned populations a GA run can need several GiB (on 200x200: 2.3 GiB at population 2431,
  3.7 GiB at 4000; measured peak private bytes), so 24 runs at once need more memory than the laptop has
  (63 GB RAM, commit limit about 94 GB, part of it held by other programs). On Windows a run then fails to
  allocate, or the whole run stops (see the second stop of round 2 under amendment 2).
* Change: every phase of `tpga-exp run` uses the same rule as the tuning (`src/tpga/experiments/v2/memory.py`):
  a run starts only while the estimates of the running runs plus its own fit in the memory usable at the start
  of the phase (smaller of free RAM and free commit, less 4 GiB), and while the memory free at that moment still
  covers it; with nothing running, a run always starts. Runs start in the same order as before. Each run is
  deterministic (its own seed), so no record changes; only the number of runs at once, and so the wall time, can.
* The pilot estimates the wall time with the same rule and lists the runs that are limited by memory, with the
  number that fit at once (`paper_artifacts_v2/pilot/PILOT.md`, section Memory). The number of runs at once and
  the memory budget of each phase are written to the run log.
