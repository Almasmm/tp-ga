# Manuscript map: where every number of the article comes from in v0.4

Every number of the revised article is taken from `paper_artifacts_v2/` after the main run (`tpga-exp report`).
v0.3.0 (`paper_artifacts/`) is referred to only through the `legacy` phase (the v0.3.0 stopping rule re-run
under v0.4). The article text quoted below is the v0.3.0 manuscript (Google Doc, tab "English manuscript");
the value in it is replaced by the v0.4 cell given on the right. The Russian and Kazakh abstracts carry the
same numbers as the English one and take them from the same cells.

## Notation

* `T2[set=uniform, size=100x100, method=GA-rand-base].gap_median` is the column `gap_median` of the row of
  `tables/T2_gap.csv` with these values. All tables are in `paper_artifacts_v2/tables/` (CSV and Markdown).
* `F:name` is `figures/{en,ru}/name.{png,pdf}`.
* Method names. v0.3.0 "GA-rand"/"GA-cost" (base parameters, stopped after 200 generations without
  improvement) correspond in v0.4 to `GA-rand-base`/`GA-cost-base` (same parameters, budget-only stop);
  the tuned variants are `GA-rand-tuned`/`GA-cost-tuned`; `SA-rand-tuned`/`SA-cost-tuned` are new. Which
  variant the text reports is a writing decision; the map gives the cell for each.
* "No v0.4 source" marks a number for which v0.4 has no table: the sentence must be rewritten or removed,
  or a phase added (decision for the authors, listed at the end).

## Abstract (EN, RU, KZ)

| Article (v0.3.0) | v0.4 source |
|---|---|
| "80 synthetic instances from 5×5 to 100×100" | `T1_instances.instances` summed over sets used in RQ1-RQ2 (uniform, structured, skewed, ties); sizes from `T1.size` (v0.4: 5x5 to 200x200) |
| "30 runs each" | `experiments/paper-v2.yaml: runs` (30; 10 at uniform 200x200, amendment 1) |
| "two illustrative cases ... Kazakhstan" | phase `applied` (amendment 4): `T10_applied_summary`, `T10_applied_instances` |
| "200 generations" stagnation | v0.4 main stop is budget only; the 200-generation rule is `T7[stop=200 generations]` |
| "median gap of GA-rand grows from 5.9% at 10×10 to 603% at 100×100" | `T2[set=uniform, size=10x10 / 100x100, method=GA-rand-base or GA-rand-tuned].gap_median` |
| "GA-rand beats random search and NWC on every instance from 10×10 on" | `T5_methods_gap[method_a=GA-rand-base, method_b=RS / NWC].wins_x == n`, per (set, size) |
| "loses to VAM on every uniform instance from 20×20 on" | `T5_methods_gap[method_a=GA-rand-base or GA-rand-tuned, method_b=VAM].wins_y`, per size |
| "GA-cost has a median gap of 30% at 100×100" | `T2[uniform, 100x100, GA-cost-tuned or GA-cost-base].gap_median` |
| "never worse than VAM" | `T5_methods_gap[method_a=GA-cost-tuned, method_b=VAM].wins_y == 0` for every (set, size) |
| "HiGHS solves 100×100 instances in 0.03 s" | `T3_time[set=uniform, size=100x100, method=LP].time_median_s` (HiGHS run time inside the solver, highspy) |
| "faster than the GA at every tested size" | `T3_time.time_median_s`, LP vs GA-*/SA-* per size |
| "lowers the gap by a factor of 9 to 14" | `T6_initialisation.ratio_median` (20x20, 50x50) |

## 1. Introduction

| Article | v0.4 source |
|---|---|
| "80 synthetic instances" | as in the abstract (`T1_instances`) |
| 1941, 1991, "180 instances", "230 of 240", "25 shipment variables", "149 instances" | literature, not experiment data; unchanged |
| H1-H4 | unchanged wording; tested by the cells of 3.2-3.5 |

## 2. Materials and methods

