# Pointwise Bakry–Émery curvature is negative on typical Wilson configurations

## Metadata

- Result ID and date: `2026-11-14-T03-typical-curvature`; 2026-11-14.
- Author: Rohan Arun, with Claude (Anthropic) assistance in a Claude Code session.
- Tracks: T03-D primary; T04 and T06 related.
- Outcome: **negative result for three untried variants of the geometric route.** (1) A probabilistic version of the curvature argument ("positive curvature on typical configurations, with the atypical set controlled separately") fails at the coupling range that matters. (2) Restricting to directions orthogonal to the gauge orbits does not repair it: the compressed horizontal matrix is also negative for $\beta\geq0.5$ (see the addendum). (3) The true quotient curvature, including the O'Neill and orbit-volume terms (Addendum 2), is also negative for $\beta\gtrsim0.5$ in four dimensions ($3^4$) and $\beta\gtrsim1$ in three dimensions. No mass-gap estimate.
- Evidence: Monte Carlo and floating-point linear algebra on $3^4$ and $4^4$ tori. Exact Hessian, validated against finite differences. No proof, no Lean, no independent review.
- Repository base commit: `ff784a0`.
- Toolchain: Python 3.9.6, numpy 2.0.2, scipy 1.13.1.
- Builds on: [curvature scope](../2026-11-12-T03-bakry-emery-scope/README.md), which bounded the worst case. This record measures the typical case.

## Question and claim tested

The earlier scope result shows the Bakry–Émery condition holds for every configuration only when $\beta<1/[4(d-1)]$. It left open whether the curvature is positive for *typical* configurations at larger $\beta$, in which case a probabilistic argument (curvature on a high-probability set plus control of its complement) would reach further.

Setting: bare SU(2) Wilson measure $\exp(\beta\sum_p\mathrm{Re}\,U_p)$, $\mathrm{Re}\,U_p=1-\mathrm{price}$, $d=4$, periodic $L^4$ torus; repository $\beta$ equals the usual $\beta_{\rm std}$. Each link carries the round unit $S^3$ ($\mathrm{Ric}=2$). For sampled configurations $U$ compute the lowest eigenvalues of the matrix $\mathrm{BE}(U)=2I+\beta\,\mathrm{Hess}\sum_p\mathrm{price}$.

Tested claim: $\lambda_{\min}\mathrm{BE}(U)\geq\rho>0$ for typical $U$, uniformly in $\beta$.

Falsification: typical $\lambda_{\min}$ at or below zero in the coupling range of interest.

## Method

- Metropolis sampling, 150 thermalization sweeps, 15 sweeps between samples, 3 hits per link, Gaussian Lie-algebra proposals with width $\min(1.2,\,1.4/\sqrt{\beta|S|})$ ($S$ the staple sum). Cold start for $\beta\geq2$, hot start below. Seeds $1000+i$.
- The Hessian is assembled exactly from quaternion algebra (as in the scope record, now vectorized and sparse) and the lowest six eigenvalues come from ARPACK. Validation: the assembled Hessian agrees with Richardson-extrapolated finite differences to $9.9\times10^{-9}$ (relative) on a $3^3$ torus, and the staple differential matches to $3\times10^{-16}$.
- Sampler sanity check against known behaviour: mean plaquette $0.060,\,0.123$ at $\beta=0.25,\,0.5$ (strong-coupling expansion gives about $\beta/4$) and $0.871,\,0.901$ at $\beta=6,\,8$ (weak-coupling expansion about $1-3/(4\beta)$). This is not a precision test of equilibrium.

## Results ($4^4$ torus, six decorrelated samples per $\beta$; $3^4$ torus, eight samples)

| $\beta$ | mean plaquette | lowest eigenvalue of BE, mean ($4^4$) | worst sample ($4^4$) | $3^4$ mean | lowest eigenvalue of $\mathrm{Hess}$, mean ($4^4$) |
| --- | --- | --- | --- | --- | --- |
| 0.25 | 0.060 | −0.014 | −0.043 | −0.002 | −8.06 |
| 0.5 | 0.123 | −1.86 | −1.92 | −1.74 | −7.71 |
| 1 | 0.235 | −5.12 | −5.33 | −4.76 | −7.12 |
| 2 | 0.491 | −9.01 | −9.70 | −8.10 | −5.51 |
| 4 | 0.797 | −9.26 | −9.61 | −9.36 | −2.81 |
| 8 | 0.901 | −12.20 | −13.17 | −11.19 | −1.78 |

