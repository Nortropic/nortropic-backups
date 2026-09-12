# Two additionally reviewed history bundles — 2026-09-12

This supplements, and does not rewrite, the initial 41-bundle batch.
The two bundles previously withheld in HISTORY-BATCH.json are now selected in
HISTORY-REMAINDER-BATCH.json following the exact FLAGGED-CONTENT-REVIEW.json.

The eight pattern findings in six source blobs are synthetic scanner inputs,
mocked visual-auth credentials and a script-created localhost smoke credential.
Source context and content identities were checked without executing those tests.
The PEM hit is an opening marker, not a private key. The token-shaped scanner
input consists of ordered alphabet/digit runs and is asserted to be detected;
no credential authentication or network validation was attempted. The three
env templates contain empty credential values and at most a false feature flag.
The nested tgz contains exactly 21 bounded UTF-8 Markdown files and directories,
with no links, special files or bounded credential-pattern matches.

This is bounded review, not a mathematical guarantee of universal secret absence.
Archived AGENTS/CLAUDE files were treated as backup data, not live instructions.
All original bytes remain unchanged. Previous withheld reports remain historical.

Recovery uses the same downloaded-digest, empty-bare import, strict fsck and
complete object projection checks as HISTORY-BATCH.md, including explicit
worktree HEAD recovery mapping. No worktree index/dirty/reflog reconstruction
or bootstrap/runtime credit follows from these Git bundles. The separate
HISTORY-REMAINDER-RESTORE-RECEIPT.json will record actual results, if successful.
The main archive and supplements remain distinct incomplete backup coverage.

Actual outcome: both assets were downloaded and restored in fresh bare stores;
empty-store bundle verification, import, strict fsck, downloaded/source/server
digests, normal refs and all object projections matched (exit 0). The second
bundle has eight worktree HEAD pseudorefs, recorded with explicit recovery
mappings. See HISTORY-REMAINDER-RESTORE-RECEIPT.json. All 43 existing catalogued
bundles now have remote Git recovery evidence across the two batches. This is
not full workspace recovery and gives no credit to absent dirty files or indexes.
