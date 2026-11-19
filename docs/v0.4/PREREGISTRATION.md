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
  the launch session and ended with it. There was no sleep (no Kernel-Power 42 / Power-Troubleshooter event)
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
  separate process, detached from the launch session; (d) the number of worker processes is reduced if the
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

### Amendment 7 (2026-11-17, before the main run): shorter plan, run order, 10 GiB memory reserve

* Reason: время прогона; выбрано до основного прогона, по оценке пилота, без знания тестовых результатов
  (run time; chosen before the main run, from the pilot estimate, without knowledge of any test result).
  No run of the phases `main`, `stagnation`, `legacy`, `factorial`, `applied`, `representation` or `timing`
  with the final tuned parameters existed when this was written; the pilot runs use shortened budgets on one
  instance per set and size and are not used in any table.
* Rule fixed in advance: target 14 h for the pilot estimate of all phases; the reductions a-f below are
  applied in this order and only while the estimate is above the target. Never removed: RS and SA from
  `main`, any phase, any instance (10 per size and set), the common seeds r = 0..k-1 of all methods.
* Pilot with the final parameters (`paper_artifacts_v2/pilot/`, commit 2d4bec4): 28.6 h for the plan as it was
  if memory did not limit the number of runs at once, 140.9 h with the memory free at that moment. The
  estimate stayed above 14 h after every step, so all six reductions are applied:
  a. `timing`: GA and SA up to 100x100 only; LP (HiGHS) and OR-Tools on every size up to 1000x1000.
  b. `factorial`: seeds r = 0..9 instead of 0..29 (unit of analysis: median per cell and instance).
  c. `stagnation`: seeds r = 0..9 instead of 0..29.
  d. `main`, 200x200: without GA-rand-base and GA-cost-base (the tuned GA, SA and RS stay).
  e. `main`, 50x50 and 100x100: seeds r = 0..19 instead of 0..29 (200x200 keeps r = 0..9; sizes below 50x50
     keep r = 0..29).
  f. `applied`, Astana: seeds r = 0..4 instead of 0..9 (wheat keeps r = 0..9).
* After step f the estimate is 18.2 h without a memory limit and 21.2 h with 60 GiB for the runs, still above
  the target. As the rule requires, the work stopped and the author was asked; the author accepted a run of
  about 21 h with the reductions a-f and no further reduction (2026-11-17, 23:50 +05:00).
* Changed by the author on 2026-11-18, 00:30 +05:00, still before the main run (no run of any phase with the
  final parameters existed; the tag `v0.4.0-run` of commit 5cf48a7 was set but no run was started from it):
  g. `representation`: sizes up to 100x100 only, without 200x200. Reason: время; решение принято до
     основного прогона, тестовые результаты неизвестны (run time; decided before the main run, test results
     unknown). For 200x200 the article uses the exact bound of Proposition 3.
  The target of the estimate is 18 h instead of 14 h. The estimate of the plan with a-g, made with the
  memory free before the start, is in `paper_artifacts_v2/pilot/PILOT.md`; the run starts only if it is
  at most 18 h. The main run is started from the tag `v0.4.0-run2` (the commit with step g).
* Consequences for the analysis. Tests still use one value per instance (median over its seeds), 10 pairs per
  (set, size); fewer seeds make that median less precise, not the number of pairs smaller. At 200x200 the
  comparisons with GA-rand-base (against NWC, LCM, VAM, RS, and GA-rand-tuned against GA-rand-base) are not
  available; the Holm family of uniform 200x200 has the remaining pre-registered pairs. `T7` pairs the
  budget-only runs of `main` (20 or 30 seeds) with the stagnation runs (10 seeds) through per-instance
  medians. The time fits of GA and SA end at 100x100.
* Run order (was: reference, main, stagnation, legacy, factorial, applied, representation, timing):
  reference, representation, main, applied, factorial, stagnation, legacy, timing. Timing runs last and
  alone, on the performance cores. Within a phase the longest runs start first, one task per submission.
  `scripts/run_main.py` starts the phases, repeats a phase that ended with an error (recorded runs are
  skipped) and runs `tpga-exp report` after each phase at idle priority on one processor.
* Memory (extends amendment 6): a run starts only while 10 GiB stay free (`memory_reserve_gib: 10`; was
  4 GiB). When the next run in the order does not fit, the first later run that fits starts instead. The
  start order does not change any record.
* Report additions (no change of any test): `T2` also gives the standard deviation and the minimum of the gap
  and the decoder call at which the best plan was found; `T0` gives the share of feasible plans; the English
  figures are also written to `figures/final_en` (600 dpi JPG and PDF); `PROGRESS.md` lists the finished
  phases.

### Run record (2026-11-18): stops, restarts and process priority (procedure, no change of the plan)

Written on 2026-11-18 while the main run was stopped, with `reference` and `representation` finished and
350 of 23 600 runs of `main` on disk (uniform 200x200, instances 00-06, 10 seeds, five methods). Nothing in
the plan, the methods, the parameters, the seeds, the budgets or the tests is changed by this record. All
times are +05:00; the source is `paper_artifacts_v2/logs/main-run.log` and `logs/errors.jsonl`.

* 01:00:37, first start (`scripts/run_main.py`, all phases, priority `above_normal` from the configuration).
  The process ended without any message before the first run was recorded. The cause was not found.
* 01:01:27, start of the phase `reference` alone: 712 runs, done at 01:01:39.
* 01:02:31, start of all phases. `representation` ended with an error twice (01:13:24 and 01:24:30,
  `PermissionError` on the state file of the monitor) and was started again by the script; it was done at
  01:44:05. `main` started at 01:44:09.
* Code after the tag `v0.4.0-run2` (e3a8fb6): commits 298b313 and 74f0caf (01:12) and dd20843 (01:24) change
  the report on a partial run, the import order of `scripts/run_main.py` and the monitor (a locked state file
  no longer stops a phase). They do not touch the methods, the decoder, the seeds, the task list or the
  records.
* 10:55, stop: the author restarted the laptop. The last record is from 10:50:01. The 24 runs in progress
  were lost.
* 12:52:42, restart with the same command and the same priority; `main` had 23 250 runs to do.
* 12:58, stop by the author. No run finished between 12:52 and 12:58; the 19 runs in progress were lost.
* Runs lost at a stop left no record. They are listed in `logs/errors.jsonl` (43 entries, all
  `BrokenProcessPool`, phase `main`) and are run again from the start with the same seed, as every run that
  is not on disk. After both stops the records were checked: 2 952 run records, no unreadable line, no
  repeated key, every `main` run has its convergence curve.
* Priority. Up to 12:58 the runs had the priority `above_normal`. From the next start they have `normal`,
  at the request of the author, because the laptop was hard to use during the run. `scripts/run_main.py` has
  the option `--priority` (default `normal`), which replaces the value of the configuration; the commit with
  this record adds it together with a test. The priority does not enter any result that is counted in
  decoder calls (gap, best plan, convergence curve). The field `time_s` of the phases before `timing` is
  therefore measured under two priorities and in several sessions.
* Command of every further start:
  `python scripts/run_main.py --config experiments/paper-v2.yaml --priority normal`.

### Amendment 8 (2026-11-18, 23:50 +05:00): additional experiment v3 - cycle mutation, one protocol for the linear problem, fixed-charge problem

Written and committed before any code of this amendment was run and before any run of it. The plan of
sections 1-8 and amendments 1-7 (RQ1-RQ4, `experiments/paper-v2.yaml`, `paper_artifacts_v2/`) is not changed
and is not replaced; nothing below is a confirmatory test of that plan. Everything below is an addition to
section 7. The existing operators, kernels and the results of v0.3.0 and v0.4 are not changed: the new
operator and the fixed-charge objective are new modules with their own kernels. Results go to
`paper_artifacts_v3/`; the configurations are `experiments/paper-v3-cycle.yaml` and
`experiments/paper-v3-fctp.yaml`. Decisions that the task left open are marked "(decision)".

**8.1 Operator: cycle mutation.** Applied to an offspring after selection and crossover.

1. The offspring is decoded (one decoder call). Its positive arcs form a forest. If there are fewer than
   m + n - 1 of them, the forest is completed to a spanning tree with zero arcs: the arcs are scanned in
   index order (i n + j) and an arc is added when it joins two components, until the tree has m + n - 1 arcs.
2. k pivots. The entering arc is drawn uniformly from the m n - (m + n - 1) non-basic arcs (one uniform
   number per pivot: the r-th non-basic arc in index order); no cost, dual value or other LP information is
   used. The cycle of the entering arc in the tree is found; theta is the minimum flow on its minus
   positions; theta is moved along the cycle; the leaving arc is the first minus arc with flow theta on the
   path that starts at the destination of the entering arc. With theta = 0 the basis changes and the plan
   does not; these pivots are counted separately.
