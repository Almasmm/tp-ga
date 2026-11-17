# Pilot estimate of the v0.4 run

| Phase | Runs | Estimated wall time, h | Share |
|---|---|---|---|
| reference | 712 | 0.00 | 0.0 % |
| representation | 2,100 | 55.10 | 39.1 % |
| main | 28,000 | 68.46 | 48.6 % |
| applied | 1,900 | 2.54 | 1.8 % |
| &nbsp;&nbsp;applied: wheat | 250 | 0.00 | |
| &nbsp;&nbsp;applied: astana | 1,650 | 2.54 | |
| factorial | 72,000 | 2.97 | 2.1 % |
| stagnation | 5,400 | 3.89 | 2.8 % |
| legacy | 1,800 | 0.67 | 0.5 % |
| timing | 425 | 7.27 | 5.2 % |
| **total** | 112,337 | **140.90** | 100 % |

* E/P speed ratio (same GA task): 1.34; quality phases use 20.0 performance-core equivalents, the timing phase 8 performance cores.
* Monitor overhead (1 Hz status through a queue): -3.17 % (0.518 s without, 0.502 s with).
* Phases with a stagnation stop are estimated with the full budget (upper bound).

## Largest items

| Phase | Item | h |
|---|---|---|
| main | uniform 200x200 GA-cost-tuned | 50.03 |
| representation | uniform 200x200 GA-cost-tuned | 49.07 |
| representation | uniform 200x200 GA-rand-tuned | 3.76 |
| timing | uniform 200x200 GA-cost-tuned | 6.25 |
| main | uniform 100x100 GA-cost-tuned | 2.39 |
| stagnation | uniform 100x100 GA-cost-tuned | 2.39 |
| main | structured 100x100 GA-cost-tuned | 2.34 |
| main | uniform 200x200 GA-rand-tuned | 2.08 |
| main | uniform 200x200 RS | 2.06 |
| main | uniform 200x200 GA-cost-base | 1.80 |
| representation | uniform 100x100 GA-cost-tuned | 1.74 |
| applied | astana 24x324 GA-cost-tuned | 1.73 |

## Memory

Memory runs may use: 4.8 GiB (smaller of free RAM and free commit when the estimate was made, less the reserve). A run starts only while its memory is free; the times above include the slowdown where fewer runs fit at once.

| Phase | Set | Size | Method | GiB per run | Runs at once |
|---|---|---|---|---|---|
| applied | astana | 24x324 | GA-cost-tuned | 0.62 | 7 of 24 |
| main | skewed | 50x50 | GA-cost-tuned | 0.30 | 16 of 24 |
| main | structured | 100x100 | GA-cost-tuned | 0.75 | 6 of 24 |
| main | structured | 50x50 | GA-cost-tuned | 0.30 | 16 of 24 |
| main | ties | 50x50 | GA-cost-tuned | 0.30 | 16 of 24 |
| main | uniform | 100x100 | GA-cost-tuned | 0.75 | 6 of 24 |
| main | uniform | 200x200 | GA-cost-base | 0.24 | 20 of 24 |
| main | uniform | 200x200 | GA-cost-tuned | 2.56 | 1 of 24 |
| main | uniform | 200x200 | GA-rand-base | 0.24 | 20 of 24 |
| main | uniform | 200x200 | GA-rand-tuned | 0.27 | 17 of 24 |
| main | uniform | 50x50 | GA-cost-tuned | 0.30 | 16 of 24 |
| representation | skewed | 50x50 | GA-cost-tuned | 0.50 | 9 of 24 |
| representation | structured | 50x50 | GA-cost-tuned | 0.50 | 9 of 24 |
| representation | ties | 50x50 | GA-cost-tuned | 0.50 | 9 of 24 |
| representation | uniform | 100x100 | GA-cost-tuned | 1.55 | 3 of 24 |
| representation | uniform | 100x100 | GA-rand-tuned | 0.22 | 21 of 24 |
| representation | uniform | 100x100 | random-parents | 0.30 | 16 of 24 |
| representation | uniform | 200x200 | GA-cost-tuned | 5.78 | 1 of 24 |
| representation | uniform | 200x200 | GA-rand-tuned | 0.44 | 10 of 24 |
| representation | uniform | 200x200 | random-parents | 0.74 | 6 of 24 |
| representation | uniform | 20x20 | GA-cost-tuned | 0.20 | 23 of 24 |
| representation | uniform | 30x30 | GA-cost-tuned | 0.27 | 17 of 24 |
| representation | uniform | 50x50 | GA-cost-tuned | 0.50 | 9 of 24 |
| stagnation | uniform | 100x100 | GA-cost-tuned | 0.75 | 6 of 24 |
| stagnation | uniform | 50x50 | GA-cost-tuned | 0.30 | 16 of 24 |
| timing | lp_scaling | 1000x1000 | LP | 1.08 | 4 of 8 |
| timing | lp_scaling | 1000x1000 | LP-ortools | 1.08 | 4 of 8 |
| timing | uniform | 100x100 | GA-cost-tuned | 0.75 | 6 of 8 |
| timing | uniform | 200x200 | GA-cost-tuned | 2.56 | 1 of 8 |

## Possible reductions (choose; not applied)

| Option | Saves, h |
|---|---|
| budget cap 1,000,000 decoder calls (shortens runs at 24x324, 100x100, 200x200) | 17.77 |
| budget cap 2,000,000 decoder calls (shortens runs at 200x200) | 11.46 |
| budget cap 4,000,000 decoder calls (shortens runs at 200x200) | 7.64 |
| drop the base GA configurations at 200x200 | 2.89 |
| timing phase without 200x200 for GA and SA | 1.61 |
| factorial plan without population 400 | 0.66 |
| 200x200 in the main phase with 10 runs instead of 30 | 0.00 |
