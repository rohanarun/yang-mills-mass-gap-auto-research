# Spin-$j$ bond-tag prediction mean for SU(2) and a one-step closure audit

## Metadata

- Result ID and date: `2026-11-11-T03-spin-j-prediction-mean`; 2026-11-11.
- Author: Rohan Arun, with Claude (Anthropic) assistance in a Claude Code session.
- Tracks: T03-B/C primary; T05 and T06 related.
- Outcome: **one elementary SU(2) inequality and one structural source audit of a single blocking step. No spatial decay estimate and no Yang–Mills mass gap.**
- Evidence: written derivation; exact rational checker (integer spins only); source inspection at the pin by the author session; an AI cross-check commissioned by the same session (see review history). No Lean formalization, no upstream replay, no independent review.
- Repository base commit: `3699c4d41ed1bbd95d719976651bd75b979e8c18`, on top of the [noise-spectrum record](../2026-11-11-T03-peter-weyl-noise-spectrum/README.md).
- Upstream: `yang-mills-group/OpenAI-YM-20261028` at `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; files read are listed in [provenance](provenance.json).
- Toolchain: Python 3.9.6, standard library only.
- Related: the open pull request on `research/su2-predictor-average` treats the spin-$1/2$ case for edge-distinct loops. That record was read in summary only and is not relied on. The spin-$1/2$ case of section 3 below agrees with its stated bound $1-r$.

## Question and exact claim

The [noise-spectrum record](../2026-11-11-T03-peter-weyl-noise-spectrum/README.md) reduces one step of coarse-field expectations to expectations of finite-spin functions of the **prediction field** $Q(U,t)$. Question: what is the bond-tag average of a spin-$j$ function of one predicted link, how far is it from a linear function of fine Wilson lines, and where exactly does non-polynomial dependence on the fine field enter?

Standing assumptions, all needed:

- $G=$ SU(2) in its fundamental representation, identified with unit quaternions, so `price(g) = 1 - Re(g)`. The source `Gauge` is a general closed subgroup of a unitary group; this specialisation is made here, and no SU(2) `Gauge` instance was exhibited.
- The three `Patch.Branches` hypotheses `frame_unique`, `predictor_unique`, `axial_exists`. The source marks them "These hypotheses need proofs" and does not prove them. Measurability of the kernel rests on them, and without `axial_exists` the site-tag likelihood can sum to zero.
- `predictor_cut` $=c\leq1$ wherever the minimizer is written $M/r$. `KernelChoices` only assumes $c>0$.

Falsification: a wrong branch condition, a wrong constant in section 3, or a failure of the sector formula on a repeated link.

## Derivation

### 1. Predictor objective and branch condition

`Patch.lean` defines weights $w_x\geq0$ with $\sum_xw_x=1$ (`weight_sum`, `weight_nonneg`), `bondCost Y u = ∑ x, weight x * price (Y x * u⁻¹)`, `best Y` as a classical choice of minimizer, and `usesBest` as `bondCost Y (best Y) < predictor_cut`. For unit quaternions $\mathrm{Re}(Y_xu^{-1})=\langle Y_x,u\rangle_{\mathbb R^4}$, so with

$$
M=\sum_xw_xY_x,\qquad r=|M|\in[0,1],
$$

$\mathrm{bondCost}(Y,u)=1-\langle M,u\rangle$. Its minimum is $1-r$; the minimizer is unique and equal to $M/r$ exactly when $r>0$. Since `best` is some minimizer, **`usesBest` holds iff $1-r<c$**, with no uniqueness hypothesis. If $c>1$, connectors with $M=0$ are on this branch and `best` is arbitrary; $c\leq1$ excludes this.

### 2. Bond-tag average of any function of one predicted link

`predict` returns `best Y` for every tag on the `usesBest` branch, with mass `1/card Points` each, and returns `Y r` with mass `weight r` otherwise. For any function $\varphi$ on $G$,

$$
\sum_r\mathrm{predictorMass}(Y,r)\,\varphi(\mathrm{predict}(Y,r))=
\begin{cases}\varphi(\mathrm{best}\,Y),&1-r<c,\\[2pt]\sum_xw_x\varphi(Y_x),&1-r\geq c.\end{cases}
$$

With $\rho_j$ the spin-$j$ representation, define

$$
B_j(Y)=\begin{cases}\rho_j(\mathrm{best}\,Y),&1-r<c,\\ D_j(Y),&1-r\geq c,\end{cases}
\qquad D_j(Y)=\sum_xw_x\rho_j(Y_x).
$$

$D_{1/2}(Y)=M$. For $j\geq1$, $D_j$ is **not** a function of $M$. Integer $j$: weights $\tfrac12,\tfrac12$ on $\{1,-1\}$ give $D_j=I$, while weights $\tfrac14$ on $\{1,i,-1,-i\}$ give $(I+\rho_j(i))/2\neq I$; both have $M=0$. Half-integer $j\geq3/2$: that pair gives $D_j=0$ twice, so use $\{1,-1\}$ against weights $\tfrac13$ on the cube roots of unity $e^{2\pi ik/3}$, for which $D_j$ has eigenvalue one on the weights $m=\pm3/2$. So the spin-$1/2$ formula of the concurrent record does not extend by substituting $M$.

### 3. The minimizing branch is close to the linear form

**Claim.** For every weighted connector $Y$, every minimizer $u$ of `bondCost`, and every $j\in\tfrac12\mathbb N$,

$$
\boxed{\Big\|\rho_j(u)-\sum_xw_x\rho_j(Y_x)\Big\|_{\mathrm{op}}\leq(2j)^2\,(1-r).}
$$

Hence $\|B_j(Y)-D_j(Y)\|\leq4j^2(1-r)\,1_{\{1-r<c\}}\leq4j^2c$.

*Proof.* A minimizer satisfies $\langle M,u\rangle=r$, and equality in Cauchy–Schwarz forces $M=ru$. Put $g_x=u^{-1}Y_x$. Then $\sum_xw_xg_x=u^{-1}M=r$, a real scalar (also when $r=0$), and $\sum_xw_x|g_x-1|^2=\sum_xw_x\,2(1-\mathrm{Re}\,g_x)=2(1-r)$. Since $\rho_j(u)$ is unitary it suffices to bound $\|I-\sum_xw_x\rho_j(g_x)\|$. $\rho_j$ is unitarily equivalent to the restriction of $g^{\otimes n}$, $n=2j$, to the symmetric subspace of $(\mathbb C^2)^{\otimes n}$. The averaged operator $\sum_xw_xg_x^{\otimes n}-I$ preserves that subspace, so its restriction has norm at most its norm on the full tensor space; the individual terms below need not preserve it. Let $a_k$ be $g$ acting in the $k$-th factor; these are unitaries that commute because they act in different factors, with $\|a_k-1\|=|g-1|$. The quaternion-to-matrix map is real-linear, so $\sum_xw_x(g_x-I)=(r-1)I$ as matrices. Telescoping twice,

$$
\prod_{k=1}^na_k-1-\sum_{k=1}^n(a_k-1)=\sum_{l<k}(a_l-1)(a_k-1)\prod_{m>k}a_m,
$$

whose norm is at most $\binom n2|g-1|^2$. Averaging over $x$, the first-order term is $\sum_k\big(\sum_xw_x(g_x-1)\big)_k=-n(1-r)I$, and the remainder has norm at most $\binom n2\cdot2(1-r)$. Total: $n(1-r)+n(n-1)(1-r)=n^2(1-r)$. $\square$

Remarks.

- The constant cannot be lowered, though it is not attained: for the pair $e^{\pm ti}$ with equal weights and small $t>0$, $r=\cos t$ and the ratio is $(1-\cos2jt)/(1-\cos t)=\sin^2(jt)/\sin^2(t/2)\to4j^2$ as $t\to0$. For larger $t$ the norm is the maximum over weights $m$ of $1-\cos2mt$.
- Away from $r$ near one the bound is far from tight for $j\geq1$.
- At $j=1/2$ the bound is the identity $|M/r-M|=1-r$.
- The bound is only informative when $4j^2c<2$. For an observable multilinear in $n$ coarse links the error telescopes to at most $\sum_e4j_e^2c$, growing with the observable.
- It is a pointwise comparison with a fictitious kernel that uses the linear form everywhere. It is not a contraction or a correlation bound.

### 4. One-step formula with repeated links

`Block.lean` defines `likelihood U t` as the product over sites of `frameMass` times the product over coarse edges $e$ of `predictorMass (connector U t.1 e) (t.2 e)`, and `prediction U t e` reads only `t.2 e`. So, **conditional on the fine field $U$ and the site tags $s$**, the predicted links $Q_e$ are independent across edges. After averaging site tags, edges sharing a coarse site are correlated, because each connector uses the frames at both endpoints.

Let $F$ lie in one Peter–Weyl sector: $F(V)=\langle\Phi,\bigotimes_e\rho_{j_e}(V_e)\rangle$ for a fixed tensor $\Phi$, each coarse link appearing in exactly one factor, with reversed traversals entering as adjoints. Any polynomial observable is a finite sum of such terms, including loops that traverse a link several times; this reduction is standard Clebsch–Gordan theory and is cited, not re-proved. Combining with the noise eigenvalues $c_j(\kappa)=I_{2j+1}(\kappa)/I_1(\kappa)$ of the earlier record,

$$
\mathbb E\big[F(V)\,\big|\,U,s\big]=\Big(\prod_ec_{j_e}(\kappa)\Big)\Big\langle\Phi,\bigotimes_eB_{j_e}\big(Y_e(U,s)\big)\Big\rangle .
$$

Example: a loop $V_1V_2$ traversed twice has $\tfrac12\mathrm{Tr}((V_1V_2)^2)=(\chi_1(V_1V_2)-1)/2$, so its bond-tag mean is $(\mathrm{Tr}(B_1(Y_1)B_1(Y_2))-1)/2$, not the value obtained by squaring fundamental means.

### 5. Closure audit of one step (source inspection)

Read at the pin: `travel` is a path-ordered product of link variables with inverses on backward steps; `route` is a sequence of straight axis legs; `axial U (root, order) x` is `travel` along the route from the root to `x`; on the non-`usesMin` branch `frame x = (axial center)⁻¹ * axial x`; and `connector` is `frame_{e.1}(x) * travel(L straight steps) * frame_{e.1+step}(x)⁻¹`.

**Polynomial event.** If both endpoint sites of $e$ are on the axial (non-`usesMin`) branch and the bond is on fallback, then $\rho_j(Q_e)$ is a convex combination, weights $w_x$, of spin-$j$ open fine Wilson lines from the centre of one patch to the centre of the next.

**Closed loops.** Each such line runs centre → root → patch point → straight leg → root → centre, so it is gauge-covariant at the two centres and no frame cancellation is needed. On the event that every site and bond of an edge-distinct coarse loop $C$ is of this kind, $W_C(Q)$ averaged over bond tags is a convex combination of closed fine Wilson loops through the patch centres. The site-tag average then mixes these with the configuration-dependent weights `1/card eligible`.

**Which event is typical is not established.** `usesMin` and `usesBest` are small-deviation conditions, so one expects them to hold for smooth fine configurations and the polynomial event to be the rough, large-field one. That is a heuristic reading of the definitions, not a probability estimate under any measure.

**Footprint.** All reads for edge $e$ lie in the union of the two patches of radius $(J+3)L$ around its endpoint coarse sites, in cover (unwrapped) coordinates. `expandAt` wraps periodically, so in physical links this is volume-independent only when the coarse side exceeds $2J+6$; nothing in `StepData` enforces that.

**Non-polynomial dependence on $U$ found in the audited files:**

1. Branch indicators and masses: `usesMin` (an open condition on `chord`), membership in `eligible` (a closed condition), the reciprocal `1/card (eligible U)`, and `usesBest`.
2. The classical-choice minimizing frame `selected` on the `usesMin` branch.
3. The classical-choice predictor `best`, which is $M/r$ here and is controlled by section 3.

These compose: `usesBest` is a function of the connector, which depends on `selected` at a `usesMin` endpoint, and `usesMin` is decided per site, so an edge can have one endpoint of each kind. This list is one reading of the source, not a proof of completeness. Only item 3 is quantitatively controlled. The observable pullback used throughout is the adjoint of the source's `push` and is this record's construction, not a source definition.

**Not examined:** whether a fixed spin cutoff survives a step. Distinct line factors can traverse the same fine link, so fine-link spins can add; no closed class $\mathcal P_J$ is claimed.

## Reproduction and evidence

From the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-spin-j-prediction-mean/check_prediction_mean.py
```

