# External FCTP benchmark: reference values

Source: MIPLIB 2017, https://miplib.zib.de (instances gr4x6, ran13x13, ran12x21; objective values as listed on the instance pages on 2026-11-19). `listed_objective` is the value given by the source; the HiGHS columns are our MIP run.

| instance | size | listed_objective | url | highs_status | highs_proved | highs_cost | highs_bound | highs_time_s | highs_minus_listed |
|---|---|---|---|---|---|---|---|---|---|
| gr4x6 | 4x6 | 202.3 | https://miplib.zib.de/instance_details_gr4x6.html | Optimal | yes | 202.3 | 202.3 | 0.0176 | 0 |
| ran13x13 | 13x13 | 3252 | https://miplib.zib.de/instance_details_ran13x13.html | Optimal | yes | 3252 | 3252 | 6.611 | 0 |
| ran12x21 | 12x21 | 3664 | https://miplib.zib.de/instance_details_ran12x21.html | Optimal | yes | 3664 | 3664 | 15.72 | 0 |
