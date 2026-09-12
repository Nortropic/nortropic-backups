# Aktuell arkivrepresentation — 2026-09-12

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