3. The new plan is encoded by the construction in the proof of Proposition 2: the m + n - 1 basic arcs in
   the order of leaf elimination (leaves are taken first by node index, sources before destinations, then
   first in, first out), then the non-basic arcs in the relative order they had in the offspring before the
   mutation. The offspring is replaced by this permutation; its cost is the cost of the new plan.
4. Counting: the one decoding of step 1 is the one decoder call of the offspring. Encoding is not counted;
   its time is part of the run time.
5. Implementations: Numba and plain Python with identical results. Tests fixed in advance: (a) the encoded
   permutation decodes to exactly the plan it was built from, on 10 000 random basic plans of sizes 5x5 to
   100x100; (b) the plan after a pivot is feasible; (c) the plan is unchanged only if theta = 0;
   (d) Numba and Python agree. Exactness of (a) is claimed for integer data (all instances here).
6. `scripts/neutrality_check.py` gets a second measurement: the share of offspring whose plan equals the plan
   of the parent, for the cycle mutation (selected k) and for `swap_scaled` with the tuned strength 0.0837,
   on random parents of the instances the script already uses (uniform 5x5 to 100x100, structured 20x20 and
   50x50), with the number of pivots that had theta = 0.

**8.2 Choice of k (no long tuning).** Variants GA-rand-cycle and GA-cost-cycle: every parameter of
GA-rand-tuned and GA-cost-tuned (`experiments/tuned-v2.yaml`), only the mutation operator is replaced.
Mutation probability as in the tuned configurations: `swap_scaled` and `swap_count` mutate every offspring,
so the cycle mutation is applied to every offspring (decision). Grid: k in {1, 2, 4, round(0.05 (m + n))}
(at least 1). Training instances: uniform 20x20 and 50x50 of the tuning set (`u20x20-00..03-train`,
`u50x50-00..03-train`, the same generator and seeds as in `paper_artifacts_v2/instances_train`), seeds
r = 0, 1, 2 (base 20261116), budget 200 m n, budget-only stop. For each variant separately (decision) the k
with the smallest mean normalised gap over the 8 instances and 3 seeds is taken; on a tie the smaller k,
with round(0.05 (m + n)) counted as the largest. Time limit 8 minutes: one run of each variant on
`u50x50-00-train` with k = round(0.05 (m + n)) is timed first; if the estimate of the whole grid (sum of run
times, 50x50 runs at the measured time and 20x20 runs at 0.16 of it, divided by 20 parallel runs) is above
8 minutes, only the first two training instances of each size are used.

**8.3 Linear problem, one protocol.** Instances and seeds of `experiments/paper-v2-quick.yaml`: uniform 5x5,
10x10, 20x20, 30x30, 50x50 and structured 20x20, 10 instances each (the first instances of the v0.4 plan).
Added: 10 uniform instances 100x100 from the same generator with new seeds 20290000 + i, i = 0..9
(`v3u100x100-00..09`; not instances of the v0.4 plan). Methods: VAM, RS, GA-rand-tuned, GA-cost-tuned,
SA-rand-tuned, SA-cost-tuned, GA-rand-cycle, GA-cost-cycle. 10 runs per instance (seeds 20261116 + r,
r = 0..9, common to all methods), budget B = 200 m n decoder calls, no stagnation limit. Reference: LP
optimum (HiGHS) and Z_rand (1000 random permutations) as in v0.4. Outcomes: gap, normalised gap, run time.

* Pilot and reduction rule: one run (seed r = 0) of every stochastic method on the first instance of every
  size; these are planned runs and are kept. Estimated total time = sum over all planned runs of the pilot
  time of their (method, size), divided by 20 (24 logical processors, 16 of them efficiency cores with the
  speed ratio 1.32 of the v0.4 pilot). If the estimate is above 30 minutes, the 100x100 set is reduced to its
  first 5 instances (`v3u100x100-00..04`). Nothing else is reduced; the run then starts whatever the
  estimate.

**8.4 Fixed-charge problem (FCTP).** Minimise sum c_ij x_ij + sum f_ij [x_ij > 0] over the plans of the
balanced transportation polytope.

* Generator: supplies and demands as in the uniform set (supplies U{20..100}, demands 1 + multinomial);
  c_ij ~ U{1..100}; f_ij ~ U{1..F}, F = round(2 rho c_mean S / (m + n - 1)), S = total supply, c_mean = mean
  of the generated c_ij, rho in {0.2, 1.0}. Sizes 10x10, 15x15, 20x20, 30x30; 5 instances per (size, rho),
  40 in all. Seeds 20300000 + 1000 s + 100 q + i (s = size index, q = rho index, i = 0..4); supplies,
  demands and costs from `default_rng(seed)`, fixed charges from `default_rng([seed, 1])` (decision).
* Reference: MIP in HiGHS (x_ij <= M_ij y_ij, M_ij = min(a_i, b_j), y binary), one thread per process, time
  limit 60 s, relative gap 0 and absolute gap 0.99 (integer data: an absolute gap below 1 proves the
  optimum). Recorded: status, value, best lower bound, MIP gap, time. The gap of a method is
  100 (Z - Z_best) / Z_best with Z_best = the optimum when it is proved, otherwise the best known value (the
  minimum of the MIP solution and of every run of every method). The gap of Z_best to the lower bound is
  reported separately.
* Methods: (1) Balinski: LP with costs c_ij + f_ij / M_ij, then the true cost of its plan; (2) VAM on the
  same linearised costs, true cost of its plan; (3) RS; (4) GA-rand-tuned (`swap_scaled`); (5) GA-rand-cycle;
  (6) GA-cost-cycle, cost-aware start built from the linearised costs; (7) SA-rand-tuned; (8) GA-hybrid =
  GA-cost-cycle plus a local search by pivots: after every 10th generation the best individual of the
  population is decoded (counted as one call, decision), its non-basic arcs are scanned in index order from
  a random start, every neighbour (one pivot) is evaluated by the true FCTP cost and counts as one call, and
  the first strictly better neighbour replaces the individual; one such step per application (decision).
  All stochastic methods minimise the true FCTP cost with the same decoder.
* Parameters come from the linear tuning (`experiments/tuned-v2.yaml`) and the k of 8.2, without any tuning
  on FCTP. This is a limitation and is reported as such. Known consequence, stated before the run: with the
  population of 2700 of GA-cost the budget 200 m n gives 6 generations at 10x10, 15 at 15x15, 28 at 20x20 and
  65 at 30x30, so the local search of GA-hybrid is applied 0, 1, 2 and 6 times; at 10x10 GA-hybrid and
  GA-cost-cycle are the same algorithm.
* 10 runs per instance (seeds 20261116 + r), budget 200 m n evaluations.

**8.5 External benchmark.** At most 10 minutes of search for a public FCTP set with published optimal
values. If a set with a stable link and known optima is found, the methods of 8.4 are run on its instances
up to 30x30 with the same rules and the source is cited. If not, this part is left out and the report says
so.

**8.6 Statistics.** As in section 5: the unit is the instance (median over its 10 seeds); two-sided
Wilcoxon signed-rank test, Holm correction, matched-pairs rank-biserial r, wins/ties/losses.

* Linear problem, per (set, size), one Holm family of five pairs: GA-rand-cycle against VAM, GA-rand-tuned
  and GA-cost-tuned; GA-cost-cycle against GA-cost-tuned and VAM. On gap; the normalised gap is reported for
  every method. With 5 instances (reduced 100x100) the smallest possible two-sided p is 0.0625; this is
  stated next to the result.
* FCTP, one Holm family of four pairs: GA-hybrid and GA-rand-cycle, each against Balinski and against
  GA-rand-tuned. A cell (size, rho) has 5 instances, so the tests are made on the 40 instances together and
  for each rho (20 instances) (decision); per cell only the median gap and wins/ties/losses are given.
* No result of this amendment is used to choose anything in the v0.4 plan.

### Record of amendment 8 (2026-11-19): what the rules gave and what differs from the text above

Written after the runs, from the files of `paper_artifacts_v3/`. Order of the commits: 7aa163b (amendment 8),
ab93a13 (code, tests, configurations; no run), the runs of 8.2 and 8.3, 01f5af2 (see "Stop of the MIP phase"),
the runs of 8.4 and 8.5. `paper_artifacts_v3/run_manifest.json` gives the commit of every command; the
working tree was clean at each of them.

