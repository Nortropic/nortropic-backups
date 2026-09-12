# Nortropic recovery backups

Private backup destination: `Nortropic/nortropic-backups` (repository ID 1367371291).
Not canonical platform authority, product publication, installation or bootstrap credit.
Established following the owner's 2026-09-12 instruction to proceed with the
documented private-backup-repository proposal.

## Working method

The ongoing checkpoint, recovery, disk-budget and handoff routine is documented
in [BACKUP-RUNBOOK.md](BACKUP-RUNBOOK.md). This is an operator/agent routine;
no unattended scheduler or automatic deletion has been installed.

- Git contains the backup catalogue, checksums, transfer results and recovery
  instructions. Actual backup archives are uniquely named private release assets,
  not duplicated in ordinary Git history. Do not overwrite historical assets.
- Preserve kernel, bootstrap and all previous H-work: sources, specifications,
  frozen gates, recipes, manifests, Git history/required objects, reviews,
  evidence and unpublished/dirty/untracked/generated work. A source-code push
  alone does not back up that complete state.
- Reuse existing local backup inventories. Copy first; never move/delete an
  original as part of transfer. Sensitive material must be reviewed before upload;
  private visibility is not permission to upload credentials. Record withheld
  material as an explicit coverage gap, without modifying original evidence.
- Verify repository ID and private visibility immediately before transfer.
  Download each asset into a fresh local destination, verify its full checksum,
  validate archive paths/types, then actually restore and compare membership,
  bytes and recorded metadata. Never execute restored project code to restore it.
- Only the tested batch may become `REMOTE_RESTORED_VERIFIED`. This is a backup
  result, never a new PASS for its historical subject. Failed/consumed attempts
  retain their historical status; new inodes cannot recreate old physical identity.
- Local retirement remains subject to the existing exact-target retention rule,
  active-dependency checks and any required scoped decision. This repository does
  not authorize deleting any local backup. Keep active working copies local.
- Do not force-push, mirror/prune refs, rewrite history, overwrite old archives,
  add CI workflows that execute archived code, or change platform/H039 originals.
- GitHub provides off-host storage but not an independent provider failure domain.
  A second independent backup destination remains a future resilience improvement.

