# Actual-weight SU(2) cutoff audit and integrated endpoint approximation

## Metadata and bounded question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03-B/C, T04, T06.
- Base: `f43cf0d76f1cc90aff46006ddc112159abd9c0ca`, after merged [PR #1](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/1).
- Upstream: `yang-mills-group/OpenAI-YM-20261028`, pin `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: written characterization of the fundamental SU(2) predictor-uniqueness cutoff, a sharper truncation remainder, and a conditional integrated endpoint bound. No spatial decay or mass gap.
- Evidence: source inspection, written derivations, integer convolution certificates and rational finite checks. No Lean formalization, upstream replay, or independent review.
- Question: does the actual source weight, together with predictor uniqueness, force the strict margin needed by the preceding geometric approximation?
- Falsification: an incorrect convolution marginal, non-unit connector, or incorrect cutoff inequality would invalidate the argument. Checks are bounded, exact, and use Python's standard library.

This develops the [predictor-average record](../2026-11-11-T03-predictor-average/README.md). It concerns the fundamental representation of SU(2), not arbitrary source `Gauge` inputs. It is separate from the open [Peter–Weyl/spin-j work in PR #2](https://github.com/rohanarun/yang-mills-mass-gap-auto-research/pull/2); no conclusions from that unmerged work are needed here.

## 1. Zero and arbitrarily small means for the actual convolution weights

The source [Patch.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean) defines odd $L\geq3$, $J\geq4$, and weights $w_x$ as the distribution of the sum of $J$ independent uniform points in the four-dimensional integer box of radius $\lfloor L/2\rfloor$. The patch contains every such sum (`roll_sites`). [Box.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Lattice/Box.lean) defines that box as a product interval.

Fix one coordinate $x_1$ and set $\zeta=e^{2\pi i/L}$. A single roll has that coordinate uniform on $L$ consecutive integers, hence its mean character is zero. Independence of the rolls gives the exact identity

$$
\sum_x w_x\zeta^{x_1}
=\left(\frac1L\sum_{z=-(L-1)/2}^{(L-1)/2}\zeta^z\right)^J=0.
$$

The other three coordinates integrate to one. This uses the actual source convolution weights, not a substitute two-point distribution.

For any $r\in[0,1]$, define the unit-quaternion connector on the source patch by

$$
Y_x^{(r)}=
\left(r,\sqrt{1-r^2}\cos\frac{2\pi x_1}{L},
\sqrt{1-r^2}\sin\frac{2\pi x_1}{L},0\right).
$$

Its norm is one, and its weighted quaternion mean is exactly $M=rI$. Thus the source connector type admits zero means, arbitrarily small positive means, and means crossing every radial cutoff in $(0,1)$.

**Scope:** these are connector functions in the universal quantifier of `Branches.predictor_unique`. We have not proved that every such connector is produced by an actual fine configuration and its shared frame tags. That distinction does not affect the cutoff necessity below, but it does affect probabilistic conclusions about the physical fine law.

## 2. Exact cutoff characterization for the predictor condition

The prior derivation gives $\min_u\mathrm{bondCost}(Y,u)=1-|M|$. A nonzero $M$ has the unique minimizing unit quaternion $M/|M|$; at $M=0$ every unit quaternion is a minimizer. The active test is the strict inequality $1-|M|<c$, where $c=\mathrm{predictor\_cut}>0$.

For these source patches and fundamental SU(2),

$$
\bigl[\text{every active connector has a unique minimizing predictor}\bigr]
\quad\Longleftrightarrow\quad c\leq1.
$$

- If $c\leq1$, an active connector has $|M|>1-c\geq0$, so its mean is nonzero and its minimizer unique.
- If $c>1$, the actual-weight connector $Y^{(0)}$ above is active and all unit quaternions minimize, contradicting uniqueness.

Therefore a selected history satisfying the source branch obligations has $0<c\leq1$ in this specialization. This is an inference from the branch hypothesis and source definitions, not an independent proof that the entire history or all its branch obligations exist.

The condition does **not** imply $c<1$. At $c=1$, predictor uniqueness holds for every active connector, yet the connectors $Y^{(r)}$ with $r\downarrow0$ remain active. A strict uniform norm margin over all connectors is impossible at that endpoint. This does not construct or alter a complete selected history at $c=1$; the frame and other obligations remain separate.

The same family strengthens the earlier threshold example: for $0<c<1$, the exact mean $A_c(rI)$ jumps from $(1-c)I$ at equality to $I$ just above it, now using the source weights. The jump is still a statement on connector space, not a theorem that the actual physical fine law crosses the boundary with positive probability.

## 3. Sharper geometric remainder without the old prefactor

Retain the source mask and the preceding notation

$$
b_n=\binom{2n}{n}4^{-n},\qquad \delta=1-r^2,
\qquad A_{c,K}(M)=M\sum_{n=0}^K b_n\delta^n
$$

on the active branch; use $M$ on fallback. For $r>0$ on the active branch, the exact error is

$$
\tau_K(r)=r\sum_{n=K+1}^\infty b_n\delta^n.
$$

The recurrence $b_{n+1}/b_n=(2n+1)/(2n+2)$ makes the coefficients decreasing. Thus $b_{K+1+j}\leq b_j$ and

$$
\tau_K(r)
\leq r\delta^{K+1}\sum_{j=0}^\infty b_j\delta^j
=\delta^{K+1}.
$$

This improves the preceding $\delta^{K+1}/r$ estimate. For $0<c<1$, put $q=2c-c^2<1$; then

$$
\|A_c-A_{c,K}\|\leq q^{K+1},\qquad
\|\overline W_C-W_{C,K}\|_\infty\leq\ell_C q^{K+1}.
$$

The former factor $1/(1-c)$ is unnecessary. The covariance truncation error for two bounded real loop observables improves to $(\ell_C+\ell_D)q^{K+1}$ by the same Cauchy–Schwarz argument as in PR #1. These are approximation estimates in degree $K$, not spatial or imaginary-time decay estimates.

At $c=1$, every fixed $K$ has $\tau_K(r)\to1$ as $r\downarrow0$, so there is no uniform convergence over all active connectors. At $r=0$ the source uses fallback and the error is zero; the formula for $\tau_K$ is only used on $r>0$.

## 4. An integrated alternative at the endpoint

Let $R$ be a connector-mean norm under the actual probability law being used. In the loop application this law is the full fine-field probability $P_1(dU)$ times the normalized joint site-tag law $p_U(s)$; no independent-Haar law for the connectors is substituted. At $c=1$, define the truncation error to be zero on $R=0$.

For $k=K+1$,

$$
\mathbb E\tau_K(R)
\leq\mathbb E[1_{\{R>0\}}(1-R^2)^k]
\leq\mathbb E[1_{\{R>0\}}e^{-kR^2}].
$$

At each fixed probability law, dominated convergence implies that this expectation tends to zero, even if the law has an atom at zero. This gives no rate uniform in volume or cutoff.

A quantitative replacement would be the **additional** small-ball hypothesis

$$
\Pr(0<R\leq\varepsilon)\leq C\varepsilon^\alpha,
\quad 0<\varepsilon\leq1,\quad C\geq1,\quad\alpha>0.
$$

Extend that bound to $\varepsilon>1$ using probability at most one. Since $e^{-kR^2}=\int_R^\infty2kt e^{-kt^2}dt$, nonnegative Fubini and $u=kt^2$ give

$$
\mathbb E\tau_K(R)
\leq C\int_0^\infty2kt^{\alpha+1}e^{-kt^2}dt
=C\,\Gamma(1+\alpha/2)\,k^{-\alpha/2}.
$$

The last equality uses [Euler's Gamma integral](https://dlmf.nist.gov/5.2.E1). This is a standard probability calculation. The small-ball bound is **not proved for the actual fine-field/tag law**. Connector-space realizability, predictor uniqueness, and finite-cutoff positivity do not supply it with uniform constants.

Loop telescoping bounds the integrated loop error by the sum of the edge errors. For real observables bounded by one, the corresponding covariance replacement error is at most twice the sum of their integrated absolute errors, using $|G-\mathbb EG|\leq2$. These statements control approximation only. Correlations of the retained masked terms and their degree/support costs are still required for a mass-gap argument.

## 5. Exact controls and failure limits

From this repository root:

```sh
python3 auto-research/general/2026-11-11-T03-cutoff-endpoint/check_endpoint.py
```

[Receipt](verification.json): Python 3.9.6, standard library only, exit 0, 0.052 seconds. [Output](check-output.json) includes:

- Twelve exact one-coordinate convolution certificates: odd $L=3,5,7,9$, $J=4,5,6$. Each residue modulo $L$ occurs $L^{J-1}$ times, certifying the zero Fourier character. The code computes coordinate convolutions, not all four-dimensional configurations; the four-dimensional factorization is written above.
- 792 rational tests of the sharpened remainder, including $c=1$ and the strict branch boundary.
- Six exact integrations of the radial error against each of two illustrative distributions on $(0,1)$: uniform $R$ gives error $b_{K+1}$, while density $2r$ gives error $1/(2K+3)$. The code integrates the finite polynomial term by term and checks these formulas.

The last distributions are probability controls, not distributions derived from Yang–Mills. In particular, the density-$2r$ example has an exact quadratic small-ball bound yet only an algebraic truncation error. A small-ball estimate does not by itself restore geometric convergence in degree. See the [endpoint failure record](../../negative-results/2026-11-11-T03-cutoff-endpoint/README.md).

## Handoff and review

The predictor uniqueness audit now supplies $c\leq1$, but leaves the exact chosen kernel's strict margin unresolved. If the history uses $c=1$, target a uniform bound on the probability of small **nonzero** connector mean under the actual fine-field/site-tag law. Preserve shared frames and all generated interactions. Also bound the connected correlations of the masked truncated observables; neither small-ball control nor approximation convergence is a spatial mixing theorem.

Review status: written source application and exact finite controls by the current author/assistant; submitted through a new PR, with no automatic merge. No mathematical novelty, independent verification of the upstream construction, or mass-gap proof is claimed.
