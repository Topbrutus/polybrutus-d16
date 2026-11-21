# Polybrutus D16 — Exact metric, Gram and ideal-graph spectrum certificate

## 1. Preserve the labelled 15D metric

Take the frozen twenty unit vectors `p1,...,p20` and embed `q_i=(p_i,0)` for `i<=20`. Add `q21=e17` orthogonal to every old point. All preceding **190 labelled squared distances** remain identical. Every new squared distance obeys

```
||q21-q_i||² = ||q21||² + ||q_i||² - 2<q21,q_i> = 2.
```

There are `190+20=C(21,2)=210` labelled pairs. The exact normalized histogram `k=4d²/R²` is `{4:6,7:2,8:179,9:3,10:10,12:6,13:2,16:2}`, and the sum of squared distances is exactly `1727R²/4`.

## 2. Exact minimal Euclidean affine dimension

Write `X` for the exact 21-by-17 coordinate array, `D` for the 21-by-21 squared-labelled-distance matrix and `H=I-11ᵀ/21` for centering. The primary exact checker proves:

```
rank([q2-q1,...,q21-q1]) = 16;
rank(B) = 16;
B = -H D H/2 = (H X)(H X)^T.
```

The factorization proves that the centered Gram `B` is positive semidefinite. Any Euclidean realization of these **same labelled distances** produces the same centered Gram matrix, so no lower-dimensional Euclidean realization exists: minimal affine rank is precisely **16**. The 17 storage slots have one exact simplex-hyperplane linear constraint.

## 3. Spectrum of the chosen ideal weighted graph

For a mathematically chosen complete graph with equal scalar masses and `w_ij=1/d_ij²` at unit radius, the new point has 20 uniform edges of weight `1/2`. Let `L15` be the previous 20-vertex graph Laplacian. The new Laplacian is

```
L16 = [ L15+(1/2)I20     -(1/2)1 ]
      [ -(1/2)1ᵀ               10 ].
```

Let `chi20(z)=det(zI-L15)` and `chi21(z)=det(zI-L16)`. A decomposition into the global zero mode, one intergroup mode, and old shifted zero-sum modes yields:

```
chi21(z) = z(z-21/2)chi20(z-1/2)/(z-1/2).
```

The earlier verified D15 factorization is `chi20(z)=z(z-10)^9(z-19/2)^4*f6(z-13/2)` with `f6(z)=chiP7(z)/z`. Therefore:

```
chi21(z) = z(z-21/2)^10(z-10)^4*f6(z-7).
```

The full 21-by-21 exact characteristic polynomial is independently calculated and compared to this closed form. Since `f6(7/2)!=0` and `f6(3)!=0`, the designated model eigenvalues have **exact multiplicities ten** at 21/2 and **four** at 10. A separate rational-metric verifier rebuilds all 210 pairs and checks multiplicities using derivatives of its independently constructed characteristic polynomial.

## 4. Negative controls and interpretation

Four invalid controls must fail: (1) corrupting a labelled squared distance, (2) duplicating a point and lowering rank, (3) adding a tilted rather than orthogonal point, (4) mislabelling points while keeping the unlabelled distance histogram unchanged.

No independently observed frequency in hertz, novel fundamental physical dimension or new universal mathematical theorem follows. These are exact results for a particular synthetic metric and a *chosen* graph model.
