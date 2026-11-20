# tp-ga

[![CI](https://github.com/Almasmm/tp-ga/actions/workflows/ci.yml/badge.svg)](https://github.com/Almasmm/tp-ga/actions/workflows/ci.yml)
[![Release](https://github.com/Almasmm/tp-ga/actions/workflows/release.yml/badge.svg)](https://github.com/Almasmm/tp-ga/actions/workflows/release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24388243.svg)](https://doi.org/10.5281/zenodo.24388243)
![Python](https://img.shields.io/badge/python-3.10%E2%80%933.14-blue)

`tpga` is a Python library for studying genetic algorithms on the transportation problem. It uses permutations
of shipping arcs to represent candidate solutions and a greedy decoder to turn them into shipment plans.
The project includes a linear programming solver for computing the optimum, scripts for reproducing the
experiments and a web interface for inspecting plans and algorithm steps. It grew out of master's research
at Astana IT University.

## Problem

Minimise $Z = \sum_i \sum_j c_{ij} x_{ij}$ subject to $\sum_j x_{ij} = a_i$, $\sum_i x_{ij} = b_j$, $x_{ij} \ge 0$.

A chromosome is a permutation of the $m \cdot n$ arcs. The decoder visits the arcs in that order and assigns
$x_{ij} = \min(a_i^{(r)}, b_j^{(r)})$, the smaller of the remaining supply and demand. For a balanced problem
with a complete arc set every chromosome therefore decodes to a feasible plan, and no penalty or repair is needed.
This feasibility guarantee applies to the balanced model with a complete arc set. The LP optimum gives a
reference for measuring the gap of a decoded plan.

## Installation

```bash
git clone https://github.com/Almasmm/tp-ga.git
cd tp-ga
pip install -e .            # library and CLI
pip install -e .[dev]       # plus pytest, ruff, mypy, build
```

## Usage

Command line:

```bash
tpga generate instance.json -m 6 -n 8 --seed 42
tpga solve examples/small_3x3.json --seed 0
tpga solve examples/random_6x8.json --method both --seed 0 --plot conv.png --plan-plot plan.png --json
```

```text
instance: 3 sources x 3 destinations, balanced=True
LP optimum: 225.0000
GA best:    225.0000  (gap 0.00%, 12060 evaluations, 0.41s)
```

Python API:

```python
from tpga import TransportProblem, GAConfig, run_ga, solve_lp

p = TransportProblem(supply=[20, 30, 20], demand=[25, 25, 20], cost=[[8, 6, 3], [5, 4, 9], [2, 7, 6]])
x_lp, z_lp = solve_lp(p)  # exact optimum: 225
r = run_ga(p, GAConfig(population=60, generations=200, seed=0))
print(r.cost, r.evaluations, p.is_feasible(r.x))
```

Unbalanced instances are balanced automatically with a zero-cost dummy source or destination.

| Convergence on `examples/random_6x8.json` | Best plan |
|---|---|
| ![convergence](docs/img/convergence_6x8.png) | ![plan](docs/img/plan_6x8.png) |

One run with seed 0 (population 80, 300 generations): GA cost 5342, LP optimum 5342.
The benchmark results across instances and seeds are reported below.

## Computational experiment

The original study compares the genetic algorithm with exact and classical methods on the balanced
transportation problem. Run the configuration in [`experiments/paper.yaml`](experiments/paper.yaml),
then build the tables and figures from the raw results.

```bash
pip install -e .[dev]
python -m tpga.experiments.run --config experiments/paper.yaml       # resumable; --pilot estimates the duration
python -m tpga.experiments.report --config experiments/paper.yaml
```

The results, instances, figures (English and Russian), tables, `METHODS.md`, `LIMITATIONS.md` and
`NUMBERS.md` (every number with its source) are in [`paper_artifacts/`](paper_artifacts/README.md).

## Paper materials

The v0.3 study uses results from release 0.3.0. Tag `v0.3.1-paper` adds the neutrality and normalised-gap checks.

| Path | Content |
|---|---|
| [`experiments/paper.yaml`](experiments/paper.yaml) | Configuration of the experiment (instances, methods, seeds, budget) |
| [`paper_artifacts/`](paper_artifacts/README.md) | Instances, raw runs, tables, figures (English and Russian), `METHODS.md`, `LIMITATIONS.md`, `NUMBERS.md` |
| [`paper_artifacts_supplement/neutrality/`](paper_artifacts_supplement/neutrality) | Check of Proposition 3 on the test instances: share of neutral swaps, the two kinds of non-neutral swaps, exceptions (0) |
| [`paper_artifacts_supplement/normalised_gap/`](paper_artifacts_supplement/normalised_gap) | `Z_rand` of every instance and the normalised gap `(Z - Z*) / (Z_rand - Z*)` of the runs of the main phase |
| [`scripts/neutrality_check.py`](scripts/neutrality_check.py), [`scripts/normalised_gap.py`](scripts/normalised_gap.py) | The scripts that write the two supplement folders |
| [`tests/test_proposition3.py`](tests/test_proposition3.py) | Property test of Proposition 3 on random and degenerate instances |

Reproduce from the repository root (tag `v0.3.1-paper`):

```bash
pip install -e .[dev]
python -m tpga.experiments.report --config experiments/paper.yaml   # tables and figures of v0.3.0 from the raw runs
python scripts/neutrality_check.py                                  # paper_artifacts_supplement/neutrality
python scripts/normalised_gap.py                                    # paper_artifacts_supplement/normalised_gap
pytest tests/test_proposition3.py
```

Both scripts use fixed seeds and write the same files on every run. `normalised_gap.py` keeps the `Z_rand`
values already in `zrand.csv`; delete that file to compute them again (a few minutes on one core).
Use `scripts/watch_tuning.py` to follow v0.4 parameter tuning from the terminal.

## Quick run of the v0.4 experiment

The [quick configuration](experiments/paper-v2-quick.yaml) uses uniform instances from 5×5 to 50×50 and
structured 20×20 instances. It uses 10 instances per size and 10 seeds, with a budget of 200 × m × n decoder
calls. The methods are LP, NWC, LCM, VAM, random search, and tuned GA and SA with random and cost-aware starts.
The three phases took about eight minutes on 24 logical processors for 4,500 runs.

```bash
pip install -e ".[runner]"
python scripts/run_main.py --config experiments/paper-v2-quick.yaml --priority normal --phase reference --phase representation --phase main
```

The [quick-run archive](paper_artifacts_quick/) contains the records, figures and tables from 18 November 2026.
This separate run uses the first instances and seeds from the [preregistered plan](docs/v0.4/PREREGISTRATION.md)
and the frozen parameters in `experiments/tuned-v2.yaml`. Its durations reflect 24 concurrent runs.
The [partial archive of the preregistered experiment](paper_artifacts_v2/README.md) has its own progress report.

## Additional experiment v3: cycle mutation and the fixed-charge problem

The additional experiment was planned in amendment 8 of
[`docs/v0.4/PREREGISTRATION.md`](docs/v0.4/PREREGISTRATION.md) before its code was written: a mutation that
makes random simplex pivots on the decoded plan (`tpga.cycle`), one protocol for the linear problem up to
100x100, and the fixed-charge transportation problem (`tpga.fctp`) with a MIP reference and three MIPLIB
instances. Amendment 9 extends it after its results were seen: the 100x100 set with all 10 instances, a grid
on FCTP training instances, the MIP solver with the run time of the GA as its limit, and FCTP sizes 50x50 and
70x70. Commands, tables and limits are in [`paper_artifacts_v3/README.md`](paper_artifacts_v3/README.md);
the experiment of amendment 8 takes about an hour on 24 logical processors and the extension another hour:

```bash
pip install -e ".[runner]"
python -m tpga.experiments.v3 kselect --config experiments/paper-v3-cycle.yaml      # then pilot, run, extend, report
python -m tpga.experiments.v3 run     --config experiments/paper-v3-fctp.yaml       # then benchmark, report
python -m tpga.experiments.v3 tune    --config experiments/paper-v3-fctp-ext.yaml   # then run, report
python -m tpga.experiments.v3 pilot   --config experiments/paper-v3-review.yaml     # amendment 10, see below
```

Amendment 10 answers a review and is exploratory as well (`experiments/paper-v3-review.yaml`, results in
`paper_artifacts_v3/review/`): a tabu search and an iterated local search over basis pivots
(`tpga.localsearch`) as rivals on the fixed-charge problem, the MIP solver with all threads and 300 s, new
instance classes and ten public instances, times with one run at a time, the share of pivots with theta > 0,
a second rule for the entering arc of the cycle mutation (`GAXConfig(entering="nondegenerate")`), effect
sizes with intervals and three figures. With the same budget of evaluations both local searches are better
than the GA on the fixed-charge problem. Its commands are `pilot`, `tune`, `rivals`, `generator`,
`degenerate`, `public`, `timing`, `mipdefault` and `report`, in this order; together they took 84 minutes.

## Project structure

```text
src/tpga/              model, decoder, ga (+ compiled _kernels), exact, classical, basis, verify, ga_trace, cli, plot
src/tpga/experiments/  configuration, instance sets, runner, reachability check, report
experiments/           paper.yaml
paper_artifacts/       instances, raw results, tables, figures and documents of the paper
platform/              FastAPI backend (app/, migrations/, tests/), Next.js interface (web/), Dockerfile, docker-compose
datasets/              kazakh-wheat (with rail-pilot), astana-potato
scripts/               dev.ps1 (local platform), benchmark.py, rail tools
tests/                 unit, property (hypothesis), kernel, experiment and CLI tests (pytest)
.github/               CI and release workflows, Dependabot, issue and PR templates
```

## Web platform

The [web application](platform/README.md) plans shipments for the Kazakhstan wheat case and the full Astana benchmark. It compares random and cost-aware GA starts with the LP optimum. The platform includes a Next.js interface and a FastAPI backend.

The numerical code uses NumPy. Numba compiles the decoder and GA operators, with plain Python versions
available for reference tests. SciPy calls HiGHS for the LP reference, and Matplotlib produces the figures.

## Quality checks and CI/CD

- [`ci.yml`](.github/workflows/ci.yml) — on every push and pull request: ruff lint and format check, mypy, then the
  test suite on **Ubuntu and Windows × Python 3.10–3.14** with a 90 % coverage gate, the platform API
  tests and the web job (ESLint, `next build`, Playwright), then a package build
  whose wheel is installed in a clean environment and smoke-tested with the CLI.
- [`release.yml`](.github/workflows/release.yml) — on a tag `vX.Y.Z`: runs the tests, checks that the tag equals the
  package version, builds the sdist and wheel and publishes them as a **GitHub Release** (continuous delivery).
- [`paper-release.yml`](.github/workflows/paper-release.yml) — on a tag `vX.Y.Z-paper` (code and data of the
  article): one archive of the tracked files of `paper_artifacts_v2/`, `paper_artifacts_quick/` and
  `paper_artifacts_v3/` with the preregistration and the configurations, attached to a **GitHub Release**.
- [`dependabot.yml`](.github/dependabot.yml) — monthly update pull requests for actions and Python dependencies.
- `main` is protected: changes arrive through pull requests that must pass CI.

Run the same checks locally:

```bash
ruff check . && ruff format --check . && mypy && pytest --cov=tpga
```

## Contributing, citation, licence

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md). Citation metadata is in
[CITATION.cff](CITATION.cff). Released under the [MIT licence](LICENSE).

The code and data of the article (tag `v0.4.1-paper`) are archived in Zenodo:
[10.5281/zenodo.24388243](https://doi.org/10.5281/zenodo.24388243) is the DOI of this version and
[10.5281/zenodo.24388242](https://doi.org/10.5281/zenodo.24388242) the DOI of all versions, which leads to the
latest one.

Author: Almas Murat, Astana IT University. ORCID [0009-0008-6202-088X](https://orcid.org/0009-0008-6202-088X).
