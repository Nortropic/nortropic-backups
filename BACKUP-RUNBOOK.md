# Löpande backup för Nortropic

Arbetsrutin dokumenterad 2026-09-12 på användarens uttryckliga begäran:
”viktigt att det dokumenteras nu hur backup:en på git ska fungera och löpande
fungera, fortsätt arbeta.” Detta gäller backup och kontinuitet, inte ändrade
produktregler, bootstrapcredit, driftstart eller generell raderingsbehörighet.

## En destination och två typer av innehåll

Privat destination: **Nortropic/nortropic-backups**, repository ID **1367371291**.
Kontrollera både ID och `private: true` före varje överföring. Avvikelse stoppar
överföringen; ändra inte synlighet eller välj ett annat repo automatiskt.

- Git-historiken i backuprepot innehåller denna rutin, katalog, manifest,
  kontrollsummor, återställningsinstruktioner, granskade backupverktyg och kvitton.
- Själva arkiven/bundlarna ligger som unikt namngivna **Release assets** i samma
  privata repo, inte som stora binärer i vanlig Git-historik. En vanlig clone av
  backuprepot hämtar alltså INTE arkiven. Återställaren måste hämta rätt assets.
- Produktrepo, arbetskopior och bootstrapens evidensbehörighet förblir separata.
  Backuprepot är inte en alternativ publiceringsväg eller aktiv auktoritetskälla.

## Vad som måste följa med

Bevara kernel, hela bootstrapkedjan och samtliga tidigare H-arbeten: implementation,
specifikationer, frusna tester, recept, manifest, beslut, Git-refs/nödvändiga objekt,
granskningar, evidens samt opublicerade, ändrade, genererade och ospårade filer.
Index, worktree-administration och relevanta filer utanför repot ingår när de
behövs för återställning. Återanvänd befintlig inventering och komplettera bara
för ändringar sedan föregående checkpoint; gör inte en ny totalinventering varje gång.

En push av produktkod eller en Git-bundle ersätter inte backup av arbetsläget.
En katalogpost, lokal kopia eller lyckad fsck ersätter inte en återställningsövning.
Förkastade/förbrukade försök och gamla PASS behåller sina ursprungliga subjekt och
sin status. Flytt, nya filidentiteter eller ny backup ger aldrig ny testcredit.

Credentials, privata nycklar, autentiseringssessioner och identitetsbundna
capability-/custodyobjekt får inte följa med enbart för att repot är privat.
Granska innehållet även inuti Git-objekt, komprimerade arkiv och metadata.
Dokumentera undantag utan att skriva hemliga värden i katalog/logg. Vid verkligt
känsligt material: behåll originalet och markera luckan; använd rätt separata
custodyväg. Ändra inte originalbevis för att göra det uppladdningsbart.

## När backup ska göras och vem som gör den

Den agent/operatör som arbetar ansvarar för att genomföra eller tydligt lämna
över checkpointen. Det är en arbetsrutin, inte en installerad bakgrundstjänst.

1. Vid varje materiell checkpoint: nya hållna kandidatbytes, färdig granskning,
   nytt viktigt fel-/försöksresultat eller ändrat opublicerat arbetsläge.
2. Före konto-/agent-/hostöverlämning och vid slutet av en aktiv arbetsdag:
   säkerställ att ändringar sedan senaste verifierade backup täcks, eller lämna
   en exakt lista över ännu osäkrade filer/resultat. Återanvänd en oförändrad,
   redan verifierad batch; skapa inte en dubblett bara för att dagen ändrats.
3. Före tillåten migration, radering eller annan svåråterkallelig ändring:
   säkerställ återställbarhet för den exakta berörda ytan. Backup är inte i sig
   godkännande att genomföra ändringen.
4. Varje aktiv arbetsvecka: gå igenom öppna täckningsluckor och öva återställning
   av senast ändrade deltakoppling. Efter ändrat arkivformat/återställningsverktyg
   eller en större milstolpe: prova en komplett relevant bas+delta-kedja.

Ingen cron/launchd/CI eller schemalagd agent är installerad för detta. Det finns
ingen utlovad nattlig körning när ingen arbetar. Mål för dataförlustfönstret är
senaste materiella checkpoint, inte en uppmätt tids-SLA. Återställningstid är inte
uppmätt för hela systemet. Missad checkpoint ska synas i överlämningen.

## Genomför en checkpoint

1. Läs senaste kvitto/katalog och kontinuitetsnotering. Återuppta inte en redan
   pågående uppladdning genom att starta en andra. Kontrollera aktuell process/
   release/receipt först; en klientförbindelse kan brytas efter en lyckad upload.
2. Avgränsa ändrade filer, repo-/ref-/objektbehov och relevanta externa artefakter.
   Kopiera ett sammanhängande, identifierat arbetsläge; attestera inte filer som
   ändras under insamling. Använd privata nya mål och exklusiv filskapning.
3. Skapa en ny unikt namngiven batch (UTC-stämpel + ändamål/subjekt). Använd
   deltakopior för ändrat arbetsläge och relevanta bundles för Git. Ange exakt
   bas, om deltat är kumulativt eller inkrementellt, ordning och borttagna paths.
   Bevara tidigare generationer; skriv inte över gamla arkiv eller kvitton.
4. Registrera källor, storlekar, SHA256, medlemskap/metadata, Git-identiteter,
   undantag och återställningsberoenden. Granska innehåll före överföring.
   Okända payloads är en öppen granskningsuppgift, inte automatiskt godkända.
