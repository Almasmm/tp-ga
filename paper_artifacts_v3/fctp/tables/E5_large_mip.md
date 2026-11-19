# FCTP above 30x30: MIP reference with 60 s (amendment 9.4)

HiGHS, one thread, 60 s. `z_best_from_heuristic` counts the instances where the best known value is a run of a heuristic and not a MIP plan.

| size | rho | instances | proved_optimal | with_plan | statuses | mip_time_median_s | mip_gap_median_percent | mip_gap_max_percent | z_best_from_heuristic | z_best_gap_to_bound_median_percent |
|---|---|---|---|---|---|---|---|---|---|---|
| 50x50 | 0.2 | 5 | 0 | 5 | Time limit reached | 60.02 | 4.434 | 5.662 | 0 | 4.434 |
| 50x50 | 1 | 5 | 0 | 5 | Time limit reached | 60.05 | 4.394 | 5.578 | 0 | 4.394 |
| 70x70 | 0.2 | 5 | 0 | 5 | Time limit reached | 60.01 | 5.846 | 7.332 | 0 | 5.846 |
| 70x70 | 1 | 5 | 0 | 5 | Time limit reached | 60.01 | 7.422 | 8.152 | 0 | 7.422 |
