# FCTP: grids of Tabu and ILS on the training instances (amendment 10.1)

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Mean training gap (%) over the 8 training instances of 9.2 and 3 seeds; the reference of an instance is its MIP value of 9.2 or a smaller value of a run of the grid of 9.2 or of these grids. `rank` is the order of the tie rule; `selected` marks the configuration with the smallest mean gap.

| method | rank | config | sample | tenure | runs | mean_gap | time_median_s | selected | perturbation | acceptance |
|---|---|---|---|---|---|---|---|---|---|---|
| Tabu | 0 | tabu-s1-T5 | 1 | 5 | 24 | 3.553 | 0.03672 | no | – | – |
| Tabu | 1 | tabu-s1-T10 | 1 | 10 | 24 | 3.319 | 0.03632 | no | – | – |
| Tabu | 2 | tabu-s1-T20 | 1 | 20 | 24 | 4.659 | 0.03671 | no | – | – |
| Tabu | 3 | tabu-s0.25-T5 | 0.25 | 5 | 24 | 3.113 | 0.04433 | yes | – | – |
| Tabu | 4 | tabu-s0.25-T10 | 0.25 | 10 | 24 | 3.896 | 0.04387 | no | – | – |
| Tabu | 5 | tabu-s0.25-T20 | 0.25 | 20 | 24 | 5.436 | 0.04337 | no | – | – |
| Tabu | 6 | tabu-s0.05-T5 | 0.05 | 5 | 24 | 4.714 | 0.06591 | no | – | – |
| Tabu | 7 | tabu-s0.05-T10 | 0.05 | 10 | 24 | 8.311 | 0.06516 | no | – | – |
| Tabu | 8 | tabu-s0.05-T20 | 0.05 | 20 | 24 | 9.264 | 0.0643 | no | – | – |
| ILS | 0 | ils-p2-better | – | – | 24 | 1.96 | 0.0398 | no | 2 | better |
| ILS | 1 | ils-p2-always | – | – | 24 | 2.776 | 0.03899 | no | 2 | always |
| ILS | 2 | ils-p4-better | – | – | 24 | 2.07 | 0.03962 | no | 4 | better |
| ILS | 3 | ils-p4-always | – | – | 24 | 2.841 | 0.0392 | no | 4 | always |
| ILS | 4 | ils-p8-better | – | – | 24 | 1.789 | 0.04041 | yes | 8 | better |
| ILS | 5 | ils-p8-always | – | – | 24 | 2.646 | 0.03956 | no | 8 | always |
| ILS | 6 | ils-p16-better | – | – | 24 | 1.85 | 0.04126 | no | 16 | better |
| ILS | 7 | ils-p16-always | – | – | 24 | 3.708 | 0.04151 | no | 16 | always |
