# Aktuell arkivrepresentation — uppdaterad 2026-09-13

## Senaste checkpoint — ofrusen loaderhållning 8dfbfeeb ovanpå D571a47b8

Privat repo ID1367371291 verifierat 0479dc/edb7de. Nytt asset **560877424**
i befintlig release387676316 (`backup-20260912-h039-product-P-005366dd`):
`h039-loader-8dfbfeeb-20260913T083032Z.tar.gz`, 1259520B, SHA256
`1388bd515114624434ca13ffb5c5e1d996878a8e1bfc883fe26dbb141b31d630`.
Upload b42b81→57862f, serverdigest3433e6, download801190→ce18fb och
faktisk restoreaba613 gav exit0.29 logiska filer/58tarposter återställdes i
`/private/tmp/nortropic-h039-loader-8dfbfeeb-restore-9gb0737o`:
bytes, medlemskap, storlek, mode, uid/gid, mtime_ns, xattrs, single-link och
oberoende inoder verifierade. Inga original eller gamla assets ändrades/raderades.

Urvalet omfattar de sex aktuella ofrusna källfilerna, tre hållna historiska
patchar, cache-/systemobservationernas källor och fem försökskvitton samt
kontinuitet vid snapshot och urvalslistan.28 källfiler var tillsammans4913916B.
Skannern fann inga mönsterträffar i arkiv/metadata eller avkodade JSON-strängar;
det är begränsad innehållsgranskning, inte bevis för universell hemlighetsfrihet.
Gamla försök förblir consumed och gamla resultat behåller sina subjekt.
92/92-modellresultat och oberoende review återges i den arkiverade checkpointen;
fulla agent-/verktygstranskript ingår inte. Ingen ny modell/nativekörning gjordes.

Läs `H039-LOADER-8DFBFEEB-SELECTION.json`, `...-INSPECTION.json`,
`...-RESTORE.json`, `...-RECONSTRUCTION.json` och `...-TRANSFER.json`.
Snapshotmetoden och den separata read-only rekonstruktionskontrollen finns i
`SNAPSHOT-H039-LOADER-8DFBFEEB.py` respektive
`RESTORE-CHECK-H039-LOADER-8DFBFEEB.py`. Snapshotmetodens prepare/verify är
förbrukade över dessa destinationsnamn; framtida restore kräver ny isolerad rot.
Denna lilla batch använder runbookens15GiB-golv +64MiB explicit arbetsbudget,
inte tidigare metodens20GiB-normalmål som startvillkor. Både total källa och
arkiv begränsas till8MiB; faktisk tillgänglig disk före steget20737140KiB.
20GiB kvarstår som normalmål. Detta ändrar ingen retention-/cleanupbefogenhet.

a921c4 exit0 rekonstruerade samtliga sex slutbytes i minnet från den faktiskt
nedladdade full-index-patchen och D:s tidigare återställda Gitobjekt. Exakt
D571a47b8/tree10d70b1b, alla sex arkiverade filer och28 originalhashar stämde;
TA-index var tomt. Första hjälpkontrollen289126 stoppade före rekonstruktion
på korta kontra fulla indexrader;7330ac isolerade396 formatteringsbytes,
inte källändring. Inga originalpatchar ändrades för att få kontrollen grön.

För återuppbyggnad: återställ först den redan dokumenterade B→C7be3→P005366→
C83→D571a-bundlekedjan i en NY separat yta. Verifiera D:s commit/förälder/träd.
Hämta detta asset separat från Releases, verifiera SHA och säkra medlemsvägar,
återställ de29 filerna i en ny rot och använd de sex hela sluttexterna eller
den exakta kumulativa patchen ovanpå D. Inga paths är borttagna. Gamla patchar
är historik, inte en serie som ska appliceras före aktuell kumulativ patch.
Inga arkiverade kommandon ska köras som en del av filåterställningen.

