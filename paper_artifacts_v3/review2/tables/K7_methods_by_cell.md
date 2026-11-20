# K7_methods_by_cell

| size | rho | method | source | config | unit | instances | gap_best_pct | gap_bound_pct | cost | budget | evals | time_s | time_limit_s | nodes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10x10 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 5.50743139 | 5.50743139 | 11571 |  | 1 | 0.0012706 |  |  |
| 10x10 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 0.84229239 | 0.848765203 | 11285 | 20000 | 18870 | 0.0668084 |  |  |
| 10x10 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 0 | 0 | 10967 | 20000 | 19770 | 0.05716625 |  |  |
| 10x10 | 0.2 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder | 5 | 0.84229239 | 0.848765203 | 11285 | 20000 | 18870 | 0.06868555 |  |  |
| 10x10 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 0 | 0 | 10967 | 20000 | 19812 | 0.05415985 |  |  |
| 10x10 | 0.2 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 0.0301356102 | 0.0301356102 | 10967 | 20000 | 19881 | 0.0635098 |  |  |
| 10x10 | 0.2 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 1.45761412 | 1.45761412 | 11331.5 | 20000 | 19881 | 0.02461925 |  |  |
| 10x10 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0 | 0 | 10967 | 20000 | 20000 | 0.00719639999 |  |  |
| 10x10 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 0 | 10967 |  |  | 1.0302908 | 60 | 3 |
| 10x10 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 0 | 10967 |  |  | 0.7570853 | 300 | 3 |
| 10x10 | 0.2 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B20000 | decoder | 5 | 49.6968577 | 49.6968577 | 16121.5 | 20000 | 20000 | 0.02510285 |  |  |
| 10x10 | 0.2 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 1.29518327 | 1.30168516 | 10980 | 20000 | 20000 | 0.01132625 |  |  |
| 10x10 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 0.617963261 | 0.624421675 | 10996 | 20000 | 20000 | 0.01015965 |  |  |
| 10x10 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 9.79094745 | 9.79094745 | 13425 |  | 1 | 0.000714599999 |  |  |
| 10x10 | 1 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 12.2725744 | 12.2725744 | 30052 |  | 1 | 0.0015072 |  |  |
| 10x10 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 1.17121829 | 1.17121829 | 27080.5 | 20000 | 18870 | 0.06667505 |  |  |
| 10x10 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 0 | 4.37082188e-09 | 26767 | 20000 | 19770 | 0.0581448 |  |  |
| 10x10 | 1 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder | 5 | 1.17121829 | 1.17121829 | 27080.5 | 20000 | 18870 | 0.067797 |  |  |
| 10x10 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 0 | 4.37082188e-09 | 26767 | 20000 | 19884 | 0.05510255 |  |  |
| 10x10 | 1 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 2.39066339 | 2.3906634 | 27625 | 20000 | 19881 | 0.06280465 |  |  |
| 10x10 | 1 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 4.7554526 | 4.7554526 | 27710 | 20000 | 19881 | 0.0243991 |  |  |
| 10x10 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0 | 4.37082188e-09 | 26767 | 20000 | 20000 | 0.00765515 |  |  |
| 10x10 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 1.08331488e-12 | 26767 |  |  | 0.5602843 | 60 | 5 |
| 10x10 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 1.08331488e-12 | 26767 |  |  | 0.4508008 | 300 | 3 |
| 10x10 | 1 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B20000 | decoder | 5 | 49.2434714 | 49.2434714 | 37149.5 | 20000 | 20000 | 0.024683 |  |  |
| 10x10 | 1 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 4.95407888 | 4.95407888 | 28195 | 20000 | 20000 | 0.01136255 |  |  |
| 10x10 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 1.13632271 | 1.13632271 | 27216 | 20000 | 20000 | 0.00988954998 |  |  |
| 10x10 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 19.4791155 | 19.4791155 | 32440 |  | 1 | 0.000695900002 |  |  |
| 15x15 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 7.17738936 | 7.17738936 | 15676 |  | 1 | 0.0132442 |  |  |
| 15x15 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 1.05932203 | 1.05932203 | 14424 | 45000 | 43125 | 0.2038919 |  |  |
| 15x15 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 0.755649718 | 0.755649718 | 14282 | 45000 | 44845 | 0.18218895 |  |  |
| 15x15 | 0.2 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 1.04444133 | 1.04444133 | 14415 | 45000 | 43198.5 | 0.20834165 |  |  |
| 15x15 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 0.822740113 | 0.822740113 | 14439.5 | 45000 | 44922 | 0.15472685 |  |  |
| 15x15 | 0.2 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 5.46993623 | 5.46993623 | 14831.5 | 45000 | 44873 | 0.2075295 |  |  |
| 15x15 | 0.2 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 9.14061405 | 9.14061405 | 15570 | 45000 | 44873 | 0.09035145 |  |  |
| 15x15 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0 | 4.84519819e-13 | 14266 | 45000 | 45000 | 0.0147627 |  |  |
| 15x15 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 4.84519819e-13 | 14266 |  |  | 2.6639008 | 60 | 43 |
| 15x15 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 4.84519819e-13 | 14266 |  |  | 2.0288551 | 300 | 7 |
| 15x15 | 0.2 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B45000 | decoder | 5 | 87.6255852 | 87.6255852 | 30878 | 45000 | 45000 | 0.1116246 |  |  |
| 15x15 | 0.2 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 6.6802187 | 6.6802187 | 15219 | 45000 | 45000 | 0.04032835 |  |  |
| 15x15 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 0.112154774 | 0.112154774 | 14282 | 45000 | 45000 | 0.01766015 |  |  |
| 15x15 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 19.6761531 | 19.6761531 | 17073 |  | 1 | 0.0011436 |  |  |
| 15x15 | 1 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 16.3952196 | 16.3952196 | 41879 |  | 1 | 0.0020622 |  |  |
| 15x15 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 1.35369915 | 1.35369915 | 37312 | 45000 | 43125 | 0.2004616 |  |  |
| 15x15 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 2.32372955 | 2.32372955 | 37052.5 | 45000 | 44845 | 0.17635465 |  |  |
| 15x15 | 1 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 1.35369915 | 1.35369915 | 37306 | 45000 | 43220.5 | 0.2078846 |  |  |
| 15x15 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 1.82601445 | 1.82601445 | 36637 | 45000 | 44857 | 0.14857155 |  |  |
| 15x15 | 1 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 6.91270194 | 6.91270194 | 38173 | 45000 | 44873 | 0.19953395 |  |  |
| 15x15 | 1 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 12.2587817 | 12.2587817 | 40663.5 | 45000 | 44873 | 0.08616135 |  |  |
| 15x15 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0.57390885 | 0.57390885 | 35980 | 45000 | 45000 | 0.0142781 |  |  |
| 15x15 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 0 | 35980 |  |  | 3.5701075 | 60 | 213 |
| 15x15 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 0 | 35980 |  |  | 2.3717563 | 300 | 29 |
| 15x15 | 1 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B45000 | decoder | 5 | 69.3597782 | 69.3597782 | 67512 | 45000 | 45000 | 0.1078513 |  |  |
| 15x15 | 1 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 10.5024455 | 10.5024455 | 38682 | 45000 | 45000 | 0.04018605 |  |  |
| 15x15 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 1.63424125 | 1.63424125 | 36568 | 45000 | 45000 | 0.01741985 |  |  |
| 15x15 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 26.9093941 | 26.9093941 | 45662 |  | 1 | 0.001096 |  |  |
| 20x20 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 7.53714348 | 7.54145271 | 22257 |  | 1 | 0.00301830001 |  |  |
| 20x20 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 1.86530745 | 1.8693894 | 20425.5 | 80000 | 78160 | 0.4861723 |  |  |
| 20x20 | 0.2 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 1.86530745 | 1.8693894 | 20425.5 | 80000 | 80000 | 0.5086313 |  |  |
| 20x20 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 1.78524432 | 1.78524432 | 20364 | 80000 | 79950 | 0.40829545 |  |  |
| 20x20 | 0.2 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 2.44821603 | 2.45232134 | 20547.5 | 80000 | 78486 | 0.51462835 |  |  |
| 20x20 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 2.4497763 | 2.4497763 | 20364 | 80000 | 79924.5 | 0.30597855 |  |  |
| 20x20 | 0.2 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 9.17877333 | 9.18500799 | 22253 | 80000 | 79947 | 0.4883102 |  |  |
| 20x20 | 0.2 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 18.5966928 | 18.5966928 | 23739.5 | 80000 | 79947 | 0.2463912 |  |  |
| 20x20 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0.293885429 | 0.293885429 | 20017 | 80000 | 80000 | 0.0248311 |  |  |
| 20x20 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 2.02659579e-12 | 20017 |  |  | 16.7830533 | 60 | 1274 |
| 20x20 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 2.02659579e-12 | 20017 |  |  | 8.5309921 | 300 | 2724 |
| 20x20 | 0.2 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B80000 | decoder | 5 | 141.97484 | 141.984536 | 47663.5 | 80000 | 80000 | 0.3405766 |  |  |
| 20x20 | 0.2 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 16.1812459 | 16.1812459 | 23256 | 80000 | 80000 | 0.11347215 |  |  |
| 20x20 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 1.23914378 | 1.23914378 | 20290 | 80000 | 80000 | 0.02922115 |  |  |
| 20x20 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 32.1027127 | 32.1027127 | 26443 |  | 1 | 0.0011245 |  |  |
| 20x20 | 0.2 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 2.57281311 | 2.57281311 | 20532 | 80000 | 80000 | 0.10219965 |  |  |
| 20x20 | 0.2 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 0.521975612 | 0.521975612 | 20372 | 80000 | 80000 | 0.1029459 |  |  |
| 20x20 | 0.2 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 1.22379156 | 1.22379156 | 20541.5 | 80000 | 80000 | 0.1079898 |  |  |
| 20x20 | 0.2 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 0.671111501 | 0.671111501 | 20342 | 80000 | 80000 | 0.11431895 |  |  |
| 20x20 | 0.2 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 0.693043249 | 0.693043249 | 20424 | 80000 | 80000 | 0.12282125 |  |  |
| 20x20 | 0.2 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 2.66032108 | 2.66032108 | 20732 | 80000 | 80000 | 0.32507655 |  |  |
| 20x20 | 0.2 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 2.39494693 | 2.39494693 | 20532 | 80000 | 80000 | 0.3621222 |  |  |
| 20x20 | 1 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 23.9096314 | 23.9117865 | 52104 |  | 1 | 0.0037022 |  |  |
| 20x20 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 3.59953475 | 3.59953475 | 42701.5 | 80000 | 78160 | 0.48564255 |  |  |
| 20x20 | 1 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 3.59953475 | 3.59953475 | 42701.5 | 80000 | 80000 | 0.48162385 |  |  |
| 20x20 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 4.56760654 | 4.56760654 | 43289 | 80000 | 79950 | 0.4196399 |  |  |
| 20x20 | 1 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 3.69605029 | 3.69605029 | 42847 | 80000 | 78341.5 | 0.5122102 |  |  |
| 20x20 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 4.78144115 | 4.78144115 | 43050.5 | 80000 | 79859.5 | 0.31118845 |  |  |
| 20x20 | 1 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 12.7421352 | 12.7438432 | 46890.5 | 80000 | 79947 | 0.4717226 |  |  |
| 20x20 | 1 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 18.7826346 | 18.7826346 | 51259 | 80000 | 79947 | 0.2291993 |  |  |
| 20x20 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0.75862069 | 0.760373118 | 41067 | 80000 | 80000 | 0.02639185 |  |  |
| 20x20 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 1.80912965e-14 | 41061 |  |  | 13.2875988 | 60 | 970 |
| 20x20 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 5 | 0 | 1.80912965e-14 | 41061 |  |  | 8.4033734 | 300 | 3475 |
| 20x20 | 1 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B80000 | decoder | 5 | 113.820901 | 113.820901 | 87797 | 80000 | 80000 | 0.33836415 |  |  |
| 20x20 | 1 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 14.0782734 | 14.0782734 | 48221 | 80000 | 80000 | 0.11207395 |  |  |
| 20x20 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 1.26884392 | 1.26884392 | 41582 | 80000 | 80000 | 0.03090345 |  |  |
| 20x20 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 32.6793973 | 32.6793973 | 55276 |  | 1 | 0.00134469999 |  |  |
| 20x20 | 1 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 4.08561237 | 4.08742266 | 42448.5 | 80000 | 80000 | 0.09798415 |  |  |
| 20x20 | 1 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 2.09972927 | 2.10127601 | 41527 | 80000 | 80000 | 0.1033217 |  |  |
| 20x20 | 1 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 3.88631956 | 3.88631956 | 42833.5 | 80000 | 80000 | 0.1087487 |  |  |
| 20x20 | 1 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 1.53745541 | 1.53922138 | 41594 | 80000 | 80000 | 0.11514185 |  |  |
| 20x20 | 1 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 2.14558827 | 2.14558827 | 42320.5 | 80000 | 80000 | 0.13121685 |  |  |
| 20x20 | 1 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 4.2089026 | 4.21048129 | 43313 | 80000 | 80000 | 0.32517185 |  |  |
| 20x20 | 1 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 2.92555982 | 2.92711907 | 43415 | 80000 | 80000 | 0.35865855 |  |  |
| 30x30 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 9.42578548 | 12.039668 | 22658 |  | 1 | 0.0170986 |  |  |
| 30x30 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 5.78467402 | 5.82547954 | 22159.5 | 180000 | 177875 | 1.6164473 |  |  |
| 30x30 | 0.2 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 5.78467402 | 5.82547954 | 22159.5 | 180000 | 180000 | 1.71540675 |  |  |
| 30x30 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 5.18441852 | 6.33911051 | 22358 | 180000 | 179955 | 1.50924955 |  |  |
| 30x30 | 0.2 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 5.901863 | 7.50172419 | 22510.5 | 180000 | 178530.5 | 1.7301643 |  |  |
| 30x30 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 5.39819376 | 7.52246441 | 22847 | 180000 | 180000 | 0.8275851 |  |  |
| 30x30 | 0.2 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 17.8184983 | 19.5983843 | 25043.5 | 180000 | 179915 | 1.5229913 |  |  |
| 30x30 | 0.2 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 27.9326307 | 30.072306 | 27914 | 180000 | 179915 | 0.99701165 |  |  |
| 30x30 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 0.970917835 | 2.12948198 | 21373 | 180000 | 180000 | 0.05826095 |  |  |
| 30x30 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0.155250282 | 1.6682973 | 21289 |  |  | 60.0136695 | 60 | 1377 |
| 30x30 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 2 | 0 | 0.385586825 | 23487 |  |  | 224.884347 | 300 | 32226.5 |
| 30x30 | 0.2 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B180000 | decoder | 5 | 204.286847 | 204.301672 | 62332 | 180000 | 180000 | 1.51488845 |  |  |
| 30x30 | 0.2 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 27.8347705 | 29.1860639 | 27290 | 180000 | 180000 | 0.4671886 |  |  |
| 30x30 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 1.73906553 | 2.84664723 | 21682 | 180000 | 180000 | 0.0645342 |  |  |
| 30x30 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 31.9905447 | 34.1980886 | 28671 |  | 1 | 0.00254849999 |  |  |
| 30x30 | 0.2 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 2.25488862 | 3.03952247 | 21717 | 180000 | 180000 | 0.29757715 |  |  |
| 30x30 | 0.2 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 0.881512853 | 2.49237002 | 21404 | 180000 | 180000 | 0.3141078 |  |  |
| 30x30 | 0.2 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 2.07114015 | 3.14293616 | 21555 | 180000 | 180000 | 0.318955 |  |  |
| 30x30 | 0.2 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 1.18684133 | 2.57958378 | 21399 | 180000 | 180000 | 0.3548784 |  |  |
| 30x30 | 0.2 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 1.36196839 | 2.89324531 | 21545.5 | 180000 | 180000 | 0.3842858 |  |  |
| 30x30 | 0.2 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 2.68137035 | 3.95570165 | 21743 | 180000 | 180000 | 1.1624187 |  |  |
| 30x30 | 0.2 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 2.56194954 | 3.81494109 | 21738.5 | 180000 | 180000 | 1.25128585 |  |  |
| 30x30 | 1 | Balinski | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 19.7529528 | 23.2121659 | 63047 |  | 1 | 0.0052907 |  |  |
| 30x30 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 7.33663151 | 7.89328391 | 56908.5 | 180000 | 177875 | 1.64651485 |  |  |
| 30x30 | 1 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 7.33663151 | 7.89328391 | 56908.5 | 180000 | 180000 | 1.77641495 |  |  |
| 30x30 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 7.33936275 | 9.54923171 | 56731 | 180000 | 179955 | 1.49377215 |  |  |
| 30x30 | 1 | GA-hybrid | paper_artifacts_v3/fctp/raw/runs.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget-ls10 | decoder + local search | 5 | 8.52191024 | 8.52378302 | 57356 | 180000 | 178321.5 | 1.75513895 |  |  |
| 30x30 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/runs_ft.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 8.03565576 | 8.14220938 | 57137.5 | 180000 | 180000 | 0.8367208 |  |  |
| 30x30 | 1 | GA-rand-cycle | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-cycle:2-random-budget | decoder | 5 | 24.0388254 | 24.9416546 | 65557 | 180000 | 179915 | 1.5969682 |  |  |
| 30x30 | 1 | GA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | P143-pc0.97724-t5-e1-swap_scaled:0.0837194-random-budget | decoder | 5 | 36.1974919 | 36.5553725 | 72171 | 180000 | 179915 | 1.01442455 |  |  |
| 30x30 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 1.57741802 | 3.21208181 | 54092 | 180000 | 180000 | 0.059061 |  |  |
| 30x30 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/mip.jsonl | - |  | 5 | 0 | 1.84094271 | 52914 |  |  | 60.0069128 | 60 | 2200 |
| 30x30 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 2 | 0 | 0.00172921565 | 54017 |  |  | 49.9394744 | 300 | 12497 |
| 30x30 | 1 | RS | paper_artifacts_v3/fctp/raw/runs.jsonl | B180000 | decoder | 5 | 153.944798 | 157.689036 | 132579.5 | 180000 | 180000 | 1.52889495 |  |  |
| 30x30 | 1 | SA-rand-tuned | paper_artifacts_v3/fctp/raw/runs.jsonl | ins0.444-acc0.164-fr0.0044-random-budget | decoder | 5 | 32.1359661 | 36.4994772 | 69690.5 | 180000 | 180000 | 0.45073255 |  |  |
| 30x30 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 2.31178433 | 3.68404473 | 54884.5 | 180000 | 180000 | 0.0667031 |  |  |
| 30x30 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/runs.jsonl | - | complete objective | 5 | 37.05527 | 39.7925711 | 71505 |  | 1 | 0.0016485 |  |  |
| 30x30 | 1 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 3.69900855 | 4.32296304 | 54807 | 180000 | 180000 | 0.29949675 |  |  |
| 30x30 | 1 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 2.3508335 | 3.71064806 | 54806 | 180000 | 180000 | 0.31682945 |  |  |
| 30x30 | 1 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 4.70494418 | 6.02998384 | 56038 | 180000 | 180000 | 0.3227369 |  |  |
| 30x30 | 1 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 2.36066505 | 4.13125282 | 55034.5 | 180000 | 180000 | 0.3560523 |  |  |
| 30x30 | 1 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 2.81291648 | 4.70564336 | 55554.5 | 180000 | 180000 | 0.39705435 |  |  |
| 30x30 | 1 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 4.8054445 | 6.73485268 | 56538.5 | 180000 | 180000 | 1.16879115 |  |  |
| 30x30 | 1 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 4.90920952 | 6.41975822 | 56244 | 180000 | 180000 | 1.2690868 |  |  |
| 50x50 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 16.9235491 | 21.340252 | 35022 |  | 1 | 0.0183384 |  |  |
| 50x50 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/large.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 9.56792269 | 13.9884075 | 32702.5 | 500000 | 498580 | 11.5124729 |  |  |
| 50x50 | 0.2 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 9.56792269 | 13.9884075 | 32702.5 | 500000 | 500000 | 11.5110552 |  |  |
| 50x50 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 7.88897386 | 11.8266141 | 32018.5 | 500000 | 499735 | 10.6463101 |  |  |
| 50x50 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 9.64861457 | 13.4007545 | 32200.5 | 500000 | 500000 | 3.15828025 |  |  |
| 50x50 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 1.77106507 | 5.20050428 | 29998.5 | 500000 | 500000 | 0.22116615 |  |  |
| 50x50 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/large_mip.jsonl | - |  | 5 | 1.67428221 | 4.13773768 | 29817 |  |  | 60.0212413 | 60 | 302 |
| 50x50 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 2 | 0 | 2.2021806 | 31000 |  |  | 301.135283 | 300 | 13273 |
| 50x50 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 3.73729796 | 6.82405754 | 30620 | 500000 | 500000 | 0.2620843 |  |  |
| 50x50 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 23.9835043 | 28.8424671 | 40446 |  | 1 | 0.0058555 |  |  |
| 50x50 | 0.2 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 3.89216455 | 7.19602206 | 30746.5 | 500000 | 500000 | 1.44869165 |  |  |
| 50x50 | 0.2 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 3.69619304 | 7.25349297 | 30653 | 500000 | 500000 | 1.4293188 |  |  |
| 50x50 | 0.2 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 5.56559081 | 9.0930829 | 31090 | 500000 | 500000 | 1.44047885 |  |  |
| 50x50 | 0.2 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 3.27528032 | 6.85987781 | 30536 | 500000 | 500000 | 1.7545522 |  |  |
| 50x50 | 0.2 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 4.51416107 | 8.24256104 | 30881.5 | 500000 | 500000 | 1.8783144 |  |  |
| 50x50 | 0.2 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 5.70873522 | 9.03780295 | 31220 | 500000 | 500000 | 6.7100137 |  |  |
| 50x50 | 0.2 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 5.53832521 | 9.13566533 | 30997 | 500000 | 500000 | 6.92866075 |  |  |
| 50x50 | 1 | Balinski | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 19.1888207 | 24.0572645 | 76277 |  | 1 | 0.016739 |  |  |
| 50x50 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/large.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 11.8714886 | 14.9493933 | 69994.5 | 500000 | 498580 | 11.1888487 |  |  |
| 50x50 | 1 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 11.8714886 | 14.9493933 | 69994.5 | 500000 | 500000 | 9.8631071 |  |  |
| 50x50 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 8.77163782 | 12.3396048 | 68085 | 500000 | 499735 | 10.4465643 |  |  |
| 50x50 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 11.183335 | 15.7247829 | 70078 | 500000 | 500000 | 3.1526914 |  |  |
| 50x50 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 1.8272581 | 5.20605789 | 65172.5 | 500000 | 500000 | 0.1996498 |  |  |
| 50x50 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/large_mip.jsonl | - |  | 5 | 0.153704816 | 4.59547501 | 65383 |  |  | 60.0499487 | 60 | 327 |
| 50x50 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 2 | 0 | 2.60665615 | 60302.5 |  |  | 300.410596 | 300 | 18991.5 |
| 50x50 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 4.00904854 | 7.56507077 | 66786 | 500000 | 500000 | 0.22175235 |  |  |
| 50x50 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 36.395949 | 41.9672434 | 86997 |  | 1 | 0.0062971 |  |  |
| 50x50 | 1 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 3.5146233 | 7.74283132 | 66192 | 500000 | 500000 | 1.46973655 |  |  |
| 50x50 | 1 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 3.60608096 | 7.41933 | 66311 | 500000 | 500000 | 1.45574655 |  |  |
| 50x50 | 1 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 6.27548709 | 10.2182337 | 68019.5 | 500000 | 500000 | 1.4537459 |  |  |
| 50x50 | 1 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 3.60998703 | 7.13721658 | 66313.5 | 500000 | 500000 | 1.79984605 |  |  |
| 50x50 | 1 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 5.06226271 | 8.55044365 | 67243 | 500000 | 500000 | 1.98127915 |  |  |
| 50x50 | 1 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 6.68953018 | 10.6972196 | 68284.5 | 500000 | 500000 | 6.8884775 |  |  |
| 50x50 | 1 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 7.11372904 | 10.4158206 | 68556 | 500000 | 500000 | 7.17586665 |  |  |
| 70x70 | 0.2 | Balinski | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 18.6442021 | 23.4104384 | 42792 |  | 1 | 0.0377624 |  |  |
| 70x70 | 0.2 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/large.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 10.404838 | 16.1789427 | 40293 | 980000 | 978290 | 40.0602918 |  |  |
| 70x70 | 0.2 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 10.404838 | 16.1789427 | 40293 | 980000 | 980000 | 35.9785259 |  |  |
| 70x70 | 0.2 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 9.02104735 | 14.5811933 | 39730.5 | 980000 | 979995 | 37.6979252 |  |  |
| 70x70 | 0.2 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 11.8731349 | 17.665589 | 40800 | 980000 | 980000 | 6.79947675 |  |  |
| 70x70 | 0.2 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 1.16547397 | 6.18488389 | 36817 | 980000 | 980000 | 0.4541096 |  |  |
| 70x70 | 0.2 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/large_mip.jsonl | - |  | 5 | 1.31248845 | 6.20931985 | 36614 |  |  | 60.0125714 | 60 | 122 |
| 70x70 | 0.2 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 1 | 0 | 5.22993812 | 37867 |  |  | 301.473449 | 300 | 6059 |
| 70x70 | 0.2 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 3.76218627 | 9.40054396 | 37173.5 | 980000 | 980000 | 0.5289524 |  |  |
| 70x70 | 0.2 | VAM-lin | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 34.6426541 | 41.2869937 | 48120 |  | 1 | 0.0103614 |  |  |
| 70x70 | 0.2 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 3.00637834 | 8.22796442 | 37180.5 | 980000 | 980000 | 4.1423674 |  |  |
| 70x70 | 0.2 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 3.34378991 | 8.74445234 | 37226.5 | 980000 | 980000 | 4.15193925 |  |  |
| 70x70 | 0.2 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 5.42273615 | 10.92521 | 37770 | 980000 | 980000 | 4.04196085 |  |  |
| 70x70 | 0.2 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 3.27076138 | 8.6609142 | 37160.5 | 980000 | 980000 | 5.0156235 |  |  |
| 70x70 | 0.2 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 4.12824748 | 9.68211661 | 37459.5 | 980000 | 980000 | 5.32376925 |  |  |
| 70x70 | 0.2 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 5.90629224 | 11.4340049 | 37833.5 | 980000 | 980000 | 23.2036016 |  |  |
| 70x70 | 0.2 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 5.15795903 | 10.4721603 | 37880 | 980000 | 980000 | 23.6354381 |  |  |
| 70x70 | 1 | Balinski | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 20.1832448 | 26.1075357 | 95887 |  | 1 | 0.0379011 |  |  |
| 70x70 | 1 | GA-cost-cycle | paper_artifacts_v3/fctp/raw/large.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 11.5099779 | 17.9835073 | 89741 | 980000 | 978290 | 42.7925443 |  |  |
| 70x70 | 1 | GA-cost-cycle | paper_artifacts_v3/review2/raw/K1.jsonl | P2700-pc0.965569-t8-e5-cycle:1-cost-aware-budget | decoder | 5 | 11.5099779 | 17.9835073 | 89741 | 980000 | 980000 | 33.4427215 |  |  |
| 70x70 | 1 | GA-cost-cycle-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget | decoder | 5 | 10.4613707 | 16.2330369 | 88887 | 980000 | 979995 | 40.9110272 |  |  |
| 70x70 | 1 | GA-hybrid-ft | paper_artifacts_v3/fctp/raw/large.jsonl | P300-pc0.965569-t8-e5-cycle:2-cost-aware-budget-ls3 | decoder + local search | 5 | 14.2220591 | 19.2531834 | 92177.5 | 980000 | 980000 | 7.28473755 |  |  |
| 70x70 | 1 | ILS | paper_artifacts_v3/review/raw/rivals.jsonl | ils-p8-better | start + neighbour | 5 | 1.54114587 | 7.37559462 | 81644 | 980000 | 980000 | 0.46217035 |  |  |
| 70x70 | 1 | MIP, 1 thread / 60 s | paper_artifacts_v3/fctp/raw/large_mip.jsonl | - |  | 5 | 1.95708394 | 8.01706615 | 82651 |  |  | 60.0146621 | 60 | 107 |
| 70x70 | 1 | MIP, default threads / 300 s | paper_artifacts_v3/review/raw/mip_default.jsonl | threads0-300s |  | 1 | 0 | 3.96499349 | 82359 |  |  | 303.04622 | 300 | 6996 |
| 70x70 | 1 | Tabu | paper_artifacts_v3/review/raw/rivals.jsonl | tabu-s0.25-T5 | start + neighbour | 5 | 4.02195292 | 10.0511057 | 85069 | 980000 | 980000 | 0.5191467 |  |  |
| 70x70 | 1 | VAM-lin | paper_artifacts_v3/fctp/raw/large.jsonl | - | complete objective | 5 | 43.0408334 | 48.7123932 | 115255 |  | 1 | 0.0112358 |  |  |
| 70x70 | 1 | a | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=1, r=4, OX=0 | complete objective | 5 | 3.87807848 | 9.25601279 | 83599 | 980000 | 980000 | 4.26511555 |  |  |
| 70x70 | 1 | b30 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=30, r=4, OX=0 | complete objective | 5 | 3.88271476 | 9.75218751 | 83571 | 980000 | 980000 | 4.25586325 |  |  |
| 70x70 | 1 | b300 | paper_artifacts_v3/review2/raw/K1.jsonl | independent, P=300, r=4, OX=0 | complete objective | 5 | 6.28743259 | 12.5780639 | 85538 | 980000 | 980000 | 4.18360715 |  |  |
| 70x70 | 1 | c30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0 | complete objective | 5 | 3.70331539 | 9.36775323 | 83684.5 | 980000 | 980000 | 5.2325652 |  |  |
| 70x70 | 1 | c300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0 | complete objective | 5 | 5.48061671 | 11.0681761 | 85057.5 | 980000 | 980000 | 5.4916296 |  |  |
| 70x70 | 1 | d30 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=30, r=4, OX=0.96556855 | complete objective | 5 | 6.25150688 | 11.6231052 | 85795 | 980000 | 980000 | 24.8972044 |  |  |
| 70x70 | 1 | d300 | paper_artifacts_v3/review2/raw/K1.jsonl | population, P=300, r=4, OX=0.96556855 | complete objective | 5 | 7.24421581 | 12.6053611 | 86308 | 980000 | 980000 | 25.890925 |  |  |
