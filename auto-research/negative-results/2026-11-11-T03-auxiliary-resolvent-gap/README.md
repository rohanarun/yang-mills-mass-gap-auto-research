# An auxiliary resolvent gap does not establish the physical mass gap

## Metadata and outcome

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T03, T04, T06, T07.
- Outcome: a candidate shortcut fails; a route through RG remains open with additional obligations.
- Evidence: selective source inspection, written finite-dimensional counterexample, exact symbolic matrix checks. No upstream kernel replay or independent review.
- Base repository commit: `574ec1821df2a19a4e5a275b3d3956c090d8242d`. Upstream: `3456e5e75cf8d4cd558955a5c7638fba2d68f464`; [source hashes](provenance.json).

## Candidate source route

[`FreeResolvent.resolve_point`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Push/FREE_RESOLVENT/Inverse.lean#L120) gives an exponential bound on entries of $(A+uI)^{-1}$, with rate at most

$$
\gamma=\min\left(\frac{\sigma}{2},\frac{r\sigma}{4(M+1)}\right).
$$

It assumes a weighted Schur estimate for the finite matrix $A$, a positive quadratic-form bound $A\geq rI$, and $u\geq0$. The rate is derived from these inputs; it is not a new lower bound on the spectrum of the physical Hamiltonian.

The concrete [`tree_gap`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Push/FREE_RESOLVENT/Flat.lean#L198) applies to `treeMatrix`, a principal submatrix on independent free-bond coordinates. Its lower bound is `treeFare = min a K.penalty / (1 + beta + gamma)`, with the denominator supplied by block calibration. The argument fixes the retained coordinates to zero via `stretch T (0, profile T v)` and controls the fluctuation directions. Its input `Gap (H.acts f) a` concerns a face-row coefficient operator; the symbol `H` here does not denote the reconstructed energy generator.

[`treeInverse`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/Push/FREE_RESOLVENT/GaugeProjection.lean#L131) inverts that matrix. A concrete later use in [`Hill.purchase`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/YM/PhysicalNext/PHYSICAL_GUARD_7F546/Hill.lean#L128) constructs `Q0 = treeMatrix ...`, proves its positive definiteness, and compares local covariance matrices with its inverse. This is useful fluctuation control. The inspected statements do not themselves identify these entries with a dense family's physical connected correlations at arbitrary separation.

## Exact obstruction to transferring a block gap

For $\varepsilon>0$, consider the Gaussian precision matrix

$$
A_\varepsilon=\begin{pmatrix}1&-1\\-1&1+\varepsilon\end{pmatrix},\qquad
(x,y)A_\varepsilon(x,y)^T=(x-y)^2+\varepsilon y^2.
$$

It is positive definite. Its fast-coordinate block is exactly $1$ for every $\varepsilon$, and the conditional variance of $x$ given $y$ in the Gaussian density proportional to $\exp[-((x-y)^2+\varepsilon y^2)/2]$ is exactly $1$. Nevertheless integrating out $x$ leaves precision $\varepsilon$ for $y$: the Schur complement is $(1+\varepsilon)-(-1)^2=\varepsilon$.

The full covariance and a Rayleigh quotient are

$$
A_\varepsilon^{-1}=\begin{pmatrix}1+\varepsilon^{-1}&\varepsilon^{-1}\\\varepsilon^{-1}&\varepsilon^{-1}\end{pmatrix},\qquad
\frac{(1,1)A_\varepsilon(1,1)^T}{\|(1,1)\|^2}=\varepsilon/2.
$$

Thus the full smallest eigenvalue is at most $\varepsilon/2$ even though the eliminated block has a uniform gap. One can make the conditional covariance strictly local on many sites by taking $\sum_i(x_i-y_i)^2+y^TLy$; eliminating the $x$ variables leaves the original slow precision $L$. The two-by-two instance already disproves the claimed general implication.

This is a Gaussian linear-algebra control, not a Yang–Mills model and not an identification between a precision eigenvalue and a physical Hamiltonian gap. It demonstrates the missing information in an attempted block-to-full inference; it does not refute the upstream theorems.

## Reproduction

From the repository root:

```sh
python3 auto-research/negative-results/2026-11-11-T03-auxiliary-resolvent-gap/check_block.py
```

[Output](block-check.json) and [receipt](verification.json) record exact SymPy checks of the inverse, determinant, Schur complement, quadratic form, and Rayleigh quotient. Positive definiteness follows from the displayed completed square for $\varepsilon>0$. The source audit is separate from these computations.

The first script run failed at a structural matrix-equality assertion because rational expressions had not been normalized. The final check simplifies each entry of the difference before testing that it is zero; the mathematical identity was unchanged.

## Revised research target

Do not identify a block precision gap, a coefficient ellipticity bound, or covariance locality with the gap of the reconstructed Hamiltonian. To pursue this route, first obtain a bound for the *retained* effective measure and its connected observables, including nonlinear terms and vacuum subtraction. Then identify those observables with the intended hierarchy, prove density, and control both limits. If $\gamma$ is per lattice step of physical length $a$, the corresponding physical exponential rate is $\gamma/a$; at a blocked scale use that scale's physical length. Its positive lower bound must be proved along the actual schedule.

The bounded next question is whether an existing connected-source RG theorem controls the retained mixed-source derivatives by separation, rather than only local covariance or finite-volume comparison errors. Success requires an exact source-to-observable identity and a common positive physical rate. Merely reusing `resolve_point` leaves this question open. The present audit is selective and does not exclude other useful upstream results. No independent review is recorded.
