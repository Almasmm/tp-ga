# T4b. Tests of the factorial plan

| size | initialization | test | blocks | treatments | statistic | p | best_mean_rank | best_rank | rank_biserial_r | cliffs_delta | p_holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20x20 | cost-aware | Friedman over population x mutation | 10 | 16 | 142.164 | 8.604e-23 | P=200.0 pm=0.2 | 1.200 | – | – | – |
| 20x20 | cost-aware | Friedman over population | 10 | 4 | 30.000 | 1.380e-06 | population=200.0 | 1.000 | – | – | – |
| 20x20 | cost-aware | Wilcoxon post-hoc population 20 vs 50 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.440 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc population 20 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.760 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc population 20 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.960 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc population 50 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.360 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc population 50 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.680 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc population 100 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.420 | 0.023 |
| 20x20 | cost-aware | Friedman over mutation_rate | 10 | 4 | 25.041 | 1.514e-05 | mutation_rate=0.2 | 1.250 | – | – | – |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.05 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.270 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.1 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.380 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.460 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.05 vs 0.1 | 10 | 2 | 9.000 | 0.064 | – | – | 0.673 | 0.120 | 0.064 |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.05 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.260 | 0.023 |
| 20x20 | cost-aware | Wilcoxon post-hoc mutation_rate 0.1 vs 0.2 | 10 | 2 | 3.000 | 0.020 | – | – | 0.867 | 0.210 | 0.039 |
| 20x20 | random | Friedman over population x mutation | 10 | 16 | 147.291 | 8.317e-24 | P=200.0 pm=0.2 | 1.000 | – | – | – |
| 20x20 | random | Friedman over population | 10 | 4 | 30.000 | 1.380e-06 | population=200.0 | 1.000 | – | – | – |
| 20x20 | random | Wilcoxon post-hoc population 20 vs 50 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.940 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc population 20 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc population 20 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc population 50 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.800 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc population 50 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.980 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc population 100 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.580 | 0.023 |
| 20x20 | random | Friedman over mutation_rate | 10 | 4 | 30.000 | 1.380e-06 | mutation_rate=0.2 | 1.000 | – | – | – |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.05 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.920 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.1 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.05 vs 0.1 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.640 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.05 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.880 | 0.023 |
| 20x20 | random | Wilcoxon post-hoc mutation_rate 0.1 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.520 | 0.023 |
| 50x50 | cost-aware | Friedman over population x mutation | 10 | 16 | 128.080 | 5.049e-20 | P=200.0 pm=0.2 | 1.400 | – | – | – |
| 50x50 | cost-aware | Friedman over population | 10 | 4 | 27.000 | 5.887e-06 | population=200.0 | 1.150 | – | – | – |
| 50x50 | cost-aware | Wilcoxon post-hoc population 20 vs 50 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.190 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc population 20 vs 100 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.290 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc population 20 vs 200 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.390 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc population 50 vs 100 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.230 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc population 50 vs 200 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.290 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc population 100 vs 200 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.210 | 0.047 |
| 50x50 | cost-aware | Friedman over mutation_rate | 10 | 4 | 26.455 | 7.660e-06 | mutation_rate=0.2 | 1.200 | – | – | – |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.05 | 10 | 2 | 0 | 0.008 | – | – | 1.000 | 0.140 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.1 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.190 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.01 vs 0.2 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.290 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.05 vs 0.1 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.130 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.05 vs 0.2 | 10 | 2 | 0 | 0.004 | – | – | 1.000 | 0.210 | 0.047 |
| 50x50 | cost-aware | Wilcoxon post-hoc mutation_rate 0.1 vs 0.2 | 10 | 2 | 0 | 0.008 | – | – | 1.000 | 0.160 | 0.047 |
| 50x50 | random | Friedman over population x mutation | 10 | 16 | 148.976 | 3.852e-24 | P=200.0 pm=0.2 | 1.000 | – | – | – |
| 50x50 | random | Friedman over population | 10 | 4 | 30.000 | 1.380e-06 | population=200.0 | 1.000 | – | – | – |
| 50x50 | random | Wilcoxon post-hoc population 20 vs 50 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc population 20 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc population 20 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc population 50 vs 100 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.980 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc population 50 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc population 100 vs 200 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.980 | 0.023 |
| 50x50 | random | Friedman over mutation_rate | 10 | 4 | 30.000 | 1.380e-06 | mutation_rate=0.2 | 1.000 | – | – | – |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.05 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.1 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.01 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.05 vs 0.1 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.860 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.05 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 1.000 | 0.023 |
| 50x50 | random | Wilcoxon post-hoc mutation_rate 0.1 vs 0.2 | 10 | 2 | 0 | 0.002 | – | – | 1.000 | 0.840 | 0.023 |
| 20x20 | cost-aware vs random | Wilcoxon over (instance, population, mutation) cells | 160 | 2 | 0 | 5.240e-28 | – | – | -1.000 | -1.000 | – |
| 50x50 | cost-aware vs random | Wilcoxon over (instance, population, mutation) cells | 160 | 2 | 0 | 5.240e-28 | – | – | -1.000 | -1.000 | – |
