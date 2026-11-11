# Single-link total-variation contraction fails for bare SU(2) at beta at least one

## Metadata and bounded question

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06. Outcome: obstruction to a specific mixing criterion, not to a Yang–Mills mass gap.
- Evidence: written finite-volume argument, source inspection, exact integer geometry and rational arithmetic checks. No Lean formalization or independent review.
- Base: `aa07212fda80802c7ad125f06cdcf60db98cda35`; upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`. [Provenance](provenance.json).
- Related: [terminal covariance](../../general/2026-11-11-T03-terminal-covariance/README.md), [strong-coupling theorem scope](../2026-11-11-T04-strong-coupling-scope/README.md).

Can the missing coarse-measure mixing estimate be obtained by a uniform, single-link Dobrushin contraction close to the bare Wilson law? Before attempting an upper bound, test whether the exact influence coefficients can be below the required threshold. The falsification criterion is a row sum exceeding one. The experiment uses only a small finite geometry enumeration and rational arithmetic; no dependency download or simulation is needed.

The written result below is specific to the **unfixed SU(2) Wilson law in its fundamental representation**, four dimensions, a periodic side length at least three, once-per-plaquette counting, and $\beta\geq1$. It does not describe every generated coarse action, other gauge groups, or a gauge-fixed specification.

## Criterion and normalization

Write the bare law as

$$
d\mu_\beta(U)=Z_\beta^{-1}\exp\!\left(\beta\sum_p\tfrac12\mathrm{Re}\,\mathrm{Tr}(U_p)\right)\prod_e dH(U_e),
$$

where $H$ is probability Haar measure on $SU(2)$. The constant in the Wilson energy cancels upon normalization. This matches [`PublicWilson.wilsonEnergy`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean#L25), [`Gauge.price`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Gauge/MatrixGroup.lean#L112), and [`Wilson.bare`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Wilson/Law.lean#L58) for this representation.

Let $\gamma_e(\cdot\mid\eta)$ be the canonical continuous single-link conditional law. Define

$$
c_{ef}=\sup_{\eta,\xi:\,\eta_g=\xi_g\ (g\ne f)}
\|\gamma_e(\cdot\mid\eta)-\gamma_e(\cdot\mid\xi)\|_{\rm TV},\qquad c_{ee}=0,
$$

with $\|\nu-\rho\|_{\rm TV}=\sup_A|\nu(A)-\rho(A)|$. This is the convention in [Paulin–Mackey–Tropp, Definition 5.1](https://tropp.caltech.edu/reports/PMT14-Deriving-Matrix-TR.pdf#page=13). The row-sum contraction test requires $\max_e\sum_f c_{ef}<1$. Failure of this sufficient test does **not** imply failure of spatial mixing. An arbitrary upper estimate above one would not establish failure of the test; the argument here bounds the exact coefficients **from below**.

## Boundary configurations producing a lower bound

Fix a positive-axis link $e$. Exactly six plaquettes contain it. Removing $e$ from their boundaries gives six three-link staples whose 18 links are all distinct when the torus side is at least three. For an edge in direction $\mu$, these staples are indexed by $\nu\ne\mu$ and the two offsets $\pm\nu$. Their opposite parallel links and transverse endpoint links are distinct. This also shows there are no additional plaquettes involving $e$.

For any one of those 18 neighbors $f$, set all boundary links to central matrices $\pm I$. Make the staple containing $f$ positive, two of the other five staples negative, and the remaining three positive. Disjointness lets us realize these choices by changing one link in each negative staple. All unspecified links may be $I$.

The sum of the six staple matrices is then $2I$. Flip just $f$ to its negative. Its staple changes from $I$ to $-I$, leaving the staple sum zero. No other staple containing $e$ changes. Plaquettes not containing $e$ contribute only a factor that cancels from the conditional density. Orientations cause no ambiguity: the boundary matrices are central and self-inverse, and $\mathrm{Re}\,\mathrm{Tr}(U^{-1})=\mathrm{Re}\,\mathrm{Tr}(U)$.

Put $x(U)=\tfrac12\mathrm{Re}\,\mathrm{Tr}(U)$. The two conditional laws are exactly

$$
d\nu_{2\beta}(U)=\frac{e^{2\beta x(U)}}{Z(2\beta)}dH(U),\qquad d\nu_0(U)=dH(U),
\qquad Z(h)=\int e^{hx(U)}dH(U).
$$

Thus every one of these neighbors satisfies $c_{ef}\geq\|\nu_{2\beta}-H\|_{\rm TV}$. The boundary pair can depend on $f$, as allowed by the separate suprema. These are valid configurations of the unfixed product-link theory, without any plaquette constraint imposed on the links. The density is strictly positive and the conditional laws are continuous, so neighborhoods of these witnesses also preclude evading the lower bound by discarding isolated null configurations.

## An analytic bound without quadrature

Identify $SU(2)$ with unit quaternions. Haar is uniform measure on $S^3$ and $x$ is one real coordinate. Symmetry and $\sum_{i=0}^3 x_i^2=1$ give

$$
|x|\leq1,\qquad \mathbb E_Hx=0,\qquad \mathbb E_Hx^2=\tfrac14.
$$

Let $m(h)=\mathbb E_{\nu_h}x$. Differentiation under the integral is valid on bounded $h$-intervals because $|x|\leq1$. It gives $m'(h)=\mathrm{Var}_{\nu_h}(x)\geq0$. Consequently, for $\beta\geq1$,

$$
m(2\beta)\geq m(2)
=\frac{\mathbb E_H[x\sinh(2x)]}{\mathbb E_H[\cosh(2x)]}
\geq\frac{2\mathbb E_Hx^2}{\cosh 2}
=\frac1{2\cosh2}>\frac18.
$$

Here $x\sinh(2x)\geq2x^2$ for all real $x$, and $\cosh2<4$. For an exact bound on the last constant, the first three terms of the series sum to $11/3$. Starting at the $n=3$ term, the ratio to the next term is at most $1/14$. Hence

$$
\cosh2\leq\frac{11}{3}+\frac{4/45}{1-1/14}
=\frac{2201}{585}<4.
$$

The bounded test function $x\in[-1,1]$ obeys $|\mathbb E_\nu x-\mathbb E_\rho x|\leq2\|\nu-\rho\|_{\rm TV}$. Therefore

$$
c_{ef}\geq\frac1{4\cosh2}\geq\frac{585}{8804}>\frac1{16},\qquad
\boxed{\sum_f c_{ef}\geq\frac{5265}{4402}>\frac98>1.}
$$

This holds for every row, all $\beta\geq1$, and every periodic side length at least three. No numerical integration is used. Positive site weights cannot repair this particular contraction test on a finite torus: choose a link $e$ of minimal weight $w_e>0$. Then $\sum_f c_{ef}w_f/w_e\geq\sum_f c_{ef}>1$.

## Stability and the exact connection to the selected history

There is a limited robustness statement. If another measure has canonical single-link kernels $\widetilde\gamma_e$ satisfying

$$
\sup_{e,\eta}\|\widetilde\gamma_e(\cdot\mid\eta)-\gamma_e(\cdot\mid\eta)\|_{\rm TV}\leq\varepsilon,
$$

then the same boundary witnesses and the triangle inequality give $\widetilde c_{ef}>1/16-2\varepsilon$ on the 18 neighbors. Its row sum is greater than $9/8-36\varepsilon$, and still exceeds one when $\varepsilon\leq1/288$. This is conditional on a **uniform conditional-law** comparison; small activities or an informal closeness of actions do not establish that comparison.

For the upstream [`History.Selected`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L234), `starts` and `reaches` imply that the $N=0$ coarse endpoint is exactly bare at $\beta=\mathrm{bar}>1$. `Fits.sizeT` ensures a side length exceeding the small-torus exclusions above. Thus this single-link criterion cannot hold for **all** $P_{0,N,p}$ including $N=0$, in the SU(2) fundamental case. Separately, the bare fine-cutoff laws eventually have $\beta\geq1$ along the running family, so the same criterion fails there too; see the earlier coupling audit.

Discarding $N=0$ is allowed when proving a continuum limit. **The calculation does not show that the generated coarse laws for large $N$ fail the test.** Their reference actions and activities must be analyzed separately. No required conditional-law comparison for them has been derived. In particular, knowing their scalar `bar` is insufficient to apply this obstruction, just as it was insufficient to invoke a bare-law mixing theorem.

## Reproduction and evidence limits

From the repository root:

```sh
python3 auto-research/negative-results/2026-11-11-T03-single-link-influence/check_influence.py
```

[The script](check_influence.py) enumerates plaquettes for side lengths 3, 4, and 5 and every edge direction at the origin; translation handles the other positions in those examples. It verifies distinct staple links, all 216 boundary pairs, staple sums $2I$ and zero, and the exact rational constants. [Output](influence-check.json) and [receipt](verification.json) record Python 3.9.6, standard-library-only execution, exit zero, and 0.037 seconds. The source and output hashes are retained. The arbitrary-volume geometry, Haar identification, differentiation, and total-variation arguments are written above; they were not checked by Lean. The finite enumeration alone does not prove the all-volume claim.

This is an elementary route audit with no novelty claim, not a new mass-gap estimate. No independent upstream replay, independent mathematical review, or analysis of all generated interactions was completed.

## Failure lesson and next attempt

The failed inference is that a sharper upper bound on the same single-link influence coefficients must eventually yield contraction. Here explicit conditional laws already force the exact coefficients above threshold. Always distinguish a failed sufficient upper estimate from a proved lower obstruction, and keep the configuration space and metric explicit. Neither proves an absence of physical mixing.

The next bounded target is a criterion for gauge-invariant block observables or for the actual large-$N$ coarse measures, retaining their complete interactions. Success requires an explicit contraction/decay estimate with a positive physical rate and quantitative localization of the transported insertions. Gauge fixing, integration of additional links, a different metric, or a larger block changes the criterion and is not excluded by this result; each needs a new argument. A single-link route can be reopened if the actual coarse kernels are shown to differ sufficiently from this bare comparison and satisfy a contraction estimate on their own merits.

Review status: awaiting independent review. No Yang–Mills mass gap proved.
