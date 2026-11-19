# Linear problem: tests on the groups completed by amendment 9.1

The same pairs, test and Holm family as in T2_tests, on three sets of instances of a group that the pilot rule had reduced: the instances of the reduced plan (reported before the extension), the instances added by amendment 9.1 alone (not seen when the amendment was written), and all of them. The test on all instances includes the instances that had been seen.

| set | size | instances | method_a | method_b | n | wins_a | ties | losses_a | median_a | median_b | W | p | rank_biserial_r | hl_shift | smallest_possible_p | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 100x100 | first 5 (plan after the pilot rule) | GA-rand-cycle | VAM | 5 | 3 | 0 | 2 | 30.81 | 36.13 | 3 | 0.3125 | -0.6 | -7.747 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | first 5 (plan after the pilot rule) | GA-rand-cycle | GA-rand-tuned | 5 | 5 | 0 | 0 | 30.81 | 110.8 | 0 | 0.0625 | -1 | -77.17 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | first 5 (plan after the pilot rule) | GA-rand-cycle | GA-cost-tuned | 5 | 0 | 0 | 5 | 30.81 | 17.96 | 0 | 0.0625 | 1 | 13.84 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | first 5 (plan after the pilot rule) | GA-cost-cycle | GA-cost-tuned | 5 | 5 | 0 | 0 | 10.4 | 17.96 | 0 | 0.0625 | -1 | -7.045 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | first 5 (plan after the pilot rule) | GA-cost-cycle | VAM | 5 | 5 | 0 | 0 | 10.4 | 36.13 | 0 | 0.0625 | -1 | -28.65 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | added 5 (amendment 9.1) | GA-rand-cycle | VAM | 5 | 5 | 0 | 0 | 36.63 | 43.84 | 0 | 0.0625 | -1 | -7.504 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | added 5 (amendment 9.1) | GA-rand-cycle | GA-rand-tuned | 5 | 5 | 0 | 0 | 36.63 | 113 | 0 | 0.0625 | -1 | -72.53 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | added 5 (amendment 9.1) | GA-rand-cycle | GA-cost-tuned | 5 | 0 | 0 | 5 | 36.63 | 22.42 | 0 | 0.0625 | 1 | 14.1 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | added 5 (amendment 9.1) | GA-cost-cycle | GA-cost-tuned | 5 | 5 | 0 | 0 | 15.89 | 22.42 | 0 | 0.0625 | -1 | -6.262 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | added 5 (amendment 9.1) | GA-cost-cycle | VAM | 5 | 5 | 0 | 0 | 15.89 | 43.84 | 0 | 0.0625 | -1 | -28.51 | 0.0625 | 0.3125 | 0.312 |
| uniform | 100x100 | all 10 | GA-rand-cycle | VAM | 10 | 8 | 0 | 2 | 33.23 | 41.7 | 4 | 0.01367 | -0.8545 | -7.747 | 0.001953 | 0.01367 | 0.014 |
| uniform | 100x100 | all 10 | GA-rand-cycle | GA-rand-tuned | 10 | 10 | 0 | 0 | 33.23 | 111.3 | 0 | 0.001953 | -1 | -75.88 | 0.001953 | 0.009766 | 0.010 |
| uniform | 100x100 | all 10 | GA-rand-cycle | GA-cost-tuned | 10 | 0 | 0 | 10 | 33.23 | 21.24 | 0 | 0.001953 | 1 | 14.14 | 0.001953 | 0.009766 | 0.010 |
| uniform | 100x100 | all 10 | GA-cost-cycle | GA-cost-tuned | 10 | 10 | 0 | 0 | 14.56 | 21.24 | 0 | 0.001953 | -1 | -6.329 | 0.001953 | 0.009766 | 0.010 |
| uniform | 100x100 | all 10 | GA-cost-cycle | VAM | 10 | 10 | 0 | 0 | 14.56 | 41.7 | 0 | 0.001953 | -1 | -28.51 | 0.001953 | 0.009766 | 0.010 |