* 8.2, choice of k (`kselect/selected.json`, `kselect/kselect.csv`): probe times 9.6 s and 12.1 s, estimate
  60 s against the limit of 480 s, so all 8 training instances were used; the grid took 79 s. Chosen:
  GA-rand-cycle k = 2 (mean normalised gap 0.0102; k = 1: 0.0213, k = 4: 0.0180, round(0.05 (m + n)): 0.0164),
  GA-cost-cycle k = 1 (0.00375; k = 2: 0.00385, k = 4: 0.00667, round(0.05 (m + n)): 0.00637). No tie.
  The training instances have the SHA-256, the seeds and the Z_rand of `paper_artifacts_v2/instances_train`.
* 8.3, pilot and reduction (`linear/pilot.json`): 49 pilot runs, estimate 3132 s (52.2 min) against the limit
  of 30 min, so the 100x100 set is `v3u100x100-00..04` (5 instances). The estimate after the rule was 28.5 min;
  the run took 47.0 min (4615 records with the pilot runs, no failed run). At 100x100 a test has 5 pairs and
  its smallest possible two-sided p is 0.0625, so no comparison at that size can pass the Holm correction.
* Check of the protocol: the 3060 runs that this protocol shares with `paper_artifacts_quick/` (same
  instance, method and seed: VAM, RS and the four tuned methods up to 50x50 and structured 20x20) have the
  same cost, the same Z* and the same Z_rand in both sets of records.
* Stop of the MIP phase (8.4). The first start of the FCTP configuration stopped in the MIP phase: on
  `f10x10-r1-00` and `f10x10-r1-02` HiGHS returned amounts 1e-7 away from a vertex and the feasibility check
  of the runner (tolerance 1e-9) refused the plan. No FCTP method had been run. Commit 01f5af2 rounds the MIP
  plan when supplies and demands are integer and the rounded plan satisfies the constraints exactly, and
  checks the MIP plan with the tolerance of the solver. The 38 MIP records written before the stop were set
  aside and all 40 MIP runs were made again; that failed start is not in `run_manifest.json`. No method,
  parameter, budget, seed or rule was changed.
* 8.4, MIP reference (`fctp/tables/F1_mip_summary`): the optimum was proved for all 30 instances of 10x10,
  15x15 and 20x20; all 10 instances of 30x30 reached the limit of 60 s with a MIP gap of 1.8 % (rho = 1) and
  2.4 % (rho = 0.2) in the median, at most 3.4 %. On every 30x30 instance the best known value is the MIP
  solution, not a heuristic run.
* 8.4, GA-hybrid: the local search was applied 0, 1, 2 and 6 times per run at 10x10, 15x15, 20x20 and 30x30,
  as stated in advance, and improved the best individual in 0.8, 1.6 and 3.0 of those applications on
  average (`fctp/tables/F2_gap`). The median gap over runs of GA-hybrid and of GA-cost-cycle differs by at
  most 0.25 percentage points in every cell (the median of instance medians by at most 1.1, in either
  direction); the comparisons of GA-hybrid in `F3_tests` are therefore in effect comparisons of GA-cost-cycle.
  At 5x5 of the linear protocol the budget of 5000 calls is below one generation of the population of 2700,
  so GA-cost-tuned and GA-cost-cycle are both the cost-aware start and give identical results there.
