# FCTP: paired comparisons on gap

Unit: the instance (median over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over the four pairs of each scope, rank-biserial r (negative: method_a has the smaller gap). The tests are made on all 40 instances and for each rho (20 instances), as fixed in amendment 8.6.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all instances | GA-hybrid | Balinski | 40 | 38 | 1 | 1 | 2.848 | 12.27 | 1 | 7.276e-12 | -0.9974 | -9.271 | 1.819e-12 | 2.91e-11 | < 0.001 |
| all instances | GA-hybrid | GA-rand-tuned | 40 | 38 | 1 | 1 | 2.848 | 15.22 | 1 | 7.276e-12 | -0.9974 | -13.03 | 1.819e-12 | 2.91e-11 | < 0.001 |
| all instances | GA-rand-cycle | Balinski | 40 | 25 | 1 | 14 | 7.834 | 12.27 | 219 | 0.01615 | -0.4385 | -3.162 | 1.819e-12 | 0.01615 | 0.016 |
| all instances | GA-rand-cycle | GA-rand-tuned | 40 | 38 | 0 | 2 | 7.834 | 15.22 | 3 | 9.095e-12 | -0.9927 | -6.414 | 1.819e-12 | 2.91e-11 | < 0.001 |
| rho = 0.2 | GA-hybrid | Balinski | 20 | 19 | 0 | 1 | 2.116 | 7.484 | 1 | 3.815e-06 | -0.9905 | -5.718 | 1.907e-06 | 1.526e-05 | < 0.001 |
| rho = 0.2 | GA-hybrid | GA-rand-tuned | 20 | 18 | 1 | 1 | 2.116 | 13.47 | 1 | 7.629e-06 | -0.9895 | -11.95 | 1.907e-06 | 2.289e-05 | < 0.001 |
| rho = 0.2 | GA-rand-cycle | Balinski | 20 | 11 | 0 | 9 | 7.344 | 7.484 | 89 | 0.5706 | -0.1524 | -0.6156 | 1.907e-06 | 0.5706 | 0.571 |
| rho = 0.2 | GA-rand-cycle | GA-rand-tuned | 20 | 18 | 0 | 2 | 7.344 | 13.47 | 3 | 9.537e-06 | -0.9714 | -6.237 | 1.907e-06 | 2.289e-05 | < 0.001 |
| rho = 1 | GA-hybrid | Balinski | 20 | 19 | 1 | 0 | 3.341 | 17.85 | 0 | 3.815e-06 | -1 | -13.64 | 1.907e-06 | 7.629e-06 | < 0.001 |
| rho = 1 | GA-hybrid | GA-rand-tuned | 20 | 20 | 0 | 0 | 3.341 | 15.22 | 0 | 1.907e-06 | -1 | -15.18 | 1.907e-06 | 7.629e-06 | < 0.001 |
| rho = 1 | GA-rand-cycle | Balinski | 20 | 14 | 1 | 5 | 9.333 | 17.85 | 26 | 0.003918 | -0.7263 | -5.625 | 1.907e-06 | 0.003918 | 0.004 |
| rho = 1 | GA-rand-cycle | GA-rand-tuned | 20 | 20 | 0 | 0 | 9.333 | 15.22 | 0 | 1.907e-06 | -1 | -6.747 | 1.907e-06 | 7.629e-06 | < 0.001 |
