# Yang–Mills Mass Gap Auto-Research

An initial investigation of what additional estimate could establish a positive mass gap for the construction in [OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028).

**This repository does not prove the Yang–Mills mass gap.** It contains a standard conditional spectral argument, an explicit obstruction to inferring a gap from polynomial decay, and an uncompiled Lean specification for a stronger target.

## What is established here?

| Item | Status |
| --- | --- |
| Polynomial decay alone does not imply a spectral gap | Explicit scalar spectral example; its integrals were checked symbolically |
| A common exponential decay rate on a dense family implies a gap | Written proof using the spectral theorem; not formalized here |
| Positive mass gap for the upstream Yang–Mills construction | **Unproved** |
| Proposed Lean gap target | Definitions only; **not compiled** |
| Independent replay of upstream Lean proofs | **Not performed** |

The initial inspection uses upstream revision [`3456e5e`](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464). The upstream README explicitly leaves positive mass gap outside its claim. Its verification reports are not independent verification by this project.

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
\operatorname{spec}(H)\subseteq\{0\}\cup[m,\infty).
$$

This is a standard reduction. The unresolved mathematical work is to derive its exponential estimate from Yang–Mills dynamics with a rate that survives cutoff removal and infinite volume.

## Research target

A concrete intermediate target is strict contraction at a fixed physical Euclidean time:

$$
\left\|e^{-\tau H}\big|_{\Omega^\perp}\right\|\leq q<1,\qquad \tau>0.
$$

This would give a gap of at least $-\log(q)/\tau$. At continuum level it reformulates the gap; it does not supply a new proof. Its possible value is as a target for quantitative estimates before taking limits.

The remaining obligations include a common positive physical rate, the correct vacuum subtraction, control of both limiting operations, and a dense family of states. An estimate for only the stress-trace channel does not automatically cover the whole Hilbert space. An unselected phase average does not automatically imply the corresponding estimate for the selected phase.

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

## Attribution and contributions

Prepared by rohanarun with OpenAI Codex assistance. This is an independent research notebook, not an official OpenAI publication or an endorsement by upstream authors. Mathematical claims require independent review. The spectral criterion is standard and is not claimed as a novel theorem.

Corrections, independent Lean replay, specification review, and quantitative infrared estimates are welcome. Contributions should distinguish assumptions, source inspection, symbolic checks, kernel verification, and conclusions about Yang–Mills.

Licensed under [Apache-2.0](LICENSE). See [NOTICE](NOTICE) for upstream attribution.
