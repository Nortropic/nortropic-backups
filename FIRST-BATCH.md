# First bounded batch: H039 material-binding source snapshot

Source: `full-20260910T103342Z/external/h039-local-material-binding-dbd51ba7-20260912.tar.gz`.
Archive SHA256: `30439948a194dda91c87ebbee1dad260393d84fd0d6db25152326437931f98d2`.
Release tag: `backup-20260912-h039-material-binding-dbd51ba7`.
See `first-batch-inspection.json` for all archive members and hashes.

The existing archive contains seven UTF-8 source/result files plus seven
AppleDouble metadata entries, with provenance xattrs. No symlinks, hardlinks,
nested archives, executable binaries or Git object stores occur in this batch.
The four held H039 source hashes match the existing working-copy pins.

Bounded token/private-key/credential-URL/JWT/literal-secret scanning produced
no findings. Manual review of credential-related keywords showed specification
requirements, not literal credentials; the result JSON contains test booleans,
source digests and local source paths, not live capability values. Focused test
sources reference local dependencies not included in this archive. The metadata
contains local provenance, not signing keys. This is a bounded review, not a
universal proof that arbitrary unknown secret formats are absent.

Inspection R1 stopped before upload because macOS tar's seven displayed files
also have seven AppleDouble members. R2 explicitly validates all fourteen
members and preserves the original archive unchanged. No member was omitted.

## Restore

Download the release asset to a new private directory. Verify the archive SHA256
above and the exact 14-member list before extracting. Use macOS `/usr/bin/tar`
in an empty directory to restore the seven logical files and metadata. Compare
the seven logical file hashes, sizes, modes, owner/group, mtime and xattrs with
the inspection manifest and a local baseline restore. Do not apply these files
to the current worktree, run the included test scripts or claim old inode identity.

Initial state at catalogue commit: reviewed for this private destination;
upload, independent download and actual remote-byte restoration NOT_DONE.
An appended restore receipt will record the actual outcome without changing
the historical inspection result or source archive.

## Executed remote restore, 2026-09-12

`FIRST-BATCH-RESTORE-RECEIPT.json` records `REMOTE_RESTORED_VERIFIED` for this
833877-byte archive ONLY. GitHub asset ID 559395238 / release ID 387596174;
server digest, freshly downloaded file digest and original archive digest agree.
Actual extraction followed by all seven logical file checks exited 0.
No restored project code or historical test was executed.

The initial home-directory restore retained file bytes but changed three test
files' GID from the archived 0 to inherited 20, so it received no complete restore
credit. It remains preserved. The successful separate restore used a fresh
`mktemp -d /private/tmp/nortropic-backup-restore-20260912.XXXXXX` directory,
verified as UID501/GID0 before extraction. After extracting the downloaded
archive, `chgrp 20` was applied ONLY to these four freshly restored files:

- `verify/bin/h-039-exit`
- `specs/tasks.spec.json`
- `controller/verify/cli`
- `docs/loop/platform-separation-final-local-development.md`

The three test/result files retained inherited GID0. This matches all seven
archived identities without root, changing group membership, or touching an
original. If a different host cannot represent these owner/group identities,
report that restoration limitation rather than claiming exact metadata recovery.
Final checks covered membership, bytes, size, mode, UID/GID, nanosecond mtime,
exact provenance xattr names/bytes, nlink1 and independent restored inodes.
Original inode/ctime/atime/birthtime are not recreated or credited.
