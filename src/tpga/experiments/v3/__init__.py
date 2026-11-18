"""Additional experiment v3 (amendment 8 of docs/v0.4/PREREGISTRATION.md): cycle mutation, one protocol for
the linear problem and the fixed-charge transportation problem.

    python -m tpga.experiments.v3 kselect --config experiments/paper-v3-cycle.yaml
    python -m tpga.experiments.v3 pilot   --config experiments/paper-v3-cycle.yaml
    python -m tpga.experiments.v3 run     --config experiments/paper-v3-cycle.yaml
    python -m tpga.experiments.v3 run     --config experiments/paper-v3-fctp.yaml
    python -m tpga.experiments.v3 benchmark --config experiments/paper-v3-fctp.yaml
    python -m tpga.experiments.v3 report  --config experiments/paper-v3-cycle.yaml
    python -m tpga.experiments.v3 report  --config experiments/paper-v3-fctp.yaml
"""
