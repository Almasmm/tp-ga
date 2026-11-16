# T2b. Sensitivity to the stopping rule: stagnation limit vs. budget only

Same instances, seeds and parameters; the only difference is the stagnation limit. Wilcoxon on per-instance median gaps (with limit vs. without).

| size | method | stopping | runs | gap_mean | gap_median | share_optimal | evals_median | time_median_s | wilcoxon_p | rank_biserial_r |
|---|---|---|---|---|---|---|---|---|---|---|
| 50x50 | GA-cost | stagnation 200 | 300 | 25.841 | 25.559 | 0 | 41505.000 | 0.615 | – | – |
| 50x50 | GA-cost | budget only | 300 | 21.865 | 20.938 | 0 | 5.000e+05 | 8.138 | 0.002 | 1.000 |
| 50x50 | GA-rand | stagnation 200 | 300 | 227.414 | 219.936 | 0 | 3.057e+05 | 4.522 | – | – |
| 50x50 | GA-rand | budget only | 300 | 177.451 | 173.095 | 0 | 5.000e+05 | 7.585 | 0.002 | 1.000 |
| 100x100 | GA-cost | stagnation 200 | 300 | 28.449 | 30.192 | 0 | 43759.000 | 4.225 | – | – |
| 100x100 | GA-cost | budget only | 300 | 24.031 | 24.839 | 0 | 2.000e+06 | 204.254 | 0.002 | 1.000 |
| 100x100 | GA-rand | stagnation 200 | 300 | 606.581 | 602.755 | 0 | 7.037e+05 | 63.545 | – | – |
| 100x100 | GA-rand | budget only | 300 | 358.795 | 358.050 | 0 | 2.000e+06 | 197.753 | 0.002 | 1.000 |
