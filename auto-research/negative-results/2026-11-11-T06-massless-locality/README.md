# Locality and quadratic low-energy bounds allow a massless field

## Metadata and question

- Date: 2026-11-11. Rohan Arun, with OpenAI Codex assistance.
- Tracks: T06, T03, T04. Outcome: counterexample to a locality-only gap inference.
- Evidence: standard free-field construction, written asymptotic/scaling derivation, and exact scalar coefficient checks. No Lean formalization or independent review of the field model is claimed.
- Base repository revision: `574ec1821df2a19a4e5a275b3d3956c090d8242d`.
- Related: [variable-time estimate](../../general/2026-11-11-T03-variable-time-average/README.md), [earlier scalar obstruction](../2026-11-11-T06-polynomial-decay/README.md).

Does adding spacelike locality, forward-cone spectrum, a unique vacuum, and balanced adjoint-state norms repair the gap inference from polynomial low-energy bounds? The massless real free scalar field in 3+1 dimensions shows that it does not. This is **not** a model of the full upstream Yang–Mills data.

## Spectral measure and nonzero infrared weight

Use the usual vacuum Fock representation. Choose real $f\in C_c^\infty(\mathbb R^4)$ with nonzero integral, and put $v=\phi(f)\Omega$. This vector is centered; the smeared real field is symmetric on the common finite-particle domain, and its adjoint acting on the vacuum gives the same vector. The free-field two-point formula is the standard one in [Schenkel's lecture notes](https://www.aschenkel.eu/LectureNotes/node-Correlation-functions-Feynman-propagator.html). With $\widehat f(p)=\int e^{ip\cdot x}f(x)\,d^4x$ and mass zero, it gives

$$
F_f(u)=\mu_v((0,u])=
\frac1{2(2\pi)^3}\int_{0<|p|\leq u}
|\widehat f(|p|,p)|^2\frac{d^3p}{|p|}.
$$

This is finite: near zero the radial measure is proportional to $E\,dE$, and at infinity the Fourier transform is rapidly decreasing. Changing to polar coordinates and then setting $E=us$ yields

$$
\frac{F_f(u)}{u^2}=
\frac1{2(2\pi)^3}\int_0^1 s\int_{S^2}
|\widehat f(us,us\omega)|^2\,d\omega\,ds
\longrightarrow\frac{|\widehat f(0)|^2}{8\pi^2}>0.
$$

Uniform continuity near zero justifies the limit. Thus every sufficiently small energy window has positive mass; by monotonicity every positive window does. A positive gap is impossible in this model. Moreover boundedness of $\widehat f$ gives a global bound of a constant times $u^2$.

The same radial formula, with $E=s/t$ and dominated convergence using $\sup|\widehat f|<\infty$, gives

$$
t^2\int e^{-tE}\,d\mu_v(E)
\longrightarrow\frac{|\widehat f(0)|^2}{4\pi^2}.
$$

These are deductions from the two-point formula, not claims that the reference proves a Yang–Mills result.

## Which hypotheses survive?

Spacelike commutativity follows from the free-field commutator; see the [Klein–Gordon field notes](https://www.aschenkel.eu/LectureNotes/node-Free-quantum-Klein-Gordon-field.html). The one-particle measure lies on the positive light cone, and multiparticle momenta lie in its closed convex cone. Compact smearing gives exactly the finite spacelike commutator radius used by the locality audit.

In the vacuum Fock representation, the normal-ordered Hamiltonian on each non-vacuum particle sector multiplies by $\sum_j|p_j|$. Its zero set has product measure zero, so its kernel is the vacuum line; nevertheless positive energies accumulate at zero. The underlying Fock construction is described in the [Hilbert-space notes](https://www.aschenkel.eu/LectureNotes/node-Hilbert-space-particle-interpretation.html). This argument concerns 3+1 dimensions, avoiding the distinct infrared problem of the undifferentiated massless scalar in 1+1 dimensions.

The example supplies locality, positive energy, uniqueness of the zero-energy vacuum, and a real local observable with equal state/adjoint-state norms. It does not assert density of a fixed-radius family with uniformly bounded adjoint cost. It supplies none of the required nonabelian Wilson-family, running-coupling, or interacting-hierarchy identifications.

## Exact scale test

For $L>0$, set $f_L(x)=L^{-3}f(x/L)$. Direct change of variables gives $\widehat f_L(p)=L\widehat f(Lp)$. Since the mass-shell measure scales as $L^{-2}$,

$$
\|\phi(f_L)\Omega\|=\|\phi(f)\Omega\|,\qquad F_{f_L}(u)=F_f(Lu).
$$

If $r$ bounds the original support, $Lr$ bounds the dilated support. At $u=c/L$, both $F_{f_L}(u)=F_f(c)>0$ and $(Lr)^2u^2=r^2c^2$ are constant. Choose $c>0$ with $2rc\leq1$ to remain within the optimized time-average estimate's domain. The improved radius power is consistent with this gapless field.

## Checks, failure lesson, and next attempt

From the repository root run:

```sh
python3 auto-research/negative-results/2026-11-11-T06-massless-locality/check_scaling.py
```

[Recorded output](scaling-check.json) and [receipt](verification.json) check only radial constants and dilation factors using SymPy; they do not verify the field construction, dominated convergence, or the upstream application. No numerical field simulation was run.

The invalid inference is that local commutators plus small low-energy weight must exclude that weight entirely. Always test locality-only proposals against this control and keep normalized support/energy costs. Reopen the route only with an estimate using Yang–Mills dynamics that fails in this massless example. The next task is to identify that additional estimate, not to further optimize a universal polynomial coefficient. No independent review is recorded.
