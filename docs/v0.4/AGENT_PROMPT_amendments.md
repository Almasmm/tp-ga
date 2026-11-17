# Prompt for the agent: amendments to v0.4 before the main run

Project: `C:\dev\tp-ga`, branch `work/v0.4`. The main run (`phase main`) has **not started yet**. Everything below
must be done and committed **before** it starts. Every change to the experiment is recorded in section 9 of
`docs/v0.4/PREREGISTRATION.md` with the date, the change and the reason. Sections 1–8 are changed only through
section 9. Do not touch `v0.3.0`, the tag `v0.3.0-paper`, `paper_artifacts/` or `experiments/paper.yaml`.

Work in this order. Stop and report to the user at the two marked points.

## 0. CI

The latest CI run on `work/v0.4` (commit `5cd4e8a`) must be green on all jobs before anything else.
Find the cause of any failure from the job log, fix it, push, and wait for green. The main run is made
from a commit with a green CI. Tag that commit `v0.4.0-run` after section 5.

## 1. Budget (decision point 1: report and wait for the user's choice)

Current state: `budget: {factor: 200, cap: 8000000}`. The cap equals 200·mn at 200×200, so it is not
active. The pilot estimates 43.9 h in total.

Prepare these two options with the updated pilot estimate for each:

* **A (recommended):** keep B = 200·mn without an effective cap at every size; run 200×200 in the main
  phase with 10 seeds (r = 0..9) instead of 30. The unit of every test is the per-instance median, so
  the tests still have 10 pairs. The budget rule is the same at every size, so the growth of the gap
  with size is not affected by a change of the budget per arc.
* **B:** cap 2 000 000 decoder calls, 30 seeds everywhere. The budget per arc at 200×200 drops from 200
  to 50, which must be reported as a limitation of the size trend.

Record the chosen option in section 9.

## 2. Repeat the tuning with a range that does not bind

Reason: both SA results have `initial_acceptance` near the lower bound 0.05 (0.0676 and 0.0688). A
comparator tuned against a bound is disadvantaged, and a reviewer will ask about it. Forty TPE trials for a
nine-dimensional conditional GA space are also few.

Changes (identical for all four tuned methods, so the tuning effort stays equal):

* `initial_acceptance`: [0.001, 0.95], sampled on a log scale.
* `trials`: 40 → 100.
* Training sets: uniform 20×20 and 50×50 (4 instances each, as now) **plus uniform 100×100 (2 instances)**,
  3 seeds, seed offset 5 000 000 as before. The training instances must not overlap the test instances
  (check SHA-256 against `paper_artifacts_v2/instances/manifest.json`).
* After the tuning, check every parameter of every method. If a value lies within 5 % of the width of
  its range from a bound, widen that bound once (log scale where the range spans more than a factor of
  10), repeat the tuning of **all** methods once and record both results. Do not widen more than once.
* Keep the old `experiments/tuned-v2.yaml` as `experiments/tuned-v2-superseded.yaml`, and quote its table in
  section 9.

## 3. New non-confirmatory phase `representation`

Purpose: explain why the gap grows with size. A quick check outside the project, on uniform instances
with costs in [1, 100], gave these values for a random permutation: share of single swaps that do not
change the decoded cost: 0.70 at 10×10, 0.81 at 20×20, 0.90 at 50×50 and 0.94 at 100×100. Only m + n − 1
of the mn arcs carry flow, so most swaps exchange two arcs that carry no flow in either order. This must
be measured in the project, with the project's decoder and instances.

Add the phase to `experiments/paper-v2.yaml` and the library code to `src/tpga/analysis/representation.py`
with tests. Instances: uniform 5×5 to 200×200 and each other class at 50×50, 10 instances each. For every
instance:

1. **Decoder prefix.** For 1000 random permutations and for the final populations of GA-rand-tuned and
   GA-cost-tuned (seeds 0..9): number of arcs with positive flow, and the length of the prefix the decoder
   reads before all supply is used (absolute and as a share of mn).
2. **Neutrality of mutation.** For every mutation operator and strength of the factorial plan and for the
   tuned settings: share of offspring whose decoded cost equals the parent's. Parents: (a) 1000 random
   permutations, (b) the individuals of the GA population at 10 %, 50 % and 100 % of the budget (seeds 0..9).
3. **Locality.** For k = 1, 2, 5, 10, 20 random swaps applied to a parent: median |ΔZ|/Z* and the share of
   neutral results; Spearman correlation between k and |ΔZ|.
4. **Heritability of crossover.** For the project's crossover operator and parents from the population
   at 50 % of the budget: share of the child's positive-flow arcs that carry positive flow in at least one
   parent.

Output: `paper_artifacts_v2/tables/representation.csv` and one figure (neutral share against mn for each
operator, log x axis). The phase is listed in section 7 of the pre-registration as non-confirmatory. It
runs on all cores and must fit in about 1 h; report its pilot estimate.

## 4. Article mapping

Create `paper_artifacts_v2/MANUSCRIPT_MAP.md`. For every number in the article it gives the table or
figure of v0.4 and the cell it comes from. Group it by article section (abstract RU/EN/KZ, 2.x, 3.1–3.8,
conclusions). All article numbers will come from v0.4. v0.3.0 is referenced only through the `legacy`
phase.

## 5. Decision point 2: report before the main run

Report to the user in Russian:

* CI status, commit and tag;
* the chosen budget option and the new pilot estimate;
* the new tuning table (parameters, training gap) next to the old one, with any widened bounds;
* the representation phase: pilot time, first numbers at 20×20 and 100×100;
* the exact command that starts the main run and the command for the live monitor.

Do not start the main run yourself. The user starts it after the laptop is prepared per
`docs/v0.4/HEAVY_RUN.md`.

## 6. After the run (not now)

* `tpga-exp report` → all tables and figures of v0.4, with Hodges–Lehmann shifts and CIs.
* GitHub release `v0.4.0` and an archive with a DOI (Zenodo GitHub integration; the user connects the
  account). Update `CITATION.cff` and the data availability statement with the DOI.

## Rules

* Defaults of the library stay bitwise identical to v0.3.0 (`tests/test_regression_v030.py` stays green).
* No changes to the system settings of the laptop.
* No mocks, no placeholders, no skipped tests to make CI green.
