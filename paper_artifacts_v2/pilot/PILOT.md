# Pilot estimate of the v0.4 run

| Phase | Runs | Estimated wall time, h | Share |
|---|---|---|---|
| reference | 712 | 0.00 | 0.0 % |
| representation | 2,100 | 53.49 | 57.5 % |
| main | 23,600 | 35.60 | 38.3 % |
| applied | 1,075 | 1.01 | 1.1 % |
| &nbsp;&nbsp;applied: astana | 825 | 1.01 | |
| &nbsp;&nbsp;applied: wheat | 250 | 0.00 | |
| factorial | 24,000 | 0.99 | 1.1 % |
| stagnation | 1,800 | 1.09 | 1.2 % |
| legacy | 1,800 | 0.67 | 0.7 % |
| timing | 380 | 0.16 | 0.2 % |
| **total** | 55,467 | **93.02** | 100 % |

* E/P speed ratio (same GA task): 1.34; quality phases use 20.0 performance-core equivalents, the timing phase 8 performance cores.
* Monitor overhead (1 Hz status through a queue): -3.17 % (0.518 s without, 0.502 s with).
* Phases with a stagnation stop are estimated with the full budget (upper bound).

## Largest items

| Phase | Item | h |
|---|---|---|
| representation | uniform 200x200 GA-cost-tuned | 49.07 |
| main | uniform 200x200 GA-cost-tuned | 25.01 |
| representation | uniform 200x200 GA-rand-tuned | 2.68 |
| main | uniform 200x200 RS | 2.06 |
| main | uniform 200x200 GA-rand-tuned | 1.60 |
| representation | uniform 100x100 GA-cost-tuned | 1.31 |
| main | uniform 100x100 GA-cost-tuned | 1.20 |
| main | structured 100x100 GA-cost-tuned | 1.17 |
| main | uniform 200x200 SA-cost-tuned | 0.80 |
| main | uniform 200x200 SA-rand-tuned | 0.75 |
| applied | astana 24x324 GA-cost-tuned | 0.60 |
| stagnation | uniform 100x100 GA-cost-tuned | 0.60 |

## Memory

Memory runs may use: 6.3 GiB (smaller of free RAM and free commit when the estimate was made, less the reserve). A run starts only while its memory is free; the times above include the slowdown where fewer runs fit at once.

| Phase | Set | Size | Method | GiB per run | Runs at once |
|---|---|---|---|---|---|
| applied | astana | 24x324 | GA-cost-tuned | 0.62 | 10 of 24 |
| main | skewed | 50x50 | GA-cost-tuned | 0.30 | 21 of 24 |
| main | structured | 100x100 | GA-cost-tuned | 0.75 | 8 of 24 |
| main | structured | 50x50 | GA-cost-tuned | 0.30 | 21 of 24 |
| main | ties | 50x50 | GA-cost-tuned | 0.30 | 21 of 24 |
| main | uniform | 100x100 | GA-cost-tuned | 0.75 | 8 of 24 |
| main | uniform | 200x200 | GA-cost-tuned | 2.56 | 2 of 24 |
| main | uniform | 200x200 | GA-rand-tuned | 0.27 | 22 of 24 |
| main | uniform | 50x50 | GA-cost-tuned | 0.30 | 21 of 24 |
| representation | skewed | 50x50 | GA-cost-tuned | 0.50 | 12 of 24 |
| representation | structured | 50x50 | GA-cost-tuned | 0.50 | 12 of 24 |
| representation | ties | 50x50 | GA-cost-tuned | 0.50 | 12 of 24 |
| representation | uniform | 100x100 | GA-cost-tuned | 1.55 | 4 of 24 |
| representation | uniform | 100x100 | random-parents | 0.30 | 21 of 24 |
| representation | uniform | 200x200 | GA-cost-tuned | 5.78 | 1 of 24 |
| representation | uniform | 200x200 | GA-rand-tuned | 0.44 | 14 of 24 |
| representation | uniform | 200x200 | random-parents | 0.74 | 8 of 24 |
| representation | uniform | 30x30 | GA-cost-tuned | 0.27 | 22 of 24 |
| representation | uniform | 50x50 | GA-cost-tuned | 0.50 | 12 of 24 |
| stagnation | uniform | 100x100 | GA-cost-tuned | 0.75 | 8 of 24 |
| stagnation | uniform | 50x50 | GA-cost-tuned | 0.30 | 21 of 24 |
| timing | lp_scaling | 1000x1000 | LP | 1.08 | 5 of 8 |
| timing | lp_scaling | 1000x1000 | LP-ortools | 1.08 | 5 of 8 |

## Possible reductions (choose; not applied)

| Option | Saves, h |
|---|---|
| budget cap 1,000,000 decoder calls (shortens runs at 24x324, 100x100, 200x200) | 12.15 |
| budget cap 2,000,000 decoder calls (shortens runs at 200x200) | 8.08 |
| budget cap 4,000,000 decoder calls (shortens runs at 200x200) | 5.39 |
| factorial plan without population 400 | 0.22 |
| 200x200 in the main phase with 10 runs instead of 30 | 0.00 |
| drop the base GA configurations at 200x200 | 0.00 |
| timing phase without 200x200 for GA and SA | 0.00 |
