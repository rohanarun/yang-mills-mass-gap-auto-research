# Yang–Mills Mass Gap Auto-Research

An initial investigation of what additional estimate could establish a positive mass gap for the construction in [OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028).

**This repository does not prove the Yang–Mills mass gap.** It contains a standard conditional spectral argument, an explicit obstruction to inferring a gap from polynomial decay, and an uncompiled Lean specification for a stronger target.

## What is established here?

| Item | Status |
| --- | --- |
| Polynomial decay alone does not imply a spectral gap | Explicit scalar spectral example; its integrals were checked symbolically |
| A common exponential decay rate on a dense family implies a gap | Written full argument; scalar support and generic projection components checked; actual Yang–Mills/dense-state integration remains open |
| Positive mass gap for the upstream Yang–Mills construction | **Unproved** |
| Generic projection/Laplace tools | Six lemmas/controls checked with Lean 4.32.0 and `--trust=0`; [receipt](auto-research/general/2026-11-11-T02-uniform-projection-criterion/verification.json) |
| Scalar Laplace support equivalence | Checked with Lean 4.32.0 and `--trust=0`, including integrability and the energy-window pullback; [receipt](auto-research/general/2026-11-11-T02-laplace-support/verification.json) |
| Proposed Yang–Mills Lean gap target | Definitions only; **not compiled** |
| Independent replay of upstream Lean proofs | **Not performed** |

The initial inspection uses upstream revision [`3456e5e`](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464). The upstream README explicitly leaves positive mass gap outside its claim. Its verification reports are not independent verification by this project.

## Research progress — 11 November 2026

**Verified formal infrastructure; the Yang–Mills mass gap remains unproved.**

- [Six initial generic lemmas and controls](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md) passed Lean 4.32.0 with `--trust=0`, covering projection contraction and scalar exponential comparisons.
- The [new Laplace support theorem](auto-research/general/2026-11-11-T02-laplace-support/README.md) now checks the full finite-measure equivalence: an integrable exponential Laplace bound at rate `m` is equivalent to no measure below `m`. It also checks the sharp endpoint and the pullback to a positive-energy window. [Proof receipt](auto-research/general/2026-11-11-T02-laplace-support/verification.json).
- A [formal criterion audit](auto-research/general/2026-11-11-T02-laplace-support/CriterionAudit.lean) confirms that the proposed strict approximation condition is itself equivalent to a zero projection. The condition must be derived from independent dynamical estimates; simply proposing it does not resolve the gap.
- The [infrared source audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md) isolates the missing localization/adjoint-state cost. [Cyclicity alone does not supply it](auto-research/negative-results/2026-11-11-T06-cyclicity-cost/README.md), and a [cited strong-coupling lattice theorem does not directly cover the running continuum regime](auto-research/negative-results/2026-11-11-T04-strong-coupling-scope/README.md).
- A [variable-time refinement](auto-research/general/2026-11-11-T03-variable-time-average/README.md) improves the written localization cost from cubic to quadratic in the support radius. Lean checks the scalar optimization; the measure-rescaling bridge remains a written derivation. The estimate is still polynomial.
- Two further controls show why more dynamics is needed: a [massless local field](auto-research/negative-results/2026-11-11-T06-massless-locality/README.md) satisfies the relevant locality assumptions without a gap, and an [auxiliary block gap](auto-research/negative-results/2026-11-11-T03-auxiliary-resolvent-gap/README.md) need not control the retained modes. Exact scalar and matrix checks passed.

The checked declarations report only `propext`, `Classical.choice`, and `Quot.sound`. These results are publishable as a reproducible research notebook and formalization contribution; **no new Yang–Mills mass-gap theorem or mathematical novelty is claimed**. Independent review, a novelty assessment, full upstream replay, and the essential nonperturbative estimate remain outstanding. The next milestone is an estimate derived for the actual hierarchy that stays positive through the continuum and infinite-volume limits—not a larger count of generic lemmas.

## The starting point

