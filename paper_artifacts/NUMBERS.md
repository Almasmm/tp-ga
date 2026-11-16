# Numbers for the paper

Every value below is computed by `python -m tpga.experiments.report` from the files named in the
*Source* column. Queries are pandas expressions on the CSV file given; `gap` is
`100 * (z - z*) / z*` with z* the HiGHS optimum of the same instance.

| Quantity | Value | Definition | Source |
|---|---|---|---|
| Runs in raw/runs.csv | 28012 | rows (one per run; LP and classical methods one per instance) | raw/runs.csv |
| Rows of LP | 118 | rows with this method | raw/runs.csv: method == 'LP' |
| Rows of NWC | 118 | rows with this method | raw/runs.csv: method == 'NWC' |
| Rows of LCM | 118 | rows with this method | raw/runs.csv: method == 'LCM' |
| Rows of VAM | 118 | rows with this method | raw/runs.csv: method == 'VAM' |
| Rows of RS | 2780 | rows with this method | raw/runs.csv: method == 'RS' |
| Rows of GA-rand | 12380 | rows with this method | raw/runs.csv: method == 'GA-rand' |
| Rows of GA-cost | 12380 | rows with this method | raw/runs.csv: method == 'GA-cost' |
| Infeasible plans | 0 | rows whose plan failed the independent check | raw/runs.csv: feasible != True |
| Mean gap LP 20x20 structured | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LP' (base config) |
| Median gap LP 20x20 structured | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LP' (base config) |
| Share optimal LP 20x20 structured | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LP' (base config) |
| Mean gap NWC 20x20 structured | 125.2601 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'NWC' (base config) |
| Median gap NWC 20x20 structured | 126.5487 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'NWC' (base config) |
| Share optimal NWC 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'NWC' (base config) |
| Mean gap LCM 20x20 structured | 10.7675 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LCM' (base config) |
| Median gap LCM 20x20 structured | 11.1942 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LCM' (base config) |
| Share optimal LCM 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'LCM' (base config) |
| Mean gap VAM 20x20 structured | 5.8960 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'VAM' (base config) |
| Median gap VAM 20x20 structured | 4.8617 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'VAM' (base config) |
| Share optimal VAM 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'VAM' (base config) |
| Mean gap RS 20x20 structured | 57.4665 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'RS' (base config) |
| Median gap RS 20x20 structured | 60.3130 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'RS' (base config) |
| Share optimal RS 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'RS' (base config) |
| Mean gap GA-rand 20x20 structured | 8.9809 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-rand' (base config) |
| Median gap GA-rand 20x20 structured | 8.0247 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 20x20 structured | 1.1879 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-cost' (base config) |
| Median gap GA-cost 20x20 structured | 0.8327 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 20x20 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '20x20' and method == 'GA-cost' (base config) |
| Mean gap LP 50x50 structured | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LP' (base config) |
| Median gap LP 50x50 structured | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LP' (base config) |
| Share optimal LP 50x50 structured | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LP' (base config) |
| Mean gap NWC 50x50 structured | 192.8271 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'NWC' (base config) |
| Median gap NWC 50x50 structured | 184.5448 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'NWC' (base config) |
| Share optimal NWC 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'NWC' (base config) |
| Mean gap LCM 50x50 structured | 15.5447 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LCM' (base config) |
| Median gap LCM 50x50 structured | 15.3401 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LCM' (base config) |
| Share optimal LCM 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'LCM' (base config) |
| Mean gap VAM 50x50 structured | 12.9075 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'VAM' (base config) |
| Median gap VAM 50x50 structured | 11.9621 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'VAM' (base config) |
| Share optimal VAM 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'VAM' (base config) |
| Mean gap RS 50x50 structured | 129.2783 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'RS' (base config) |
| Median gap RS 50x50 structured | 121.2021 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'RS' (base config) |
| Share optimal RS 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'RS' (base config) |
| Mean gap GA-rand 50x50 structured | 29.0598 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-rand' (base config) |
| Median gap GA-rand 50x50 structured | 27.1278 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 50x50 structured | 4.5307 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-cost' (base config) |
| Median gap GA-cost 50x50 structured | 4.3730 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 50x50 structured | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'structured' and size == '50x50' and method == 'GA-cost' (base config) |
| Mean gap LP 5x5 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LP' (base config) |
| Median gap LP 5x5 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LP' (base config) |
| Share optimal LP 5x5 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LP' (base config) |
| Mean gap NWC 5x5 uniform | 107.2542 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'NWC' (base config) |
| Median gap NWC 5x5 uniform | 105.1402 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'NWC' (base config) |
| Share optimal NWC 5x5 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'NWC' (base config) |
| Mean gap LCM 5x5 uniform | 10.5474 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LCM' (base config) |
| Median gap LCM 5x5 uniform | 10.0726 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LCM' (base config) |
| Share optimal LCM 5x5 uniform | 0.1000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'LCM' (base config) |
| Mean gap VAM 5x5 uniform | 3.6914 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'VAM' (base config) |
| Median gap VAM 5x5 uniform | 1.9452 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'VAM' (base config) |
| Share optimal VAM 5x5 uniform | 0.2000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'VAM' (base config) |
| Mean gap RS 5x5 uniform | 0.2071 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'RS' (base config) |
| Median gap RS 5x5 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'RS' (base config) |
| Share optimal RS 5x5 uniform | 0.8033 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'RS' (base config) |
| Mean gap GA-rand 5x5 uniform | 0.0139 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-rand' (base config) |
| Median gap GA-rand 5x5 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 5x5 uniform | 0.9733 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 5x5 uniform | 0.0153 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-cost' (base config) |
| Median gap GA-cost 5x5 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 5x5 uniform | 0.9100 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '5x5' and method == 'GA-cost' (base config) |
| Mean gap LP 10x10 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LP' (base config) |
| Median gap LP 10x10 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LP' (base config) |
| Share optimal LP 10x10 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LP' (base config) |
| Mean gap NWC 10x10 uniform | 265.4317 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'NWC' (base config) |
| Median gap NWC 10x10 uniform | 250.0122 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'NWC' (base config) |
| Share optimal NWC 10x10 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'NWC' (base config) |
| Mean gap LCM 10x10 uniform | 33.6854 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LCM' (base config) |
| Median gap LCM 10x10 uniform | 28.5977 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LCM' (base config) |
| Share optimal LCM 10x10 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'LCM' (base config) |
| Mean gap VAM 10x10 uniform | 15.3775 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'VAM' (base config) |
| Median gap VAM 10x10 uniform | 9.3896 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'VAM' (base config) |
| Share optimal VAM 10x10 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'VAM' (base config) |
| Mean gap RS 10x10 uniform | 66.5447 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'RS' (base config) |
| Median gap RS 10x10 uniform | 63.3439 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'RS' (base config) |
| Share optimal RS 10x10 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'RS' (base config) |
| Mean gap GA-rand 10x10 uniform | 7.9170 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-rand' (base config) |
| Median gap GA-rand 10x10 uniform | 5.9059 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 10x10 uniform | 0.0100 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 10x10 uniform | 2.0417 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-cost' (base config) |
| Median gap GA-cost 10x10 uniform | 1.2254 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 10x10 uniform | 0.0300 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '10x10' and method == 'GA-cost' (base config) |
| Mean gap LP 20x20 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LP' (base config) |
| Median gap LP 20x20 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LP' (base config) |
| Share optimal LP 20x20 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LP' (base config) |
| Mean gap NWC 20x20 uniform | 435.5134 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'NWC' (base config) |
| Median gap NWC 20x20 uniform | 435.4116 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'NWC' (base config) |
| Share optimal NWC 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'NWC' (base config) |
| Mean gap LCM 20x20 uniform | 49.7176 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LCM' (base config) |
| Median gap LCM 20x20 uniform | 46.5369 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LCM' (base config) |
| Share optimal LCM 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'LCM' (base config) |
| Mean gap VAM 20x20 uniform | 24.4731 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'VAM' (base config) |
| Median gap VAM 20x20 uniform | 23.9128 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'VAM' (base config) |
| Share optimal VAM 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'VAM' (base config) |
| Mean gap RS 20x20 uniform | 219.2637 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'RS' (base config) |
| Median gap RS 20x20 uniform | 215.8469 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'RS' (base config) |
| Share optimal RS 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'RS' (base config) |
| Mean gap GA-rand 20x20 uniform | 50.2334 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-rand' (base config) |
| Median gap GA-rand 20x20 uniform | 48.7096 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 20x20 uniform | 8.4393 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-cost' (base config) |
| Median gap GA-cost 20x20 uniform | 7.7614 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 20x20 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '20x20' and method == 'GA-cost' (base config) |
| Mean gap LP 30x30 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LP' (base config) |
| Median gap LP 30x30 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LP' (base config) |
| Share optimal LP 30x30 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LP' (base config) |
| Mean gap NWC 30x30 uniform | 719.4166 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'NWC' (base config) |
| Median gap NWC 30x30 uniform | 765.7369 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'NWC' (base config) |
| Share optimal NWC 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'NWC' (base config) |
| Mean gap LCM 30x30 uniform | 54.7772 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LCM' (base config) |
| Median gap LCM 30x30 uniform | 51.3930 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LCM' (base config) |
| Share optimal LCM 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'LCM' (base config) |
| Mean gap VAM 30x30 uniform | 24.5095 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'VAM' (base config) |
| Median gap VAM 30x30 uniform | 25.6717 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'VAM' (base config) |
| Share optimal VAM 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'VAM' (base config) |
| Mean gap RS 30x30 uniform | 426.0919 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'RS' (base config) |
| Median gap RS 30x30 uniform | 424.7696 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'RS' (base config) |
| Share optimal RS 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'RS' (base config) |
| Mean gap GA-rand 30x30 uniform | 109.0598 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-rand' (base config) |
| Median gap GA-rand 30x30 uniform | 103.8533 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 30x30 uniform | 12.9500 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-cost' (base config) |
| Median gap GA-cost 30x30 uniform | 12.4618 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 30x30 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '30x30' and method == 'GA-cost' (base config) |
| Mean gap LP 50x50 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LP' (base config) |
| Median gap LP 50x50 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LP' (base config) |
| Share optimal LP 50x50 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LP' (base config) |
| Mean gap NWC 50x50 uniform | 1176.2668 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'NWC' (base config) |
| Median gap NWC 50x50 uniform | 1149.0716 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'NWC' (base config) |
| Share optimal NWC 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'NWC' (base config) |
| Mean gap LCM 50x50 uniform | 73.3441 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LCM' (base config) |
| Median gap LCM 50x50 uniform | 69.0171 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LCM' (base config) |
| Share optimal LCM 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'LCM' (base config) |
| Mean gap VAM 50x50 uniform | 33.9797 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'VAM' (base config) |
| Median gap VAM 50x50 uniform | 31.0392 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'VAM' (base config) |
| Share optimal VAM 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'VAM' (base config) |
| Mean gap RS 50x50 uniform | 760.6712 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'RS' (base config) |
| Median gap RS 50x50 uniform | 755.5219 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'RS' (base config) |
| Share optimal RS 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'RS' (base config) |
| Mean gap GA-rand 50x50 uniform | 227.4141 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-rand' (base config) |
| Median gap GA-rand 50x50 uniform | 219.9363 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 50x50 uniform | 25.8414 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-cost' (base config) |
| Median gap GA-cost 50x50 uniform | 25.5591 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 50x50 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '50x50' and method == 'GA-cost' (base config) |
| Mean gap LP 100x100 uniform | 0 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LP' (base config) |
| Median gap LP 100x100 uniform | 0 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LP' (base config) |
| Share optimal LP 100x100 uniform | 1.0000 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LP' (base config) |
| Mean gap NWC 100x100 uniform | 2043.5579 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'NWC' (base config) |
| Median gap NWC 100x100 uniform | 2050.5802 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'NWC' (base config) |
| Share optimal NWC 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'NWC' (base config) |
| Mean gap LCM 100x100 uniform | 94.1681 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LCM' (base config) |
| Median gap LCM 100x100 uniform | 93.1220 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LCM' (base config) |
| Share optimal LCM 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'LCM' (base config) |
| Mean gap VAM 100x100 uniform | 36.4789 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'VAM' (base config) |
| Median gap VAM 100x100 uniform | 38.5096 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'VAM' (base config) |
| Share optimal VAM 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'VAM' (base config) |
| Mean gap RS 100x100 uniform | 1525.7653 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'RS' (base config) |
| Median gap RS 100x100 uniform | 1497.8059 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'RS' (base config) |
| Share optimal RS 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'RS' (base config) |
| Mean gap GA-rand 100x100 uniform | 606.5814 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-rand' (base config) |
| Median gap GA-rand 100x100 uniform | 602.7554 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-rand' (base config) |
| Share optimal GA-rand 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-rand' (base config) |
| Mean gap GA-cost 100x100 uniform | 28.4490 | mean of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-cost' (base config) |
| Median gap GA-cost 100x100 uniform | 30.1924 | median of gap over runs, % | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-cost' (base config) |
| Share optimal GA-cost 100x100 uniform | 0 | share of runs with |z - z*| <= 1e-9 max(1, |z*|) | tables/T2_gap.csv; raw/runs.csv: suite == 'uniform' and size == '100x100' and method == 'GA-cost' (base config) |
| Exponent b, GA-cost, time per run | 0.9120 | slope of log10 t on log10(m n), 95% CI [0.866, 0.958], 60 instances, m n in [25, 10000] | tables/T3_time_fit.csv |
| Exponent b, GA-cost, time per decoder call | 0.7481 | slope of log10 t on log10(m n), 95% CI [0.709, 0.787], 60 instances, m n in [25, 10000] | tables/T3_time_fit.csv |
| Exponent b, GA-rand, time per run | 1.3872 | slope of log10 t on log10(m n), 95% CI [1.322, 1.452], 60 instances, m n in [25, 10000] | tables/T3_time_fit.csv |
| Exponent b, GA-rand, time per decoder call | 0.7283 | slope of log10 t on log10(m n), 95% CI [0.689, 0.768], 60 instances, m n in [25, 10000] | tables/T3_time_fit.csv |
| Exponent b, LP, time per run | 0.5378 | slope of log10 t on log10(m n), 95% CI [0.487, 0.589], 60 instances, m n in [25, 10000] | tables/T3_time_fit.csv |
| Median time LP 5x5 | 0.0011 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 5x5 | 0.0085 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 5x5 | 0.0085 | median wall-clock per run, s | tables/T3_time.csv |
| Median time LP 10x10 | 0.0013 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 10x10 | 0.0148 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 10x10 | 0.0146 | median wall-clock per run, s | tables/T3_time.csv |
| Median time LP 20x20 | 0.0020 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 20x20 | 0.1306 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 20x20 | 0.0603 | median wall-clock per run, s | tables/T3_time.csv |
| Median time LP 30x30 | 0.0030 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 30x30 | 0.4881 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 30x30 | 0.1242 | median wall-clock per run, s | tables/T3_time.csv |
| Median time LP 50x50 | 0.0073 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 50x50 | 2.1925 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 50x50 | 0.3913 | median wall-clock per run, s | tables/T3_time.csv |
| Median time LP 100x100 | 0.0281 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-rand 100x100 | 26.8943 | median wall-clock per run, s | tables/T3_time.csv |
| Median time GA-cost 100x100 | 1.6963 | median wall-clock per run, s | tables/T3_time.csv |
| Wilcoxon GA-rand vs NWC (structured, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (structured, 20x20) | 0.1172 | Holm-adjusted p on per-instance median gaps; n = 10, r = -0.818, Cliff's delta = -0.500 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (structured, 20x20) | 0.6543 | Holm-adjusted p on per-instance median gaps; n = 10, r = 0.564, Cliff's delta = 0.540 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (structured, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (structured, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (structured, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (structured, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.880 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 0.960 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 0.940 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (structured, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 100x100) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.540 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.980 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 10x10) | 0.6543 | Holm-adjusted p on per-instance median gaps; n = 10, r = -0.564, Cliff's delta = -0.280 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.860 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 10x10) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.780 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 20x20) | 1.0000 | Holm-adjusted p on per-instance median gaps; n = 10, r = -0.055, Cliff's delta = 0 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 0.940 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 20x20) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.940 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 30x30) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.640 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 50x50) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.430 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (uniform, 5x5) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -1.000 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (uniform, 5x5) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.900 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (uniform, 5x5) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.800 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (uniform, 5x5) | 1.0000 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.200 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (uniform, 5x5) | 1.0000 | Holm-adjusted p on per-instance median gaps; n = 10, r = 1.000, Cliff's delta = 0.100 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (uniform, 5x5) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.890 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (uniform, 5x5) | 0.1094 | Holm-adjusted p on per-instance median gaps; n = 10, r = -1.000, Cliff's delta = -0.770 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs NWC (all synthetic, all) | 4.9452e-13 | Holm-adjusted p on per-instance median gaps; n = 80, r = -1.000, Cliff's delta = -0.696 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs LCM (all synthetic, all) | 0.0198 | Holm-adjusted p on per-instance median gaps; n = 80, r = 0.463, Cliff's delta = 0.037 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs VAM (all synthetic, all) | 8.7120e-08 | Holm-adjusted p on per-instance median gaps; n = 80, r = 0.788, Cliff's delta = 0.297 | tables/T5_tests.csv |
| Wilcoxon GA-rand vs RS (all synthetic, all) | 9.9525e-12 | Holm-adjusted p on per-instance median gaps; n = 80, r = -1.000, Cliff's delta = -0.413 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs GA-rand (all synthetic, all) | 1.4961e-11 | Holm-adjusted p on per-instance median gaps; n = 80, r = -0.999, Cliff's delta = -0.504 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs LCM (all synthetic, all) | 7.1241e-13 | Holm-adjusted p on per-instance median gaps; n = 80, r = -1.000, Cliff's delta = -0.689 | tables/T5_tests.csv |
| Wilcoxon GA-cost vs VAM (all synthetic, all) | 2.1997e-12 | Holm-adjusted p on per-instance median gaps; n = 80, r = -1.000, Cliff's delta = -0.405 | tables/T5_tests.csv |
| RQ4 mean gap 20x20 cost-aware P=20 pm=0.01 | 19.9104 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=20 pm=0.05 | 17.2520 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=20 pm=0.1 | 15.9039 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=20 pm=0.2 | 14.7433 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=50 pm=0.01 | 14.7426 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=50 pm=0.05 | 12.4281 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=50 pm=0.1 | 11.6888 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=50 pm=0.2 | 10.6334 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=100 pm=0.01 | 11.0347 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=100 pm=0.05 | 9.3899 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=100 pm=0.1 | 9.0618 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=100 pm=0.2 | 8.4393 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=200 pm=0.01 | 8.3546 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=200 pm=0.05 | 7.5340 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=200 pm=0.1 | 7.1643 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 cost-aware P=200 pm=0.2 | 6.5212 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=20 pm=0.01 | 239.8417 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=20 pm=0.05 | 161.0218 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=20 pm=0.1 | 131.6781 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=20 pm=0.2 | 106.4880 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=50 pm=0.01 | 158.5654 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=50 pm=0.05 | 105.8485 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=50 pm=0.1 | 83.4150 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=50 pm=0.2 | 64.9119 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=100 pm=0.01 | 111.2878 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=100 pm=0.05 | 74.9373 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=100 pm=0.1 | 60.6408 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=100 pm=0.2 | 50.2334 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=200 pm=0.01 | 76.8303 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=200 pm=0.05 | 61.0639 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=200 pm=0.1 | 52.5652 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 20x20 random P=200 pm=0.2 | 43.2680 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=20 pm=0.01 | 33.1991 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=20 pm=0.05 | 32.1973 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=20 pm=0.1 | 31.4200 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=20 pm=0.2 | 30.3946 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=50 pm=0.01 | 31.8242 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=50 pm=0.05 | 30.2735 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=50 pm=0.1 | 29.1893 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=50 pm=0.2 | 27.8159 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=100 pm=0.01 | 30.0101 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=100 pm=0.05 | 28.1841 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=100 pm=0.1 | 27.2659 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=100 pm=0.2 | 23.8533 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=200 pm=0.01 | 27.8268 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=200 pm=0.05 | 25.9008 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=200 pm=0.1 | 24.7531 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 cost-aware P=200 pm=0.2 | 23.6405 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=20 pm=0.01 | 854.9964 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=20 pm=0.05 | 672.0582 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=20 pm=0.1 | 557.5985 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=20 pm=0.2 | 466.6971 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=50 pm=0.01 | 666.7474 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=50 pm=0.05 | 450.3435 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=50 pm=0.1 | 376.2634 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=50 pm=0.2 | 320.0829 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=100 pm=0.01 | 490.1335 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=100 pm=0.05 | 333.9017 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=100 pm=0.1 | 280.1377 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=100 pm=0.2 | 202.4325 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=200 pm=0.01 | 368.0892 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=200 pm=0.05 | 259.1542 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=200 pm=0.1 | 214.2811 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| RQ4 mean gap 50x50 random P=200 pm=0.2 | 179.9671 | mean gap over 10 instances x runs, % | tables/T4_factorial.csv |
| Stopping stagnation 200 GA-cost 50x50: mean gap | 25.8414 | mean gap over runs, %; median decoder calls 41505.000 | tables/T2b_stopping.csv |
| Stopping budget only GA-cost 50x50: mean gap | 21.8653 | mean gap over runs, %; median decoder calls 5.000e+05 | tables/T2b_stopping.csv |
| Stopping stagnation 200 GA-rand 50x50: mean gap | 227.4141 | mean gap over runs, %; median decoder calls 3.057e+05 | tables/T2b_stopping.csv |
| Stopping budget only GA-rand 50x50: mean gap | 177.4509 | mean gap over runs, %; median decoder calls 5.000e+05 | tables/T2b_stopping.csv |
| Stopping stagnation 200 GA-cost 100x100: mean gap | 28.4490 | mean gap over runs, %; median decoder calls 43759.000 | tables/T2b_stopping.csv |
| Stopping budget only GA-cost 100x100: mean gap | 24.0311 | mean gap over runs, %; median decoder calls 2.000e+06 | tables/T2b_stopping.csv |
| Stopping stagnation 200 GA-rand 100x100: mean gap | 606.5814 | mean gap over runs, %; median decoder calls 7.037e+05 | tables/T2b_stopping.csv |
| Stopping budget only GA-rand 100x100: mean gap | 358.7950 | mean gap over runs, %; median decoder calls 2.000e+06 | tables/T2b_stopping.csv |
| Reachability instances | 1000 | random integer instances checked | reachability.json: instances |
| Reachability reproduced | 1000 | decoded plan equals the HiGHS vertex and its cost equals z* | reachability.json: reproduced |
| Reachability degenerate vertices | 693 | vertices with fewer than m + n - 1 positive cells | reachability.json: degenerate_vertices |
| Wall time of phase reachability | 6.4869e-04 | hours, sum over invocations | environment.json: phases |
| Wall time of phase main | 1.3164 | hours, sum over invocations | environment.json: phases |
| Wall time of phase factorial | 0.2212 | hours, sum over invocations | environment.json: phases |
| Wall time of phase applied | 0.9542 | hours, sum over invocations | environment.json: phases |
| Wall time of phase stopping | 1.3048 | hours, sum over invocations | environment.json: phases |
| Wall time of phase timing | 0.0576 | hours, sum over invocations | environment.json: phases |
| Base-configuration rows | 8812 | rows used for RQ1-RQ3 | raw/runs.csv with the base configuration filter in report.base_mask |
| Timing runs with the same cost as in raw/runs.csv | 600 of 600 | GA runs of the timing phase matched by instance, method, configuration and seed; equality of cost | raw/timing.csv joined with raw/runs.csv |
