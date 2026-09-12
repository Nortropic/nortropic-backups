# Nortropic recovery backups

Private backup destination: `Nortropic/nortropic-backups` (repository ID 1367371291).
Not canonical platform authority, product publication, installation or bootstrap credit.
Established following the owner's 2026-09-12 instruction to proceed with the
documented private-backup-repository proposal.

## Working method

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
