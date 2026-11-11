# Gauge-invariant response: forest observations and the remaining loop problem

## Metadata and bounded question

- Date / author: 2026-11-11; Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03-B/D; T05 observable scope and T06 controls.
- Base: `d95fa752e993c81ce2e01008efb75862aaf39ab6`.
- Upstream: [OpenAI-YM-20261028](https://github.com/yang-mills-group/OpenAI-YM-20261028/tree/3456e5e75cf8d4cd558955a5c7638fba2d68f464), commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: a written symmetry reduction of the conditional-response target, with exact finite non-Abelian controls. No new spatial decay estimate or mass-gap theorem.
- Evidence: source inspection, self-contained written arguments, and Python integer/rational checks. No Lean formalization, upstream replay, or independent mathematical review.
- Bounded question: can the full-link posterior target be narrowed to gauge-invariant information before trying to derive spatial smallness?
- Falsification: failure of coarse gauge invariance, incorrect conditional normalization, or a finite counterexample to the forest identity would invalidate this application. Computation is limited to small finite-group enumerations, with no new dependencies.

The [buffered-posterior reduction](../2026-11-11-T03-buffered-posterior/README.md) bounds all output events. The physical task may need only a specified family of gauge-invariant observables. These are different demands. The result below removes gauge-only directions but leaves the dependence on physical loop data unbounded.

## 1. The actual coarse law is gauge invariant

Write the finite coarse law as $P(dV)=Z^{-1}v(V)d\mu(V)$, where $\mu$ is product probability Haar and $v$ is the selected history's full density, including generated interactions. Its invariance follows inductively from inspected source declarations:

- [Wilson/Law.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Wilson/Law.lean): `bare_gauge` gives gauge invariance at the finest endpoint.
- [Wilson/Symmetry.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Wilson/Symmetry.lean#L69): `prior_gauge` preserves the product Haar measure.
- [RG/History.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean): `BlockControl.gauge`, `Selected.starts`, and `Selected.steps` give the covariance of the integrated kernel and the exact density recurrence.
- [MULTISOURCE_TRAJECTORIES/Block.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Block.lean#L138): `invariant_push` transports invariance through a step. It lifts a coarse gauge transformation using the parent map; no independent gauge-covariance assertion for each hidden branch is required.
- [Signals.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Extra/MULTISOURCE_TRAJECTORIES/Signals.lean): `vac_smooth`, `vac_pos`, and `vac_eq` supply continuity, positivity, and equality with the selected density. `total_gauge` and `cumulant_gauge` give invariance of transported insertions under the explicit `Insertions.Symmetric` hypothesis. Normalized insertion ratios inherit invariance from numerator and vacuum denominator.

Thus this is an application to the marginalized physical coarse law. It does not assume that hidden tags transform separately in a way not established by the source. At finite volume the continuous density is bounded on a compact configuration space; its positive conditional denominators exist. None of this gives a uniform correlation length.

## 2. Exact forest-conditioning identity

Let $P$ be any gauge-invariant probability law on links of a finite graph with compact group $G$. Choose one orientation for each independent edge and use

$$
(gV)_{xy}=g_xV_{xy}g_y^{-1}.
$$

Let $T$ be a set of edges whose underlying undirected graph is a forest. It must contain no self-loop, cycle, or pair of parallel edges forming a cycle. For any bounded gauge-invariant real or complex observable $F$ and bounded measurable $h$ of $V_T$,

$$
\mathbb E_P[F(V)h(V_T)]
=\mathbb E_P[F]\int h(u_T)\prod_{e\in T}dH(u_e).
$$

In particular, $V_T$ has product Haar law and

$$
\mathbb E_P[F\mid V_T]=\mathbb E_P[F].
$$

This is a standard consequence of tree gauge freedom, not a new Yang–Mills dynamical theorem. It concerns observing **only** the forest, with all other links integrated.

**Proof.** Fix a root in each tree component. Average independent Haar gauge transformations over its non-root vertices, fixing roots and other vertices to the identity. For any fixed $V$, the transformed tree links have product Haar law. To see this, remove a leaf: its gauge variable occurs in exactly one remaining tree edge, and left/right Haar invariance integrates that edge independently. Iterate to the roots. Equivalently, the map from non-root gauges to tree links is a triangular change of variables preserving product Haar.

For each fixed gauge transformation, invariance of $P$ and $F$ gives
$\mathbb E_P[F(V)h(V_T)]=\mathbb E_P[F(V)h((gV)_T)]$.
Integrate over the above gauge transformations and apply bounded Fubini. The inner average of $h$ is the product-Haar integral, independent of $V$, proving the formula. For the actual positive continuous finite density and bounded observables, the canonical density-ratio conditional also satisfies the identity pointwise: its numerator and denominator are invariant functions of the forest assignment, and gauge transformations act transitively on those assignments.

A related immediate fact is that a gauge-invariant observable depending only on a forest is constant. Nontrivial physical observables require cycle information or other appropriate gauge-invariant structure.

## 3. General exterior data: retain joint loop orbits

For an observed set $O$, define the canonical expectation

$$
h_F(\eta)=
\frac{\int F(V_{O^c},\eta)v(V_{O^c},\eta)d\mu_{O^c}}
{\int v(V_{O^c},\eta)d\mu_{O^c}}.
$$

Changing integrated variables by a fixed gauge transformation gives $h_F(g\eta)=h_F(\eta)$ whenever $F$ is gauge invariant. Choose a spanning forest of the observed graph. Gauge transformations can set those tree links to the identity. Each remaining edge then carries a holonomy around the corresponding based cycle; the remaining root transformation conjugates all based holonomies in that connected component simultaneously. Consequently $h_F$ depends only on this **joint gauge orbit**, not a chosen gauge representative.

For background on this established construction, see Burbano–Bauer, [Section III.1 and Appendix C.3.2](https://arxiv.org/html/2409.13812v2#S3.SS1). The probability identity above is proved here directly; the paper is not being cited as a proof of our Yang–Mills decay target.

Two cautions matter for research:

1. Tree gauge fixing changes the remaining link values into loop variables. One cannot delete tree observations while keeping the original chord values fixed. Those are different conditionals. A single changed link in a cyclic exterior can change a physical holonomy.
2. In a non-Abelian group, individual fundamental-loop traces do not generally determine the joint orbit. For example, unit quaternions $(i,i)$ and $(i,j)$ have identical individual normalized traces $(0,0)$ but product traces $-1$ and $0$. They are not simultaneously conjugate, even in SU(2). Relative loop information must be retained.

The tree paths used to form based loops can be long. Any later locality or support budget must account for those paths; gauge fixing is not a license to treat the new variables as independent local plaquettes. We have not proved density of a proposed loop-observable family in the reconstructed continuum Hilbert space.

## 4. Why activity bounds still do not close the estimate

The inspected [Activities.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Activities.lean) gives gauge invariance of forced payloads and their tests, weighted absolute `EBound`/`KBound` controls, and exact-flag admissibility. [Masks.lean](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Masks.lean) makes flags invariant too. These are compatible with the symmetry reduction; they do not in themselves bound the normalized dependence on joint loop data.

After fixing a tree, the full reference action and generated terms remain. A bound on small corrections does not establish mixing of that interacting reference law. The earlier [normalization obstruction](../../negative-results/2026-11-11-T03-conditional-normalization/README.md) also remains relevant. No existing activity declaration is promoted here into a relative posterior covariance estimate.

The revised bounded target is therefore an observable-specific, physically normalized estimate on changes of $h_F$ under distant changes of **joint cycle data**, or directly on the corresponding covariance in the buffered-posterior identity. Gauge-equivalent changes contribute exactly zero. Changes between distinct gauge orbits require a dynamical bound with uniform scale/volume control.

## 5. Exact non-Abelian controls and their limitations

The checker uses the quaternion group $Q_8$, a finite non-Abelian subgroup of unit quaternions. It builds multiplication from quaternion arithmetic, verifies associativity, and uses the real part as the normalized fundamental SU(2) trace restricted to this subgroup. It is not a replacement for continuous SU(2) Haar integration or an instance of the full upstream construction.

For two edge-disjoint triangular loops under product counting Haar, let $\phi_1,\phi_2$ denote their normalized holonomy traces. Each has mean zero and second moment $1/4$. The strictly positive gauge-invariant density

$$
w=1+c\phi_1\phi_2,\qquad 0<c<1,
$$

is already normalized. Direct enumeration gives

$$
\mathrm{Cov}(\phi_1,\phi_2)=c/16,
\qquad
\mathbb E[\phi_1\mid\text{all links of loop 2}]=(c/4)\phi_2.
$$

Observing any proper subset of the second triangle gives conditional mean zero for $\phi_1$ and uniform marginal links. Once the cycle is fully observed, changing its holonomy from $+1$ to $-1$ changes that conditional mean by $c/2$. Thus forest screening does not establish independence after other observed links complete a cycle.

One can connect the loops by an arbitrarily long chain of independent Haar edges without changing this covariance: the density and observables do not depend on the chain, so it integrates to one. **The density then contains an explicitly long-range interaction.** This is only a counterexample to inferring spatial decay from gauge invariance and positivity alone. It is not a finite-range Wilson model, an RG history, or a Yang–Mills counterexample.

The separate based-loop control distinguishes $(i,i)$ from $(i,j)$ by their product trace despite equal individual traces. The code also checks that no common $Q_8$ conjugation relates the pairs; the different product traces rule out common SU(2) conjugation analytically.

## Reproduction

From this repository root:

```sh
python3 auto-research/general/2026-11-11-T03-gauge-orbit-response/check_gauge_response.py
```

[Receipt](verification.json): Python 3.9.6, standard library only, exit 0, 0.518 seconds. [Output](check-output.json) records:

- 262,144 triangle gauge-invariance checks and 32,768 root-fixed tree assignments;
- 262,144 raw two-loop configurations for each of $c=1/2,2/3$;
- 217 forest assignments and 512 full-cycle conditionals per coupling;
- nonzero loop covariances $1/32$ and $1/24$;
- the individual-trace counterexample.

These exact tests verify the stated finite controls. They do not verify the general compact-group proof, replay the upstream Lean declarations, or establish spatial clustering.

## Next task, failure lesson, and review

Next: choose the actual gauge-invariant transported insertions required by the spectral construction and derive a relative crossing estimate for their conditional response to distant cycle data, preserving complete supports. If using a loop expansion, control its normalized connected coefficients and all non-Abelian joint information. A finite-dimensional spectrum calculation or a symmetry identity alone cannot supply the missing common physical rate.

The failure lesson for [future agents](../../../auto-research.md): raw-link influence includes gauge-dependent directions, but forest screening applies only before additional cycle-closing data are conditioned. Quotient by gauge transformations while retaining the full interacting law, joint loop information, and locality costs. Do not infer a mass gap from gauge symmetry.

Review status: current author/assistant derivation and exact checks only, 2026-11-11. Independent review and any formal compact-group integration remain open. No novelty claim is made for tree gauge fixing or its probability consequences.
