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
