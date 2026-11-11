# Small activity amplitudes and local noise do not imply spatial mixing

## Metadata and precise scope

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tasks/tracks: T03-B, T03-D, T04, T06.
- Outcome: two finite-probability controls against unsupported inferences, plus an exact-coverage source audit. No Yang–Mills counterexample or mass-gap proof.
- Evidence: written arguments, source inspection, symbolic sums and exact rational enumeration. No Lean proof or independent review.
- Base: `2c86f4fca925a7c64973e6573059329e446af56a`. Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [provenance](../../general/2026-11-11-T03-block-conditional-bounds/provenance.json).
- Related: [actual coarse conditional bound](../../general/2026-11-11-T03-block-conditional-bounds/README.md), [terminal covariance](../../general/2026-11-11-T03-terminal-covariance/README.md).

## The source gas has exact coverage, not a universal empty term

[`Activities.admissible`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Activities.lean#L114) requires disjoint forced supports and equality between the union of their inventories and the complete flag set of the configuration. Its empty collection contributes only when there are no flags. `gas_one` proves $G(U)=1$ on that no-flag sector. For configurations with flags, no unconditional unit term exists.

[`KBound`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/Activities.lean#L102) bounds absolute payloads with support weights. `gasSeries` in [`ActivityBounds`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/RG/ActivityBounds.lean#L56) supplies absolute summability. Neither displayed statement is a relative lower bound on $G$ or a mixed-boundary estimate on $\log G$. Positivity of the selected density does not quantify such a relative estimate. This is a selective audit of these declarations, not a claim that no other source theorem could help.

Consequently, applying a generic `log(1 + small)` argument to this exact-coverage gas requires an additional identity and hypotheses. Small absolute amplitudes can cancel when a conditional law is normalized.

## Control 1: a rare flagged sector can have strong conditional dependence

Take $h\in\{0,1\}$ and $x,y\in\{-1,1\}$, with uniform product prior. For $\alpha>0$ and $0<q<1$, set

$$
G(h,x,y)=\begin{cases}1,&h=0,\\ \alpha(1+qxy),&h=1.\end{cases}
$$

This reproduces only the abstract exact-coverage bookkeeping: the flag set is empty for $h=0$ and a fixed nonempty set $X$ for $h=1$; one label has support/inventory $X$ and payload $K=\mathbf1_{h=1}\alpha(1+qxy)$. Then the admissible empty term and one-label term give precisely $G$. It is **not** a realization of the source's geometric flag definition, gauge invariance, full activity interface, selected history, or Yang–Mills theory.

The payload is strictly positive on its eligible sector and has supremum $\alpha(1+q)$, arbitrarily small as $\alpha\to0$. For any fixed positive support weight, its weighted amplitude can likewise be made arbitrarily small. Yet conditioning on $h=1$ cancels $\alpha$:

$$
P(x\mid y,h=1)=\frac{1+qxy}{2},\qquad
\|P(x\mid y=1,h=1)-P(x\mid y=-1,h=1)\|_{\rm TV}=q.
$$

The log-density double difference is $2\log((1+q)/(1-q))$, whose quarter hyperbolic tangent is exactly $q$. Absolute smallness supplies no improvement in this conditional influence. Taking $q$ close to one makes it arbitrarily strong.

This does **not** mean the rare sector ruins averaged correlations. Exact summation gives

$$
Z=\frac{1+\alpha}{2},\qquad P(h=1)=\frac{\alpha}{1+\alpha},\qquad
\mathrm{Cov}(x,y)=\frac{\alpha q}{1+\alpha}.
$$

The averaged covariance tends to zero with $\alpha$. A probability-weighted treatment of exceptional sectors remains possible; it must be proved for the actual measure and geometry, rather than assumed from an absolute coefficient budget.

## Control 2: independent local noise can preserve a distant common cause

Let $S\in\{-1,1\}$ be uniform. Given $S$, take $X_1,\ldots,X_n$ independently with

$$
P(X_i=x\mid S)=\frac{1+rSx}{2},\qquad 0<r<1.
$$

This is a strictly positive noisy output law. Equivalently the one-site channel is proportional to $e^{\kappa Sx}$ with $r=\tanh\kappa$. The input field shares the latent sign everywhere. Then

$$
\mathbb E X_i=0,\qquad \mathrm{Cov}(X_i,X_j)=r^2\quad(i\ne j).
$$

The sites can be placed arbitrarily far apart without changing this value. Meanwhile, for any exterior configuration, the conditional law of $X_i$ is a mixture of its two channels. Therefore its total-variation diameter over all exteriors is at most $r<1$, just like the distance-independent one-link noise bound in the related audit.

For even $n$, fix all exterior spins except $X_j$ so their sum is zero. The posterior mean of $S$ is then $rX_j$. Flipping $X_j$ changes the conditional law of $X_i$ by total variation $r^2$. Thus the spatial influence row sum is at least $(n-1)r^2$, unbounded in volume for fixed $r>0$. Uniformly small conditional diameter does not give a summable spatial influence matrix.

This model lacks the Yang–Mills dynamics, gauge constraints, and reconstructed vacuum/phase requirements. Its infinite-volume mixed law also retains the latent phase; conditioning on $S$ removes the pair covariance. It is a counterexample only to deducing spatial decay from a positive local-noise channel and arbitrary hidden-field distribution. It does not refute a result that controls that hidden distribution or selects and analyzes the relevant phase.

## Reproduction and limits

The shared [script](../../general/2026-11-11-T03-block-conditional-bounds/check_conditionals.py), [output](../../general/2026-11-11-T03-block-conditional-bounds/conditional-check.json), and [receipt](../../general/2026-11-11-T03-block-conditional-bounds/verification.json) are in the general audit. Run from the repository root:

```sh
python3 auto-research/general/2026-11-11-T03-block-conditional-bounds/check_conditionals.py
```

The script checks the flag model symbolically, the latent covariance symbolically for four sites, and exact conditional probabilities for $n=4,6,8$ at $r=1/5,1/2,3/4$. All nine enumerations verify the diameter bound and single-neighbor influence $r^2$. The all-$n$ and arbitrary-separation statements follow from the written model argument, not extrapolation of a simulation. No asymptotic Yang–Mills estimate was computed.

## Failure lesson and next task

Do not replace absolute smallness with relative smallness after normalization. Check whether a polymer gas has a unit term in every configuration before expanding its logarithm. Distinguish worst-case conditional influence from probability-weighted exceptional events, and distinguish local noise smoothing from decay of the hidden-field correlations.

Reopen these routes with either a relative mixed-boundary estimate for the actual coarse law, or a rigorous weighted treatment of exceptional configurations that also controls the reference measure and transported observables. The first concrete target is a normalized block partition-function ratio across a buffer, with all generated interactions retained and constants uniform in the required limits. Review pending; mass gap remains unproved.
