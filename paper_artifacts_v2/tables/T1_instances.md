# Instance sets

Median LP optimum and Z_rand (mean cost of 1000 decoded random permutations).

| set | size | instances | arcs | z_star_median | z_rand_median | generator |
|---|---|---|---|---|---|---|
| uniform | 5x5 | 10 | 25 | 7508.000 | 13890.250 | tpga.experiments.v2.instances._uniform |
| uniform | 10x10 | 10 | 100 | 8824.500 | 29173.210 | tpga.experiments.v2.instances._uniform |
| uniform | 20x20 | 10 | 400 | 10338.500 | 62484.955 | tpga.experiments.v2.instances._uniform |
| uniform | 30x30 | 10 | 900 | 11412.500 | 95665.644 | tpga.experiments.v2.instances._uniform |
| uniform | 50x50 | 10 | 2500 | 12013.500 | 1.503e+05 | tpga.experiments.v2.instances._uniform |
| uniform | 100x100 | 10 | 10000 | 13818.500 | 2.942e+05 | tpga.experiments.v2.instances._uniform |
| uniform | 200x200 | 10 | 40000 | 17805.000 | 5.978e+05 | tpga.experiments.v2.instances._uniform |
| structured | 20x20 | 10 | 400 | 29025.500 | 71714.817 | tpga.experiments.v2.instances._structured |
| structured | 50x50 | 10 | 2500 | 53291.000 | 1.695e+05 | tpga.experiments.v2.instances._structured |
| structured | 100x100 | 10 | 10000 | 91491.000 | 3.450e+05 | tpga.experiments.v2.instances._structured |
| skewed | 20x20 | 10 | 400 | 65656.000 | 1.436e+05 | tpga.experiments.v2.instances.skewed_instance |
| skewed | 50x50 | 10 | 2500 | 92103.000 | 4.219e+05 | tpga.experiments.v2.instances.skewed_instance |
| ties | 20x20 | 10 | 400 | 228.500 | 638.798 | tpga.experiments.v2.instances.ties_instance |
| ties | 50x50 | 10 | 2500 | 525.000 | 1554.447 | tpga.experiments.v2.instances.ties_instance |
| lp_scaling | 100x100 | 10 | 10000 | – | – | tpga.experiments.v2.instances._uniform |
| lp_scaling | 200x200 | 10 | 40000 | – | – | tpga.experiments.v2.instances._uniform |
| lp_scaling | 500x500 | 10 | 250000 | – | – | tpga.experiments.v2.instances._uniform |
| lp_scaling | 1000x1000 | 10 | 1000000 | – | – | tpga.experiments.v2.instances._uniform |
| wheat | 15x7 | 5 | 105 | 1.368e+11 | 1.477e+11 | – |
| astana | 24x324 | 33 | 7776 | 4.632e+05 | 6.684e+05 | – |