* 8.5, external benchmark: found. MIPLIB 2017 (https://miplib.zib.de) has three pure fixed-charge
  transportation problems up to 30x30: `gr4x6` (4x6), `ran13x13`, `ran12x21`, with the objective values
  202.35, 3252 and 3664 listed on their pages (status "easy"). The other `ran*` instances of older MIPLIB
  versions are not in MIPLIB 2017 and were not looked for elsewhere; `ran14x18-disj-8` has additional
  constraints and is left out. Decisions made when the set was found: the reference is the listed value;
  our MIP is also run (it proves the same three values); `gr4x6` has non-integer costs, so the MIP of this
  part uses an absolute gap of 1e-6 instead of 0.99. Three instances: no test.
* 8.1, item 6: `scripts/neutrality_check.py` is the script of the branch `main` with the second measurement
  added (`--operators`); its first measurement is unchanged. Because the two variants got different k, the
  cycle mutation is measured with k = 2 and with k = 1.
* Finding that limits 8.1: on random parents 2 to 10 % of the pivots have theta = 0, but inside the GA runs
  the share is 1.6 to 74 % and grows with the size (`linear/tables/T4_cycle_counters`: at 100x100, 74 % of the
  pivots of GA-rand-cycle and 65 % of those of GA-cost-cycle; 56 % and 65 % of the offspring keep the decoded
  plan). The cycle mutation removes the neutrality of the swap on non-degenerate plans, not on the
  degenerate plans that the search produces.

### Amendment 9 (2026-11-19, 14:15 +05:00): extension of experiment v3 after its results were seen

Written and committed before any code of this amendment and before any run of it. Everything below was
decided **after** the results of amendment 8 were read (`paper_artifacts_v3/` at commit 923773b), in answer to
four limits of those results: (1) on every FCTP instance up to 30x30 the MIP solver with 60 s gives a plan at
least as good as any heuristic run; (2) the 100x100 set has 5 instances, so no test there can pass;
(3) nothing was tuned on FCTP; (4) the local search of GA-hybrid is applied 0 to 6 times per run. None of
this is confirmatory. The fifth limit (pivots with theta = 0 inside the GA runs) is not addressed: no operator
is changed by this amendment. Results stay in `paper_artifacts_v3/`; the raw records and the tables of
amendment 8 are not rewritten, except the linear tables named in 9.1. Decisions are marked "(decision)".

**9.1 Linear problem: the 100x100 set with all 10 instances.** The five instances `v3u100x100-05..09` that
the reduction rule of 8.3 left out are run with the methods, seeds, budget and reference of 8.3. The
instances were fixed by 8.3 (seeds 20290005..20290009); nothing is chosen. The record of 8.3 stands: the
rule gave 5 instances; this run is made because the time is now accepted.

* The linear tables are rebuilt with 10 instances at 100x100. The tests at 100x100 are given three times in
  a separate table: on the first five instances (the plan of 8.3 after its rule, as already reported), on the
  five new instances alone (not seen when this amendment was written; 5 pairs, smallest possible two-sided
  p = 0.0625, so wins/ties/losses and medians are what can be read), and on all ten (smallest possible
  p = 0.002; the same Holm family of five pairs as in 8.6). The test on ten instances includes five that
  had been seen; this is stated next to it.
* Expected time: about 45 minutes with 20 runs at once.

**9.2 FCTP: a small grid on training instances for the cost-aware variant and its local search.**

* Training instances: generator of 8.4, sizes 20x20 and 30x30, rho in {0.2, 1.0}, 2 instances per
  (size, rho), 8 in all, seeds 20310000 + 1000 s + 100 q + i (s = 0 for 20x20, 1 for 30x30; q = rho index;
  i = 0, 1); ids `t<m>x<n>-r<rho>-<i>`. They are not test instances. Reference of a training instance: the
  MIP of 8.4 (60 s); the training gap is 100 (Z - Z_ref) / Z_ref with Z_ref the smaller of the MIP solution
  and the best run of the grid.
* Grid (decision): population P in {2700, 900, 300, 100}, pivots k in {1, 2, 4}, local search after every
  g-th generation with g in {0 (none), 10, 3, 1}; 48 configurations. Everything else as in GA-cost-cycle
  (cost-aware start from the linearised costs, crossover rate, tournament 8, elite 5 of GA-cost in
  `experiments/tuned-v2.yaml`). Seeds r = 0, 1, 2, budget 200 m n, budget-only stop; the local search is
  that of 8.4 without change (its decoding and every neighbour are counted).
* Rule: **GA-cost-cycle-ft** is the configuration with g = 0 that has the smallest mean training gap over
  the 8 instances and 3 seeds; **GA-hybrid-ft** is the configuration with g > 0 that has the smallest mean
  training gap. Ties: the earlier configuration in the order P = 2700, 900, 300, 100, then k = 1, 2, 4, then
  g = 10, 3, 1 (the one closest to the configuration of 8.4).
* Test: both variants on the 40 instances of 8.4, seeds 20261116 + r, r = 0..9, budget 200 m n. Z_best of
  an instance follows the rule of 8.4 and now includes these runs; if a new run is below the MIP solution of
  an instance without a proved optimum, the gaps of all methods on that instance change and this is reported.
* One Holm family of three pairs, on the 40 instances and for each rho (as in 8.6): GA-cost-cycle-ft against
  GA-cost-cycle (does the grid on FCTP help); GA-hybrid-ft against GA-cost-cycle-ft (does the local search
  help when it is applied often); GA-hybrid-ft against GA-hybrid.
* Limits stated in advance: only P, k and g of one variant are chosen, on a grid, not by a full tuning; the
  other methods are not tuned on FCTP, so no test compares the `-ft` variants with them. If the rule returns
  the configuration of 8.4 (P = 2700, k = 1) for g = 0, GA-cost-cycle-ft is GA-cost-cycle and the first pair
  is reported as identical.

**9.3 FCTP: the MIP solver with the time of the GA.** For every instance i, T_i is the median run time of
GA-cost-cycle (the variant of 8.4) over its 10 runs on that instance, as recorded (20 runs at once). The MIP
of 8.4 (one thread, same options) is run with the time limit T_i and, on the 40 instances of 8.4, also with
10 T_i (decision), with 20 runs at once. Recorded: status, whether a plan was found, its cost, the bound, the
time actually used. Reported per (size, rho): the number of instances where the MIP has no plan at the
limit, and where its plan is better than, equal to or worse than the median cost of GA-cost-cycle over the
seeds (no plan counts as worse); the gap of the MIP plan to Z_best. No test is made: the comparison depends
on the machine, on the load and on two different kinds of code (Numba kernels, a compiled solver), and is
descriptive.

**9.4 FCTP: sizes above 30x30.** Generator and seed rule of 8.4 continued (decision): sizes 50x50 (size
index s = 4) and 70x70 (s = 5), rho in {0.2, 1.0}, 5 instances per (size, rho), 20 in all, seeds
20300000 + 1000 s + 100 q + i; ids `f50x50-...`, `f70x70-...`.

* Methods: MIP of 8.4 with 60 s; MIP with the limit T_i of 9.3; Balinski; VAM-lin; GA-cost-cycle
  (parameters of 8.4); GA-cost-cycle-ft and GA-hybrid-ft (parameters of 9.2). 10 runs per instance, budget
  200 m n. RS, SA and the GA with a random start are left out to keep the time (decision).
* Z_best and gap as in 8.4. One Holm family of three pairs: GA-cost-cycle, GA-cost-cycle-ft and GA-hybrid-ft,
  each against the MIP with 60 s, on the cost; unit: the instance (median over the seeds against the one MIP
  value); on the 20 instances and for each size (10 instances). An instance where the MIP has no plan at
  60 s is counted as a win of the GA and is left out of the Wilcoxon test.
* Expected time: about 20 minutes (a 70x70 run about 45 s). No reduction rule: the run is made whatever the
  time.
* The outcome is open: the MIP solution may stay better at these sizes as well. It is reported either way.

**9.5 Order and records.** Order: this amendment; the code of 9.1; the run of 9.1; the code of 9.2-9.4; the
grid of 9.2; the test runs of 9.2; the runs of 9.4; the runs of 9.3. Every command is written to
`paper_artifacts_v3/run_manifest.json` with the commit of the code. The state of the code is taken when a
command starts and the output directory is not counted as a change, because the commands themselves append
to tracked files there.

**9.6 Corrections made with the code, before any run of 9.2-9.4 (2026-11-19, 14:25 +05:00).** The run of
9.1 was in progress and no result of it had been read.

* 9.4, test against the MIP: made on the gap to Z_best in percent, not on the raw cost. The two values of a
  pair are divided by the same Z_best, so wins, ties and losses are those of the cost; the ranks of the
  Wilcoxon test are then not dominated by the 70x70 instances, whose costs are larger.
* Z_best of an instance (9.2, 9.4) is the smallest value among the MIP solution with 60 s, every run of
  every method and the MIP plans of 9.3; a proved optimum stays the reference.
* 9.3: the comparison with the MIP at 60 s is added to the same table from the records that already exist
  (no new run), next to the limits T_i and 10 T_i.
* A MIP run that ends before the root relaxation has no lower bound; it is recorded as no bound.
* Configuration: `experiments/paper-v3-fctp-ext.yaml`; commands `tune`, `run`, `report`; tables `E1` to `E7`
  and the figure `fctp_gap_sizes` in `paper_artifacts_v3/fctp/`.

### Record of amendment 9 (2026-11-19): what the runs gave

Written after the runs, from the files of `paper_artifacts_v3/`. Order of the commits: 8faa6e6 (amendment 9),
8db4537 (code of 9.1), the run of 9.1, 4ff8499 (code of 9.2-9.4 and the corrections 9.6, committed while the
run of 9.1 was in progress), the grid of 9.2, the runs of 9.2, 9.4 and 9.3, the reports, 3a3cf0b (the new
figure only: its shared axis cut off the largest values; no table changed), the report again.
`run_manifest.json` gives the commit of every command; the code was unchanged at the start of each. No run
failed. Total run time 57 minutes (9.1: 42.8 min; grid 2.2 min; 9.2-9.4: 11.9 min).

* 9.1 (`linear/tables/T2_tests_extension`, `T1_gap`). 355 new runs; the 4615 earlier records are unchanged.
  On the five added instances alone every pair has the direction it had on the first five (GA-rand-cycle
  against VAM 5 wins of 5 where the first five gave 3 of 5). On all ten instances the five pairs pass the Holm
  correction: GA-cost-cycle below GA-cost-tuned and below VAM on 10 of 10 (p_Holm = 0.0098), GA-rand-cycle
  below GA-rand-tuned on 10 of 10 (0.0098) and below VAM on 8 of 10 (0.014), GA-rand-cycle above GA-cost-tuned
  on 10 of 10 (0.0098; the cycle mutation with a random start loses to the tuned GA with the cost-aware
  start). Median gap over runs at 100x100: GA-cost-cycle 14.0 %, GA-cost-tuned 20.5 %, GA-rand-cycle 34.3 %,
  VAM 41.7 % (with five instances: 10.3, 18.3, 30.4, 36.1). The share of pivots with theta = 0 is 66 % and
  75 %, as before.
* 9.2, grid (`fctp/tables/E1_tuning`): the MIP proved the optimum on 5 of the 8 training instances. Chosen
  without the local search: P = 300, k = 2 (mean training gap 5.57 %; the configuration of 8.4, P = 2700,
  k = 1: 5.96 %). Chosen with the local search: P = 300, k = 2, every 3rd generation (5.66 %). The 48 means
  lie between 5.57 % and 8.55 %. No tie.
* 9.2, test on the 40 instances (`E2_gap_tuned`, `E3_tests_tuned`): none of the three comparisons is
  significant. GA-cost-cycle-ft against GA-cost-cycle: 19 wins, 3 ties, 18 losses, p = 0.72. GA-hybrid-ft
  against GA-cost-cycle-ft: 11, 11, 18, p = 0.72. GA-hybrid-ft against GA-hybrid: 20, 4, 16, p = 0.41. The
  chosen population helps at 10x10 (median gap 0 instead of 0.8 % and 1.1 %; 66 generations instead of 6) and
  not from 15x15 on. The local search of GA-hybrid-ft is applied 20, 42, 66 and 110 times per run at 10x10 to
  30x30 and takes up to 45 % of the budget at 30x30; it does not lower the gap. The answer to limits (3) and
  (4) is therefore negative: a grid on FCTP and a local search that is applied often do not change the
  result of 8.4.
* Z_best was lowered on one instance, `f30x30-r1-03`: the MIP run with the limit 10 T (16 s) returned 55455,
  below the 55569 of the MIP run with 60 s. HiGHS under a time limit does not repeat the same search, so a
  shorter run can end with a better plan. No heuristic run is below a MIP plan on any instance.
* 9.3 (`E4_mip_equal_time`), 40 instances of 8.4: with the limit T (0.07 s at 10x10 to 1.6 s at 30x30) the
  MIP has a plan on every instance; the median GA-cost-cycle cost is lower on 38 instances and equal on 2
  (both 10x10); the median gap of the MIP plan is 2.2 to 20.9 % against 0.8 to 7.3 % of the GA. At 15x15 to
  30x30 with rho = 0.2 the MIP plan at T has the gap of the Balinski plan. With 10 T the MIP is better on 34,
  equal on 3, worse on 3; with 60 s better on 37 and equal on 3.
* 9.4 (`E5_large_mip`, `E6_large_gap`, `E7_large_tests`): at 50x50 and 70x70 the MIP proves no optimum in
  60 s (MIP gap 4.4 to 7.4 % in the median) and has a plan on all 20 instances. Its plan is better than the
  median of every GA variant on 20 of 20 (p_Holm < 0.001; per size 10 of 10, p_Holm = 0.006). Median gap to
  the MIP plan: GA-cost-cycle 7.8 to 11.1 %, GA-cost-cycle-ft 6.6 to 9.3 %, GA-hybrid-ft 8.2 to 11.9 %,
  Balinski 16.0 to 19.2 %. With the limit T (11 s at 50x50, 40 s at 70x70) the MIP is better than
  GA-cost-cycle on 19 of 20 instances. Limit (1) therefore stands and is wider than stated: the GA is ahead
  of the MIP solver only at the same short time up to 30x30 (at most 1.8 s); from 50x50 on the MIP solver
  is ahead at the same time as well.
* Not planned and noticed in the records: GA-hybrid-ft runs 3 to 6 times shorter than GA-cost-cycle-ft at
  50x50 and 70x70 (3.1 s against 10.5 s; 7 s against 39 s) because 70 % and 82 % of its budget are local-search
  neighbours, which cost less time than a decoder call. The budget counts evaluations, not time.

### Amendment 10 (2026-11-20, 01:30 +05:00): answers to a review - rivals on FCTP, MIP in its usual setting, more instance classes, one measure of effort, degenerate pivots, more statistics

Written and committed before any code of this amendment and before any run of it. **It is written after the
results of amendments 8 and 9 were read** (`paper_artifacts_v3/` at commit aa743c1), in answer to the remarks
of a review of the article draft (numbers of the remarks in brackets). **Every result of this amendment is
exploratory; nothing here is confirmatory.** The raw records and the tables of amendments 8 and 9 are not
rewritten. New files go to `paper_artifacts_v3/review/`. Decisions are marked "(decision)". Configuration:
`experiments/paper-v3-review.yaml`; commands `python -m tpga.experiments.v3 <command> --config` that file.

**10.0 Time limit and the reduction rules.** The sum of the wall-clock times of all run commands of this
amendment (pilot included, report excluded) is at most **90 minutes**. The commands run in the order of the
table; each has an allowance. Before a command starts, the time already used is read from
`review/budget.json`; its allowance is cut to `90 min - used` when that is smaller.

| order | command | content | allowance | at once |
|---|---|---|---|---|
| 1 | `pilot` | times of single runs, used only for the estimates below | 2 min | 20 |
| 2 | `tune` | grids of Tabu and ILS on the 8 training instances of 9.2 | 2 min | 20 |
| 3 | `rivals` | Tabu and ILS on the 60 FCTP instances of 8.4 and 9.4 | 3 min | 20 |
| 4 | `generator` | new instance classes: MIP reference and the methods | 11 min | 20 |
| 5 | `degenerate` | share of pivots with theta > 0 by generation; the second rule for the entering arc | 15 min | 20 |
| 6 | `public` | public instance sets, if the search of 10.3 finds any | 5 min | 20 |
| 7 | `timing` | times on one processor, one run at a time | 10 min | 1 |
| 8 | `mipdefault` | MIP with all threads and 300 s | 36 min | 1 |

The allowances sum to 84 minutes. The pilot runs, with at most 20 at once: Tabu and ILS with the first entry of
their grids and GA-cost-cycle, seed `base_seed`, on four pilot FCTP instances (20x20, 30x30, 50x50, 70x70,
rho = 1, generator of 8.4, seeds 20340000 + 1000 s; they are used for nothing else), and GA-rand-cycle and
GA-cost-cycle with both rules for the entering arc (10.5) on the training instance `u50x50-00-train` of 8.2.
Only the times of the pilot runs are used. The estimate of a command with 20 runs at once is
`1.25 * (sum of the estimated times of its runs) / 20`, plus the longest estimated run for the command
`degenerate`. The estimated time of a run is the pilot time of its method at its size (sizes below 20x20 use
the time at 20x20; 50x50 serves for sizes up to 50x50 that the pilot does not have); a MIP run of the
reference counts with its limit (60 s); a linear run with the present mutation counts with the median time of
the same method and size in the records of amendments 8 and 9; a linear run with the second rule counts with
that median times the ratio (pilot time with the second rule) / (pilot time with the present rule) of its
method. When the estimate is above the allowance, **the number of instances is reduced, never the seeds, the
budget or the limits** (decision):

* `rivals`: the cells 70x70, then also 50x50, use their first k instances, k the largest of 5, 3, 2, 1 that
  fits.
* `generator`: every new cell uses its first k instances, k the largest of 5, 4, 3, 2, 1 that fits.
* `degenerate`: the group 100x100 of the comparison of 10.5 b uses its first k instances, k the largest of
  10, 5, 3, 2, 1, 0 that fits; the other groups keep their 10 instances. If k = 0 does not fit, the runs of
  10.5 a at 100x100 use 2 instances, then 1.
* `public`: the instances are taken in the order (size, name) while they fit.
* `timing` is run in rounds; round q (q = 0, 1, 2) is instance q of every cell with all its runs. A round
  starts only if its estimate (pilot times, factor 1.15) fits in what is left of the allowance. If round 0
  does not fit, the largest size is left out, then the next, until it fits.
* `mipdefault` runs one instance at a time in this order: first the instances whose reference run of 8.4
  proved the optimum (by size, rho, index), then the others in rounds, round q = instance q of every cell
  (by size, then rho). A run starts only if what is left of the allowance is at least its time limit.
  Instances that were not started are listed as "not run (time rule)". The command takes `--minutes N`: a
  later start with more time continues the same order and completes the plan of 60 instances; whatever is
  added that way is reported as added after this amendment.

A cell with fewer instances is reported with its number of instances; a test uses the instances that both
methods have. What each rule gave is written in the record of this amendment.

**10.1 Rivals for FCTP (remark 6).** Two local-search methods work on the basic plan (a spanning tree of
m + n - 1 arcs) with the true FCTP cost. Both start from the plan of Balinski's linearisation (the plan of
the method `Balinski` of 8.4), completed to a spanning tree with zero arcs in index order. A *neighbour* of a
plan is the plan after one pivot: a non-basic arc enters, theta is moved along its cycle, the first arc on a
minus position with the smallest amount leaves. A *neighbour evaluation* computes theta and the change of the
true cost (variable cost and fixed charges) of one neighbour, without building the plan. Budget: the cost of
the start plan counts as one evaluation and every neighbour evaluation as one, the sum is
B = 200 m n as for the GA; both counters are recorded separately. The result of a run is the best plan met.

