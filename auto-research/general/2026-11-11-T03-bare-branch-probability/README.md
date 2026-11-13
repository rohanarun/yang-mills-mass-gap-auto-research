# A volume-uniform bare Wilson bound for leaving the frame branch

## Metadata and scope

- Date: 2026-11-11; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03-B, T04, T07. Base: `ea4ac9dc28710fcfa86cd229a04ae19b967d4c9e`.
- Evidence: written derivation using pinned source definitions and an existing upstream theorem; finite geometry checks. **The new probability bound is not Lean-checked or independently reviewed.**
- Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Group/representation: SU(2), fundamental representation. Measure: the normalized **bare Wilson law**, not a generated coarse density, conditional posterior, or reconstructed phase.
- No novelty claim. The partition-function/convexity argument is elementary. The contribution is an explicit application to the source's frame-branch event, proposed for review.

## Question and written result

Can one bound an actual frame-branch failure probability without assuming a lower bound on the normalized density? For the bare law, yes, with a weak bound whose constants are independent of the total torus volume.

Let the periodic four-dimensional lattice have side n >= 3 and V = n^4 sites. Set

$$
S(U)=\sum_p \left(1-\tfrac12\mathrm{Re}\,\mathrm{Tr}(U_p)\right),
\qquad d\mu_\beta=Z_\beta^{-1}e^{-\beta S}\,d\nu,
$$

where the sum has 6V positively oriented faces and nu is product probability Haar measure over 4V links. This is the normalization in [`YM.Wilson.Law`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Wilson/Law.lean).

For beta >= 1 define

$$
B(\beta)=\min\left\{2,\frac{1+\log(8\beta)+\frac23\log(3\pi^3/8)}{\beta}\right\}.
$$

For a source patch of radius r, put

$$
N_r=6(2r)^2(2r+1)^2,\qquad
C_r=48(2r+1).
$$

For every positive frame cutoff epsilon, the proposed written bound is

$$
\mu_\beta(\neg\mathrm{usesMin})
\leq\min\left\{1,\frac{2C_r^2N_r^2}{\epsilon^2}B(\beta)\right\}.
\tag{1}
$$

Here `usesMin` is evaluated on the periodic lift at any patch origin, with `frame_cut = epsilon`. Other kernel fields do not enter this event. The result does not require identifying an opaque chosen kernel's cutoff with a numerical constant.

For fixed r and epsilon, the right side tends to zero as beta grows, uniformly in n. At practical parameter values it can equal the trivial upper bound 1. There is no dependence on separation between observables, hence no correlation decay conclusion.

## 1. A normalized one-plaquette estimate

Write an SU(2) element as a unit quaternion with polar angle theta. The source's normalized matrix chord equals 2 sin(theta/2), and its price equals 1 - cos(theta). Probability Haar measure gives the angular density (2/pi) sin(theta)^2 on [0, pi].

For 0 < delta <= 1, the angular cap theta <= delta has mass

$$
p_\delta=\frac2\pi\int_0^\delta\sin^2\theta\,d\theta
\geq\frac{8\delta^3}{3\pi^3}.
$$

This uses sin(theta) >= 2 theta/pi on [0, pi/2]. On the event that every link belongs to this cap, each link chord is at most delta. The chord triangle inequality bounds every plaquette chord by 4 delta, hence every plaquette price by 8 delta^2. Independence is used only for the product Haar prior, giving

$$
Z_\beta\geq p_\delta^{4V}\exp(-8\beta\delta^2\,6V).
\tag{2}
$$

All integrands are bounded on the finite compact configuration space. Thus f(beta) = log Z_beta is differentiable and convex, f(0) = 0, and f'(beta) = -E_beta S. The tangent inequality at beta yields

$$
\beta\mathbb E_\beta S\leq-\log Z_\beta.
\tag{3}
$$

