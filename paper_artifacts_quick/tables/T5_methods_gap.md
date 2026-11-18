# Paired method comparisons, gap

Unit: per-instance median over seeds (10 instances per set and size). Wilcoxon signed-rank test (exact for n <= 50 without ties, normal approximation otherwise), Holm correction within each (set, size). hl_shift = Hodges-Lehmann estimate of method_a minus method_b in percentage points of gap, with a 95 % CI. p < 0.001 is printed as "< 0.001".

| set | size | method_a | method_b | value | n | nonzero | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_method | wins_x | wins_y | ties | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | GA-rand-tuned | VAM | gap | 10 | 5 | 0 | 0.062 | -1.000 | -1.147 | -8.798 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | GA-cost-tuned | VAM | gap | 10 | 5 | 0 | 0.062 | -1.000 | -1.147 | -8.798 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | SA-rand-tuned | VAM | gap | 10 | 5 | 0 | 0.062 | -1.000 | -1.489 | -8.798 | 0 | exact Walsh-average CI | 5 | 0 | 5 | 0.312 | 0.312 |
| uniform | 5x5 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 1 | 0 | 1.000 | -1.000 | 0 | -0.350 | 0 | exact Walsh-average CI | 1 | 0 | 9 | 1.000 | 1.000 |
| uniform | 5x5 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 2 | 0 | 0.500 | -1.000 | 0 | -0.698 | 0 | exact Walsh-average CI | 2 | 0 | 8 | 1.000 | 1.000 |
| uniform | 10x10 | GA-rand-tuned | VAM | gap | 10 | 10 | 1.000 | 0.004 | -0.964 | -7.519 | -15.838 | -3.070 | exact Walsh-average CI | 9 | 1 | 0 | 0.020 | 0.020 |
| uniform | 10x10 | GA-cost-tuned | VAM | gap | 10 | 9 | 0 | 0.004 | -1.000 | -7.614 | -17.480 | -2.410 | exact Walsh-average CI | 9 | 0 | 1 | 0.020 | 0.020 |
| uniform | 10x10 | SA-rand-tuned | VAM | gap | 10 | 10 | 1.000 | 0.004 | -0.964 | -8.684 | -16.805 | -3.380 | exact Walsh-average CI | 9 | 1 | 0 | 0.020 | 0.020 |
| uniform | 10x10 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 7 | 2.000 | 0.047 | -0.857 | -0.792 | -1.730 | 0 | exact Walsh-average CI | 6 | 1 | 3 | 0.047 | 0.047 |
| uniform | 10x10 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 9 | 0 | 0.004 | -1.000 | -0.990 | -2.137 | -0.479 | exact Walsh-average CI | 9 | 0 | 1 | 0.020 | 0.020 |
| uniform | 20x20 | GA-rand-tuned | VAM | gap | 10 | 10 | 11.000 | 0.105 | -0.600 | -5.309 | -12.209 | 0.905 | exact Walsh-average CI | 8 | 2 | 0 | 0.422 | 0.422 |
| uniform | 20x20 | GA-cost-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -17.932 | -26.331 | -9.376 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 20x20 | SA-rand-tuned | VAM | gap | 10 | 10 | 11.000 | 0.105 | -0.600 | -7.940 | -16.466 | 1.264 | exact Walsh-average CI | 7 | 3 | 0 | 0.422 | 0.422 |
| uniform | 20x20 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 10 | 15.000 | 0.232 | -0.455 | -2.025 | -6.486 | 1.663 | exact Walsh-average CI | 7 | 3 | 0 | 0.465 | 0.465 |
| uniform | 20x20 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 10 | 15.000 | 0.232 | 0.455 | 0.678 | -0.618 | 1.916 | exact Walsh-average CI | 5 | 5 | 0 | 0.465 | 0.465 |
| uniform | 30x30 | GA-rand-tuned | VAM | gap | 10 | 10 | 8.000 | 0.049 | 0.709 | 8.664 | 0.650 | 17.351 | exact Walsh-average CI | 3 | 7 | 0 | 0.146 | 0.146 |
| uniform | 30x30 | GA-cost-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -19.626 | -25.124 | -11.591 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 30x30 | SA-rand-tuned | VAM | gap | 10 | 10 | 11.000 | 0.105 | 0.600 | 7.729 | -1.168 | 15.680 | exact Walsh-average CI | 2 | 8 | 0 | 0.211 | 0.211 |
| uniform | 30x30 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 10 | 19.000 | 0.432 | -0.309 | -1.630 | -4.268 | 1.646 | exact Walsh-average CI | 5 | 5 | 0 | 0.432 | 0.432 |
| uniform | 30x30 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 10 | 1.000 | 0.004 | 0.964 | 2.995 | 0.955 | 5.002 | exact Walsh-average CI | 1 | 9 | 0 | 0.016 | 0.016 |
| uniform | 50x50 | GA-rand-tuned | VAM | gap | 10 | 10 | 5.000 | 0.020 | 0.818 | 24.155 | 4.790 | 33.626 | exact Walsh-average CI | 2 | 8 | 0 | 0.020 | 0.020 |
| uniform | 50x50 | GA-cost-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -22.489 | -35.084 | -11.021 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-rand-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | 1.000 | 55.530 | 35.318 | 61.135 | exact Walsh-average CI | 0 | 10 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 10 | 0 | 0.002 | 1.000 | 30.524 | 26.692 | 33.886 | exact Walsh-average CI | 0 | 10 | 0 | 0.010 | 0.010 |
| uniform | 50x50 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 10 | 2.000 | 0.006 | 0.927 | 2.849 | 1.384 | 5.605 | exact Walsh-average CI | 1 | 9 | 0 | 0.012 | 0.012 |
| structured | 20x20 | GA-rand-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -6.544 | -11.860 | -5.296 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | GA-cost-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -7.309 | -12.249 | -5.870 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | SA-rand-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -6.929 | -11.560 | -5.316 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | 20x20 | SA-rand-tuned | GA-rand-tuned | gap | 10 | 10 | 19.000 | 0.432 | -0.309 | -0.194 | -0.702 | 0.225 | exact Walsh-average CI | 6 | 4 | 0 | 0.432 | 0.432 |
| structured | 20x20 | SA-cost-tuned | GA-cost-tuned | gap | 10 | 10 | 3.000 | 0.010 | -0.891 | -0.388 | -0.650 | -0.133 | exact Walsh-average CI | 8 | 2 | 0 | 0.020 | 0.020 |
