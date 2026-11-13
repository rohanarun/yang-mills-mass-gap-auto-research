# Spatial tails and conditional perturbation from the actual regular-activity budget

## Metadata and bounded task

- Date: 2026-11-13; Rohan Arun with OpenAI Codex assistance.
- Tracks: T03-B/D, T04, T06, T07. Base: `ff784a0ae4a886580dfb8e0c7aa4e9dac6ce94f6`.
- Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).
- Outcome: explicit written exponential spatial bound for the regular sector's direct mixed variation, and a conditional-law perturbation bound removing that sector while retaining the reference action and forced gas. No buffered correlation estimate or mass gap.
- Evidence: source inspection, written derivation, exact finite geometry/probability diagnostics. No new Lean proof or independent mathematical review.
- Task: extract spatial control from the actual generated interaction budget, including flag read supports; then test whether the estimate survives integrating a buffer. Falsification: missing support enlargement, a volume-dependent anchor sum, or an unjustified replacement of a marginal by a fixed-buffer conditional. Computation is finite exact arithmetic only.

These are consequences of existing upstream support and activity controls, not newly discovered Yang–Mills dynamics. In particular, the connected-cover geometry and its extent theorem are already upstream. The scoped search does not establish novelty of the explicit corollaries below. This work is independent of unmerged PRs #10–#12.

## Source inputs

Fix a selected history and one valid representation at level m, N>=m. Write E(U) for `R.activities.additive R.p U`, s=R.p.supportExponent>0, B=R.p.B>=1, and delta for the regular allowance. `History.Conv.good` supplies the following existing certificate:

$$
E=\sum_i\phi_i,\quad o_i\in P_i,\quad |\phi_i(U)|\leq b_i,\quad
\sum_{i:o_i=o}e^{s k_i}b_i\leq\delta,
\qquad k_i=\mathrm{coverNumber}_B(P_i),\quad b_i\geq0.
\tag{1}
$$

Here phi_i is the masked regular occurrence. The supremum bound follows by using the empty derivative list in `supBounds` on a healthy configuration; the masked occurrence is zero elsewhere. Each sum in (1) is absolutely summable by `SumBudget`. Summing over the finitely many anchors also proves absolute convergence of E at fixed volume.

Relevant declarations:

