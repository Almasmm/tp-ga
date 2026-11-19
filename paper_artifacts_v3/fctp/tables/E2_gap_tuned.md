# FCTP: the variants chosen on FCTP training instances against the variants of 8.4

gap = 100 (Z - Z_best) / Z_best on the 40 instances of 8.4. Z_best follows the rule of 8.4 and includes the runs of this table and the MIP runs of E4; `z_best_lowered_on` counts the instances of the cell where that lowered Z_best. GA-cost-cycle and GA-hybrid have the parameters of 8.4; the `-ft` variants have the population, pivots and local-search period of E1.

| size | rho | method | config | instances | runs | gap_median | gap_instance_median | gap_mean | gap_min | gap_max | share_at_z_best | time_median_s | generations_median | local_search_calls_mean | local_search_evaluations_mean | local_search_improvements_mean | z_best_lowered_on |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10x10 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 0.7911 | 0.8423 | 1.063 | 0 | 3.538 | 0.24 | 0.06686 | 6 | 0 | 0 | 0 | 0 |
| 10x10 | 0.2 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 0.7911 | 0.8423 | 1.063 | 0 | 3.538 | 0.24 | 0.06869 | 6 | 0 | 0 | 0 | 0 |
| 10x10 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 0 | 0 | 0.08611 | 0 | 1.084 | 0.9 | 0.05727 | 66 | 0 | 0 | 0 | 0 |
| 10x10 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 0 | 0 | 0.1169 | 0 | 1.084 | 0.84 | 0.05434 | 61 | 20 | 1444 | 3.38 | 0 |
| 10x10 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 1.084 | 1.171 | 1.254 | 0 | 4.112 | 0.28 | 0.06625 | 6 | 0 | 0 | 0 | 0 |
| 10x10 | 1 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 1.084 | 1.171 | 1.254 | 0 | 4.112 | 0.28 | 0.06759 | 6 | 0 | 0 | 0 | 0 |
| 10x10 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 0 | 0 | 1.012 | 0 | 4.842 | 0.54 | 0.05821 | 66 | 0 | 0 | 0 | 0 |
| 10x10 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 0 | 0 | 0.858 | 0 | 4.079 | 0.52 | 0.0551 | 61 | 20 | 1516 | 2.44 | 0 |
| 15x15 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 0.9784 | 1.059 | 1.294 | 0 | 5.461 | 0.16 | 0.2035 | 15 | 0 | 0 | 0 | 0 |
| 15x15 | 0.2 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 0.9784 | 1.044 | 1.295 | 0 | 5.201 | 0.16 | 0.2089 | 15 | 1 | 85.56 | 0.8 | 0 |
| 15x15 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 0.6628 | 0.7556 | 1.184 | 0 | 6.484 | 0.26 | 0.1817 | 151 | 0 | 0 | 0 | 0 |
| 15x15 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 0.6628 | 0.8227 | 1.373 | 0 | 6.484 | 0.24 | 0.1546 | 126 | 41.82 | 7418 | 5.58 | 0 |
| 15x15 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 1.394 | 1.354 | 2.026 | 0 | 4.4 | 0.1 | 0.1986 | 15 | 0 | 0 | 0 | 0 |
| 15x15 | 1 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 1.367 | 1.354 | 2.025 | 0 | 4.31 | 0.12 | 0.2044 | 15 | 1 | 106.5 | 0.76 | 0 |
| 15x15 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 2.324 | 2.324 | 2.544 | 0 | 7.085 | 0.06 | 0.1759 | 151 | 0 | 0 | 0 | 0 |
| 15x15 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 1.996 | 1.826 | 2.524 | 0 | 6.349 | 0.04 | 0.1502 | 126 | 41.88 | 7308 | 6.38 | 0 |
| 20x20 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 1.785 | 1.865 | 1.858 | 0 | 4.386 | 0.08 | 0.4816 | 28 | 0 | 0 | 0 | 0 |
| 20x20 | 0.2 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 1.85 | 2.448 | 2.002 | 0 | 5.078 | 0.08 | 0.5074 | 28 | 2 | 268.6 | 1.56 | 0 |
| 20x20 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 2.057 | 1.785 | 2.548 | 0 | 6.255 | 0.08 | 0.4045 | 270 | 0 | 0 | 0 | 0 |
| 20x20 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 2.307 | 2.45 | 2.488 | 0 | 6.174 | 0.08 | 0.3039 | 198 | 66 | 2.098e+04 | 10.22 | 0 |
| 20x20 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 4.32 | 3.6 | 4.248 | 0.828 | 8.182 | 0 | 0.4847 | 28 | 0 | 0 | 0 | 0 |
| 20x20 | 1 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 4.069 | 3.696 | 4.206 | 0.5285 | 8.182 | 0 | 0.5137 | 28 | 2 | 244.6 | 1.66 | 0 |
| 20x20 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 4.559 | 4.568 | 4.972 | 0.4003 | 12.52 | 0 | 0.4175 | 270 | 0 | 0 | 0 | 0 |
| 20x20 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 4.709 | 4.781 | 5.086 | 0 | 11.16 | 0.02 | 0.3116 | 199 | 66.2 | 2.081e+04 | 11.12 | 0 |
| 30x30 | 0.2 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 5.677 | 4.786 | 5.467 | 1.522 | 10.89 | 0 | 1.587 | 65 | 0 | 0 | 0 | 0 |
| 30x30 | 0.2 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 5.704 | 5.281 | 5.454 | 1.447 | 10.38 | 0 | 1.74 | 64 | 6 | 3055 | 2.94 | 0 |
| 30x30 | 0.2 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 5.118 | 5.021 | 5.314 | 1.139 | 9.747 | 0 | 1.497 | 609 | 0 | 0 | 0 | 0 |
| 30x30 | 0.2 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 5.804 | 4.916 | 5.958 | 1.139 | 11.41 | 0 | 0.8458 | 330 | 110 | 8.216e+04 | 15.36 | 0 |
| 30x30 | 1 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 5 | 50 | 7.144 | 7.337 | 7.788 | 3.293 | 15.21 | 0 | 1.652 | 65 | 0 | 0 | 0 | 1 |
| 30x30 | 1 | GA-hybrid | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | 5 | 50 | 7.4 | 8.395 | 7.758 | 1.868 | 12.76 | 0 | 1.755 | 64 | 6 | 3006 | 3.06 | 1 |
| 30x30 | 1 | GA-cost-cycle-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | 5 | 50 | 7.289 | 7.214 | 7.258 | 1.81 | 14.41 | 0 | 1.485 | 609 | 0 | 0 | 0 | 1 |
| 30x30 | 1 | GA-hybrid-ft | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | 5 | 50 | 6.959 | 7.982 | 7.342 | 3.088 | 13.08 | 0 | 0.8281 | 333 | 111 | 8.127e+04 | 17.96 | 1 |