Detta återanvände tidigare återställda D-objekt, inte en ny full fjärrbas+delta-
återställning. Originalens Gitadministration, katalogmetadata, process-/inode-
identiteter och custody återställs inte. Tidigare helhetstäckningsluckor består.
Kontinuitetsnotiser efter snapshot ingår först i nästa checkpoint.
Native-rollanropets verktygsfilter är fortsatt olöst; denna backup är inte en
alternativ exekveringsväg. H039, installation och supervisor resume är inte klara.

## Senaste checkpoint — D571a47b8, faktisk CPython3.9-kompatibilitet

Lokal kontraktscommit `571a47b8f5fbf1718125742718d2f5908d49e95c`, parent
`83f75968b9892ae98a6a879178c407d2a6fd935e`, tree
`10d70b1b77601b72b07c633510cb12f5ac657b02`; exakt sex filer,+405/-11,
inga produktändringar.75/75 rena3.12-kontroller följdes av oberoende review,
lokal frysning, separat fysisk kopia och faktisk kvalificering fc1f3c→6ecc99 exit0.
30/30 rader, varav25 semantiska fall i samma ägda direkta CPython3.9.6/arm64-process.
`PASS_CPYTHON39_INERT_VERIFIER_COMPATIBILITY_ONLY`. Source261/qual226 fysiska
rader oförändrade. Oberoende postreview67b6b0 READY. Ingen adapterload/query,
full H039, installation, receipt-, runtime- eller bootstrapcredit.

Privat repo-ID1367371291 återkontrollerat e598ca/359e40, release387676316:

- Bundle559956924,10486B SHA256
  `1f0e03597c3b9dbf503bf2d56d9428f4e175864406599814744e7cc59ee8172c`.
 16 nya objekt inspekterade; faktisk download9de276 och restore489a9f→bb4dbd
 verifierar alla144 Gitblobbytes/modes, commit/förälder/tree med302 Gitkommandon0.
 Tidigare verifierade lokala B/C7be3/P005366/C83-bundlar återanvändes, ej omhämtade.
- Filasset559959521,1258488B SHA256
  `ad0ddacef3ba553193e431748d8457a7bc4002ace4332de3e62a2a9e0772a211`.
 39 logiska filer/78tarposter; ingen mönsterträff. Faktisk downloadab8da3 och
 restore399cbd exit0 verifierar medlemskap, bytes, size, mode,uid/gid,mtime,xattrs
 och oberoende single-link-inoder. Restoreplats
 `/private/tmp/nortropic-h039-verifier-py39-D-qualified-restore-26uiaw7x`.

Exakta urval/metoder/kvittens finns i `H039-VERIFIER-PY39-D571A47B8-*.json`,
`BACKUP-H039-VERIFIER-PY39-D571A47B8.py` och `SNAPSHOT-H039-VERIFIER-PY39-D571A47B8.py`.
Metoderna är förbrukade över befintliga destinationer; en senare restore ska
använda NY separat rot. Urvalet bevarar hållna mellanversioners prov, det frusna
subjektet, faktiska råloggar och reviews; gamla resultat behåller sina subjekt.
Ingen arkiverad projektkod kördes under återställning. Original Gitadministration,
katalogidentiteter och full ny fjärrbas+delta-restoration är inte verifierade här.
Känslig lokal custody-evidens och tidigare dokumenterade helhetsluckor består.
Inget gammalt asset överfördes igen, inget raderades eller pushades till plattformen.
Senare kontinuitetsnotiser efter snapshot är nästa checkpoints lokala material.

## Senaste checkpoint — frusen verifierare C83f75968 och 31 evidens-/källfiler

Lokal C `83f75968b9892ae98a6a879178c407d2a6fd935e`, enda förälder
P `005366dd5e3a9a74d8140c9dd0c0175aea268294`, tree
`8da632c48be1705d536be39bb2afc3b4b2d70f51` är bevarad.
Exakt sex kontraktsfiler, ingen ny produkt. 70/70 rena/inerta prov följdes av
en verklig lokal verifierarkörning: ab1d84→377734 exit0, 30/30 rader,
`PASS_LOCAL_VERIFIER_INTEGRATION_ONLY_NOT_FULL_FINAL`.
Oberoende postreview12644c READY, fulla fysiska pre/postmappar oförändrade.
Det ger inte full H039, bootstrap-, installations- eller runtimecredit.