Full table with intermediate couplings and second-lowest eigenvalues in [out_L4.json](out_L4.json) and [out_L3.json](out_L3.json).

Observations, all at these sizes only:

1. **Negative everywhere above $\beta\approx0.25$.** The zero crossing is at about $\beta\approx0.25$ (where $2+\beta\lambda_{\min}(\mathrm{Hess})\approx2-0.25\times8$), about three times the analytic worst-case threshold $1/12$ and consistent with the earlier local-search estimate $\approx0.22$. At $\beta=0.5$ the minimum is already $-1.9$.
2. **Typical is almost as bad as the worst case.** The lowest Hessian eigenvalue of a typical configuration at $\beta=0.25$ is $-8.01$ on a $3^4$ torus, close to the lowest value found by adversarial search on the same torus in the scope record ($-8.9$). The negative direction is not rare.
3. **It is a band, not an outlier.** The second-lowest BE eigenvalue is nearly as negative as the lowest (e.g. $-11.7$ against $-12.2$ at $\beta=8$).
4. **It worsens with coupling.** $\lambda_{\min}\mathrm{BE}$ falls from $-1.9$ at $\beta=0.5$ to $-12.2$ at $\beta=8$, while the Hessian's own minimum shrinks only from $-7.7$ to $-1.8$, so $\beta\lambda_{\min}$ wins.
5. **Mild volume dependence.** $3^4$ and $4^4$ agree to about 10%, with $4^4$ slightly more negative at most couplings.

## Interpretation (hypothesis, not tested here)

At identity, $\mathrm{Hess}\sum_p\mathrm{price}$ is positive semidefinite (it is the lattice curl-curl operator), so the negative eigenvalues come from the deviation of $U_p$ from the identity. I expect the leading effect to be the non-abelian commutator term of the second variation of the Yang–Mills action in a fluctuating background field strength, the same structure behind the known negative modes of the Hessian in chromomagnetic backgrounds (Nielsen–Olesen type instabilities). That is a physics expectation recalled from the literature, not checked against sources or against these data; a clean scaling law of $\lambda_{\min}(\mathrm{Hess})$ with $\sqrt{1-\langle P\rangle}$ was **not** found (the ratio drifts from $-8$ to $-5.6$ between $\beta=1$ and $\beta=8$).

## What this rules out and what it does not

Rules out, at these sizes: a probabilistic Bakry–Émery argument for the bare Wilson measure that relies on positive curvature on typical configurations at $\beta\gtrsim0.3$. Since the notebook records the endpoint coupling $\mathrm{bar}>1$, the range that matters is covered.

Does not rule out: any non-pointwise geometric mechanism. Pointwise curvature is a sufficient condition for a Poincaré inequality, not a necessary one; the bare measure presumably has a gap at these couplings. The routes that remain untested here are a multiscale Bakry–Émery criterion applied to a fluctuation field after a Gaussian-type decomposition (the structure used for the sine-Gordon model in the work cited in the [posterior-curvature record](../../general/2026-11-13-T03-geometric-posterior-curvature/README.md) on its branch), curvature of a gauge-quotient metric, and curvature of the ground-state-weighted measure. None was attempted.

Not checked: infinite volume; larger tori; longer thermalization; other gauge groups; the generated coarse measures.

Triage note, an opinion rather than a result: I could not identify a mechanism by which an $E_8$ structure would enter a four-dimensional $SU(N)$ estimate. The exceptional four-dimensional lattice is $D_4$ (the Hurwitz quaternions), and $E_8$ reaches $SU(2)$ only through the McKay correspondence for the binary icosahedral subgroup, which gives a finite-group approximation rather than a new estimate. Symmetry of the spacetime lattice does not address the dynamical obstruction recorded elsewhere in this notebook.

## Reproduction

