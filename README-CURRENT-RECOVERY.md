# Aktuell arkivrepresentation — 2026-09-12

## Senare H039 P005366dd — Git-objekt återställda, kvalificering röd

Privata repot ID1367371291 kontrollerades före överföring. Ny release
`backup-20260912-h039-product-P-005366dd` ID387676316 innehåller asset559802438,
`h039-product-P-005366dd-incremental.bundle`,9603B, SHA256
`f6f7e95b97d49f1d1c12cc1559d46f0727d870d9d785d0509c978af68a3cf30a`.
Upload36a387→f14b9c exit0, serverdigest5ec5f3 och faktisk download5923d1→90c58e
matchade. Den kräver redan verifierade B8095- och C7be3-bundlar nedan.

`H039-P-005366DD-BUNDLE-RESTORE.json` är faktiskt återställningskvitto:
`RESTORE-H039-P-005366DD.py` SHA256
`b0745e1855822b1bed5d3581cf04d1cdc29759a0e82dd69975c8f144c47277a8`
kördes96ee56→544ed1 exit0. Ny isolerad bare-yta
`/private/tmp/nortropic-h039-P-bundle-restore-5r2gc3b5`:306 Git-kommandon exit0,
raw C/P commits, parentkedja, tree och144 blobs/modes samt fsck verifierade.
Kvittots SHA256 `7bed5077a86aef1bdc784975ca2497f19614249297e2bee0f58e803149a2a101`.
B och C hämtades inte på nytt denna gång. Originalindex/admin/dirty/ospårat
återställs inte genom denna bundle; ingen projektkod kördes och inget raderades.

P `005366dd5e3a9a74d8140c9dd0c0175aea268294`, ensam parent C7be3,
tree `a548cb8876346eb505906fb3feaa7b8d33ec43aa`, exakt4 produktpaths.
Den första faktiska lokala final-kvalificeringen gav exit1/RED:
119 true,1 abort,13 ej nådda rader. H039-child2/UNJUDGEABLE eftersom fixturens
`.git/info` saknades innan Git-prestate/material. Se
`H039-P-005366DD-FIRST-FINAL-RECORD.json`. Backupen ger ingen produkt-/runtime-
eller bootstrapcredit och ersätter inte det bevarade misslyckade försöket.

Ny builder-/metod-/råbygg- och full kvalificeringsevidens ligger fortfarande
lokalt i `evidence/v316-h039-continuity-review-20260912/` och de uttryckligen
namngivna rårotarna. Enbart Git-bundle, återställningsverktyg/kvitto och denna
avgränsade kvalificeringssammanfattning täcks här; inga äldre arkiv får sägas
innehålla dessa senare filer. Kvarstående filbackup görs som separat delta.

## Senare H039 C/R4-checkpoint

Efter arkivsnapshot slutfördes även samlad oberoende review av samma immutable C:
`H039-C-7BE3A5AB-INDEPENDENT-CONTRACT-REVIEW.md`, SHA256
`4d401d4aaa598159e26b17ae0250bb5d5d5db91f88126a9baa3dc0cad20a6eb8`.
C är därmed accepterat som lokalt fryst kontrakt för separat asset-builder.
Denna senare review ligger i backuprepots Git, inte retroaktivt i55-filarkivet.
Det tidigare avbrutna reviewförsöket behåller sin status. Ingen P-kvalificering,
H039-taskcredit, installation eller drift följer. Separat builderförberedelse
sker lokalt; nya metod-/produktbytes täcks inte av den gamla checkpointen.

`H039-C-7BE3A5AB-RESTORE-RECEIPT.json` binder två nya assets i release
`backup-20260912-h039-contract-C-7be3a5ab`: ett55-filarkiv och en inkrementell
Git-bundle. Båda har faktiskt hämtats tillbaka. De55 filerna har återställts
med registrerade bytes/metadata i en ny separat yta. Arkivnamnen är platta;
ursprungliga paths finns i inspektionens source-fält. Återställ aldrig blint
över originalens absoluta paths.

C-bundlen kräver exakt B8095d947 från den redan säkrade
`v316-h039-continuity-product-8095d94.bundle`; se kvittots exakta SHA256 och
release/asset-ID. Återställaren importerade hashbunden lokal B-bundle och den
nyss nedladdade C-bundlen i ett nytt bare repo. Raw C/parent/tree, samtliga144
spårade blobs/modes och fsck kontrollerades. B hämtades inte på nytt denna gång.
Detta är inte originalets index/worktree-administration eller full ny
fjärrbas+delta-filsystemsrestaurering. Kör ingen arkiverad projektkod.

