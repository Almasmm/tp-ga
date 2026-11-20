# Linear problem: two rules for the entering arc of the cycle mutation (amendment 10.5 b)

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). `-nd`: the entering arc is drawn among the non-basic arcs whose cycle has no arc with zero amount on a minus position (theta > 0); otherwise the same GA, parameters, k, seeds and budget. Gap to Z* in percent, columns as in R2_gap. The runs without `-nd` are the records of amendments 8 and 9. `pivots_left_to_uniform_rule_share`: pivots for which no such arc existed. `unchanged_offspring_share`: offspring whose pivots all had theta = 0. Times with 20 runs at once.

| set | size | method | instances | runs | gap_instance_median | ci95_low | ci95_high | gap_min | gap_max | time_median_s | pivots | pivots_theta_zero_share | pivots_left_to_uniform_rule_share | unchanged_offspring_share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | GA-rand-cycle | 10 | 100 | 0 | 0 | 0 | 0 | 0 | 0.01057 | 965600 | 0.01635 | – | 0.005433 |
| uniform | 5x5 | GA-rand-cycle-nd | 10 | 100 | 0 | 0 | 0 | 0 | 0 | 0.01779 | 965600 | 0 | 0 | 0 |
| uniform | 5x5 | GA-cost-cycle | 10 | 100 | 0 | 0 | 0.3504 | 0 | 1.396 | 0.01293 | 0 | – | – | – |
| uniform | 5x5 | GA-cost-cycle-nd | 10 | 100 | 0 | 0 | 0.3504 | 0 | 1.396 | 0.0122 | 0 | – | – | – |
| uniform | 10x10 | GA-rand-cycle | 10 | 100 | 0 | 0 | 0.142 | 0 | 4.721 | 0.0648 | 3947600 | 0.08102 | – | 0.0245 |
| uniform | 10x10 | GA-rand-cycle-nd | 10 | 100 | 0 | 0 | 0.1054 | 0 | 4.721 | 0.1627 | 3947600 | 0 | 0 | 0 |
| uniform | 10x10 | GA-cost-cycle | 10 | 100 | 0.2654 | 0.02718 | 0.6163 | 0 | 1.972 | 0.06734 | 1617000 | 0.05755 | – | 0.05755 |
| uniform | 10x10 | GA-cost-cycle-nd | 10 | 100 | 0.1464 | 0 | 0.3103 | 0 | 1.867 | 0.105 | 1617000 | 0 | 0 | 0 |
| uniform | 20x20 | GA-rand-cycle | 10 | 100 | 1.766 | 0.8564 | 3.477 | 0 | 15.29 | 0.4872 | 15960800 | 0.2587 | – | 0.1134 |
| uniform | 20x20 | GA-rand-cycle-nd | 10 | 100 | 2.813 | 1.477 | 3.994 | 0 | 15.83 | 1.645 | 15960800 | 0 | 0 | 0 |
| uniform | 20x20 | GA-cost-cycle | 10 | 100 | 0.7617 | 0.3414 | 2.29 | 0 | 4.705 | 0.4959 | 7546000 | 0.1535 | – | 0.1535 |
| uniform | 20x20 | GA-cost-cycle-nd | 10 | 100 | 0.6956 | 0.3568 | 1.718 | 0 | 4.04 | 1.037 | 7546000 | 0 | 0 | 0 |
| uniform | 30x30 | GA-rand-cycle | 10 | 100 | 6.98 | 5.383 | 7.761 | 0.3969 | 23.9 | 1.661 | 35954400 | 0.3908 | – | 0.1962 |
| uniform | 30x30 | GA-rand-cycle-nd | 10 | 100 | 8.241 | 6.94 | 10.3 | 1.084 | 46.83 | 6.548 | 35954400 | 0 | 0 | 0 |
| uniform | 30x30 | GA-cost-cycle | 10 | 100 | 2.703 | 1.443 | 3.376 | 0.3862 | 10.15 | 1.821 | 17517500 | 0.268 | – | 0.268 |
| uniform | 30x30 | GA-cost-cycle-nd | 10 | 100 | 1.943 | 1.501 | 2.469 | 0.3155 | 5.251 | 4.326 | 17517500 | 0 | 0 | 0 |
| uniform | 50x50 | GA-rand-cycle | 10 | 100 | 11.87 | 11.53 | 13.04 | 2.586 | 27.66 | 9.112 | 99968000 | 0.5458 | – | 0.3298 |
| uniform | 50x50 | GA-rand-cycle-nd | 10 | 100 | 21.17 | 19.04 | 24.13 | 3.769 | 49.75 | 35.82 | 99968000 | 0 | 0 | 0 |
| uniform | 50x50 | GA-cost-cycle | 10 | 100 | 7.31 | 5.23 | 9.715 | 0.2352 | 17.31 | 11.33 | 49588000 | 0.4518 | – | 0.4518 |
| uniform | 50x50 | GA-cost-cycle-nd | 10 | 100 | 4.262 | 2.898 | 5.883 | 0.676 | 9.261 | 25.54 | 49588000 | 0 | 0 | 0 |
| structured | 20x20 | GA-rand-cycle | 10 | 100 | 0.2483 | 0.1511 | 0.3932 | 0 | 2.004 | 0.4802 | 15960800 | 0.2192 | – | 0.08777 |
| structured | 20x20 | GA-rand-cycle-nd | 10 | 100 | 0.3647 | 0.2969 | 0.5273 | 0 | 8.889 | 1.689 | 15960800 | 0 | 0 | 0 |
| structured | 20x20 | GA-cost-cycle | 10 | 100 | 0.3373 | 0.1455 | 0.498 | 0 | 1.853 | 0.496 | 7546000 | 0.1738 | – | 0.1738 |
| structured | 20x20 | GA-cost-cycle-nd | 10 | 100 | 0.3317 | 0.1455 | 0.493 | 0 | 1.452 | 1.069 | 7546000 | 0 | 0 | 0 |
