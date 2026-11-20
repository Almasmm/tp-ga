# Paired method comparisons, gap

Unit: per-instance median over seeds (10 instances per set and size). Wilcoxon signed-rank test (exact for n <= 50 without ties, normal approximation otherwise), Holm correction within each (set, size). hl_shift = Hodges-Lehmann estimate of method_a minus method_b in percentage points of gap, with a 95 % CI. p < 0.001 is printed as "< 0.001".

| set | size | method_a | method_b | value | n | nonzero | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_method | wins_x | wins_y | ties | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 200x200 | GA-rand-tuned | VAM | gap | 7 | 7 | 0 | 0.016 | 1.000 | 132.883 | 117.857 | 149.439 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | GA-cost-tuned | VAM | gap | 7 | 7 | 0 | 0.016 | -1.000 | -17.050 | -40.780 | -13.644 | exact Walsh-average CI | 7 | 0 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-rand-tuned | VAM | gap | 7 | 7 | 0 | 0.016 | 1.000 | 501.843 | 458.906 | 534.538 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-rand-tuned | GA-rand-tuned | gap | 7 | 7 | 0 | 0.016 | 1.000 | 362.889 | 332.720 | 406.269 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
| uniform | 200x200 | SA-cost-tuned | GA-cost-tuned | gap | 7 | 7 | 0 | 0.016 | 1.000 | 6.039 | 3.271 | 8.808 | exact Walsh-average CI | 0 | 7 | 0 | 0.078 | 0.078 |
