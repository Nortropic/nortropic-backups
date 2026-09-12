# Bootstrap — arbetssätt och källnavigation

Uppdaterad 2026-09-09. Lokal dokumentation enligt ägarens dokumentationsmandat.
Detta är **inte** authority, task-spec, grind, backlog eller färdigstatusdatabas.
Ingen säkerhetsregel införs genom denna text. Handoff beskriver VAR vi är;
källor/evidens visar VAD som är tillåtet och bevisat; denna fil beskriver HUR.

## Källor och giltighet

### Löpande off-host-backup — tillägg 2026-09-12

Användaren begärde uttryckligen att dokumentera hur GitHub-backupen ska fungera
löpande. Rutinen finns i det privata backuprepots
[BACKUP-RUNBOOK.md](https://github.com/Nortropic/nortropic-backups/blob/main/BACKUP-RUNBOOK.md),
repository ID1367371291. Lokal arbetskopia:
`/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/repo/BACKUP-RUNBOOK.md`.
Git håller katalog/metod/kvitton; arkiv ligger som separata Release assets och
hämtas inte genom en vanlig clone. Följ checkpoint-, innehållsgransknings-,
återläsnings- och återställningsrutinen där. Rapportera öppna täckningsluckor vid
överlämning och aktiv arbetsdags slut. Ingen bakgrundsscheduler är installerad.
Senaste faktiska resultat står i BOOTSTRAP-DISK-CLEANUP-JOURNAL.md och backupkvittot.
Upload/strömmad återläsning är inte full filsystemsrestaurering och ger ingen
cleanup-, runtime- eller bootstrapcredit. Befintlig retentionregel kvarstår.

### Tidigare mandat- och källnoteringar

Senaste uttryckliga ägarmandat i denna konversation, 2026-09-09:
”Du har mitt fulla godkännande att göra det du anser fram till supervisor resume,
arbeta mot slutmålet. Om du behöver uppdatera någo dokumentations för att alltid
förstå detta, gör det gärna.” Beslutet kom som svar på frågan om ett nytt exakt
byggmätningsförsök med utökad hostbehörighet och färsk byggrot. Fortsätt därför
autonomt med nödvändiga kontraktsenliga steg och dokumentation; begär inte nya
generella scheduling-godkännanden vid varje delmål. Det tidigare nekade försöket
förblir consumed/no-credit; det nya försöket får inte återanvända dess rot.
Mandatet är inte ett verifieringsresultat och ändrar inte frusna säkerhetskrav,
föreskriven rollseparation eller faktiska verktygs-/behörighetsspärrar. Särskilda
mänskliga ceremonier och materiella policyval hanteras enligt sina styrande
krav, inte genom att återuppliva gamla generella operationsförbud.

Senare ägarmandat 2026-09-09 ger full behörighet inom målet supervisor resume
och upphäver tidigare operativa förbud för kontraktsenligt arbete. Se handoffens
översta status för ordagrann källa och den nya read-only remote-kontrollen.
Frusna grindar, förbrukade försök och human-only-ceremonier kvarstår.
Tidigare dokumentationscheckpoint hade canonical aktualitet **OVERIFIERAD**
under Git-/nätverks-/processförbud. Nedanstående källtabell beskriver den
checkpointen: lokala källor är lästa, inte därmed bevisat
aktuella på origin/main. Nyare text eller lokal förekomst löser inte precedence.
Inga gamla instruktioner får exekveras bara för att de finns i en länk.

| Källa/avsnitt | Egenskap och tillämpning | Källstatus |
|---|---|---|
| [AGENTS-router](worktrees/h039-r33-formal-gate-review-a-r4/AGENTS.md), Auktoritet/rollseparation/v3/v4 | Hänvisar i ordning till konstitution, regelverk, loopregler, aktuell task och dess exit-test; separerar roller och mekanisk authority | Lokalt dokumenterad repo-kopia; canonical aktualitet overifierad |
| [Roadmap-delegation v3](worktrees/h039-r33-formal-gate-review-a-r4/docs/loop/codex-autopilot-v3-full-roadmap.md), roadmap, owner-routing, closeout | Planref `0b3212c991d4227c8df2656465ae2c0252dda39e`; autonomt arbete inom delegerad plan, särskilda hard stops och slutgrind | Lokalt dokumenterad; aktiveringsvillkor måste verifieras före användning |
| [Harness substitution v1](worktrees/h039-r33-formal-gate-review-a-r4/docs/loop/harness-substitution-contract-v1.md), §§1–4 | Provider äger intelligens, Nortropic äger policy/containment/attestation/promotion; substitution kräver bevis | Lokalt dokumenterad owner-amendment 2026-08-11; inte ny behörighet här |
| [Owner-author workflow](worktrees/h039-r33-formal-gate-review-a-r4/docs/loop/owner-author-workflow-v1.md), berörd H039-revision | Specifik freeze/review/publication/effect-kedja; historiska avsnitt är inte nya körorder | Frusen reviewkopias dokumentation; exakt aktuell task/gate måste bindas senare |
| [Evidence-kontrakt](worktrees/h039-r33-formal-gate-review-a-r4/docs/loop/codex-evidence-contract.md), status/closeout | Kommando, exit och identitet skiljs från agentutsagor; ingen prosa-PASS | Lokalt dokumenterat rapportformat, inte verdict authority |
| [Disk-retention](BOOTSTRAP-DISK-RETENTION-RULE.md), Standing rule 1–9 | Diskgolv, dependency/identity-kontroll och bevarande av okänt | Etablerad lokal driftregel 2026-08-31; ingen generell deletion-authority |
| [Cleanupjournal](BOOTSTRAP-DISK-CLEANUP-JOURNAL.md), daterade poster | Exakta tidigare mål, godkännanden, bevis och undantag | Historisk/workflow-evidens; inte återanvändbar körbehörighet |
| [Bootstrap-handoff](CODEX-BOOTSTRAP-HANDOFF.md), Arbetsmetod och kontinuitet | Bestående navigering; äldre daterade lägen hålls isär | Etablerad lokal kontinuitetsyta |
| [Socket-handoff](CODEX-TO-CODEX-TAKEOVER-20260908-H039-R33-SOCKET-ANALYSIS.md), §§2–10 | R33-resultat, consumed attempts, custody och dåvarande offlinegräns | Historisk hashbunden checkpoint, bevarad oförändrad; senare uttryckliga beslut måste läsas |

## Mål och leveransnivåer

Slutmålet är oförändrat: Trust Kernel och full planerad autonomi enligt den
auktoritativa roadmapens verkliga kriterier, inte ett MVP. Den lokalt lästa
roadmapen skiljer frozen program gate/oberoende empirical closeout från extern
aktivering/promoter-identitet. Verifiera aktuell version innan slutstatus döms.

Kontrakt publicerat ≠ produkt granskad ≠ installerad effekt ≠ H039 completed ≠
återstående Bootstrap completed ≠ supervisor resume ≠ första verkliga mission ≠
full software-/externt aktiverad autonomi. PASS-, PR- eller R-antal ger ingen
procent färdigt. Provideroutput, sessioner och rollseparation är inte trust proof.

## Arbetsflöde och stoppklassificering

Arbeta autonomt inom exakt verifierat mandat: rollseparerad kandidat, liten
förkontroll, freeze, oberoende review, tillåten rättning och guarded publication
när aktuell authority kräver/tillåter detta. Vanliga findings inom skrivytan
hanteras utan ett nytt mänskligt "kör". Förbrukat liveförsök är inte vanlig
utvecklingsretry. Rapportera inte en granskning av dokument som en körd grind.

Klassificera före mänsklig eskalering:

- `LOCAL_MANDATE_BOUNDARY`: deluppgift slut; högre **verifierad** delegation
  tillåter fortsättning utan mänsklig scheduling.
- `CANONICAL_OWNER_HARD_STOP`: identifierad högre/frusen klausul kräver owner.
- `CANONICAL_OWNER_TTY_OR_ROOT_CEREMONY`: exakt föreskriven mänsklig operation.
- `AUTHORITY_UNVERIFIED`: precedence/aktivering kan inte fastställas. Ange vilken
  read-only canonical kontroll som saknas, inte en påhittad behörighet.

Generell delegation upphäver inte automatiskt specifika aktuella förbud; lokala
historiska owner-stops upphäver inte automatiskt senare canonical delegation.
Ange källa, hinder, minsta nödvändiga owner action och vad som sedan fortsätter.
Oklar nästa fas ska inte blockera orelaterat redan tillåtet arbete.

Skilj ett faktiskt nekat verktygs-/behörighetsbeslut från en tvetydig felkod
inne i en granskad drivrutin. Exempel från aktuell byggmätning: sandbox_apply
EPERM stoppade den första miljön; i senare godkänt hostförsök lyckades clang,
men killpg efter WNOWAIT-exit gav EPERM. Den senare koden kan enligt Apple XNU
även uppstå för en zombie-only-grupp. Den får varken ignoreras eller automatiskt
utlösa ännu en generell fullmaktsfråga. Bevara utfallet, gör tillåten read-only
orsaksanalys och låt föreskriven rollseparation pröva en avgränsad rättning.
Verkliga behörighetsspärrar kringgås inte; inga gamla försök återfår credit.

Ett agentverktygsfel gäller den observerade operationen, inte automatiskt all
fortsättning. `agent thread limit reached` vid kontakt med en gammal tråd
bevisade här inte behov av konto-/sessionsbyte: statuskontroll följd av normal
spawn av en separat TEST_AUTHOR lyckades i samma session. Kontrollera tillgängliga
normala verktygsvägar, bevara rollseparationen och fortsätt opåverkat arbete.
Påstå inte känd global gräns eller garanterad återställning utifrån en felsträng.

Efter ett meddelandeavbrott kan en rollagent stå som `interrupted`. Kontrollera
status innan väntan: ett vanligt meddelande är inte samma sak som att återuppta
agentens uppgift. Använd den normala återupptagningsfunktionen och bevara dess
roll och hållna bytes; starta inte en andra writer för samma yta.

## Bevarande inför eventuell uppdelning — ägarförtydligande 2026-09-09

Användarens aktuella meddelande förmedlar uttryckligen följande svar från
Improvements-uppgift `01a0865b-3206-7061-9344-29d0c67c0253`, host local:
”Ja, så inge arbete går förlorat för kernel, bootstrap, det gäller ju förstås
även tidigare h-arbeten”. Originaltranskriptet i den andra uppgiften har inte
hämtats i denna avstämning; separat transkriptverifikation är OVERIFIERAT.
Det aktuella direkta meddelandet beställer självt detta bevarandekrav och dess
bokföring. Kravet dokumenteras här, inte som en redan körd migrationsgrind.

Bevarande omfattar kernel, hela bootstrapkedjan och samtliga tidigare H-arbeten,
inte bara H039: implementation, specifikationer, frusna tester, byggrecept,
manifest, dokumenterade beslut, Git-historik och nödvändiga objekt, granskningar,
evidens, pågående/opublicerade ändringar samt relevanta genererade, ospårade
och ignorerade artefakter. Ålder, okänd klassning eller frånvaro ur senaste
kandidaten innebär inte att något är raderbart. Förkastade/förbrukade försök
behåller sin historiska status; flytt ger dem aldrig ny credit.

För en senare konkret migrationskandidat ska följande tas in som acceptanskrav
genom den då gällande test-first-/ändringsvägen, före faktisk flytt:

- Utgå från [befintlig inventering](INVENTERING-SEPARATION-20260909/RAPPORT.md)
  och dess fil-, Git-, evidens- och WIP-kartor. Komplettera för den konkreta
  flyttytan och dess beroenden; senaste kandidatens fillista räcker inte.
  Redovisa var varje berört tidigare arbete och nödvändiga objekt finns,
  deras identiteter/status, undantag och kvarstående luckor.
- Visa verifierbart hur originaltillståndet kan återställas, inklusive refs,
  nödvändig objektmängd, index-/arbetskopieändringar och relevanta artefakter
  utanför Git. Ange faktiska återställningsprov och resultat; en kopia, clean
  status eller lyckad fsck ensam bevisar inte komplett återställbarhet.
- Spåra beroenden och verifieringsbindningar från original till föreslagen
  struktur: konsumenter, paths, blob-/manifest-/snapshotidentiteter, byggrecept,
  frusna tester och evidensreferenser. Saknat arbete eller bruten beviskedja
  får inte döljas genom svagare tester eller omklassning till ovidkommande.
- Bevara gamla PASS som bevis endast för sina ursprungliga subjekt och
  förutsättningar. Pröva påverkan på den nya strukturen separat; varken flytt
  eller ny kontrollsumma överför review-, bootstrap- eller runtimecredit.

Full historisk bevarande-/återställnings- och beroendeslutning är inte bevisad
genom denna dokumentationsavstämning. Ingen fysisk migration, cleanup,
historikomskrivning eller utökad operationsbehörighet beställs. Eventuell
tvårepoindelning är fortsatt en möjlig struktur, inte beslutad fysisk flytt.
Credential-/identitetsbunden evidens kräver sin separata custodyväg; kravet är
inte tillåtelse att kopiera credentials. Fortsätt tillåtet avgränsat arbete
utan att göra detta till en ny generell fullmaktsfråga.

## Cleanup och retention

Containment får inte ersättas av cleanup. Cleanupens säkerhetsroll, obligatoriska
livscykelkrav och befogenheter bestäms av respektive fruset kontrakt; de får inte
nedgraderas genom denna arbetsmetodsbeskrivning. Housekeeping av disk/worktrees
och H039:s privilegierade runtime-cleanup är separata behörighetsdomäner.
En sista identitetskontroll ensam eliminerar inte en möjlig race; använd endast
den mekanism som respektive kontrakt föreskriver.

Följ retentionskällans exakta klassificering och dependencies. NO-CREDIT,
historisk eller reproducerbar innebär inte raderbar. Bevara WIP, unique proof,
aktuella reviews, förbrukade latchar och okända objekt. Äldre journalscripts är
exempel med egna exakta beslut, inte en generell verktygslåda för nya raderingar.
Identitetsbyte/foreign data ska stoppa. Ingen cleanup utförs enligt denna fil.

Hänvisade worktrees och andra lokala artifacts kan vara fortsättningsberoenden.
Vid nästa redan tillåtna retentionsbedömning ska deras betydelse bedömas enligt
befintlig retentionsregel innan borttagning. En länk innebär inte automatiskt
permanent retention; lokal förekomst innebär inte canonical aktualitet.

Diskregelns golv inför tungt arbete är 15 GiB (15 728 640 KiB); normalmål 20 GiB.
Mät när relevant, använd inte gamla df-värden som aktuella. Reboot är inte en
ofarlig cleanupmetod: journalen 2026-09-08 dokumenterar förlust av transient
/private/tmp-custody och ändrade dev-identiteter. Sessionsarkiv/credentials är
separata frågor; kopiera/radera dem inte för att göra handoff enklare.

## Integration, lärdomar och parallellitet

**Infört/belagt:** separata hashbundna kandidater/reviews, bevarade failure-records,
och R33:s riktade kausala mapping-/registry-kontroller enligt cleanupjournalens
poster 2026-09-08. Dessa ger inte assurance för senare bytes.

**Aktuell arbetsprincip, ännu inte en körd adapterpreflight:** kontrollera
`adapter → consumer → validator → lifecycle` tillsammans före nästa freeze.
Ta med wrapper/scope, bytegränser, names/counts, historisk kontra live identity,
resultatschema och positiva/kausalt negativa fall. Kontrollera syskonfel inom
tillåtet scope. Testa faktisk genererad logik där authority medger det; mockar
bevisar inte host-ABI. Behåll formella reviews och alla negativa kontroller.

Återkommande dokumenterade klasser: fixture-umask/config/object-closure
(Bootstrap-handoff september 5); boot-volatila identiteter och stale counts
(cleanupjournal september 8); consumer/socket-API-antagande och close-metadata
([offlineanalys](worktrees/h039-r33-socket-compat-probe/OFFLINE-ANALYSIS.md)).
Minsta förbättring är en sammanhängande bounded konsistenskontroll, inte ännu
ett generellt preflight-/assurance-system. Mät dess kostnad innan påstådd vinst.

Oberoende read-only analys kan parallelliseras när mandatet medger det. En writer
per gemensam yta; trust transitions följer föreskriven serie. Reads, Git och
separata worktrees är inte automatiskt ofarliga under exklusiv körning. Ändra
inte metod/metadata eller rensa beroenden mitt i sådan körning. En levande process
är inte framstegsbevis; processfrånvaro får inte hävdas utan tillåten observation.

## Aktuella begränsningar och öppna frågor (checkpoint 2026-09-09)

Historiskt checkpointläge nedan. Det senare fullmaktsbeslutet och återverifierat
remote-main står överst i handoffen; de gamla generella operationsförbuden ska
inte återinföras som aktuella. Specifika kontraktskrav måste fortsatt beläggas.

- Explicit godkänt: offline adapterkandidatens åtta filer samt den exklusiva
  byggytan. Senare kandidatleverans 2026-09-09: två förreviews, kompilering/statisk
  inspektion och två statiska slutreviews utförda. Ingen native-loading/query.
  Se aktuell handoff för exakta subjekt, resultat, varning och beslutskällor;
  tidigare dokumentationscheckpoint var före kompilering.
- Git/nätverk/processinspektion, produkt-/kontraktsändring, root/runtime/probe,
  cleanup och downstream är fortsatt otillåtna. Befogenhet efter leveransen:
  `AUTHORITY_UNVERIFIED`, inte bevisat canonical hard stop.
- Äldre v2-rebase-text samexisterar med senare no-force/normal-merge-regler.
  Detta dokument löser inte konflikten. Current main/task/gate/aktivering måste
  verifieras när read-only Git/nätverk tillåts; saknade objekt ska redovisas.
- Adapter-image/ABI/loading, ny sequence2-livscykel och receipt-policy är
  separata releaseblockers; designreview är inte operativt bevis.

## Handoffdisciplin — ingen ny hashceremoni

Läs först den aktuella handoffsektionen och arbetsmetodsbeskrivningen. Läs
därefter de relevanta auktoritativa källorna och evidensen för nästa operation.
Äldre kronologi läses när den behövs för beroenden, motsägelser, förbrukade
försök eller felsökning — inte rutinmässigt i sin helhet vid varje arbetssteg.
Detta ersätter aldrig en föreskriven kontraktsläsning eller återverifiering.

Godkännandets källtyp och faktiska uttryckliga ord ska kunna återfinnas separat
från beslutsförslag och deras hashvärden. Aktuell handoff återger ägarens två
godkännanden ur denna konversation utan påhittade meddelande-ID:n. En sådan
återgivning är inte självständig autentisering: om mottagaren inte kan belägga
mandatet ska kontinuitetsluckan redovisas. Det stoppar inte redan uttryckligen
godkänt arbete i avsändarsessionen. Historiska UNAPPROVED-etiketter bevaras.

Inför framtida handoff: kontrollera denna fils åtkomlighet, för med hänvisningen
och uppdatera endast betydelsefulla beslut/lärdomar. Bevara befintlig bevis- och
retentionsdisciplin; inför ingen rutinmässig totalinventering. Lägg aktuell
kandidat/resultat/attempt-status i handoffens statusdel, inte i en ny databank.
Äldre hashbundna handoffs/evidens ska inte skrivas om för att verka aktuella.

Mottagaren måste faktiskt läsa hänvisade dokument och göra fasens tillåtna
återkontroller. Vi kan inte garantera automatisk läsning. Vid konto/providerbyte
på samma host: verifiera läsåtkomst. Vid annan host saknas åtkomst tills den är
bevisad; en gammal absolut path räcker inte. Flytta inte credentials eller
identitetsbundna evidensobjekt; ange nödvändig separat custody/återverifiering.