[Receipt](verification.json): exit 0, about 2.2 seconds, fixed seed. [Output](check-output.json). Rational unit quaternions come from stereographic projection, so all arithmetic is exact.

- Cost identity $\mathrm{bondCost}=1-\langle M,u\rangle$ and $\langle M,u\rangle^2\leq|M|^2$: 200 of 200 families.
- $D_1$ not a function of $M$: the integer-spin pair gives diagonals $(1,1,1)$ and $(1,0,0)$ with $M=0$.
- Section 3 at $j=1$ and $j=2$: 360 of 360 families each, by an exact positive-definiteness test of $(4j^2\delta)^2H-E^{\top}HE$ with $\delta$ a rational lower bound for $1-r$. Spin 2 is realised on symmetric traceless matrices with its Gram matrix $H$.
- Sharpness at $j=1$: the ratio equals $2(1+\cos t)$ exactly, reaching $3.9999999996$.
- Repeated link: direct enumeration over bond tags equals the sector formula in 60 of 60 cases covering all four branch combinations; the fundamental-mean rule gives a different value.

Not covered by the exact checker: half-integer spins, the multi-site frame structure, anything about the source. A separate floating-point search (42,000 adversarial families and hill-climbing, $j\leq5/2$) run during the cross-check found maximum ratios $1,4,9,16,25$, consistent with section 3; its scripts were scratch files and are not in the repository.