```sh
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_typical_curvature.py validate
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_typical_curvature.py run 4 0.25,0.5,1,1.5,2,2.5,3,4,6,8 6 150 15 out_L4.json
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_typical_curvature.py run 3 0.25,0.5,1,2,4,8 8 150 15 out_L3.json
```

The $4^4$ run took about 215 seconds on 10 parallel processes; the $3^4$ run was faster. [Receipt](verification.json). numpy printed spurious matmul warnings in the validation step; all reported values are finite and the finite-difference agreement is the check that matters.

## Addendum: are the negative directions gauge or physical?

Question: the full matrix includes gauge directions, which gauge-invariant observables do not see. Does the negative band disappear once they are projected out?

Method (script [check_horizontal_curvature.py](check_horizontal_curvature.py), which imports the sampler and Hessian above). At each sampled $U$ write tangent vectors as $\xi$ with $V=U\exp(\xi)$. An infinitesimal gauge transformation $\epsilon$ gives $\xi_e=\mathrm{Ad}(U_e^{-1})\epsilon_x-\epsilon_{x+\mu}$. The horizontal subspace is the orthogonal complement of these vectors in the product metric. The script reports (a) the lowest eigenvalues of the compressed matrix $Q_h^{T}(2I+\beta\,\mathrm{Hess})Q_h$, and (b) the gauge weight $\|Q_g^{T}v\|^2$ of the lowest eigenvectors $v$ of the full matrix.

Validation of the gauge map: the derivative of $\sum_p\mathrm{price}$ along gauge directions is $2\times10^{-8}$ (it must vanish); a finite gauge transformation changes it by $6\times10^{-14}$; the map agrees with the true infinitesimal gauge move to $8\times10^{-6}$; the map has full rank ($243$ of $243$ on $3^4$).

| $\beta$ | lowest BE, full ($4^4$) | lowest BE, horizontal ($4^4$) | horizontal, worst sample | $\beta\times$ horizontal $\lambda_{\min}(\mathrm{Hess})$ | gauge weight of lowest eigenvectors |
| --- | --- | --- | --- | --- | --- |
| 0.5 | −1.84 | −1.74 | −1.83 | −3.7 | 0.03 |
| 1 | −4.98 | −4.87 | −5.11 | −6.9 | 0.03 |
| 2 | −8.46 | −7.70 | −8.37 | −9.7 | 0.12 |
| 4 | −9.55 | −3.51 | −3.62 | −5.5 | 0.66 |
| 8 | −11.47 | −3.07 | −3.25 | −5.1 | 0.84 |

Four samples per coupling on $4^4$; the $3^4$ run (six samples, $\beta\in\{0.25,\dots,8\}$) agrees with the $4^4$ horizontal minimum to within $0.3$ at every common coupling ([horiz_L3.json](horiz_L3.json), [horiz_L4.json](horiz_L4.json)). At $\beta=0.25$ on $3^4$ the horizontal minimum is $+0.035$ (worst sample $-0.003$), the same threshold behaviour as before.

Observations:

1. **At $\beta\leq1$ the negative band is physical.** Less than 4% of the lowest eigenvectors lies in gauge directions and projecting them out changes the minimum by $0.1$–$0.2$.
2. **At $\beta\geq4$ the full matrix is dominated by gauge directions** (gauge weight $0.66$–$0.84$; the gauge block alone has minimum $-6.5$ at $\beta=8$). Removing them improves the minimum from $-11.5$ to $-3.1$, but it stays negative.
3. **The horizontal minimum appears to saturate at weak coupling.** The product $\beta\times\lambda_{\min}(\mathrm{Hess}|_h)$ is about $-5.5$ at $\beta=4$ and $-5.1$ at $\beta=8$ on $4^4$ (and $-5.5,-5.3$ on $3^4$): the Hessian's negative part shrinks like $1/\beta$, consistent with a correction of second order in the typical plaquette angle ($\theta^2\sim1/\beta$). Two couplings do not establish a limit, but if it holds, the compressed horizontal curvature tends to about $2-5\approx-3$, a bounded negative constant rather than a divergence.

