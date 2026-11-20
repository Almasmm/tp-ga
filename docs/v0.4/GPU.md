# GPU prototype (v0.4)

**Decision: the GPU is not used in the v0.4 experiment.** In the form that keeps the GA unchanged (the CPU
creates the offspring, the GPU decodes them), the GPU decoder is exact but 4 to 25 times slower than the
same decoder on all 24 CPU threads. The acceptance rule set before the benchmark was "enable only if more
than 2 times faster and bitwise equal". It is bitwise equal, but it is not faster.

## Machine and software

| Item | Value |
|---|---|
| GPU | NVIDIA GeForce RTX 5090 Laptop GPU, 24 GB, compute capability 12.0, driver 621.01, WDDM |
| CPU | 24 logical processors (8 performance cores, 16 efficiency cores) |
| Software | Python 3.14, numba 0.68.1, numba-cuda 0.30.4 with the CUDA 13.5 pip wheels, numpy 2.4.6 |

State before the prototype: `numba.cuda.is_available()` was `False` in the project environment (no CUDA
toolkit) and CuPy was not installed. The prototype uses a separate environment `.venv-gpu` (not tracked)
so that the main environment is unchanged. numba-cuda 0.30.4 does not import with numpy 2.5 (it refers
to `np.row_stack`, which numpy 2.5 removed), so `.venv-gpu` pins numpy 2.4.6. The main environment keeps
numpy 2.5.4.

## What was built

`src/tpga/gpu.py`: the greedy decoder as a CUDA kernel, one thread per permutation, following
`tpga._kernels._decode_cost_py` step by step (same arc order, same early stop when all supply is used).
Two variants: `float64`, and `int64` for integer data (exact integer arithmetic; consumer GPUs run FP64 at
1/64 of the FP32 rate). The module is not imported by the GA or by the experiment.

## Benchmark

`experiments/gpu_bench.py` (raw numbers in `docs/v0.4/gpu_bench.json`): decoding a batch of random
permutations of a uniform instance; median of 5 timed repeats after a warm-up. The GPU time includes copying
the permutations to the device and the costs back, as it would in a GA whose operators stay on the CPU.
"All cores" is the same CPU kernel under `numba.prange` with 24 threads.

| Size | Batch | CPU, 1 core, ms | CPU, 24 threads, ms | GPU int64, ms | GPU float64, ms | GPU / 24 threads speed | Bitwise equal |
|---|---|---|---|---|---|---|---|
| 50x50 | 100 | 0.53 | 0.076 | 1.44 | 1.46 | 0.05 | yes |
| 50x50 | 2400 | 13.9 | 1.58 | 5.80 | 5.71 | 0.27 | yes |
| 100x100 | 100 | 1.86 | 0.236 | 5.70 | 5.92 | 0.04 | yes |
| 100x100 | 2400 | 48.3 | 4.42 | 22.4 | 22.9 | 0.20 | yes |
| 200x200 | 100 | 7.74 | 0.835 | 22.7 | 24.3 | 0.04 | yes |
| 200x200 | 2400 | 181.0 | 19.8 | 93.5 | 102.2 | 0.21 | yes |

Batch 100 is one GA population; batch 2400 is what 24 GA processes would decode per generation together.
Every GPU cost equalled the CPU cost bit for bit (integer data, all partial sums below 2^53).

### Where the time goes

Kernel time alone (permutations already on the device; `docs/v0.4/gpu_kernel_only.json`, measured by a
one-off script, int64 variant):

| Size | Batch | Kernel, ms | Copy of the permutations, ms |
|---|---|---|---|
| 50x50 | 2400 | 0.99 | 4.7 |
| 50x50 | 24000 | 2.36 | 44.6 |
| 100x100 | 2400 | 4.86 | 21.8 |
| 100x100 | 24000 | 10.5 | 190 |
| 200x200 | 2400 | 19.8 | 95 |
| 200x200 | 6000 | 21.3 | 169 |

The copy of the permutations (8 bytes per arc and per individual) dominates. Without it, at batch 2400 the
kernel is about as fast as 24 CPU threads (1.6x at 50x50, 0.9x to 1.0x at 100x100 and 200x200); only at
batches of 6000 to 24000 decodes per step does it reach several times the CPU rate.

## What would be needed for a real gain (not done)

A GPU-resident GA: populations, selection, order crossover and swap mutation on the device, many
independent runs at once (thousands of individuals per step), and only the uniforms copied from the host.
To stay bitwise equal to the CPU GA, the device code would have to consume the same uniforms in the same
order as `tpga._kernels._next_generation_py`. That is a separate project; it is not needed for the v0.4
experiment and is not part of it.

## Reproduce

```
python -m venv .venv-gpu
.venv-gpu/Scripts/python -m pip install -e . "numba-cuda[cu13]" "numpy<2.5" pyyaml
.venv-gpu/Scripts/python experiments/gpu_bench.py
```
