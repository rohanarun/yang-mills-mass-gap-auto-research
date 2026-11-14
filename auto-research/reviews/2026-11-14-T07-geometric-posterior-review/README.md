# Numerical re-check of the geometric posterior-Hessian claims (PRs #11 and #12)

## Metadata

- Result ID and date: `2026-11-14-T07-geometric-posterior-review`; 2026-11-14.
- Reviewer: Claude (Anthropic) in a Claude Code session. The reviewed work was authored with OpenAI Codex assistance. That is a different AI system, but the same repository owner's workflow; **no human mathematician has reviewed either side**.
- Tracks: T07 primary; T03 and T06 related.
- Reviewed work, by exact commit:
  - [PR #11](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/11) at `5f41029f18f89695cb0867f612ca5ecd33985054`: posterior Hessian of the generated coarse law and a noise-only counterexample.
  - [PR #12](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/12) at `ac461fb132186393e184fb99aaf57773e5ced88a` (stacked on #11): a smooth mixture whose auxiliary Poincaré constant degrades with volume although the averaged curvature does not.
- Repository base of this review: `ff784a0ae4a886580dfb8e0c7aa4e9dac6ce94f6`.
- Outcome: **the four checkable claims reproduced; nothing in scope was refuted.** The review covers a small part of those PRs and does not review their source correspondence.
- Evidence level: independent floating-point re-computation from the README formulas. No Lean, no symbolic proof, no upstream replay.
- Toolchain: Python 3.9.6, numpy 2.0.2.

## What was and was not independent

I wrote the checker from the formulas displayed in the two READMEs and **did not read the authors' `check_geometry.py` or `check_average.py`**. The formulas, the choice of test cases, and the numerical methods are therefore my own. The reviewed READMEs were read in full for the checked claims only.

## Claims checked

| # | Claim (as stated in the reviewed PRs) | Result |
| --- | --- | --- |
| C1 | Single link, Haar prediction: posterior density of $x=\mathrm{Re}(Q^{-1}V)$ is $\propto e^{\kappa x}\sqrt{1-x^2}$, so $\mathbb E y_j^2=a/\kappa$ with $a=I_2/I_1$, and the two terms of the Hessian identity cancel exactly. | Reproduced for $\kappa\in\{0.5,1,3,10,40\}$ by 400-node Gauss–Chebyshev quadrature. Errors in $\mathbb E x-a$ and $\mathbb E y_j^2-a/\kappa$ are at most $3.4\times10^{-16}$ and $5.6\times10^{-17}$; the cancellation residual $\kappa a-\kappa^2\mathbb E y_j^2$ is at most $7.1\times10^{-15}$. |
| C2 | Identity (1): $\mathrm{Hess}\,S_{\rm eff}(\xi,\xi)=\kappa\sum_e\mathbb E_\pi x_e|\xi_e|^2-\kappa^2\mathrm{Var}_\pi(\sum_ey_e\cdot\xi_e)$ along product geodesics. | Reproduced on a finite latent mixture (3 coupled links, 9 atoms, $\kappa=1.7$, six random directions). Worst relative error against Richardson-extrapolated finite differences: $8.7\times10^{-10}$. In the first direction tested the covariance term is far from negligible ($\kappa^2\mathrm{Var}\approx3.35$ against a first term $\approx4.80$), so the check is not vacuous. |
| C3 | For $\rho=1+cW_p$, noise output is $1+bW_p$ with $b=ca^4$; along the stated geodesic $S_{\rm eff}''=-16b/(1-b)$; the unit-direction value is $2-4b/(1-b)$, and at $\kappa=10$, $c=3/4$ it is at most $-223378/389437\approx-0.5736$. | Reproduced. With $a(10)=0.854185308323681$, $b=0.399273$: Monte Carlo ($2\times10^6$ samples, three random $V$) agrees with $1+bW_p(V)$ within $1.3$ standard errors; numerical $S''=-10.63434$ against predicted $-10.63438$; unit-direction value $-0.6586$, below the claimed bound $-0.5736$ as required. |
| C4 | The mixture $f_n$ of #12 has $\mathrm{Var}(F_n)=\frac1{4n}+\frac{(n-1)b^2}{16n}$, Dirichlet energy $3/n$, hence $\lambda_n\leq48/[4+(n-1)b^2]\to0$. | Reproduced by exact quadrature for $b\in\{0.2,0.5,0.9\}$ and $n$ up to 625 using $g=nF_n$: my variance $n/4-nb^2/16+n^2b^2/16$ and energy $3n$ divide to the same expression. The Rayleigh quotient of $g$ grows linearly in $n$. |
| C5 | Per-link gradient identity $|\nabla_aW|^2=1-W^2$ (used by C4 and by #12's energy computation). | Reproduced for 40 random configurations, each of four orientation patterns in the plaquette word, worst error $1.5\times10^{-10}$. It is also immediate analytically: $W=\mathrm{Re}(q\,e^{s\xi})$ with $q$ a unit quaternion whose real part is $W$. |

## One failure of my own script

The first run of C2 failed its assertion. The cause was my tolerance, not the identity: a plain central difference at $h=2\times10^{-3}$ gave $1.450896$ against the formula's $1.450944$, and halving $h$ reduced the error by exactly four ($1.9\times10^{-4}$, $4.9\times10^{-5}$, $1.2\times10^{-5}$ for $h=4,2,1\times10^{-3}$), which is the signature of $O(h^2)$ truncation error. I switched to Richardson extrapolation instead of loosening the bound, and the comment in the script records this.

## References cited by #11

A delegated web-reading agent loaded the abstract pages. It read abstracts only, not full texts.

- arXiv:1907.12308, Bauerschmidt–Bodineau, *Log-Sobolev inequality for the continuum sine-Gordon model*, Comm. Pure Appl. Math. 74 (2021): the abstract states a multiscale generalisation of the Bakry–Émery criterion applied to the massive sine-Gordon model with $\beta<6\pi$. Matches the use in #11.
- arXiv:1809.06318, Moncrief–Marini–Maitra, *Orbit Space Curvature as a Source of Mass in Quantum Gauge Theory*: the abstract describes a Bakry–Émery Ricci tensor on the Yang–Mills orbit space computed from the ground-state wave functional. Matches the use in #11.
- Louis (1982), J. Roy. Statist. Soc. B 44(2) 226–233, DOI `10.1111/j.2517-6161.1982.tb01203.x`: exists. The accessible abstract describes recovering the observed information from complete-data quantities but the page showed no formula, so the missing-information identity itself was not confirmed from that source. It is also elementary to derive; C2 checks it numerically.

## Not reviewed

- Source correspondence: that the actual selected kernel gives $\Phi$ and $\rho$ as stated, the dominated-differentiation argument for smoothness despite branch masks, and the identification of $f$ with the history's normalized coarse density.
- The companion identity behind "averaged Bakry–Émery matrix at least $2I$" in #12, and the positivity of $\lambda_n$ at fixed $n$.
- The rational Bessel enclosure $a>17/20$ as a rigorous statement (checked only numerically: $a(10)=0.8542$).
- Gauge-quotient geometry, and whether the comparison laws are realizable by the actual prediction map. Both PRs say they are not claimed to be.
- Other open PRs, in particular #10 (curvature transfer with a Lean file) and #13.

## Outcome and limits

The algebra that the geometric reduction rests on is numerically sound in the tested cases. Two points matter for how the results are used.

1. The exact Hessian identity makes the missing input explicit: positive Bakry–Émery curvature of the generated coarse law is equivalent to controlling the posterior covariance $C_{ef}$ in identity (2) of #11, i.e. the same posterior correlations the [buffered-posterior record](../../general/2026-11-11-T03-buffered-posterior/README.md) isolates. The geometric route adds a formulation, not an estimate.
2. C3 and C4 are counterexamples to *inferences* (noise-only positivity; averaged curvature implying a volume-uniform gap) for comparison laws that are not shown to be realized by the construction. They do not bear on whether the actual construction has a gap.

This review does not make either PR's evidence independent: it re-checks algebra on toy and comparison models only.

## Reproduction

```sh
python3 auto-research/reviews/2026-11-14-T07-geometric-posterior-review/check_review.py
```

[Receipt](verification.json), [output](check-output.json). About 6.5 seconds, fixed seed `20261114`.

## Failure lesson

A finite-difference assertion that fails with exact $h^2$ scaling is a method error; check the scaling before suspecting the formula, and extrapolate rather than loosen.

## Track contributions and next experiment

- T07: first numerical re-check of the geometric posterior-Hessian algebra (scope above).
- Next bounded review task: source correspondence for #11 section 1 — confirm from `Block.lean`, `Transfer` and `partition_eq` that $f(V)=z_\kappa^{-M}Z(V)$ is the actual normalized coarse density, and that no $V$-dependence enters `Q`, `likelihood`, or the branch masks. Cost: source reading of three files, which are already in the local upstream checkout.

## Review and correction history

- 2026-11-14: created by a single AI session; no human review.
