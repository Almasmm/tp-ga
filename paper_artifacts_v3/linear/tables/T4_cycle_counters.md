# Cycle mutation inside the GA runs

Pivots made by the cycle mutation in the main runs, the pivots with theta = 0 and the offspring whose pivots all had theta = 0 (their plan is the plan decoded before the mutation).

| set | size | method | config | runs | offspring | pivots | pivots_theta_zero | share_pivots_theta_zero | offspring_all_pivots_theta_zero | share_offspring_all_pivots_theta_zero |
|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 482800 | 965600 | 15786 | 0.01635 | 2623 | 0.005433 |
| uniform | 10x10 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 1973800 | 3947600 | 319828 | 0.08102 | 48360 | 0.0245 |
| uniform | 10x10 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 100 | 1617000 | 1617000 | 93060 | 0.05755 | 93060 | 0.05755 |
| uniform | 20x20 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 7980400 | 15960800 | 4128996 | 0.2587 | 905122 | 0.1134 |
| uniform | 20x20 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 100 | 7546000 | 7546000 | 1158477 | 0.1535 | 1158477 | 0.1535 |
| uniform | 30x30 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 17977200 | 35954400 | 14052209 | 0.3908 | 3526926 | 0.1962 |
| uniform | 30x30 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 100 | 17517500 | 17517500 | 4695280 | 0.268 | 4695280 | 0.268 |
| uniform | 50x50 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 49984000 | 99968000 | 54561837 | 0.5458 | 16482933 | 0.3298 |
| uniform | 50x50 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 100 | 49588000 | 49588000 | 22403612 | 0.4518 | 22403612 | 0.4518 |
| uniform | 100x100 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 50 | 99989300 | 199978600 | 147043774 | 0.7353 | 55979344 | 0.5599 |
| uniform | 100x100 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 50 | 99849750 | 99849750 | 64903840 | 0.65 | 64903840 | 0.65 |
| structured | 20x20 | GA-rand-cycle | P143-pc0.97724-t5-e1-cycle:2-random-budget | 100 | 7980400 | 15960800 | 3498230 | 0.2192 | 700404 | 0.08777 |
| structured | 20x20 | GA-cost-cycle | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | 100 | 7546000 | 7546000 | 1311767 | 0.1738 | 1311767 | 0.1738 |
