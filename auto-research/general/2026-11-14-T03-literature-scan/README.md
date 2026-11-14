# Literature scan: adjacent approaches not yet tried in this notebook

## Metadata

- Result ID and date: `2026-11-14-T03-literature-scan`; 2026-11-14.
- Author: Rohan Arun, with Claude (Anthropic) assistance in a Claude Code session.
- Tracks: T03 primary; T06 and T07 related.
- Outcome: **candidate list, not a result.** It identifies approaches in neighbouring fields that the notebook has not used, states what each could and could not do, and proposes one cheap falsifiable test per candidate. It proves nothing about Yang–Mills and gives no evidence that any candidate works.
- Evidence level: source inspection at the weakest levels, tagged per claim below. No computation.
- Repository base commit: `ff784a0`.
- Related: the geometric records (curvature scope, typical-curvature, posterior-Hessian review).

## How the evidence was gathered, and its limits

- Web searches returned titles and snippets. Tag **[S]** means a claim rests on a snippet only.
- A delegated reader fetched abstract pages. Tag **[A]** means the abstract page was read. Abstracts can overstate or understate a paper's result.
- The Bauerschmidt–Bodineau paper was read by a delegated reader in verbatim text for Sections 1 and 2 only; Section 3 and the appendix were available only as a model-generated summary. Tag **[V]** means verbatim, **[V-partial]** means the rest was summary.
- Tag **[U]** means unverified or from general knowledge.
- Not searched: Hamiltonian truncation and tensor-network approaches, integrability and large-$N$ solvability beyond the area-law papers, center-vortex and Gribov–Zwanziger pictures, and any paper after the search tool's coverage. Absence from this list is not absence from the literature.

## Candidates

### 1. Multiscale (Polchinski) Bakry–Émery criteria

