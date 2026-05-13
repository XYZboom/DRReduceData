This repository stores all data for DRReduce, including the programs before reduction and those reduced by different state‑of‑the‑art (SOTA) reducers.

- **[gcc](./gcc) and [clang](./clang)** – bugs for C compilers.
- **[java](./java)** – bugs for Java compilers or type‑checking plugins.

Each bug is named as `{compiler_name}-{id}`.

For example, in [clang-22382]:
- [cdd_result](clang/clang-22382/cdd_result): Result of CDD
    - [cdd_result.txt](clang/clang-22382/cdd_result/cdd_result.txt): Statistical information such as reduction time and query invocations
    - [small.c](clang/clang-22382/cdd_result/small.c): Reduction Result
- [predict.sh](clang/clang-22382/predict.sh): The predict script for this bug. Should run outside docker.
- [r.sh](clang/clang-22382/r.sh): The original predict script for this bug. Should run inside docker.
- [small.c](clang/clang-22382/small.c): The program before reduction.
- [ssreducer](clang/clang-22382/ssreducer): Result of DRReducer
- [ssreducer_no_g_rdp0](clang/clang-22382/ssreducer_no_g_rdp0): Result that without reconstruction.