a) **Tabu** (tabu search over basis pivots). In every iteration a set of candidate non-basic arcs is
evaluated: all N' = m n - (m + n - 1) of them (phi = 1), or s = max(1, round(phi N')) arcs drawn uniformly
with replacement (phi < 1). A candidate is tabu when its entering arc or its leaving arc is on the tabu list;
an arc that entered or left the basis stays on the list for the next T iterations. Aspiration: a tabu
candidate is admitted when it gives a cost below the best cost found so far. The admitted candidate with
the smallest change is applied, also when the change is zero or positive (the first one met on ties); with no
admitted candidate the iteration makes no move. Grid: phi in {1, 0.25, 0.05} x T in {5, 10, 20}.

b) **ILS** (iterated local search). Descent: the non-basic arcs are scanned in index order, cyclically from a
random start; the first neighbour with a lower cost is applied and the scan goes on from the next position of the
list of non-basic arcs; the
descent ends when N' neighbours in a row give no improvement. Perturbation: p pivots whose entering arcs are
drawn uniformly among the non-basic arcs (the pivot of the cycle mutation); each counts as one neighbour
evaluation. Acceptance after the next descent: `better` - the search goes on from the new local optimum if
its cost is not above the cost of the previous one, otherwise it returns to the previous one; `always` - it
goes on from the new one. Grid: p in {2, 4, 8, 16} x acceptance in {better, always}.

* Parameters: each grid is run on the 8 training instances of 9.2 with 3 seeds (`base_seed + r`), with the
  rule of 9.2: the smallest mean gap to the training Z_best (the MIP value of 9.2, or a smaller value found
  by a run of the grid of 9.2 or of these two grids); ties go to the earlier grid entry (order of the lists above, the first list
  outermost). The chosen configurations are fixed before the test instances are run.
* Test: Tabu and ILS, 10 seeds each, on the 40 instances of 8.4 and the 20 instances of 9.4.
  Gap = 100 (Z - Z_best) / Z_best with Z_best of this amendment: the proved optimum if a MIP run proved one,
  otherwise the smallest cost over all MIP runs and all heuristic runs on disk, including the runs of this
  amendment. The tables of amendments 8 and 9 keep their Z_best; the instances where Z_best becomes smaller
  are listed. Pairs: [GA-cost-cycle, Tabu], [GA-cost-cycle, ILS]; unit = instance, median over the seeds;
  two-sided Wilcoxon test, Holm over the two pairs within a scope; scopes: all 60 instances, each rho, each
  size. Reported with wins/ties/losses, the Hodges-Lehmann shift with its 95 % interval and the
  rank-biserial r.