- [`Activities.EBound`, `Valid`, and `regularOccurrence`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Activities.lean#L98).
- [`BudgetPoint.mass` and `supBounds`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Masks.lean#L144).
- [`History.Conv.good`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/History.lean#L207).

The actual read set of phi_i is contained in I_i=inspected(P_i), not merely P_i. Its payload is local on P_i and its health mask reads the relevant face flags; [`flags_agree` and `inspected`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Masks.lean#L87) account for these reads. Every point of I_i lies within native separation 2 of P_i: two corners of a tested elementary face can be joined by at most two unit steps. This conservative bound is enough and also covers wrapping faces.

The support cost is a **connected-cover** cost, even for disconnected P_i. [`Corona.extent`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Corona/Fit.lean#L84) already proves

$$
 d(x,y)\leq (4B+2)k_i+2B\qquad(x,y\in P_i).
\tag{2}
$$

No new replay of that module is claimed.

## Anchor summation without a volume factor

The source distance is periodic maximum-coordinate distance in four dimensions. For c>0 define

$$
C_4(c)=\left(\frac{1+e^{-c/4}}{1-e^{-c/4}}\right)^4.
$$

For any nonempty finite site set A on any finite torus,

$$
\sum_o e^{-c d(o,A)}\leq |A|C_4(c).
\tag{3}
$$

Indeed, the exponential of the distance to A is bounded by the sum of the corresponding exponentials to each a in A. Translate a to zero and inject the canonical minimal coordinate representatives into Z^4. Since the maximum norm is at least one quarter of the sum norm, the lattice sum is at most the product of four convergent two-sided geometric series. This proves (3) uniformly in the period, including even periods with a fixed choice of minimal representatives.

## A direct exponential crossing bound

Let A,D be nonempty site sets, and let d=d(A,D). These will be the endpoint sets of two disjoint sets of changed link variables. Define

$$
L=4B+2,\qquad \alpha=\frac{s}{2L}.
$$

For an occurrence whose inspected support meets both A and D, (2) and the two flag halos imply

$$
 d\leq Lk_i+2B+4,\qquad d(o_i,A)\leq Lk_i+2B+2.
$$

Adding these inequalities and using s=2L alpha gives

$$
e^{-s k_i}\leq e^{\alpha(6+4B)}e^{-\alpha d}e^{-\alpha d(o_i,A)}.
$$

Group by anchor in (1), use (3), and repeat with D in place of A to obtain

$$
\boxed{\sum_{i:I_i\cap A\ne\varnothing,\ I_i\cap D\ne\varnothing}b_i
\leq\delta\min(|A|,|D|)C_4(\alpha)
 e^{\alpha(6+4B)}e^{-\alpha d(A,D)}.}
\tag{4}
$$

This is a bound on actual regular-activity envelopes. It is not a posterior covariance bound.

For four field configurations obtained by independently changing two disjoint link sets with endpoint sets A and D, hold every other link fixed and let Delta_A Delta_D denote their alternating four-term difference. Occurrences that do not read both changed sets cancel. Bounding the other four values by b_i yields

$$
\boxed{|\Delta_A\Delta_D E|
\leq4\delta\min(|A|,|D|)C_4(\alpha)
 e^{\alpha(6+4B)}e^{-\alpha d(A,D)}.}
\tag{5}
$$

Using endpoint sets overcounts possible reads, so it gives a safe upper bound. Absolute summability justifies taking the four-term difference inside the occurrence sum. No derivative of a flag indicator is used.

## Conditional perturbation while retaining the other interactions

A separate consequence of (1) controls all regular occurrences reading one block. Put gamma=s/L. The anchor-to-block estimate alone gives

$$
Q_A:=\sum_{i:I_i\cap A\ne\varnothing}b_i
\leq\delta |A|C_4(\gamma)e^{\gamma(2+2B)}=:M_A.
\tag{6}
$$

Let J be a nonempty set of independent block links and A its endpoint set. For a fixed exterior eta, write the actual conditional law on J as

$$
\gamma_J^\eta(du)\propto e^{-S(u,\eta)-E(u,\eta)}G(u,\eta)\,dH_J(u).
$$

Here H_J integrates precisely the links in J. Define nu_J^eta by removing E only, retaining the complete reference action S and forced gas G. The actual selected density is positive; therefore G is positive in this representation. At finite volume, bounded E makes this comparison conditional well defined even if the separate factors are merely measurable.

The oscillation of E as the block varies is at most 2Q_A. Applying the standard log-density oscillation comparison already derived in the [conditional-law record](../2026-11-11-T03-block-conditional-bounds/README.md), with TV defined as sup over events, gives

$$
\boxed{\mathrm{TV}(\gamma_J^\eta,\nu_J^\eta)
\leq\tanh(Q_A/2)\leq\tanh(M_A/2).}
\tag{7}
$$

This is an actual conditional-law perturbation bound, uniform in the exterior. It does not prove that nu mixes, and the displayed constants have not been shown small enough for a block contraction. This comparison is not a replacement by the bare Wilson law.

## Uniformity and the unresolved buffer

At a fixed history and fixed level m, `Conv.vac` identifies s and B with `Levels.budget m`, and `Conv.good` uses the common `clock.allowance m`. Thus (4)-(7), for fixed block cardinalities, are independent of cutoff depth N>=m and total volume p. They are not asserted uniform over all levels m or different histories. Native lattice distance is not physical time; no common physical decay rate is obtained here.

Equations (4)-(5) concern the **direct regular contribution** while the buffer is fixed. The complete log density is c-S-E+log G. Neither the reference-action correlations nor the log-gas mixed variation is bounded by (5). Small absolute forced-label weights do not alone provide a relative lower bound for the exact-coverage gas or a convergent local expansion of its logarithm.

Integrating a buffer can generate an effective interaction between regions with no direct common term. The [exact chain control](../../negative-results/2026-11-13-T03-direct-versus-buffered/README.md) illustrates this using only nearest-neighbour interactions: direct endpoint mixed variation is zero, but the endpoint covariance after buffer integration is q^L. It is not a Yang–Mills model. This is why (5) cannot be inserted as the missing buffered-posterior estimate.

## Verification and next task

Run `python3 auto-research/general/2026-11-13-T03-regular-spatial-tail/check_tail.py`. [Output](checks.json) and [receipt](verification.json) record 24 finite four-dimensional flag-halo checks, seven exact torus-sum checks, 1,616 rational exponent-split cases, and 21 exact integrated-chain cases, all passed. These are diagnostics of support accounting, constants, and conditioning. They do not verify the general countable-sum derivation, replay source theorems, or provide independent review.

The next missing estimate is mixing for the reference-action/forced-gas block law nu, with a relative treatment of exact flag coverage, followed by a perturbation or multiscale theorem incorporating the regular budget. Alternatively derive the full buffered-posterior response directly. Keep (4)-(7) as sector-specific inputs; do not relabel direct interaction locality as correlation decay.

The result is ready for mathematical review. No ongoing worker or recurring process remains after handoff. The Yang–Mills mass gap remains unproved.
