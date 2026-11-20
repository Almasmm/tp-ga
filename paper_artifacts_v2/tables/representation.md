# Representation: decoder prefix, neutrality, locality, heritability (non-confirmatory)

Medians over instances and seeds; source random = random permutations, otherwise the tuned GA population at the given fraction of the budget.

| set | size | mn | source | snapshot | measure | operator | k | metric | median | q1 | q3 | values | instances |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.932 | 0.925 | 0.939 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.500 | 0.444 | 0.556 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.581 | 0.546 | 0.591 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0.053 | 0.043 | 0.069 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.350 | 0.311 | 0.361 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.250 | 0.177 | 0.270 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.086 | 0.073 | 0.095 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.421 | 0.275 | 0.491 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.014 | 0.011 | 0.016 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.605 | 0.411 | 0.685 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.001 | 0.001 | 0.002 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.616 | 0.592 | 0.643 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.039 | 0.031 | 0.043 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.039 | 0.032 | 0.044 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.039 | 0.033 | 0.044 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.039 | 0.031 | 0.043 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.039 | 0.032 | 0.044 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.039 | 0.033 | 0.044 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.582 | 0.546 | 0.592 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.581 | 0.549 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.578 | 0.546 | 0.589 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.582 | 0.546 | 0.592 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.581 | 0.549 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.578 | 0.546 | 0.589 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.582 | 0.545 | 0.598 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.583 | 0.546 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.582 | 0.544 | 0.594 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.582 | 0.545 | 0.598 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.583 | 0.546 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.582 | 0.544 | 0.594 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.011 | 0.015 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.011 | 0.016 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.011 | 0.016 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.011 | 0.015 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.011 | 0.016 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.011 | 0.016 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.215 | 0.183 | 0.226 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.216 | 0.181 | 0.231 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.216 | 0.182 | 0.229 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.215 | 0.183 | 0.226 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.216 | 0.181 | 0.231 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.216 | 0.182 | 0.229 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.048 | 0.052 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.052 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.978 | 0.976 | 0.981 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.977 | 0.981 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.978 | 0.976 | 0.980 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.571 | 0.529 | 0.599 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.570 | 0.534 | 0.605 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.563 | 0.528 | 0.605 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.196 | 0.203 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.195 | 0.206 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.194 | 0.205 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.914 | 0.908 | 0.920 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.914 | 0.908 | 0.920 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.916 | 0.910 | 0.920 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.573 | 0.544 | 0.597 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.571 | 0.547 | 0.601 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.575 | 0.548 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.582 | 0.550 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.583 | 0.551 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.584 | 0.549 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.582 | 0.550 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.583 | 0.551 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.584 | 0.549 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.750 | 0 | 1.000 | 16 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 1.000 | 1.000 | 15 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.583 | 0 | 1.000 | 22 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.001 | 7.407e-04 | 0.001 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.001 | 7.407e-04 | 0.002 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.001 | 7.407e-04 | 0.001 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.500 | 0.333 | 0.750 | 93 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.600 | 0.421 | 0.800 | 96 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.571 | 0.400 | 0.800 | 97 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.026 | 0.024 | 0.028 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.025 | 0.023 | 0.027 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.026 | 0.024 | 0.028 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.989 | 0.987 | 0.990 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.989 | 0.987 | 0.990 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.571 | 0.516 | 0.606 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.576 | 0.529 | 0.621 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.566 | 0.533 | 0.606 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.580 | 0.546 | 0.592 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.582 | 0.547 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.583 | 0.547 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.580 | 0.546 | 0.592 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.582 | 0.547 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.583 | 0.547 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.578 | 0.545 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.585 | 0.544 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.584 | 0.546 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.578 | 0.545 | 0.593 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.585 | 0.544 | 0.596 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.584 | 0.546 | 0.595 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.349 | 0.311 | 0.364 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.349 | 0.311 | 0.361 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.350 | 0.312 | 0.365 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.349 | 0.311 | 0.364 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.349 | 0.311 | 0.361 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.350 | 0.312 | 0.365 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 9.000 | 9.000 | 9.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 9.000 | 9.000 | 9.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 22.000 | 21.000 | 23.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.880 | 0.840 | 0.920 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.959 | 0.953 | 0.967 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.556 | 0.556 | 0.667 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.584 | 0.552 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0.076 | 0.041 | 0.105 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.357 | 0.320 | 0.385 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.303 | 0.200 | 0.410 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.091 | 0.070 | 0.119 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.513 | 0.372 | 0.704 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.730 | 0.487 | 0.917 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.626 | 0.608 | 0.647 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.035 | 0.028 | 0.049 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.042 | 0.028 | 0.056 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.042 | 0.035 | 0.058 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.035 | 0.028 | 0.049 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.042 | 0.028 | 0.056 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.042 | 0.035 | 0.058 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.552 | 0.524 | 0.589 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.584 | 0.552 | 0.615 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.594 | 0.573 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.552 | 0.524 | 0.589 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.584 | 0.552 | 0.615 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.594 | 0.573 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.587 | 0.559 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.594 | 0.566 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.587 | 0.559 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.594 | 0.566 | 0.622 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.014 | 0.007 | 0.028 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.014 | 0.007 | 0.028 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.203 | 0.175 | 0.231 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.217 | 0.187 | 0.245 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.231 | 0.210 | 0.266 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.203 | 0.175 | 0.231 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.217 | 0.187 | 0.245 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.231 | 0.210 | 0.266 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.972 | 0.986 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.972 | 0.986 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.972 | 0.986 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.600 | 0.490 | 0.700 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.600 | 0.500 | 0.733 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.600 | 0.429 | 0.723 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.173 | 0.217 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.173 | 0.224 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.175 | 0.217 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.916 | 0.902 | 0.930 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.923 | 0.909 | 0.930 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.559 | 0.481 | 0.630 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.607 | 0.533 | 0.646 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.625 | 0.558 | 0.701 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.601 | 0.552 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.608 | 0.573 | 0.636 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.601 | 0.552 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.608 | 0.573 | 0.636 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0 | 0 | 0 | 1 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | – | – | – | 0 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.500 | 0.250 | 0.750 | 2 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 1.000 | 0 | 1.000 | 12 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 1.000 | 0 | 1.000 | 16 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 1.000 | 0 | 1.000 | 21 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.028 | 0.014 | 0.035 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.028 | 0.021 | 0.035 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.028 | 0.014 | 0.035 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.990 | 0.986 | 0.993 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.993 | 0.986 | 0.993 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.993 | 0.986 | 0.993 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.500 | 0.400 | 0.750 | 97 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.571 | 0.425 | 0.750 | 98 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.500 | 0.400 | 0.800 | 96 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.566 | 0.531 | 0.594 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.594 | 0.565 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.608 | 0.573 | 0.636 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.566 | 0.531 | 0.594 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.594 | 0.565 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.608 | 0.573 | 0.636 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.591 | 0.558 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.615 | 0.579 | 0.643 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.566 | 0.538 | 0.587 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.591 | 0.558 | 0.629 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.615 | 0.579 | 0.643 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.336 | 0.308 | 0.357 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.364 | 0.322 | 0.392 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.378 | 0.343 | 0.406 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.336 | 0.308 | 0.357 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.364 | 0.322 | 0.392 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.378 | 0.343 | 0.406 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 9.000 | 9.000 | 9.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 9.000 | 9.000 | 9.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 22.000 | 21.000 | 23.000 | 100 | 10 |
| uniform | 5x5 | 25 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.880 | 0.840 | 0.920 | 100 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 1.000 | neutral_share | 0.556 | 0.538 | 0.562 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 2.000 | median_rel_change | 0.072 | 0.064 | 0.081 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 2.000 | neutral_share | 0.320 | 0.316 | 0.323 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 5.000 | median_rel_change | 0.189 | 0.157 | 0.224 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 5.000 | neutral_share | 0.075 | 0.074 | 0.079 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 10.000 | median_rel_change | 0.257 | 0.215 | 0.312 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 10.000 | neutral_share | 0.014 | 0.014 | 0.018 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 20.000 | median_rel_change | 0.302 | 0.242 | 0.370 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | 20.000 | neutral_share | 0.002 | 0.001 | 0.003 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.481 | 0.473 | 0.491 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.037 | 0.035 | 0.038 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.037 | 0.035 | 0.038 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.564 | 0.554 | 0.572 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.564 | 0.554 | 0.572 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.560 | 0.554 | 0.564 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.560 | 0.554 | 0.564 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.011 | 0.009 | 0.014 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.011 | 0.009 | 0.014 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.189 | 0.184 | 0.198 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.189 | 0.184 | 0.198 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.046 | 0.053 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.979 | 0.976 | 0.983 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.593 | 0.511 | 0.637 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.204 | 0.200 | 0.208 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.915 | 0.902 | 0.923 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.566 | 0.533 | 0.601 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.550 | 0.537 | 0.559 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.550 | 0.537 | 0.559 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | – | – | – | 0 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.002 | 0 | 0.003 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 1.000 | 0.999 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.833 | 0.167 | 1.000 | 6 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.027 | 0.024 | 0.028 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.989 | 0.988 | 0.992 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.571 | 0.562 | 0.644 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.548 | 0.543 | 0.557 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.548 | 0.543 | 0.557 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.552 | 0.540 | 0.569 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.552 | 0.540 | 0.569 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.325 | 0.313 | 0.334 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.325 | 0.313 | 0.334 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | prefix | - | - | basis_size | 9.000 | 9.000 | 9.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | prefix | - | - | positive_cells | 9.000 | 9.000 | 9.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | prefix | - | - | prefix_length | 22.250 | 22.000 | 23.000 | 10 | 10 |
| uniform | 5x5 | 25 | random | - | prefix | - | - | prefix_share | 0.890 | 0.880 | 0.920 | 10 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.862 | 0.853 | 0.869 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.526 | 0.474 | 0.556 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.678 | 0.663 | 0.685 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0.010 | 0.007 | 0.012 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.463 | 0.445 | 0.472 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.148 | 0.106 | 0.187 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.153 | 0.134 | 0.158 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.333 | 0.217 | 0.415 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.025 | 0.021 | 0.029 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.634 | 0.399 | 0.759 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 7.407e-04 | 3.704e-04 | 0.001 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.662 | 0.657 | 0.665 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.067 | 0.059 | 0.074 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.072 | 0.066 | 0.078 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.077 | 0.071 | 0.083 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.067 | 0.059 | 0.074 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.072 | 0.066 | 0.078 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.077 | 0.071 | 0.083 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.452 | 0.431 | 0.460 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.463 | 0.444 | 0.474 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.464 | 0.455 | 0.478 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.452 | 0.431 | 0.460 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.463 | 0.444 | 0.474 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.464 | 0.455 | 0.478 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.670 | 0.657 | 0.680 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.676 | 0.662 | 0.688 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.683 | 0.675 | 0.689 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.670 | 0.657 | 0.680 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.676 | 0.662 | 0.688 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.683 | 0.675 | 0.689 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.022 | 0.019 | 0.026 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.023 | 0.021 | 0.029 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.027 | 0.024 | 0.030 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.022 | 0.019 | 0.026 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.023 | 0.021 | 0.029 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.027 | 0.024 | 0.030 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.302 | 0.288 | 0.317 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.316 | 0.304 | 0.327 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.326 | 0.313 | 0.336 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.302 | 0.288 | 0.317 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.316 | 0.304 | 0.327 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.326 | 0.313 | 0.336 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.048 | 0.053 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.047 | 0.052 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.984 | 0.982 | 0.985 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.984 | 0.983 | 0.986 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.984 | 0.983 | 0.986 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.676 | 0.644 | 0.696 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.678 | 0.650 | 0.700 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.686 | 0.651 | 0.713 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.195 | 0.204 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.205 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.206 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.933 | 0.929 | 0.939 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.936 | 0.932 | 0.939 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.937 | 0.933 | 0.940 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.665 | 0.649 | 0.690 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.676 | 0.662 | 0.690 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.680 | 0.665 | 0.697 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.670 | 0.657 | 0.678 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.676 | 0.663 | 0.685 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.683 | 0.673 | 0.691 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.670 | 0.657 | 0.678 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.676 | 0.663 | 0.685 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.683 | 0.673 | 0.691 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.001 | 7.407e-04 | 0.002 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.001 | 7.407e-04 | 0.001 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.001 | 7.407e-04 | 0.002 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.999 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.667 | 0.500 | 1.000 | 98 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.667 | 0.500 | 1.000 | 94 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.667 | 0.500 | 1.000 | 98 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.017 | 0.016 | 0.019 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.017 | 0.016 | 0.019 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.017 | 0.015 | 0.019 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.994 | 0.994 | 0.996 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.995 | 0.994 | 0.996 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.994 | 0.994 | 0.996 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.678 | 0.630 | 0.723 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.674 | 0.630 | 0.736 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.692 | 0.643 | 0.734 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.281 | 0.276 | 0.289 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.282 | 0.277 | 0.288 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.282 | 0.277 | 0.288 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.909 | 0.904 | 0.912 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.910 | 0.906 | 0.915 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.911 | 0.907 | 0.916 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.650 | 0.636 | 0.664 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.661 | 0.646 | 0.674 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.663 | 0.649 | 0.682 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.669 | 0.658 | 0.679 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.677 | 0.666 | 0.687 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.682 | 0.674 | 0.690 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.669 | 0.658 | 0.679 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.677 | 0.666 | 0.687 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.682 | 0.674 | 0.690 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.448 | 0.431 | 0.465 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.460 | 0.444 | 0.473 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.467 | 0.456 | 0.478 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.448 | 0.431 | 0.465 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.460 | 0.444 | 0.473 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.467 | 0.456 | 0.478 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.139 | 0.127 | 0.151 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.149 | 0.139 | 0.158 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.156 | 0.148 | 0.162 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.139 | 0.127 | 0.151 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.149 | 0.139 | 0.158 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.156 | 0.148 | 0.162 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 19.000 | 19.000 | 19.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 19.000 | 19.000 | 19.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 89.000 | 88.000 | 89.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.890 | 0.880 | 0.890 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.963 | 0.960 | 0.968 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.684 | 0.667 | 0.737 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.734 | 0.706 | 0.755 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 5.378e-04 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.531 | 0.497 | 0.554 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.183 | 0.141 | 0.243 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.192 | 0.175 | 0.224 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.468 | 0.344 | 0.610 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.045 | 0.035 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.883 | 0.629 | 1.102 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0 | 0 | 0.007 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.689 | 0.676 | 0.698 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.077 | 0.063 | 0.091 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.105 | 0.084 | 0.133 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.119 | 0.103 | 0.133 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.077 | 0.063 | 0.091 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.105 | 0.084 | 0.133 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.119 | 0.103 | 0.133 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.476 | 0.441 | 0.503 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.517 | 0.483 | 0.554 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.524 | 0.495 | 0.573 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.476 | 0.441 | 0.503 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.517 | 0.483 | 0.554 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.524 | 0.495 | 0.573 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.685 | 0.657 | 0.713 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.720 | 0.699 | 0.743 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.727 | 0.706 | 0.762 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.685 | 0.657 | 0.713 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.720 | 0.699 | 0.743 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.727 | 0.706 | 0.762 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.028 | 0.021 | 0.037 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.042 | 0.033 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.042 | 0.028 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.028 | 0.021 | 0.037 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.042 | 0.033 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.042 | 0.028 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.329 | 0.301 | 0.364 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.385 | 0.364 | 0.413 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.399 | 0.357 | 0.427 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.329 | 0.301 | 0.364 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.385 | 0.364 | 0.413 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.399 | 0.357 | 0.427 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.045 | 0.028 | 0.056 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.058 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.984 | 0.993 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.696 | 0.600 | 0.833 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.750 | 0.625 | 0.833 | 99 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.774 | 0.634 | 0.878 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.175 | 0.219 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.182 | 0.231 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.175 | 0.219 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.937 | 0.921 | 0.944 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.944 | 0.935 | 0.958 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.951 | 0.937 | 0.958 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.672 | 0.600 | 0.734 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.739 | 0.679 | 0.778 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.730 | 0.656 | 0.784 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.678 | 0.664 | 0.706 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.724 | 0.698 | 0.748 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.720 | 0.699 | 0.736 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.678 | 0.664 | 0.706 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.724 | 0.698 | 0.748 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.720 | 0.699 | 0.736 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0 | 0 | 0 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 1.000 | 1.000 | 16 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 1.000 | 1.000 | 9 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 0 | 1.000 | 13 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.014 | 0.014 | 0.023 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.014 | 0.007 | 0.021 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.014 | 0.007 | 0.023 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.750 | 0.500 | 1.000 | 95 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.750 | 0.500 | 1.000 | 93 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.750 | 0.500 | 1.000 | 88 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.280 | 0.252 | 0.315 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.280 | 0.252 | 0.301 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.280 | 0.259 | 0.308 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.916 | 0.895 | 0.932 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.923 | 0.909 | 0.937 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.679 | 0.621 | 0.741 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.731 | 0.667 | 0.776 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.708 | 0.656 | 0.757 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.685 | 0.664 | 0.713 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.720 | 0.685 | 0.748 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.734 | 0.706 | 0.755 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.685 | 0.664 | 0.713 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.720 | 0.685 | 0.748 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.734 | 0.706 | 0.755 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.476 | 0.441 | 0.510 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.531 | 0.510 | 0.559 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.535 | 0.503 | 0.559 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.476 | 0.441 | 0.510 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.531 | 0.510 | 0.559 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.535 | 0.503 | 0.559 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.140 | 0.182 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.203 | 0.175 | 0.238 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.210 | 0.182 | 0.226 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.140 | 0.182 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.203 | 0.175 | 0.238 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.210 | 0.182 | 0.226 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 19.000 | 19.000 | 19.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 19.000 | 18.000 | 19.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 89.000 | 86.000 | 91.000 | 100 | 10 |
| uniform | 10x10 | 100 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.890 | 0.860 | 0.910 | 100 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 1.000 | neutral_share | 0.660 | 0.644 | 0.669 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 2.000 | median_rel_change | 0.016 | 0.011 | 0.018 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 2.000 | neutral_share | 0.442 | 0.436 | 0.453 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 5.000 | median_rel_change | 0.142 | 0.099 | 0.156 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 5.000 | neutral_share | 0.141 | 0.141 | 0.145 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 10.000 | median_rel_change | 0.249 | 0.162 | 0.267 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 10.000 | neutral_share | 0.021 | 0.017 | 0.023 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 20.000 | median_rel_change | 0.334 | 0.224 | 0.393 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | 20.000 | neutral_share | 0 | 0 | 0.001 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.573 | 0.566 | 0.579 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.067 | 0.059 | 0.068 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.067 | 0.059 | 0.068 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 2.000 | 2.000 | 2.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.449 | 0.446 | 0.462 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.449 | 0.446 | 0.462 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.669 | 0.666 | 0.677 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.669 | 0.666 | 0.677 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.022 | 0.020 | 0.026 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.022 | 0.020 | 0.026 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.301 | 0.295 | 0.309 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.301 | 0.295 | 0.309 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.048 | 0.043 | 0.049 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.985 | 0.982 | 0.987 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.666 | 0.613 | 0.722 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.204 | 0.197 | 0.210 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.931 | 0.925 | 0.936 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.659 | 0.646 | 0.680 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.673 | 0.664 | 0.685 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.673 | 0.664 | 0.685 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 5.000e-04 | 0 | 0.001 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.999 | 1.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.667 | 0 | 1.000 | 5 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.017 | 0.015 | 0.018 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.994 | 0.993 | 0.995 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.613 | 0.572 | 0.675 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 0.286 | 0.280 | 0.294 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.907 | 0.903 | 0.913 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.654 | 0.651 | 0.666 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.666 | 0.662 | 0.672 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.666 | 0.662 | 0.672 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.450 | 0.446 | 0.458 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.450 | 0.446 | 0.458 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.141 | 0.135 | 0.150 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.141 | 0.135 | 0.150 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | prefix | - | - | basis_size | 19.000 | 19.000 | 19.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | prefix | - | - | positive_cells | 19.000 | 19.000 | 19.000 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | prefix | - | - | prefix_length | 90.000 | 90.000 | 90.750 | 10 | 10 |
| uniform | 10x10 | 100 | random | - | prefix | - | - | prefix_share | 0.900 | 0.900 | 0.907 | 10 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.897 | 0.877 | 0.914 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.653 | 0.613 | 0.692 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.815 | 0.807 | 0.826 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.666 | 0.656 | 0.678 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.037 | 0.032 | 0.042 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.366 | 0.347 | 0.381 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.190 | 0.178 | 0.222 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.133 | 0.125 | 0.146 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.481 | 0.435 | 0.571 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.019 | 0.016 | 0.023 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.653 | 0.649 | 0.657 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.199 | 0.192 | 0.205 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.244 | 0.234 | 0.260 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.270 | 0.260 | 0.282 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.199 | 0.192 | 0.205 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.244 | 0.234 | 0.260 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.270 | 0.260 | 0.282 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.496 | 0.488 | 0.507 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.542 | 0.528 | 0.562 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.571 | 0.563 | 0.580 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.496 | 0.488 | 0.507 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.542 | 0.528 | 0.562 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.571 | 0.563 | 0.580 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.791 | 0.785 | 0.798 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.816 | 0.810 | 0.824 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.829 | 0.822 | 0.835 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.791 | 0.785 | 0.798 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.816 | 0.810 | 0.824 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.829 | 0.822 | 0.835 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.098 | 0.093 | 0.106 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.135 | 0.124 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.157 | 0.147 | 0.165 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.098 | 0.093 | 0.106 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.135 | 0.124 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.157 | 0.147 | 0.165 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.497 | 0.488 | 0.505 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.544 | 0.528 | 0.560 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.569 | 0.560 | 0.576 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.497 | 0.488 | 0.505 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.544 | 0.528 | 0.560 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.569 | 0.560 | 0.576 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.047 | 0.052 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.052 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.048 | 0.054 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.991 | 0.990 | 0.992 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.991 | 0.990 | 0.993 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.789 | 0.764 | 0.816 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.820 | 0.800 | 0.846 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.831 | 0.810 | 0.857 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.201 | 0.196 | 0.205 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.194 | 0.203 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.195 | 0.205 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.959 | 0.956 | 0.961 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.963 | 0.961 | 0.967 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.966 | 0.964 | 0.969 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.793 | 0.783 | 0.805 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.813 | 0.802 | 0.830 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.828 | 0.819 | 0.840 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.792 | 0.786 | 0.799 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.817 | 0.811 | 0.827 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.828 | 0.823 | 0.834 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.792 | 0.786 | 0.799 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.817 | 0.811 | 0.827 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.828 | 0.823 | 0.834 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.017 | 0.016 | 0.019 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.018 | 0.017 | 0.019 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.018 | 0.016 | 0.020 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.996 | 0.996 | 0.997 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.997 | 0.996 | 0.997 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.997 | 0.996 | 0.998 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.786 | 0.743 | 0.833 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.818 | 0.778 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.830 | 0.795 | 0.868 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.201 | 0.195 | 0.207 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.201 | 0.195 | 0.208 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.200 | 0.195 | 0.205 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.959 | 0.956 | 0.962 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.964 | 0.962 | 0.966 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.966 | 0.963 | 0.969 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.785 | 0.775 | 0.801 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.812 | 0.799 | 0.825 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.822 | 0.811 | 0.837 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.749 | 1.735 | 1.763 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.748 | 1.734 | 1.762 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.749 | 1.730 | 1.763 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.684 | 0.674 | 0.690 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.716 | 0.706 | 0.728 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.734 | 0.727 | 0.741 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.652 | 0.643 | 0.659 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.686 | 0.677 | 0.702 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.708 | 0.701 | 0.716 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.627 | 0.619 | 0.635 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.663 | 0.653 | 0.680 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.689 | 0.680 | 0.696 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.627 | 0.619 | 0.635 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.663 | 0.653 | 0.680 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.689 | 0.680 | 0.696 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.395 | 0.386 | 0.402 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.445 | 0.431 | 0.461 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.473 | 0.463 | 0.482 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.395 | 0.386 | 0.402 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.445 | 0.431 | 0.461 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.473 | 0.463 | 0.482 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.098 | 0.092 | 0.104 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.136 | 0.123 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.158 | 0.150 | 0.162 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.098 | 0.092 | 0.104 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.136 | 0.123 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.158 | 0.150 | 0.162 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 39.000 | 39.000 | 39.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 39.000 | 38.000 | 39.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 352.000 | 348.000 | 355.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.880 | 0.870 | 0.887 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.982 | 0.976 | 0.985 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.821 | 0.789 | 0.846 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.846 | 0.811 | 0.867 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.703 | 0.678 | 0.727 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0.032 | 0.018 | 0.055 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.420 | 0.392 | 0.442 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.256 | 0.218 | 0.317 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.168 | 0.147 | 0.196 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.622 | 0.562 | 0.741 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.028 | 0.021 | 0.042 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.652 | 0.637 | 0.665 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.238 | 0.203 | 0.259 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.280 | 0.257 | 0.322 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.294 | 0.273 | 0.315 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.238 | 0.203 | 0.259 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.280 | 0.257 | 0.322 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.294 | 0.273 | 0.315 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.538 | 0.510 | 0.573 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.587 | 0.558 | 0.615 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.594 | 0.559 | 0.622 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.538 | 0.510 | 0.573 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.587 | 0.558 | 0.615 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.594 | 0.559 | 0.622 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.811 | 0.783 | 0.834 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.832 | 0.811 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.846 | 0.825 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.811 | 0.783 | 0.834 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.832 | 0.811 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.846 | 0.825 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.126 | 0.110 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.168 | 0.147 | 0.191 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.175 | 0.154 | 0.198 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.126 | 0.110 | 0.147 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.168 | 0.147 | 0.191 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.175 | 0.154 | 0.198 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.538 | 0.509 | 0.573 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.587 | 0.552 | 0.610 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.587 | 0.566 | 0.615 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.538 | 0.509 | 0.573 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.587 | 0.552 | 0.610 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.587 | 0.566 | 0.615 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.042 | 0.035 | 0.063 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.833 | 0.714 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.833 | 0.750 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.857 | 0.800 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.182 | 0.224 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.182 | 0.210 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.189 | 0.219 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.965 | 0.958 | 0.979 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.965 | 0.958 | 0.979 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.818 | 0.755 | 0.871 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.831 | 0.800 | 0.890 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.845 | 0.804 | 0.880 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.818 | 0.790 | 0.832 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.839 | 0.818 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.839 | 0.811 | 0.867 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.818 | 0.790 | 0.832 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.839 | 0.818 | 0.860 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.839 | 0.811 | 0.867 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.021 | 0.014 | 0.028 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.014 | 0.007 | 0.023 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.021 | 0.014 | 0.028 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 0.667 | 1.000 | 93 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 0.667 | 1.000 | 90 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 1.000 | 0.800 | 1.000 | 93 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.196 | 0.175 | 0.219 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.196 | 0.175 | 0.224 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.203 | 0.175 | 0.231 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.965 | 0.951 | 0.979 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.965 | 0.958 | 0.979 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.965 | 0.958 | 0.979 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.830 | 0.760 | 0.869 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.828 | 0.791 | 0.870 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.827 | 0.783 | 0.870 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.741 | 1.678 | 1.811 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.748 | 1.699 | 1.818 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.762 | 1.699 | 1.811 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.720 | 0.678 | 0.741 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.748 | 0.719 | 0.776 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.748 | 0.720 | 0.769 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.686 | 0.652 | 0.716 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.725 | 0.692 | 0.747 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.726 | 0.693 | 0.749 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.664 | 0.642 | 0.685 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.706 | 0.685 | 0.734 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.699 | 0.671 | 0.720 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.664 | 0.642 | 0.685 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.706 | 0.685 | 0.734 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.699 | 0.671 | 0.720 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.434 | 0.406 | 0.462 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.490 | 0.448 | 0.510 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.490 | 0.460 | 0.524 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.434 | 0.406 | 0.462 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.490 | 0.448 | 0.510 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.490 | 0.460 | 0.524 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.133 | 0.105 | 0.154 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.168 | 0.147 | 0.203 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.182 | 0.152 | 0.210 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.133 | 0.105 | 0.154 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.168 | 0.147 | 0.203 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.182 | 0.152 | 0.210 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 39.000 | 39.000 | 39.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 38.000 | 38.000 | 39.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 355.000 | 340.000 | 371.000 | 100 | 10 |
| uniform | 20x20 | 400 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.887 | 0.850 | 0.927 | 100 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 1.000 | neutral_share | 0.790 | 0.788 | 0.794 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 2.000 | neutral_share | 0.621 | 0.611 | 0.627 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 5.000 | median_rel_change | 0.057 | 0.053 | 0.067 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 5.000 | neutral_share | 0.298 | 0.289 | 0.303 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 10.000 | median_rel_change | 0.146 | 0.139 | 0.172 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 10.000 | neutral_share | 0.086 | 0.076 | 0.091 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 20.000 | median_rel_change | 0.252 | 0.233 | 0.304 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | 20.000 | neutral_share | 0.009 | 0.008 | 0.011 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.614 | 0.609 | 0.623 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.184 | 0.178 | 0.188 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.184 | 0.178 | 0.188 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.478 | 0.477 | 0.488 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.478 | 0.477 | 0.488 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.786 | 0.779 | 0.794 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.786 | 0.779 | 0.794 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.088 | 0.085 | 0.094 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.088 | 0.085 | 0.094 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.482 | 0.475 | 0.491 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.482 | 0.475 | 0.491 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.046 | 0.044 | 0.053 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.990 | 0.989 | 0.991 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.789 | 0.770 | 0.823 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.194 | 0.191 | 0.203 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.958 | 0.957 | 0.964 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.792 | 0.776 | 0.810 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.792 | 0.781 | 0.799 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.792 | 0.781 | 0.799 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.019 | 0.017 | 0.021 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.997 | 0.996 | 0.998 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.846 | 0.805 | 0.881 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.207 | 0.199 | 0.210 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.955 | 0.950 | 0.956 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.770 | 0.748 | 0.774 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 1.742 | 1.734 | 1.767 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.673 | 0.669 | 0.686 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.642 | 0.632 | 0.652 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 2.000 | 2.000 | 2.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.601 | 0.592 | 0.614 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.601 | 0.592 | 0.614 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 4.000 | 4.000 | 4.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.369 | 0.358 | 0.383 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.369 | 0.358 | 0.383 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.086 | 0.075 | 0.095 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.086 | 0.075 | 0.095 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | prefix | - | - | basis_size | 39.000 | 39.000 | 39.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | prefix | - | - | positive_cells | 39.000 | 39.000 | 39.000 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | prefix | - | - | prefix_length | 362.000 | 361.000 | 362.375 | 10 | 10 |
| uniform | 20x20 | 400 | random | - | prefix | - | - | prefix_share | 0.905 | 0.902 | 0.906 | 10 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.966 | 0.958 | 0.973 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.814 | 0.789 | 0.831 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.882 | 0.877 | 0.886 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.777 | 0.771 | 0.785 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.530 | 0.523 | 0.541 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.098 | 0.085 | 0.115 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.285 | 0.276 | 0.293 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.365 | 0.318 | 0.396 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.082 | 0.077 | 0.087 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.608 | 0.603 | 0.611 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.344 | 0.329 | 0.388 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.416 | 0.404 | 0.425 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.428 | 0.416 | 0.437 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.344 | 0.329 | 0.388 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.416 | 0.404 | 0.425 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.428 | 0.416 | 0.437 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.470 | 0.447 | 0.515 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.534 | 0.525 | 0.543 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.545 | 0.533 | 0.555 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.470 | 0.447 | 0.515 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.534 | 0.525 | 0.543 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.545 | 0.533 | 0.555 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.859 | 0.851 | 0.871 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.881 | 0.875 | 0.884 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.884 | 0.880 | 0.889 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.859 | 0.851 | 0.871 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.881 | 0.875 | 0.884 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.884 | 0.880 | 0.889 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.219 | 0.203 | 0.260 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.284 | 0.277 | 0.294 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.295 | 0.287 | 0.306 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.219 | 0.203 | 0.260 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.284 | 0.277 | 0.294 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.295 | 0.287 | 0.306 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.631 | 0.617 | 0.665 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.686 | 0.679 | 0.694 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.692 | 0.687 | 0.702 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.631 | 0.617 | 0.665 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.686 | 0.679 | 0.694 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.692 | 0.687 | 0.702 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.047 | 0.053 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.991 | 0.994 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.994 | 0.993 | 0.995 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.994 | 0.994 | 0.995 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.857 | 0.832 | 0.883 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.883 | 0.861 | 0.897 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.888 | 0.873 | 0.906 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.195 | 0.204 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.206 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.195 | 0.204 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.972 | 0.970 | 0.975 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.977 | 0.974 | 0.978 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.978 | 0.976 | 0.979 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.860 | 0.850 | 0.874 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.881 | 0.871 | 0.891 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.886 | 0.878 | 0.896 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.859 | 0.851 | 0.873 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.880 | 0.876 | 0.885 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.887 | 0.882 | 0.891 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.859 | 0.851 | 0.873 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.880 | 0.876 | 0.885 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.887 | 0.882 | 0.891 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.076 | 0.073 | 0.080 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.076 | 0.073 | 0.080 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.076 | 0.073 | 0.079 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.991 | 0.990 | 0.993 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.991 | 0.990 | 0.993 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.864 | 0.842 | 0.884 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.888 | 0.869 | 0.899 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.885 | 0.870 | 0.901 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.653 | 0.647 | 0.664 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.653 | 0.645 | 0.667 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.657 | 0.651 | 0.666 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.911 | 0.905 | 0.917 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.924 | 0.921 | 0.927 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.926 | 0.923 | 0.929 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.833 | 0.822 | 0.846 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.858 | 0.853 | 0.863 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.862 | 0.855 | 0.868 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.249 | 4.231 | 4.266 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.256 | 4.230 | 4.269 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.252 | 4.230 | 4.266 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.537 | 0.524 | 0.569 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.596 | 0.589 | 0.607 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.604 | 0.598 | 0.613 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.536 | 0.523 | 0.569 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.596 | 0.588 | 0.606 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.603 | 0.597 | 0.612 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.632 | 0.619 | 0.665 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.684 | 0.678 | 0.692 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.694 | 0.687 | 0.700 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.632 | 0.619 | 0.665 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.684 | 0.678 | 0.692 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.694 | 0.687 | 0.700 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.404 | 0.383 | 0.446 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.472 | 0.464 | 0.481 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.481 | 0.472 | 0.492 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.404 | 0.383 | 0.446 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.472 | 0.464 | 0.481 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.481 | 0.472 | 0.492 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.105 | 0.091 | 0.136 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.152 | 0.145 | 0.158 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.155 | 0.168 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.105 | 0.091 | 0.136 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.152 | 0.145 | 0.158 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.155 | 0.168 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 59.000 | 59.000 | 59.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 58.000 | 57.000 | 58.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 785.000 | 761.000 | 804.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.872 | 0.846 | 0.893 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.985 | 0.982 | 0.987 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.862 | 0.845 | 0.879 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.888 | 0.867 | 0.897 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.783 | 0.762 | 0.797 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.545 | 0.524 | 0.573 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.123 | 0.082 | 0.160 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.294 | 0.259 | 0.329 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.408 | 0.345 | 0.466 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.091 | 0.070 | 0.105 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.604 | 0.588 | 0.623 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.385 | 0.362 | 0.413 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.427 | 0.392 | 0.455 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.434 | 0.397 | 0.455 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.385 | 0.362 | 0.413 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.427 | 0.392 | 0.455 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.434 | 0.397 | 0.455 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.510 | 0.481 | 0.545 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.542 | 0.517 | 0.573 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.552 | 0.524 | 0.580 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.510 | 0.481 | 0.545 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.542 | 0.517 | 0.573 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.552 | 0.524 | 0.580 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.874 | 0.853 | 0.895 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.895 | 0.874 | 0.909 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.888 | 0.874 | 0.902 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.874 | 0.853 | 0.895 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.895 | 0.874 | 0.909 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.888 | 0.874 | 0.902 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.259 | 0.217 | 0.287 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.301 | 0.278 | 0.322 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.297 | 0.266 | 0.330 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.259 | 0.217 | 0.287 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.301 | 0.278 | 0.322 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.297 | 0.266 | 0.330 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.668 | 0.643 | 0.692 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.685 | 0.657 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.699 | 0.678 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.668 | 0.643 | 0.692 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.685 | 0.657 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.699 | 0.678 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.042 | 0.035 | 0.063 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.993 | 0.993 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.894 | 0.833 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.894 | 0.833 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.905 | 0.814 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.206 | 0.175 | 0.224 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.175 | 0.217 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.182 | 0.217 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.979 | 0.965 | 0.986 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.979 | 0.972 | 0.986 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.979 | 0.965 | 0.986 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.893 | 0.837 | 0.933 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.894 | 0.853 | 0.940 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.893 | 0.847 | 0.929 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.867 | 0.846 | 0.888 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.888 | 0.872 | 0.902 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.881 | 0.867 | 0.909 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.867 | 0.846 | 0.888 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.888 | 0.872 | 0.902 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.881 | 0.867 | 0.909 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.077 | 0.063 | 0.093 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.077 | 0.056 | 0.091 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.070 | 0.056 | 0.086 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.986 | 0.986 | 0.993 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.862 | 0.800 | 0.917 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.900 | 0.830 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.900 | 0.846 | 1.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.661 | 0.622 | 0.706 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.650 | 0.615 | 0.692 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.664 | 0.635 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.923 | 0.902 | 0.930 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.923 | 0.909 | 0.944 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.852 | 0.822 | 0.876 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.865 | 0.836 | 0.896 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.857 | 0.831 | 0.886 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.266 | 4.145 | 4.344 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.231 | 4.154 | 4.330 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.217 | 4.152 | 4.323 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.580 | 0.559 | 0.601 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.612 | 0.593 | 0.636 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.612 | 0.587 | 0.643 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.580 | 0.559 | 0.601 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.609 | 0.591 | 0.636 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.611 | 0.587 | 0.641 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.675 | 0.642 | 0.699 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.692 | 0.664 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.703 | 0.671 | 0.727 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.675 | 0.642 | 0.699 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.692 | 0.664 | 0.720 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.703 | 0.671 | 0.727 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.455 | 0.420 | 0.477 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.490 | 0.462 | 0.519 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.490 | 0.462 | 0.524 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.455 | 0.420 | 0.477 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.490 | 0.462 | 0.519 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.490 | 0.462 | 0.524 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.133 | 0.112 | 0.161 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.164 | 0.140 | 0.189 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.147 | 0.191 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.133 | 0.112 | 0.161 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.164 | 0.140 | 0.189 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.147 | 0.191 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 59.000 | 59.000 | 59.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 58.000 | 57.000 | 58.000 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 793.000 | 763.750 | 827.250 | 100 | 10 |
| uniform | 30x30 | 900 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.881 | 0.849 | 0.919 | 100 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 1.000 | neutral_share | 0.841 | 0.835 | 0.850 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 2.000 | neutral_share | 0.696 | 0.692 | 0.701 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 5.000 | median_rel_change | 0.022 | 0.015 | 0.026 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 5.000 | neutral_share | 0.413 | 0.402 | 0.419 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 10.000 | median_rel_change | 0.101 | 0.093 | 0.104 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 10.000 | neutral_share | 0.176 | 0.167 | 0.184 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 20.000 | median_rel_change | 0.195 | 0.170 | 0.201 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | 20.000 | neutral_share | 0.033 | 0.030 | 0.035 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.603 | 0.598 | 0.611 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.292 | 0.279 | 0.303 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.292 | 0.279 | 0.303 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.414 | 0.412 | 0.424 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.414 | 0.412 | 0.424 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.847 | 0.838 | 0.856 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.847 | 0.838 | 0.856 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.175 | 0.170 | 0.183 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.175 | 0.170 | 0.183 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.597 | 0.594 | 0.607 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.597 | 0.594 | 0.607 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.048 | 0.053 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.992 | 0.992 | 0.994 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.847 | 0.829 | 0.867 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.195 | 0.191 | 0.209 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.967 | 0.964 | 0.968 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.833 | 0.829 | 0.844 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.841 | 0.835 | 0.847 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.841 | 0.835 | 0.847 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.079 | 0.073 | 0.085 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.986 | 0.984 | 0.992 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.829 | 0.806 | 0.881 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 0.661 | 0.652 | 0.671 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.900 | 0.890 | 0.904 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.813 | 0.803 | 0.819 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 4.257 | 4.237 | 4.292 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.496 | 0.489 | 0.500 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.496 | 0.488 | 0.499 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.581 | 0.574 | 0.598 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.581 | 0.574 | 0.598 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 6.000 | 6.000 | 6.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.359 | 0.353 | 0.368 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.359 | 0.353 | 0.368 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 15.000 | 15.000 | 15.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.076 | 0.073 | 0.079 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.076 | 0.073 | 0.079 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | prefix | - | - | basis_size | 59.000 | 59.000 | 59.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | prefix | - | - | positive_cells | 59.000 | 58.250 | 59.000 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | prefix | - | - | prefix_length | 818.750 | 818.000 | 820.625 | 10 | 10 |
| uniform | 30x30 | 900 | random | - | prefix | - | - | prefix_share | 0.910 | 0.909 | 0.912 | 10 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.909 | 0.898 | 0.928 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.928 | 0.926 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.862 | 0.857 | 0.867 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.690 | 0.683 | 0.696 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.006 | 0.004 | 0.010 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.476 | 0.467 | 0.487 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.188 | 0.174 | 0.206 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.227 | 0.219 | 0.232 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.531 | 0.524 | 0.536 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.559 | 0.509 | 0.585 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.595 | 0.587 | 0.603 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.598 | 0.589 | 0.605 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.559 | 0.509 | 0.585 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.595 | 0.587 | 0.603 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.598 | 0.589 | 0.605 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.514 | 0.469 | 0.541 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.554 | 0.548 | 0.560 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.556 | 0.548 | 0.564 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.514 | 0.469 | 0.541 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.554 | 0.548 | 0.560 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.556 | 0.548 | 0.564 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.917 | 0.909 | 0.926 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.928 | 0.924 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.930 | 0.926 | 0.933 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.917 | 0.909 | 0.926 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.928 | 0.924 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.930 | 0.926 | 0.933 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.438 | 0.384 | 0.461 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.477 | 0.467 | 0.486 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.480 | 0.471 | 0.489 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.438 | 0.384 | 0.461 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.477 | 0.467 | 0.486 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.480 | 0.471 | 0.489 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.777 | 0.753 | 0.793 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.799 | 0.795 | 0.807 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.802 | 0.796 | 0.807 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.777 | 0.753 | 0.793 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.799 | 0.795 | 0.807 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.802 | 0.796 | 0.807 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.046 | 0.053 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.054 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.048 | 0.053 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.995 | 0.997 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.996 | 0.997 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.996 | 0.997 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.923 | 0.907 | 0.936 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.926 | 0.911 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.927 | 0.918 | 0.943 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.193 | 0.204 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.201 | 0.195 | 0.205 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.201 | 0.196 | 0.206 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.984 | 0.981 | 0.986 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.984 | 0.987 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.984 | 0.987 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.918 | 0.909 | 0.928 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.929 | 0.921 | 0.934 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.927 | 0.920 | 0.935 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.917 | 0.911 | 0.927 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.927 | 0.925 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.929 | 0.926 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.917 | 0.911 | 0.927 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.927 | 0.925 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.929 | 0.926 | 0.932 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.397 | 0.388 | 0.405 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.395 | 0.389 | 0.405 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.396 | 0.389 | 0.403 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.968 | 0.965 | 0.972 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.971 | 0.969 | 0.974 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.971 | 0.970 | 0.974 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.910 | 0.902 | 0.922 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.921 | 0.914 | 0.926 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.920 | 0.915 | 0.926 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.249 | 2.234 | 2.263 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.250 | 2.238 | 2.268 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.255 | 2.237 | 2.269 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.835 | 0.812 | 0.845 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.848 | 0.843 | 0.854 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.851 | 0.847 | 0.856 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.829 | 0.804 | 0.839 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.841 | 0.837 | 0.847 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.845 | 0.840 | 0.849 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.250 | 12.220 | 12.282 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.263 | 12.219 | 12.293 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.244 | 12.220 | 12.281 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.371 | 0.319 | 0.396 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.410 | 0.401 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.413 | 0.403 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.371 | 0.319 | 0.396 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.410 | 0.401 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.413 | 0.403 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.662 | 0.619 | 0.680 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.691 | 0.685 | 0.697 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.691 | 0.687 | 0.700 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.662 | 0.619 | 0.680 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.691 | 0.685 | 0.697 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.691 | 0.687 | 0.700 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.445 | 0.386 | 0.462 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.475 | 0.466 | 0.487 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.479 | 0.470 | 0.487 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.445 | 0.386 | 0.462 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.475 | 0.466 | 0.487 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.479 | 0.470 | 0.487 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.128 | 0.093 | 0.146 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.158 | 0.151 | 0.162 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.151 | 0.166 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.128 | 0.093 | 0.146 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.158 | 0.151 | 0.162 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.151 | 0.166 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 97.000 | 95.000 | 98.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 2149.000 | 2087.875 | 2188.500 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.860 | 0.835 | 0.875 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.907 | 0.897 | 0.918 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.864 | 0.846 | 0.881 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.685 | 0.664 | 0.713 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0.004 | 0 | 0.014 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.483 | 0.455 | 0.517 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.189 | 0.167 | 0.217 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.224 | 0.203 | 0.252 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.528 | 0.514 | 0.543 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.573 | 0.544 | 0.608 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.594 | 0.566 | 0.622 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.598 | 0.573 | 0.622 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.573 | 0.544 | 0.608 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.594 | 0.566 | 0.622 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.598 | 0.573 | 0.622 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.528 | 0.503 | 0.559 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.545 | 0.517 | 0.573 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.559 | 0.524 | 0.587 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.528 | 0.503 | 0.559 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.545 | 0.517 | 0.573 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.559 | 0.524 | 0.587 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.934 | 0.916 | 0.951 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.934 | 0.916 | 0.951 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.455 | 0.425 | 0.497 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.483 | 0.455 | 0.517 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.476 | 0.453 | 0.503 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.455 | 0.425 | 0.497 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.483 | 0.455 | 0.517 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.476 | 0.453 | 0.503 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.783 | 0.769 | 0.797 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.797 | 0.776 | 0.818 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.797 | 0.783 | 0.818 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.783 | 0.769 | 0.797 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.797 | 0.776 | 0.818 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.797 | 0.783 | 0.818 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.056 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.040 | 0.063 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.857 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.875 | 1.000 | 99 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.900 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.182 | 0.217 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.175 | 0.217 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.182 | 0.217 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.931 | 0.885 | 0.962 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.931 | 0.894 | 0.963 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.932 | 0.893 | 0.966 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.937 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.937 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.930 | 0.909 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.399 | 0.364 | 0.427 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.399 | 0.364 | 0.434 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.392 | 0.357 | 0.428 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.958 | 0.979 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.965 | 0.986 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.965 | 0.979 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.920 | 0.890 | 0.946 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.929 | 0.898 | 0.959 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.925 | 0.904 | 0.944 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.259 | 2.187 | 2.302 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.269 | 2.189 | 2.329 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.259 | 2.189 | 2.329 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.846 | 0.825 | 0.867 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.846 | 0.830 | 0.874 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.853 | 0.832 | 0.867 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.841 | 0.817 | 0.861 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.842 | 0.825 | 0.866 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.844 | 0.826 | 0.861 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.308 | 12.124 | 12.427 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.262 | 12.107 | 12.378 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.227 | 12.096 | 12.371 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.392 | 0.364 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.413 | 0.378 | 0.442 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.413 | 0.392 | 0.441 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.392 | 0.364 | 0.420 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.413 | 0.378 | 0.442 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.413 | 0.392 | 0.441 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.678 | 0.650 | 0.706 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.699 | 0.671 | 0.713 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.696 | 0.671 | 0.720 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.678 | 0.650 | 0.706 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.699 | 0.671 | 0.713 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.696 | 0.671 | 0.720 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.455 | 0.434 | 0.490 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.483 | 0.460 | 0.510 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.479 | 0.448 | 0.503 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.455 | 0.434 | 0.490 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.483 | 0.460 | 0.510 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.479 | 0.448 | 0.503 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.140 | 0.119 | 0.168 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.140 | 0.189 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.161 | 0.140 | 0.189 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.140 | 0.119 | 0.168 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.140 | 0.189 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.161 | 0.140 | 0.189 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 97.000 | 95.000 | 97.000 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 2189.500 | 2116.250 | 2286.750 | 100 | 10 |
| uniform | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.876 | 0.847 | 0.915 | 100 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 1.000 | neutral_share | 0.893 | 0.886 | 0.897 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 2.000 | neutral_share | 0.804 | 0.794 | 0.816 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 5.000 | neutral_share | 0.589 | 0.561 | 0.596 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 10.000 | median_rel_change | 0.041 | 0.039 | 0.045 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 10.000 | neutral_share | 0.326 | 0.323 | 0.330 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 20.000 | median_rel_change | 0.124 | 0.113 | 0.133 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | 20.000 | neutral_share | 0.110 | 0.102 | 0.117 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.574 | 0.566 | 0.580 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.462 | 0.453 | 0.474 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.462 | 0.453 | 0.474 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.407 | 0.398 | 0.418 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.407 | 0.398 | 0.418 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.891 | 0.889 | 0.903 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.891 | 0.889 | 0.903 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.324 | 0.310 | 0.332 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.324 | 0.310 | 0.332 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.716 | 0.709 | 0.722 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.716 | 0.709 | 0.722 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.054 | 0.049 | 0.060 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.994 | 0.997 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.923 | 0.894 | 0.937 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.209 | 0.203 | 0.221 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.978 | 0.977 | 0.980 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.895 | 0.891 | 0.900 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.895 | 0.890 | 0.899 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.895 | 0.890 | 0.899 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.398 | 0.378 | 0.403 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.958 | 0.955 | 0.962 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.880 | 0.873 | 0.892 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.242 | 2.223 | 2.257 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.786 | 0.784 | 0.798 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.778 | 0.775 | 0.790 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.246 | 12.160 | 12.303 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.268 | 0.253 | 0.272 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.268 | 0.253 | 0.272 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.573 | 0.567 | 0.583 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.573 | 0.567 | 0.583 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.326 | 0.317 | 0.335 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.326 | 0.317 | 0.335 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.064 | 0.057 | 0.069 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.064 | 0.057 | 0.069 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | prefix | - | - | positive_cells | 98.000 | 98.000 | 98.000 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | prefix | - | - | prefix_length | 2278.750 | 2270.000 | 2283.500 | 10 | 10 |
| uniform | 50x50 | 2500 | random | - | prefix | - | - | prefix_share | 0.911 | 0.908 | 0.913 | 10 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.998 | 0.997 | 0.998 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.960 | 0.953 | 0.969 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.964 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.928 | 0.925 | 0.931 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.829 | 0.824 | 0.835 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.687 | 0.682 | 0.694 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.011 | 0.008 | 0.015 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.470 | 0.466 | 0.477 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.416 | 0.413 | 0.420 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.766 | 0.759 | 0.774 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.769 | 0.763 | 0.776 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.769 | 0.764 | 0.774 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.766 | 0.759 | 0.774 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.769 | 0.763 | 0.776 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.769 | 0.764 | 0.774 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.519 | 0.514 | 0.529 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.529 | 0.522 | 0.535 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.528 | 0.522 | 0.536 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.519 | 0.514 | 0.529 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.529 | 0.522 | 0.535 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.528 | 0.522 | 0.536 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.963 | 0.960 | 0.965 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.963 | 0.960 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.963 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.963 | 0.960 | 0.965 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.963 | 0.960 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.963 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.681 | 0.675 | 0.690 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.686 | 0.681 | 0.691 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.687 | 0.679 | 0.693 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.681 | 0.675 | 0.690 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.686 | 0.681 | 0.691 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.687 | 0.679 | 0.693 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.893 | 0.887 | 0.896 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.892 | 0.888 | 0.897 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.894 | 0.890 | 0.899 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.893 | 0.887 | 0.896 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.892 | 0.888 | 0.897 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.894 | 0.890 | 0.899 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.046 | 0.053 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.047 | 0.053 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.047 | 0.053 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.998 | 0.998 | 0.999 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.998 | 0.997 | 0.999 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.999 | 0.998 | 0.999 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.966 | 0.953 | 0.976 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.962 | 0.950 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.967 | 0.956 | 0.977 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.201 | 0.195 | 0.206 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.198 | 0.195 | 0.203 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.201 | 0.197 | 0.206 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.992 | 0.991 | 0.994 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.993 | 0.991 | 0.994 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.992 | 0.991 | 0.993 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.962 | 0.956 | 0.968 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.961 | 0.957 | 0.968 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.962 | 0.955 | 0.967 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.963 | 0.960 | 0.965 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.963 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.964 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.963 | 0.960 | 0.965 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.963 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.964 | 0.961 | 0.966 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.250 | 2.240 | 2.264 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.248 | 2.232 | 2.263 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.247 | 2.230 | 2.263 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.919 | 0.916 | 0.922 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.920 | 0.916 | 0.924 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.919 | 0.916 | 0.924 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.915 | 0.912 | 0.919 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.917 | 0.913 | 0.921 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.916 | 0.913 | 0.920 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.745 | 9.719 | 9.773 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.762 | 9.733 | 9.788 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.743 | 9.717 | 9.772 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.692 | 0.686 | 0.699 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.696 | 0.688 | 0.703 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.696 | 0.690 | 0.701 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.692 | 0.686 | 0.699 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.696 | 0.688 | 0.703 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.696 | 0.690 | 0.701 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.750 | 49.671 | 49.812 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.755 | 49.693 | 49.821 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.764 | 49.685 | 49.833 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.153 | 0.147 | 0.160 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.159 | 0.152 | 0.164 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.157 | 0.152 | 0.162 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.153 | 0.147 | 0.160 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.159 | 0.152 | 0.164 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.157 | 0.152 | 0.162 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.682 | 0.676 | 0.691 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.688 | 0.681 | 0.694 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.686 | 0.681 | 0.694 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.682 | 0.676 | 0.691 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.688 | 0.681 | 0.694 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.686 | 0.681 | 0.694 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.466 | 0.460 | 0.474 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.471 | 0.463 | 0.478 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.473 | 0.462 | 0.479 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.466 | 0.460 | 0.474 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.471 | 0.463 | 0.478 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.473 | 0.462 | 0.479 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.148 | 0.144 | 0.155 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.153 | 0.148 | 0.159 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.154 | 0.150 | 0.159 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.148 | 0.144 | 0.155 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.153 | 0.148 | 0.159 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.154 | 0.150 | 0.159 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 199.000 | 199.000 | 199.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 194.000 | 193.000 | 196.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 8689.000 | 8450.000 | 8803.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.869 | 0.845 | 0.880 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.994 | 0.993 | 0.995 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.948 | 0.938 | 0.953 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.832 | 0.811 | 0.860 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.699 | 0.671 | 0.727 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.005 | 0 | 0.018 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.483 | 0.446 | 0.510 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.409 | 0.389 | 0.429 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.769 | 0.741 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.755 | 0.734 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.762 | 0.734 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.769 | 0.741 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.755 | 0.734 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.762 | 0.734 | 0.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.517 | 0.483 | 0.540 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.531 | 0.497 | 0.561 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.524 | 0.497 | 0.559 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.517 | 0.483 | 0.540 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.531 | 0.497 | 0.561 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.524 | 0.497 | 0.559 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.965 | 0.951 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.965 | 0.944 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.965 | 0.951 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.965 | 0.944 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.671 | 0.650 | 0.699 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.692 | 0.664 | 0.706 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.685 | 0.664 | 0.713 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.671 | 0.650 | 0.699 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.692 | 0.664 | 0.706 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.685 | 0.664 | 0.713 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.895 | 0.874 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.902 | 0.881 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.902 | 0.881 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.895 | 0.874 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.902 | 0.881 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.902 | 0.881 | 0.916 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.056 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.042 | 0.035 | 0.063 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.915 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.168 | 0.217 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.175 | 0.224 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.182 | 0.226 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.993 | 0.986 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.969 | 0.948 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.968 | 0.942 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.966 | 0.935 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.958 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.965 | 0.951 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.958 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.965 | 0.951 | 0.972 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.965 | 0.951 | 0.979 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.255 | 2.210 | 2.315 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.234 | 2.175 | 2.302 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.259 | 2.189 | 2.315 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.916 | 0.902 | 0.932 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.916 | 0.909 | 0.937 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.923 | 0.909 | 0.937 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.914 | 0.896 | 0.930 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.914 | 0.904 | 0.935 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.919 | 0.904 | 0.935 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.717 | 9.600 | 9.841 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.762 | 9.621 | 9.897 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.696 | 9.607 | 9.790 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.692 | 0.671 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.699 | 0.671 | 0.727 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.699 | 0.671 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.692 | 0.671 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.699 | 0.671 | 0.727 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.699 | 0.671 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.664 | 49.439 | 49.941 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.815 | 49.509 | 50.023 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.808 | 49.497 | 50.003 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.147 | 0.126 | 0.168 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.154 | 0.140 | 0.177 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.154 | 0.126 | 0.175 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.147 | 0.126 | 0.168 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.154 | 0.140 | 0.177 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.154 | 0.126 | 0.175 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.682 | 0.664 | 0.701 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.685 | 0.664 | 0.706 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.692 | 0.664 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.682 | 0.664 | 0.701 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.685 | 0.664 | 0.706 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.692 | 0.664 | 0.720 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.455 | 0.427 | 0.490 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.462 | 0.434 | 0.490 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.476 | 0.441 | 0.505 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.455 | 0.427 | 0.490 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.462 | 0.434 | 0.490 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.476 | 0.441 | 0.505 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.147 | 0.126 | 0.161 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.157 | 0.133 | 0.170 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.154 | 0.133 | 0.175 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.147 | 0.126 | 0.161 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.157 | 0.133 | 0.170 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.154 | 0.133 | 0.175 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 199.000 | 199.000 | 199.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 193.500 | 192.000 | 195.000 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 8908.500 | 8635.500 | 9154.250 | 100 | 10 |
| uniform | 100x100 | 10000 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.891 | 0.864 | 0.915 | 100 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 1.000 | neutral_share | 0.943 | 0.936 | 0.945 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 2.000 | neutral_share | 0.883 | 0.879 | 0.890 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 5.000 | neutral_share | 0.747 | 0.731 | 0.750 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 10.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 10.000 | neutral_share | 0.548 | 0.532 | 0.552 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 20.000 | median_rel_change | 0.044 | 0.041 | 0.045 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | 20.000 | neutral_share | 0.303 | 0.295 | 0.310 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.488 | 0.481 | 0.494 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.661 | 0.655 | 0.665 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.661 | 0.655 | 0.665 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 17.000 | 17.000 | 17.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.362 | 0.349 | 0.373 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.362 | 0.349 | 0.373 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.942 | 0.939 | 0.950 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.942 | 0.939 | 0.950 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.542 | 0.533 | 0.558 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.542 | 0.533 | 0.558 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.841 | 0.835 | 0.843 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.841 | 0.835 | 0.843 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.046 | 0.053 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.996 | 0.998 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.936 | 0.914 | 0.958 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.193 | 0.205 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.987 | 0.985 | 0.991 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.936 | 0.924 | 0.954 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.942 | 0.935 | 0.946 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.942 | 0.935 | 0.946 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 2.237 | 2.215 | 2.255 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.871 | 0.867 | 0.881 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.865 | 0.860 | 0.876 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 9.718 | 9.665 | 9.771 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.563 | 0.559 | 0.568 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.563 | 0.559 | 0.568 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 49.748 | 49.589 | 49.862 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.059 | 0.050 | 0.063 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.059 | 0.050 | 0.063 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.552 | 0.549 | 0.562 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.552 | 0.549 | 0.562 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 20.000 | 20.000 | 20.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.297 | 0.294 | 0.305 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.297 | 0.294 | 0.305 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 50.000 | 50.000 | 50.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.052 | 0.051 | 0.055 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.052 | 0.051 | 0.055 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | prefix | - | - | basis_size | 199.000 | 199.000 | 199.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | prefix | - | - | positive_cells | 197.000 | 197.000 | 197.000 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | prefix | - | - | prefix_length | 9116.500 | 9093.000 | 9132.625 | 10 | 10 |
| uniform | 100x100 | 10000 | random | - | prefix | - | - | prefix_share | 0.912 | 0.909 | 0.913 | 10 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.987 | 0.982 | 0.990 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.898 | 0.886 | 0.909 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.927 | 0.923 | 0.931 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.860 | 0.854 | 0.864 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.686 | 0.678 | 0.693 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 7.405e-04 | 4.937e-04 | 0.001 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.471 | 0.462 | 0.478 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.029 | 0.022 | 0.036 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.222 | 0.214 | 0.231 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.532 | 0.528 | 0.536 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.472 | 0.412 | 0.508 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.589 | 0.583 | 0.597 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.597 | 0.590 | 0.603 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.472 | 0.412 | 0.508 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.589 | 0.583 | 0.597 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.597 | 0.590 | 0.603 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.421 | 0.363 | 0.461 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.546 | 0.538 | 0.556 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.552 | 0.546 | 0.561 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.421 | 0.363 | 0.461 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.546 | 0.538 | 0.556 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.552 | 0.546 | 0.561 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.897 | 0.882 | 0.908 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.928 | 0.924 | 0.932 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.929 | 0.926 | 0.933 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.897 | 0.882 | 0.908 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.928 | 0.924 | 0.932 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.929 | 0.926 | 0.933 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.339 | 0.277 | 0.386 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.469 | 0.463 | 0.483 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.477 | 0.468 | 0.487 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.339 | 0.277 | 0.386 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.469 | 0.463 | 0.483 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.477 | 0.468 | 0.487 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.726 | 0.680 | 0.746 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.798 | 0.791 | 0.804 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.800 | 0.796 | 0.808 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.726 | 0.680 | 0.746 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.798 | 0.791 | 0.804 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.800 | 0.796 | 0.808 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.048 | 0.052 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.047 | 0.052 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.995 | 0.994 | 0.996 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.996 | 0.997 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.997 | 0.996 | 0.997 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.902 | 0.880 | 0.920 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.926 | 0.911 | 0.941 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.930 | 0.914 | 0.945 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.194 | 0.205 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.205 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.194 | 0.204 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.979 | 0.977 | 0.982 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.985 | 0.984 | 0.987 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.984 | 0.987 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.896 | 0.884 | 0.911 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.927 | 0.919 | 0.934 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.930 | 0.921 | 0.935 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.897 | 0.885 | 0.908 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.926 | 0.923 | 0.930 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.929 | 0.926 | 0.932 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.897 | 0.885 | 0.908 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.926 | 0.923 | 0.930 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.929 | 0.926 | 0.932 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.396 | 0.387 | 0.403 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.395 | 0.389 | 0.404 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.397 | 0.390 | 0.402 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.960 | 0.954 | 0.964 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.971 | 0.969 | 0.974 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.970 | 0.974 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.888 | 0.872 | 0.901 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.919 | 0.913 | 0.926 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.922 | 0.915 | 0.927 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.247 | 2.238 | 2.264 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.249 | 2.231 | 2.259 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.247 | 2.233 | 2.264 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.792 | 0.756 | 0.812 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.848 | 0.843 | 0.852 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.850 | 0.845 | 0.855 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.784 | 0.746 | 0.804 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.841 | 0.837 | 0.846 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.844 | 0.838 | 0.849 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.252 | 12.217 | 12.272 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.255 | 12.217 | 12.285 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.257 | 12.213 | 12.283 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.280 | 0.217 | 0.309 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.403 | 0.396 | 0.410 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.411 | 0.403 | 0.423 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.280 | 0.217 | 0.309 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.403 | 0.396 | 0.410 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.411 | 0.403 | 0.423 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.583 | 0.538 | 0.616 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.685 | 0.677 | 0.694 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.689 | 0.681 | 0.698 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.583 | 0.538 | 0.616 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.685 | 0.677 | 0.694 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.689 | 0.681 | 0.698 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.339 | 0.281 | 0.379 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.472 | 0.463 | 0.480 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.476 | 0.470 | 0.486 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.339 | 0.281 | 0.379 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.472 | 0.463 | 0.480 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.476 | 0.470 | 0.486 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.068 | 0.041 | 0.090 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.151 | 0.145 | 0.160 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.159 | 0.152 | 0.165 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.068 | 0.041 | 0.090 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.151 | 0.145 | 0.160 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.159 | 0.152 | 0.165 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 96.000 | 96.000 | 97.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 2156.500 | 2083.375 | 2206.500 | 100 | 10 |
| structured | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.863 | 0.833 | 0.883 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.907 | 0.889 | 0.918 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.860 | 0.839 | 0.874 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.682 | 0.657 | 0.706 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 8.692e-04 | 0 | 0.002 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.469 | 0.441 | 0.503 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.031 | 0.022 | 0.038 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.231 | 0.203 | 0.247 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.531 | 0.515 | 0.548 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.573 | 0.552 | 0.601 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.594 | 0.573 | 0.629 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.608 | 0.580 | 0.636 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.573 | 0.552 | 0.601 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.594 | 0.573 | 0.629 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.608 | 0.580 | 0.636 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.524 | 0.495 | 0.559 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.545 | 0.510 | 0.566 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.549 | 0.516 | 0.573 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.524 | 0.495 | 0.559 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.545 | 0.510 | 0.566 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.549 | 0.516 | 0.573 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.923 | 0.909 | 0.937 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.930 | 0.916 | 0.939 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.923 | 0.909 | 0.937 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.930 | 0.916 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.930 | 0.916 | 0.939 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.441 | 0.418 | 0.476 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.483 | 0.448 | 0.517 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.483 | 0.441 | 0.517 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.441 | 0.418 | 0.476 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.483 | 0.448 | 0.517 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.483 | 0.441 | 0.517 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.783 | 0.755 | 0.804 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.808 | 0.781 | 0.832 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.790 | 0.767 | 0.813 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.783 | 0.755 | 0.804 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.808 | 0.781 | 0.832 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.790 | 0.767 | 0.813 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.052 | 0.042 | 0.063 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.875 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.889 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.851 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.187 | 0.224 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.168 | 0.217 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.173 | 0.217 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.926 | 0.897 | 0.953 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.931 | 0.896 | 0.960 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.932 | 0.902 | 0.962 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.923 | 0.909 | 0.937 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.930 | 0.916 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.927 | 0.914 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.923 | 0.909 | 0.937 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.930 | 0.916 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.927 | 0.914 | 0.944 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.399 | 0.364 | 0.428 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.392 | 0.350 | 0.420 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.399 | 0.371 | 0.434 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.965 | 0.958 | 0.979 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.965 | 0.979 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.965 | 0.979 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.905 | 0.873 | 0.941 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.922 | 0.895 | 0.942 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.930 | 0.904 | 0.947 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.248 | 2.187 | 2.322 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.255 | 2.196 | 2.308 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.252 | 2.189 | 2.322 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.839 | 0.818 | 0.867 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.846 | 0.832 | 0.867 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.846 | 0.823 | 0.860 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.833 | 0.806 | 0.861 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.841 | 0.824 | 0.859 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.840 | 0.814 | 0.855 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.245 | 12.133 | 12.406 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.245 | 12.112 | 12.376 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.245 | 12.119 | 12.420 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.385 | 0.357 | 0.413 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.413 | 0.390 | 0.441 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.413 | 0.385 | 0.441 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.385 | 0.357 | 0.413 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.413 | 0.390 | 0.441 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.413 | 0.385 | 0.441 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.678 | 0.650 | 0.706 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.685 | 0.664 | 0.720 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.685 | 0.670 | 0.706 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.678 | 0.650 | 0.706 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.685 | 0.664 | 0.720 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.685 | 0.670 | 0.706 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.451 | 0.434 | 0.476 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.469 | 0.448 | 0.503 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.469 | 0.441 | 0.498 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.451 | 0.434 | 0.476 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.469 | 0.448 | 0.503 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.469 | 0.441 | 0.498 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.140 | 0.119 | 0.154 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.147 | 0.133 | 0.175 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.154 | 0.131 | 0.175 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.140 | 0.119 | 0.154 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.147 | 0.133 | 0.175 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.154 | 0.131 | 0.175 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 97.000 | 96.000 | 98.000 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 2157.000 | 2075.250 | 2238.250 | 100 | 10 |
| structured | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.863 | 0.830 | 0.895 | 100 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 1.000 | neutral_share | 0.896 | 0.889 | 0.902 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 2.000 | neutral_share | 0.803 | 0.792 | 0.806 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 5.000 | neutral_share | 0.577 | 0.572 | 0.583 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 10.000 | median_rel_change | 0.007 | 0.006 | 0.007 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 10.000 | neutral_share | 0.330 | 0.316 | 0.338 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 20.000 | median_rel_change | 0.021 | 0.018 | 0.023 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | 20.000 | neutral_share | 0.111 | 0.106 | 0.119 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.573 | 0.567 | 0.579 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.459 | 0.446 | 0.468 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.459 | 0.446 | 0.468 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.404 | 0.395 | 0.417 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.404 | 0.395 | 0.417 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.889 | 0.885 | 0.899 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.889 | 0.885 | 0.899 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.324 | 0.306 | 0.340 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.324 | 0.306 | 0.340 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.718 | 0.703 | 0.730 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.718 | 0.703 | 0.730 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.048 | 0.053 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.994 | 0.997 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.911 | 0.882 | 0.934 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.182 | 0.207 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.978 | 0.974 | 0.980 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.886 | 0.878 | 0.893 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.895 | 0.889 | 0.904 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.895 | 0.889 | 0.904 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.406 | 0.392 | 0.409 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.958 | 0.955 | 0.959 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.881 | 0.877 | 0.884 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.248 | 2.212 | 2.289 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.786 | 0.782 | 0.790 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.779 | 0.770 | 0.782 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.224 | 12.215 | 12.253 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.265 | 0.257 | 0.276 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.265 | 0.257 | 0.276 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.577 | 0.563 | 0.590 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.577 | 0.563 | 0.590 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.324 | 0.313 | 0.332 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.324 | 0.313 | 0.332 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.058 | 0.053 | 0.062 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.058 | 0.053 | 0.062 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | prefix | - | - | positive_cells | 98.000 | 98.000 | 98.000 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | prefix | - | - | prefix_length | 2279.000 | 2272.750 | 2282.375 | 10 | 10 |
| structured | 50x50 | 2500 | random | - | prefix | - | - | prefix_share | 0.912 | 0.909 | 0.913 | 10 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.993 | 0.991 | 0.994 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.919 | 0.909 | 0.939 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.931 | 0.927 | 0.935 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.867 | 0.859 | 0.874 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.701 | 0.692 | 0.710 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 3.154e-04 | 0 | 0.001 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.493 | 0.481 | 0.506 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.031 | 0.017 | 0.042 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.240 | 0.230 | 0.252 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.522 | 0.516 | 0.527 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.496 | 0.483 | 0.508 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.610 | 0.599 | 0.619 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.619 | 0.601 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.496 | 0.483 | 0.508 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.610 | 0.599 | 0.619 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.619 | 0.601 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.449 | 0.435 | 0.462 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.566 | 0.557 | 0.577 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.576 | 0.562 | 0.592 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.449 | 0.435 | 0.462 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.566 | 0.557 | 0.577 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.576 | 0.562 | 0.592 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.905 | 0.902 | 0.909 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.932 | 0.929 | 0.935 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.934 | 0.930 | 0.937 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.905 | 0.902 | 0.909 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.932 | 0.929 | 0.935 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.934 | 0.930 | 0.937 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.365 | 0.353 | 0.380 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.493 | 0.479 | 0.505 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.501 | 0.486 | 0.517 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.365 | 0.353 | 0.380 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.493 | 0.479 | 0.505 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.501 | 0.486 | 0.517 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.739 | 0.729 | 0.746 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.809 | 0.801 | 0.817 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.815 | 0.806 | 0.822 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.739 | 0.729 | 0.746 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.809 | 0.801 | 0.817 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.815 | 0.806 | 0.822 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.047 | 0.051 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.048 | 0.053 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.051 | 0.048 | 0.053 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.995 | 0.994 | 0.996 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.997 | 0.996 | 0.997 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.997 | 0.996 | 0.997 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.904 | 0.889 | 0.922 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.934 | 0.919 | 0.948 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.934 | 0.924 | 0.945 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.196 | 0.204 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.194 | 0.205 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.193 | 0.204 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.981 | 0.979 | 0.983 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.985 | 0.988 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.987 | 0.985 | 0.989 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.905 | 0.893 | 0.914 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.931 | 0.925 | 0.938 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.936 | 0.926 | 0.943 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.906 | 0.899 | 0.909 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.931 | 0.927 | 0.935 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.933 | 0.929 | 0.939 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.906 | 0.899 | 0.909 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.931 | 0.927 | 0.935 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.933 | 0.929 | 0.939 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.395 | 0.387 | 0.405 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.393 | 0.387 | 0.403 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.394 | 0.389 | 0.400 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.963 | 0.961 | 0.965 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.974 | 0.971 | 0.976 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.974 | 0.972 | 0.976 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.896 | 0.889 | 0.902 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.925 | 0.918 | 0.931 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.926 | 0.921 | 0.934 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.254 | 2.236 | 2.263 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.251 | 2.236 | 2.269 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.251 | 2.236 | 2.265 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.803 | 0.795 | 0.811 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.856 | 0.849 | 0.862 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.858 | 0.852 | 0.865 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.795 | 0.787 | 0.804 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.850 | 0.843 | 0.856 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.852 | 0.846 | 0.860 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.252 | 12.215 | 12.287 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.248 | 12.210 | 12.278 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.249 | 12.214 | 12.277 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.302 | 0.292 | 0.312 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.422 | 0.411 | 0.439 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.435 | 0.418 | 0.453 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.302 | 0.292 | 0.312 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.422 | 0.411 | 0.439 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.435 | 0.418 | 0.453 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.604 | 0.594 | 0.615 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.700 | 0.690 | 0.711 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.708 | 0.696 | 0.719 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.604 | 0.594 | 0.615 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.700 | 0.690 | 0.711 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.708 | 0.696 | 0.719 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.366 | 0.356 | 0.379 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.493 | 0.478 | 0.501 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.501 | 0.486 | 0.518 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.366 | 0.356 | 0.379 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.493 | 0.478 | 0.501 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.501 | 0.486 | 0.518 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.083 | 0.076 | 0.090 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.169 | 0.159 | 0.182 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.178 | 0.165 | 0.194 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.083 | 0.076 | 0.090 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.169 | 0.159 | 0.182 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.178 | 0.165 | 0.194 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 98.000 | 97.000 | 98.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 2362.750 | 2289.625 | 2386.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.945 | 0.916 | 0.954 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.995 | 0.993 | 0.996 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.927 | 0.908 | 0.938 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.930 | 0.923 | 0.951 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.874 | 0.853 | 0.890 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.713 | 0.685 | 0.734 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0 | 0 | 0.001 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.517 | 0.490 | 0.538 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.025 | 0.017 | 0.043 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.262 | 0.231 | 0.288 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.511 | 0.493 | 0.530 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.601 | 0.573 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.636 | 0.594 | 0.664 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.622 | 0.600 | 0.664 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.601 | 0.573 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.636 | 0.594 | 0.664 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.622 | 0.600 | 0.664 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.580 | 0.538 | 0.608 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.577 | 0.545 | 0.622 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.594 | 0.559 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.580 | 0.538 | 0.608 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.577 | 0.545 | 0.622 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.594 | 0.559 | 0.629 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.937 | 0.921 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.937 | 0.930 | 0.951 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.937 | 0.923 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.937 | 0.921 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.937 | 0.930 | 0.951 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.937 | 0.923 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.497 | 0.455 | 0.531 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.517 | 0.488 | 0.545 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.503 | 0.469 | 0.540 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.497 | 0.455 | 0.531 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.517 | 0.488 | 0.545 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.503 | 0.469 | 0.540 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.818 | 0.783 | 0.832 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.818 | 0.797 | 0.839 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.818 | 0.797 | 0.846 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.818 | 0.783 | 0.832 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.818 | 0.797 | 0.839 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.818 | 0.797 | 0.846 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.042 | 0.063 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.052 | 0.042 | 0.063 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.857 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.875 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.889 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.192 | 0.175 | 0.217 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.173 | 0.217 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.189 | 0.175 | 0.217 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.993 | 0.986 | 0.993 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.938 | 0.908 | 0.966 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.949 | 0.913 | 0.966 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.943 | 0.904 | 0.963 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.930 | 0.909 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.937 | 0.923 | 0.951 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.944 | 0.923 | 0.953 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.930 | 0.909 | 0.944 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.937 | 0.923 | 0.951 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.944 | 0.923 | 0.953 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.385 | 0.364 | 0.421 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.378 | 0.355 | 0.413 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.388 | 0.357 | 0.420 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.976 | 0.965 | 0.986 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.979 | 0.965 | 0.986 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.979 | 0.965 | 0.986 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.929 | 0.901 | 0.959 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.935 | 0.907 | 0.958 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.936 | 0.905 | 0.957 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.252 | 2.192 | 2.308 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.238 | 2.182 | 2.315 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.266 | 2.203 | 2.329 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.860 | 0.832 | 0.881 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.867 | 0.853 | 0.888 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.867 | 0.853 | 0.883 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.853 | 0.823 | 0.875 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.863 | 0.846 | 0.883 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.864 | 0.845 | 0.878 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.231 | 12.105 | 12.339 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.294 | 12.149 | 12.420 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.234 | 12.117 | 12.400 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.416 | 0.385 | 0.448 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.441 | 0.420 | 0.483 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.448 | 0.420 | 0.490 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.416 | 0.385 | 0.448 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.441 | 0.420 | 0.483 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.448 | 0.420 | 0.490 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.703 | 0.671 | 0.734 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.717 | 0.691 | 0.741 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.720 | 0.692 | 0.741 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.703 | 0.671 | 0.734 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.717 | 0.691 | 0.741 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.720 | 0.692 | 0.741 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.497 | 0.462 | 0.538 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.507 | 0.469 | 0.538 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.521 | 0.483 | 0.545 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.497 | 0.462 | 0.538 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.507 | 0.469 | 0.538 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.521 | 0.483 | 0.545 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.175 | 0.140 | 0.203 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.192 | 0.161 | 0.231 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.189 | 0.154 | 0.210 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.175 | 0.140 | 0.203 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.192 | 0.161 | 0.231 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.189 | 0.154 | 0.210 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 97.000 | 96.000 | 98.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 2373.500 | 2326.750 | 2412.000 | 100 | 10 |
| skewed | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.949 | 0.931 | 0.965 | 100 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 1.000 | neutral_share | 0.903 | 0.893 | 0.908 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 2.000 | neutral_share | 0.796 | 0.790 | 0.802 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 5.000 | neutral_share | 0.565 | 0.553 | 0.593 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 10.000 | median_rel_change | 0.009 | 0.005 | 0.013 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 10.000 | neutral_share | 0.333 | 0.322 | 0.341 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 20.000 | median_rel_change | 0.029 | 0.022 | 0.041 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | 20.000 | neutral_share | 0.107 | 0.098 | 0.115 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.575 | 0.571 | 0.585 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.459 | 0.455 | 0.479 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.459 | 0.455 | 0.479 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.418 | 0.408 | 0.436 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.418 | 0.408 | 0.436 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.899 | 0.892 | 0.907 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.899 | 0.892 | 0.907 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.332 | 0.328 | 0.344 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.332 | 0.328 | 0.344 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.722 | 0.712 | 0.729 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.722 | 0.712 | 0.729 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.048 | 0.044 | 0.053 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.995 | 0.994 | 0.996 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.900 | 0.870 | 0.923 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.199 | 0.194 | 0.207 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.979 | 0.975 | 0.981 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.891 | 0.879 | 0.903 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.895 | 0.891 | 0.907 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.895 | 0.891 | 0.907 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.403 | 0.390 | 0.405 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.957 | 0.953 | 0.964 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.886 | 0.870 | 0.894 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.244 | 2.221 | 2.267 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.795 | 0.778 | 0.799 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.787 | 0.768 | 0.792 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.262 | 12.211 | 12.329 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.275 | 0.262 | 0.286 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.275 | 0.262 | 0.286 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.577 | 0.572 | 0.583 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.577 | 0.572 | 0.583 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.331 | 0.318 | 0.343 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.331 | 0.318 | 0.343 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.065 | 0.058 | 0.069 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.065 | 0.058 | 0.069 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | prefix | - | - | positive_cells | 99.000 | 99.000 | 99.000 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | prefix | - | - | prefix_length | 2306.750 | 2305.625 | 2340.625 | 10 | 10 |
| skewed | 50x50 | 2500 | random | - | prefix | - | - | prefix_share | 0.923 | 0.922 | 0.936 | 10 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.990 | 0.988 | 0.991 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.896 | 0.862 | 0.912 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.937 | 0.933 | 0.940 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.879 | 0.873 | 0.883 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.724 | 0.716 | 0.732 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.522 | 0.513 | 0.531 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.035 | 0.033 | 0.038 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.276 | 0.263 | 0.285 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.508 | 0.502 | 0.513 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.548 | 0.528 | 0.560 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.634 | 0.626 | 0.645 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.635 | 0.629 | 0.643 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.548 | 0.528 | 0.560 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.634 | 0.626 | 0.645 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.635 | 0.629 | 0.643 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.504 | 0.486 | 0.517 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.599 | 0.589 | 0.607 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.596 | 0.589 | 0.603 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.504 | 0.486 | 0.517 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.599 | 0.589 | 0.607 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.596 | 0.589 | 0.603 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.917 | 0.912 | 0.924 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.938 | 0.934 | 0.942 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.936 | 0.934 | 0.940 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.917 | 0.912 | 0.924 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.938 | 0.934 | 0.942 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.936 | 0.934 | 0.940 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.421 | 0.404 | 0.445 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.524 | 0.515 | 0.535 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.525 | 0.516 | 0.533 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.421 | 0.404 | 0.445 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.524 | 0.515 | 0.535 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.525 | 0.516 | 0.533 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.769 | 0.762 | 0.784 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.824 | 0.820 | 0.830 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.824 | 0.818 | 0.830 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.769 | 0.762 | 0.784 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.824 | 0.820 | 0.830 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.824 | 0.818 | 0.830 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.053 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.050 | 0.047 | 0.052 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.996 | 0.995 | 0.997 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.997 | 0.996 | 0.998 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 0.997 | 0.996 | 0.998 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.919 | 0.903 | 0.938 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.944 | 0.923 | 0.954 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.939 | 0.923 | 0.950 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.206 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.205 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.200 | 0.195 | 0.205 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.984 | 0.982 | 0.986 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.988 | 0.986 | 0.989 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.989 | 0.986 | 0.990 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.919 | 0.911 | 0.928 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.938 | 0.930 | 0.948 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.942 | 0.931 | 0.949 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.917 | 0.912 | 0.923 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.940 | 0.934 | 0.942 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.939 | 0.935 | 0.941 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.917 | 0.912 | 0.923 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.940 | 0.934 | 0.942 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.939 | 0.935 | 0.941 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.399 | 0.389 | 0.403 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.400 | 0.391 | 0.405 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.394 | 0.389 | 0.401 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.969 | 0.966 | 0.971 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.975 | 0.973 | 0.977 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.975 | 0.974 | 0.977 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.910 | 0.903 | 0.918 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.930 | 0.923 | 0.937 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.931 | 0.925 | 0.935 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.249 | 2.233 | 2.263 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.249 | 2.237 | 2.268 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.247 | 2.236 | 2.267 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.828 | 0.818 | 0.836 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.868 | 0.864 | 0.873 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.865 | 0.860 | 0.873 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.821 | 0.810 | 0.829 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.863 | 0.858 | 0.867 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.859 | 0.854 | 0.867 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.240 | 12.213 | 12.275 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.262 | 12.226 | 12.288 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.242 | 12.217 | 12.273 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.358 | 0.341 | 0.372 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.458 | 0.449 | 0.470 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.459 | 0.450 | 0.470 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.358 | 0.341 | 0.372 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.458 | 0.449 | 0.470 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.459 | 0.450 | 0.470 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.651 | 0.637 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.723 | 0.717 | 0.730 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.727 | 0.718 | 0.732 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.651 | 0.637 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.723 | 0.717 | 0.730 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.727 | 0.718 | 0.732 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.421 | 0.408 | 0.445 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.527 | 0.515 | 0.535 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.525 | 0.515 | 0.532 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.421 | 0.408 | 0.445 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.527 | 0.515 | 0.535 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.525 | 0.515 | 0.532 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.120 | 0.109 | 0.132 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.199 | 0.191 | 0.208 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.198 | 0.190 | 0.207 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.120 | 0.109 | 0.132 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.199 | 0.191 | 0.208 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.198 | 0.190 | 0.207 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 2700.000 | 2700.000 | 2700.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | positive_cells | 90.000 | 88.000 | 91.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_length | 2134.250 | 2097.375 | 2175.875 | 100 | 10 |
| ties | 50x50 | 2500 | GA-cost-tuned | 1.000 | prefix | - | - | prefix_share | 0.854 | 0.839 | 0.870 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share | 0.988 | 0.986 | 0.990 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | inherited_share_min | 0.902 | 0.889 | 0.914 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | heritability | OX1 | - | pairs | 200.000 | 200.000 | 200.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 1.000 | neutral_share | 0.937 | 0.923 | 0.958 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 2.000 | neutral_share | 0.881 | 0.867 | 0.897 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 5.000 | neutral_share | 0.720 | 0.699 | 0.741 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | median_rel_change | 0 | 0 | 0 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 10.000 | neutral_share | 0.524 | 0.503 | 0.554 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | median_rel_change | 0.034 | 0.029 | 0.040 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | 20.000 | neutral_share | 0.287 | 0.252 | 0.308 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | locality | - | - | spearman_k_vs_abs_change | 0.511 | 0.483 | 0.524 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.629 | 0.608 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.636 | 0.608 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.636 | 0.608 | 0.671 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.629 | 0.608 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.636 | 0.608 | 0.664 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.636 | 0.608 | 0.671 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.587 | 0.565 | 0.622 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.608 | 0.586 | 0.629 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.598 | 0.573 | 0.629 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.587 | 0.565 | 0.622 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.608 | 0.586 | 0.629 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.598 | 0.573 | 0.629 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share | 0.937 | 0.916 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share | 0.937 | 0.923 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share | 0.944 | 0.937 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.937 | 0.916 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.937 | 0.923 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | neutral_share_mutated | 0.944 | 0.937 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share | 0.524 | 0.490 | 0.547 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share | 0.528 | 0.497 | 0.552 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share | 0.538 | 0.497 | 0.566 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.524 | 0.490 | 0.547 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.528 | 0.497 | 0.552 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | neutral_share_mutated | 0.538 | 0.497 | 0.566 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:10 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share | 0.825 | 0.804 | 0.839 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share | 0.818 | 0.804 | 0.846 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share | 0.825 | 0.811 | 0.846 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.825 | 0.804 | 0.839 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.818 | 0.804 | 0.846 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | neutral_share_mutated | 0.825 | 0.811 | 0.846 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_count:3 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.056 | 0.035 | 0.063 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.040 | 0.063 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.035 | 0.063 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share | 1.000 | 0.993 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.885 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.889 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 1.000 | 0.875 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.203 | 0.187 | 0.219 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.180 | 0.219 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.196 | 0.175 | 0.219 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.990 | 0.979 | 0.993 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share | 0.986 | 0.979 | 0.993 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.936 | 0.913 | 0.967 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.944 | 0.904 | 0.969 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.933 | 0.896 | 0.963 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:0.2 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share | 0.930 | 0.923 | 0.944 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share | 0.937 | 0.923 | 0.953 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share | 0.944 | 0.930 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.930 | 0.923 | 0.944 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.937 | 0.923 | 0.953 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.944 | 0.930 | 0.951 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_fixed:1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.395 | 0.350 | 0.427 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.406 | 0.364 | 0.427 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.388 | 0.369 | 0.441 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.972 | 0.965 | 0.986 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.976 | 0.972 | 0.986 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.979 | 0.965 | 0.986 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.925 | 0.901 | 0.953 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.929 | 0.911 | 0.958 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.935 | 0.917 | 0.963 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.0005 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.231 | 2.189 | 2.288 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.227 | 2.182 | 2.308 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.231 | 2.173 | 2.295 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.860 | 0.844 | 0.881 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.874 | 0.860 | 0.888 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share | 0.871 | 0.853 | 0.890 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.856 | 0.838 | 0.877 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.868 | 0.853 | 0.883 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.865 | 0.846 | 0.885 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.002 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.241 | 12.112 | 12.414 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.262 | 12.119 | 12.420 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.255 | 12.112 | 12.413 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.448 | 0.413 | 0.476 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.462 | 0.427 | 0.490 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share | 0.458 | 0.427 | 0.497 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.448 | 0.413 | 0.476 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.462 | 0.427 | 0.490 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.458 | 0.427 | 0.497 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_per_position:0.01 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.720 | 0.692 | 0.741 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.727 | 0.699 | 0.748 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share | 0.741 | 0.713 | 0.762 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.720 | 0.692 | 0.741 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.727 | 0.699 | 0.748 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.741 | 0.713 | 0.762 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.05 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.524 | 0.497 | 0.552 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.535 | 0.502 | 0.566 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share | 0.535 | 0.503 | 0.559 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.524 | 0.497 | 0.552 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.535 | 0.502 | 0.566 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.535 | 0.503 | 0.559 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.1 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.189 | 0.168 | 0.217 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.206 | 0.182 | 0.224 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share | 0.210 | 0.182 | 0.233 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.189 | 0.168 | 0.217 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.206 | 0.182 | 0.224 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.210 | 0.182 | 0.233 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.100 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 0.500 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | neutrality | swap_scaled:0.25 | - | offspring | 143.000 | 143.000 | 143.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | positive_cells | 88.000 | 87.000 | 90.000 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_length | 2152.000 | 2072.500 | 2234.750 | 100 | 10 |
| ties | 50x50 | 2500 | GA-rand-tuned | 1.000 | prefix | - | - | prefix_share | 0.861 | 0.829 | 0.894 | 100 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 1.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 1.000 | neutral_share | 0.899 | 0.896 | 0.912 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 2.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 2.000 | neutral_share | 0.821 | 0.812 | 0.832 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 5.000 | median_rel_change | 0 | 0 | 0 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 5.000 | neutral_share | 0.601 | 0.591 | 0.619 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 10.000 | median_rel_change | 0.009 | 0.009 | 0.010 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 10.000 | neutral_share | 0.362 | 0.354 | 0.371 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 20.000 | median_rel_change | 0.026 | 0.025 | 0.027 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | 20.000 | neutral_share | 0.134 | 0.128 | 0.143 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | locality | - | - | spearman_k_vs_abs_change | 0.564 | 0.558 | 0.571 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | mean_swaps | 7.000 | 7.000 | 7.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share | 0.487 | 0.484 | 0.500 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | neutral_share_mutated | 0.487 | 0.484 | 0.500 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-cost-tuned (swap_count:7) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | mean_swaps | 8.000 | 8.000 | 8.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share | 0.444 | 0.434 | 0.447 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | neutral_share_mutated | 0.444 | 0.434 | 0.447 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | GA-rand-tuned (swap_scaled:0.0837) | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share | 0.905 | 0.895 | 0.914 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | neutral_share_mutated | 0.905 | 0.895 | 0.914 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share | 0.370 | 0.365 | 0.379 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | neutral_share_mutated | 0.370 | 0.365 | 0.379 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:10 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | mean_swaps | 3.000 | 3.000 | 3.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share | 0.740 | 0.735 | 0.751 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | neutral_share_mutated | 0.740 | 0.735 | 0.751 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_count:3 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | mean_swaps | 0.049 | 0.044 | 0.054 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share | 0.994 | 0.994 | 0.996 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | neutral_share_mutated | 0.899 | 0.858 | 0.913 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | mean_swaps | 0.208 | 0.203 | 0.214 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share | 0.978 | 0.977 | 0.982 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | neutral_share_mutated | 0.895 | 0.891 | 0.910 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:0.2 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | mean_swaps | 1.000 | 1.000 | 1.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share | 0.905 | 0.902 | 0.911 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | neutral_share_mutated | 0.905 | 0.902 | 0.911 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_fixed:1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | mean_swaps | 0.403 | 0.396 | 0.410 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share | 0.960 | 0.958 | 0.965 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | neutral_share_mutated | 0.891 | 0.886 | 0.902 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.0005 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | mean_swaps | 2.276 | 2.223 | 2.304 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share | 0.800 | 0.792 | 0.804 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | neutral_share_mutated | 0.790 | 0.785 | 0.796 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.002 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | mean_swaps | 12.253 | 12.231 | 12.319 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share | 0.307 | 0.288 | 0.311 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | neutral_share_mutated | 0.307 | 0.288 | 0.311 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_per_position:0.01 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | mean_swaps | 5.000 | 5.000 | 5.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share | 0.593 | 0.588 | 0.597 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | neutral_share_mutated | 0.593 | 0.588 | 0.597 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.05 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | mean_swaps | 10.000 | 10.000 | 10.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share | 0.367 | 0.355 | 0.377 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | neutral_share_mutated | 0.367 | 0.355 | 0.377 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.1 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | mean_swaps | 25.000 | 25.000 | 25.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share | 0.088 | 0.084 | 0.093 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | neutral_share_mutated | 0.088 | 0.084 | 0.093 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | neutrality | swap_scaled:0.25 | - | offspring | 1000.000 | 1000.000 | 1000.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | prefix | - | - | basis_size | 99.000 | 99.000 | 99.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | prefix | - | - | positive_cells | 94.000 | 93.250 | 94.000 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | prefix | - | - | prefix_length | 2250.500 | 2246.750 | 2259.250 | 10 | 10 |
| ties | 50x50 | 2500 | random | - | prefix | - | - | prefix_share | 0.900 | 0.899 | 0.904 | 10 | 10 |