Privat repo ID1367371291 bekräftat f38726/a86843. Samma release387676316:

- Bundleasset559913147, `h039-verifier-C-83f75968-incremental.bundle`, 37895B,
  SHA256 `81cabd9181d7341a1c53c25d6739a73042523de3ee9d10ef081905c78d19e6e9`.
  16 nya dekomprimerade objekt inspekterade utan mönsterfynd. Faktisk download
  och restore b1a93a→5d9e94: 301 Git-kommandon0, alla144 blobbytes/modes,
  exakt commit/förälder/träd i `/private/tmp/nortropic-h039-verifier-C-restore-zitp3lie`.
  Importeras efter den tidigare verifierade B→C7be3→P005366-bundlekedjan;
  tidigare bundlar hämtades inte om. Inte en full ny fjärrbas+delta-restore.
- Filasset559915642, `h039-verifier-C83f75968-qualified-20260912.tar.gz`, 1230309B,
  SHA256 `072a3966460512fd4ff880f80c56589672ab8a92c20d4ba862a037a53f17e135`.
  31 logiska filer/62tarposter, inget mönsterfynd. Faktisk download68c69f→09064e
  och restore017aba exit0 kontrollerar membership, bytes, storlek, mode, uid/gid,
  mtime, xattrs och oberoende single-link-inoder i en ny rot.

Exakt urval, metoder, kommandon, checksummor och återställningskvitton ligger i
`H039-VERIFIER-C83F75968-*.json`, `BACKUP-H039-VERIFIER-C83F75968.py` och
`SNAPSHOT-H039-VERIFIER-C83F75968.py`. Metoderna avser förbrukade backupoperationer;
kör dem inte igen över befintliga destinationsfiler. En senare återställning ska
använda en ny separat rot och samma verifierade medlems-/identitetskrav.

Filsnapshoten bevarar de sex frusna källorna, 65/67/70-prov, gamla67-diffen,
bevarandekontroller/reviews, kopiemetodens NOT_RUN-föregångare och körda version,
fulla preparation/qualification/post-captures samt kontinuitet vid snapshot.
Gamla resultat behåller sina subjekt. Arkivet återställer inte originala Git-admin,
processer, katalogmetadata eller hela Nortropic. Ingen projektkod kördes vid restore.
Gamla assets överfördes inte igen och inget raderades eller pushades till plattformen.
Senare kontinuitetsnotiser tillhör nästa checkpoint; tidigare kvarvarande luckor
för känslig lokal evidens och full fjärrbas+delta-restore är oförändrade.

## Senare H039 verifierarutkast — 12 filer faktiskt återställda

En ny liten batch säkrar det ofrusna sexfilsutkastet vid exakt
P `005366dd5e3a9a74d8140c9dd0c0175aea268294` plus tre inerta provrekord,
rootens bevarandekontroll, kontinuitet och urvalslista.
43/43 är endast 18 inerta semantikfall och25 rena käll-/syntetiska graphfall.
Ingen ny full grind/frysning/produkt/load/query/runtimecredit.
138 andra spårade filer jämfördes med P:s exakta blobbytes/modes i ec6c28;
original kvalificerad P är ren. Denna jämförelse finns bland arkivets evidens.

Privat repoID1367371291 kontrollerades602900 före överföring.
Release `backup-20260912-h039-product-P-005366dd` ID387676316,
nytt asset559877762, `h039-verifier-draft-P005366dd-20260912.tar.gz`,
1080389B, SHA256 `98caf435fb124c9ca5b80bad507aaa7f84909a23418ae2729f99a6b013aa22da`.
Preparef5de4c, upload8376c5→e73e15, download e1bd34→a0f71c och
faktisk restore40b464 gav allaexit0; serverdigest b0c9f4 stämmer.
12 logiska filer/24tarposter, inga skannerträffar, oförändrade källor.
Restore: `/private/tmp/nortropic-h039-verifier-draft-restore-if8crf7p`;
bytes/storlek/mode/uid/gid/mtime/xattrs/singlelink/oberoende inoder verifierade.

