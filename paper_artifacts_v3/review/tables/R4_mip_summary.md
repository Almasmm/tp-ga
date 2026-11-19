# FCTP: the MIP solver in two settings, by size and rho

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Counts and medians of R4_mip_instances. `gap_*` is the gap of the solver, 100 (cost - bound) / cost. The columns of setting 2 cover the instances that were run (`run_all_threads_300s`); `gap_median_percent_1thread_60s_same_instances` gives setting 1 on these same instances.

| size | rho | instances | proved_1thread_60s | gap_median_percent_1thread_60s | time_median_s_1thread_60s | run_all_threads_300s | proved_all_threads_300s | gap_median_percent_all_threads_300s | time_median_s_all_threads_300s | cpu_over_wall_median | gap_median_percent_1thread_60s_same_instances | plan_better_with_300s | plan_equal | plan_worse_with_300s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10x10 | 0.2 | 5 | 5 | 6.628e-13 | 1.03 | 5 | 5 | 0 | 0.7571 | 1.838 | 6.628e-13 | 0 | 5 | 0 |
| 10x10 | 1 | 5 | 5 | 4.371e-09 | 0.5603 | 5 | 5 | 4.371e-09 | 0.4508 | 1.759 | 4.371e-09 | 0 | 5 | 0 |
| 15x15 | 0.2 | 5 | 5 | 0.004708 | 2.664 | 5 | 5 | 4.845e-13 | 2.029 | 1.363 | 0.004708 | 0 | 5 | 0 |
| 15x15 | 1 | 5 | 5 | 8.089e-14 | 3.57 | 5 | 5 | 0 | 2.372 | 1.719 | 8.089e-14 | 0 | 5 | 0 |
| 20x20 | 0.2 | 5 | 5 | 0.001274 | 16.78 | 5 | 5 | 0.002004 | 8.531 | 4.969 | 0.001274 | 0 | 5 | 0 |
| 20x20 | 1 | 5 | 5 | 0.001515 | 13.29 | 5 | 5 | 1.809e-14 | 8.403 | 4.71 | 0.001515 | 0 | 5 | 0 |
| 30x30 | 0.2 | 5 | 0 | 2.424 | 60.01 | 2 | 1 | 0.3827 | 224.9 | 8.682 | 2.746 | 2 | 0 | 0 |
| 30x30 | 1 | 5 | 0 | 1.808 | 60.01 | 2 | 2 | 0.001729 | 49.94 | 9.345 | 1.481 | 1 | 1 | 0 |
| 50x50 | 0.2 | 5 | 0 | 4.434 | 60.02 | 2 | 0 | 2.154 | 301.1 | 7.835 | 4.6 | 2 | 0 | 0 |
| 50x50 | 1 | 5 | 0 | 4.394 | 60.05 | 2 | 0 | 2.538 | 300.4 | 8.589 | 4.231 | 2 | 0 | 0 |
| 70x70 | 0.2 | 5 | 0 | 5.846 | 60.01 | 1 | 0 | 4.97 | 301.5 | 9.505 | 6.397 | 1 | 0 | 0 |
| 70x70 | 1 | 5 | 0 | 7.422 | 60.01 | 1 | 0 | 3.814 | 303 | 8.321 | 5.779 | 1 | 0 | 0 |
