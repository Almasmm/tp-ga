# FCTP: GA-cost-cycle against Tabu and ILS

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Unit: the instance (median gap over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over the two pairs of each scope; `rank_biserial_r` and `hl_shift` (Hodges-Lehmann, with its 95 % interval) are for gap(method_a) - gap(method_b): positive means method_a (the GA) is worse.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_ci_method | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all instances | GA-cost-cycle | Tabu | 60 | 6 | 3 | 51 | 4.865 | 2.008 | 71 | 1.942e-09 | 0.9141 | 3.4 | 2.39 | 4.338 | normal-approximation Walsh-average CI | 1.735e-18 | 1.942e-09 | < 0.001 |
| all instances | GA-cost-cycle | ILS | 60 | 2 | 3 | 55 | 4.865 | 0.9192 | 5 | 6.711e-11 | 0.994 | 4.701 | 3.41 | 5.727 | normal-approximation Walsh-average CI | 1.735e-18 | 1.342e-10 | < 0.001 |
| rho = 0.2 | GA-cost-cycle | Tabu | 30 | 2 | 1 | 27 | 4.005 | 1.329 | 11 | 2.049e-07 | 0.9494 | 2.853 | 1.56 | 4.254 | exact Walsh-average CI | 1.863e-09 | 2.049e-07 | < 0.001 |
| rho = 0.2 | GA-cost-cycle | ILS | 30 | 0 | 2 | 28 | 4.005 | 0.5839 | 0 | 7.451e-09 | 1 | 4.038 | 2.385 | 5.5 | exact Walsh-average CI | 1.863e-09 | 1.49e-08 | < 0.001 |
| rho = 1 | GA-cost-cycle | Tabu | 30 | 4 | 2 | 24 | 5.625 | 2.513 | 22 | 3.994e-06 | 0.8916 | 3.804 | 2.392 | 5.168 | exact Walsh-average CI | 1.863e-09 | 3.994e-06 | < 0.001 |
| rho = 1 | GA-cost-cycle | ILS | 30 | 2 | 1 | 27 | 5.625 | 1.318 | 5 | 3.725e-08 | 0.977 | 5.273 | 3.461 | 6.708 | exact Walsh-average CI | 1.863e-09 | 7.451e-08 | < 0.001 |
| size 10x10 | GA-cost-cycle | Tabu | 10 | 3 | 2 | 5 | 0.963 | 0.8222 | 15 | 0.7422 | 0.1667 | 0.03405 | -0.3022 | 1.064 | exact Walsh-average CI | 0.001953 | 0.7422 | 0.742 |
| size 10x10 | GA-cost-cycle | ILS | 10 | 0 | 2 | 8 | 0.963 | 0 | 0 | 0.007812 | 1 | 1.043 | 0.4211 | 1.94 | exact Walsh-average CI | 0.001953 | 0.01562 | 0.016 |
| size 15x15 | GA-cost-cycle | Tabu | 10 | 3 | 1 | 6 | 1.213 | 0.9951 | 15 | 0.4258 | 0.3333 | 0.4072 | -0.6131 | 1.458 | exact Walsh-average CI | 0.001953 | 0.4258 | 0.426 |
| size 15x15 | GA-cost-cycle | ILS | 10 | 2 | 1 | 7 | 1.213 | 0 | 5 | 0.03906 | 0.7778 | 1.108 | 0.01375 | 2.222 | exact Walsh-average CI | 0.001953 | 0.07812 | 0.078 |
| size 20x20 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 2.785 | 1.254 | 0 | 0.001953 | 1 | 1.255 | 0.7597 | 2.98 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 20x20 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 2.785 | 0.328 | 0 | 0.001953 | 1 | 2.316 | 1.63 | 3.692 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 30x30 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 6.362 | 1.872 | 0 | 0.001953 | 1 | 4.412 | 3.475 | 5.818 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 30x30 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 6.362 | 1.013 | 0 | 0.001953 | 1 | 4.954 | 4.23 | 6.455 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 50x50 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 10.95 | 3.873 | 0 | 0.001953 | 1 | 7.1 | 5.013 | 8.41 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 50x50 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 10.95 | 1.799 | 0 | 0.001953 | 1 | 8.994 | 7.208 | 10.24 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 70x70 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 11.28 | 3.964 | 0 | 0.001953 | 1 | 7.083 | 5.651 | 9.185 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
| size 70x70 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 11.28 | 1.365 | 0 | 0.001953 | 1 | 9.65 | 8.042 | 11.35 | exact Walsh-average CI | 0.001953 | 0.003906 | 0.004 |
