# Every paired comparison of experiment v3 with effect sizes (amendment 10.6)

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Rows of the test tables named in `comparison`, unchanged. Unit: the instance (median over its seeds); the measure is the gap in percent (to Z* for the linear problem, to the Z_best of the table it comes from for FCTP). `hl_shift`: Hodges-Lehmann estimate of gap(method_a) - gap(method_b) with its 95 % interval from the Walsh averages; `rank_biserial_r`: matched-pairs rank-biserial correlation (negative: method_a has the smaller gap). `p_holm`: Holm within the family of its table.

| comparison | scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | p | p_holm | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_ci_method |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8.6 linear (T2_tests) | uniform 5x5 | GA-rand-cycle | VAM | 10 | 5 | 5 | 0 | 0 | 1.067 | 0.0625 | 0.3125 | -1 | -1.489 | -8.798 | 0 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 5x5 | GA-rand-cycle | GA-rand-tuned | 10 | 1 | 9 | 0 | 0 | 0 | 1 | 1 | -1 | 0 | -0.3504 | 0 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 5x5 | GA-rand-cycle | GA-cost-tuned | 10 | 2 | 8 | 0 | 0 | 0 | 0.5 | 1 | -1 | 0 | -0.6981 | 0 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 5x5 | GA-cost-cycle | GA-cost-tuned | 10 | 0 | 10 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 5x5 | GA-cost-cycle | VAM | 10 | 5 | 5 | 0 | 0 | 1.067 | 0.0625 | 0.3125 | -1 | -1.147 | -8.798 | 0 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 10x10 | GA-rand-cycle | VAM | 10 | 9 | 1 | 0 | 0 | 8.377 | 0.003906 | 0.01953 | -1 | -8.998 | -17.83 | -3.927 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 10x10 | GA-rand-cycle | GA-rand-tuned | 10 | 9 | 1 | 0 | 0 | 1.547 | 0.003906 | 0.01953 | -1 | -1.763 | -2.773 | -0.5469 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 10x10 | GA-rand-cycle | GA-cost-tuned | 10 | 8 | 1 | 1 | 0 | 1.382 | 0.007812 | 0.01953 | -0.9556 | -1.311 | -2.601 | -0.4792 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 10x10 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 1 | 0 | 0.2654 | 1.382 | 0.003906 | 0.01953 | -1 | -0.9703 | -2.04 | -0.3884 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 10x10 | GA-cost-cycle | VAM | 10 | 9 | 1 | 0 | 0.2654 | 8.377 | 0.003906 | 0.01953 | -1 | -8.835 | -17.87 | -3.324 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 20x20 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 1.766 | 22.73 | 0.001953 | 0.009766 | -1 | -20.54 | -29.49 | -11.68 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 20x20 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 1.766 | 14.03 | 0.001953 | 0.009766 | -1 | -14.57 | -19.27 | -9.564 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 20x20 | GA-rand-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 1.766 | 4.793 | 0.001953 | 0.009766 | -1 | -2.396 | -3.405 | -1.436 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 20x20 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 0.7617 | 4.793 | 0.001953 | 0.009766 | -1 | -3.388 | -4.415 | -2.528 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 20x20 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 0.7617 | 22.73 | 0.001953 | 0.009766 | -1 | -21.02 | -29.94 | -12.18 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 30x30 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 6.98 | 25.62 | 0.001953 | 0.009766 | -1 | -18.64 | -25.44 | -11.29 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 30x30 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 6.98 | 33.57 | 0.001953 | 0.009766 | -1 | -27.09 | -30.56 | -23.92 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 30x30 | GA-rand-cycle | GA-cost-tuned | 10 | 3 | 0 | 7 | 6.98 | 5.636 | 0.2754 | 0.2754 | 0.4182 | 1.137 | -0.9015 | 2.691 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 30x30 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 2.703 | 5.636 | 0.003906 | 0.009766 | -0.9636 | -2.991 | -4.457 | -1.836 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 30x30 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 2.703 | 25.62 | 0.001953 | 0.009766 | -1 | -22.11 | -28.77 | -16.3 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 50x50 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 11.87 | 31.47 | 0.001953 | 0.009766 | -1 | -19.95 | -35.86 | -8.969 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 50x50 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 11.87 | 55.2 | 0.001953 | 0.009766 | -1 | -43.44 | -46.33 | -40.42 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 50x50 | GA-rand-cycle | GA-cost-tuned | 10 | 3 | 0 | 7 | 11.87 | 11.86 | 0.4316 | 0.4316 | 0.3091 | 1.115 | -1.392 | 2.746 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 50x50 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 7.31 | 11.86 | 0.001953 | 0.009766 | -1 | -4.2 | -5.524 | -2.767 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 50x50 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 7.31 | 31.47 | 0.001953 | 0.009766 | -1 | -25.49 | -39.59 | -13.7 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 100x100 | GA-rand-cycle | VAM | 10 | 8 | 0 | 2 | 33.23 | 41.7 | 0.01367 | 0.01367 | -0.8545 | -7.747 | -14.81 | -1.812 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 100x100 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 33.23 | 111.3 | 0.001953 | 0.009766 | -1 | -75.88 | -80.8 | -70.16 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 100x100 | GA-rand-cycle | GA-cost-tuned | 10 | 0 | 0 | 10 | 33.23 | 21.24 | 0.001953 | 0.009766 | 1 | 14.14 | 11.19 | 17.04 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 100x100 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 14.56 | 21.24 | 0.001953 | 0.009766 | -1 | -6.329 | -7.565 | -4.778 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | uniform 100x100 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 14.56 | 41.7 | 0.001953 | 0.009766 | -1 | -28.51 | -33.53 | -23.42 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | structured 20x20 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 0.2483 | 8.357 | 0.001953 | 0.009766 | -1 | -8.055 | -12.55 | -6.578 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | structured 20x20 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 0.2483 | 1.522 | 0.001953 | 0.009766 | -1 | -1.244 | -1.806 | -0.6643 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | structured 20x20 | GA-rand-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 0.2483 | 0.9751 | 0.003906 | 0.009766 | -0.9636 | -0.534 | -0.7923 | -0.2458 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | structured 20x20 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 0.3373 | 0.9751 | 0.005859 | 0.009766 | -0.9273 | -0.4051 | -0.6914 | -0.1367 | exact Walsh-average CI |
| 8.6 linear (T2_tests) | structured 20x20 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 0.3373 | 8.357 | 0.001953 | 0.009766 | -1 | -7.977 | -12.49 | -6.197 | exact Walsh-average CI |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | VAM | 5 | 3 | 0 | 2 | 30.81 | 36.13 | 0.3125 | 0.3125 | -0.6 | -7.747 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-rand-tuned | 5 | 5 | 0 | 0 | 30.81 | 110.8 | 0.0625 | 0.3125 | -1 | -77.17 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-cost-tuned | 5 | 0 | 0 | 5 | 30.81 | 17.96 | 0.0625 | 0.3125 | 1 | 13.84 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | GA-cost-tuned | 5 | 5 | 0 | 0 | 10.4 | 17.96 | 0.0625 | 0.3125 | -1 | -7.045 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | VAM | 5 | 5 | 0 | 0 | 10.4 | 36.13 | 0.0625 | 0.3125 | -1 | -28.65 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | VAM | 5 | 5 | 0 | 0 | 36.63 | 43.84 | 0.0625 | 0.3125 | -1 | -7.504 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-rand-tuned | 5 | 5 | 0 | 0 | 36.63 | 113 | 0.0625 | 0.3125 | -1 | -72.53 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-cost-tuned | 5 | 0 | 0 | 5 | 36.63 | 22.42 | 0.0625 | 0.3125 | 1 | 14.1 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | GA-cost-tuned | 5 | 5 | 0 | 0 | 15.89 | 22.42 | 0.0625 | 0.3125 | -1 | -6.262 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | VAM | 5 | 5 | 0 | 0 | 15.89 | 43.84 | 0.0625 | 0.3125 | -1 | -28.51 | – | – | exact Walsh-average CI (too few pairs for this level) |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | VAM | 10 | 8 | 0 | 2 | 33.23 | 41.7 | 0.01367 | 0.01367 | -0.8545 | -7.747 | -14.81 | -1.812 | exact Walsh-average CI |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 33.23 | 111.3 | 0.001953 | 0.009766 | -1 | -75.88 | -80.8 | -70.16 | exact Walsh-average CI |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-rand-cycle | GA-cost-tuned | 10 | 0 | 0 | 10 | 33.23 | 21.24 | 0.001953 | 0.009766 | 1 | 14.14 | 11.19 | 17.04 | exact Walsh-average CI |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 14.56 | 21.24 | 0.001953 | 0.009766 | -1 | -6.329 | -7.565 | -4.778 | exact Walsh-average CI |
| 9.1 linear 100x100 (T2_tests_extension) | uniform 100x100 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 14.56 | 41.7 | 0.001953 | 0.009766 | -1 | -28.51 | -33.53 | -23.42 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | all instances | GA-hybrid | Balinski | 40 | 38 | 1 | 1 | 2.848 | 12.27 | 7.276e-12 | 2.91e-11 | -0.9974 | -9.271 | -11.59 | -7.366 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | all instances | GA-hybrid | GA-rand-tuned | 40 | 38 | 1 | 1 | 2.848 | 15.22 | 7.276e-12 | 2.91e-11 | -0.9974 | -13.03 | -16.45 | -9.602 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | all instances | GA-rand-cycle | Balinski | 40 | 25 | 1 | 14 | 7.834 | 12.27 | 0.01615 | 0.01615 | -0.4385 | -3.162 | -5.519 | -0.5128 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | all instances | GA-rand-cycle | GA-rand-tuned | 40 | 38 | 0 | 2 | 7.834 | 15.22 | 9.095e-12 | 2.91e-11 | -0.9927 | -6.414 | -7.999 | -4.79 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 0.2 | GA-hybrid | Balinski | 20 | 19 | 0 | 1 | 2.116 | 7.484 | 3.815e-06 | 1.526e-05 | -0.9905 | -5.718 | -7.085 | -4.042 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 0.2 | GA-hybrid | GA-rand-tuned | 20 | 18 | 1 | 1 | 2.116 | 13.47 | 7.629e-06 | 2.289e-05 | -0.9895 | -11.95 | -16.7 | -7.797 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 0.2 | GA-rand-cycle | Balinski | 20 | 11 | 0 | 9 | 7.344 | 7.484 | 0.5706 | 0.5706 | -0.1524 | -0.6156 | -3.431 | 2.522 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 0.2 | GA-rand-cycle | GA-rand-tuned | 20 | 18 | 0 | 2 | 7.344 | 13.47 | 9.537e-06 | 2.289e-05 | -0.9714 | -6.237 | -8.406 | -3.698 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 1 | GA-hybrid | Balinski | 20 | 19 | 1 | 0 | 3.341 | 17.85 | 3.815e-06 | 7.629e-06 | -1 | -13.64 | -16.67 | -10.96 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 1 | GA-hybrid | GA-rand-tuned | 20 | 20 | 0 | 0 | 3.341 | 15.22 | 1.907e-06 | 7.629e-06 | -1 | -15.18 | -19.2 | -8.847 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 1 | GA-rand-cycle | Balinski | 20 | 14 | 1 | 5 | 9.333 | 17.85 | 0.003918 | 0.003918 | -0.7263 | -5.625 | -10.23 | -2.091 | exact Walsh-average CI |
| 8.4 FCTP (F3_tests) | rho = 1 | GA-rand-cycle | GA-rand-tuned | 20 | 20 | 0 | 0 | 9.333 | 15.22 | 1.907e-06 | 7.629e-06 | -1 | -6.747 | -8.898 | -4.358 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | all instances | GA-cost-cycle-ft | GA-cost-cycle | 40 | 19 | 3 | 18 | 2.652 | 2.66 | 0.7204 | 1 | -0.0697 | -0.09734 | -0.5436 | 0.4246 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | all instances | GA-hybrid-ft | GA-cost-cycle-ft | 40 | 11 | 11 | 18 | 2.391 | 2.652 | 0.7172 | 1 | 0.08046 | 0.01171 | -0.1341 | 0.2882 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | all instances | GA-hybrid-ft | GA-hybrid | 40 | 20 | 4 | 16 | 2.391 | 2.848 | 0.414 | 1 | -0.1592 | -0.1526 | -0.5856 | 0.2336 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 0.2 | GA-cost-cycle-ft | GA-cost-cycle | 20 | 10 | 2 | 8 | 1.596 | 1.825 | 0.3465 | 0.6364 | -0.2632 | -0.1872 | -0.7288 | 0.2381 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 0.2 | GA-hybrid-ft | GA-cost-cycle-ft | 20 | 4 | 7 | 9 | 1.596 | 1.596 | 0.3054 | 0.6364 | 0.3407 | 0.05623 | -0.0923 | 0.4702 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 0.2 | GA-hybrid-ft | GA-hybrid | 20 | 11 | 2 | 7 | 1.596 | 2.116 | 0.2121 | 0.6364 | -0.345 | -0.1839 | -0.5839 | 0.1614 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 1 | GA-cost-cycle-ft | GA-cost-cycle | 20 | 9 | 1 | 10 | 3.89 | 2.956 | 0.7086 | 1 | 0.1053 | 0.2101 | -0.8037 | 1.14 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 1 | GA-hybrid-ft | GA-cost-cycle-ft | 20 | 7 | 4 | 9 | 4.143 | 3.89 | 0.7436 | 1 | -0.1029 | 0 | -0.6009 | 0.3554 | exact Walsh-average CI |
| 9.2 FCTP tuned (E3_tests_tuned) | rho = 1 | GA-hybrid-ft | GA-hybrid | 20 | 9 | 2 | 9 | 4.143 | 3.341 | 0.865 | 1 | -0.05263 | -0.05949 | -0.8819 | 0.8159 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | all instances | GA-cost-cycle | MIP-60s | 20 | 0 | 0 | 20 | 10.23 | 0 | 1.907e-06 | 5.722e-06 | 1 | 9.648 | 8.111 | 11.08 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | all instances | GA-cost-cycle-ft | MIP-60s | 20 | 0 | 0 | 20 | 7.622 | 0 | 1.907e-06 | 5.722e-06 | 1 | 7.845 | 6.761 | 9.325 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | all instances | GA-hybrid-ft | MIP-60s | 20 | 0 | 0 | 20 | 10.68 | 0 | 1.907e-06 | 5.722e-06 | 1 | 10.3 | 8.821 | 11.59 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 50x50 | GA-cost-cycle | MIP-60s | 10 | 0 | 0 | 10 | 10.94 | 0 | 0.001953 | 0.005859 | 1 | 9.642 | 7.294 | 11.91 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 50x50 | GA-cost-cycle-ft | MIP-60s | 10 | 0 | 0 | 10 | 7.605 | 0 | 0.001953 | 0.005859 | 1 | 7.635 | 5.787 | 9.62 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 50x50 | GA-hybrid-ft | MIP-60s | 10 | 0 | 0 | 10 | 9.913 | 0 | 0.001953 | 0.005859 | 1 | 9.577 | 7.181 | 11.64 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 70x70 | GA-cost-cycle | MIP-60s | 10 | 0 | 0 | 10 | 9.511 | 0 | 0.001953 | 0.005859 | 1 | 9.534 | 7.465 | 11.51 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 70x70 | GA-cost-cycle-ft | MIP-60s | 10 | 0 | 0 | 10 | 8.06 | 0 | 0.001953 | 0.005859 | 1 | 8.512 | 6.656 | 9.923 | exact Walsh-average CI |
| 9.4 FCTP large (E7_large_tests) | size 70x70 | GA-hybrid-ft | MIP-60s | 10 | 0 | 0 | 10 | 11.48 | 0 | 0.001953 | 0.005859 | 1 | 11.04 | 9.014 | 12.58 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | all instances | GA-cost-cycle | Tabu | 60 | 6 | 3 | 51 | 4.865 | 2.008 | 1.942e-09 | 1.942e-09 | 0.9141 | 3.4 | 2.39 | 4.338 | normal-approximation Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | all instances | GA-cost-cycle | ILS | 60 | 2 | 3 | 55 | 4.865 | 0.9192 | 6.711e-11 | 1.342e-10 | 0.994 | 4.701 | 3.41 | 5.727 | normal-approximation Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | rho = 0.2 | GA-cost-cycle | Tabu | 30 | 2 | 1 | 27 | 4.005 | 1.329 | 2.049e-07 | 2.049e-07 | 0.9494 | 2.853 | 1.56 | 4.254 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | rho = 0.2 | GA-cost-cycle | ILS | 30 | 0 | 2 | 28 | 4.005 | 0.5839 | 7.451e-09 | 1.49e-08 | 1 | 4.038 | 2.385 | 5.5 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | rho = 1 | GA-cost-cycle | Tabu | 30 | 4 | 2 | 24 | 5.625 | 2.513 | 3.994e-06 | 3.994e-06 | 0.8916 | 3.804 | 2.392 | 5.168 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | rho = 1 | GA-cost-cycle | ILS | 30 | 2 | 1 | 27 | 5.625 | 1.318 | 3.725e-08 | 7.451e-08 | 0.977 | 5.273 | 3.461 | 6.708 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 10x10 | GA-cost-cycle | Tabu | 10 | 3 | 2 | 5 | 0.963 | 0.8222 | 0.7422 | 0.7422 | 0.1667 | 0.03405 | -0.3022 | 1.064 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 10x10 | GA-cost-cycle | ILS | 10 | 0 | 2 | 8 | 0.963 | 0 | 0.007812 | 0.01562 | 1 | 1.043 | 0.4211 | 1.94 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 15x15 | GA-cost-cycle | Tabu | 10 | 3 | 1 | 6 | 1.213 | 0.9951 | 0.4258 | 0.4258 | 0.3333 | 0.4072 | -0.6131 | 1.458 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 15x15 | GA-cost-cycle | ILS | 10 | 2 | 1 | 7 | 1.213 | 0 | 0.03906 | 0.07812 | 0.7778 | 1.108 | 0.01375 | 2.222 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 20x20 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 2.785 | 1.254 | 0.001953 | 0.003906 | 1 | 1.255 | 0.7597 | 2.98 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 20x20 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 2.785 | 0.328 | 0.001953 | 0.003906 | 1 | 2.316 | 1.63 | 3.692 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 30x30 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 6.362 | 1.872 | 0.001953 | 0.003906 | 1 | 4.412 | 3.475 | 5.818 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 30x30 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 6.362 | 1.013 | 0.001953 | 0.003906 | 1 | 4.954 | 4.23 | 6.455 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 50x50 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 10.95 | 3.873 | 0.001953 | 0.003906 | 1 | 7.1 | 5.013 | 8.41 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 50x50 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 10.95 | 1.799 | 0.001953 | 0.003906 | 1 | 8.994 | 7.208 | 10.24 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 70x70 | GA-cost-cycle | Tabu | 10 | 0 | 0 | 10 | 11.28 | 3.964 | 0.001953 | 0.003906 | 1 | 7.083 | 5.651 | 9.185 | exact Walsh-average CI |
| 10.1 FCTP rivals (R3_tests) | size 70x70 | GA-cost-cycle | ILS | 10 | 0 | 0 | 10 | 11.28 | 1.365 | 0.001953 | 0.003906 | 1 | 9.65 | 8.042 | 11.35 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 0.05 | GA-cost-cycle | Tabu | 15 | 0 | 1 | 14 | 4.045 | 0.4931 | 0.0001221 | 0.0002441 | 1 | 3.341 | 1.649 | 5.073 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 0.05 | GA-cost-cycle | ILS | 15 | 0 | 1 | 14 | 4.045 | 0.1567 | 0.0001221 | 0.0002441 | 1 | 3.844 | 2.022 | 5.63 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 0.2 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 5.785 | 2.004 | 6.104e-05 | 0.0001221 | 1 | 3.496 | 1.692 | 5.34 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 0.2 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 5.785 | 0.9709 | 6.104e-05 | 0.0001221 | 1 | 4.512 | 2.853 | 6.405 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 1 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 7.337 | 2.586 | 6.104e-05 | 0.0001221 | 1 | 4.989 | 3.363 | 6.612 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 1 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 7.337 | 1.577 | 6.104e-05 | 0.0001221 | 1 | 6.266 | 4.184 | 7.968 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 5 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 9.941 | 2.666 | 6.104e-05 | 0.0001221 | 1 | 7.193 | 5.364 | 9.829 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | uniform, rho = 5 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 9.941 | 1.192 | 6.104e-05 | 0.0001221 | 1 | 8.879 | 6.675 | 11.64 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 0.05 | GA-cost-cycle | Tabu | 15 | 1 | 0 | 14 | 0.7348 | 0.06936 | 0.0001221 | 0.0001221 | 0.9833 | 1.36 | 0.3119 | 2.362 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 0.05 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 0.7348 | 0.01574 | 6.104e-05 | 0.0001221 | 1 | 1.44 | 0.3486 | 2.392 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 0.2 | GA-cost-cycle | Tabu | 15 | 2 | 0 | 13 | 1.177 | 0.5356 | 0.0006104 | 0.0006104 | 0.9167 | 1.432 | 0.4228 | 2.601 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 0.2 | GA-cost-cycle | ILS | 15 | 0 | 1 | 14 | 1.177 | 0.09703 | 0.0001221 | 0.0002441 | 1 | 1.789 | 0.7177 | 2.849 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 1 | GA-cost-cycle | Tabu | 15 | 2 | 0 | 13 | 2.692 | 1.348 | 0.002014 | 0.002014 | 0.85 | 1.109 | 0.5557 | 1.941 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 1 | GA-cost-cycle | ILS | 15 | 1 | 0 | 14 | 2.692 | 0.8335 | 0.0001831 | 0.0003662 | 0.9667 | 1.572 | 0.9596 | 2.335 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 5 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 5.211 | 2.48 | 6.104e-05 | 0.0001221 | 1 | 3.043 | 1.724 | 4.199 | exact Walsh-average CI |
| 10.3 FCTP classes (R5_generator_tests) | concentrated, rho = 5 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 5.211 | 2.239 | 6.104e-05 | 0.0001221 | 1 | 3.285 | 1.989 | 4.585 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 5x5 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 0 | 10 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 5x5 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 0 | 10 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 10x10 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 2 | 5 | 3 | 0 | 0 | 1 | 1 | 0.06667 | 0 | -0.4127 | 0.4419 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 10x10 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 5 | 4 | 1 | 0.1464 | 0.2654 | 0.0625 | 0.125 | -0.9048 | -0.1156 | -0.2677 | 0 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 20x20 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 3 | 0 | 7 | 2.813 | 1.766 | 0.3223 | 0.5 | 0.3818 | 0.6361 | -0.7347 | 1.525 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 20x20 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 5 | 1 | 4 | 0.6956 | 0.7617 | 0.25 | 0.5 | -0.4667 | -0.1014 | -0.5598 | 0.05185 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 30x30 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 2 | 0 | 8 | 8.241 | 6.98 | 0.02734 | 0.05469 | 0.7818 | 2.239 | 0.2127 | 3.328 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 30x30 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 8 | 0 | 2 | 1.943 | 2.703 | 0.03711 | 0.05469 | -0.7455 | -0.5106 | -1.01 | -0.02545 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 50x50 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 0 | 0 | 10 | 21.17 | 11.87 | 0.001953 | 0.003906 | 1 | 9.1 | 6.336 | 11.86 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | uniform 50x50 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 10 | 0 | 0 | 4.262 | 7.31 | 0.001953 | 0.003906 | -1 | -3.202 | -4.607 | -2.197 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | structured 20x20 | GA-rand-cycle-nd | GA-rand-cycle | 10 | 3 | 0 | 7 | 0.3647 | 0.2483 | 0.1309 | 0.2617 | 0.5636 | 0.09728 | -0.02923 | 0.2648 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | structured 20x20 | GA-cost-cycle-nd | GA-cost-cycle | 10 | 6 | 1 | 3 | 0.3317 | 0.3373 | 0.5703 | 0.5703 | -0.2444 | -0.00719 | -0.2438 | 0.109 | exact Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | all instances | GA-rand-cycle-nd | GA-rand-cycle | 60 | 10 | 15 | 35 | 0.7523 | 0.5443 | 2.093e-05 | 2.093e-05 | 0.6908 | 0.8955 | 0.1572 | 1.768 | normal-approximation Walsh-average CI |
| 10.5 entering rule (R9_entering_tests) | all instances | GA-cost-cycle-nd | GA-cost-cycle | 60 | 34 | 16 | 10 | 0.503 | 0.6451 | 4.149e-06 | 8.299e-06 | -0.7455 | -0.2497 | -0.606 | -0.07572 | normal-approximation Walsh-average CI |
