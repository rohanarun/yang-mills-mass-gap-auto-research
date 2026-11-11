# T01 specification review of the proposed gap target

**This is a review of a statement, not a proof of it.** No Yang–Mills mass gap is proved or claimed. Nothing here was checked in Lean.

## Metadata

- Result ID and date: `2026-11-12-T01-gap-target-specification`; 2026-11-12.
- Reviewer/session: [@DanieleCorso](https://github.com/DanieleCorso), with Claude (Anthropic) assistance. The reviewer did not write the reviewed target. The review is AI-assisted and has not been read by a subject expert; treat it as a first specification review, not as expert sign-off.
- Primary track and related tracks: T01; T02, T05, T07.
- Outcome: specification review with one conditional result (energy-slab gap is equivalent to an invariant-mass gap under stated upstream hypotheses), three supporting observations, and five findings. No defect was found that makes the target vacuous or circular. Two limits of the target are recorded.
- Evidence level(s): source inspection; written derivation; exact finite arithmetic checks of the explicit boosts. **No Lean elaboration, no kernel replay, no upstream replay, no independent expert review.**
- Repository base commit: `3e4346626680f8ef782d0e2daca99056428d9c7d`. Reviewed file: [`MassGapTarget.lean`](../../../research/mass-gap-20261111/MassGapTarget.lean) at that commit.
- Upstream: `yang-mills-group/OpenAI-YM-20261028`, commit `3456e5e75cf8d4cd558955a5c7638fba2d68f464`. Definitions used: [`PublicTheory.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean), [`PublicWilson.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean), [`ChallengeSpec.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean), [`Solution.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/Solution.lean). The Git blob SHA-256 values of `PublicTheory.lean`, `ChallengeSpec.lean`, `Solution.lean` and the three `YM/EveryPhase` files were recomputed and match [the baseline provenance](../../../research/mass-gap-20261111/provenance.json).
- Mathlib: the definition of `charFun` and the name `Measure.ext_of_charFun` were read in `Mathlib/MeasureTheory/Measure/CharacteristicFunction/Basic.lean` at the revision pinned by the upstream `lake-manifest.json`, `81a5d257c8e410db227a6665ed08f64fea08e997`. The theorem's typeclass hypotheses were not checked against `Spacetime` by elaboration.
- Toolchain: Python 3.10.6, standard library only, for [`check_boosts.py`](check_boosts.py). No Lean toolchain was available on the review host.
- Related results: [initial reduction](../../general/2026-11-11-T02-initial-reduction/README.md), [Laplace support theorem](../../general/2026-11-11-T02-laplace-support/README.md). Nothing is superseded.

## Question and exact claim

T01 asks whether `HasEnergyGapAt` and `GappedJointExistence` say what is intended for the same upstream hierarchy, whether an energy gap differs from an invariant-mass gap, and whether the common gap across volume refinements is needed.

The reviewed definitions are

```lean
def HasEnergyGapAt (T : WightmanTheory H Labels) (m : ℝ) : Prop :=
  0 < m ∧ T.energyMomentum.projection {p : Spacetime | 0 < time p ∧ time p < m} = 0

def GappedJointExistence : Prop :=
  ∀ g : GaugeGroup, g.IsSimple → ∃ C : WilsonFamily g,
    WilsonRegularity C ∧ ∃ m : ℝ, 0 < m ∧
      ∀ p : ℕ → ℕ, StrictMono p → ∃ q : ℕ → ℕ, StrictMono q ∧
        ∃ T : Hierarchy C, T.Properties (p ∘ q) ∧ HasEnergyGapAt T.theory m
```

Falsification criterion for this review: any step below that uses a field the upstream structures do not provide, a wrong sign or transpose convention, or a set whose projection the upstream axioms do not constrain, invalidates the corresponding conclusion.

What this review establishes is limited to the written statements in the next section. It does not establish that the target is true.

## Approach and derivation

Notation. $P(B)$ is `energyMomentum.projection B`, $\mu_\psi$ is `energyMomentum.diagonal ψ`, $T(x)$ is `translations.operator x`, $U(g)$ is `poincare.onStates g`, $\Omega$ is the vacuum vector. Upstream puts time in the last coordinate, with `forwardCone` $=\{\|\mathrm{spatial}\,p\|\le \mathrm{time}\,p\}$ and `minkowskiSquare` $p=(\mathrm{time}\,p)^2-\|\mathrm{spatial}\,p\|^2$ ([PublicTheory.lean L57–L66](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L57-L66)). Write $S_m=\{p: 0<\mathrm{time}\,p<m\}$ for the slab and $R_m=\{p\ne0:\ \mathrm{minkowskiSquare}\,p<m^2\}$ for the mass region. Both are open, hence measurable. The upstream PVM axioms constrain $P$ only on measurable sets ([L180–L200](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L180-L200)); this matters only as a reminder never to state a target on a non-measurable set.

Hypotheses used, all fields of the upstream structures for `T.theory` when `T.Properties _` holds (via `reconstruction.axioms`, [ChallengeSpec.lean L117–L118](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean#L117-L118)):

- (PVM) `intersection`, `selfAdjoint`, `countablyAdditive`, `finite`, `diagonalIdentity`.
- (W0) `spectralRepresentation`, `positiveEnergy`, `uniqueVacuum` ([L270–L278](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L270-L278)).
- (P) the `PoincareAction` fields `composition`, `unitary`, `coordinates`, `productCoordinates`, `translationCoordinates`, and `translationCompatibility` ([L219–L262](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicTheory.lean#L219-L262)).
- (W2) `vacuumInvariant`, used only in Observation 3.

### Observation 1: the PVM is fixed by the translations

*Statement.* Under (PVM) and `spectralRepresentation`, the operator $P(B)$ for every measurable $B$ is determined by the translation operators. So the target cannot be met by attaching an unrelated projection-valued measure to the theory.

*Argument.* Mathlib defines `charFun μ t` as $\int e^{i\langle x,t\rangle}\,d\mu(x)$ with the Euclidean inner product of `Spacetime`. `spectralRepresentation` says $\widehat{\mu_\psi}(x)=\langle\psi,T(x)\psi\rangle$ for all $x$. A finite Borel measure on $\mathbb{R}^4$ is determined by its characteristic function (`Measure.ext_of_charFun`), so $\mu_\psi$ is determined by $T$. `diagonalIdentity` gives $\langle\psi,P(B)\psi\rangle=\mu_\psi(B)$ for every $\psi$, and polarization on a complex Hilbert space recovers the bounded operator $P(B)$.

Two facts used repeatedly follow from `intersection` and `selfAdjoint`: $P(B)$ is an orthogonal projection, so $\mu_\psi(B)=\|P(B)\psi\|^2$, and therefore $P(B)=0$ if and only if $\mu_\psi(B)=0$ for all $\psi$.

### Proposition 2: energy slab and invariant-mass region

*Statement.* Assume (PVM), `spectralRepresentation`, `positiveEnergy` and (P). For $m>0$,

$$
P(S_m)=0 \iff P(R_m)=0 .
$$

The implication from right to left needs no hypothesis beyond monotonicity of $P$. The implication from left to right uses Lorentz covariance and positive energy; it is false without covariance (see the control at the end of this subsection).

*Right to left.* If $0<\mathrm{time}\,p<m$ then $p\neq0$ and $\mathrm{minkowskiSquare}\,p\le(\mathrm{time}\,p)^2<m^2$, so $S_m\subseteq R_m$ and $P(S_m)=P(S_m)P(R_m)=0$.

*Left to right.*

1. *Intertwining.* Let $g$ have coordinates $(\Lambda,a)$. By `productCoordinates` and `translationCoordinates`, both $g\cdot\tau(x)$ and $\tau(\Lambda x)\cdot g$ have coordinates $(\Lambda,\Lambda x+a)$, where $\tau$ is `pureTranslation`. `coordinates` is a bijection, so the two elements are equal. `composition` and `translationCompatibility` give $U(g)T(x)=T(\Lambda x)U(g)$.
2. *Transport of diagonal measures.* $U(g)$ is linear and norm preserving, hence preserves inner products. So $\langle U(g)\psi,T(\Lambda x)U(g)\psi\rangle=\langle\psi,T(x)\psi\rangle$. In terms of characteristic functions, and using $\langle p,\Lambda x\rangle=\langle\Lambda^{\mathsf T}p,x\rangle$ for the Euclidean pairing, the pushforward of $\mu_{U(g)\psi}$ under $\Lambda^{\mathsf T}$ has the same characteristic function as $\mu_\psi$. By uniqueness, $\mu_\psi(\Lambda^{\mathsf T}B)=\mu_{U(g)\psi}(B)$ for measurable $B$.
3. *Invariance of null sets.* If $P(B)=0$ then $\mu_\varphi(B)=0$ for all $\varphi$, so $\mu_\psi(\Lambda^{\mathsf T}B)=0$ for all $\psi$, so $P(\Lambda^{\mathsf T}B)=0$. `coordinates` is surjective, so $\Lambda$ ranges over all of `ProperLorentz`. The Euclidean transpose of a proper orthochronous Lorentz map is again one ($\Lambda^{\mathsf T}=\eta\Lambda^{-1}\eta$, with the same time–time entry). Hence $P(LS_m)=0$ for every proper orthochronous $L$.
4. *Covering.* Let $p\in R_m$ lie in the forward cone. Then $\mathrm{time}\,p>0$ and $0\le\mathrm{minkowskiSquare}\,p=\mu^2<m^2$. If $\mu>0$, a boost $L$ takes the rest vector of energy $\mu\in(0,m)$ to $p$, so $p\in LS_m$. If $\mu=0$, then $p=E(n,1)$ with $E>0$, and the boost along $n$ with $e^{s}=u$ sends $p$ to energy $E/u$, which lies in $(0,m)$ for $u$ large; so again $p\in LS_m$ for some $L$. Thus $R_m\cap\mathrm{forwardCone}\subseteq\bigcup_L LS_m$.
5. *Countability.* The sets $LS_m$ are open in $\mathbb{R}^4$, which is second countable, so countably many of them have the same union. Countable subadditivity of each finite measure $\mu_\psi$ gives $\mu_\psi(\bigcup_L LS_m)=0$.
6. *Outside the cone.* `positiveEnergy` gives $\mu_\psi(\mathrm{forwardCone}^c)=0$. Together with step 5, $\mu_\psi(R_m)=0$ for every $\psi$, so $P(R_m)=0$.

*Control showing covariance is used.* A point of invariant mass $\mu<m$ boosted to energy at least $m$ is outside $S_m$. A PVM supported on such a point alone has an empty slab and a nonempty mass region; it is excluded only because its boosted images must also carry spectrum. [`check_boosts.py`](check_boosts.py) exhibits such a point exactly.

*Scope.* This is the standard relation between the spectrum condition and the mass operator, applied to the upstream structure fields. It is not new mathematics.

### Observation 3: the zero-energy sector is the vacuum line

*Statement.* Under (PVM), W0 and `vacuumInvariant`, the range of $P(\{p:\mathrm{time}\,p=0\})$ is $\mathbb{C}\Omega$. So `HasEnergyGapAt T.theory m` together with `T.Properties _` says: the energy spectral measure of every state is carried by $\{0\}\cup[m,\infty)$, and the part at $0$ is the vacuum component. The target does not need its own vacuum clause.

*Argument.* The forward cone meets $\{\mathrm{time}=0\}$ only at $0$, so by `positiveEnergy` the projection equals $P(\{0\})$. If $P(\{0\})\psi=\psi$ then $\mu_\psi=\|\psi\|^2\delta_0$, so $\langle\psi,T(x)\psi\rangle=\|\psi\|^2$ and, since $T(x)$ is norm preserving, $\|T(x)\psi-\psi\|^2=0$. `uniqueVacuum` gives $\psi\in\mathbb{C}\Omega$. Conversely `vacuumInvariant` and `translationCompatibility` give $T(x)\Omega=\Omega$, so $\mu_\Omega=\delta_0$ and $P(\{0\})\Omega=\Omega$.

### Observation 4: shape of the bridge to the checked scalar theorem

`HasEnergyGapAt T m` holds if and only if $0<m$ and $\mu_\psi(S_m)=0$ for all $\psi$. Because $P(S_m)$ is bounded and linear, it is enough to have this for a set of vectors whose span is dense; $\Omega$ always satisfies it by Observation 3. The Lean-checked [`energy_window_zero_of_heat_bound`](../../general/2026-11-11-T02-laplace-support/LaplaceSupport.lean) has exactly this conclusion shape when instantiated with `ρ := T.energyMomentum.diagonal ψ` and `energy := time`. **This instantiation was not elaborated.** Two obligations remain and are not addressed here: identifying $\int e^{-t\,\mathrm{time}\,p}\,d\mu_\psi(p)$ with the heat correlation that a dynamical estimate would bound, and supplying the dense family with a common rate.

## Findings

1. **No vacuity or circularity found.** `GappedJointExistence` keeps every clause of upstream [`JointExistence`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean#L186-L188) and adds a conjunct on the same `T`. It implies `JointExistence` by forgetting `m`. The gap clause is an additional requirement: the upstream README states that a positive mass gap is outside its claim, and no derivation of it from `Properties` is known to this review.
2. **Energy gap versus mass gap.** By Proposition 2 the slab formulation is equivalent to the invariant-mass formulation for any theory satisfying the upstream axioms. The choice of the slab is therefore not a weakening. An uncompiled statement of the mass form is in [`SpecVariants.lean`](SpecVariants.lean).
3. **Common gap across refinements is stronger than needed for existence.** The quantifier order is $\exists C\,\exists m\,\forall p\,\exists q\,\exists T$. Reordering to $\exists C\,\forall p\,\exists q\,\exists T\,\exists m$ gives a weaker statement (`GappedJointExistencePerHierarchy` in [`SpecVariants.lean`](SpecVariants.lean), uncompiled) that still asserts a gapped theory for every requested volume sequence. The stronger form is a uniformity claim across possibly different subsequential limits. It is a legitimate target, and the baseline already labels it as stronger; this review confirms that reading and recommends that any future proof state which of the two it reaches.
4. **The value of `m` has no meaning beyond positivity.** Physical units enter only through the chosen `C`: `mesh N` is the reciprocal of `denominator N`, `place` embeds lattice sites with that spacing, and `Properties.wilson` ties `T.correlation none` to the limit of that family ([PublicWilson.lean L50–L91](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/PublicWilson.lean#L50-L91)). `WilsonRegularity.running` constrains only the leading logarithmic slope of `beta`. Since `C` is chosen before `m`, a different admissible family can rescale the gap. This is expected, but a result should not report a numerical gap as if it were canonical. This paragraph is source inspection, not a theorem.
5. **The target is witness-agnostic and concerns one phase.** The target accepts any `C` and any `T : Hierarchy C` with `Properties`. It does not name the witness built in upstream [`Solution.lean`](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/Solution.lean), `YangMills.hierarchy F Q`. The project objective speaks of the same upstream hierarchy; that is a constraint on the intended proof, not something the target enforces. Separately, `T.theory` is tied to the `selected` character through `Reconstructed.root` and `boundary` ([ChallengeSpec.lean L137–L143](https://github.com/yang-mills-group/OpenAI-YM-20261028/blob/3456e5e75cf8d4cd558955a5c7638fba2d68f464/ChallengeSpec.lean#L137-L143)), while `Properties.wilson` concerns the phase average `correlation none`. The gap is asserted for the selected phase only. The upstream structure carries no Wightman theory for the other characters, so an all-phases statement cannot be phrased on `T.theory` alone.

Minor points. `0 < m` appears both in `GappedJointExistence` and inside `HasEnergyGapAt`; this is harmless redundancy. The slab is open at `m`, so spectrum exactly at `m` is allowed, which matches "gap at least `m`"; the property is monotone downward in `m`. By reading only, no elaboration obstacle was noticed in `MassGapTarget.lean` (names resolve through the enclosing `YangMills` namespace; `Hierarchy` has no universe parameters). This is not a substitute for compiling it.

## Reproduction and evidence

From this directory:

```bash
python check_boosts.py > boost-check.json
```

Executed on 2026-11-12 with Python 3.10.6; exit code 0; output in [`boost-check.json`](boost-check.json). All arithmetic is exact rational. The checks cover: 27 rational boosts and rotations and 210 triple products are proper orthochronous, as are their Euclidean transposes (196 of the products are non-symmetric); the pairing identity $\langle p,\Lambda x\rangle=\langle\Lambda^{\mathsf T}p,x\rangle$ on 1500 cases; 400 timelike orbit cases returning to rest energy $\mu$; 27 lightlike cases boosted into a prescribed slab; 2295 grid points for $S_m\subseteq R_m$ and the cone intersection; and one explicit point showing the covariance hypothesis is used.

These checks test the finite-dimensional algebra in steps 3 and 4 on samples. They do not test steps 1, 2, 5, 6, either observation, or any finding. Upstream hash recomputation used `git show <commit>:<path> | sha256sum`; on a Windows checkout with line-ending conversion the working-tree files hash differently, so hash the Git blobs.

No Lean command was run. [`SpecVariants.lean`](SpecVariants.lean) is uncompiled, contains definitions only, and is excluded from every proof claim.

## Outcome and limits

- Established in writing, conditional on the listed upstream fields: Observation 1, Proposition 2, Observation 3.
- Recorded by source inspection: Observation 4 and the five findings.
- Not established: that the target holds; that `MassGapTarget.lean` or `SpecVariants.lean` elaborate; that `Measure.ext_of_charFun` applies to `Spacetime` without further instance work; any dynamical estimate.
- The written arguments are standard and were produced with AI assistance. They have not been reviewed by a second person.

## Failure lesson or revised expectation

No failure is recorded. Revised expectations for later work:

- Do not spend effort re-deriving a mass-shell formulation: under the upstream axioms it is equivalent to the slab, and the slab is the form that the checked scalar Laplace theorem feeds.
- Any claimed gap should say whether its rate is common across volume refinements (the present target) or per hierarchy, and should not present the numerical value as canonical.
- State targets only on measurable sets of the PVM.

## Track contributions and next experiment

- T01: first specification review recorded. Next bounded task: elaborate `MassGapTarget.lean` and `SpecVariants.lean` against the pinned upstream build and record the receipt; then formalize Proposition 2. Success criterion: Lean 4.32.0 accepts both files without `sorry`, with an axiom report. Dependency: a pinned upstream build with Mathlib. The proof of Proposition 2 needs characteristic-function uniqueness and a Lindelöf step and is expected to be the main cost.
- T02/T07: Observation 4 names the instantiation of the checked scalar theorem at the public PVM. Next task: elaborate that instantiation as a lemma `HasEnergyGapAt` from per-state heat bounds on a spanning dense set.
- T05: Finding 5 records that the target concerns the selected phase only.

## Review and correction history

- 2026-11-12: initial record. No corrections.
