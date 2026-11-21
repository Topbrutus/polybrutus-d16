# Polybrutus 16D: Exact Conservative Euclidean Completion and a Tenfold Weighted-Graph Mode

**Research author:** Gabriel St-Pierre  
**Affiliation:** Independent researcher  
**Project:** Polybrutus-X72  
**Date:** 20 November 2026  
**Version:** 0.1.0  
**Status:** Mathematical computational preprint, without independent human peer review  
**Predecessor:** Polybrutus 15D, DOI 10.5281/zenodo.24408887  
**Frozen scientific code:** https://github.com/Topbrutus/polybrutus-d16/tree/v0.1.0 (upon public release)

## Abstract

An exact **twenty-one-point labelled Euclidean distance configuration** is constructed, with **minimal affine embedding dimension sixteen**, by a conservative orthogonal extension of the frozen Polybrutus 15D metric. All **190 previous labelled pairwise squared distances** remain unchanged. One new orthogonal radius-R point adds **20 squared distances of exactly 2R²**, producing **210 labelled pair distances** in eight exact normalized families. Two independently implemented verifiers establish the complete metric, the exact affine dimension, and a centered Euclidean distance Gram certificate. The primary verifier additionally proves an exact positive-semidefinite Gram factorization.

For a deliberately **chosen theoretical complete weighted-graph scalar-oscillator model**, with dimensionless couplings `w_ij=R²/d_ij²` and equal scalar masses, the exact graph Laplacian has **an eigenvalue 21/2 of multiplicity ten** and **an eigenvalue 10 of multiplicity four**. These are properties of a particular mathematical model, independently verified using the full exact characteristic polynomial. Neither new spacetime physics, empirical resonances, nor a novel universal mathematical theorem is claimed.

## 1. Research provenance and frozen predecessor

Polybrutus begins with seven analytically defined points on a Euclidean three-dimensional sphere. An orthogonal completion with five vertices of a regular four-dimensional simplex produced the published 7D twelve-point metric, preserving the original seven labelled points. That record is [DOI 10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952).

The subsequent research programme archived individual exact computational case studies: 8D, 13 vertices and 78 pairs (DOI 10.5281/zenodo.24408344); 9D, 14 vertices and 91 pairs (DOI 10.5281/zenodo.24408448); 10D, 15 vertices and 105 pairs (DOI 10.5281/zenodo.24408569); 11D, 16 vertices and 120 pairs (DOI 10.5281/zenodo.24408650); 12D, 17 vertices and 136 pairs (DOI 10.5281/zenodo.24408720); 13D, 18 vertices and 153 pairs (DOI 10.5281/zenodo.24408769); 14D, 19 vertices and 171 pairs (DOI 10.5281/zenodo.24408836); and 15D, 20 vertices and 190 pairs (DOI 10.5281/zenodo.24408887).

The current 16D calculation starts exclusively from the **immutable source tag** `Topbrutus/polybrutus-d15@v0.1.0`, commit `680182c69307fe1be8df831cf7b8eacae2f8ff62`. The frozen predecessor source and certificate files are included unchanged in the new `prior/` audit directory. The previous geometry is neither perturbed nor regenerated approximately.

## 2. Construction: twenty-one exact labelled points

Normalize `R=1`. Let `p1,...,p20` be the exact twenty previous radius-one Polybrutus 15D vectors, represented using sixteen coordinate-storage slots. Five of these slots represent a centered regular simplex in a four-dimensional hyperplane and therefore obey one exact linear constraint.

Embed each old point by adding a zero last coordinate:

```
q_i = (p_i,0),            1 <= i <= 20.
```

Adjoin a new orthogonal unit vector in the seventeenth storage slot:

```
q21 = e17 = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1).
```

All twenty-one vectors have norm one, and `q21` is orthogonal to every old vector. Therefore, each of the old **190 distances** remains exactly the same, while every new distance obeys:

```
||q21-q_i||² = ||q21||²+||q_i||²-2<q21,q_i> = 2.
```

There are `C(21,2)=210` labelled unordered pairs: 190 old and twenty new. For general radius `R>0`, scale all vectors by `R` so that new squared pair distances are `2R²`.

The complete exact histogram for normalized squared-distance parameter `k=4d²/R²` is

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity | 6 | 2 | **179** | 3 | 10 | 6 | 2 | 2 |

The counts sum to **210**, and the exact total of pairwise squared lengths is

```
sum_{i<j} d_ij² / R² = 1727/4.
```

At radius one the exact centroid in seventeen storage slots is

```
G = (0,0,1/42,0,0,0,0,0,1/21,1/21,1/21,1/21,1/21,1/21,1/21,1/21,1/21).
```

These seventeen storage coordinates are a representation of an **affine sixteen-dimensional metric**: one exact simplex-hyperplane relation remains.

## 3. Exact Gram certificate and minimal affine rank

Let `X` be the full 21-by-17 exact coordinate matrix, and let `D` be the 21-by-21 **squared Euclidean distance matrix**. Define the centering projection `H=I-11ᵀ/21`. The centered Euclidean distance Gram matrix is

```
B = -1/2 H D H.
```

The primary exact symbolic verifier establishes all three properties:

```
rank([q2-q1,...,q21-q1]) = 16;
rank(B) = 16;
B = (H X)(H X)^T.
```

The third identity gives an exact **positive-semidefinite factorization** of the centered Gram. The complete labelled Euclidean distance matrix determines its centered Gram uniquely, therefore **every Euclidean realization** with the same exact 210 labelled squared distances has minimal affine embedding dimension precisely **sixteen**. This is a mathematical dimension certificate rather than an assertion of extra physical spacetime dimensions.

