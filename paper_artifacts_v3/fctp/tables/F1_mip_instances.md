# FCTP: reference by instance

MIP in HiGHS, one thread, time limit as configured. z_best is the proved optimum, otherwise the best known value (minimum of the MIP solution and of every run of every method). `z_best_gap_to_bound_percent` = 100 (z_best - bound) / z_best.

| instance | size | rho | mip_status | proved | mip_cost | mip_bound | mip_gap_percent | mip_time_s | mip_nodes | z_best | z_best_source | z_best_gap_to_bound_percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f10x10-r0.2-00 | 10x10 | 0.2 | Optimal | yes | 9955 | 9955 | 0 | 0.0794 | 1 | 9955 | MIP (proved optimum) | 0 |
| f10x10-r0.2-01 | 10x10 | 0.2 | Optimal | yes | 1.181e+04 | 1.181e+04 | 0.006418 | 1.162 | 7 | 1.181e+04 | MIP (proved optimum) | 0.006418 |
| f10x10-r0.2-02 | 10x10 | 0.2 | Optimal | yes | 1.043e+04 | 1.043e+04 | 6.628e-13 | 1.03 | 3 | 1.043e+04 | MIP (proved optimum) | 6.628e-13 |
| f10x10-r0.2-03 | 10x10 | 0.2 | Optimal | yes | 1.097e+04 | 1.097e+04 | 0 | 0.134 | 1 | 1.097e+04 | MIP (proved optimum) | 0 |
| f10x10-r0.2-04 | 10x10 | 0.2 | Optimal | yes | 1.352e+04 | 1.352e+04 | 0.005586 | 2.477 | 43 | 1.352e+04 | MIP (proved optimum) | 0.005586 |
| f10x10-r1-00 | 10x10 | 1 | Optimal | yes | 2.288e+04 | 2.288e+04 | 4.371e-09 | 0.03906 | 1 | 2.288e+04 | MIP (proved optimum) | 4.371e-09 |
| f10x10-r1-01 | 10x10 | 1 | Optimal | yes | 2.677e+04 | 2.677e+04 | 5.437e-14 | 0.5464 | 1 | 2.677e+04 | MIP (proved optimum) | 5.437e-14 |
| f10x10-r1-02 | 10x10 | 1 | Optimal | yes | 2.035e+04 | 2.035e+04 | 4.914e-09 | 0.5603 | 5 | 2.035e+04 | MIP (proved optimum) | 4.914e-09 |
| f10x10-r1-03 | 10x10 | 1 | Optimal | yes | 2.776e+04 | 2.776e+04 | 0.002 | 1.993 | 207 | 2.776e+04 | MIP (proved optimum) | 0.002 |
| f10x10-r1-04 | 10x10 | 1 | Optimal | yes | 3.157e+04 | 3.157e+04 | 1.083e-12 | 1.85 | 67 | 3.157e+04 | MIP (proved optimum) | 1.083e-12 |
| f15x15-r0.2-00 | 15x15 | 0.2 | Optimal | yes | 1.613e+04 | 1.613e+04 | 0.005108 | 3.763 | 138 | 1.613e+04 | MIP (proved optimum) | 0.005108 |
| f15x15-r0.2-01 | 15x15 | 0.2 | Optimal | yes | 1.427e+04 | 1.427e+04 | 0.006509 | 2.231 | 11 | 1.427e+04 | MIP (proved optimum) | 0.006509 |
| f15x15-r0.2-02 | 15x15 | 0.2 | Optimal | yes | 1.901e+04 | 1.901e+04 | 0 | 3.851 | 63 | 1.901e+04 | MIP (proved optimum) | 0 |
| f15x15-r0.2-03 | 15x15 | 0.2 | Optimal | yes | 1.317e+04 | 1.317e+04 | 5.248e-13 | 0.8322 | 1 | 1.317e+04 | MIP (proved optimum) | 5.248e-13 |
| f15x15-r0.2-04 | 15x15 | 0.2 | Optimal | yes | 1.416e+04 | 1.416e+04 | 0.004708 | 2.664 | 43 | 1.416e+04 | MIP (proved optimum) | 0.004708 |
| f15x15-r1-00 | 15x15 | 1 | Optimal | yes | 4.211e+04 | 4.211e+04 | 0 | 2.729 | 69 | 4.211e+04 | MIP (proved optimum) | 0 |
| f15x15-r1-01 | 15x15 | 1 | Optimal | yes | 3.374e+04 | 3.373e+04 | 0.001641 | 10.36 | 1314 | 3.374e+04 | MIP (proved optimum) | 0.001641 |
| f15x15-r1-02 | 15x15 | 1 | Optimal | yes | 3.598e+04 | 3.598e+04 | 8.089e-14 | 3.054 | 61 | 3.598e+04 | MIP (proved optimum) | 8.089e-14 |
| f15x15-r1-03 | 15x15 | 1 | Optimal | yes | 3.454e+04 | 3.454e+04 | 0 | 9.335 | 1619 | 3.454e+04 | MIP (proved optimum) | 0 |
| f15x15-r1-04 | 15x15 | 1 | Optimal | yes | 4.147e+04 | 4.147e+04 | 0.0002819 | 3.57 | 213 | 4.147e+04 | MIP (proved optimum) | 0.0002819 |
| f20x20-r0.2-00 | 20x20 | 0.2 | Optimal | yes | 2.28e+04 | 2.28e+04 | 0.001274 | 16.52 | 1274 | 2.28e+04 | MIP (proved optimum) | 0.001274 |
| f20x20-r0.2-01 | 20x20 | 0.2 | Optimal | yes | 1.645e+04 | 1.645e+04 | 0.005762 | 17.76 | 1640 | 1.645e+04 | MIP (proved optimum) | 0.005762 |
| f20x20-r0.2-02 | 20x20 | 0.2 | Optimal | yes | 2.002e+04 | 2.002e+04 | 0 | 10.35 | 931 | 2.002e+04 | MIP (proved optimum) | 0 |
| f20x20-r0.2-03 | 20x20 | 0.2 | Optimal | yes | 2.025e+04 | 2.025e+04 | 0 | 16.78 | 744 | 2.025e+04 | MIP (proved optimum) | 0 |
| f20x20-r0.2-04 | 20x20 | 0.2 | Optimal | yes | 1.844e+04 | 1.844e+04 | 0.004007 | 18.21 | 2108 | 1.844e+04 | MIP (proved optimum) | 0.004007 |
| f20x20-r1-00 | 20x20 | 1 | Optimal | yes | 4.022e+04 | 4.022e+04 | 0.001589 | 13.29 | 970 | 4.022e+04 | MIP (proved optimum) | 0.001589 |
| f20x20-r1-01 | 20x20 | 1 | Optimal | yes | 4.205e+04 | 4.205e+04 | 0.00232 | 37.91 | 4846 | 4.205e+04 | MIP (proved optimum) | 0.00232 |
| f20x20-r1-02 | 20x20 | 1 | Optimal | yes | 4.106e+04 | 4.106e+04 | 0.0004859 | 4.195 | 207 | 4.106e+04 | MIP (proved optimum) | 0.0004859 |
| f20x20-r1-03 | 20x20 | 1 | Optimal | yes | 4.765e+04 | 4.765e+04 | 0.001515 | 43.2 | 4694 | 4.765e+04 | MIP (proved optimum) | 0.001515 |
| f20x20-r1-04 | 20x20 | 1 | Optimal | yes | 4.041e+04 | 4.041e+04 | 0.0007297 | 6.473 | 184 | 4.041e+04 | MIP (proved optimum) | 0.0007297 |
| f30x30-r0.2-00 | 30x30 | 0.2 | Time limit reached | no | 2.037e+04 | 1.987e+04 | 2.441 | 60.02 | 1720 | 2.037e+04 | MIP (best solution at the time limit) | 2.441 |
| f30x30-r0.2-01 | 30x30 | 0.2 | Time limit reached | no | 2.694e+04 | 2.612e+04 | 3.052 | 60.04 | 1150 | 2.694e+04 | MIP (best solution at the time limit) | 3.052 |
| f30x30-r0.2-02 | 30x30 | 0.2 | Time limit reached | no | 2.031e+04 | 1.997e+04 | 1.679 | 60.01 | 1339 | 2.031e+04 | MIP (best solution at the time limit) | 1.679 |
| f30x30-r0.2-03 | 30x30 | 0.2 | Time limit reached | no | 2.129e+04 | 2.094e+04 | 1.641 | 60.01 | 1718 | 2.129e+04 | MIP (best solution at the time limit) | 1.641 |
| f30x30-r0.2-04 | 30x30 | 0.2 | Time limit reached | no | 2.204e+04 | 2.151e+04 | 2.424 | 60.01 | 1377 | 2.204e+04 | MIP (best solution at the time limit) | 2.424 |
| f30x30-r1-00 | 30x30 | 1 | Time limit reached | no | 5.518e+04 | 5.446e+04 | 1.311 | 60.03 | 3250 | 5.518e+04 | MIP (best solution at the time limit) | 1.311 |
| f30x30-r1-01 | 30x30 | 1 | Time limit reached | no | 5.291e+04 | 5.204e+04 | 1.651 | 60 | 2459 | 5.291e+04 | MIP (best solution at the time limit) | 1.651 |
| f30x30-r1-02 | 30x30 | 1 | Time limit reached | no | 5.221e+04 | 5.075e+04 | 2.801 | 60.01 | 1912 | 5.221e+04 | MIP (best solution at the time limit) | 2.801 |
| f30x30-r1-03 | 30x30 | 1 | Time limit reached | no | 5.557e+04 | 5.368e+04 | 3.395 | 60.01 | 1898 | 5.557e+04 | MIP (best solution at the time limit) | 3.395 |
| f30x30-r1-04 | 30x30 | 1 | Time limit reached | no | 4.577e+04 | 4.494e+04 | 1.808 | 60.01 | 2200 | 4.577e+04 | MIP (best solution at the time limit) | 1.808 |
