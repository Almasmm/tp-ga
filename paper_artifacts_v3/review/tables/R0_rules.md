# Amendment 10: time used by every run command and what the reduction rules gave

Times in seconds, measured inside the commands (`review/budget.json`). Limit of all run commands: 90 minutes. `allowance_s`: what the command could use when it started (10.0, 10.9).

| command | started | allowance_s | wall_s | beyond_limit | rule_gave |
|---|---|---|---|---|---|
| pilot | 2026-11-20T01:18:34 | 120 | 30.39 | no | 16 single runs |
| tune | 2026-11-20T01:19:09 | 209.6 | 2.977 | no | grids complete |
| rivals | 2026-11-20T01:19:16 | 386.6 | 10.46 | no | 5 instances per cell at 70x70, 5 at 50x50 |
| generator | 2026-11-20T01:19:31 | 1036 | 358.8 | no | 5 instances per new cell |
| degenerate | 2026-11-20T01:25:34 | 1577 | 694.7 | no | 0 instances at 100x100 for 10.5 b, 3 for 10.5 a |
| public | 2026-11-20T01:37:13 | 1183 | 79.87 | no | 10 instances, 0 left out |
| timing | 2026-11-20T01:38:37 | 1703 | 1350 | no | 3 round(s) of one instance per cell; sizes left out: [] |
| mipdefault | 2026-11-20T02:01:12 | 2753 | 2519 | no | see R4_mip_instances |
| all commands within the limit | – | 5400 | 5046 | – | MIP in its usual setting: 40 run in the last start, 20 not run (time rule) |