* Tabu is **not a reproduction** of the tabu search of Sun, Aronson, McKeown and Drinka (EJOR 106, 1998,
  441-456), and ILS is not the method of Buson, Roberti and Toth (Operations Research 62, 2014). What is
  known to differ is written in 10.1 c below.

c) What is known about the published methods. The full text of Sun et al. (1998) is closed and no open copy
was found (search of 2026-11-20), so its rules (tenures, memory structures, candidate lists, stopping rule,
parameter values) are not known to this work and none of them is copied. Our Tabu has a short tabu list and an
aspiration rule only: no intermediate-term or long-term memory, no restarts, a random candidate sample, its own
grid for two parameters and a budget in evaluations instead of time. The paper of Buson, Roberti and Toth is
closed as well; our ILS uses no reduced costs and no other LP information after the start plan. If the plan of
the linearisation were not basic (its positive cells contain a cycle), the run stops with an error; on the 68
existing FCTP instances it is basic (checked before this amendment with the existing code, no new run of a
method).

**10.2 MIP in its usual setting (remark 7).** The model of 8.4 (x_ij <= M_ij y_ij with
M_ij = min(a_i, b_j)) is solved again by HiGHS with `threads = 0` (the solver's automatic choice: all
processors of the machine are offered), a limit of 300 s, and the other options as in 8.4 (relative gap 0,
absolute gap 0.99, so that "optimal" means a proved optimum for integer data in both settings; this is the
only change from the defaults of the solver). One run per instance, one at a time, nothing else running;
each run in a fresh process. Planned for all 60 FCTP instances; the rule of 10.0 decides how many are run.
Recorded: status, cost, bound, gap, wall time, processor time of the process (it shows how much the solver
really ran in parallel), nodes. The table gives the same instances in both settings: 1 thread and 60 s (the
records of 8.4 and 9.4, made with 20 runs at once) and all threads and 300 s.

**10.3 Instance sets (remarks 8 and 17).**

a) Public sets. A search of at most 15 minutes for public FCTP instance sets with published values (Sun et
al.; Buson, Roberti, Toth; Roberti, Bartolini, Mingozzi; others). The MIPLIB instances of 8.5 are already
used. Result of the search (9 minutes, 2026-11-20, before any code):

* Found with a link: the subset of the test problems of Sun et al. (1998) that Glover, Amini and Kochenberger
  (Journal of Heuristics 11, 2005, 307-336) used, as 132 files `N*.FCTP` in the third-party repository
  https://github.com/Tybirk/RL-FCTP (directory `Java/Glover`, commit
  1ab1ba073363c7b650fab7ef1f93b8a7755ba2cb of 2020-11-26). The repository states no licence and the original
  source of the files could not be confirmed. Ten instances have m, n <= 70: N104, N107 (10x10), N204, N207
  (15x15), N304, N307 (10x20), N504, N507 (10x30), N1004, N1007 (50x50). Published values: Table 3 of Glover
  et al. (2005) (author copy: https://leeds-faculty.colorado.edu/glover/fred%20pubs/354%20-%20parametric%20ghost%20image%20fixed%20charge%20%28GIP%29.pdf)
  with the columns CPLEX 9.0, tabu search of Sun et al. and parametric ghost image process. Barr et al.
  (Networks, 2021, Table 2) list values that are 3 to 5 units lower for seven of the eight small instances and
  247 lower for N504; the cause is not known to us. The values of Glover et al. are used and the difference is
  reported.
* Not found with a public link: the sets of Agarwal and Aneja (2012), of Roberti, Bartolini and Mingozzi
  (2015) and of Buson, Roberti and Toth (2014). Found without published values and therefore not used:
  https://github.com/gjleroux/PhD (150 instances).
* Rule (decision): the ten instances are run. Because no licence is stated, the files are not copied into
  this repository: the command `public` downloads them from the commit named above, checks the SHA-256 values
  written in the configuration before the first run, and keeps them in a directory that git ignores. The data
  are used as they are (line 1: m n; supplies; demands; m lines of costs; m lines of fixed charges).
  Reference: the MIP of 8.4 (1 thread, 60 s). Methods: Balinski, Tabu, ILS, GA-cost-cycle, 10 seeds,
  B = 200 m n. Reported for every instance: the three published values, the MIP result and its status, the
  median and the best cost of every method, and the gap to Z_ref = the optimum proved by our MIP, otherwise
  the smallest of the published values and of all our values.

b) Generator. New cells with the sizes 20x20, 30x30, 50x50 and 5 instances per cell:

* class `uniform` (generator of 8.4) with rho = 0.05 and rho = 5: seed = 20320000 + 1000 s + 100 q + i
  (s = 0, 1, 2 for the sizes, q = 0 for rho = 0.05, q = 1 for rho = 5); ids `g<m>x<n>-r<rho>-<i>`. The
  cells of this class with rho = 0.2 and rho = 1 are the instances of 8.4 and 9.4 at these sizes.
* class `concentrated` (few large suppliers, many small customers) with rho in {0.05, 0.2, 1, 5}:
  S = 60 m; h = max(2, round(0.1 m)) large suppliers share round(0.8 S), the other m - h suppliers share the
  rest, each group by `1 + multinomial(amount - group size, equal shares)`; demands
  `1 + multinomial(S - n, equal shares)`; costs U{1..100}; all from `default_rng(seed)` in this order (large
  suppliers, small suppliers, demands, costs); fixed charges as in 8.4 (U{1..F},
  F = round(2 rho c_mean S / (m + n - 1)), from `default_rng([seed, 1])`);
  seed = 20330000 + 1000 s + 100 q + i (q = 0..3 in the order of the list); ids `c<m>x<n>-r<rho>-<i>`.

Reference: the MIP of 8.4 (1 thread, 60 s). Methods: Balinski, Tabu, ILS (chosen configurations of 10.1) and
GA-cost-cycle of 8.4, 10 seeds, B = 200 m n. Reported: median gap to Z_best by class, rho and size, with
the pairs of 10.1 in the scopes: each class with each rho. Nothing is tuned on these instances.

**10.4 One measure of effort (remark 13).** The budget stays in evaluations. Next to it the time is
measured with one run at a time, the process bound to one logical processor (number 2; the affinity of the
process is set, no system setting is changed) and no other run of the experiment active; other activity of
the machine is not controlled. Subsample: the first 3 instances of each of the 12 cells of 8.4 and 9.4
(size x rho), 5 seeds (`base_seed + r`, r = 0..4); methods GA-cost-cycle, Tabu, ILS; then one MIP run
(1 thread) per instance whose limit is the median time of the 5 GA-cost-cycle runs of this block on that
instance. Reported by cell: median time of each method, decoder calls, neighbour evaluations (a separate
counter, as in 10.1), the limit and the result of the MIP run, and how each method stands against that MIP
plan.

**10.5 Degenerate pivots (remark 14).**

a) GA-rand-cycle and GA-cost-cycle of 8.3 are run again with a record, for every generation, of the number
of pivots and of pivots with theta = 0: the first 3 instances of the uniform sets 20x20, 50x50 and 100x100,
seeds `base_seed + r`, r = 0..4. The runs repeat runs of amendments 8 and 9 (same seeds); their costs must
be equal to the recorded ones, which is checked. Reported: share of pivots with theta > 0 in each tenth of
the budget (median over the runs of a size, with the smallest and the largest value), and a figure.

b) A second rule for the entering arc (`entering: nondegenerate`): the entering arc is drawn uniformly among
the non-basic arcs whose cycle has no basic arc with zero amount on a minus position (then theta > 0); when
there is no such arc, the present rule is used (uniform among all non-basic arcs). The same uniform number
chooses the arc under both rules, so the random numbers of a run are used in the same way. The present
operator is not changed. GA-rand-cycle-nd and GA-cost-cycle-nd (the parameters and k of GA-rand-cycle and
GA-cost-cycle, nothing tuned again) are run on the linear set of 8.3 (all groups, 10 seeds, the seeds of
8.3) and compared with the recorded runs of GA-rand-cycle and GA-cost-cycle: gap to Z* in percent, unit =
instance, pairs [GA-rand-cycle-nd, GA-rand-cycle] and [GA-cost-cycle-nd, GA-cost-cycle], Holm over the two
pairs within a scope, scopes: every group, and all instances. Also reported: share of pivots with theta = 0,
how often the present rule had to be used, and the time. The runs of this point record the pivots by
generation as in a).

