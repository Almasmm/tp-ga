# Linear problem: the second rule for the entering arc against the present rule

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Unit: the instance (median gap over 10 seeds). Two-sided Wilcoxon signed-rank test, Holm over the two pairs of each scope; `hl_shift` and `rank_biserial_r` are for gap(method_a) - gap(method_b): negative means the second rule gives the smaller gap.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_ci_method | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform 5x5 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | exact Walsh-average CI | 0.001953 | 1 | 1.000 |
| uniform 5x5 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | exact Walsh-average CI | 0.001953 | 1 | 1.000 |
| uniform 10x10 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 2 | 5 | 3 | 0 | 0 | 7 | 1 | 0.06667 | 0 | -0.4127 | 0.4419 | exact Walsh-average CI | 0.001953 | 1 | 1.000 |
| uniform 10x10 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 5 | 4 | 1 | 0.1464 | 0.2654 | 1 | 0.0625 | -0.9048 | -0.1156 | -0.2677 | 0 | exact Walsh-average CI | 0.001953 | 0.125 | 0.125 |
| uniform 20x20 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 3 | 0 | 7 | 2.813 | 1.766 | 17 | 0.3223 | 0.3818 | 0.6361 | -0.7347 | 1.525 | exact Walsh-average CI | 0.001953 | 0.5 | 0.500 |
| uniform 20x20 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 5 | 1 | 4 | 0.6956 | 0.7617 | 12 | 0.25 | -0.4667 | -0.1014 | -0.5598 | 0.05185 | exact Walsh-average CI | 0.001953 | 0.5 | 0.500 |
| uniform 30x30 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 2 | 0 | 8 | 8.241 | 6.98 | 6 | 0.02734 | 0.7818 | 2.239 | 0.2127 | 3.328 | exact Walsh-average CI | 0.001953 | 0.05469 | 0.055 |
| uniform 30x30 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 8 | 0 | 2 | 1.943 | 2.703 | 7 | 0.03711 | -0.7455 | -0.5106 | -1.01 | -0.02545 | exact Walsh-average CI | 0.001953 | 0.05469 | 0.055 |
| uniform 50x50 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 0 | 0 | 10 | 21.17 | 11.87 | 0 | 0.001953 | 1 | 9.1 | 6.336 | 11.86 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| uniform 50x50 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 10 | 0 | 0 | 4.262 | 7.31 | 0 | 0.001953 | -1 | -3.202 | -4.607 | -2.197 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| structured 20x20 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 3 | 0 | 7 | 0.3647 | 0.2483 | 12 | 0.1309 | 0.5636 | 0.09728 | -0.02923 | 0.2648 | exact Walsh-average CI | 0.001953 | 0.2617 | 0.262 |
| structured 20x20 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 6 | 1 | 3 | 0.3317 | 0.3373 | 17 | 0.5703 | -0.2444 | -0.00719 | -0.2438 | 0.109 | exact Walsh-average CI | 0.001953 | 0.5703 | 0.570 |
| all instances | GA-rand-cycle-nd | GA-rand-cycle | 60 | 10 | 15 | 35 | 0.7523 | 0.5443 | 160 | 2.093e-05 | 0.6908 | 0.8955 | 0.1572 | 1.768 | normal-approximation Walsh-average CI | 1.735e-18 | 2.093e-05 | < 0.001 |
| all instances | GA-cost-cycle-nd | GA-cost-cycle | 60 | 34 | 16 | 10 | 0.503 | 0.6451 | 126 | 4.149e-06 | -0.7455 | -0.2497 | -0.606 | -0.07572 | normal-approximation Walsh-average CI | 1.735e-18 | 8.299e-06 | < 0.001 |