Translation and signed-axis symmetry make all plaquette prices have the same expectation. The law-preserving symmetry is supplied by [`law_pull`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Wilson/Symmetry.lean#L93). Dividing (2)-(3) by 6V beta gives

$$
\mathbb E_\beta\mathrm{price}(U_p)
\leq8\delta^2+\frac{2}{3\beta}\log(1/p_\delta)
\leq8\delta^2+\frac{2}{3\beta}\log(3\pi^3/8)-\frac2\beta\log\delta.
$$

Take delta = (8 beta)^(-1/2), which is at most one in the stated regime. This minimizes the last displayed upper bound as a function of delta, and gives E_beta price(U_p) <= B(beta), using also price <= 2.

The volume cancellation is explicit. We did not divide an absolute large-field estimate by an unknown partition function. Nor did we assert that the all-links-small event itself is probable under the interacting law: it is only a lower-bound device for Z.

## 2. Curvature controls the source branch event

For a cover box X = [-r,r]^4, let F(U) be the sum of chords of all internal plaquettes. It is exactly `P.facesum U`, with N_r terms. It remains a sum with multiplicities if the box wraps around the torus.

Upstream [`YM.Axial.existence`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Pick.lean#L80) supplies a cover gauge in which the sum T of all internal positive-link chords obeys

$$
T\leq16(2r+1)F(U).
$$

This uses existence directly, not the value of `axial_factor` in a chosen kernel. The theorem belongs to the [previously replayed upstream branch closure](../2026-11-11-T03-upstream-branch-audit/README.md).

Every coordinate route between two points in X remains in X and uses each unoriented edge at most once. Its transport chord is therefore at most T, by the product triangle inequality and invariance under inversion. Each `via` in [`Patch.usesMin`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Patch.lean#L109) consists of three such routes: center to x, x to y, and y to center. Edges can occur in different routes; this is why the factor is 3T, not T. Consequently every chord tested by `usesMin` is at most

$$
3T\leq48(2r+1)F(U)=C_rF(U).
$$

These are closed-loop chords, invariant under the cover gauge. This also follows from [`Patch.min_gauged`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Branch/Transport.lean#L106). The gauge need not descend to the torus: it is only used to bound the original periodic lift's gauge-invariant loop tests. Thus

$$
C_rF(U)<\epsilon\ \Longrightarrow\ \mathrm{usesMin},\qquad
\{\neg\mathrm{usesMin}\}\subseteq\{F\geq\epsilon/C_r\}.
\tag{4}
$$

The strict branch inequality and non-strict bad-event threshold are intentional. For r = 0 all routes are empty and the branch always holds.

Measurability causes no extra hypothesis: each route chord is continuous in the finite configuration, and `usesMin` is a finite intersection of strict sublevel sets. F is a finite sum of continuous bounded functions.

## 3. From a curvature moment to probability

Pointwise Cauchy-Schwarz and `chord^2 = 2 price` give

$$
F^2\leq N_r\sum_{p\subset X}\mathrm{chord}(U_p)^2,
\qquad \mathbb E_\beta F^2\leq2N_r^2 B(\beta).
$$

No independence between plaquettes is assumed. Repeated torus faces in the lift have the same individual expectation, so wrapping causes no extra assumption. Markov's inequality applied to F^2 in (4) proves (1).

For a specified list of M patches of the same radius, the union bound multiplies the untruncated right side of (1) by M. This does not bound a bad cluster's connection probability across a large distance: there is no joint-defect or mixing estimate here.

## What this changes, and what it does not

This supplies a written bare-law answer to one previously open local probability question. It uses an existing upstream axial estimate; it is not a new frame uniqueness theorem or an exponential-decay theorem.

The following extensions remain unproved:

1. **Generated measures.** The fine input of a later RG step is generally not the bare Wilson law. Applying (1) there requires an actual comparison, curvature-moment estimate, or relative entropy bound for that law. Generated interactions and normalization cannot be discarded.
2. **Predictor branch.** Frame branch control alone does not estimate the connector event `usesBest` or control the remaining covariance.
3. **Growing patches and physical limits.** The untruncated bound grows like r^10/epsilon^2 for large r. A sufficient condition for its convergence to zero is r(beta)^10 log(beta)/(epsilon(beta)^2 beta) -> 0 (for r >= 1). No such relation is verified along the chosen hierarchy. Fixed physical size as the lattice spacing shrinks is not fixed r.
4. **Spatial decay.** Rare local defects alone do not prove exponential clustering. The smooth-sector covariance, defect connections, transported observables, and dense-state/reconstruction bridges remain open. An additive local approximation error is not an exponential separation estimate.

The inspected `CenteredCharge.lean` explicitly distinguishes its estimate from a uniform bound relative to the blocked Gaussian density. `FrameMin.minimizing_used` supplies a deterministic sufficient condition; `Psalm.Branches` supplies locality, gauge invariance, and openness. These inspected results are not by themselves normalized bad-event estimates. This is a selective source audit, not an assertion that no stronger upstream probability theorem exists.

## Reproduction and evidence boundaries

Run from the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-bare-branch-probability/check_geometry.py
```

The [script](check_geometry.py) exhausts coordinate routes in the radius-one four-dimensional box, checks internal face counts for radii zero through three, and checks scalar Haar-cap inequalities and convexity on finite toy Gibbs laws. [Output](checks.json) and [receipt](verification.json) record the execution. Finite checks do not prove the arbitrary-radius geometry, SU(2) integral inequalities, or the new source application; the written arguments above carry those claims. There is no simulation of Yang–Mills, no new Lean replay, and no independent review.

Next bounded task: seek an expectation bound for the same local curvature sum under the actual fine law entering a specified RG step. Equation (4) then converts it to frame-branch probability without redoing the geometric argument. Before extending the claim, record the density, scale, chosen cutoff, and all normalization factors. If that bridge fails, preserve the bare-law statement with its limited scope.

## Review history

2026-11-11: initial AI-assisted derivation proposed for review. Mathematical novelty unassessed; mass gap remains unproved.
