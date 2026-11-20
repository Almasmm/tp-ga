# FCTP: GA-cost-cycle against Tabu and ILS on the instance classes

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). As R3_tests; one scope per class and rho (the three sizes together), Holm over the two pairs.

| scope | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_ci_method | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform, rho = 0.05 | GA-cost-cycle | Tabu | 15 | 0 | 1 | 14 | 4.045 | 0.4931 | 0 | 0.0001221 | 1 | 3.341 | 1.649 | 5.073 | exact Walsh-average CI | 6.104e-05 | 0.0002441 | < 0.001 |
| uniform, rho = 0.05 | GA-cost-cycle | ILS | 15 | 0 | 1 | 14 | 4.045 | 0.1567 | 0 | 0.0001221 | 1 | 3.844 | 2.022 | 5.63 | exact Walsh-average CI | 6.104e-05 | 0.0002441 | < 0.001 |
| uniform, rho = 0.2 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 5.785 | 2.004 | 0 | 6.104e-05 | 1 | 3.496 | 1.692 | 5.34 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| uniform, rho = 0.2 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 5.785 | 0.9709 | 0 | 6.104e-05 | 1 | 4.512 | 2.853 | 6.405 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| uniform, rho = 1 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 7.337 | 2.586 | 0 | 6.104e-05 | 1 | 4.989 | 3.363 | 6.612 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| uniform, rho = 1 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 7.337 | 1.577 | 0 | 6.104e-05 | 1 | 6.266 | 4.184 | 7.968 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| uniform, rho = 5 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 9.941 | 2.666 | 0 | 6.104e-05 | 1 | 7.193 | 5.364 | 9.829 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| uniform, rho = 5 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 9.941 | 1.192 | 0 | 6.104e-05 | 1 | 8.879 | 6.675 | 11.64 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| concentrated, rho = 0.05 | GA-cost-cycle | Tabu | 15 | 1 | 0 | 14 | 0.7348 | 0.06936 | 1 | 0.0001221 | 0.9833 | 1.36 | 0.3119 | 2.362 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| concentrated, rho = 0.05 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 0.7348 | 0.01574 | 0 | 6.104e-05 | 1 | 1.44 | 0.3486 | 2.392 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| concentrated, rho = 0.2 | GA-cost-cycle | Tabu | 15 | 2 | 0 | 13 | 1.177 | 0.5356 | 5 | 0.0006104 | 0.9167 | 1.432 | 0.4228 | 2.601 | exact Walsh-average CI | 6.104e-05 | 0.0006104 | < 0.001 |
| concentrated, rho = 0.2 | GA-cost-cycle | ILS | 15 | 0 | 1 | 14 | 1.177 | 0.09703 | 0 | 0.0001221 | 1 | 1.789 | 0.7177 | 2.849 | exact Walsh-average CI | 6.104e-05 | 0.0002441 | < 0.001 |
| concentrated, rho = 1 | GA-cost-cycle | Tabu | 15 | 2 | 0 | 13 | 2.692 | 1.348 | 9 | 0.002014 | 0.85 | 1.109 | 0.5557 | 1.941 | exact Walsh-average CI | 6.104e-05 | 0.002014 | 0.002 |
| concentrated, rho = 1 | GA-cost-cycle | ILS | 15 | 1 | 0 | 14 | 2.692 | 0.8335 | 2 | 0.0001831 | 0.9667 | 1.572 | 0.9596 | 2.335 | exact Walsh-average CI | 6.104e-05 | 0.0003662 | < 0.001 |
| concentrated, rho = 5 | GA-cost-cycle | Tabu | 15 | 0 | 0 | 15 | 5.211 | 2.48 | 0 | 6.104e-05 | 1 | 3.043 | 1.724 | 4.199 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
| concentrated, rho = 5 | GA-cost-cycle | ILS | 15 | 0 | 0 | 15 | 5.211 | 2.239 | 0 | 6.104e-05 | 1 | 3.285 | 1.989 | 4.585 | exact Walsh-average CI | 6.104e-05 | 0.0001221 | < 0.001 |
