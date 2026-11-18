# FCTP: MIP status and time by size and rho

`proved_optimal` counts the instances where HiGHS proved the optimum within the limit.

| size | rho | instances | proved_optimal | statuses | mip_time_median_s | mip_time_max_s | mip_gap_median_percent | mip_gap_max_percent | z_best_from_heuristic | z_best_gap_to_bound_median_percent |
|---|---|---|---|---|---|---|---|---|---|---|
| 10x10 | 0.2 | 5 | 5 | Optimal | 1.03 | 2.477 | 6.628e-13 | 0.006418 | 0 | 6.628e-13 |
| 10x10 | 1 | 5 | 5 | Optimal | 0.5603 | 1.993 | 4.371e-09 | 0.002 | 0 | 4.371e-09 |
| 15x15 | 0.2 | 5 | 5 | Optimal | 2.664 | 3.851 | 0.004708 | 0.006509 | 0 | 0.004708 |
| 15x15 | 1 | 5 | 5 | Optimal | 3.57 | 10.36 | 8.089e-14 | 0.001641 | 0 | 8.089e-14 |
| 20x20 | 0.2 | 5 | 5 | Optimal | 16.78 | 18.21 | 0.001274 | 0.005762 | 0 | 0.001274 |
| 20x20 | 1 | 5 | 5 | Optimal | 13.29 | 43.2 | 0.001515 | 0.00232 | 0 | 0.001515 |
| 30x30 | 0.2 | 5 | 0 | Time limit reached | 60.01 | 60.04 | 2.424 | 3.052 | 0 | 2.424 |
| 30x30 | 1 | 5 | 0 | Time limit reached | 60.01 | 60.03 | 1.808 | 3.395 | 0 | 1.808 |