| Section, article | v0.4 source |
|---|---|
| 2.2 Example 1: Z = 2445, 2345, 2310, 2835, 2220; gaps 10.14, 5.63, 4.05, 27.70 %; 6 shipments | `T0_example1.cost`, `.gap`, `.positive` (recomputed by the library) |
| 2.2 Table 1 order of shipments | `T0_example1.shipments_in_order`. The VAM row and the leaf-elimination row of the article list the same plans in another order (VAM: x12 = 20 before x22, x32; leaf order: x31 before x12, x11); take the v0.4 order or say that any leaf order works |
| 2.3 Table 2: P = 100, pc = 0.9, pm = 0.2, t = 3, e = 2 | base configuration: `experiments/paper-v2.yaml: methods.GA-rand-base.params`; tuned: `experiments/tuned-v2.yaml: parameters` |
| 2.3 "B = 200·m·n ... bounded below by 20,000 and above by 2,000,000" | `paper-v2.yaml: budget` = min(200 m n, 8 000 000): no lower bound, the upper bound is not active (amendment 1) |
| 2.3 "200 generations" | `paper-v2.yaml: phases.legacy.stop` (legacy phase only) |
| 2.3 RQ4 levels 20, 50, 100, 200 and 0.01-0.2 | `paper-v2.yaml: phases.factorial` (P 20-400; 4 mutation operators x 3 strengths) |
| 2.4 "HiGHS ... version 1.12.0 through linprog" | `run_manifest.json: invocations[0].packages.highspy` (1.16.0, highspy); OR-Tools version from the same entry |
| 2.4 "tolerances of 10⁻⁹" | `paper-v2.yaml: tolerance` |
| 2.5 sizes, 10 per size, U[1,100], supplies [20,100] | `paper-v2.yaml: instances`; counts `T1_instances.instances` |
| 2.5 Table 3 | `T1_instances` (set, size, instances, arcs, z_star_median, z_rand_median, generator) |
| 2.6 seeds s0 = 20261116, r = 0..29 | `paper-v2.yaml: base_seed, runs`, `phases.main.runs_by_size` |
| 2.6 gap formula | unchanged; normalised gap added: `T2.gap_norm_median`, `T5_methods_gap_norm` |
| 2.7 "family of seven comparisons; 7·2⁻⁹ ≈ 0.014" | v0.4: family of 10 (PREREGISTRATION section 5); floor 10·2/1024 ≈ 0.0195; `T5_methods_gap.p_holm` |
| 2.7 Cliff's delta | replaced by `rank_biserial_r` and the Hodges-Lehmann shift `hl_shift [hl_ci_low, hl_ci_high]` |
| 2.7 "No parameter was tuned" | v0.4 tunes on training instances: `tuned-v2.yaml` (procedure, training_instances, best_objective) |
| 2.8 "version 0.3.0", Python, NumPy, SciPy, Numba versions | `run_manifest.json: invocations[0].packages`, `.environment` |
| 2.8 "28,012 recorded runs and took about 3 h 52 min" | `T0_checks[phase=total].records`, `.wall_h` |

## 3. Results and discussion

### 3.1 Correctness

| Article | v0.4 source |
|---|---|
| "1,000 random balanced integer instances with 2 to 30 sources and destinations ... supplies of at most 20" | `reachability.json: instances, generator` |
| "decoded exactly to the optimal vertex, including 693 degenerate vertices" | `reachability.json: reproduced, degenerate_vertices, degenerate_reproduced` (also in `report.json: reachability`) |
| "none of the 28,012 recorded plans failed ... largest constraint residual was zero" | `T0_checks[phase=total].plans_checked, plans_infeasible, max_residual` |

### 3.2 Distance from the optimum (RQ1)

| Article | v0.4 source |
|---|---|
| 5×5: optimum in 97.3 / 91.0 / 80.3 % of runs | `T2[uniform, 5x5, method].share_optimal` |
| medians 5.9, 48.7, 103.9, 219.9, 602.8 % (GA-rand) | `T2[uniform, size, GA-rand-*].gap_median` (v0.4 adds 200x200) |
| "1.0% of its runs reached the optimum at 10×10" | `T2[uniform, 10x10, GA-rand-*].share_optimal` |
| GA-cost medians 1.2, 7.8, 12.5, 25.6, 30.2 %; "largest gap of 47.0%" | `T2[uniform, size, GA-cost-*].gap_median`; maximum of `T2[uniform, *, GA-cost-*].gap_max` |
| "without the limit the mean gap ... falls from 606.6% to 358.8%" | `T7[uniform, 100x100, GA-rand-base, stop=200 generations / budget only].gap_mean` |
| structured vs uniform: 7.9 / 26.1 vs 52.7 / 221.9 %; 0.85 / 4.4 vs 8.0 / 26.7 % | `T2[set, size, method].instance_median_median` |
| "Mann–Whitney test, p < 0.001" | No v0.4 source: not pre-registered; report the medians descriptively or drop the test |
| Figure 3 statements ("passes the LCM line after about 2·10³ calls", "ends 5 to 16 percentage points below VAM") | `F:convergence` (median, IQR, NWC/LCM/VAM lines; uniform set); exact values from `raw/curves` (median gap at each budget point) and `T2[...].gap_median` of GA-cost-* minus VAM |
| "Most runs ... end through the stagnation rule" | not applicable to the budget-only main phase; see 3.6 (`T7`) |
| Table 4 (median (maximum)) | `T2.gap_median (gap_max)`; for NWC/LCM/VAM `runs` = instances, so the median is over the ten instances |
| Figure 2 | `F:boxplot_gap` (and `F:boxplot_gap_norm`) |

