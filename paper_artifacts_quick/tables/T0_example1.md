# Example 1 (Section 2.2)

Recomputed by the library; shipments in the order of allocation.

| method | shipments_in_order | positive | cost | gap |
|---|---|---|---|---|
| NWC | x11 = 50, x12 = 20, x22 = 30, x23 = 35, x33 = 15, x34 = 25 | 6 | 2445.000 | 10.135 |
| LCM | x23 = 50, x31 = 40, x11 = 10, x14 = 25, x12 = 35, x22 = 15 | 6 | 2345.000 | 5.631 |
| VAM | x23 = 50, x11 = 50, x34 = 25, x12 = 20, x22 = 15, x32 = 15 | 6 | 2310.000 | 4.054 |
| Decoder, random permutation | x11 = 50, x24 = 25, x23 = 40, x32 = 40, x13 = 10, x12 = 10 | 6 | 2835.000 | 27.703 |
| Decoder, leaf-elimination order | x23 = 50, x34 = 25, x22 = 15, x31 = 15, x12 = 35, x11 = 35 | 6 | 2220.000 | 0 |
| LP optimum (HiGHS) | x11 = 35, x12 = 35, x22 = 15, x23 = 50, x31 = 15, x34 = 25 | 6 | 2220.000 | 0 |
