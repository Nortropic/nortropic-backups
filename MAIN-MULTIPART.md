# Exact main archive — two-part backup transport

This is a backup of the unchanged 2026-09-10 base tar, not current product
publication or complete latest-workspace recovery. Later supplements remain
necessary. See MAIN-CONTENT-REVIEW.json for the completed bounded content review.

Manifest: MAIN-MULTIPART-MANIFEST.json. There are EXACTLY TWO gzip segments.
Part 1 is `nortropic-full-20260910T103342Z.tar.gz`; despite the suffix it is NOT
a standalone complete tar. It is the unchanged preserved output of an earlier
size-limited compression attempt, now explicitly described as a verified prefix.
Part 2 is `nortropic-full-20260910T103342Z.part-002.tar-segment.gz`.
Both names, compressed hashes/sizes, contiguous decoded ranges and raw hashes
are required. Neither segment alone receives whole-archive backup credit.

The local check actually decoded both parts, checked individual compressed/raw
hashes and lengths, compared every decoded byte to the original tar and verified
the full 4848679936-byte SHA256:
`b69532a32d38a0ac18065709f501ac7a9e5a40bb966a3890ec9ea6012087bb3c`.
The same verifier rejected missing, reordered, duplicate, modified, truncated,
appended, wrong-offset, wrong-full-hash and wrong-original test cases.
The streaming decoder used for upload preflight/remote verification bounds each
decoded buffer to 8 MiB. These are transport tests, not tests of archived code.

## Recovery

Download both exact assets from release `backup-20260912-main-archive-multipart`
of private repository `Nortropic/nortropic-backups` (ID1367371291).
Check each compressed size/SHA256 against the manifest BEFORE extracting.
Decompress part 1 then part 2 and concatenate the decoded bytes; this reconstructs
the original tar, not two separate tar archives. Verify its full size and SHA256
above. A fresh output filename must be used; do not overwrite a prior attempt.

Before filesystem extraction, budget disk space, verify tar paths/types/link
targets, and follow the existing README-RESTORE.md and relevant original
manifest/supplement records. Do not execute archived code or reactivate links
into original repositories as a recovery test. Absolute Git-admin paths, indexes,
dirty state, metadata and later supplements require their own exact comparisons.
Historical PASS/FAIL/consumed states and original physical identity do not change.

The immediate remote check streams both assets from GitHub into the verifier and
compares the reconstructed tar with the unchanged local original, without writing
another 4.8 GB tar or extracting 4.27 GB of logical file data. Its receipt, if
successful, is REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED, NOT a full remote
filesystem restoration. Keep all originals; this status grants no local deletion.
Whole current-workspace off-host preservation remains incomplete until remaining
supplements and the required restoration checks are handled.

## Actual remote result — 2026-09-12T16:10:35Z

MAIN-MULTIPART-REMOTE-RECEIPT.json records successful streamed downloads of both
assets from release387620383, each exit0 and empty stderr. The actual verifier
checked compressed hashes/lengths, decoded part hashes/lengths/order, the full
4848679936-byte tar hash and byte-for-byte equality with the unchanged original.
Status: `REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED`.
The positive and nine negative actual-callable transport cases also passed.
No full remote tar was materialized; filesystem restoration remains `NOT_RUN`.
No original or preserved attempt was deleted and no archived code executed.