What this does **not** settle: the compressed matrix is not the Ricci curvature of the quotient. For a Riemannian submersion O'Neill's formulas add a non-negative term built from the curvature of the connection, and gauge orbits are not totally geodesic, so the volume of the orbit also weights the quotient measure. I have not computed either. Both were computed afterwards (Addendum 2 below), which also corrects a heuristic originally stated here, that they would vanish at weak coupling. Orbit-space geometry in the literature (Singer; the work cited in the posterior-curvature record) concerns exactly these terms and was not consulted.

Reproduction:

```sh
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_horizontal_curvature.py validate
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_horizontal_curvature.py run 4 0.5,1,2,4,8 4 150 15 horiz_L4.json
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_horizontal_curvature.py run 3 0.25,0.5,1,2,4,8 6 150 15 horiz_L3.json
```

The $3^4$ run took about 22 seconds per coupling in parallel; the $4^4$ run several minutes. Receipt fields are in [verification.json](verification.json).

## Addendum 2: the quotient terms, computed

The first addendum left open the two terms that separate the compressed matrix from the Bakry–Émery matrix of the gauge quotient $B=M/\mathcal G$. They are now computed exactly, validated, and run on the sampled configurations. **The first addendum's heuristic that these terms vanish at weak coupling was wrong**; the conclusion it was meant to support nevertheless stands.

### What is computed

$M=(S^3)^E$ with the product round metric ($\mathrm{Ric}_M=2$), gauge map $G=G_1-G_2$ as above, and the quotient measure $e^{-\beta S}\,V\,d\mathrm{vol}_B$ with $V\propto\det(G^{T}G)^{1/2}$ the orbit volume. For a horizontal $X$:

$$
\mathrm{Ric}_B(X,X)+\mathrm{Hess}_B(\beta S-\log V)(X,X)
=2|X|^2+X^{T}(Q_1+Q_2)X+\beta X^{T}\mathrm{Hess}_MS\,X+X^{T}\mathrm{Hess}_M\psi\,X,
\qquad\psi=-\tfrac12\log\det(G^{T}G).
$$

- $\mathrm{Ric}_B(X,X)=\mathrm{Ric}_M(X,X)-\sum_{V}K_M(X,V)+3\sum_Y|A_XY|^2$, from O'Neill's formula $K_B=K_M+3|A_XY|^2$ for horizontal orthonormal $X,Y$, which does not require totally geodesic fibres. Vertical sectional curvatures give $Q_1$; the $A$-tensor gives $Q_2$.
- $S$ and $V$ are gauge invariant, so their Hessians on $B$ equal the compressed Hessians on $M$ at horizontal vectors.
- Closed forms, with $P=(G^{T}G)^{-1}$, $\Pi=GPG^{T}$, $\Pi_h=I-\Pi$ and $C_i$ the cross-product matrices: $Q_1=-\mathrm{blockdiag}_e(\mathrm{tr}\,\Pi_{ee}\,I-\Pi_{ee})$; $Q_2=3\sum_aB_a^{T}\Pi_hB_a$ with $B_a=\mathrm{blockdiag}_e[c_{a,e}]_\times$ and $c_a=(G_1+G_2)\epsilon_a$, $\epsilon=P^{1/2}$ (from $\nabla_XK_\epsilon=-\tfrac12\mathrm{ad}(X)(G_1+G_2)\epsilon$ for the gauge Killing fields $K_\epsilon$); and $\mathrm{Hess}\,\psi=T_1+T_2$ with $T_1,T_2$ given by contractions of $G_1PG^{T}$, $G_1PG_1^{T}$, $GPG_1^{T}$ in the script docstring.

### Validation (all in [quotient_validation.txt](quotient_validation.txt))

