# Cyclicity does not supply uniform adjoint-state costs

## Metadata

- Date: 2026-11-11; author: Rohan Arun with OpenAI Codex assistance.
- Tracks: T06, T03, T05.
- Outcome: counterexample to a proposed shortcut from cyclicity/separation to uniform adjoint-state control on a dense family.
- Evidence: written Hilbert-space argument. No Lean formalization or numerical experiment is claimed.
- Context: [infrared cost audit](../../general/2026-11-11-T03-infrared-cost-audit/README.md), based on upstream revision `3456e5e75cf8d4cd558955a5c7638fba2d68f464`.

## Inference tested

Could a cyclic separating vacuum by itself let us approximate every vector by operator-created states with a fixed bound on $\|A^*\Omega\|/\|A\Omega\|$? Such a bound would address part of the cost in the inspected shell estimate.

## Explicit fixed-space example

Let $K=\ell^2(\mathbb N)$ and let the algebra $B(K)$ act on $K\otimes K$ in the first factor. Set

$$
\lambda_j=2^{-(j+1)},\qquad
\Omega=\sum_{j\geq0}\sqrt{\lambda_j}\,e_j\otimes e_j.
$$

The vector has norm one. It is cyclic: every elementary tensor is $(A\otimes I)\Omega$ for an appropriate finite-rank matrix unit $A$. It is separating: if $(A\otimes I)\Omega=0$, then every $\sqrt{\lambda_j}Ae_j=0$, so $A=0$.

For $A_n=|e_0\rangle\langle e_n|$, one obtains

$$
\|(A_n\otimes I)\Omega\|^2=\lambda_n,\qquad
\|(A_n^*\otimes I)\Omega\|^2=\lambda_0,\qquad
\frac{\|(A_n^*\otimes I)\Omega\|^2}{\|(A_n\otimes I)\Omega\|^2}=2^n.
$$

These vectors are centered for $n\geq1$. Thus cyclicity and separation do not bound the adjoint cost even with a single fixed vacuum and algebra.

## Why choosing a different dense family does not repair this example

Write $v=(A\otimes I)\Omega$. Its coefficient along $e_0\otimes e_n$ equals $\sqrt{\lambda_n}A_{0n}$, while the coefficient of $(A^*\otimes I)\Omega$ along $e_n\otimes e_0$ has absolute value $\sqrt{\lambda_0}|A_{0n}|$. Consequently,

$$
\|(A^*\otimes I)\Omega\|\geq2^{n/2}|\langle e_0\otimes e_n,v\rangle|.
$$

If $\|v-e_0\otimes e_n\|<\varepsilon<1$, then

$$
\frac{\|(A^*\otimes I)\Omega\|}{\|v\|}
\geq2^{n/2}\frac{1-\varepsilon}{1+\varepsilon}.
$$

For any proposed finite common bound, choose $n$ large and fix, for example, $\varepsilon=1/4$. The ball around this centered unit vector contains no operator-created state obeying the bound. Hence the bounded-ratio states are not dense, even in the centered subspace.

## Scope and lesson

This example is an operator-algebra construction, not a Yang–Mills theory. It has no spacetime locality, Wilson origin, or specified Hamiltonian. It rules out a logical shortcut based on cyclicity and separation alone, not a Yang–Mills-specific estimate restricted to a low-energy subspace.

Agents should always retain the adjoint-state term in the source bound and distinguish qualitative density from approximation with controlled costs. Reopen this route only with additional dynamics or a quantitative preparation theorem for the actual selected phase. The focused low-energy approximation criterion remains a possible target; its hypothesis has not been proved.

## Next contribution and review

T05 should identify the extra structure that controls adjoint-state costs for low-energy vectors. T03 should test that estimate against the explicit threshold in the source audit. Independent review is pending.
