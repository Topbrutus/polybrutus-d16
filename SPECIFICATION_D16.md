# Polybrutus D16 — Formal twenty-one-point exact Euclidean configuration

**Immutable parent:** `Topbrutus/polybrutus-d15@v0.1.0`, source commit `680182c69307fe1be8df831cf7b8eacae2f8ff62`, DOI `10.5281/zenodo.24408887`.

## Exact construction

Let `p1,...,p20` be the frozen Polybrutus D15 points on a unit sphere, represented in 16 storage slots. Their five-simplex coordinate block has one exact centered-hyperplane linear constraint.

Embed all old vertices as `q_i=(p_i,0)` in 17 storage slots for `i=1,...,20`. Adjoin `q21=e17=(0,...,0,1)`. The new point is orthogonal to all old vectors and has norm 1, hence

```
||q21-q_i||² = 1+1-0 = 2,  for all i=1,...,20.
```

All **190 parent distances remain unchanged**. One obtains **20** new labelled distances and `C(21,2)=210` in total. Scaling by radius `R>0` multiplies every squared distance by `R²`.

Normalized histogram for `k=4d²/R²`:

| k | 4 | 7 | 8 | 9 | 10 | 12 | 13 | 16 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Number of labelled pairs | 6 | 2 | **179** | 3 | 10 | 6 | 2 | 2 |

The sum of all squared distances is `1727 R²/4`. For unit radius the centroid in 17 storage slots is `(0,0,1/42,0,0,0,0,0,1/21,1/21,1/21,1/21,1/21,1/21,1/21,1/21,1/21)`.

The exact **intrinsic affine rank is 16**, not 17; the centered five-simplex coordinate relation accounts for one redundant storage coordinate.

## Selected theoretical graph

Define an ideal equal-mass scalar-oscillator graph on the 21 vertices with complete weights `w_ij=R²/d_ij²`. The twenty new edges each have weight 1/2, so for the parent twenty-vertex graph Laplacian `L15`:

```
L16 = [ L15+(1/2)I20     -(1/2)1 ]
      [ -(1/2)1ᵀ               10 ].
```

Let `f6(z)=chiP7(z)/z` for the six nonzero modes of the original seven-vertex graph. Then

```
chi21(z)=z(z-21/2)*chi20(z-1/2)/(z-1/2)
        =z(z-21/2)^10(z-10)^4*f6(z-7).
```

Eigenvalue 21/2 has multiplicity **10** and eigenvalue 10 multiplicity **4**. Both apply only to this chosen mathematical graph model.
