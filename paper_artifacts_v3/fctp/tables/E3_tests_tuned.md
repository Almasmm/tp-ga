# FCTP: paired comparisons of the variants chosen on FCTP (amendment 9.2)

Unit: the instance (median gap over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over the three pairs of each scope, rank-biserial r (negative: method_a has the smaller gap). Only one variant was given a grid on FCTP, so the `-ft` variants are not tested against the other heuristics.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all instances | GA-cost-cycle-ft | GA-cost-cycle | 40 | 19 | 3 | 18 | 2.652 | 2.66 | 327 | 0.7204 | -0.0697 | -0.09734 | 1.819e-12 | 1 | 1.000 |
| all instances | GA-hybrid-ft | GA-cost-cycle-ft | 40 | 11 | 11 | 18 | 2.391 | 2.652 | 200 | 0.7172 | 0.08046 | 0.01171 | 1.819e-12 | 1 | 1.000 |
| all instances | GA-hybrid-ft | GA-hybrid | 40 | 20 | 4 | 16 | 2.391 | 2.848 | 280 | 0.414 | -0.1592 | -0.1526 | 1.819e-12 | 1 | 1.000 |
| rho = 0.2 | GA-cost-cycle-ft | GA-cost-cycle | 20 | 10 | 2 | 8 | 1.596 | 1.825 | 63 | 0.3465 | -0.2632 | -0.1872 | 1.907e-06 | 0.6364 | 0.636 |
| rho = 0.2 | GA-hybrid-ft | GA-cost-cycle-ft | 20 | 4 | 7 | 9 | 1.596 | 1.596 | 30 | 0.3054 | 0.3407 | 0.05623 | 1.907e-06 | 0.6364 | 0.636 |
| rho = 0.2 | GA-hybrid-ft | GA-hybrid | 20 | 11 | 2 | 7 | 1.596 | 2.116 | 56 | 0.2121 | -0.345 | -0.1839 | 1.907e-06 | 0.6364 | 0.636 |
| rho = 1 | GA-cost-cycle-ft | GA-cost-cycle | 20 | 9 | 1 | 10 | 3.89 | 2.956 | 85 | 0.7086 | 0.1053 | 0.2101 | 1.907e-06 | 1 | 1.000 |
| rho = 1 | GA-hybrid-ft | GA-cost-cycle-ft | 20 | 7 | 4 | 9 | 4.143 | 3.89 | 61 | 0.7436 | -0.1029 | 0 | 1.907e-06 | 1 | 1.000 |
| rho = 1 | GA-hybrid-ft | GA-hybrid | 20 | 9 | 2 | 9 | 4.143 | 3.341 | 81 | 0.865 | -0.05263 | -0.05949 | 1.907e-06 | 1 | 1.000 |
