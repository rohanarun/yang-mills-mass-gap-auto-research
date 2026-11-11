# Transfer assessment of the YM3D verification program

## Metadata and question

- Date / tracks: 2026-11-11; T03, T04, T07.
- Assessment: Rohan Arun, with OpenAI Codex assistance, following the user's repository suggestion.
- Our base: `72f573c274bf0a53717bb4a98f0691908a39bc45`.
- External repository: [HiroSakuraba/Yang-Mills-3D-AI-verification-program](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/tree/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d), pinned at `fc63a83a6cd1746f89f546b9f6bcdf50381ae16d`.
- Authorship: the repository README attributes the design and cited working notes to Benjamin John Schulz. These are external contributions, not work by this project or an endorsement of it. The external repository is MIT-licensed; no implementation is copied here.
- Question: does it supply the missing exponential estimate, or reusable intermediate evidence for our four-dimensional construction?
- Evidence: selected source inspection and local replay of two supplied checkers plus their two test suites. No general analytic proof, Lean replay, full harness verification, or novel theorem is established by this assessment.

**Assessment: useful methods, finite checks, and overlapping audits; no missing Yang–Mills decay estimate found in the inspected material.** This is a scoped assessment, not a review of every file.

## What can transfer

1. **Explicit proof dependencies.** Its gate graph, separate generators/checkers, artifact hashes, and claim restrictions are useful patterns for preventing a finite calculation from being promoted into a continuum theorem. Passing a supplied checker is still distinct from an independent mathematical proof of what it implements. We replayed selected tests; we did not validate all harness guarantees.
2. **An audit of the same 4D source.** Its [spectral bridge](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/blob/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d/docs/upstream-4d-lean-audit/SPECTRAL_GAP_BRIDGE_3.md) uses our pinned OpenAI revision and describes the same standard positivity/density route. It correctly retains a common exponential rate and explains why a polynomial prefactor does not change the spectral threshold. This supports the formulation of our target; it does not discharge its dynamical hypothesis. A Hamiltonian obtained from a transfer operator also needs the stated injectivity/domain qualification.
3. **A finite signed-polymer comparison.** Its [finite-gas note](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/blob/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d/docs/upstream-4d-lean-audit/FINITE_GAS_TRANSFER.md) gives an elementary product-telescoping bound with a fixed admissibility family. That algebra is dimension-independent and could be used once activities, supports, and hypotheses are matched. The supplied 3D rational example verifies finite combinatorics and arithmetic, not Wilson-derived activities or uniform RG control.
4. **Useful failure cases.** Its tests reject changed admissibility, corrupted bounds, false gate closure, and false continuum claims. We can adopt the research expectation that every imported estimate must retain its exact law, normalization, geometry, coupling regime, and quantified limits.

## Why this does not yet supply Step 3

The main program targets **three-dimensional SU(2)**. Its [plaquette-clustering lane](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/blob/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d/lanes/plaquette_clustering/README.md) proposes fixed-spacing, small-beta estimates and explicitly leaves analytic review open. Its [strong-coupling KP lane](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/blob/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d/lanes/strong_coupling_kp_domain/README.md) is blocked behind a validation guard and disclaims continuum clustering. We did not replay those more expensive enumerations or certify their analytic bounds.

The spectral bridge itself explains the regime mismatch: in its 3D convention $\beta(a)=4/(g_3^2a)$ grows as spacing $a$ tends to zero, whereas its sufficient Dobrushin bound requires $12\beta<1$. Changing dimension changes both geometry and coupling scaling. Substituting four for three in a checker cannot establish the 4D result.

It also contains separate [4D Wilson comparison notes](https://github.com/HiroSakuraba/Yang-Mills-3D-AI-verification-program/blob/fc63a83a6cd1746f89f546b9f6bcdf50381ae16d/docs/ym4-wilson-audit/Wilson-comparison-and-gap-lemma.md). Those carefully distinguish certified coefficient sums from physical clustering and still require a proof placing the **full generated effective action**, including additional interactions, inside the proposed basin. We have not reproduced their interval certificates. Their numerical frontier is not an established physical mass-gap threshold.

## The precise connection to our conditional-law problem

Write $Z_{\mathcal F}(p)=\sum_{S\in\mathcal F}\prod_{i\in S}p_i$. The finite-gas argument bounds $|Z_{\mathcal F}(p)-Z_{\mathcal F}(q)|$ when both sums use the same $\mathcal F$. A change in support tests or flags can change $\mathcal F$ and requires an additional eligibility-change term. Its explicit counterexample confirms that identical coefficients are insufficient when admissibility changes.

Even when admissibility is fixed, an absolute bound on a signed gas does not provide the relative control needed after normalizing a positive probability law. Dividing a small absolute error by an uncontrolled small denominator can destroy its usefulness. The external example's gas sums are even negative; they are algebraic sums, not probability densities. Our [normalization control](../../negative-results/2026-11-11-T03-conditional-normalization/README.md) already exhibits the corresponding positive-density obstruction.

Our [buffered-posterior reduction](../2026-11-11-T03-buffered-posterior/README.md) identifies the more specific quantity: the covariance of a local hidden-prediction observable with a distant likelihood ratio under the actual posterior. The inspected external estimates do not bound that covariance. A productive transfer task is to derive **relative, spatially decaying** changes from actual Yang–Mills activities, accounting for eligibility changes and all generated interactions. A finite gas-difference calculation would then be one checked ingredient.

## Replay and limits

[Verification receipt](verification.json) pins source hashes, commands, durations, and output hashes. From the external repository root, with Python 3.11.15, bytecode disabled and temporary outputs on the SSD:

```sh
python3.11 -B tools/check_finite_gas_transfer.py docs/upstream-4d-lean-audit/finite_gas_seed.json
python3.11 -B -m unittest discover -s tests -p 'test_finite_gas_transfer.py' -v
python3.11 -B tools/check_mass_gap_obligations.py docs/upstream-4d-lean-audit/mass_gap_obligations.json
python3.11 -B -m unittest discover -s tests -p 'test_mass_gap_obligations.py' -v
```

Both checkers exited zero. The suites passed **12 + 17 = 29 tests**; see [finite example output](check-1.txt), [finite example tests](check-2.txt), [obligation output](check-3.txt), and [obligation tests](check-4.txt). They include exact finite identities, invalid-input controls, coupling arithmetic, and examples showing why limited observable or lattice information is insufficient. The obligation checker explicitly reports that it has not verified the analytic theorem.

This is independent execution of the external authors' tests, not an independently written verifier or a full mathematical review. No 3D or 4D mass gap has been established here.

## Next bounded task and review

Use the fixed-admissibility lemma only after mapping actual upstream labels, masks, and conditional normalizers. Determine whether a crossing-activity budget can bound the local posterior response uniformly in cutoff and volume. Stop the inference if it only supplies an absolute gas error, a fixed-spacing estimate, or an assumed exponential rate.

Review status: selected source assessment and test replay by the current assistant, 2026-11-11. External analytic claims remain unverified by this project. No messages were sent to external authors and no external repository state was changed.