**10.6 Statistics (remarks 12 and 15).** No new runs. The test tables of amendments 8 and 9 are rebuilt by
their own reports with the interval of the Hodges-Lehmann shift as new columns; their other numbers must not
change, which is checked. For every paired comparison of experiment v3 (the
pairs of 8.6 for the linear problem with the scopes of 9.1, the pairs of 8.4, 9.2 and 9.4 for FCTP, and the
pairs of 10.1 and 10.5): wins/ties/losses, the Wilcoxon p and its Holm value as already reported, the
Hodges-Lehmann shift with its 95 % interval (Walsh averages, exact distribution; with too few pairs for the
level this is said) and the rank-biserial r. For every method in every cell (linear: set and size; FCTP:
size and rho; cells of 10.3 b): the median over the instances of the per-instance median gap, with a
bootstrap interval: 10 000 resamples of the instances of the cell with replacement, percentile interval
2.5 %-97.5 %, generator seed 20261120. Second normalisation for the linear problem:
(Z - Z*) / (Z_NWC - Z*) with Z_NWC the cost of the north-west corner plan, next to the normalisation of 8.3
with Z_rand; reported for every cell: the two medians of every method, the order of the methods under each,
and whether the order is the same.

**10.7 Figures (remark 22).** (1) Linear problem: median gap by size (uniform sets 5x5 to 100x100) for VAM,
GA-rand-tuned, GA-cost-tuned, GA-rand-cycle and GA-cost-cycle with the bootstrap intervals of 10.6.
(2) FCTP: gap to Z_best by size from 10x10 to 70x70, one panel per rho, for Balinski, Tabu, ILS,
GA-cost-cycle and the MIP with the time of the GA (the runs of 9.3 with the limit T), with the intervals.
(3) The figure of 10.5 a. JPG with 600 dpi and PDF, a serif font, English labels.

**10.8 Archive (remark 25).** After the results are committed: `.zenodo.json`, `CITATION.cff` with the
version `0.4.0-paper`, a workflow that builds a GitHub release for a tag `v*.*.*-paper` with one archive of
the tracked files of `paper_artifacts_v2/` (the raw records of the main run of v0.4 are not tracked and the
run is not finished, so they are not in it), `paper_artifacts_quick/` and `paper_artifacts_v3/`, and the tag
`v0.4.0-paper` on the final commit. Existing tags are not moved. No DOI is requested by this work.

**10.9 Corrections made with the code, before any run of this amendment (2026-11-20).**

* Time left unused passes on (10.0). With the fixed allowances the estimates made from the recorded times of
  amendments 8 and 9 (no new run) gave k = 0 for the 100x100 group of 10.5 b while the commands before it
  were expected to use less than half of their allowances, so that about 19 of the 90 minutes would stay
  unused. Rule now: a command may use the sum of the allowances of the table up to and including its own,
  minus the time already used. The last command (`mipdefault`) may go on until 88 minutes of total time
  (the limit minus a margin of 2 minutes for the start of processes and the writing of files). The limit of
  90 minutes, the order, the reduction rules and the allowances of the table do not change.
* The runs of 10.5 a and 10.5 b share one file (`review/raw/linear.jsonl`, phases `trace` and `nd`) and one
  pool of 20 processes, so that the processors are used all the time.
* Instances of the pilot have the prefix `p`. The pilot time at a size stands for every instance whose larger
  side is at most that size (this also covers the public instances 10x20 and 10x30).
* 10.4: before the first timed run each method is run once on the smallest instance without a record, so
  that the compilation of the kernels is not inside a measured time.
* 10.2: the processor time of a MIP run is that of its process (`cpu_s`), measured around the call of the
  solver together with the building of the model.

### Record of amendment 10 (2026-11-20): what the rules and the runs gave

Written after the runs, from the files of `paper_artifacts_v3/review/`. All of it is exploratory: amendment 10
was written after the results of amendments 8 and 9 were seen. Order of the commits: 855458e (amendment 10),
978c6f4 (code and the corrections 10.9), the commands `pilot`, `tune`, `rivals`, `generator` and `degenerate`,
858771a (code of the report only, committed while `degenerate` was running), the commands `public`, `timing`
and `mipdefault`, e9957da (three corrections of the report, listed below), the reports. No run failed.

**Time and the reduction rules** (`tables/R0_rules`, `budget.json`). All run commands together took 5046 s
(84.1 minutes) of the 90 minutes.

| command | allowance at its start, s | used, s | what the rule gave |
|---|---|---|---|
| `pilot` | 120 | 30.4 | 16 single runs |
| `tune` | 210 | 3.0 | both grids complete (408 runs) |
| `rivals` | 387 | 10.5 | estimate 31 s: 5 instances per cell at 70x70 and at 50x50 (1200 runs) |
| `generator` | 1036 | 358.8 | estimate 573 s: 5 instances per new cell (90 instances, 90 MIP runs, 2790 runs) |
| `degenerate` | 1577 | 694.7 | estimate 1057 s with **k = 0** at 100x100 for 10.5 b (the next larger k = 1 did not fit) and 3 instances at 100x100 for 10.5 a (1290 runs) |
| `public` | 1183 | 79.9 | all 10 instances |
| `timing` | 1703 | 1349.9 | all three rounds, no size left out (540 runs, 36 MIP runs) |
| `mipdefault` | 2753 | 2518.9 | **40 of the 60 instances run, 20 not run (time rule)** |

The second rule for the entering arc was 2.50 times (GA-cost-cycle) and 3.86 times (GA-rand-cycle) slower
than the present rule in the pilot at 50x50; this is what left the 100x100 group without the comparison of
10.5 b. The 20 instances of 10.2 that were not run are the instances 1 to 4 of 70x70 and 2 to 4 of 30x30 and
50x50 (both rho). `python -m tpga.experiments.v3 mipdefault --config experiments/paper-v3-review.yaml
--minutes 105` continues the same order and completes them; nothing of that kind has been run.

**What differs from the text of the amendment.**

* The pilot stores its times under the key "method|size". GA-cost-cycle at 50x50 was run twice in the pilot,
  on the FCTP pilot instance (7.58 s) and on the linear training instance (8.16 s), and the second value
  replaced the first. The ratio of the two rules of 10.5 uses the linear value, as written. The estimates of
  the FCTP runs at 50x50 used 8.16 s where 7.58 s was meant, so they were about 8 % too high for this method;
  every estimate was below its allowance with either value, so no decision of a rule depends on it. The code
  was not changed, so that the plans can be recomputed from the same files.
* `degenerate` started while the code of the report (`rev_report.py`, `report.py`, a test file) had
  uncommitted changes; `run_manifest.json` marks it `git_dirty`. The code that makes runs was that of
  978c6f4. The later commands started from 858771a with no uncommitted change.
* The report was corrected after the runs (e9957da): (1) in `R9_entering_rule` a cell in which no run makes a
  pivot gave a division by zero (GA-cost-cycle at 5x5: every run stops on its start plan, which is optimal);
  such a cell now has empty shares, and a cell without instances (100x100) is left out; (2) the numbers of
  `S1_pairs` are written as numbers; (3) the legend of the FCTP figure is below the panels. No raw record and
  no rule changed.
* 10.2: the rows "MIP, all threads, 300 s" of `R2_gap` and the columns of setting 2 of `R4_mip_summary` cover
  only the instances that were run (2 of 5 per cell at 30x30 and 50x50, 1 of 5 at 70x70).
* 10.4: the limit of a MIP run of the timing block is the median time of the five GA-cost-cycle runs of the
  same instance in that block (one processor), not the limit T of 9.3.
* Z_best of amendment 10 is smaller than the value used by the tables of amendments 8 and 9 on 22 of the 60
  instances (`R2_z_best_lowered`, by 0.02 to 2.6 %): 2 are optima proved by the MIP with all threads, 7 are
  its plans at the time limit, 13 are plans of ILS. The tables `F*` and `E*` keep their values. On the 10
  instances from 30x30 up that have a run with 300 s, that run gives Z_best on 9 and confirms the earlier
  value on 1; on the 20 that have no such run, ILS gives Z_best on 13. The gaps at 30x30 to 70x70 are
  therefore measured against a value that is weaker on the instances without the 300 s run, by an amount we
  do not know (where the run exists it lowered the value of the MIP with 60 s by 0 to 2.3 %).

**Results.**

* 10.1, grids (`R1_tuning`). Tabu: phi = 0.25, T = 5 (mean training gap 3.11 %; range of the grid 3.11 to
  9.26 %). ILS: p = 8, acceptance `better` (1.79 %; range 1.79 to 3.71 %).
