# Lean-checked conditional projection and Laplace criteria

## Metadata and result

- Date: 2026-11-11; author: Rohan Arun with OpenAI Codex assistance.
- Primary track: T02. Related: T03, T05, T06, T07.
- Outcome: five proved generic conditional lemmas and one proved negative control.
- Evidence: successful Lean 4.32.0 run with `--trust=0 -j1`, checking imported modules at trust level zero and elaborating the new source. Six axiom reports contain only `propext`, `Classical.choice`, and `Quot.sound`.
- Exact [source](lean/GapCriteria.lean), [verification receipt](verification.json), [output](kernel-check.log), and [runtime provenance](runtime-provenance.json).
- No independent human review and no replay of the upstream Yang–Mills project have been performed. These are standard functional-analytic tools, not a new Yang–Mills theorem.

## Statements checked

| Theorem | Scope |
| --- | --- |
| `idempotent_eq_zero_of_bound` | A continuous linear idempotent on a real normed space is zero if its norm on every vector is bounded by one fixed factor strictly below one. |
| `idempotent_eq_zero_of_dense_bound` | The same conclusion follows if the uniform bound holds on a dense subset, by continuity. |
| `idempotent_eq_zero_of_approximation` | For a contractive idempotent, it is enough to approximate every vector in its range with combined approximation error and projected-state cost strictly below one times its norm. All such estimates are explicit hypotheses. |
| `zero_of_exponential_bound` | A nonnegative scalar bounded for all nonnegative times by a fixed decaying exponential is zero. |
| `zero_of_laplace_comparison` | If `exp(-a*t)*mass <= C*exp(-m*t)` for all nonnegative times, `mass >= 0`, and `a < m`, then `mass = 0`. This checks the scalar core of the earlier spectral argument. |
| `identity_counterexample` | The nonzero identity operator is idempotent and satisfies the non-strict norm bound at one. Strictness cannot be dropped. |

The exact quantifiers and hypotheses are in the source. The projection theorems use a real normed space; a complex Hilbert space can be viewed as a real normed space, but the application to upstream objects is not formalized here.

## Reproduce

Use the pinned `lean-toolchain` and Lake manifest. From this result's `lean/` directory:

```sh
lake exe cache get Mathlib.Analysis.Normed.Operator.ContinuousLinearMap Mathlib.Analysis.SpecialFunctions.Exp Mathlib.Tactic.Linarith Mathlib.Tactic.Ring
lake env lean --trust=0 -j1 GapCriteria.lean
```

Run in an authorized workspace. For the owner's local host, keep the project, toolchain, `MATHLIB_CACHE_DIR`, temporary files, and dependencies on the external SSD as required by the agent prompt. No toolchain or build outputs are committed here. Fresh setup may require Lake to resolve the packages in the manifest before fetching the cache.

The actual run exited zero in approximately 16 seconds after dependencies were prepared. The [receipt](verification.json) gives the exact duration, source hashes, package revisions, and command. The Lean release archive SHA-256 matched the digest returned by GitHub's release API. The setup retrieved a subset of Mathlib's cache sufficient for the imports; it did not build the full upstream Yang–Mills project.

## Limits and missing obligations

The scalar lemma does not itself build a spectral measure, prove the integral lower bound, or connect the public energy-momentum PVM to the continuum Hamiltonian. The projection lemmas require uniform norm or approximation estimates. The [infrared cost audit](../2026-11-11-T03-infrared-cost-audit/README.md) describes a candidate way to supply those estimates and exactly what remains missing.

No theorem here proves that the actual Yang–Mills projection vanishes, verifies the original `MassGapTarget.lean`, or establishes a common positive mass in the continuum/infinite-volume construction. The original target remains uncompiled. Passing these generic checks must not be reported as full upstream or end-to-end verification.

## Development failures and lesson

The first elaboration rejected two proofs because an addition monotonicity lemma and a multiplication-cancellation lemma used different argument orientations than expected. Their proof terms were corrected without changing the mathematical statements. The successful final run contains no `sorryAx`; failed elaboration output is not proof evidence. The development logs remain in the local runtime workspace and are not needed to reproduce the final source.

## Track contributions and next question

T02 now has checked scalar/projection components. T07 has a pinned environment and a successful bounded trust-zero check, while upstream replay remains open. T03 and T05 must supply actual infrared/approximation hypotheses. The next formal step is a measure-theoretic Laplace support theorem and an explicit connection to the upstream PVM; the next dynamical step is the preparation-cost estimate.

## Review history

Author/tool self-check only; independent review pending.
