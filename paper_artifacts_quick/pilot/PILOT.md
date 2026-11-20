# Pilot estimate of the v0.4 run

| Phase | Runs | Estimated wall time, h | Share |
|---|---|---|---|
| reference | 240 | 0.00 | 0.0 % |
| representation | 1,260 | 0.07 | 40.6 % |
| main | 3,000 | 0.10 | 59.4 % |
| applied | 0 | 0.00 | 0.0 % |
| factorial | 0 | 0.00 | 0.0 % |
| stagnation | 0 | 0.00 | 0.0 % |
| legacy | 0 | 0.00 | 0.0 % |
| timing | 0 | 0.00 | 0.0 % |
| **total** | 4,500 | **0.17** | 100 % |

* E/P speed ratio (same GA task): 1.32; quality phases use 20.1 performance-core equivalents, the timing phase 8 performance cores.
* Monitor overhead (1 Hz status through a queue): -4.75 % (0.640 s without, 0.610 s with).
* Phases with a stagnation stop are estimated with the full budget (upper bound).

## Largest items

| Phase | Item | h |
|---|---|---|
| representation | uniform 50x50 GA-cost-tuned | 0.03 |
| main | uniform 50x50 GA-cost-tuned | 0.02 |
| main | uniform 50x50 RS | 0.02 |
| representation | uniform 50x50 GA-rand-tuned | 0.01 |
| main | uniform 50x50 GA-rand-tuned | 0.01 |
| representation | uniform 30x30 GA-cost-tuned | 0.01 |
| main | uniform 50x50 SA-cost-tuned | 0.01 |
| main | uniform 50x50 SA-rand-tuned | 0.01 |
| main | uniform 30x30 GA-cost-tuned | 0.01 |
| representation | uniform 20x20 GA-cost-tuned | 0.00 |
| main | uniform 30x30 RS | 0.00 |
| representation | structured 20x20 GA-cost-tuned | 0.00 |

## Memory

Memory runs may use: 13.5 GiB (smaller of free RAM and free commit when the estimate was made, less the reserve). A run starts only while its memory is free; the times above include the slowdown where fewer runs fit at once.

No run is limited by memory: every phase runs all workers at once.