Läs `H039-VERIFIER-DRAFT-SELECTION.json`, `...-INSPECTION.json`,
`...-RESTORE.json` och `SNAPSHOT-H039-VERIFIER-DRAFT.py`.
SelectionSHA36c69f7ced73350ecd5d5ac8005ec237c8f619335792afe80e3981a63e3aedfb,
inspectionSHAe2e30a97fc7284a91238330ecec46671387adc12a108e90f789b68f065ff96ff,
receiptSHA3d0a13e743b37d3324b6508587836f75ae239ff8063c9aadb18bb435cce018b8,
methodSHAeb801ac94cd87b88aa8662a65ce2b7c6a5bf1c4cd3d4d6d078d4c8fae2d99756.
Metoddiff dd96a5 ändrar endast urval/namn/antal/omfattning och höjer diskmarginalen
från32 till64MiB över20GiB; samma prövade innehålls-/metadata-/restorekontroller.

Återställ först i NY isolerad rot, aldrig över original. De sex källfilerna kan
rekonstruera just detta opublicerade utkast ovanpå den separat redan återställda
B→C→P-bundlekedjan; detta är INTE en backup av dess hela Gitadministration,
index-/processidentiteter eller full Nortropic. Ingen arkiverad kod kördes.
Inget gammalt asset omöverfördes, inget raderades och inget plattformsrepo pushades.
Författaren fick fortsätta nästa tranche efter att dessa exakta bytes säkrats:
senare ändringar och senare kontinuitet tillhör nästa checkpoint.
Befintliga generella custody-/bas+delta-/lokala representationsluckor består.


## Senare korrigerad H039 P005366dd — lokal kvalificering och ny96filers backup

Samma oförändrade P har nu kvalificerats i den separat granskade korrigerade
fixturen: faktiskt final-exit0,133/133 unika sanna rader,
`PASS_LOCAL_QUALIFICATION_ONLY`. Dess H039-child0 ger40/40 och endast
`PASS_ASSET_BUILD_ONLY_NOT_H039_PASS_OR_ATTESTATION`. Oberoende postreview
SHA256 `ce1b7231bc951e6e351a30131f29db11a6220c1d43f429930ae15086f18e4474`
bekräftar utfallet och exakt230rader före/efter, gamlaP:s253oförändrade rader,
16fångade byggkommandon och20byteidentiska laneoutputs. TidigareRED bevaras
på sin ursprungliga fixtur; nedanstående historiskaRED-checkpoint omskrivs inte.
Ingen fullH039, attestation, native-loading, installation eller runtimecredit.

Privata repot ID1367371291 återkontrollerades57735e. Nytt asset559832407 i
befintlig release `backup-20260912-h039-product-P-005366dd` ID387676316:
`h039-P-005366dd-corrected-final-green-20260912.tar.gz`,592950bytes,
SHA256 `da0fdb1c85f1e204a5081aa9a3297ba59d0fe9bb42808f8717ec4eb9376fea15`.
Upload462006 exit0, faktisk download/serverdigest485161 exit0.
Restore6a468c exit0 återställde96reguljära filer i ny isolerad rot
`/private/tmp/nortropic-h039-P-green-restore-mjnkb0tp`.
Bytes/storlek/mode/uid/gid/mtime/xattrs/singlelink/oberoende inoder verifierade.
192tarposter inkluderar AppleDouble; inga absoluta paths/länkar. Ingen arkiverad
kod kördes, inget original ändrades och inget raderades.

