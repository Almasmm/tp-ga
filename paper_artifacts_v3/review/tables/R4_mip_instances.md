# FCTP: the MIP solver in two settings, by instance

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Model of 8.4 (x <= min(a, b) y) in HiGHS, relative gap 0, absolute gap 0.99. Setting 1: one thread, 60 s, made with 20 runs at once (records of 8.4 and 9.4). Setting 2: `threads = 0` (the solver's own choice among all processors), 300 s, one run at a time in a fresh process; `cpu_s` is the processor time of that process, `cpu_over_wall` shows how much of the run was parallel. `order` is the order of the time rule (10.0); `not run (time rule)`: not started within the limit of 90 minutes. `cost_change_percent` = 100 (cost of setting 2 - cost of setting 1) / cost of setting 1.

| order | instance | size | rho | status_1thread_60s | proved_1thread_60s | cost_1thread_60s | gap_percent_1thread_60s | time_s_1thread_60s | status_all_threads_300s | proved_all_threads_300s | cost_all_threads_300s | gap_percent_all_threads_300s | time_s_all_threads_300s | cpu_s_all_threads_300s | cpu_over_wall | nodes_all_threads_300s | cost_change_percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | f10x10-r0.2-00 | 10x10 | 0.2 | Optimal | yes | 9955 | 0 | 0.0794 | Optimal | yes | 9955 | 0 | 0.05981 | 0.2656 | 4.441 | 1 | 0 |
| 1 | f10x10-r0.2-01 | 10x10 | 0.2 | Optimal | yes | 1.181e+04 | 0.006418 | 1.162 | Optimal | yes | 1.181e+04 | 0.006418 | 0.8755 | 1.609 | 1.838 | 5 | 0 |
| 2 | f10x10-r0.2-02 | 10x10 | 0.2 | Optimal | yes | 1.043e+04 | 6.628e-13 | 1.03 | Optimal | yes | 1.043e+04 | 6.977e-14 | 0.7571 | 1.141 | 1.507 | 3 | 0 |
| 3 | f10x10-r0.2-03 | 10x10 | 0.2 | Optimal | yes | 1.097e+04 | 0 | 0.134 | Optimal | yes | 1.097e+04 | 0 | 0.1034 | 0.4219 | 4.078 | 1 | 0 |
| 4 | f10x10-r0.2-04 | 10x10 | 0.2 | Optimal | yes | 1.352e+04 | 0.005586 | 2.477 | Optimal | yes | 1.352e+04 | 0 | 1.873 | 2.469 | 1.318 | 7 | 0 |
| 5 | f10x10-r1-00 | 10x10 | 1 | Optimal | yes | 2.288e+04 | 4.371e-09 | 0.03906 | Optimal | yes | 2.288e+04 | 4.371e-09 | 0.0403 | 0.4219 | 10.47 | 1 | 0 |
| 6 | f10x10-r1-01 | 10x10 | 1 | Optimal | yes | 2.677e+04 | 5.437e-14 | 0.5464 | Optimal | yes | 2.677e+04 | 5.437e-14 | 0.4058 | 0.6875 | 1.694 | 1 | 0 |
| 7 | f10x10-r1-02 | 10x10 | 1 | Optimal | yes | 2.035e+04 | 4.914e-09 | 0.5603 | Optimal | yes | 2.035e+04 | 4.914e-09 | 0.4508 | 0.875 | 1.941 | 3 | 0 |
| 8 | f10x10-r1-03 | 10x10 | 1 | Optimal | yes | 2.776e+04 | 0.002 | 1.993 | Optimal | yes | 2.776e+04 | 2.621e-14 | 1.359 | 2.391 | 1.759 | 15 | 0 |
| 9 | f10x10-r1-04 | 10x10 | 1 | Optimal | yes | 3.157e+04 | 1.083e-12 | 1.85 | Optimal | yes | 3.157e+04 | 0.002077 | 1.406 | 2.094 | 1.489 | 11 | 0 |
| 10 | f15x15-r0.2-00 | 15x15 | 0.2 | Optimal | yes | 1.613e+04 | 0.005108 | 3.763 | Optimal | yes | 1.613e+04 | 1.127e-14 | 3.012 | 4.172 | 1.385 | 19 | 0 |
| 11 | f15x15-r0.2-01 | 15x15 | 0.2 | Optimal | yes | 1.427e+04 | 0.006509 | 2.231 | Optimal | yes | 1.427e+04 | 4.845e-13 | 1.67 | 2.188 | 1.31 | 5 | 0 |
| 12 | f15x15-r0.2-02 | 15x15 | 0.2 | Optimal | yes | 1.901e+04 | 0 | 3.851 | Optimal | yes | 1.901e+04 | 1.914e-13 | 3.074 | 4.188 | 1.362 | 22 | 0 |
| 13 | f15x15-r0.2-03 | 15x15 | 0.2 | Optimal | yes | 1.317e+04 | 5.248e-13 | 0.8322 | Optimal | yes | 1.317e+04 | 5.248e-13 | 0.6413 | 1.125 | 1.754 | 1 | 0 |
| 14 | f15x15-r0.2-04 | 15x15 | 0.2 | Optimal | yes | 1.416e+04 | 0.004708 | 2.664 | Optimal | yes | 1.416e+04 | 2.447e-11 | 2.029 | 2.766 | 1.363 | 7 | 0 |
| 15 | f15x15-r1-00 | 15x15 | 1 | Optimal | yes | 4.211e+04 | 0 | 2.729 | Optimal | yes | 4.211e+04 | 0 | 2.286 | 2.875 | 1.258 | 9 | 0 |
| 16 | f15x15-r1-01 | 15x15 | 1 | Optimal | yes | 3.374e+04 | 0.001641 | 10.36 | Optimal | yes | 3.374e+04 | 0 | 4.268 | 20.52 | 4.807 | 3072 | 0 |
| 17 | f15x15-r1-02 | 15x15 | 1 | Optimal | yes | 3.598e+04 | 8.089e-14 | 3.054 | Optimal | yes | 3.598e+04 | 0.002594 | 2.11 | 2.844 | 1.348 | 9 | 0 |
| 18 | f15x15-r1-03 | 15x15 | 1 | Optimal | yes | 3.454e+04 | 0 | 9.335 | Optimal | yes | 3.454e+04 | 0 | 4.706 | 18.53 | 3.938 | 2860 | 0 |
| 19 | f15x15-r1-04 | 15x15 | 1 | Optimal | yes | 4.147e+04 | 0.0002819 | 3.57 | Optimal | yes | 4.147e+04 | 0 | 2.372 | 4.078 | 1.719 | 29 | 0 |
| 20 | f20x20-r0.2-00 | 20x20 | 0.2 | Optimal | yes | 2.28e+04 | 0.001274 | 16.52 | Optimal | yes | 2.28e+04 | 2.027e-12 | 8.367 | 38.64 | 4.618 | 2360 | 0 |
| 21 | f20x20-r0.2-01 | 20x20 | 0.2 | Optimal | yes | 1.645e+04 | 0.005762 | 17.76 | Optimal | yes | 1.645e+04 | 0.00571 | 9.71 | 68.88 | 7.094 | 5852 | 0 |
| 22 | f20x20-r0.2-02 | 20x20 | 0.2 | Optimal | yes | 2.002e+04 | 0 | 10.35 | Optimal | yes | 2.002e+04 | 1.817e-14 | 7.183 | 35.69 | 4.969 | 2724 | 0 |
| 23 | f20x20-r0.2-03 | 20x20 | 0.2 | Optimal | yes | 2.025e+04 | 0 | 16.78 | Optimal | yes | 2.025e+04 | 0.002004 | 11.12 | 27.97 | 2.514 | 627 | 0 |
| 24 | f20x20-r0.2-04 | 20x20 | 0.2 | Optimal | yes | 1.844e+04 | 0.004007 | 18.21 | Optimal | yes | 1.844e+04 | 0.004497 | 8.531 | 73.23 | 8.585 | 7028 | 0 |
| 25 | f20x20-r1-00 | 20x20 | 1 | Optimal | yes | 4.022e+04 | 0.001589 | 13.29 | Optimal | yes | 4.022e+04 | 1.809e-14 | 8.403 | 39.58 | 4.71 | 3475 | 0 |
| 26 | f20x20-r1-01 | 20x20 | 1 | Optimal | yes | 4.205e+04 | 0.00232 | 37.91 | Optimal | yes | 4.205e+04 | 0.001739 | 12.33 | 83.69 | 6.789 | 7211 | 0 |
| 27 | f20x20-r1-02 | 20x20 | 1 | Optimal | yes | 4.106e+04 | 0.0004859 | 4.195 | Optimal | yes | 4.106e+04 | 0 | 3.11 | 4.219 | 1.356 | 27 | 0 |
| 28 | f20x20-r1-03 | 20x20 | 1 | Optimal | yes | 4.765e+04 | 0.001515 | 43.2 | Optimal | yes | 4.765e+04 | 0.001527 | 19.43 | 153.7 | 7.913 | 11295 | 0 |
| 29 | f20x20-r1-04 | 20x20 | 1 | Optimal | yes | 4.041e+04 | 0.0007297 | 6.473 | Optimal | yes | 4.041e+04 | 0 | 5.301 | 7.719 | 1.456 | 33 | 0 |
| 30 | f30x30-r0.2-00 | 30x30 | 0.2 | Time limit reached | no | 2.037e+04 | 2.441 | 60.02 | Optimal | yes | 2.018e+04 | 0.004872 | 149.3 | 1332 | 8.922 | 23153 | -0.9474 |
| 31 | f30x30-r1-00 | 30x30 | 1 | Time limit reached | no | 5.518e+04 | 1.311 | 60.03 | Optimal | yes | 5.518e+04 | 0.001733 | 50.16 | 461.2 | 9.193 | 11888 | 0 |
| 32 | f50x50-r0.2-00 | 50x50 | 0.2 | Time limit reached | no | 2.982e+04 | 4.434 | 60.02 | Time limit reached | no | 2.933e+04 | 2.366 | 301.6 | 2487 | 8.245 | 12811 | -1.647 |
| 33 | f50x50-r1-00 | 50x50 | 1 | Time limit reached | no | 5.669e+04 | 2.884 | 60.05 | Time limit reached | no | 5.66e+04 | 2.086 | 300.3 | 2424 | 8.073 | 18916 | -0.1535 |
| 34 | f70x70-r0.2-00 | 70x70 | 0.2 | Time limit reached | no | 3.836e+04 | 6.397 | 60.21 | Time limit reached | no | 3.787e+04 | 4.97 | 301.5 | 2866 | 9.505 | 6059 | -1.295 |
| 35 | f70x70-r1-00 | 70x70 | 1 | Time limit reached | no | 8.388e+04 | 5.779 | 60.16 | Time limit reached | no | 8.236e+04 | 3.814 | 303 | 2522 | 8.321 | 6996 | -1.809 |
| 36 | f30x30-r0.2-01 | 30x30 | 0.2 | Time limit reached | no | 2.694e+04 | 3.052 | 60.04 | Time limit reached | no | 2.68e+04 | 0.7605 | 300.5 | 2537 | 8.442 | 41300 | -0.5419 |
| 37 | f30x30-r1-01 | 30x30 | 1 | Time limit reached | no | 5.291e+04 | 1.651 | 60 | Optimal | yes | 5.285e+04 | 0.001726 | 49.72 | 472.1 | 9.497 | 13106 | -0.1172 |
| 38 | f50x50-r0.2-01 | 50x50 | 0.2 | Time limit reached | no | 3.343e+04 | 4.767 | 60.02 | Time limit reached | no | 3.267e+04 | 1.943 | 300.7 | 2232 | 7.424 | 13735 | -2.261 |
| 39 | f50x50-r1-01 | 50x50 | 1 | Time limit reached | no | 6.538e+04 | 5.578 | 60.02 | Time limit reached | no | 6.4e+04 | 2.991 | 300.6 | 2737 | 9.105 | 19067 | -2.111 |
| 40 | f70x70-r0.2-01 | 70x70 | 0.2 | Time limit reached | no | 3.661e+04 | 5.297 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 41 | f70x70-r1-01 | 70x70 | 1 | Time limit reached | no | 8.265e+04 | 7.422 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 42 | f30x30-r0.2-02 | 30x30 | 0.2 | Time limit reached | no | 2.031e+04 | 1.679 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 43 | f30x30-r1-02 | 30x30 | 1 | Time limit reached | no | 5.221e+04 | 2.801 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 44 | f50x50-r0.2-02 | 50x50 | 0.2 | Time limit reached | no | 2.934e+04 | 3.684 | 60.06 | not run (time rule) | – | – | – | – | – | – | – | – |
| 45 | f50x50-r1-02 | 50x50 | 1 | Time limit reached | no | 7.386e+04 | 5.312 | 60.07 | not run (time rule) | – | – | – | – | – | – | – | – |
| 46 | f70x70-r0.2-02 | 70x70 | 0.2 | Time limit reached | no | 3.383e+04 | 5.846 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 47 | f70x70-r1-02 | 70x70 | 1 | Time limit reached | no | 8.008e+04 | 5.044 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 48 | f30x30-r0.2-03 | 30x30 | 0.2 | Time limit reached | no | 2.129e+04 | 1.641 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 49 | f30x30-r1-03 | 30x30 | 1 | Time limit reached | no | 5.557e+04 | 3.395 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 50 | f50x50-r0.2-03 | 50x50 | 0.2 | Time limit reached | no | 2.931e+04 | 5.662 | 60.02 | not run (time rule) | – | – | – | – | – | – | – | – |
| 51 | f50x50-r1-03 | 50x50 | 1 | Time limit reached | no | 6.163e+04 | 3.945 | 60.08 | not run (time rule) | – | – | – | – | – | – | – | – |
| 52 | f70x70-r0.2-03 | 70x70 | 0.2 | Time limit reached | no | 3.874e+04 | 5.573 | 60.05 | not run (time rule) | – | – | – | – | – | – | – | – |
| 53 | f70x70-r1-03 | 70x70 | 1 | Time limit reached | no | 8.075e+04 | 8.152 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 54 | f30x30-r0.2-04 | 30x30 | 0.2 | Time limit reached | no | 2.204e+04 | 2.424 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 55 | f30x30-r1-04 | 30x30 | 1 | Time limit reached | no | 4.577e+04 | 1.808 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 56 | f50x50-r0.2-04 | 50x50 | 0.2 | Time limit reached | no | 3.253e+04 | 3.71 | 60.06 | not run (time rule) | – | – | – | – | – | – | – | – |
| 57 | f50x50-r1-04 | 50x50 | 1 | Time limit reached | no | 6.664e+04 | 4.394 | 60.03 | not run (time rule) | – | – | – | – | – | – | – | – |
| 58 | f70x70-r0.2-04 | 70x70 | 0.2 | Time limit reached | no | 3.415e+04 | 7.332 | 60.01 | not run (time rule) | – | – | – | – | – | – | – | – |
| 59 | f70x70-r1-04 | 70x70 | 1 | Time limit reached | no | 8.752e+04 | 7.693 | 60.21 | not run (time rule) | – | – | – | – | – | – | – | – |
