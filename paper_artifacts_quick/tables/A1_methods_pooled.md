# Appendix: comparisons pooled over sizes

Not used for conclusions; see T5.

| set | size | method_a | method_b | value | n | nonzero | W | p | rank_biserial_r | hl_shift | hl_ci_low | hl_ci_high | hl_method | wins_x | wins_y | ties | p_holm | p_holm_text |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| structured | all sizes | GA-rand-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -6.544 | -11.860 | -5.296 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | all sizes | GA-cost-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -7.309 | -12.249 | -5.870 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | all sizes | SA-rand-tuned | VAM | gap | 10 | 10 | 0 | 0.002 | -1.000 | -6.929 | -11.560 | -5.316 | exact Walsh-average CI | 10 | 0 | 0 | 0.010 | 0.010 |
| structured | all sizes | SA-rand-tuned | GA-rand-tuned | gap | 10 | 10 | 19.000 | 0.432 | -0.309 | -0.194 | -0.702 | 0.225 | exact Walsh-average CI | 6 | 4 | 0 | 0.432 | 0.432 |
| structured | all sizes | SA-cost-tuned | GA-cost-tuned | gap | 10 | 10 | 3.000 | 0.010 | -0.891 | -0.388 | -0.650 | -0.133 | exact Walsh-average CI | 8 | 2 | 0 | 0.020 | 0.020 |
| uniform | all sizes | GA-rand-tuned | VAM | gap | 50 | 45 | 483.000 | 0.704 | 0.067 | 0.053 | -2.986 | 6.578 | exact Walsh-average CI | 27 | 18 | 5 | 0.921 | 0.921 |
| uniform | all sizes | GA-cost-tuned | VAM | gap | 50 | 44 | 0 | 1.137e-13 | -1.000 | -13.498 | -17.737 | -9.826 | exact Walsh-average CI | 44 | 0 | 6 | 5.684e-13 | < 0.001 |
| uniform | all sizes | SA-rand-tuned | VAM | gap | 50 | 45 | 444.000 | 0.414 | 0.142 | 1.502 | -2.670 | 12.069 | exact Walsh-average CI | 23 | 22 | 5 | 0.921 | 0.921 |
| uniform | all sizes | SA-rand-tuned | GA-rand-tuned | gap | 50 | 38 | 299.000 | 0.307 | 0.193 | 0.243 | -0.713 | 9.655 | exact Walsh-average CI | 19 | 19 | 12 | 0.921 | 0.921 |
| uniform | all sizes | SA-cost-tuned | GA-cost-tuned | gap | 50 | 41 | 229.000 | 0.008 | 0.468 | 0.792 | 0 | 1.508 | exact Walsh-average CI | 18 | 23 | 9 | 0.033 | 0.033 |
