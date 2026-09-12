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

Next transfer work: the remaining external archives and backup containers.
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
