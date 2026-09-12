# Existing Git-history bundles — bounded transfer

All 43 existing bundle files were verified against empty, independent local bare
repositories. Every packed object was decompressed and its Git object ID checked;
11,683 distinct objects were scanned for bounded credential/key/token patterns.
Duplicate objects reused their exact ID/type/size-bound content inspection.
No checkout, archived code, hook, network helper or product gate was executed.

41 bundles have no scan findings, nested-compressed payloads or sensitive filename
candidates in the inspected surfaces. They are selected in `HISTORY-BATCH.json`
for private backup transfer. This includes the platform history and older H-work
bundles, not just the latest candidate. No refs in original repositories changed.

Two bundles are withheld pending separate content review:

- `nortropic__verkstadsgolvet.bundle`: eight scanner findings in test/smoke source
  blobs and three `.env.example` path candidates. These are not established live
  secrets; test locations alone are insufficient to clear them. No matched values
  are printed in the report or uploaded as part of this batch.
- `nortropic__innovation-intake.bundle`: one nested compressed blob whose inner
  content has not yet been inspected. The other innovation-intake bundle is a
  separately reviewed exact subject, not a substitute for this withheld one.

## Restoration procedure

1. Download the exact uniquely named asset from this private backup repository.
2. Require the full SHA256 and byte size from `HISTORY-BATCH.json`.
3. Initialize a NEW empty bare repository with user/system Git config disabled.
   Verify the bundle there before importing; do not use existing original objects
   to satisfy absent prerequisites.
4. Unbundle without checkout. Recreate only the advertised refs, with validated
   names, then compare every ref OID and the advertised HEAD OID. A bundle does
   not encode whether original HEAD was symbolic; do not invent that evidence.
5. Run strict Git object validation and compare the complete object ID/type/size
   projection to the pre-upload inspection. Check actual files/refs before credit.
6. Append a remote restore receipt. Never apply restored refs to active repositories.

Bundle recovery preserves only what is in the bundle. It does not establish
recovery of index/dirty/untracked/generated files, reflogs or missing unreachable
objects. Those remain dependent on the main archive and supplemental backups,
which are still local-only. Historical PASS/FAIL/consumed state is unchanged.
No local archive, bundle, inspection store or restored copy may be deleted here.

Initial state: selected for upload; no remote-restore result yet. Subsequent
receipts state actual results per asset rather than inferring whole-system safety.

## Completed remote restoration — 2026-09-12

`HISTORY-RESTORE-RECEIPT.json` records all 41 assets actually downloaded from
private repository ID 1367371291, release ID 387613278, and restored into fresh
bare stores. The downloaded SHA256/size, server asset digest, source bundle,
advertised refs and complete object ID/type/size projection agree. Every bundle
verified against an empty store and passed strict fsck after restoration.
The 41 assets total 254655172 bytes. This is Git-bundle recovery credit only.

R1 restored two bundles, then rejected a worktree HEAD pseudoref in the third.
Its stores, log and helper remain preserved; R1 did not complete the batch.
R2 repeated all 41 in NEW stores with one explicit extension to step 4:
`worktrees/<name>/HEAD` is preserved as an original name/OID pair in the receipt
and mapped to `refs/backup-recovery/worktree-heads/<name>` only in the recovery
store. All 242 such pairs across three bundles have collision-checked mappings.
Normal refs retain their exact names/OIDs, and the advertised HEAD OID is exact.
This does NOT recreate worktree administration, symbolic HEAD relationships,
indexes or unpublished files. No refs in any original repository were modified.

The two withheld bundles remain withheld. `MAIN-ARCHIVE-TRIAGE.json` records a
separate read-only inspection of the existing 4848679936-byte main tar archive:
321051 headers, 282785 regular members, 10990 unique regular contents. Its SHA256
matches the existing backup receipt. Six bounded scanner matches remain to be
classified, and 36 Git-pack payloads plus one nested compressed payload still
require decoded inspection. No live credential has been established by those
matches. The main archive and remaining supplements are NOT uploaded or remotely
restored by this batch. The catalogue is not a claim that all work is secured.

Local inspection/recovery workspace (retained):
`/Users/elinhaggstrom/nortropic-backups-20260910/github-history-transfer-20260912.HYawFS`.
R2 downloads are in `download-r2`, restored Git stores in `remote-restored-r2`.
All original archives and local copies remain. There is no deletion, operational
bootstrap credit, product publication, installation or supervisor transition.