## Outcome and limits

Established in writing: sections 1–4 for SU(2), one step, under the standing assumptions. Section 5 is a source audit by one reader.

Not established:

- Any covariance or separation bound. Items 1 and 2 of section 5 are uncontrolled, and nothing is known about how often each branch occurs under any measure.
- Closure of a finite-spin class, or any iteration across RG levels.
- The `Branches` hypotheses for any concrete patch and kernel.
- Lean formalization, upstream replay, independent review.

## Failure lesson or revised expectation

A formula for the fundamental prediction mean does not determine higher-spin means: decompose into sectors first, then average each sector. A small predictor cutoff controls only the predictor nonlinearity; the frame minimizer and the branch indicators are separate obligations.

## Track contributions and next experiment

- T03: with the noise record, the one-step map on finite-spin observables is explicit conditional on site tags. The remaining one-step obstacles are named: branch indicators, `1/card eligible`, and `selected`.
- T06: the spin-$1/2$ substitution $D_j\mapsto$ function of $M$ fails for $j\geq1$.

Next bounded task: on the `usesMin` branch, compare the minimizing frame `selected` with the normalised axial frame. Unverified sketch: `usesMin` makes every transported link in the axial frame lie within `frame_cut` in chord distance, so the minimal `score` is at most of order `frame_cut`$^2$; writing `selected` $=k\cdot$ axial with $k(\mathrm{centre})=1$, the score controls the average of $|k_x-k_y|^2$, and the centre row then gives $\mathrm{avg}_x|k_x-1|^2\lesssim|\mathrm{Points}|\cdot$`frame_cut`$^2$. If this survives, connectors on the typical branch are within an explicit, cutoff- and volume-independent distance of fine Wilson lines, by analogy with section 3. Success: a proved inequality with its constant, or a counterexample showing the factor $|\mathrm{Points}|$ or worse is unavoidable. Cost: written analysis and a small exact check. This still would not bound a covariance.

## Review and correction history

- 2026-11-11: drafted with a weaker constant $4j^2+2j(4j^2-1)/3$ obtained from a Hermitian/anti-Hermitian splitting.
- 2026-11-11, AI cross-check commissioned by the author session (four verifier agents with analysis, numeric, source, and review lenses, then a critic). **This is not independent review.** Outcome: sections 1–3 could not be refuted; the non-function-of-$M$ example was corrected for half-integer spins; `best` versus $M/r$, the $c\leq1$ assumption, the `Branches` hypotheses, the union-of-patches footprint, the cover-coordinate caveat, `1/card eligible`, and mixed endpoints were added; "exactly three mechanisms" was weakened. The numeric lens observed that the supremum looked like $4j^2$.
- 2026-11-11: the tensor telescoping proof of the sharp constant $4j^2$ replaced the weaker one. A second AI cross-check by the same session (one proof-reading agent, one numerical agent; again not independent review) then examined this proof. Neither refuted it. The proof reader confirmed each step by hand and asked for four expository additions, now applied. The numerical agent found no violation beyond rounding over about 3.9 million families for $j\leq4$, confirmed the telescoping identity for $n\leq6$, and corrected the sharpness formula to a small-$t$ statement. Their scripts were scratch files and are not in the repository.