C7be3a5ab är ett lokalt immutable reviewsubject med korrekt uppmätt frånvaro;
ett ytterligare slutreviewförsök avbröts av usage. Ingen accepterad freeze,
produkt, installation eller bootstrapcredit följer av arkiveringen. Bevara
tidigare trancher och deras creditstatus. Senare ändringar i kontinuitetstexten
ingår inte retroaktivt i arkivets snapshot.

## Tidigare arkivrepresentationer, fortsatt giltiga

Läs denna före den historiska README-RESTORE.md. Den gamla instruktionen och
dess verifierade hash bevaras oförändrade. Åtta råa tarfiler pensionerades efter
byte-exakt lokal rekonstruktion och färsk kontroll av redan återlästa GitHub-assets.
Data har inte försvunnit: de nio komprimerade delarna behålls lokalt och i privata
`Nortropic/nortropic-backups` (repo ID1367371291).

Exakt lokal karta och kvitto:
`../github-history-transfer-20260912.HYawFS/RAW-ARCHIVE-RETIREMENT-PROPOSAL.json`
och `../github-history-transfer-20260912.HYawFS/raw-retirement-result.json`.
Samma karta/kvitto finns i backuprepots Git-träd med namn
`RAW-ARCHIVE-RETIREMENT-PROPOSAL.json` / `RAW-ARCHIVE-RETIREMENT-RESULT.json`.

För basen: verifiera de två kodade filernas hash och längd, avkoda gzipdelarna i
kartans ordning och sammanfoga deras AVKODADE bytes. Kontrollera full tarhash
`b69532a32d38a0ac18065709f501ac7a9e5a40bb966a3890ec9ea6012087bb3c`
och längd4848679936. Första gzipfilen är endast en prefixdel, inte hela basen.
Release: `backup-20260912-main-archive-multipart`.

Senare samma dag pensionerades även två råa scratchpad-backuprepresentationer
under external/. Exakta identiteter och lokala gzipvägar finns i
`../github-history-transfer-20260912.HYawFS/large-raw-retirement-result.json`
(backuprepot: LARGE-RAW-RETIREMENT-RESULT.json). Arkiven är
scratchpad-refresh-20260910T195603Z.tar och scratchpad-refresh-20260910T202553Z.tar.
Deras lokala `.tar.local-representation.gz` kan avkodas direkt till respektive
ursprungligt råarkiv. Kontrollera både gziphash och full råhash/längd mot kvittot.
På GitHub finns i stället20 respektive25 RÅsegment i release
`backup-20260912-large-scratchpad-segments`; kontrollera delhashar/offsets och
sammanfoga RAW bytes enligt LARGE-EXTERNAL-MANIFEST.json. Alla45 har faktiskt
återlästs; LARGE-EXTERNAL-REMOTE-RECEIPT.json bevisar fulla arkivbytes, inte en
ny filsystemsrestaurering. Gzipfilerna är inte uppladdade. Originalscratchpads
och övriga arbetskopior finns kvar; historiska råfilreferenser ändras inte.

För varje delta: hämta dess gzip från
`backup-20260912-seven-cumulative-supplements`, kontrollera kodad identitet och
avkoda; råhash och längd ska stämma med samma karta. Deltorna är kumulativa, inte
sju steg som ska läggas ovanpå varandra. Använd rätt generation och dess manifest.

Återskapa vid behov råtar exklusivt i en NY återställningsyta, aldrig ovanpå
originalarbete, eller använd en granskad strömmande återställare. Budgetera både
extraktion och marginal före start. Validera arkivpaths/länkar och låt inte
Git-pekare nå originalen. Kör inte arkiverad projektkod. Därefter gäller den
historiska metodens innehålls-/mode-/manifest- och Git-omlokaliseringskontroller.
Gamla dev/inode/live-identiteter blir inte giltiga genom återställning.

Full ny fjärrbas+delta-filsystemsrestaurering: NOT_RUN. De sju separata deltorna
har faktiska filåterställningskvitton; basens fjärrprov återskapade alla tarbytes.
Originalarbetskopior, manifester, evidens och återställda träd är kvar.
Den känsliga H036-loggens custody är separat och materialet är inte uppladdat.
