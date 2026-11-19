# FCTP above 30x30: gap of every method

gap = 100 (Z - Z_best) / Z_best; Z_best is the best known value (no optimum is proved at these sizes unless E5 says so). The row MIP-60s is the plan of the MIP solver at 60 s (`runs` = instances with a plan). Run times were measured with 20 runs at once.

| size | rho | method | config | instances | runs | gap_median | gap_instance_median | gap_mean | gap_min | gap_max | share_at_z_best | time_median_s | generations_median | local_search_calls_mean | local_search_evaluations_mean | local_search_improvements_mean |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 50x50 | 0.2 | Balinski | - | 5 | 5 | 16.02 | 16.02 | 15.99 | 12.73 | 19.36 | 0 | 0.01834 | – | – | – | – |
| 50x50 | 0.2 | VAM-lin | - | 5 | 5 | 23.98 | 23.98 | 25.44 | 21.09 | 35.65 | 0 | 0.005855 | – | – | – | – |
| 50x50 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 7.811 | 7.534 | 8.245 | 0.9243 | 14.29 | 0 | 11.56 | 184 | 0 | 0 | 0 |
| 50x50 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 6.556 | 7.383 | 6.892 | 1.636 | 14.32 | 0 | 10.45 | 1693 | 0 | 0 | 0 |
| 50x50 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 8.175 | 7.994 | 8.166 | 2.764 | 15.9 | 0 | 3.149 | 501 | 168 | 3.509e+05 | 25.62 |
| 50x50 | 0.2 | MIP-60s | - | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 60.02 | – | – | – | – |
| 50x50 | 1 | Balinski | - | 5 | 5 | 19.16 | 19.16 | 19.05 | 16.66 | 22.53 | 0 | 0.01674 | – | – | – | – |
| 50x50 | 1 | VAM-lin | - | 5 | 5 | 36.37 | 36.37 | 38.82 | 32.3 | 49.13 | 0 | 0.006297 | – | – | – | – |
| 50x50 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 11.12 | 11.7 | 10.73 | 6.265 | 16.51 | 0 | 11.23 | 184 | 0 | 0 | 0 |
| 50x50 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 8.57 | 7.869 | 8.55 | 3.016 | 14.87 | 0 | 10.48 | 1693 | 0 | 0 | 0 |
| 50x50 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 10.66 | 10.94 | 10.6 | 5.267 | 18.08 | 0 | 3.133 | 510 | 170.6 | 3.486e+05 | 29.74 |
| 50x50 | 1 | MIP-60s | - | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 60.05 | – | – | – | – |
| 70x70 | 0.2 | Balinski | - | 5 | 5 | 16.87 | 16.87 | 16.08 | 12.14 | 20.97 | 0 | 0.03776 | – | – | – | – |
| 70x70 | 0.2 | VAM-lin | - | 5 | 5 | 33.03 | 33.03 | 32.47 | 27.22 | 36.4 | 0 | 0.01036 | – | – | – | – |
| 70x70 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 8.975 | 8.975 | 9.272 | 1.268 | 17.23 | 0 | 40.23 | 362 | 0 | 0 | 0 |
| 70x70 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 7.11 | 7.609 | 7.397 | 1.678 | 16.16 | 0 | 37.46 | 3321 | 0 | 0 | 0 |
| 70x70 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 10.03 | 10.42 | 9.958 | 2.896 | 17.72 | 0 | 6.773 | 601.5 | 200.8 | 8.02e+05 | 36.58 |
| 70x70 | 0.2 | MIP-60s | - | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 60.01 | – | – | – | – |
| 70x70 | 1 | Balinski | - | 5 | 5 | 18.56 | 18.56 | 18.07 | 14.62 | 21.36 | 0 | 0.0379 | – | – | – | – |
| 70x70 | 1 | VAM-lin | - | 5 | 5 | 40.45 | 40.45 | 39.98 | 34.49 | 44.88 | 0 | 0.01124 | – | – | – | – |
| 70x70 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 10.28 | 10.57 | 9.975 | 5.575 | 14.19 | 0 | 42.78 | 362 | 0 | 0 | 0 |
| 70x70 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 9.33 | 9.778 | 8.942 | 4.697 | 13.72 | 0 | 41.16 | 3321 | 0 | 0 | 0 |
| 70x70 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 11.9 | 12.03 | 11.57 | 5.929 | 17.76 | 0 | 7.283 | 591 | 198.3 | 8.041e+05 | 32.94 |
| 70x70 | 1 | MIP-60s | - | 5 | 5 | 0 | 0 | 0.01575 | 0 | 0.07874 | 0.8 | 60.01 | – | – | – | – |