5. Mät disk och budgetera skapande, eventuell download, uppackning och marginal.
   Följ befintlig retentionregel (15 GiB startgolv, 20 GiB normalmål). Vid stora
   arkiv: använd prövad multiparttransport med fasta delidentiteter, ordning,
   fullarkivhash och negativa prov. Kontrollera GitHubs aktuella assetgräns inför
   ett nytt format; den senast dokumenterade gränsen är under 2 GiB per asset.
6. Kontrollera privat repoidentitet och ladda upp EN gång under nya assetnamn.
   Ingen force-push, mirror/prune, clobber eller automatisk ersättning av en
   befintlig release/asset. Vid delvis lyckad upload: dokumentera de faktiska
   objekten och fortsätt bara med identifierade saknade delar.
7. Hämta tillbaka från GitHub. Kontrollera server-/download-/källidentiteter och
   fullständiga bytes. Strömmad återläsning kan spara disk men får inte kallas
   fullständig filsystemsrestaurering om inga filer faktiskt har återställts.
8. Gör verklig återställning i ny isolerad yta när batchens nivå kräver det:
   verifiera medlemskap, bytes, typer, modes och stödd metadata samt Git-objekt/
   refs. Kontrollera paths/länkar före extraktion. Bevara felresultat; kör inte
   arkiverad projektkod och aktivera inte pekare till originalkopiorna.
9. Skriv faktiskt kvitto med kommandon/exit, identiteter, omfattning och luckor.
   Uppdatera endast berörda katalogposter, gör vanlig backup-only commit/push,
   och kontrollera remote commit/privat status. Länka kvittot från befintlig
   lokal kontinuitetsdokumentation. Dokumentändringar efter arkivets snapshot
   tillhör nästa checkpoint och får inte låtsas ingå i det äldre arkivet.

## Resultatnivåer — håll isär dem

| Faktiskt bevis | Vad det inte bevisar |
|---|---|
| Lokal/granskad/överföringsklar kopia | Att något finns på GitHub |
| Uppladdad asset | Att download eller återställning fungerar |
| `REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED` | Återskapat tar-byteflöde, inte uppackat arbetsläge |
| `REMOTE_GIT_BUNDLE_RESTORED_VERIFIED` | Återställda bundleobjekt/refs, inte index, dirty/ospårat eller hela worktree-administrationen |
| `REMOTE_RESTORED_VERIFIED` för en avgränsad filbatch | Bara det faktiskt provade medlemskapet/metadata, inte hela Nortropic |
| Komplett relevant bas+delta-restaurering med redovisade kontroller | Ingen runtime-, publicerings- eller bootstrapcredit |

Äldre rapporter får ha sina ursprungliga statusnamn. Läs deras omfattning, inte
bara ett ord som PASS. En statussammanställning får inte skriva om historiska
försök som lyckade. Återställningsmappade worktree-HEADs bevarar commitspetsar;
de är inte originalens administrationsstruktur. Inode/ctime/levande identiteter
återskapas inte av en ny kopia och måste vid behov prövas genom rätt senare väg.

## Disk och retention

Behåll aktiva arbetskopior och nödvändig aktuell evidens lokalt. Använd deltakopior
och strömmad kontroll där det är lämpligt; skapa inte flera fulla arbetskopior av
slentrian. En ny full bas kan tas vid en större milstolpe eller när deltakedjan
blir svår att återställa, men äldre beroenden får inte pensioneras förrän den nya
kedjans täckning och återställning är bevisad.

Inget raderas automatiskt lokalt eller i GitHub. Lokal pensionering kräver separat
exakt målklassning enligt BOOTSTRAP-DISK-RETENTION-RULE.md och cleanupjournalen:
återställningsbevis för just målens data, inga aktiva process-/review-/ref-/evidens-
beroenden, inga okända filer och rätt befogenhet. Upload eller strömmad tar-kontroll
ensam räcker inte. Repo/.git/worktree-förbud i retentionregeln får inte kringgås.
Okänt = behåll. Det finns ingen automatisk åldersgräns som gör gamla H-arbeten
raderbara, och ingen maxkvot som motiverar att unika bevis tappas.

GitHub ger en kopia utanför datorn, men konto-/organisationsåtkomst och GitHub är
fortfarande gemensamma felkällor. En separat oberoende destination är en kvarstående
resiliensförbättring, inte något som redan finns. Credentials flyttas inte till
backuprepot för att lösa åtkomst eller återställning.

## Överlämningsrad

För den befintliga 2026-09-10-kedjan finns kontrollerade kopplingar i
`RESTORE-CHAIN-INDEX.json`: basens manifesthash, sju kumulativa deltas,
respektive manifest/fillista och historisk borttagningslista. Indexet är inte
överföring av dessa payloads. Se dess uttryckliga local-only-luckor innan någon
försöker återställa det senaste arbetsläget från bara huvudarkivet.

Varje avstämning ska ange: senaste verifierade batch/remote commit, exakt vad som
täcks, vad som endast är uppladdat/strömkontrollerat, lokalt-only arbete sedan dess,
bas/delta-/custodyberoenden, pågående transfer-ID/process, diskstatus och nästa
avgränsade åtgärd. Fråga inte efter en ny generell fullmakt för redan beställd backup.
Påstå inte att allt är säkrat när en enda relevant koppling fortfarande saknas.
