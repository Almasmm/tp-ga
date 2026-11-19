# FCTP above 30x30: the GA variants against the MIP solver with 60 s

Unit: the instance; the median gap of the GA over its seeds against the gap of the one MIP plan (both to the same Z_best, so wins and losses are those of the cost). Two-sided Wilcoxon signed-rank test, Holm correction over the three pairs of each scope, rank-biserial r (negative: the GA has the smaller gap). Instances where the MIP has no plan at 60 s are left out of the test and counted in the last column.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | smallest_possible_p | p_holm | p_holm_text | mip_without_plan_counted_as_wins_a |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all instances | GA-cost-cycle | MIP-60s | 20 | 0 | 0 | 20 | 10.23 | 0 | 0 | 1.907e-06 | 1 | 9.648 | 1.907e-06 | 5.722e-06 | < 0.001 | 0 |
| all instances | GA-cost-cycle-ft | MIP-60s | 20 | 0 | 0 | 20 | 7.622 | 0 | 0 | 1.907e-06 | 1 | 7.845 | 1.907e-06 | 5.722e-06 | < 0.001 | 0 |
| all instances | GA-hybrid-ft | MIP-60s | 20 | 0 | 0 | 20 | 10.68 | 0 | 0 | 1.907e-06 | 1 | 10.3 | 1.907e-06 | 5.722e-06 | < 0.001 | 0 |
| size 50x50 | GA-cost-cycle | MIP-60s | 10 | 0 | 0 | 10 | 10.94 | 0 | 0 | 0.001953 | 1 | 9.642 | 0.001953 | 0.005859 | 0.006 | 0 |
| size 50x50 | GA-cost-cycle-ft | MIP-60s | 10 | 0 | 0 | 10 | 7.605 | 0 | 0 | 0.001953 | 1 | 7.635 | 0.001953 | 0.005859 | 0.006 | 0 |
| size 50x50 | GA-hybrid-ft | MIP-60s | 10 | 0 | 0 | 10 | 9.913 | 0 | 0 | 0.001953 | 1 | 9.577 | 0.001953 | 0.005859 | 0.006 | 0 |
| size 70x70 | GA-cost-cycle | MIP-60s | 10 | 0 | 0 | 10 | 9.511 | 0 | 0 | 0.001953 | 1 | 9.534 | 0.001953 | 0.005859 | 0.006 | 0 |
| size 70x70 | GA-cost-cycle-ft | MIP-60s | 10 | 0 | 0 | 10 | 8.06 | 0 | 0 | 0.001953 | 1 | 8.512 | 0.001953 | 0.005859 | 0.006 | 0 |
| size 70x70 | GA-hybrid-ft | MIP-60s | 10 | 0 | 0 | 10 | 11.48 | 0 | 0 | 0.001953 | 1 | 11.04 | 0.001953 | 0.005859 | 0.006 | 0 |