A second separately implemented program does not import the primary or ancestor point generator. Instead, it independently derives each squared distance from rational rules for the original seven points, the five-vertex regular-simplex internal squared distance `5/2`, and the successive mutually orthogonal unit-axis points. It reproduces **all 210 labelled distances** and verifies the centered Gram rank **16**; it additionally checks the **190** predecessor pair values exactly.

## 4. A tenfold mode in a chosen ideal weighted graph

For an illustrative scalar-oscillator graph, assign a hypothetical scalar displacement and equal unit mass to each vertex. Connect every unordered pair with a positive dimensionless weight `w_ij=R²/d_ij²`. These weights are **a modelling choice**, not extracted from any real apparatus.

The newly appended vertex lies at squared radius-normalized distance `2` from all twenty preceding points, so each new graph edge has weight `1/2`. Let `L15` be the twenty-vertex parent graph Laplacian. Then the new 21-by-21 Laplacian satisfies the exact block identity

```
L16 = [ L15+(1/2)I20      -(1/2)1 ]
      [ -(1/2)1ᵀ                10 ].
```

Write `chi20(z)=det(zI-L15)` and `chi21(z)=det(zI-L16)`. A decomposition of the global uniform mode, one intergroup mode and all parent zero-sum modes proves the graph spectral recurrence

```
chi21(z)=z(z-21/2)chi20(z-1/2)/(z-1/2).
```

The frozen predecessor factorization is

```
chi20(z)=z(z-10)^9(z-19/2)^4 f6(z-13/2),
f6(z)=chiP7(z)/z,
```

where `chiP7` is the characteristic polynomial of the original seven-point complete weighted graph and `f6` describes its six nonzero modes. Substituting the parent expression into the recurrence gives

```
chi21(z)=z(z-21/2)^10(z-10)^4 f6(z-7).
```

The primary program explicitly computes the full exact **21-by-21 characteristic polynomial** and proves equality to this closed form. It verifies that `f6(7/2)!=0` and `f6(3)!=0`, excluding accidental additional root multiplicities. The eigenvalue at **21/2 has exact multiplicity ten**, while the eigenvalue at **10 has exact multiplicity four**.

The independent rational-metric verifier constructs the full weighted graph separately, computes its exact characteristic polynomial and checks both multiplicities by testing its derivatives at the two designated roots. All model eigenvalues are dimensionless in this normalization; they are **not** experimentally measured vibrations or frequencies in hertz.

## 5. Reproducibility and falsification

The scientific repository includes exact geometric source `src/verify_d16.py`, the independently written rational checker `tests/independent_d16.py`, `results/certificate_d16.json` with all **210 labelled exact squared distances**, the entire frozen ancestor source chain in `prior/`, the specification, a proof file, provenance, a GitHub Actions workflow and an SHA-256 index of frozen Git blobs.

To reproduce:

```sh
python -m pip install sympy==1.14.0
python src/verify_d16.py
python tests/independent_d16.py
```

Both programs must report PASS and the same SHA-256 for the regenerated 210-pair JSON certificate. Four deliberately invalid variants are detected: (1) tampering with a distance value, (2) duplicating a point and lowering affine rank, (3) inserting a nonorthogonal point, and (4) swapping labels while preserving the unlabelled distance histogram.

The Zenodo record deposits the exact frozen Git-tag source archive ZIP, the present scientific PDF and the JSON certificate. Their sizes and checksums enable later byte-level verification. The source is linked by its exact Git tag and commit, without overwriting earlier scientific releases.

## 6. Scientific precedence and interpretative limits

Orthogonal completion of labelled Euclidean configurations, centered squared-distance Gram matrices and uniform weighted-graph attachment are mathematical techniques with prior antecedents. This preprint is a reproducible exact **Polybrutus sixteen-dimensional case study**, not a claim to have invented those general operations. The sixteen-dimensional statement concerns the **minimal affine embedding rank of twenty-one mathematical points**; it is not evidence for a sixteen-dimensional physical universe or a measured resonance. There is no claim of new particle physics or independent human peer review.

## 7. Author responsibility, generative AI disclosure and rights

**Human research author and responsible investigator:** Gabriel St-Pierre, independent researcher. The canonical Polybrutus project, staged publication programme and research direction originate with him.

**Generative AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted mathematical proof checking, source auditing, exact symbolic implementation, the separately implemented rational-metric verifier, graph-spectral analysis, documentation, manuscript drafting and release operations. This tool is **not listed as an author**. Human scientific peer review remains pending.

**Licenses:** scientific note and prose CC BY 4.0, source programs MIT.

**Predecessor sources:** canonical Polybrutus geometry https://github.com/Topbrutus/polybrutus/blob/main/SPECIFICATION.md ; 7D https://doi.org/10.5281/zenodo.24407952 ; 8D https://doi.org/10.5281/zenodo.24408344 ; 9D https://doi.org/10.5281/zenodo.24408448 ; 10D https://doi.org/10.5281/zenodo.24408569 ; 11D https://doi.org/10.5281/zenodo.24408650 ; 12D https://doi.org/10.5281/zenodo.24408720 ; 13D https://doi.org/10.5281/zenodo.24408769 ; 14D https://doi.org/10.5281/zenodo.24408836 ; 15D https://doi.org/10.5281/zenodo.24408887 ; frozen D15 source https://github.com/Topbrutus/polybrutus-d15/tree/v0.1.0 .
