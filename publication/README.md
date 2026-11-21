# Polybrutus D16 — controlled scientific release

This is a **reproducible unreviewed mathematical preprint**, not a claim of a novel universal theorem or a physical extra dimension. AI assistance is disclosed in the full note and in the deposit metadata.

1. Verify `src/verify_d16.py` and `tests/independent_d16.py` using SymPy 1.14.0.
2. Create a private GitHub repository; enable GitHub Actions and require both tests PASS on the candidate commit.
3. Freeze the successful source commit as `v0.1.0`; archive with `git archive v0.1.0`, never from a mutable working tree.
4. Check SHA-256 of source ZIP, PDF and 210-pair JSON certificate; stage exactly these three files in **one Zenodo direct-REST draft** with author, license, parent DOI, GitHub tag and AI disclosure.
5. Confirm draft metadata and remote file checksums, make GitHub public, verify tag via public GitHub API.
6. Publish the same Zenodo draft, confirm DOI and public file hashes with the Zenodo public API.
7. Add DOI to README, CITATION, release_manifest and Memoria. Never move science tag or silently replace parent.

Do not enable parallel automatic GitHub-to-Zenodo archiving that could create duplicate records. Never expose passwords, API keys, private chats or tokens in public source.
