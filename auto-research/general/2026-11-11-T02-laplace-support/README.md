# Checked Laplace support theorem and criterion audit

## Result and scope

Date: 11 November 2026. Author: Rohan Arun with OpenAI Codex assistance. Tracks: T02, T03, T04, T05, T07. Outcome: a standard scalar spectral theorem formalized, plus an audit of a proposed conditional criterion. Evidence: author-run Lean 4.32.0 checks with `--trust=0 -j1`; [receipt](verification.json), [Laplace output](LaplaceSupport.log), and [criterion-audit output](CriterionAudit.log). All reported axiom dependencies are `propext`, `Classical.choice`, and `Quot.sound`.

**No Yang–Mills dynamical bound or mass gap is proved.** These are verified infrastructure and proof-obligation analysis. No mathematical novelty or independent review is claimed. The upstream Yang–Mills construction was not replayed and its proposed gap target remains uncompiled.

## Complete scalar support equivalence

For a finite positive Borel measure $\mu$ on the real line and a real threshold $m$, the [source](LaplaceSupport.lean) proves the equivalence between:

1. There is one finite $C\geq0$ such that, for every $t\geq0$, the heat integrand is integrable and
   $$\int e^{-tE}\,d\mu(E)\leq Ce^{-tm}.$$
2. $\mu(( -\infty,m))=0$.

The forward proof establishes the lower bound from every closed half-line, removes its mass using the exponential comparison, and exhausts the open threshold by rational endpoints. The converse supplies $C=\mu(\mathbb R)$ and proves integrability by domination. The endpoint is sharp: an atom at exactly $m$ is permitted, as checked by `threshold_atom_allowed`.

The formal theorem allows arbitrary real $m$ and the zero measure. A positive physical gap needs the additional condition $m>0$ and the appropriate nontrivial theory.

**Integrability is explicit.** Lean's Bochner integral is defined to be zero for nonintegrable functions; a bound on that value alone would be an unsound substitute for the analytic hypothesis. The reverse direction constructs integrability from the support condition, and the forward direction requires it at every relevant time.

## Bridge back to an energy window

`energy_window_zero_of_heat_bound` applies the theorem to the pushforward of a finite measure restricted to strictly positive energies under a measurable energy map. It concludes

$$\rho\{x:0<E(x)<m\}=0.$$

This handles removing the zero-energy part and pulling the scalar support conclusion back to the original measure space. It does not construct the Yang–Mills spectral measure, prove its exponential estimate, establish the necessary dense-state bridge, or identify its zero-energy projection with the vacuum. Those are distinct obligations.

## The approximation criterion is a reformulation

[CriterionAudit.lean](CriterionAudit.lean) proves that, for a contractive idempotent, existence of the previously advertised strict range-approximation bounds is **equivalent** to the operator being zero. In the reverse direction the range is zero and the bounds hold with the zero approximant.

This does not invalidate the criterion. It explains its logical strength: proposing the bound does not itself make progress toward proving it. It becomes useful only if the required approximation costs can be derived from independent Yang–Mills estimates. The source cost extraction remains an unverified analytic application of the upstream shell lemma, not a derived cost bound.

## Implication for limit arguments

The converse also clarifies the role of prefactors. If each cutoff measure already satisfies an exponential estimate with the same rate $m$, first apply the support theorem at that cutoff; the prefactor may then be replaced by that measure's total mass. A divergent initially chosen prefactor is therefore not, by itself, an obstruction to this support-first route. If the measures converge weakly, their common closed support $[m,\infty)$ is preserved; that standard weak-convergence step is a written observation here, **not** one of the Lean statements in this record.

One still needs the same positive rate, actual spectral measures, and a justified convergence theorem for the correct states and phase. This does not manufacture the missing rate or justify exchanging the upstream limits.

## Reproduce

Reuse the pinned formal project in [the earlier result](../2026-11-11-T02-uniform-projection-criterion/README.md). From its `lean/` directory, with Lean 4.32.0 and the pinned dependency manifest:

```sh
lake exe cache get Mathlib.Analysis.Normed.Operator.ContinuousLinearMap Mathlib.Analysis.SpecialFunctions.Exp Mathlib.Tactic.Linarith Mathlib.Tactic.Ring Mathlib.MeasureTheory.Integral.Bochner.Set
lake build GapCriteria
lake env lean --trust=0 -j1 -R ../../2026-11-11-T02-laplace-support ../../2026-11-11-T02-laplace-support/LaplaceSupport.lean
lake env lean --trust=0 -j1 -R ../../2026-11-11-T02-laplace-support ../../2026-11-11-T02-laplace-support/CriterionAudit.lean
```

The final checks exited zero in approximately 19 and 3 seconds after setup. The receipt records exact durations, hashes, package revisions, and commands. A deprecated-alias warning in the audit is preserved in the output; it did not prevent checking. No dependency trees or compiled caches are committed.

Earlier development checks rejected syntactic conversions of scalar products and interval membership; the statements were retained and the proof terms corrected. Only the final successful source/log pairs are proof evidence.

## What would make this a research contribution on the mass gap?

A newly derived nonperturbative estimate that applies to the actual Yang–Mills hierarchy and survives its limits, or a substantial independently reviewed result resolving a real obstruction, would change the mathematical status. Standard lemmas, source audits, and verified equivalences are useful but do not establish such novelty. A literature/library novelty review and independent verification would be required before presenting a paper as a new mathematical advance.

## Next contribution

T03 should prioritize deriving a cost or decay estimate from actual dynamics. T02/T05 can connect the checked energy-window statement to the upstream PVM and dense family. T04 should distinguish direct passage of heat bounds from support-first limit arguments. T07 still owes an upstream replay. Track progress by discharged obligations, not theorem counts.