### 3.3 Classical rules and random search (RQ2)

| Article | v0.4 source |
|---|---|
| wins/ties/losses, pHolm, δ in Table 5 | `T5_methods_gap[set, size, method_a, method_b]`: `wins_x / ties / wins_y`, `p_holm_text`, `rank_biserial_r`, `hl_shift [hl_ci_low, hl_ci_high]` |
| "better than NWC on all 80 instances" | sum of `T5[method_b=NWC].wins_x` over (set, size) vs sum of `n` |
| "GA-cost ... better on 76 and equal on 4" | sums of `T5[method_a=GA-cost-tuned, method_b=VAM].wins_x` and `.ties` |
| RS medians 63.3, 215.9, 755.5, 1497.8 %; "2.5 to 11 times" | `T2[uniform, size, RS].gap_median`; ratio to `T2[..., GA-rand-*].gap_median` |
| RS optimum 80.3 % at 5×5; tie on 8 of 10 | `T2[uniform, 5x5, RS].share_optimal`; `T5[uniform, 5x5, GA-rand-base, RS].ties` |

### 3.4 Runtime growth (RQ3)

| Article | v0.4 source |
|---|---|
| HiGHS 0.028 s; GA-cost 1.70 s; GA-rand 26.9 s; "60 and 960 times" | `T3_time[uniform, 100x100, method].time_median_s` (LP, GA-*-tuned, SA-rand-tuned) and their ratios |
| β = 0.91 (0.87–0.96, R² 0.97), β = 1.39 (1.32–1.45, 0.97) | `T3_fits[method, measure=time per run, range=all sizes or m n >= 2500].b, b_ci_low, b_ci_high, r2` |
| "time of one decoder call grows from 0.43 µs at 5×5 to 36 µs at 100×100, with β between 0.73 and 0.75" | `T3_time.us_per_eval_median` (5x5, 100x100); `T3_fits[measure=time per decoder call].b` |
| HiGHS β = 0.54, R² = 0.89; "1.1 ms at 5×5" | `T3_fits[method=LP]`; `T3_time[uniform, 5x5, LP].time_median_s` (v0.4 measures inside HiGHS; presolve, build and wrapper times in `T3_time.presolve_median_s, build_median_s, wrapper_median_s`) |
| new: exact solvers up to 1000x1000 | `T8_lp_scaling` (HiGHS and OR-Tools), `T8_lp_disagreement` (expected empty) |
| Figure 4 | `F:time_scaling` |

### 3.5 Population, mutation, initialisation (RQ4)

| Article | v0.4 source |
|---|---|
| "32 cells", Table 6 (mean gap per cell) | `T4_factorial[size, initialization, population, mutation].gap_mean` (v0.4: 5 populations x 12 mutation settings x 2 starts x 2 sizes = 240 cells; Table 6 must be redesigned, e.g. `F:factorial_heatmap` plus the best and worst cells) |
| Friedman χ² 128–149, 15 df, p < 0.001; Kendall's W 0.85–0.99 | `T4_tests[test=Friedman, all cells].chi2, p_text, kendall_w` (df = `treatments` - 1) |
| "best mean rank" / "worst" cell | `T4_factorial.mean_rank` (minimum / maximum per size and start) |
| post-hoc pairs, "pHolm = 0.064" | `T4_tests[test=Wilcoxon population: ... / mutation: ...].p_holm, p_text, hl_shift` |
| "from 106.5% to 43.3%", "from 111.3% to 50.2%" | `T4_factorial[20x20, random, P, mutation].gap_mean` for the cells named in the text |
| "GA-cost has the lower gap on all ten instances of both sizes (p = 0.002)" | `T6_initialisation[size].wins_x, p_text` |
| ratio "9.3 at 20×20 and 14.3 at 50×50"; "exceeds 1 in every cell" | `T6_initialisation.ratio_median`; `.cells_cost_aware_lower_share` (1.0 = every cell) |
| "70 and 344 percentage points" | `T6_initialisation.reduction_pp_median` |
| "median number of calls ... from 8,138 ... to 79,994" | not applicable: the factorial phase stops by budget only, every run uses B (the confound described in the article is removed) |

### 3.6 Use of the evaluation budget