The source theorem [`light_bound`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Light.lean#L221) bounds low-energy spectral weight for finite word states by a constant times the square of the energy threshold. The theorem [`inverse_square`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/EveryPhase/Decay.lean#L173) gives

$$
0\leq\langle\psi,(e^{-tH}-P_0)\psi\rangle\leq C_\psi t^{-2},\qquad t\geq1.
$$

Here $P_0$ is initially the full zero-energy projection. The upstream vacuum argument identifies that projection with the vacuum line. These are source-level observations, pending independent replay.

## Why polynomial decay is insufficient

Consider the finite positive measure

$$
d\mu(E)=Ee^{-E}\,dE,\qquad E>0.
$$

It satisfies

$$
\mu((0,u])=1-(1+u)e^{-u}\leq\frac{u^2}{2},\qquad
\int_0^\infty e^{-tE}\,d\mu(E)=\frac{1}{(1+t)^2}.
$$

Every interval $(0,u)$ nevertheless has positive measure. Thus quadratic control of low-energy weight and inverse-square heat decay allow spectral weight arbitrarily close to zero.

The notes realize this as a nonnegative self-adjoint operator with a unique zero-energy vacuum and no positive gap. **This is an obstruction to a spectral inference, not a counterexample to the full Yang–Mills construction.** It does not satisfy all of the upstream Wilson, field-theoretic, OPE, and trace requirements.

## The conditional route to a gap

Let $H\geq0$ be self-adjoint, with normalized vacuum $\Omega$ and $\ker H=\mathbb C\Omega$. Suppose a dense subset $D$ of $\Omega^\perp$ satisfies

$$
\exists m>0\;\;\forall\psi\in D\;\;\exists C_\psi\geq0\;\;\forall t\geq1:\quad
\langle\psi,e^{-tH}\psi\rangle\leq C_\psi e^{-mt}.
$$

The prefactor can depend on the state. **The positive rate must be common to the dense family.**

For $0<a<m$, spectral positivity gives

$$
e^{-at}\mu_\psi((0,a])\leq\langle\psi,e^{-tH}\psi\rangle
\leq C_\psi e^{-mt}.
$$

Taking $t\to\infty$ forces $\mu_\psi((0,a])=0$. Letting $a\uparrow m$, then using density and boundedness of spectral projections, gives $P((0,m))=0$ and

$$
\sigma(H)\subseteq\{0\}\cup[m,\infty).
$$

This is a standard reduction. The unresolved mathematical work is to derive its exponential estimate from Yang–Mills dynamics with a rate that survives cutoff removal and infinite volume.

## Research target

A concrete intermediate target is strict contraction at a fixed physical Euclidean time:

$$
\left\|e^{-\tau H}\big|_{\Omega^\perp}\right\|\leq q<1,\qquad \tau>0.
$$

This would give a gap of at least $-\log(q)/\tau$. At continuum level it reformulates the gap; it does not supply a new proof. Its possible value is as a target for quantitative estimates before taking limits.

The remaining obligations include a common positive physical rate, the correct vacuum subtraction, control of both limiting operations, and a dense family of states. An estimate for only the stress-trace channel does not automatically cover the whole Hilbert space. An unselected phase average does not automatically imply the corresponding estimate for the selected phase.

## Research workflow

Agents should start with [auto-research.md](auto-research.md), choose a research track, and record every investigation—including negative and inconclusive results—in [auto-research/](auto-research/README.md). Each result must update its track ledger with evidence, remaining assumptions, and a concrete next question. The prompt and archive do not launch a background job.

## Files

- [First-pass notes](research/mass-gap-20261111/FirstPass.txt): detailed argument, operator example, source locations, and remaining obligations.
- [Lean target](research/mass-gap-20261111/MassGapTarget.lean): proposed gap and strengthened existence definitions, with no proof asserted.
- [Symbolic check](research/mass-gap-20261111/check_obstruction.py): exact integral and asymptotic calculations for the scalar example.
- [Recorded output](research/mass-gap-20261111/obstruction-check.json): output from the symbolic check.
- [Provenance](research/mass-gap-20261111/provenance.json): upstream revision, source hashes, and verification status.

## Reproduce the symbolic check

With Python 3 and `venv` available, from this repository's root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python research/mass-gap-20261111/check_obstruction.py
```

The check verifies the total mass, low-energy integral, heat integral, and failure of every positive exponential decay rate for the scalar example. It does not verify the Yang–Mills construction or the spectral theorem argument in Lean.

`MassGapTarget.lean` imports `ChallengeSpec` from the pinned upstream project. This repository does not bundle that project's dependencies or provide a standalone Lean build. Upstream pins Lean **4.32.0**. The target remains uncompiled and also requires a mathematical review of its specification; it asks for a common gap per chosen Wilson family across volume refinements, a stronger requirement than a separate gap for each resulting hierarchy.

## Contributors

Contributions from people and AI-assisted researchers are welcome. Start with [auto-research.md](auto-research.md) and [CONTRIBUTING.md](CONTRIBUTING.md). Useful negative results, corrections, and independent reviews receive credit alongside positive results.

Snapshot: **11 November 2026**. Contribution state and mathematical verification are separate. Being on `main` does not establish a Yang–Mills mass gap.

| Work | Contributor | Contribution | Verification status | State |
| --- | --- | --- | --- | --- |
| [Initial investigation](research/mass-gap-20261111/FirstPass.txt) | [Rohan Arun (@rohanarun)](https://github.com/rohanarun), with OpenAI Codex assistance | Source inspection, standard conditional spectral criterion, and proposed gap specification | Written argument; Lean target uncompiled; upstream proofs not independently replayed | On main |
| [Polynomial-decay obstruction](auto-research/negative-results/2026-11-11-T06-polynomial-decay/README.md) | Rohan Arun, with OpenAI Codex assistance | Explicit scalar spectral example showing why polynomial decay alone does not imply a gap | Exact symbolic integral/asymptotic checks; not a counterexample to the full Yang–Mills construction | On main |
| [Research tracks and archive](auto-research.md) | Rohan Arun, with OpenAI Codex assistance | Seven research tracks, agent instructions, result template, and preservation of negative results | Documentation contribution; no mathematical verification implied | On main |
| [Conditional Lean tools](auto-research/general/2026-11-11-T02-uniform-projection-criterion/README.md) | Rohan Arun, with OpenAI Codex assistance | Five generic criteria and a non-strict-bound counterexample | Lean 4.32.0 trust-zero check passed; no YM application proved | On main |
| [Infrared source audit](auto-research/general/2026-11-11-T03-infrared-cost-audit/README.md) and related obstructions | Rohan Arun, with OpenAI Codex assistance | Extracted preparation costs, a cyclicity counterexample, and a coupling-regime comparison | Written/source-level analysis; coefficient algebra checked; independent review pending | On main |
| [Laplace support and criterion audit](auto-research/general/2026-11-11-T02-laplace-support/README.md) | Rohan Arun, with OpenAI Codex assistance | Finite-measure support equivalence, energy-window pullback, and criterion-strength audit | Lean 4.32.0 trust-zero checks passed; standard results, no new YM estimate | On main |
| [Time-average refinement and infrared controls](auto-research/general/2026-11-11-T03-variable-time-average/README.md) | Rohan Arun, with OpenAI Codex assistance | Written localization improvement, massless-field control, and auxiliary resolvent audit | Scalar optimization checked in Lean; scalar/matrix checks passed; no YM gap or independent review | On main |

[Full contributor credits](CONTRIBUTORS.md) record authorship, AI assistance, inherited work, and future contributions. Credits remain when results are corrected or superseded; their evidence status is updated.

The underlying construction is the work credited by [yang-mills-group/OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028). This repository is an independent project, not an official OpenAI publication or an endorsement by upstream authors. The spectral criterion is standard and is not claimed as a novel theorem.

## License

The original code and documentation in this repository are licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution. Referenced upstream work and external dependencies retain their own licenses and notices; this repository does not relicense them.
