# External FCTP benchmark: gap of every method

Source: MIPLIB 2017, https://miplib.zib.de (instances gr4x6, ran13x13, ran12x21; objective values as listed on the instance pages on 2026-11-19). gap = 100 (Z - listed objective) / listed objective. Same methods, parameters, budget (200 m n) and seeds as in the generated FCTP set; three instances, so no test is made.

| instance | size | method | runs | listed_objective | cost_median | cost_min | gap_median | gap_min | gap_max | runs_at_listed_objective | time_median_s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| gr4x6 | 4x6 | Balinski | 1 | 202.3 | 229.1 | 229.1 | 13.19 | 13.19 | 13.19 | 0 | 0.01145 |
| gr4x6 | 4x6 | VAM-lin | 1 | 202.3 | 227.8 | 227.8 | 12.6 | 12.6 | 12.6 | 0 | 0.0005572 |
| gr4x6 | 4x6 | RS | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.001997 |
| gr4x6 | 4x6 | GA-rand-tuned | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.003291 |
| gr4x6 | 4x6 | GA-rand-cycle | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.009128 |
| gr4x6 | 4x6 | GA-cost-cycle | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.009611 |
| gr4x6 | 4x6 | SA-rand-tuned | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.001707 |
| gr4x6 | 4x6 | GA-hybrid | 10 | 202.3 | 202.3 | 202.3 | 0 | 0 | 0 | 10 | 0.01053 |
| ran13x13 | 13x13 | Balinski | 1 | 3252 | 3521 | 3521 | 8.272 | 8.272 | 8.272 | 0 | 0.01167 |
| ran13x13 | 13x13 | VAM-lin | 1 | 3252 | 4014 | 4014 | 23.43 | 23.43 | 23.43 | 0 | 0.0008198 |
| ran13x13 | 13x13 | RS | 10 | 3252 | 4352 | 4170 | 33.84 | 28.23 | 36.35 | 0 | 0.06323 |
| ran13x13 | 13x13 | GA-rand-tuned | 10 | 3252 | 3412 | 3271 | 4.92 | 0.5843 | 11.9 | 0 | 0.04981 |
| ran13x13 | 13x13 | GA-rand-cycle | 10 | 3252 | 3390 | 3326 | 4.228 | 2.276 | 8.456 | 0 | 0.1195 |
| ran13x13 | 13x13 | GA-cost-cycle | 10 | 3252 | 3338 | 3304 | 2.66 | 1.599 | 4.397 | 0 | 0.1306 |
| ran13x13 | 13x13 | SA-rand-tuned | 10 | 3252 | 3458 | 3276 | 6.319 | 0.738 | 9.902 | 0 | 0.0495 |
| ran13x13 | 13x13 | GA-hybrid | 10 | 3252 | 3338 | 3304 | 2.645 | 1.599 | 4.643 | 0 | 0.1427 |
| ran12x21 | 12x21 | Balinski | 1 | 3664 | 4080 | 4080 | 11.35 | 11.35 | 11.35 | 0 | 0.01222 |
| ran12x21 | 12x21 | VAM-lin | 1 | 3664 | 4470 | 4470 | 22 | 22 | 22 | 0 | 0.0009791 |
| ran12x21 | 12x21 | RS | 10 | 3664 | 5296 | 5066 | 44.53 | 38.26 | 46.29 | 0 | 0.3302 |
| ran12x21 | 12x21 | GA-rand-tuned | 10 | 3664 | 4040 | 3782 | 10.25 | 3.221 | 16.43 | 0 | 0.3395 |
| ran12x21 | 12x21 | GA-rand-cycle | 10 | 3664 | 4038 | 3853 | 10.22 | 5.158 | 13.32 | 0 | 0.247 |
| ran12x21 | 12x21 | GA-cost-cycle | 10 | 3664 | 3762 | 3675 | 2.675 | 0.3002 | 2.948 | 0 | 0.2108 |
| ran12x21 | 12x21 | SA-rand-tuned | 10 | 3664 | 4038 | 3748 | 10.21 | 2.293 | 14.47 | 0 | 0.06967 |
| ran12x21 | 12x21 | GA-hybrid | 10 | 3664 | 3762 | 3675 | 2.675 | 0.3002 | 2.948 | 0 | 0.2297 |
