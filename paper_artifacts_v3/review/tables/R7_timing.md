# FCTP: time with one run at a time on one logical processor (amendment 10.4)

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Processor 2 (process bound to it: True), no other run of the experiment active; 5 seeds per instance. The MIP run of an instance (1 thread) has the median time of its five GA-cost-cycle runs of this block as its limit. `decoder_or_start_evaluations`: decoder calls of the GA, or the one evaluation of the start plan of Tabu and ILS; `neighbour_evaluations`: the separate counter of the local searches; their sum is B = 200 m n. `better/equal/worse_than_mip`: the median cost of the method on an instance against the cost of that MIP plan. `time_20_at_once_median_s`: the same method on the same instances in the runs made with 20 at once.

| size | rho | method | instances | runs | time_one_processor_median_s | time_20_at_once_median_s | decoder_or_start_evaluations | neighbour_evaluations | gap_median | better_than_mip | equal_to_mip | worse_than_mip | mip_no_plan | time_limit_median_s | mip_proved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10x10 | 0.2 | GA-cost-cycle | 3 | 15 | 0.05611 | 0.0668 | 18870 | 0 | 0.3809 | 2 | 1 | 0 | 0 | – | – |
| 10x10 | 0.2 | Tabu | 3 | 15 | 0.007827 | 0.01004 | 1 | 19999 | 1.295 | 2 | 0 | 1 | 0 | – | – |
| 10x10 | 0.2 | ILS | 3 | 15 | 0.005634 | 0.007235 | 1 | 19999 | 0 | 2 | 1 | 0 | 0 | – | – |
| 10x10 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.05861 | – | – | – | 1.515 | – | – | – | 0 | 0.05632 | 0 |
| 10x10 | 1 | GA-cost-cycle | 3 | 15 | 0.0547 | 0.06469 | 18870 | 0 | 0.7518 | 2 | 1 | 0 | 0 | – | – |
| 10x10 | 1 | Tabu | 3 | 15 | 0.007579 | 0.009883 | 1 | 19999 | 0 | 2 | 1 | 0 | 0 | – | – |
| 10x10 | 1 | ILS | 3 | 15 | 0.005614 | 0.007531 | 1 | 19999 | 0 | 2 | 1 | 0 | 0 | – | – |
| 10x10 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.05669 | – | – | – | 12.27 | – | – | – | 0 | 0.05438 | 1 |
| 15x15 | 0.2 | GA-cost-cycle | 3 | 15 | 0.1699 | 0.2053 | 43125 | 0 | 0.6628 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 0.2 | Tabu | 3 | 15 | 0.01453 | 0.01763 | 1 | 44999 | 0.09468 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 0.2 | ILS | 3 | 15 | 0.01204 | 0.0145 | 1 | 44999 | 0 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.1781 | – | – | – | 6.912 | – | – | – | 0 | 0.1709 | 0 |
| 15x15 | 1 | GA-cost-cycle | 3 | 15 | 0.1691 | 0.1999 | 43125 | 0 | 1.977 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 1 | Tabu | 3 | 15 | 0.01454 | 0.01788 | 1 | 44999 | 1.938 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 1 | ILS | 3 | 15 | 0.01219 | 0.01455 | 1 | 44999 | 0 | 3 | 0 | 0 | 0 | – | – |
| 15x15 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.1711 | – | – | – | 13.11 | – | – | – | 0 | 0.1691 | 0 |
| 20x20 | 0.2 | GA-cost-cycle | 3 | 15 | 0.3859 | 0.4789 | 78160 | 0 | 1.785 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 0.2 | Tabu | 3 | 15 | 0.02517 | 0.02896 | 1 | 79999 | 0.3347 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 0.2 | ILS | 3 | 15 | 0.02182 | 0.02455 | 1 | 79999 | 0.2939 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.3996 | – | – | – | 7.43 | – | – | – | 0 | 0.3859 | 0 |
| 20x20 | 1 | GA-cost-cycle | 3 | 15 | 0.3906 | 0.4831 | 78160 | 0 | 2.939 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 1 | Tabu | 3 | 15 | 0.0247 | 0.03102 | 1 | 79999 | 0.6992 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 1 | ILS | 3 | 15 | 0.02133 | 0.02626 | 1 | 79999 | 0.5945 | 3 | 0 | 0 | 0 | – | – |
| 20x20 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 0.3992 | – | – | – | 20.92 | – | – | – | 0 | 0.3919 | 0 |
| 30x30 | 0.2 | GA-cost-cycle | 3 | 15 | 1.342 | 1.551 | 177875 | 0 | 5.4 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 0.2 | Tabu | 3 | 15 | 0.05875 | 0.06463 | 1 | 179999 | 1.974 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 0.2 | ILS | 3 | 15 | 0.05306 | 0.05917 | 1 | 179999 | 0.9455 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 1.362 | – | – | – | 12.29 | – | – | – | 0 | 1.348 | 0 |
| 30x30 | 1 | GA-cost-cycle | 3 | 15 | 1.355 | 1.655 | 177875 | 0 | 5.792 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 1 | Tabu | 3 | 15 | 0.05879 | 0.06671 | 1 | 179999 | 2.236 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 1 | ILS | 3 | 15 | 0.05391 | 0.05878 | 1 | 179999 | 1.946 | 3 | 0 | 0 | 0 | – | – |
| 30x30 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 1.358 | – | – | – | 19.41 | – | – | – | 0 | 1.337 | 0 |
| 50x50 | 0.2 | GA-cost-cycle | 3 | 15 | 8.087 | 11.51 | 498580 | 0 | 8.723 | 0 | 0 | 3 | 0 | – | – |
| 50x50 | 0.2 | Tabu | 3 | 15 | 0.2011 | 0.2654 | 1 | 499999 | 4.851 | 1 | 0 | 2 | 0 | – | – |
| 50x50 | 0.2 | ILS | 3 | 15 | 0.1849 | 0.2253 | 1 | 499999 | 2.194 | 3 | 0 | 0 | 0 | – | – |
| 50x50 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 8.1 | – | – | – | 3.639 | – | – | – | 0 | 8.087 | 0 |
| 50x50 | 1 | GA-cost-cycle | 3 | 15 | 7.971 | 11.48 | 498580 | 0 | 11.47 | 1 | 0 | 2 | 0 | – | – |
| 50x50 | 1 | Tabu | 3 | 15 | 0.1997 | 0.2264 | 1 | 499999 | 4.322 | 1 | 0 | 2 | 0 | – | – |
| 50x50 | 1 | ILS | 3 | 15 | 0.1826 | 0.2018 | 1 | 499999 | 2.371 | 1 | 0 | 2 | 0 | – | – |
| 50x50 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 8.156 | – | – | – | 2.138 | – | – | – | 0 | 8.147 | 0 |
| 70x70 | 0.2 | GA-cost-cycle | 3 | 15 | 26.74 | 39.89 | 978290 | 0 | 10.64 | 0 | 0 | 3 | 0 | – | – |
| 70x70 | 0.2 | Tabu | 3 | 15 | 0.4838 | 0.5413 | 1 | 979999 | 3.598 | 0 | 0 | 3 | 0 | – | – |
| 70x70 | 0.2 | ILS | 3 | 15 | 0.4323 | 0.4727 | 1 | 979999 | 1.494 | 1 | 0 | 2 | 0 | – | – |
| 70x70 | 0.2 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 26.87 | – | – | – | 1.312 | – | – | – | 0 | 26.85 | 0 |
| 70x70 | 1 | GA-cost-cycle | 3 | 15 | 25.63 | 42.7 | 978290 | 0 | 12.37 | 0 | 0 | 3 | 0 | – | – |
| 70x70 | 1 | Tabu | 3 | 15 | 0.4801 | 0.5172 | 1 | 979999 | 4.488 | 0 | 0 | 3 | 0 | – | – |
| 70x70 | 1 | ILS | 3 | 15 | 0.4349 | 0.4597 | 1 | 979999 | 2.697 | 1 | 0 | 2 | 0 | – | – |
| 70x70 | 1 | MIP, limit = time of GA-cost-cycle | 3 | 3 | 25.64 | – | – | – | 1.842 | – | – | – | 0 | 25.63 | 0 |