| Article | v0.4 source |
|---|---|
| shares stopped by the rule (70 %, 57 %, 94 %, all) | `T7[uniform, size, method, stop].stopped_early_share` (sizes 20x20, 50x50, 100x100) |
| "median run used 35% of the budget", "2.2%", "found after 1.2%" | `T7.budget_used_median`, `T7.best_found_median` |
| mean gaps with and without the limit (227.4→177.5, 606.6→358.8, 25.8→21.9, 28.4→24.0); p = 0.002, r = 1 | `T7[...].gap_mean` for `budget only` and `200 generations`; `T7.p_text, hl_shift, hl_ci_low, hl_ci_high` |
| "204 s per 100×100 run instead of 4.2 s" | `T7.time_median_s` (quality phase, all cores) |
| "VAM ... mean gap at 100×100 is 36.5%" | `T2[uniform, 100x100, VAM].gap_mean` |

### 3.7 Illustrative cases

| Article | v0.4 source |
|---|---|
| Table 7, wheat rows (5 scenarios): NWC/LCM/VAM gaps, RS and GA means over runs | `T10_applied_instances[set=wheat, instance, method].gap_mean` (10 runs per stochastic method) |
| "VAM is 0.47–2.24% above the optimum", "RS 0.47–1.39%", "below 0.14%", "1.5–6.9%" | min and max of `T10_applied_instances[set=wheat, method].gap_mean` over the scenarios |
| "105 arcs" | 15 x 7 (`T10_applied_summary[set=wheat].size`) |
| Astana row: median (range) over 33 instances: 34.4, 8.4, 6.2, 37.7, 8.4, 1.6 % | `T10_applied_summary[set=astana, method].gap_median (gap_min - gap_max)`, `instances` = 33 |
| "GA-cost was better than VAM on all 33 instances and GA-rand on 3" | `T10_applied_summary[set=astana, method=GA-*-tuned].better_than_vam` |
| "7,776 arcs" | 24 x 324 |
| **Size of the Astana instances: 24×324, not 8×40.** Wherever section 3.7 (text, Table 7, figure captions) gives the Astana problem as 8×40 (320 arcs), it changes to 24×324 (7,776 arcs). The 8×40 API sample is not an instance of the phase `applied` (amendment 4) | `T10_applied_summary[set=astana].size` = `24x324`; `paper_artifacts_v2/instances/manifest.json` (33 instances, m = 24, n = 324) |
| "22 s" (GA-cost per run), "0.044 s" (HiGHS) | `T10_applied_summary[set=astana, method=GA-cost-tuned / LP].time_median_s` (quality phase, all cores; LP is HiGHS run time) |
| v0.4 adds SA-rand-tuned, SA-cost-tuned | same tables |

### 3.8 Discussion, 3.9 Threats to validity

| Article | v0.4 source |
|---|---|
| "0.028 s", "about 30% above the optimum after 1.7 s" | `T3_time[uniform, 100x100, LP / GA-cost-*].time_median_s`; `T2[uniform, 100x100, GA-cost-*].gap_median` |
| "30 seeded runs per instance" | `paper-v2.yaml: runs`, `runs_by_size` |
| "A gap normalised by the cost of a random basic plan ... planned" | now reported: `T2.gap_norm_median`, `T5_methods_gap_norm`, `F:boxplot_gap_norm`; Z_rand per instance in `instances/manifest.json` and `T1.z_rand_median` |
| "parameters were not tuned", "mutation intensity does not grow" | v0.4: tuned (`tuned-v2.yaml`), mutation modes `swap_count`, `swap_per_position`, `swap_scaled` |
| new: why the gap grows with size | `tables/representation.csv` (prefix_share, neutral_share by operator and m n, locality, inherited_share) and `F:representation_neutrality`; sizes 5x5 to 100x100 (amendment 7, g); for 200x200 use the exact bound of Proposition 3, not a measured value |

## 4. Conclusions

| Article | v0.4 source |
|---|---|
| RQ1: 48.7 % and 602.8 % (GA-rand), 7.8 % and 30.2 % (GA-cost) | `T2[uniform, 20x20 / 100x100, GA-*].gap_median` |
| RQ2: "all 80 instances", "after 5×5", "after 10×10", "from 20×20", "from 30×30" | `T5_methods_gap` wins per (set, size) |
| RQ3: "25 and 10,000 arcs"; exponents 1.39 and 0.91 | `T1.arcs` range; `T3_fits.b` |
| RQ4: 9.3 and 14.3; "up to 98% of the budget unused" | `T6.ratio_median`; `1 - T7[stop=200 generations].budget_used_median` (minimum) |
| Data availability: "release v0.3.0-paper" | release `v0.4.0` and its DOI (after the run) |

## Numbers without a v0.4 source (decision needed before writing)

1. Section 3.7: resolved by the phase `applied` (amendment 4, 2026-11-17).
2. Section 3.2, Mann–Whitney comparison of structured and uniform instances: not pre-registered in v0.4;
   report the medians from `T2.instance_median_median` without a test, or drop the sentence.
