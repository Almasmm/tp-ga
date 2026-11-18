# Linear problem: paired comparisons on gap

Unit: the instance (median over its seeds). Two-sided Wilcoxon signed-rank test, Holm correction over the five pairs of each (set, size), matched-pairs rank-biserial r (negative: method_a has the smaller gap), Hodges-Lehmann shift of gap(a) - gap(b) in percentage points. wins_a counts the instances where method_a has the smaller median gap. `smallest_possible_p` is 2 / 2^n.

| set | size | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | GA-rand-cycle | VAM | 10 | 5 | 5 | 0 | 0 | 1.067 | 0 | 0.0625 | -1 | -1.489 | 0.001953 | 0.3125 | 0.312 |
| uniform | 5x5 | GA-rand-cycle | GA-rand-tuned | 10 | 1 | 9 | 0 | 0 | 0 | 0 | 1 | -1 | 0 | 0.001953 | 1 | 1.000 |
| uniform | 5x5 | GA-rand-cycle | GA-cost-tuned | 10 | 2 | 8 | 0 | 0 | 0 | 0 | 0.5 | -1 | 0 | 0.001953 | 1 | 1.000 |
| uniform | 5x5 | GA-cost-cycle | GA-cost-tuned | 10 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0.001953 | 1 | 1.000 |
| uniform | 5x5 | GA-cost-cycle | VAM | 10 | 5 | 5 | 0 | 0 | 1.067 | 0 | 0.0625 | -1 | -1.147 | 0.001953 | 0.3125 | 0.312 |
| uniform | 10x10 | GA-rand-cycle | VAM | 10 | 9 | 1 | 0 | 0 | 8.377 | 0 | 0.003906 | -1 | -8.998 | 0.001953 | 0.01953 | 0.020 |
| uniform | 10x10 | GA-rand-cycle | GA-rand-tuned | 10 | 9 | 1 | 0 | 0 | 1.547 | 0 | 0.003906 | -1 | -1.763 | 0.001953 | 0.01953 | 0.020 |
| uniform | 10x10 | GA-rand-cycle | GA-cost-tuned | 10 | 8 | 1 | 1 | 0 | 1.382 | 1 | 0.007812 | -0.9556 | -1.311 | 0.001953 | 0.01953 | 0.020 |
| uniform | 10x10 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 1 | 0 | 0.2654 | 1.382 | 0 | 0.003906 | -1 | -0.9703 | 0.001953 | 0.01953 | 0.020 |
| uniform | 10x10 | GA-cost-cycle | VAM | 10 | 9 | 1 | 0 | 0.2654 | 8.377 | 0 | 0.003906 | -1 | -8.835 | 0.001953 | 0.01953 | 0.020 |
| uniform | 20x20 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 1.766 | 22.73 | 0 | 0.001953 | -1 | -20.54 | 0.001953 | 0.009766 | 0.010 |
| uniform | 20x20 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 1.766 | 14.03 | 0 | 0.001953 | -1 | -14.57 | 0.001953 | 0.009766 | 0.010 |
| uniform | 20x20 | GA-rand-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 1.766 | 4.793 | 0 | 0.001953 | -1 | -2.396 | 0.001953 | 0.009766 | 0.010 |
| uniform | 20x20 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 0.7617 | 4.793 | 0 | 0.001953 | -1 | -3.388 | 0.001953 | 0.009766 | 0.010 |
| uniform | 20x20 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 0.7617 | 22.73 | 0 | 0.001953 | -1 | -21.02 | 0.001953 | 0.009766 | 0.010 |
| uniform | 30x30 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 6.98 | 25.62 | 0 | 0.001953 | -1 | -18.64 | 0.001953 | 0.009766 | 0.010 |
| uniform | 30x30 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 6.98 | 33.57 | 0 | 0.001953 | -1 | -27.09 | 0.001953 | 0.009766 | 0.010 |
| uniform | 30x30 | GA-rand-cycle | GA-cost-tuned | 10 | 3 | 0 | 7 | 6.98 | 5.636 | 16 | 0.2754 | 0.4182 | 1.137 | 0.001953 | 0.2754 | 0.275 |
| uniform | 30x30 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 2.703 | 5.636 | 1 | 0.003906 | -0.9636 | -2.991 | 0.001953 | 0.009766 | 0.010 |
| uniform | 30x30 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 2.703 | 25.62 | 0 | 0.001953 | -1 | -22.11 | 0.001953 | 0.009766 | 0.010 |
| uniform | 50x50 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 11.87 | 31.47 | 0 | 0.001953 | -1 | -19.95 | 0.001953 | 0.009766 | 0.010 |
| uniform | 50x50 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 11.87 | 55.2 | 0 | 0.001953 | -1 | -43.44 | 0.001953 | 0.009766 | 0.010 |
| uniform | 50x50 | GA-rand-cycle | GA-cost-tuned | 10 | 3 | 0 | 7 | 11.87 | 11.86 | 19 | 0.4316 | 0.3091 | 1.115 | 0.001953 | 0.4316 | 0.432 |
| uniform | 50x50 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 7.31 | 11.86 | 0 | 0.001953 | -1 | -4.2 | 0.001953 | 0.009766 | 0.010 |
| uniform | 50x50 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 7.31 | 31.47 | 0 | 0.001953 | -1 | -25.49 | 0.001953 | 0.009766 | 0.010 |
| uniform | 100x100 | GA-rand-cycle | VAM | 5 | 3 | 0 | 2 | 30.81 | 36.13 | 3 | 0.3125 | -0.6 | -7.747 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | GA-rand-cycle | GA-rand-tuned | 5 | 5 | 0 | 0 | 30.81 | 110.8 | 0 | 0.0625 | -1 | -77.17 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | GA-rand-cycle | GA-cost-tuned | 5 | 0 | 0 | 5 | 30.81 | 17.96 | 0 | 0.0625 | 1 | 13.84 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | GA-cost-cycle | GA-cost-tuned | 5 | 5 | 0 | 0 | 10.4 | 17.96 | 0 | 0.0625 | -1 | -7.045 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | GA-cost-cycle | VAM | 5 | 5 | 0 | 0 | 10.4 | 36.13 | 0 | 0.0625 | -1 | -28.65 | 0.0625 | 0.3125 | 0.312 |
| structured | 20x20 | GA-rand-cycle | VAM | 10 | 10 | 0 | 0 | 0.2483 | 8.357 | 0 | 0.001953 | -1 | -8.055 | 0.001953 | 0.009766 | 0.010 |
| structured | 20x20 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 0.2483 | 1.522 | 0 | 0.001953 | -1 | -1.244 | 0.001953 | 0.009766 | 0.010 |
| structured | 20x20 | GA-rand-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 0.2483 | 0.9751 | 1 | 0.003906 | -0.9636 | -0.534 | 0.001953 | 0.009766 | 0.010 |
| structured | 20x20 | GA-cost-cycle | GA-cost-tuned | 10 | 9 | 0 | 1 | 0.3373 | 0.9751 | 2 | 0.005859 | -0.9273 | -0.4051 | 0.001953 | 0.009766 | 0.010 |
| structured | 20x20 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 0.3373 | 8.357 | 0 | 0.001953 | -1 | -7.977 | 0.001953 | 0.009766 | 0.010 |
