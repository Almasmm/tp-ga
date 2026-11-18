# Paired method comparisons, normalised gap

Unit: per-instance median over seeds (10 instances per set and size). Wilcoxon signed-rank test (exact for n <= 50 without ties, normal approximation otherwise), Holm correction within each (set, size). hl_shift = Hodges-Lehmann estimate of method_a minus method_b in percentage points of gap, with a 95 % CI. p < 0.001 is printed as "< 0.001".

| set | size | method_a | method_b | value | n | nonzero | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_method | wins_x | wins_y | ties | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | GA-rand-tuned | VAM | gap_norm | 10 | 5 | 0 | 0.062 | -1.000 | -0.019 | -0.075 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | GA-cost-tuned | VAM | gap_norm | 10 | 5 | 0 | 0.062 | -1.000 | -0.010 | -0.075 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | SA-rand-tuned | VAM | gap_norm | 10 | 5 | 0 | 0.062 | -1.000 | -0.019 | -0.075 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 1 | 0 | 1.000 | -1.000 | 0 | -0.001 | 0 | exact Walsh-average CI | 1 | 0 | 9 | 1.000 | 1.000 |
| uniform | 5x5 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 2 | 0 | 0.500 | -1.000 | 0 | -0.010 | 0 | exact Walsh-average CI | 2 | 0 | 8 | 1.000 | 1.000 |
| uniform | 10x10 | GA-rand-tuned | VAM | gap_norm | 10 | 10 | 1.000 | 0.004 | -0.964 | -0.036 | -0.074 | -0.013 | exact Walsh-average CI | 9 | 1 | 0 | 0.020 | 0.020 |
| uniform | 10x10 | GA-cost-tuned | VAM | gap_norm | 10 | 9 | 0 | 0.004 | -1.000 | -0.035 | -0.079 | -0.011 | exact Walsh-average CI | 9 | 0 | 1 | 0.020 | 0.020 |
| uniform | 10x10 | SA-rand-tuned | VAM | gap_norm | 10 | 10 | 1.000 | 0.004 | -0.964 | -0.040 | -0.078 | -0.015 | exact Walsh-average CI | 9 | 1 | 0 | 0.020 | 0.020 |
| uniform | 10x10 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 7 | 2.000 | 0.047 | -0.857 | -0.004 | -0.008 | 0 | exact Walsh-average CI | 6 | 1 | 3 | 0.047 | 0.047 |
| uniform | 10x10 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 9 | 0 | 0.004 | -1.000 | -0.005 | -0.012 | -0.002 | exact Walsh-average CI | 9 | 0 | 1 | 0.020 | 0.020 |
| uniform | 20x20 | GA-rand-tuned | VAM | gap_norm | 10 | 10 | 11.000 | 0.105 | -0.600 | -0.011 | -0.025 | 0.003 | exact Walsh-average CI | 8 | 2 | 0 | 0.422 | 0.422 |
| uniform | 20x20 | GA-cost-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.033 | -0.049 | -0.019 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 20x20 | SA-rand-tuned | VAM | gap_norm | 10 | 10 | 12.000 | 0.131 | -0.564 | -0.015 | -0.032 | 0.003 | exact Walsh-average CI | 7 | 3 | 0 | 0.422 | 0.422 |
| uniform | 20x20 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 10 | 17.000 | 0.322 | -0.382 | -0.004 | -0.011 | 0.004 | exact Walsh-average CI | 7 | 3 | 0 | 0.465 | 0.465 |
| uniform | 20x20 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 10 | 15.000 | 0.232 | 0.455 | 0.001 | -0.001 | 0.004 | exact Walsh-average CI | 5 | 5 | 0 | 0.465 | 0.465 |
| uniform | 30x30 | GA-rand-tuned | VAM | gap_norm | 10 | 10 | 9.000 | 0.064 | 0.673 | 0.012 | -1.906e-04 | 0.023 | exact Walsh-average CI | 3 | 7 | 0 | 0.193 | 0.193 |
| uniform | 30x30 | GA-cost-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.029 | -0.038 | -0.016 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 30x30 | SA-rand-tuned | VAM | gap_norm | 10 | 10 | 11.000 | 0.105 | 0.600 | 0.009 | -0.003 | 0.021 | exact Walsh-average CI | 2 | 8 | 0 | 0.211 | 0.211 |
| uniform | 30x30 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 10 | 18.000 | 0.375 | -0.345 | -0.002 | -0.006 | 0.002 | exact Walsh-average CI | 5 | 5 | 0 | 0.375 | 0.375 |
| uniform | 30x30 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 10 | 1.000 | 0.004 | 0.964 | 0.004 | 0.001 | 0.007 | exact Walsh-average CI | 1 | 9 | 0 | 0.016 | 0.016 |
| uniform | 50x50 | GA-rand-tuned | VAM | gap_norm | 10 | 10 | 6.000 | 0.027 | 0.782 | 0.021 | 0.003 | 0.031 | exact Walsh-average CI | 2 | 8 | 0 | 0.027 | 0.027 |
| uniform | 50x50 | GA-cost-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.020 | -0.032 | -0.010 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-rand-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | 1.000 | 0.048 | 0.030 | 0.056 | exact Walsh-average CI | 0 | 10 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 10 | 0 | 0.002 | 1.000 | 0.027 | 0.024 | 0.030 | exact Walsh-average CI | 0 | 10 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 10 | 2.000 | 0.006 | 0.927 | 0.003 | 0.001 | 0.005 | exact Walsh-average CI | 1 | 9 | 0 | 0.012 | 0.012 |
| structured | 20x20 | GA-rand-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.054 | -0.079 | -0.037 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | GA-cost-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.062 | -0.083 | -0.043 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | SA-rand-tuned | VAM | gap_norm | 10 | 10 | 0 | 0.002 | -1.000 | -0.059 | -0.080 | -0.040 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | SA-rand-tuned | GA-rand-tuned | gap_norm | 10 | 10 | 17.000 | 0.322 | -0.382 | -0.001 | -0.006 | 0.001 | exact Walsh-average CI | 6 | 4 | 0 | 0.322 | 0.322 |
| structured | 20x20 | SA-cost-tuned | GA-cost-tuned | gap_norm | 10 | 10 | 3.000 | 0.010 | -0.891 | -0.003 | -0.006 | -0.001 | exact Walsh-average CI | 8 | 2 | 0 | 0.020 | 0.020 |