- **Source.** Bauerschmidt–Bodineau, *Log-Sobolev inequality for the continuum sine-Gordon model* (CPAM 2021), [arXiv:1907.12308](https://arxiv.org/abs/1907.12308); Bauerschmidt–Bodineau–Dagallier survey, *Stochastic dynamics and the Polchinski equation* (Probab. Surveys 21, 2024), [arXiv:2307.07619](https://arxiv.org/abs/2307.07619); Bauerschmidt–Dagallier, near-critical Ising and $\phi^4_{2,3}$, [arXiv:2202.02301](https://arxiv.org/abs/2202.02301), [arXiv:2202.02295](https://arxiv.org/abs/2202.02295).
- **What is established [V, Sections 1–2].** The criterion lives on a linear field space $X\subset\mathbb R^N$ with a Gaussian covariance decomposition $C=\int\dot C_t\,dt$ and a renormalised potential $V_t$ satisfying the Polchinski equation. The hypothesis is a one-sided bound on the Hessian of $V_t$ **uniform over all field configurations** (for every scale $t$), and the conclusion is a log-Sobolev inequality with constant given by an explicit integral. Hessians of $V_t$ need not be positive; the paper says the renormalised potential stays non-convex at all scales for sine-Gordon. When the bare potential is convex (with a scalar mass operator) the criterion recovers ordinary Bakry–Émery.
- **What it achieves [V, S].** Log-Sobolev inequalities for models whose bare potential is far outside the Bakry–Émery regime (sine-Gordon for $\beta<6\pi$ [V-partial]) and near-critical Ising in $d>4$, which uses a known mean-field susceptibility bound [S].
- **Relevance.** It is the clearest published mechanism for passing from pointwise non-convexity (which this notebook has measured for the Wilson measure) to a spectral conclusion. $\phi^4_{2,3}$ (superrenormalisable) is the nearest analogue of three-dimensional Yang–Mills.
- **Obstacles.** (a) I found **no** formulation for group-valued or gauge fields; the survey's spin models take values in $\mathbb R^n$ [S]. A lattice experiment on $SU(2)$ links would therefore not test the published criterion. (b) In a linear gauge-fixed formulation the Yang–Mills Hessian is expected to be unbounded below (an indefinite term proportional to the field strength, the Nielsen–Olesen-type structure), which would break the uniform hypothesis at $t=0$ [U]. In the compact lattice formulation the Hessian is bounded (the notebook's $8(d-1)\beta$) but the flow is not defined. (c) The route past the scale where the tilted measure stops being log-concave is exactly where the published proofs need cluster-expansion input (Section 3 of the sine-Gordon paper [V-partial]).
- **Cheapest falsifiable test.** On paper: compute whether $\inf_A\mathrm{Hess}\,S_{\rm YM}$ in a linear gauge is bounded below. If unbounded, the uniform hypothesis fails as stated and a modified formulation (large-field cutoff, as in Balaban's decomposition) is required. Cost: written analysis.

### 2. Localization schemes and spectral independence

- **Source.** Chen–Eldan, *Localization schemes* [arXiv:2203.04163](https://arxiv.org/abs/2203.04163) [A]; Eldan–Koehler–Zeitouni, *A spectral condition for spectral gap* [arXiv:2007.08200](https://arxiv.org/abs/2007.08200) [A]; weak Poincaré inequalities and spherical spin glasses, [arXiv:2411.09075](https://arxiv.org/abs/2411.09075) [S].
- **What is established.** The localization-scheme framework unifies spectral independence and stochastic localization [A]. For Ising models with quadratic interactions a Poincaré inequality holds when the **operator norm** of the interaction matrix is below a threshold (the abstract states below one; a talk uses one half with different normalisation, so the constant needs checking against the paper) [A, S]. A 2024 paper treats spherical spin glasses (a compact-manifold-valued spin) using bounds on the operator norm of a covariance matrix [S].
- **Relevance.** The notebook's recurring obstruction is a posterior covariance matrix. The criterion in the posterior-curvature record uses an absolute **row sum** of covariance blocks. Spectral-independence arguments use the **operator norm**, which can be far smaller than a row sum when correlations have mixed signs. That is a concrete, quantitative improvement available to the existing reduction.
- **Obstacles.** The cited results are for quadratic (Ising-type) interactions or spin glasses; a plaquette interaction is multilinear in group elements. I did not find an application to gauge theory [S]. Uniformity over all pinnings is required.
- **Cheapest falsifiable test.** On the posterior-covariance matrices already computable in the toy models of the posterior-curvature record, compare the operator norm with the maximal row sum. Success: operator norm at most half the row sum in a nontrivial model. Cost: small. This improves constants, not the regime.

### 3. Weak-coupling decay for finite gauge groups

- **Source.** Adhikari–Cao, *Correlation decay for finite lattice gauge theories at weak coupling*, Ann. Probab. 53 (2025), [arXiv:2202.10375](https://arxiv.org/abs/2202.10375) [A].
- **What is established [A].** Exponential decay of correlations for finite, possibly non-abelian gauge groups at weak coupling, for a broad class of gauge-invariant observables.
- **Relevance and obstacle.** Finite groups have an energy gap for plaquette excitations, which is absent for $SU(2)$, where weak coupling is Gaussian-like with soft modes. I expect the weak-coupling threshold in such results to depend on the group size, so they would not transfer along a sequence of finite subgroups approaching $SU(2)$, but I did not read the theorem to check this [U].
- **Cheapest falsifiable test.** Read the theorem and record the dependence of its coupling threshold on $|G|$. If it grows with $|G|$ the route is closed for continuous groups; if it is uniform, it would be a major result and should be checked with great care. Cost: reading.
- **On $E_8$.** The binary icosahedral subgroup of $SU(2)$ corresponds to $E_8$ under the McKay correspondence, so $E_8$ is relevant here only as a discretisation of $SU(2)$, with the dependence just described. I found no mechanism by which $E_8$ would enter a four-dimensional $SU(N)$ estimate.

### 4. Orbit-space geometry and the ground-state-weighted measure

- **Source.** Moncrief–Marini–Maitra, [arXiv:1809.06318](https://arxiv.org/abs/1809.06318) [A]; Mondal, *A geometric approach to the Yang–Mills mass gap*, [arXiv:2301.06996](https://arxiv.org/abs/2301.06996) [A].
- **What is established [A].** Both describe a Bakry–Émery Ricci tensor on the orbit space weighted by the ground-state wave functional. Mondal's abstract calls the gap calculation heuristic and not rigorous, assuming a quantised theory exists; the page shows no publication or withdrawal. Moncrief et al. state the same framework in their abstract.
- **Relevance.** This is the Hamiltonian counterpart of the notebook's Euclidean curvature experiments.
- **Observation (informal, [U]).** For infinite time extent the ground-state measure $|\Psi_0|^2$ on a spatial slice is the slice marginal of the Euclidean measure, so its Bakry–Émery tensor again has the form $\mathbb E[\mathrm{Hess}]-\mathrm{Cov}(\nabla)$ under a conditional measure. If correct, this route reduces to the same posterior-covariance control.
- **Cheapest falsifiable test.** Derive the identity carefully on a finite lattice with a transfer matrix (written derivation), then check it numerically on a toy with an exactly diagonalisable ground state. Cost: moderate.

### 5. Constructive renormalisation

- **Source.** Dimock's expository series on Balaban's renormalisation group ([arXiv:1108.1335](https://arxiv.org/abs/1108.1335), [arXiv:1212.5562](https://arxiv.org/abs/1212.5562)) [S]; Magnen–Rivasseau–Sénéor, *Construction of $YM_4$ with an infrared cutoff*, [mp_arc 92-38](https://web.ma.utexas.edu/mp_arc/a/92-38) [S].
- **What is established [S].** Magnen–Rivasseau–Sénéor construct four-dimensional pure $SU(2)$ Yang–Mills Schwinger functions in the trivial topological sector with a **fixed infrared cutoff** and no ultraviolet cutoff, using axial-gauge positivity for large fields and a different gauge for small fields. Dimock's series treats Balaban's ultraviolet stability bounds and notes that the Yang–Mills bounds in $d=3,4$ are Balaban's [S].
- **Relevance.** The gap lives precisely in removing the infrared cutoff. The upstream construction audited in this notebook is a lattice analogue of this program.
- **Obstacle.** No part of this scan addresses the infrared problem; the search results state the infrared cutoff was kept fixed.
- **Cheapest test.** None proposed; this is background for judging how far the upstream construction could plausibly go.

### 6. Stochastic quantisation and area-law results (context)

- Chandra–Chevyrev–Hairer–Shen and Chevyrev–Shen on three-dimensional stochastic quantisation of Yang–Mills–Higgs, [arXiv:2201.03487](https://arxiv.org/abs/2201.03487) [S]: a gauge-covariant Markov process on the orbit space, locally in time; a 2026 follow-up states that the scaling limit of the lattice dynamics is open [S].
- Cao–Chatterjee, *A state space for 3D Euclidean Yang–Mills theories*, [arXiv:2111.12813](https://arxiv.org/abs/2111.12813) [S].
- Shen–Zhu–Zhu, [arXiv:2204.12737](https://arxiv.org/abs/2204.12737) [S]: strong-coupling Poincaré and log-Sobolev inequalities and a mass gap for $|\beta|<1/[16(d-1)]$ (already in the notebook).
- Cao–Nissim–Sheffield, *Expanded regimes of area law for lattice Yang–Mills theories*, [arXiv:2505.16585](https://arxiv.org/abs/2505.16585) [A]: enlarges the parameter regime for the area law for $U(N)$, via the master loop equation. An area law is not a mass gap.
- Chatterjee, [arXiv:2006.16229](https://arxiv.org/abs/2006.16229) [S]: states that a mass gap is comparatively easy at large coupling and that four-dimensional $SU(3)$ at all couplings remains open.

## Claims to disregard

Several search results claim or imply a solution. They are not relied on: a 2025 preprint claiming a constructive proof for $SU(3)$ ([arXiv:2506.00284](https://arxiv.org/abs/2506.00284)) is reported withdrawn by arXiv administrators [S]; a conditional single-author preprint ([arXiv:2406.16881](https://arxiv.org/abs/2406.16881)) states its confinement result assuming the gap exists, lists no journal publication and is in a general-mathematics category [A]; a recent preprint on charge conjugation and the mass gap ([arXiv:2509.03513](https://arxiv.org/abs/2509.03513)) was not read and its status is unknown [S]. Mondal's preprint is conditional and heuristic by its own abstract [A].

## Cross-cutting observation

Three formulations met in this scan end in the same object. (i) Coarse-graining a gauge field (posterior-curvature record). (ii) The heat-flow or Polchinski renormalised potential, whose Hessian in flat space is $I/t-t^{-2}\mathrm{Cov}_\pi(y)$ under the tilted measure $\pi$ (a standard Tweedie-type identity, derived here from memory and not checked numerically). (iii) The ground-state slice marginal (informal, above). In each, the curvature of an effective potential equals an expectation of Hessians minus a covariance of gradients under a conditional measure. If that is right, the geometric programme is equivalent to controlling a conditional covariance, which is the same missing estimate the notebook has isolated several times. A published multiscale criterion is a way to *use* such control across scales, not a way to avoid proving it.

## What would make a faithful multiscale test

(a) A formulation of the Polchinski flow and its Hessian criterion for compact-group-valued fields, replacing the Gaussian reference with heat-kernel smoothing and the flat Hessian with the Riemannian one; none was found. (b) A model in the formulation's native setting where the answer is known, to validate the machinery before applying it to gauge fields. (c) Only then a gauge-invariant lattice experiment. Until (a) exists, an $SU(2)$ lattice toy would not test the published criterion.

## Recommendation, with honest odds

None of these candidates is likely, on present evidence, to close the infrared problem. The two with a cheap, falsifiable first step are candidate 2 (operator norm versus row sum) and the reading task in candidate 3 ($|G|$-dependence). Candidate 1 is the most promising direction in the literature but requires a formulation that does not exist in anything I found.

## Review and correction history

- 2026-11-14: created. Single AI session; evidence levels as tagged; no independent review.
