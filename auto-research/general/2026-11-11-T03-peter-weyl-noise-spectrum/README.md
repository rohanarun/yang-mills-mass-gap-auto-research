# Peter–Weyl spectrum of the one-step blocking noise for SU(2)

## Metadata

- Result ID and date: `2026-11-11-T03-peter-weyl-noise-spectrum`; 2026-11-11.
- Author: Rohan Arun, with Claude (Anthropic) assistance in a Claude Code session.
- Tracks: T03-B/C primary; T05 (observable families) and T06 (obstructions) related.
- Outcome: **conditional structural result plus a sharpened obstruction.** The noise half of one blocking step is diagonalized exactly on all square-integrable observables. It is shown to be *rate-neutral*: it can neither create nor destroy separation decay. **No spatial decay estimate and no Yang–Mills mass gap are obtained.**
- Evidence: written derivation from standard harmonic analysis (Schur, Peter–Weyl); exact rational enclosures by two independent routes; exact finite non-Abelian control. No Lean formalization, no upstream replay, no independent review.
- Repository base commit: `3699c4d41ed1bbd95d719976651bd75b979e8c18`.
- Upstream: `yang-mills-group/OpenAI-YM-20261028` at `3456e5e75cf8d4cd558955a5c7638fba2d68f464`. In this session only [`YM/RG/Block.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Block.lean) was re-read (definitions `penaltyWeight`, `penaltyZ`, `noise`, `density`). Everything else about the source is inherited from the [loop-transfer record](../2026-11-11-T03-loop-noise-transfer/README.md); see [provenance](provenance.json).
- Toolchain: Python 3.9.6, standard library only.
- Extends, does not supersede: [one-step loop transfer](../2026-11-11-T03-loop-noise-transfer/README.md), [perimeter is not separation](../../negative-results/2026-11-11-T03-perimeter-not-separation/README.md).

## Question and exact claim

The loop-transfer record handles simple fundamental loops on distinct links and leaves three items open: links used more than once, overlapping supports, and whether a better choice of observable could extract separation dependence from the noise. Question: what does the actual noise kernel do to an **arbitrary** observable?

Scope is the same as the earlier record: gauge group SU(2) with `price(g) = 1 - Re Tr(g)/2` in the fundamental representation, one step from level 1 to level 0 of a fixed selected history, $\kappa=\lambda\beta_1>0$. Nothing is asserted for other `Gauge` instances.

Falsification: a wrong Haar normalization, a wrong Bessel index, or a failure of the isotypic formula on an observable with repeated links would invalidate the result. The checker tests each.

## Derivation

### 1. Source form of the noise

`Block.lean` defines `noise β Q V` as the product over coarse links $b$ of `(penaltyZ β G)⁻¹ * penaltyWeight β (V b * (Q b)⁻¹)`, with `penaltyWeight β v = exp(-β * penalty * price v)`. Hence, conditionally on the fine field and tags, $V_b=N_bQ_b$ with independent $N_b$ of density $k_\kappa(g)=e^{\kappa x(g)}/Z(\kappa)$ against probability Haar measure, $x(g)=\mathrm{Tr}(g)/2$. For any bounded measurable $F$ on coarse configurations,

$$
\mathbb E[F(V)\mid U,t]=(T_\kappa F)(Q(U,t)),\qquad
(T_\kappa F)(Q)=\int F\big((N_bQ_b)_b\big)\prod_b k_\kappa(N_b)\,dH(N_b).
$$

$T_\kappa=\bigotimes_bK_b$ is a product of commuting single-link convolution operators.

### 2. Single-link eigenvalues

Let $\rho_j$ be the spin-$j$ irreducible representation, $j\in\tfrac12\mathbb N$, $d_j=2j+1$, character $\chi_j$. Since $k_\kappa$ is a class function, $\int\rho_j(g)k_\kappa(g)\,dH(g)$ commutes with $\rho_j$ and is scalar by Schur's lemma:

$$
\int\rho_j(g)k_\kappa(g)\,dH(g)=c_j(\kappa)I,\qquad
c_j(\kappa)=\frac1{d_j}\int\chi_jk_\kappa\,dH .
$$

With $x=\cos\theta$, Haar class measure $(2/\pi)\sin^2\theta\,d\theta$ and $\chi_j=\sin((2j+1)\theta)/\sin\theta$,

$$
\int\chi_je^{\kappa x}dH
=\frac1\pi\int_0^\pi\big[\cos(2j\theta)-\cos((2j+2)\theta)\big]e^{\kappa\cos\theta}d\theta
=I_{2j}(\kappa)-I_{2j+2}(\kappa)=\frac{2(2j+1)}{\kappa}I_{2j+1}(\kappa),
$$

using [DLMF 10.32.3](https://dlmf.nist.gov/10.32.E3) and the recurrence [DLMF 10.29.1](https://dlmf.nist.gov/10.29.E1). The case $j=0$ gives $Z(\kappa)=2I_1(\kappa)/\kappa$. Therefore

$$
\boxed{c_j(\kappa)=\frac{I_{2j+1}(\kappa)}{I_1(\kappa)}}
$$

and $c_{1/2}=I_2/I_1=a(\kappa)$ recovers the earlier coefficient. Because $k_\kappa(g^{-1})=k_\kappa(g)$ and $k_\kappa$ is real, the same scalar applies to $\rho_j(g^{-1})$, and $K$ is self-adjoint on $L^2(H)$. On a matrix coefficient $f(q)=\langle u,\rho_j(q)w\rangle$ one gets $Kf=c_jf$. By Peter–Weyl, $K$ is diagonal with eigenvalue $c_j$ on the $d_j^2$-dimensional spin-$j$ isotypic block.

Properties, for $\kappa>0$:

- $1=c_0>c_{1/2}>c_1>\dots>0$, since $\nu\mapsto I_\nu(\kappa)$ is positive and decreasing ([DLMF §10.37](https://dlmf.nist.gov/10.37)). **Cited, not re-proved here.**
- $c_j\leq a^{2j}$. This follows from the Turán-type inequality $I_\nu^2\geq I_{\nu-1}I_{\nu+1}$, which makes $I_{n+1}/I_n$ non-increasing in $n$ (Thiruvenkatachar–Nanjundiah 1951; see Baricz, *Bull. Aust. Math. Soc.* 82 (2010)). **Cited, not re-proved here**; the bibliographic details were recalled, not re-read, and should be confirmed by a reviewer. The checker confirms both properties at the sampled parameters only.

### 3. The full one-step noise spectrum

Decompose $F\in L^2(\prod_bH)$ as $F=\sum_{\mathbf j}F_{\mathbf j}$ over spin assignments $\mathbf j=(j_b)_b$, where $F_{\mathbf j}$ is the projection onto the tensor product of isotypic blocks. Then

$$
\boxed{T_\kappa F=\sum_{\mathbf j}\Big(\prod_bc_{j_b}(\kappa)\Big)F_{\mathbf j}.}
$$

Consequences:

1. **Repeated links are handled exactly.** A link traversed twice is not multiplied by $a^2$; its tensor square is decomposed first. Example: $\tfrac12\mathrm{Tr}(g^2)=(\chi_1(g)-1)/2$, so $\mathbb E[\tfrac12\mathrm{Tr}(N^2)]=(3c_1-1)/2$. A backtrack lies in the trivial sector and has eigenvalue one.
2. **Gauge invariance is preserved.** $K_b$ commutes with left and right translations, so $T_\kappa$ commutes with gauge transformations. Gauge-invariant elements of a single sector (spin-network functions) are eigenfunctions with eigenvalue $\prod_bc_{j_b}\leq a^{\sum_b2j_b}$. Their span is dense in the gauge-invariant continuous functions of finitely many links, so the noise half of the step is now known on a dense observable family, not only on simple loops.
3. **Overlap covariance is explicit.** For any bounded $F,G$, with $\rho(dU,t)=P_1(dU)L_U(t)$, the law of total covariance gives
$$
\mathrm{Cov}_{P_0}(F,G)=\mathrm{Cov}_\rho\big(T_\kappa F(Q),T_\kappa G(Q)\big)
+\mathbb E_\rho\big[\big(T_\kappa(FG)-T_\kappa F\cdot T_\kappa G\big)(Q)\big].
$$
The second term is the conditional output-noise covariance that the earlier record said must be retained. It is now computable sector by sector, and vanishes when $F,G$ depend on disjoint link sets, because $T_\kappa$ is then multiplicative on the product.

### 4. Rate-neutrality

Fix disjoint finite link sets $A,B$ and a spin cutoff $J$. Let $\mathcal P_J(A)$ be the finite-dimensional span of sectors on $A$ with all $j_b\leq J$. It is $T_\kappa$-invariant, and all eigenvalues are strictly positive, so $T_\kappa$ is a bijection of $\mathcal P_J(A)$. For $F\in\mathcal P_J(A)$, $G\in\mathcal P_J(B)$,

$$
\mathrm{Cov}_{P_0}(F,G)=\mathrm{Cov}_\rho\big(T_\kappa F(Q),T_\kappa G(Q)\big),\qquad
\mathrm{Cov}_\rho\big(F(Q),G(Q)\big)=\mathrm{Cov}_{P_0}\big(T_\kappa^{-1}F,T_\kappa^{-1}G\big).
$$

$T_\kappa$ is a sup-norm contraction. For the inverse, a function $f$ in the spin-$j$ block satisfies $f=d_j\chi_j*f$ and so $\|f\|_\infty\leq d_j\|f\|_2$; summing over sectors,

$$
\|T_\kappa^{-1}F\|_\infty\leq M_J(\kappa)^{|A|}\|F\|_\infty,\qquad
M_J(\kappa)=\sum_{j\leq J}\frac{d_j}{c_j(\kappa)} .
$$

**Statement.** Let $\varepsilon\geq0$. The bound $|\mathrm{Cov}_\rho(F(Q),G(Q))|\leq\varepsilon\|F\|_\infty\|G\|_\infty$ on $\mathcal P_J(A)\times\mathcal P_J(B)$ implies the same bound for $\mathrm{Cov}_{P_0}(F,G)$. Conversely the $P_0$ bound implies the $\rho$ bound with $\varepsilon$ replaced by $M_J^{|A|+|B|}\varepsilon$. The constants depend on $(\kappa,J,|A|,|B|)$ and not on the positions of $A$ and $B$.

So an exponential-in-separation bound holds for the coarse law on these classes **if and only if** it holds, at the same rate, for the prediction observables under $\rho$. The noise contributes prefactors only. $M_J$ grows without bound in $J$, so the equivalence is not uniform over the whole dense family; the spectral criterion in this project permits observable-dependent prefactors but not observable-dependent rates.

For vertex-disjoint supports, the tag factorization of the earlier record replaces $\mathrm{Cov}_\rho(T_\kappa F(Q),T_\kappa G(Q))$ by $\mathrm{Cov}_{P_1}(\overline{T_\kappa F},\overline{T_\kappa G})$ with $\overline\Phi(U)=\sum_tL_U(t)\Phi(Q(U,t))$. That step is inherited, not re-derived.

## Reproduction and evidence

From the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-peter-weyl-noise-spectrum/check_noise_spectrum.py
```

[Receipt](verification.json): exit 0, about 0.9 seconds. [Output](check-output.json).

1. **SU(2) coefficients**, $\kappa\in\{1/2,1,2,5,10,40\}$, $2j=0,\dots,6$. Route one encloses $I_{2j+1}/I_1$ from the positive series [DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2) with a geometric tail bound. Route two does not use Bessel functions: it expands $e^{\kappa x}$, uses the exact semicircle moments $(2/\pi)\int x^{2k}\sqrt{1-x^2}dx=\binom{2k}{k}/[(k+1)4^k]$, and integrates the Chebyshev polynomial $\chi_j=U_{2j}(x)$. All 42 pairs of enclosures intersect with widths below $10^{-12}$. Positivity, strict decrease in $j$, and $c_j\leq a^{2j}$ hold at every sample. Example: $c_1(1)\in[0.03922510451964,0.03922510451965]$.
2. **Twice-used link.** $\mathbb E[2x^2-1]$ computed from moments agrees with $(3c_1-1)/2$ and is separated from $a^2$ at every sample; at $\kappa=1$ the values are $-0.4411623\ldots$ and $0.0576930\ldots$.
3. **Finite non-Abelian control on $Q_8$**, noise weights $w^{\mathrm{Re}\,g}$ with $w=2,3$. Eigenvalues from the character table are $1,\tfrac1{17},\tfrac1{17},\tfrac1{17},\tfrac3{17}$ and $1,\tfrac17,\tfrac17,\tfrac17,\tfrac27$. For five two-link observables, including a link used twice, a commutator, and a product of overlapping observables, the directly enumerated transfer (64 noise pairs at each of 64 predictions) equals the isotypic formula exactly, and the isotypic projections sum back to the observable. The value $-7/17$ for the squared link at $w=2$ reproduces the earlier record. Disjoint links factorize; a shared link leaves noise covariance $76/289$.

The $Q_8$ control tests the group-theoretic mechanism on a different group. It is not a test of the SU(2) multi-link statement, which rests on the written argument.

## Outcome and limits

Established at the written level: the complete action of the actual noise kernel on observables, for fundamental SU(2), one step. This closes the three items listed in the question.

Not established:

- Any separation-dependent bound. Rate-neutrality says the noise half cannot supply one. All spatial information sits in the fine law $P_1$ and the prediction map $Q(U,t)$.
- Any statement about the prediction map. `Patch.predict` was not inspected in this session. $T_\kappa F\circ Q$ is not shown to lie in a class closed under a second step, so no iteration across RG levels is justified.
- Uniformity in $J$, physical units, continuum and volume limits, phase selection, or the heat-kernel pairing.
- Lean formalization, upstream replay, or independent review. The author of this record checked their own argument; that is not independent review.

Heuristic only, not used: for large $\kappa$, $c_j\approx e^{-2j(j+1)/\kappa}$, i.e. the noise resembles a heat kernel at time $1/\kappa$.

## Failure lesson or revised expectation

The earlier obstruction "perimeter is not separation" extends from simple loops to every observable: each noise eigenvalue depends only on the observable's own spin content. Do not search for a cleverer observable class to extract decay from the noise. Any proposed one-step contraction must be checked against the statement in section 4: if it does not use the fine law or the prediction map, it cannot depend on separation.

## Track contributions and next experiment

- T03: the noise half of the step is finished for SU(2). Remaining target is unchanged in substance but sharper in form: bound $\mathrm{Cov}_\rho(\Phi(Q),\Psi(Q))$ for $\Phi,\Psi$ in finite spin sectors on separated supports.
- T05: spin-network functions give a dense gauge-invariant family on which one step of noise is explicit. Density in the reconstructed Hilbert space is not addressed.
- T06: sharpened noise-only obstruction, above.

Concurrent work: the open pull request on branch `research/su2-predictor-average` (same base commit, different author session) proposes an exact bond-tag mean of the **fundamental** prediction, $A_c(M)$, equal to $M/|M|$ on the minimizing branch and to the connector mean $M=\sum_xw_xY_x$ on fallback. It was found after this record was drafted, was read only in summary, and is not verified or relied on here. The two records are complementary: that one treats the prediction half for spin $1/2$, this one the noise half for all spins. Both edit the same ledger lines, so whichever merges second needs a small rebase.

Next bounded task, conditional on that record surviving review: extend its bond-tag mean to the spin-$j$ sectors required by section 3. The expected form is $\rho_j(M/|M|)$ on the minimizing branch and $\sum_xw_x\rho_j(Y_x)$ on fallback, which for $j\geq1$ is not a function of $M$ alone. Success: a source-checked formula and the resulting read footprint for $\overline{T_\kappa F}$ with $F$ a spin network; or a documented reason the fallback branch leaves the finite-sector class. Cost: source reading of `Patch.lean` only. This still would not bound a covariance.

## Review and correction history

- 2026-11-11: created. No review yet.