* 10.1, test instances (`R2_gap`, `R3_tests`). Median over the instances of the median gap, by size
  (10 instances, both rho): GA-cost-cycle 0.96, 1.21, 2.79, 6.36, 10.95, 11.28 %; Tabu 0.82, 1.00, 1.25,
  1.87, 3.87, 3.96 %; ILS 0, 0, 0.33, 1.01, 1.80, 1.36 % (10x10 to 70x70). GA-cost-cycle against Tabu on the
  60 instances: 6 wins, 3 ties, 51 losses, p_Holm = 1.9e-9, r = 0.91, Hodges-Lehmann shift 3.40 points
  (95 % interval 2.39 to 4.34). Against ILS: 2, 3, 55, p_Holm = 1.3e-10, r = 0.99, shift 4.70 (3.41 to
  5.73). From 30x30 up, 80 of the 300 ILS runs (on 21 of the 30 instances) and 9 of the 300 Tabu runs (on 7
  instances) are below the plan of the MIP with one thread and 60 s. By rho the same direction (rho = 0.2:
  2/1/27 and 0/2/28; rho = 1: 4/2/24 and 2/1/27; all
  p_Holm < 0.001). By size: at 10x10 and 15x15 the GA is not separated from Tabu (3/2/5, p_Holm = 0.74;
  3/1/6, 0.43) and loses to ILS (0/2/8, p_Holm = 0.016; 2/1/7, 0.078); from 20x20 to 70x70 it loses to both
  on 10 of 10 instances of every size (p_Holm = 0.0039, the smallest value possible with 10 pairs and two
  tests), with shifts from 1.3 to 7.1 points against Tabu and 2.3 to 9.6 against ILS. Run time with 20 runs
  at once: Tabu and ILS 0.007 to 0.53 s, GA-cost-cycle 0.07 to 43 s. With the same budget of evaluations the
  two local searches are better than the GA and take 7 to 62 times less time (one processor, 10.4).
* 10.2 (`R4_mip_instances`, `R4_mip_summary`). One thread, 60 s (runs of 8.4 and 9.4): optimum proved on the
  30 instances up to 20x20 and on none of the 30 from 30x30 up (gap of the solver at the limit, median by
  cell: 1.8 to 7.4 %). All threads, 300 s: 40 instances run; optimum proved on the 30 up to 20x20 (median
  time 0.45 to 8.5 s by cell) and on 3 of the 4 run at 30x30 (50 to 149 s; the fourth stops with a gap of
  0.76 %); none of the 4 at 50x50 (gaps 1.9 to 3.0 %) and none of the 2 at 70x70 (3.8 and 5.0 %). Processor
  time over wall time 1.3 to 10.5 (median by cell 1.4 to 9.5). On the 10 instances run from 30x30 up the plan with 300 s is better than
  the plan with one thread and 60 s on 9 (by 0.12 to 2.3 %) and equal on 1.
* 10.3 a (`R6_public`). Ten instances of the subset of Sun et al. used by Glover, Amini and Kochenberger
  (2005). Our MIP (1 thread, 60 s) proves the optimum on the 8 instances up to 10x30, and it equals the
  CPLEX 9.0 value of their Table 3 on all 8; N1004 and N1007 (50x50) stop at the limit. Median gap to the
  reference: ILS 0 % on the 8 and 0.057 and 0.026 % on the two 50x50; Tabu 0 to 0.11 %; GA-cost-cycle 0.002
  to 0.62 %; the Balinski plan 0.08 to 0.54 %. On N1007 the best ILS run has the cost 162193, which is 44
  below the smallest value of that table (162237); the plan was computed again from its seed and checked by
  hand (row and column sums exact, cost 162193). We do not call it a new best known value: the later
  literature was not searched, and Barr et al. (2021) print 161186 for this name. Their values are below our
  proved optima on the other instances as well (by 3 to 5, and by 247 on N504), so their data or their cost
  differ from the files used here. The fixed charges of this set are small (the Balinski plan is within
  0.54 % everywhere), so it separates the methods weakly.
* 10.3 b (`R5_generator_gap`, `R5_generator_tests`). 90 new instances: `uniform` with rho = 0.05 and 5, and
  `concentrated` with the four rho, sizes 20x20, 30x30, 50x50, 5 per cell. In each of the 8 scopes (class and
  rho, 15 instances) GA-cost-cycle is worse than Tabu and worse than ILS (p_Holm from 0.00012 to 0.0020;
  losses 13 to 15 of 15). Shift against Tabu from 1.1 points (concentrated, rho = 1) to 7.2 (uniform,
  rho = 5), against ILS from 1.4 to 8.9. In all 18 new cells the median gap of GA-cost-cycle is above those of
  Tabu and of ILS. ILS is ahead of Tabu in 17 of them (the exception: `concentrated`, rho = 5, 20x20, 1.38
  against 1.29 %). In 5 of the 18 cells the Balinski plan, from which the two local searches start, has a
  smaller median gap than GA-cost-cycle: `uniform` with rho = 0.05 at 30x30 and 50x50, `concentrated` with
  rho = 0.05 at 30x30 and 50x50 and with rho = 0.2 at 50x50.
* 10.4 (`R7_timing`). One run at a time on logical processor 2, median by size from 10x10 to 70x70:
  GA-cost-cycle 0.055, 0.17, 0.39, 1.35, 8.0, 26 s; Tabu 0.008, 0.015, 0.025, 0.059, 0.20, 0.48 s; ILS 0.006,
  0.012, 0.022, 0.054, 0.18, 0.43 s. The same runs with 20 at once took 1.1 to 1.7 times longer (GA at
  70x70: 40 to 43 s). Evaluations per run: the GA 18870 to 978290 decoder calls; Tabu and ILS one evaluation
  of the start plan and B - 1 neighbour evaluations. The MIP with one thread and the GA time on one processor
  as its limit: gap of its plan 1.5 to 21 % up to 30x30, 2.1 to 3.6 % at 50x50, 1.3 to 1.8 % at 70x70. ILS is
  better than that plan on all instances up to 30x30 except two ties at 10x10, on 4 of 6 at 50x50 and on 2 of
  6 at 70x70; GA-cost-cycle is worse than it on 5 of 6 at 50x50 and 6 of 6 at 70x70.
* 10.5 a (`R8_theta_share`, figure `theta_share`). Median share of pivots with theta > 0 in the first tenth
  of the budget and in the last: GA-rand-cycle 0.91 and 0.65 at 20x20, 0.64 and 0.47 at 50x50, 0.36 and 0.27
  at 100x100; GA-cost-cycle 0.97 and 0.76, 0.82 and 0.41, 0.50 and 0.31. The share falls in the first two or
  three tenths and then stays level. The 90 repeated runs have the costs of their records.
* 10.5 b (`R9_entering_rule`, `R9_entering_tests`). 60 instances (5x5 to 50x50 and the structured 20x20),
  1200 runs. With the second rule no pivot had theta = 0 and no pivot was left to the uniform rule in any
  run. GA-cost-cycle: the second rule gives the smaller gap on 34 instances, ties on 16, the larger on 10
  (p_Holm = 8.3e-6, shift -0.25 points, interval -0.61 to -0.08); at 50x50 on 10 of 10 (4.26 against 7.31 %,
  shift -3.20, interval -4.61 to -2.20, p_Holm = 0.0039); at 30x30 8 of 10 (p_Holm = 0.055); no difference
  up to 20x20. GA-rand-cycle: the second rule is worse on 35, ties on 15, better on 10 (p_Holm = 2.1e-5,
  shift +0.90, interval 0.16 to 1.77); at 50x50 worse on 10 of 10 (21.2 against 11.9 %). With the same
  budget of evaluations a run with the second rule took 2.1 to 3.9 times longer from 20x20 up. 100x100 was
  not compared (time rule).
* 10.6 (`S1_pairs`, `S2_bootstrap_linear`, `S3_normalisation`). 128 paired comparisons of 8.6, 9.1, 8.4, 9.2,
  9.4, 10.1, 10.3 and 10.5 with the shift and its interval; the earlier test tables gained three columns and
  their other columns did not change. With the denominator Z_NWC - Z* the order of the eight methods by
  median is the same as with Z_rand - Z* in all 7 cells.
* 10.7: `figures/linear_gap_sizes`, `figures/fctp_gap_rivals`, `figures/theta_share` (PDF and JPG, 600 dpi).
* 10.8: `.zenodo.json`, `CITATION.cff` with the version `0.4.0-paper`, the workflow
  `.github/workflows/paper-release.yml` and the release notes `docs/releases/v0.4.0-paper.md`. The tag
  `v0.4.0-paper` is set on the commit that holds the tables of this record. No DOI was requested; the
  repository has to be enabled in Zenodo by its owner first.
