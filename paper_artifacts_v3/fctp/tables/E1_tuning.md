# FCTP: grid on the training instances (amendment 9.2)

Mean training gap (%) over 8 training instances and 3 seeds; the reference of an instance is the smaller of its MIP solution (60 s) and the best run of the grid. `rank` is the order of the tie rule. `selected_as` marks the configuration with the smallest mean gap without the local search (GA-cost-cycle-ft) and with it (GA-hybrid-ft).

| rank | population | pivots | local_search_every | config | runs | mean_gap | mean_gap_20x20 | mean_gap_30x30 | generations_median | local_search_calls_mean | local_search_improvements_mean | time_median_s | selected_as |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 2700 | 1 | 0 | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 24 | 5.961 | 4.607 | 7.314 | 46.5 | 0 | 0 | 0.9733 |  |
| 1 | 2700 | 1 | 10 | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 24 | 6.234 | 4.694 | 7.773 | 46 | 4 | 2.292 | 0.9611 |  |
| 2 | 2700 | 1 | 3 | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls3 | 24 | 6.021 | 4.122 | 7.919 | 44.5 | 14.58 | 7.75 | 0.9557 |  |
| 3 | 2700 | 1 | 1 | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls1 | 24 | 5.976 | 3.525 | 8.427 | 40 | 40.25 | 17.25 | 0.8853 |  |
| 4 | 2700 | 2 | 0 | P2700-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 24 | 6.123 | 3.95 | 8.296 | 46.5 | 0 | 0 | 1.145 |  |
| 5 | 2700 | 2 | 10 | P2700-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls10 | 24 | 5.879 | 4.153 | 7.606 | 46 | 4 | 2.958 | 1.149 |  |
| 6 | 2700 | 2 | 3 | P2700-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 24 | 6.154 | 4.128 | 8.179 | 44.5 | 14.79 | 9.375 | 1.114 |  |
| 7 | 2700 | 2 | 1 | P2700-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls1 | 24 | 5.934 | 3.914 | 7.955 | 39.5 | 40.54 | 18.21 | 0.9606 |  |
| 8 | 2700 | 4 | 0 | P2700-pc0.965569-t8-e5-cycle:4-cost-aware-budget | 24 | 7.346 | 5.946 | 8.747 | 46.5 | 0 | 0 | 1.473 |  |
| 9 | 2700 | 4 | 10 | P2700-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls10 | 24 | 7.265 | 5.858 | 8.672 | 46 | 4 | 3.708 | 1.457 |  |
| 10 | 2700 | 4 | 3 | P2700-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls3 | 24 | 6.578 | 5.273 | 7.883 | 44.5 | 14.79 | 11.17 | 1.41 |  |
| 11 | 2700 | 4 | 1 | P2700-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls1 | 24 | 6.189 | 4.826 | 7.553 | 40 | 40.79 | 20.25 | 1.284 |  |
| 12 | 900 | 1 | 0 | P900-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 24 | 6.776 | 3.97 | 9.581 | 144 | 0 | 0 | 0.8952 |  |
| 13 | 900 | 1 | 10 | P900-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 24 | 6.509 | 3.964 | 9.055 | 135 | 13.04 | 3.125 | 0.8591 |  |
| 14 | 900 | 1 | 3 | P900-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls3 | 24 | 6.82 | 4.216 | 9.424 | 119 | 39.38 | 8.583 | 0.7598 |  |
| 15 | 900 | 1 | 1 | P900-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls1 | 24 | 6.818 | 4.518 | 9.117 | 87.5 | 88.88 | 17.58 | 0.5693 |  |
| 16 | 900 | 2 | 0 | P900-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 24 | 6.159 | 4.538 | 7.78 | 144 | 0 | 0 | 1.066 |  |
| 17 | 900 | 2 | 10 | P900-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls10 | 24 | 5.875 | 3.881 | 7.869 | 136 | 13.04 | 4.417 | 1.021 |  |
| 18 | 900 | 2 | 3 | P900-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 24 | 6.361 | 4.07 | 8.652 | 118.5 | 39.58 | 10.08 | 0.8982 |  |
| 19 | 900 | 2 | 1 | P900-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls1 | 24 | 6.516 | 4.772 | 8.26 | 87 | 89.71 | 19.25 | 0.6085 |  |
| 20 | 900 | 4 | 0 | P900-pc0.965569-t8-e5-cycle:4-cost-aware-budget | 24 | 6.705 | 4.707 | 8.703 | 144 | 0 | 0 | 1.377 |  |
| 21 | 900 | 4 | 10 | P900-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls10 | 24 | 6.904 | 5.07 | 8.738 | 137 | 13.21 | 6.417 | 1.307 |  |
| 22 | 900 | 4 | 3 | P900-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls3 | 24 | 6.612 | 4.734 | 8.489 | 119 | 40.38 | 14.42 | 1.151 |  |
| 23 | 900 | 4 | 1 | P900-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls1 | 24 | 7.005 | 5.635 | 8.375 | 90 | 90.92 | 22.58 | 0.8526 |  |
| 24 | 300 | 1 | 0 | P300-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 24 | 6.565 | 4.539 | 8.59 | 439.5 | 0 | 0 | 0.7669 |  |
| 25 | 300 | 1 | 10 | P300-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 24 | 7.157 | 4.769 | 9.544 | 364.5 | 36 | 3.542 | 0.6473 |  |
| 26 | 300 | 1 | 3 | P300-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls3 | 24 | 7.176 | 4.91 | 9.442 | 260.5 | 87.21 | 9.25 | 0.4771 |  |
| 27 | 300 | 1 | 1 | P300-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls1 | 24 | 7.654 | 5.336 | 9.973 | 149.5 | 149.6 | 17.79 | 0.2798 |  |
| 28 | 300 | 2 | 0 | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 24 | 5.57 | 4.339 | 6.8 | 439.5 | 0 | 0 | 0.9354 | GA-cost-cycle-ft |
| 29 | 300 | 2 | 10 | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls10 | 24 | 6.327 | 4.501 | 8.152 | 363.5 | 36.08 | 5.583 | 0.7715 |  |
| 30 | 300 | 2 | 3 | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 24 | 5.658 | 4.1 | 7.215 | 267 | 89 | 15.25 | 0.556 | GA-hybrid-ft |
| 31 | 300 | 2 | 1 | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls1 | 24 | 7.037 | 5.411 | 8.663 | 151 | 152.5 | 22.04 | 0.3225 |  |
| 32 | 300 | 4 | 0 | P300-pc0.965569-t8-e5-cycle:4-cost-aware-budget | 24 | 7.312 | 5.662 | 8.962 | 439.5 | 0 | 0 | 1.199 |  |
| 33 | 300 | 4 | 10 | P300-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls10 | 24 | 7.545 | 5.862 | 9.228 | 367.5 | 36.5 | 8.625 | 1.008 |  |
| 34 | 300 | 4 | 3 | P300-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls3 | 24 | 8.1 | 6.618 | 9.581 | 265.5 | 89.12 | 15.83 | 0.7423 |  |
| 35 | 300 | 4 | 1 | P300-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls1 | 24 | 7.699 | 5.964 | 9.433 | 153 | 152.2 | 21.83 | 0.4338 |  |
| 36 | 100 | 1 | 0 | P100-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 24 | 7.262 | 4.907 | 9.616 | 1367 | 0 | 0 | 0.6526 |  |
| 37 | 100 | 1 | 10 | P100-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 24 | 7.841 | 5.34 | 10.34 | 818.5 | 81.83 | 4.792 | 0.4013 |  |
| 38 | 100 | 1 | 3 | P100-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls3 | 24 | 8.546 | 5.9 | 11.19 | 444 | 147.6 | 10.38 | 0.2303 |  |
| 39 | 100 | 1 | 1 | P100-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls1 | 24 | 8.386 | 6.893 | 9.878 | 197 | 198.9 | 20.5 | 0.1252 |  |
| 40 | 100 | 2 | 0 | P100-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 24 | 7.117 | 5.321 | 8.913 | 1367 | 0 | 0 | 0.8052 |  |
| 41 | 100 | 2 | 10 | P100-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls10 | 24 | 6.83 | 4.382 | 9.278 | 828.5 | 82.67 | 7.458 | 0.5071 |  |
| 42 | 100 | 2 | 3 | P100-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 24 | 6.927 | 4.424 | 9.43 | 450 | 149.8 | 15.17 | 0.2826 |  |
| 43 | 100 | 2 | 1 | P100-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls1 | 24 | 8.113 | 6.033 | 10.19 | 197 | 198.2 | 19.79 | 0.1441 |  |
| 44 | 100 | 4 | 0 | P100-pc0.965569-t8-e5-cycle:4-cost-aware-budget | 24 | 7.608 | 5.815 | 9.402 | 1367 | 0 | 0 | 1.093 |  |
| 45 | 100 | 4 | 10 | P100-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls10 | 24 | 7.7 | 6.238 | 9.162 | 844.5 | 84.29 | 12.79 | 0.6936 |  |
| 46 | 100 | 4 | 3 | P100-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls3 | 24 | 7.232 | 5.212 | 9.252 | 459 | 153.5 | 20.5 | 0.4015 |  |
| 47 | 100 | 4 | 1 | P100-pc0.965569-t8-e5-cycle:4-cost-aware-budget-ls1 | 24 | 8.461 | 6.142 | 10.78 | 200 | 201.3 | 23.71 | 0.1987 |  |
