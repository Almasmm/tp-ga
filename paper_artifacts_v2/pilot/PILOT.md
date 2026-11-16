# Pilot estimate of the v0.4 run

| Phase | Runs | Estimated wall time, h | Share |
|---|---|---|---|
| reference | 560 | 0.00 | 0.0 % |
| main | 29,400 | 35.84 | 81.7 % |
| stagnation | 5,400 | 2.23 | 5.1 % |
| legacy | 1,800 | 0.79 | 1.8 % |
| factorial | 72,000 | 3.33 | 7.6 % |
| timing | 425 | 1.67 | 3.8 % |
| **total** | 109,585 | **43.88** | 100 % |

* E/P speed ratio (same GA task): 1.48; quality phases use 18.8 performance-core equivalents, the timing phase 8 performance cores.
* Monitor overhead (1 Hz status through a queue): -9.21 % (0.620 s without, 0.563 s with).
* Phases with a stagnation stop are estimated with the full budget (upper bound).

## Largest items

| Phase | Item | h |
|---|---|---|
| main | uniform 200x200 GA-cost-tuned | 6.09 |
| main | uniform 200x200 RS | 5.97 |
| main | uniform 200x200 GA-cost-base | 4.57 |
| main | uniform 200x200 GA-rand-tuned | 4.44 |
| main | uniform 200x200 GA-rand-base | 4.18 |
| main | uniform 200x200 SA-rand-tuned | 2.49 |
| main | uniform 200x200 SA-cost-tuned | 2.32 |
| factorial | uniform 50x50 GA-rand | 1.36 |
| factorial | uniform 50x50 GA-cost | 1.36 |
| main | uniform 100x100 RS | 0.50 |
| main | structured 100x100 RS | 0.48 |
| main | structured 100x100 GA-cost-tuned | 0.46 |

## Possible reductions (choose; not applied)

| Option | Saves, h |
|---|---|
| budget cap 1,000,000 decoder calls (shortens runs at 100x100, 200x200) | 31.62 |
| budget cap 2,000,000 decoder calls (shortens runs at 200x200) | 23.69 |
| 200x200 in the main phase with 10 runs instead of 30 | 20.04 |
| budget cap 4,000,000 decoder calls (shortens runs at 200x200) | 15.80 |
| drop the base GA configurations at 200x200 | 8.75 |
| timing phase without 200x200 for GA and SA | 1.53 |
| factorial plan without population 400 | 0.76 |
