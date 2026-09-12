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
