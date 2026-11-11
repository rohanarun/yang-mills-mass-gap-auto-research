# Initial spectral reduction and source inspection

## Metadata

- Date: 2026-11-11.
- Author: rohanarun with OpenAI Codex assistance; original investigation, now indexed for future agents.
- Primary track: [T02](../../tracks/T02-spectral-criterion.md). Related: T01, T05, T07.
- Outcome: conditional result and source audit.
- Evidence: written derivation and source inspection; no formalization or independent kernel replay.
- Historical artifact commit: [`7148938bfe2fd8e1e545db7ece41f24f8aa98e51`](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/tree/7148938bfe2fd8e1e545db7ece41f24f8aa98e51/research/mass-gap-20261111).
- Upstream revision and hashes: [provenance](../../../research/mass-gap-20261111/provenance.json).
- Upstream toolchain: Lean 4.32.0; not replayed. This indexing operation performs no new mathematical verification.

## Claim and evidence

For a nonnegative self-adjoint Hamiltonian with unique normalized vacuum, a common positive exponential decay rate for a dense family of vacuum-orthogonal states implies absence of spectrum in a positive interval above zero. The state-dependent prefactors need not be uniform. See the [full written proof](../../../research/mass-gap-20261111/FirstPass.txt).

The public upstream claim does not include a positive gap. The inspected internal source supplies polynomial heat decay, and its zero-energy projection/vacuum argument supplies potential interfaces for a future proof. Source inspection is not independent proof replay.

## Limits

The necessary exponential estimate has not been derived from Yang–Mills dynamics. The [Lean target](../../../research/mass-gap-20261111/MassGapTarget.lean) consists of uncompiled definitions. Its common-gap requirement across refinements is stronger than merely allowing separate gaps, and needs specification review. The conditional argument is standard and is not claimed as a novel theorem.

## Reproduction and next contribution

Read the pinned source statements and the complete derivation above. No command executed for this indexing entry proves the criterion in Lean. T01 should audit the target; T02 should formalize the criterion; T05 should identify the exact dense centered family; T07 should independently replay relevant upstream proofs with the pinned dependencies.

## Review history

No independent review recorded.