1. $\mathrm{Hess}\,\psi$ against Richardson-extrapolated finite differences of $-\tfrac12\log\det(G^{T}G)$ on a $3^3$ torus: worst relative error $8.7\times10^{-8}$.
2. The $A$-tensor on a lattice with distinct link endpoints ($d=2$, $L=3$): $\langle A_XY,V_a\rangle$ from a finite-difference derivative of the horizontal projector (with $\nabla_XY=dY(X)+\tfrac12[X,Y]$) against the closed form: worst relative error $2.1\times10^{-9}$ on components of size $1.6$–$2.7$.
3. The assembled $\mathrm{Ric}_B$ pieces against an independent computation of the Ricci tensor of the toy quotient (one site, two links, quotient by simultaneous conjugation, a three-dimensional orbit space whose metric is pushed forward from the invariants $\mathrm{Re}\,a,\mathrm{Re}\,b,\mathrm{Re}\,ab$): six points, three directions each, worst absolute difference $3.1\times10^{-5}$, with $Q_1\approx-1.2$ to $-2.1$ and $Q_2\approx0.007$ to $0.24$ in those comparisons.

### Results (6 thermalized samples per coupling; lowest eigenvalue on the horizontal space)

| $d$, $L$ | $\beta$ | compressed (Addendum 1) | full quotient, mean | full quotient, range over samples | $Q_1$ | $Q_2$ |
| --- | --- | --- | --- | --- | --- | --- |
| 4, 3 | 0.25 | 0.04 | **+1.29** | [+1.26, +1.36] | −0.50 | 1.75 |
| 4, 3 | 0.5 | −1.66 | −0.40 | [−0.54, −0.28] | −0.50 | 1.75 |
| 4, 3 | 1 | −4.57 | −3.32 | [−3.72, −2.85] | −0.50 | 1.75 |
| 4, 3 | 2 | −7.70 | −6.44 | [−7.82, −5.60] | −0.50 | 1.76 |
| 4, 3 | 4 | −3.80 | −2.50 | [−3.22, −1.40] | −0.51 | 1.84 |
| 4, 3 | 8 | −3.35 | −1.95 | [−2.73, −1.22] | −0.51 | 1.95 |
| 3, 3 | 0.5 | −0.99 | **+0.85** | [+0.71, +1.00] | −0.67 | 2.49 |
| 3, 4 | 0.5 | −1.12 | **+0.73** | [+0.57, +0.89] | −0.67 | 2.50 |
| 3, 3 | 1 | −3.30 | −1.45 | [−1.65, −0.85] | −0.67 | 2.49 |
| 3, 4 | 1 | −3.59 | −1.73 | [−2.31, −1.25] | −0.67 | 2.50 |
| 3, 3 | 8 | −4.20 | −2.16 | [−3.47, −1.30] | −0.68 | 2.90 |
| 3, 4 | 8 | −4.40 | −2.42 | [−3.14, −0.82] | −0.67 | 2.76 |

Full tables, including $\beta=1.5,3,6$ in four dimensions and $\beta=2,4$ in three, are in [quot_d4_L3.json](quot_d4_L3.json), [quot_d3_L3.json](quot_d3_L3.json) and [quot_d3_L4.json](quot_d3_L4.json).

Observations:

1. **The quotient terms act as an almost $\beta$-independent upward shift.** The net shift of the lowest eigenvalue is $+1.26$ in four dimensions and $+1.85$ in three, nearly constant from $\beta=0.25$ to $\beta=6$ and rising slightly at $\beta=8$. $Q_1\approx-2/d$ and $Q_2\approx1.75$ ($d=4$) or $2.5$ ($d=3$) vary little over the horizontal space.
2. **The orbit-volume term is negligible.** The eigenvalues of $\mathrm{Hess}\,\psi$ on the horizontal space stay within $\pm0.2$ in four dimensions ($\pm0.5$ in three at $\beta=8$).
3. **The sign threshold moves up, then stops.** Linear interpolation puts the zero crossing of the lowest eigenvalue at about $\beta\approx0.44$ ($d=4$, $L=3$; it was about $0.25$ before the quotient terms) and about $0.65$–$0.7$ ($d=3$). Every sample at $\beta\geq0.5$ ($d=4$) and $\beta\geq1$ ($d=3$) is negative; at $\beta=0.25$ ($d=4$) and $\beta=0.5$ ($d=3$) every sample is positive.
4. **At weak coupling the quotient curvature appears to settle at a negative constant** near $-2$ in four dimensions ($-2.5,-2.05,-1.95$ at $\beta=4,6,8$; the worst samples are up to about $0.8$ lower). Three couplings do not establish a limit.
5. **Volume makes it worse, not better.** In three dimensions $L=4$ is more negative than $L=3$ at $\beta\geq1$ (for example $-5.1$ against $-3.1$ at $\beta=4$), as expected for a minimum over more modes. The four-dimensional numbers are for $L=3$ only ($4^4$ would cost roughly 30 times more per sample and several gigabytes per process), so they are probably optimistic.
6. **The earlier heuristic failed.** I expected the $A$-tensor contribution to scale with plaquette field strength and vanish as $\beta\to\infty$. It does not: $Q_2$ is $1.75$–$1.95$ at every coupling in four dimensions, and I did not identify why. The correction is nonetheless a bounded constant, too small to change the sign above the threshold.

