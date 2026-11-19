# FCTP: new instance classes (amendment 10.3 b)

Exploratory (amendment 10, written after the results of amendments 8 and 9 were seen). Class `uniform`: generator of 8.4 with rho = 0.05 and 5 (new) and rho = 0.2 and 1 (instances of 8.4 and 9.4). Class `concentrated`: a tenth of the suppliers hold 80 % of the supply. Gap to Z_best (proved optimum of the MIP with 1 thread and 60 s, otherwise the best known value); `mip_proved` counts the new instances of the cell with a proved optimum. Columns as in R2_gap. Nothing was tuned on these instances.

| class | rho | size | instances_from | mip_proved | method | instances | runs | gap_instance_median | ci95_low | ci95_high | gap_min | gap_max | time_median_s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 0.05 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 2.277 | 1.8 | 3.761 | 1.8 | 3.761 | 0.002989 |
| uniform | 0.05 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 0.1629 | 0 | 0.4931 | 0 | 0.9945 | 0.03011 |
| uniform | 0.05 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 0 | 0 | 0.02036 | 0 | 0.6 | 0.0263 |
| uniform | 0.05 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 0.8946 | 0 | 1.731 | 0 | 5.12 | 0.4942 |
| uniform | 0.05 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 4.163 |
| uniform | 0.05 | 30x30 | amendment 10 | 2 | Balinski | 5 | 5 | 3.525 | 2.652 | 4.138 | 2.652 | 4.138 | 0.005427 |
| uniform | 0.05 | 30x30 | amendment 10 | 2 | Tabu | 5 | 50 | 0.3677 | 0 | 1.615 | 0 | 1.974 | 0.0709 |
| uniform | 0.05 | 30x30 | amendment 10 | 2 | ILS | 5 | 50 | 0.1567 | 0 | 0.3198 | 0 | 0.9994 | 0.06493 |
| uniform | 0.05 | 30x30 | amendment 10 | 2 | GA-cost-cycle | 5 | 50 | 4.045 | 2.224 | 5.441 | 0.348 | 8.95 | 1.801 |
| uniform | 0.05 | 30x30 | amendment 10 | 2 | MIP-60s | 5 | 5 | 0 | 0 | 0.1236 | 0 | 0.1236 | 60.01 |
| uniform | 0.05 | 50x50 | amendment 10 | 0 | Balinski | 5 | 5 | 6.259 | 4.346 | 7.004 | 4.346 | 7.004 | 0.01811 |
| uniform | 0.05 | 50x50 | amendment 10 | 0 | Tabu | 5 | 50 | 1.47 | 0.9185 | 1.669 | 0.5447 | 2.399 | 0.276 |
| uniform | 0.05 | 50x50 | amendment 10 | 0 | ILS | 5 | 50 | 0.5854 | 0.1896 | 1.152 | 0 | 1.911 | 0.248 |
| uniform | 0.05 | 50x50 | amendment 10 | 0 | GA-cost-cycle | 5 | 50 | 7.436 | 5.692 | 10.26 | 3.227 | 12.58 | 11.47 |
| uniform | 0.05 | 50x50 | amendment 10 | 0 | MIP-60s | 5 | 5 | 0.06942 | 0 | 0.3757 | 0 | 0.3757 | 60.03 |
| uniform | 0.2 | 20x20 | amendments 8 and 9 | – | Balinski | 5 | 5 | 7.537 | 7.325 | 16.23 | 7.325 | 16.23 | 0.003018 |
| uniform | 0.2 | 20x20 | amendments 8 and 9 | – | Tabu | 5 | 50 | 1.239 | 0 | 3.359 | 0 | 5.231 | 0.02909 |
| uniform | 0.2 | 20x20 | amendments 8 and 9 | – | ILS | 5 | 50 | 0.2939 | 0 | 0.6174 | 0 | 2.781 | 0.02515 |
| uniform | 0.2 | 20x20 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 1.865 | 1.137 | 3.759 | 0 | 4.386 | 0.4816 |
| uniform | 0.2 | 20x20 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 16.78 |
| uniform | 0.2 | 30x30 | amendments 8 and 9 | – | Balinski | 5 | 5 | 9.426 | 5.754 | 12.87 | 5.754 | 12.87 | 0.0171 |
| uniform | 0.2 | 30x30 | amendments 8 and 9 | – | Tabu | 5 | 50 | 1.739 | 1.053 | 2.012 | 0 | 2.782 | 0.06479 |
| uniform | 0.2 | 30x30 | amendments 8 and 9 | – | ILS | 5 | 50 | 0.9709 | 0.5504 | 1.353 | 0 | 2.87 | 0.05834 |
| uniform | 0.2 | 30x30 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 5.785 | 4.251 | 7.188 | 2.15 | 11.07 | 1.587 |
| uniform | 0.2 | 30x30 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 0.1553 | 0 | 0.9565 | 0 | 0.9565 | 60.01 |
| uniform | 0.2 | 50x50 | amendments 8 and 9 | – | Balinski | 5 | 5 | 16.92 | 15.33 | 19.36 | 15.33 | 19.36 | 0.01834 |
| uniform | 0.2 | 50x50 | amendments 8 and 9 | – | Tabu | 5 | 50 | 3.737 | 2.454 | 5.192 | 1.185 | 6.155 | 0.2486 |
| uniform | 0.2 | 50x50 | amendments 8 and 9 | – | ILS | 5 | 50 | 1.771 | 1.297 | 2.859 | 0 | 4.536 | 0.2191 |
| uniform | 0.2 | 50x50 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 9.568 | 6.52 | 12.57 | 3.259 | 14.29 | 11.56 |
| uniform | 0.2 | 50x50 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 1.674 | 0 | 2.314 | 0 | 2.314 | 60.02 |
| uniform | 1 | 20x20 | amendments 8 and 9 | – | Balinski | 5 | 5 | 23.91 | 13.66 | 29.24 | 13.66 | 29.24 | 0.003702 |
| uniform | 1 | 20x20 | amendments 8 and 9 | – | Tabu | 5 | 50 | 1.269 | 0.6992 | 2.586 | 0.02616 | 7.275 | 0.03072 |
| uniform | 1 | 20x20 | amendments 8 and 9 | – | ILS | 5 | 50 | 0.7586 | 0 | 1.631 | 0 | 5.152 | 0.02619 |
| uniform | 1 | 20x20 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 3.6 | 2.524 | 6.175 | 0.828 | 8.182 | 0.4847 |
| uniform | 1 | 20x20 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 13.29 |
| uniform | 1 | 30x30 | amendments 8 and 9 | – | Balinski | 5 | 5 | 19.75 | 16.33 | 20.98 | 16.33 | 20.98 | 0.005291 |
| uniform | 1 | 30x30 | amendments 8 and 9 | – | Tabu | 5 | 50 | 2.312 | 0.7796 | 3.846 | 0.4252 | 6.861 | 0.06671 |
| uniform | 1 | 30x30 | amendments 8 and 9 | – | ILS | 5 | 50 | 1.577 | 0.3208 | 2.383 | 0.1168 | 5.63 | 0.05951 |
| uniform | 1 | 30x30 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 7.337 | 4.871 | 10.17 | 3.293 | 15.21 | 1.652 |
| uniform | 1 | 30x30 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 0 | 0 | 0.2056 | 0 | 0.2056 | 60.01 |
| uniform | 1 | 50x50 | amendments 8 and 9 | – | Balinski | 5 | 5 | 19.19 | 16.93 | 22.72 | 16.93 | 22.72 | 0.01674 |
| uniform | 1 | 50x50 | amendments 8 and 9 | – | Tabu | 5 | 50 | 4.009 | 2.826 | 5.212 | 0.4281 | 7.44 | 0.2232 |
| uniform | 1 | 50x50 | amendments 8 and 9 | – | ILS | 5 | 50 | 1.827 | 0.7076 | 3.011 | 0 | 4.929 | 0.1991 |
| uniform | 1 | 50x50 | amendments 8 and 9 | – | GA-cost-cycle | 5 | 50 | 11.87 | 9.361 | 12.68 | 7.11 | 17.48 | 11.23 |
| uniform | 1 | 50x50 | amendments 8 and 9 | – | MIP-60s | 5 | 5 | 0.1537 | 0 | 2.156 | 0 | 2.156 | 60.05 |
| uniform | 5 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 19.03 | 11.37 | 26.62 | 11.37 | 26.62 | 0.002295 |
| uniform | 5 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 2.612 | 1.342 | 4.819 | 0 | 7.12 | 0.02899 |
| uniform | 5 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 1.145 | 0.6497 | 4.113 | 0 | 5.354 | 0.02552 |
| uniform | 5 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 6.616 | 2.554 | 11.2 | 0.5378 | 15.94 | 0.5044 |
| uniform | 5 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 21.43 |
| uniform | 5 | 30x30 | amendment 10 | 0 | Balinski | 5 | 5 | 17 | 14.32 | 23.43 | 14.32 | 23.43 | 0.005098 |
| uniform | 5 | 30x30 | amendment 10 | 0 | Tabu | 5 | 50 | 2.252 | 2.001 | 4.249 | 0 | 6.78 | 0.06898 |
| uniform | 5 | 30x30 | amendment 10 | 0 | ILS | 5 | 50 | 1.192 | 0 | 1.809 | 0 | 5.101 | 0.06234 |
| uniform | 5 | 30x30 | amendment 10 | 0 | GA-cost-cycle | 5 | 50 | 9.941 | 6.345 | 14.13 | 4.368 | 17.64 | 1.817 |
| uniform | 5 | 30x30 | amendment 10 | 0 | MIP-60s | 5 | 5 | 0.398 | 0.01811 | 0.8653 | 0.01811 | 0.8653 | 60.01 |
| uniform | 5 | 50x50 | amendment 10 | 0 | Balinski | 5 | 5 | 24.03 | 19.23 | 31.37 | 19.23 | 31.37 | 0.01613 |
| uniform | 5 | 50x50 | amendment 10 | 0 | Tabu | 5 | 50 | 3.69 | 1.848 | 5.791 | 0.09881 | 10.51 | 0.2738 |
| uniform | 5 | 50x50 | amendment 10 | 0 | ILS | 5 | 50 | 1.564 | 1.113 | 3.459 | 0 | 5.274 | 0.2461 |
| uniform | 5 | 50x50 | amendment 10 | 0 | GA-cost-cycle | 5 | 50 | 13.53 | 9.674 | 20.46 | 6.644 | 27.35 | 11.25 |
| uniform | 5 | 50x50 | amendment 10 | 0 | MIP-60s | 5 | 5 | 0.9824 | 0 | 1.89 | 0 | 1.89 | 60.02 |
| concentrated | 0.05 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 0.1385 | 0 | 0.6073 | 0 | 0.6073 | 0.002605 |
| concentrated | 0.05 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 0.0224 | 0 | 0.08183 | 0 | 0.1916 | 0.02577 |
| concentrated | 0.05 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 0 | 0 | 0.01574 | 0 | 0.07553 | 0.02294 |
| concentrated | 0.05 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 0.08703 | 0.07093 | 0.2792 | 0 | 0.5665 | 0.4659 |
| concentrated | 0.05 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1.673 |
| concentrated | 0.05 | 30x30 | amendment 10 | 5 | Balinski | 5 | 5 | 0.2702 | 0.1887 | 0.724 | 0.1887 | 0.724 | 0.004665 |
| concentrated | 0.05 | 30x30 | amendment 10 | 5 | Tabu | 5 | 50 | 0.04156 | 0.01239 | 0.2382 | 0 | 0.4194 | 0.05956 |
| concentrated | 0.05 | 30x30 | amendment 10 | 5 | ILS | 5 | 50 | 0 | 0 | 0.132 | 0 | 0.1942 | 0.05576 |
| concentrated | 0.05 | 30x30 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 0.7348 | 0.3303 | 1.164 | 0 | 2.167 | 1.705 |
| concentrated | 0.05 | 30x30 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 3.441 |
| concentrated | 0.05 | 50x50 | amendment 10 | 1 | Balinski | 5 | 5 | 0.9648 | 0.4796 | 1.295 | 0.4796 | 1.295 | 0.01783 |
| concentrated | 0.05 | 50x50 | amendment 10 | 1 | Tabu | 5 | 50 | 0.1771 | 0.06936 | 0.3005 | 0 | 0.4437 | 0.2257 |
| concentrated | 0.05 | 50x50 | amendment 10 | 1 | ILS | 5 | 50 | 0.05945 | 0.03118 | 0.1127 | 0 | 0.2958 | 0.2107 |
| concentrated | 0.05 | 50x50 | amendment 10 | 1 | GA-cost-cycle | 5 | 50 | 3.744 | 2.655 | 4.796 | 0.6036 | 6.805 | 10.91 |
| concentrated | 0.05 | 50x50 | amendment 10 | 1 | MIP-60s | 5 | 5 | 0.02147 | 0 | 0.1115 | 0 | 0.1115 | 60.02 |
| concentrated | 0.2 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 1.112 | 0.4481 | 1.85 | 0.4481 | 1.85 | 0.002346 |
| concentrated | 0.2 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 0.2006 | 0.1073 | 0.5356 | 0 | 0.9611 | 0.0254 |
| concentrated | 0.2 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 0 | 0 | 0 | 0 | 0.887 | 0.02276 |
| concentrated | 0.2 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 0.5821 | 0 | 1.786 | 0 | 2.678 | 0.4565 |
| concentrated | 0.2 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1.745 |
| concentrated | 0.2 | 30x30 | amendment 10 | 5 | Balinski | 5 | 5 | 1.654 | 1.353 | 2.963 | 1.353 | 2.963 | 0.004492 |
| concentrated | 0.2 | 30x30 | amendment 10 | 5 | Tabu | 5 | 50 | 0.6708 | 0.09703 | 1.076 | 0 | 1.342 | 0.06076 |
| concentrated | 0.2 | 30x30 | amendment 10 | 5 | ILS | 5 | 50 | 0.3356 | 0.03312 | 0.6514 | 0 | 1.183 | 0.05625 |
| concentrated | 0.2 | 30x30 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 1.167 | 0.5504 | 1.742 | 0.1791 | 3.608 | 1.676 |
| concentrated | 0.2 | 30x30 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 9.128 |
| concentrated | 0.2 | 50x50 | amendment 10 | 1 | Balinski | 5 | 5 | 2.788 | 1.294 | 3.409 | 1.294 | 3.409 | 0.01401 |
| concentrated | 0.2 | 50x50 | amendment 10 | 1 | Tabu | 5 | 50 | 0.5551 | 0.2886 | 0.7735 | 0.1342 | 1.392 | 0.2065 |
| concentrated | 0.2 | 50x50 | amendment 10 | 1 | ILS | 5 | 50 | 0.3232 | 0.08225 | 0.568 | 0.06802 | 0.7477 | 0.1967 |
| concentrated | 0.2 | 50x50 | amendment 10 | 1 | GA-cost-cycle | 5 | 50 | 4.827 | 3.148 | 5.339 | 1.771 | 6.796 | 11.09 |
| concentrated | 0.2 | 50x50 | amendment 10 | 1 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 60.01 |
| concentrated | 1 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 4.762 | 0.5116 | 8.15 | 0.5116 | 8.15 | 0.002542 |
| concentrated | 1 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 0.4024 | 0.1814 | 1.273 | 0 | 2.138 | 0.02587 |
| concentrated | 1 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 0.3161 | 0 | 1.307 | 0 | 1.505 | 0.0227 |
| concentrated | 1 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 0.5281 | 0.3896 | 2.692 | 0 | 2.692 | 0.4553 |
| concentrated | 1 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1.392 |
| concentrated | 1 | 30x30 | amendment 10 | 5 | Balinski | 5 | 5 | 7.47 | 6.24 | 10.01 | 6.24 | 10.01 | 0.004399 |
| concentrated | 1 | 30x30 | amendment 10 | 5 | Tabu | 5 | 50 | 1.348 | 0.2489 | 1.645 | 0.04407 | 3.768 | 0.06063 |
| concentrated | 1 | 30x30 | amendment 10 | 5 | ILS | 5 | 50 | 0.8179 | 0.2189 | 0.916 | 0.04407 | 2.832 | 0.05597 |
| concentrated | 1 | 30x30 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 2.306 | 1.634 | 2.724 | 0.8132 | 6.145 | 1.887 |
| concentrated | 1 | 30x30 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 7.587 |
| concentrated | 1 | 50x50 | amendment 10 | 1 | Balinski | 5 | 5 | 8.717 | 6.888 | 10.56 | 6.888 | 10.56 | 0.0132 |
| concentrated | 1 | 50x50 | amendment 10 | 1 | Tabu | 5 | 50 | 2.534 | 1.517 | 3.09 | 1.166 | 3.578 | 0.2141 |
| concentrated | 1 | 50x50 | amendment 10 | 1 | ILS | 5 | 50 | 1.959 | 1.093 | 2.056 | 0.3203 | 3.612 | 0.2014 |
| concentrated | 1 | 50x50 | amendment 10 | 1 | GA-cost-cycle | 5 | 50 | 4.691 | 2.927 | 4.951 | 1.984 | 8.147 | 11.25 |
| concentrated | 1 | 50x50 | amendment 10 | 1 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 60.01 |
| concentrated | 5 | 20x20 | amendment 10 | 5 | Balinski | 5 | 5 | 12.02 | 6.094 | 16.7 | 6.094 | 16.7 | 0.002254 |
| concentrated | 5 | 20x20 | amendment 10 | 5 | Tabu | 5 | 50 | 1.286 | 0.823 | 3.014 | 0 | 3.143 | 0.0253 |
| concentrated | 5 | 20x20 | amendment 10 | 5 | ILS | 5 | 50 | 1.381 | 0.6161 | 2.896 | 0 | 6.046 | 0.02271 |
| concentrated | 5 | 20x20 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 3.066 | 1.54 | 4.234 | 1.121 | 5.743 | 0.4431 |
| concentrated | 5 | 20x20 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 1.943 |
| concentrated | 5 | 30x30 | amendment 10 | 5 | Balinski | 5 | 5 | 13.16 | 6.242 | 17.9 | 6.242 | 17.9 | 0.004504 |
| concentrated | 5 | 30x30 | amendment 10 | 5 | Tabu | 5 | 50 | 3.028 | 1.06 | 5.802 | 0.2605 | 6.415 | 0.05874 |
| concentrated | 5 | 30x30 | amendment 10 | 5 | ILS | 5 | 50 | 2.407 | 0.6958 | 4.966 | 0.06501 | 7.098 | 0.05505 |
| concentrated | 5 | 30x30 | amendment 10 | 5 | GA-cost-cycle | 5 | 50 | 5.211 | 3.346 | 7.698 | 0.9936 | 9.944 | 1.736 |
| concentrated | 5 | 30x30 | amendment 10 | 5 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 7.709 |
| concentrated | 5 | 50x50 | amendment 10 | 2 | Balinski | 5 | 5 | 15.77 | 7.752 | 17.49 | 7.752 | 17.49 | 0.01301 |
| concentrated | 5 | 50x50 | amendment 10 | 2 | Tabu | 5 | 50 | 4.049 | 2.04 | 4.747 | 0.9225 | 7.389 | 0.217 |
| concentrated | 5 | 50x50 | amendment 10 | 2 | ILS | 5 | 50 | 3.894 | 1.226 | 4.863 | 0.6943 | 7.015 | 0.2043 |
| concentrated | 5 | 50x50 | amendment 10 | 2 | GA-cost-cycle | 5 | 50 | 8.587 | 7.432 | 10.41 | 5.181 | 12.96 | 11.33 |
| concentrated | 5 | 50x50 | amendment 10 | 2 | MIP-60s | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 60.01 |