GitHub asset limits were checked on 2026-09-12: each release asset must be below
2 GiB. Larger archives need a reviewed chunk/reassembly scheme and restoration
proof; they are not implicitly approved by the small first batch.
[GitHub release documentation](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

## Coverage

Latest representation checkpoint, 2026-09-12T17:02:02Z: exactly eight redundant
raw tar files were retired under the user's direct continuation instruction,
after fresh local byte reconstruction, remote asset ID/size/digest checks and
open-file checks. All nine local compressed parts, remote assets, receipts,
original working copies and restored trees remain. See
RAW-ARCHIVE-RETIREMENT-AUTHORIZATION.md, RAW-ARCHIVE-RETIREMENT-PROPOSAL.json,
RAW-ARCHIVE-RETIREMENT-PREFLIGHT.json, RAW-ARCHIVE-RETIREMENT-EXECUTION.jsonl and
RAW-ARCHIVE-RETIREMENT-RESULT.json. Historical statements below about raw paths
describe their checkpoint; current catalogue rows now record their replacement.

Reconstruction: base uses the two gzip parts in proposal order; concatenate the
DECODED bytes and verify the full raw hash/length. Each supplement has one gzip
part; decode and verify its raw hash/length. Never treat the first base part as
a whole archive. A normal Git clone does not download these release payloads.
Only reconstruct into a fresh budgeted recovery area; this retirement does not
prove a new composed filesystem restore or recreate historical runtime identity.
The observed free-space increase was5,232,234,496 bytes; concurrent host activity
means it is not an exact attribution of reclaimed blocks. A later df measured
20,988,296 KiB available, just over20 GiB. Recheck before every heavy operation.

See `catalogue.json` and batch records. `LOCAL_ONLY_NOT_REVIEWED` is not remotely
secured. The first H039 source batch is not a complete repository, history backup,
all-H039 backup or all-H-work backup. Local backups must remain available.

2026-09-12 checkpoint: all 43 existing catalogued Git bundles have remote
download/restore receipts across HISTORY-RESTORE-RECEIPT.json and
HISTORY-REMAINDER-RESTORE-RECEIPT.json. Their 250 worktree HEAD pseudorefs have
explicit recovery mappings, not recreated worktree administration or dirty state.

MAIN-CONTENT-REVIEW.json and MAIN-GIT-OBJECT-REVIEW.json finish the bounded content
review of the existing main tar, including all 36 packs and 1810 loose objects
(28619 unique Git objects). This does not prove each original checkout's full
independent closure: the aggregate object store was inspected for backup contents.
At that content-review checkpoint, main archive transfer and remote filesystem
restoration were NOT_RUN; see the later multipart records for actual progress.
The size-limited gzip attempt stopped and is explicitly an incomplete prefix,
not an uploaded complete archive. Its exact hash and decoded byte boundary are
recorded. Do not mistake the `.tar.gz` suffix for a complete-backup verdict.

Later checkpoint, 2026-09-12T16:10:35Z: both reviewed multipart assets were actually
downloaded from private release387620383. Compressed and decoded hashes/lengths,
ordered full-tar hash and every original byte matched; both download commands
returned0 with empty stderr. See MAIN-MULTIPART-REMOTE-RECEIPT.json and
MAIN-MULTIPART.md. The result is
`REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED`, not filesystem restoration.
The historical failed compression remains preserved; its unchanged output is
now explicitly part1 of the new verified two-part transport, never a whole tar.

Later checkpoint: all seven cumulative supplements are uploaded and have actual
regular-file restore receipts in SUPPLEMENT-REMOTE-RECEIPT.json (8425 files across
seven separate generations). RECOVERY-METADATA-REMOTE-RECEIPT.json covers52 exact
recovery manifests, member lists, instructions and reports downloaded/restored.
These checks cover file membership/bytes/modes/uid/gid; they do not claim complete
directory metadata, a composed baseline+delta worktree or archived helper execution.
RESTORE-CHAIN-INDEX.json originally recorded local-only status; consult these later
receipts for transfer progress. Its historical source pins are unchanged.

External-archive checkpoint: EXTERNAL-ARCHIVE-CONTENT-REVIEW.json records all50
bounded archive reviews. EXTERNAL-GIT-CONTENT-REVIEW.json closes31 previously
unknown packs (31,975 objects, fsck0); its sole nested archive is byte-identical
to the21 Markdown documents in FLAGGED-CONTENT-REVIEW.json. Historical unresolved
review rows are retained, not rewritten as though already cleared at that time.
The34 initial clear archives have completed streamed remote byte verification;
see EXTERNAL-BATCH1-REMOTE-RECEIPT.json. This is not filesystem restoration.
The13 subsequently cleared archives have also completed streamed remote byte
verification, all commands exit0/empty stderr and source bytes unchanged:
EXTERNAL-BATCH2-REMOTE-RECEIPT.json. Together these two batches cover47 external
archives. This is complete archive-byte readback for those subjects, not a new
full filesystem restoration.

LARGE-EXTERNAL-MANIFEST.json defines45 consecutive raw128MiB-or-smaller segments
for the two large scratchpad archives, with part offsets, sizes and hashes and
whole-archive hashes. The named private release is
`backup-20260912-large-scratchpad-segments`; upload/readback are in progress.
Download each archive's parts in manifest order, verify them, concatenate their
RAW bytes (not gzip), then verify the full archive before any safe extraction.
The upload helper streams exactly Content-Length bytes through configured gh;
no credentials are extracted and no local segment payloads are created.
GitHub API and gh2.97.0 source were checked for this input behavior:
https://docs.github.com/en/rest/releases/assets#upload-a-release-asset
and https://github.com/cli/cli/blob/v2.97.0/pkg/cmd/api/http.go .
LARGE-EXTERNAL-TRANSPORT-TESTS.json covers actual bounded-reader/partition helpers,
not remote content or filesystem restoration. Do not rerun the upload while the
existing process is active, clobber parts, or treat a partial release as complete.

The v314 H036 archive remains withheld: one historical log contains raw capability
values whose custody clearance is not established. It is not sanitized/replaced.
Cleanup recovery material is now verified in CLEANUP-MATERIALS-REMOTE-RECEIPT.json:
17,866 mapped files /9,389 content objects, downloaded as an exact121,740,798-byte
archive and all mapping/object hashes checked. Eleven additional Git packs were
decoded and scanned (CLEANUP-PAYLOAD-GIT-REVIEW.json, fsck0, no findings; same
previously reviewed nested Markdown archive). One identical H036 log copy in
reports is withheld. Existing restored duplicate trees remain local and were
not repackaged; catalogue container rows state this partial coverage explicitly.

To recover these materials, download the exact asset in CLEANUP-MATERIALS-PACKAGE.json,
verify its archive hash, validate mapping.json's pinned hash, and require exactly
that mapping plus objects/<sha256>. Verify every object length/hash and each mapped
path before writing into a NEW isolated recovery tree. Copy object bytes to mapped
regular paths; never hardlink recovery files into originals. The recorded stat
identity is historical, not recreated authority. Do not execute archived helpers
or recreate absolute pointers into live repositories as a backup test.
Full composed baseline+delta restoration and later-work coverage remain open.
Eight redundant download-cache files were retired after completed restoration;
their byte-identical local encoded source copies, remote assets and restored trees
remain. This is not retirement of original backups or repositories.
Budget genuine remote filesystem restoration separately: the main tar's logical
regular-file bytes alone are 4266945226, beyond the currently observed margin
above the 15 GiB floor. Historical local restoration reports are retained but are
not silently promoted to a new remote-restoration result. No generic new owner
approval is needed for the already-authorized backup engineering; deletion is
not authorized by this checkpoint.