### What this establishes and what it does not

For the bare four-dimensional Wilson measure at $3^4$ and the three-dimensional measures at $3^3$ and $4^3$, the pointwise Bakry–Émery matrix of the **gauge quotient** (not only of the unfixed space) is negative on typical configurations for $\beta\gtrsim0.5$ ($d=4$) and $\beta\gtrsim1$ ($d=3$), in a band of directions. Since the notebook records the endpoint coupling $\mathrm{bar}>1$, this closes pointwise and probabilistic Bakry–Émery arguments on the quotient at the relevant couplings, at least at these volumes.

Not established: infinite volume (the volume trend is the wrong way); larger four-dimensional tori; the singular strata of the quotient (stabilizer-nontrivial configurations), where the quotient is not a manifold and the Bakry–Émery argument would need separate justification; and, as before, any non-pointwise geometric mechanism. Pointwise curvature is sufficient for a Poincaré inequality, not necessary.

Reproduction:

```sh
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_quotient_curvature.py validate
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_quotient_curvature.py run 3 0.25,0.5,1,1.5,2,3,4,6,8 6 150 15 quot_d4_L3.json 4
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_quotient_curvature.py run 3 0.5,1,2,4,8 6 150 15 quot_d3_L3.json 3
python3 auto-research/negative-results/2026-11-14-T03-typical-curvature/check_quotient_curvature.py run 4 0.5,1,2,4,8 6 150 15 quot_d3_L4.json 3
```

About nine seconds per sample on $3^4$ for the full quotient computation.

## Failure lesson

Pointwise convexity of the Wilson action's configuration space is not the mechanism behind spatial mixing at intermediate coupling: negative curvature directions are typical, not rare. Before building a probabilistic argument on a curvature bound, measure the typical spectrum.

## Track contributions and next experiment

- T03-D: the typical-configuration variant of the curvature route is closed at $\beta\gtrsim0.3$; the horizontal-compression variant is closed as well, and so is the true quotient curvature (O'Neill and orbit-volume terms computed in Addendum 2) for $\beta\gtrsim0.5$ ($d=4$, $L=3$).
- T06: a recorded scope result for the geometric family.

Next bounded experiment, if the geometric theme continues: every pointwise curvature variant tried here is negative at the relevant couplings, so what remains is non-pointwise. The most concrete candidate is a multiscale criterion (curvature of a fluctuation field after a Gaussian-type decomposition). **Correction (same day):** the published Bauerschmidt–Bodineau criterion is stated on a linear field space with a Gaussian covariance decomposition, and requires a lower bound on the Hessian of the renormalised potential uniform over all field configurations at every scale; I found no formulation for group-valued fields, so a lattice toy for SU(2) would not test that criterion. See the literature-scan record for what a faithful test would need. A useful outcome would be a multiscale constant that is positive and uniform in volume where the pointwise one is negative; the opposite outcome would close that route too. No code exists for it, so the cost is substantial.

## Review and correction history

- 2026-11-14: created. Single AI session, small samples, no independent review.
- 2026-11-14: addendum on gauge versus horizontal directions added to this record (same branch and PR). A first commit message and PR description announced the addendum before the README edit had been applied (an escape-sequence error in my edit script); corrected by the follow-up commit.
- 2026-11-14: Addendum 2 (quotient terms) added. It corrects a heuristic stated in Addendum 1: the O'Neill term does not vanish at weak coupling (about 1.75 in four dimensions at every coupling sampled). The Addendum 1 conclusion is unchanged.
