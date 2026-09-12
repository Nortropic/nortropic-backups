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