Läs `H039-P-005366DD-GREEN-SELECTION.json`, `...-INSPECTION.json` och
`...-RESTORE.json`; restorereceipt SHA256
`b75c0a7e012c05eb5a1158498ee9e358aca1160dfb36cde28d888c62fd72fd87`.
`SNAPSHOT-H039-P-005366DD-GREEN.py` SHA256
`34db093a10ab41bee1f1aaf4a5ead3a2aa4f253b5790d9fd19d34d69ee227175`
är samma tidigare prövade fasta tar-/filrestoremetod, endast urval/namn/antal
och omfattning anpassade. Root jämförde e4f9c3 och kontrollerade alla fyra
kopierade rapport-/metodbytes c553c4. Innehållssökningen gav inga träffar.

Omfattning: korrigerad replik-R2/metodreviews/mockprov, verkliga prepresultat,
grönfinalens huvudresultat/captures/fullpre-/postmap, oberoende produktreview,
de två nya råbyggbanorna och kontinuitetsfilen vid snapshot, plus fillistan.
Paths är källhierarki utan ledande slash: återställ ENDAST i ny isolerad rot.
Detta är fristående evidensfilurval, inte ett överlägg för arbetskopian.
Produktens Gitobjekt följer den redan återställda B→C→P-bundlekedjan nedan;
ingen ny produktbundle eller gammalöverföring har upprepats.

Hela final-fixturens interna Gitkopior och samtliga understimulusfiler, original-
repoernas administration och en full ny fjärrbas+delta-filsystemsrestore täcks
INTE av denna96filers kontroll. Katalogmetadata/ursprungliga inoder återskapas
inte. Senare kontinuitet efter snapshot tillhör nästa checkpoint. De tidigare
generella backup-/custodyluckorna kvarstår; denna batch påstår inte att allt är säkrat.

## Senare H039 P005366dd — Git-objekt återställda, kvalificering röd

Senare i samma release finns även asset559809543:
`h039-P-005366dd-construction-and-first-final-20260912.tar.gz`,473518B,
SHA256 `d738c02c4d6fcc45c0d30cfa2cd6bfa2c12e97eccf1762759134dc7dd1a192c8`.
Faktisk uploadcf80e0→77dc41, download952b98→84620e och filrestore9ffc8c
gav exit0.97 utvalda reguljära filer (194 tarposter inklusive AppleDouble)
återställdes med bytes/storlek/mode/uid/gid/mtime/xattrs och oberoende inoder.
Se `H039-P-005366DD-EVIDENCE-INSPECTION.json`, `...-SELECTION.json` och
`...-RESTORE.json`; faktisk restorereceipt SHA256
`195f0be6e697d3492e39a6237657b509601f575ded202523ecae07384cb3b355`.

Arkivet använder källans hierarki UTAN inledande slash för att undvika namn-
kollisioner. Packa bara upp i ny isolerad rot, aldrig i `/` eller över original.
`SNAPSHOT-H039-P-005366DD-EVIDENCE.py` är det granskade fasta verktyget,
SHA256 `55d827c20919b7e68aabe5cd003961ab804bb9abb891e757bd56bb52739c169d`.
Omfattning: byggmetodens gamla/R2-versioner, reviews, placementmetod,
två råbyggbanor med outputs och16 kommandofångster, samt första misslyckade
finalförsökets huvudresultat/fångster och148raders pre/postmap.97 inkluderar
fillistan själv. Inga filer raderades. Källkatalogernas metadata, hela final-
fixturen och senare korrigerad replikmetod R2 är INTE täckta av denna snapshot.
Den ursprungliga oförsökta replikmetoden f6b2/d3e0 ingår som historik, inte READY.

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

Vid den första bundlecheckpointen var builder-/metod-/råbygg- och full
kvalificeringsevidens fortfarande LOCAL_ONLY. Den senare97-filssnapshoten ovan
säkrar den där exakt uppräknade delen. Originalen ligger kvar i
`evidence/v316-h039-continuity-review-20260912/` och namngivna rårotar.
Senare replik-R2-arbete och ej utvalda fulla fixturer är ännu LOCAL_ONLY;
inga äldre arkiv får sägas innehålla dessa senare filer.

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
