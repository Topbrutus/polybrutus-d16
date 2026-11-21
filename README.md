# POLYBRUTUS 16D — Exact Euclidean distance metric and tenfold ideal-graph eigenvalue

**Human research author:** Gabriel St-Pierre (Topbrutus), independent researcher.  
**Scientific status:** reproducible exact mathematical computation; **not independently peer reviewed**.  
**AI disclosure:** OpenAI ChatGPT (Astra) substantially assisted exact calculations, two separately implemented verification programs, research drafting and release work; AI is not an author.

## Reproducible mathematics (radius R=1)

- **21 labelled vertices**, **210 labelled pairwise squared distances**, minimal Euclidean affine embedding dimension exactly **16**.
- All **190/190** labelled squared distances from the frozen Polybrutus D15 parent are conserved without moving any previous vertex.
- One new perpendicular unit vector adds **20** squared distances, each equal to **2**.
- Eight normalized squared-distance families `k=4d²/R²`: `{4:6,7:2,8:179,9:3,10:10,12:6,13:2,16:2}`.
- Exact total `sum(d_ij²)=1727R²/4`.
- The primary verifier proves coordinate-difference rank **16**, centered-distance Gram rank **16** and the exact positive-semidefinite identity `B=(HX)(HX)^T`. The coordinate representation has 17 storage slots with one simplex hyperplane relation.
- **Selected ideal graph model:** complete weighted graph with unit scalar masses and `w_ij=R²/d_ij²`. Eigenvalue **21/2** has exact multiplicity **10**; eigenvalue **10** has exact multiplicity **4**. These are hypothetical model eigenvalues, not experimental physical frequencies.
- The independent verifier reconstructs all **210/210** exact rational labelled squared distances and verifies the centered Gram rank and spectral root multiplicities. The primary program rejects **4/4** deliberately incorrect configurations.

## Exact reproducibility

```sh
python -m pip install sympy==1.14.0
python src/verify_d16.py
python tests/independent_d16.py
```

The independent checker **does not import** the geometric point generator. The `prior/` directory preserves the frozen D15 source and its predecessor certificates from `Topbrutus/polybrutus-d15@v0.1.0`, commit `680182c69307fe1be8df831cf7b8eacae2f8ff62`.

## Files and provenance

- `src/verify_d16.py`: exact labelled 210-pair metric, centered Gram and graph spectrum, falsification tests.
- `tests/independent_d16.py`: separately implemented rational-metric and exact eigenvalue multiplicity checks.
- `results/certificate_d16.json`: full table of all 210 labelled squared distances, histogram, ranks and graph polynomial.
- `SPECIFICATION_D16.md`, `PREUVE_D16.md`, `PROVENANCE.md`: geometry, proof, source lineage.
- `publication/POLYBRUTUS_16D_NOTE.pdf` and `.md`: mathematical preprint; narrative content CC BY 4.0.
- `SHA256SUMS.txt`: frozen Git blob checksum index; source scripts MIT.

**Previous records:** D07 [10.5281/zenodo.24407952](https://doi.org/10.5281/zenodo.24407952), D08 [10.5281/zenodo.24408344](https://doi.org/10.5281/zenodo.24408344), D09 [10.5281/zenodo.24408448](https://doi.org/10.5281/zenodo.24408448), D10 [10.5281/zenodo.24408569](https://doi.org/10.5281/zenodo.24408569), D11 [10.5281/zenodo.24408650](https://doi.org/10.5281/zenodo.24408650), D12 [10.5281/zenodo.24408720](https://doi.org/10.5281/zenodo.24408720), D13 [10.5281/zenodo.24408769](https://doi.org/10.5281/zenodo.24408769), D14 [10.5281/zenodo.24408836](https://doi.org/10.5281/zenodo.24408836), D15 [10.5281/zenodo.24408887](https://doi.org/10.5281/zenodo.24408887).

**Limits:** The affine rank of a synthetic Euclidean metric is not evidence for additional physical dimensions. Orthogonal point completion and uniform-join graph spectral shifts are existing methods; **no novel universal theorem, particle discovery or measured resonance is claimed**.
