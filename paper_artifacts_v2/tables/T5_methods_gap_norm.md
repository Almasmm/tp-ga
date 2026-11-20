# Paired method comparisons, normalised gap

Unit: per-instance median over seeds (10 instances per set and size). Wilcoxon signed-rank test (exact for n <= 50 without ties, normal approximation otherwise), Holm correction within each (set, size). hl_shift = Hodges-Lehmann estimate of method_a minus method_b in percentage points of gap, with a 95 % CI. p < 0.001 is printed as "< 0.001".

| set | size | method_a | method_b | value | n | nonzero | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_method | wins_x | wins_y | ties | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 200x200 | GA-rand-tuned | VAM | gap_norm | 7 | 7 | 0 | 0.016 | 1.000 | 0.040 | 0.036 | 0.044 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | GA-cost-tuned | VAM | gap_norm | 7 | 7 | 0 | 0.016 | -1.000 | -0.005 | -0.012 | -0.004 | exact Walsh-average CI | 7 | 0 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-rand-tuned | VAM | gap_norm | 7 | 7 | 0 | 0.016 | 1.000 | 0.151 | 0.140 | 0.161 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-rand-tuned | GA-rand-tuned | gap_norm | 7 | 7 | 0 | 0.016 | 1.000 | 0.110 | 0.101 | 0.120 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-cost-tuned | GA-cost-tuned | gap_norm | 7 | 7 | 0 | 0.016 | 1.000 | 0.002 | 9.589e-04 | 0.003 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
