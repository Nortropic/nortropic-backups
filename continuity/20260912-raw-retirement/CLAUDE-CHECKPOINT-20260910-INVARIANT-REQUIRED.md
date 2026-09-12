# Claude-checkpoint 2026-09-10 — fail-open-rättning, backup, H039-källgranskning

Operativt minne för omstart av Claude Code-sessionen. Inte authority, inte
nytt mandat. Källor: [Codex→Claude-handoff](CODEX-TO-CLAUDE-20260910-LOCAL-CONTINUATION.md),
[arbetsmetoden](BOOTSTRAP-WORKING-METHOD.md), användarens direkta meddelanden 2026-09-10.

## Backupkontinuitet — tillägg 2026-09-12

Senaste delkontroll: session98870 är nu slutförd exit0. Båda stora scratchpad-
arkiven (5846117376 bytes) har alla45 assets uppladdade, tom stderr, källor
oförändrade. `large-external-upload-receipt.json` är ett UPLOADED-kvitto,
inte återläsningsbevis. Session49613 fortsätter strömmad fjärråterläsning; starta
inte om uppladdningen. Det historiska första verifieringsfelet ligger kvar.
`README-CURRENT-RECOVERY.md` i backupbasen beskriver de ersatta råtarvägarna;
använd den före gamla README-RESTORE.md. Ingen full ny bas+delta-restaurering
har gjorts. Senast mätt disk20968120KiB ligger strax UNDER20GiB; tung H039-byggning
är därför fortfarande inte startad. Lokal källberedning kan fortsätta.

Senare checkpoint17:02Z+: åtta utpekade råtarrepresentationer pensionerade efter
färsk byte-exakt gziprekonstruktion och remote-/identitets-/öppna-filkontroller.
Alla nio komprimerade lokala delar, assets, originalarbetskopior och återställda
träd är kvar. Exakt karta/kvitto ligger i backuprepot som
RAW-ARCHIVE-RETIREMENT-PROPOSAL.json / RAW-ARCHIVE-RETIREMENT-RESULT.json.
Backup-only main `80804933113ba48b401ee85f7ed50f334759a2d3` pushad och remote
återkontrollerad exakt, privat repo ID1367371291; backuparbetskopia ren.
Samma commit dokumenterar liten aktiv lokal arbetsyta + GitHub-arkiv, inte
flyttad bootstrapruntime, och slutförd remote bytekontroll för ytterligare13
externa arkiv (sammanlagt47 i de två externa batcherna). Full ny fjärrbas+delta-
filsystemsrestaurering är NOT_RUN. Känslig H036-logg kvar lokalt under separat
custody, inte uppladdad. Två stora arkiv överförs/återläses i45delar; inga nya
starter av redan levande session98870(upload)/49613(readback). Session72857 är
slutförd exit0 och ska inte startas om. Tidigare status nedan är historisk.
Faktisk df efter rensning och efterkontroll20,989,380KiB (~20,02GiB); tunn marginal,
kontrollera golvet på nytt före varje tung körning. Plattformsrepot rent8095d947.
H039:s separata TEST_AUTHOR fortsätter källtranche efter dbd51ba7-hållpunkten;
inget gammalt resultat får överföras till dess ändrade bytes.

Aktuell löpande backuprutin finns i privata `Nortropic/nortropic-backups`,
repository ID1367371291, fil `BACKUP-RUNBOOK.md`; lokal kopia:
`/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/repo/BACKUP-RUNBOOK.md`.
Läs den och senaste BOOTSTRAP-DISK-CLEANUP-JOURNAL.md före fortsatt backuparbete.
Git håller metod/katalog/kvitton; stora arkiv ligger som Release assets och följer
inte med en vanlig clone. Ingen schemalagd bakgrundskörning har installerats.
Alla43befintliga katalogförda Git-bundlar har avgränsade remote restore-kvitton.
Huvudarkivets multipart-release är uppladdad; kontrollens faktiska terminalstatus
ska hämtas ur senaste kvitto/journal, inte antas från denna hänvisning. Starta inte
om en redan pågående transfer vid sessionsbyte. Kompletteringar/externt material
och senare arbetslägen har kvarstående täckningsluckor. Upload eller rekonstruerat
tar-byteflöde betyder inte full filsystemsrestaurering eller tillåten deletion.
Tidigare daterad historik nedan bevaras; denna notis ger ingen bootstrapcredit.

## Ägarens preciseringar 2026-09-10 (direkta meddelanden i sessionen)

- Tolkningen bekräftad: fail-open-rättning först, separat builder, oberoende review.
- Slutriktning: **två repos**. Plattform/kernel/bootstrap behåller repoidentitet
  `git@github.com:Nortropic/nortropic-system.git` och historik; webbförvaltningen
  flyttas ut till separat repo med allt relevant arbete och all evidens bevarad.
  "Ingen migration nu" avgränsar bara aktuellt steg; intern separation och provet
  "plattform utan webb" förbereder uppdelningen.
- Backup ska täcka evidens/opublicerat även utanför `~/nortropic` inkl. temporära
  arbetsytor; ändringar under kopiering ska redovisas och kompletteras. Bundles
  kompletterar filkopian, ersätter inte index/ospårat.
- Återställningsprov endast från kopierat material; absoluta Git-pekare får inte
  leda tillbaka till originalen; anpassning endast i kopian. Samma-disk-kopia är
  ett första bevarandesteg.
- Statisk kontroll av fem anropare ≠ fem flödestester; håll isär i rapportering.
- Ingen migration, cleanup, publicering, installation, livekörning, supervisor resume.

## Fail-open-rättning `run_invariants` — läge

| Steg | Identitet | Status |
|---|---|---|
| Bas (bevarad, orörd) | `0581dc05c1ab586a315795ea6b0a185af012edb9`, autopilot `eabcc762…` | oförändrad |
| TEST_AUTHOR-kontrakt | `worktrees/test-author-invariant-required-20260909`, gren `nortropic/loop-invariant-required-contract`, commit `0936fb6c223705dda01c5fc6ab47ba93d81ec109`, tree `f76b8310…` | fryst lokalt; arbetsyta ren (gate 755 efter chmod) |
| Nya kontraktsfiler | `verify/bin/invariant-required-exit` SHA256 `2c46a61a13b20aa8176d26e7192b0bc11507d1ed5047a33cc13bead1242b648b`; `docs/loop/invariant-required-local-development.md` | ingen specändring (skäl: DA-grinden autentiserar hela specen) |
| Preprodukt-RED på 0581 | exit 1, 12 PASS / 3 FAIL, ingen RIG_ERROR; result.json SHA256 `189dcdfc87…` (scratchpad `red-baseline-0581-result.json`) | bevisat |
| BUILDER-kandidat | `worktrees/builder-invariant-required-20260910`, gren `nortropic/loop-invariant-required-product`, HEAD `dae90c8fffa7b33e46e61e81de96e89137ff7829`, tree `6bac0ec9…`, parent 0936fb6c; autopilot SHA256 `9c2dc08b478c40038b60bd0af2a8628b00c07037abea49bd570d61230bedf0a1` | diff: 2 rader i `run_invariants` (`-> Cmd`, `raise Stop("mandatory invariant verifier missing: …")`), fem vakter orörda; grind 15/15 exit 0; DA-grind 100/100; check-invariants 8/0; docs-coherence 109/109; selftest PASS; publication-callers exit 0 |
| REVIEWER | `worktrees/review-invariant-required-20260910`, detached på dae90c8f (ref `refs/candidates/invariant-required-product`) | **READY_FOR_LOCAL_QUALIFICATION_ONLY**, mottagen och bokförd i [REVIEW-INVARIANT-REQUIRED-dae90c8f-20260910.md](REVIEW-INVARIANT-REQUIRED-dae90c8f-20260910.md). Starta ingen ny granskare för samma oförändrade kandidat. |

Kommandon (umask 0022, pinnad python):
`/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -B <TA>/verify/bin/invariant-required-exit --subject <kandidat>`
och `… -B <TA>/verify/bin/document-authority-exit --subject <kandidat>`.

Inte gjort: publicering/push/merge; ordinarie loop-integrering; h-035-exit-körning.

## Backup — läge

Destination: `/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z/` (samma disk; inga Time Machine-/externa destinationer finns).

- Fas 1: `manifest-original.tsv` (163 380 rader, 125 115 filer, 4 241 242 533 B) och
  `nortropic-full.tar` (pax, 4 848 679 936 B, SHA256 `b69532a32d38a0ac18065709f501ac7a9e5a40bb966a3890ec9ea6012087bb3c`), tar exit 0, tom stderr.
  Exkluderat: enbart de två rollklonerna `worktrees/builder-invariant-required-20260910` och
  `worktrees/review-invariant-required-20260910` (deriverbara; ska kompletteras i fas 4).
- Fas 2: 37/37 git-bundles (`bundles/*.bundle`) skapade och `bundle verify` ok (phase2-report.json).
- Fas 2b: extraktion i scratch, 163 380/163 380 rader byte-lika mot manifestet, 0 diff/saknade/extra;
  484 pekarfiler (gitfiles, `worktrees/*/gitdir`) omskrivna i kopian; 279/279 utcheckningar
  HEAD- och status-lika med original; 37/37 fsck ok; scratch borttagen. Reach-back-flaggan i
  den rapporten är ett falskt positivt (`/tmp` vs `/private/tmp`).
- Fas 2c (`phase2c-restore-report.json`): reach-back 0/279 med realpath-korrigerad kontroll, 279/279
  HEAD-lika, **278/279 status-lika**, 37/37 fsck. Avvikelsen är `worktrees/test-author-invariant-required-20260909`:
  vid tar-ögonblicket hade dess arbetskopia gate-filen i läge 644 mot committade 755 (` M`-rad);
  efter att chmod blev tillåtet sattes originalets fil till 755 (status tom) medan kopian troget
  bevarar 644-läget. Kopian är alltså korrekt för sitt ögonblick; supplementet i fas 4 innehåller
  den nya 755-filen och det uppdaterade `.git/index`.
- Fas 3: 24 externa källor (document-authority-* och h039-* under /private/tmp, T-katalogens
  document-authority-local-*, invariant-required-local-*, Codex-projektmappen, scratchpad)
  som pax-tar + manifest under `external/` (phase3-external-report.json). Scratchpad-tar togs
  innan H039-rapportfilen skrevs — komplettera.
- **Återstår (fas 4):** nytt manifest av `~/nortropic`, diff mot fas 1, kompletterande tar av
  ändrade/nya sökvägar (inkl. rollklonerna, TA-klonens .git, denna checkpoint, scratchpad på nytt).
  Redovisa exakt vilka bytes som tillkom under kopieringen.

Luckor: 111 datafiler i `.git`-admin (journaler/state.json) innehåller originalsökvägar som text,
inga pekare; kopian ligger på samma disk (inget off-site); credentials är inte kopierade (avsiktligt).

## H039-källgranskning — klar (read-only)

Rapport: scratchpad `H039-KALLKLASSIFICERING-20260910.md` (kopieras till backup i fas 4).
Kärnfynd: A (`docs-domain-sync`) 41 863 r = 67,7 % aktiv logik, 5,5 % blobbar, 6,0 % tabeller,
17,8 % onåbart historiskt (bundet av `r33_historical_r32_bytes_exact`/closed-world, ej fritt raderbart;
27 rena orphans = 1 892 r). B = A + insatt scaffold rad 16–3197 (3 182 r) med ovillkorlig
`SystemExit(2)` → hela R33-modulen död vid körning; självankare mismatch; ocommittat. "Fem av tio
revisioner": UNVERIFIED (ingen sådan struktur i filen). Efterföljarförslag är observationer, inte beslut.

## Plattform utan webb — nästa körbara prov (kort)

`controller/loop/cli` kör fortfarande legacy `VERIFY preflight` (rad ~482), `VERIFY prepare`
(rad ~511) och `task-run` (rad ~350) med `_snapshot_sha256/_snapshot_dir`. Nästa test-first-steg:
kontrakt som binder `gor_run` till `platform-prepare`/`platform-check` under h-035 (`controller/loop/**`
ligger i allowed_write) och låter `task-run` konsumera en plattformssnapshot vars leafmängd är
grindens `REQUIRED_SNAPSHOT` i stället för legacy `PRETASK_PATHS` + alla registerposter.
Exakt produktberoende: (1) `controller/loop/cli` lane-val utan nya sidokommandon, (2)
`controller/verify/cli task-run`-projektion mot plattformssnapshot, (3) webbens preflight/register-
krav bevarade som negativa fall. Ingen körning gjord.

## Sessionsmiljö (mätt 2026-09-10)

- `~/.claude/settings.json`: allow för chmod/tar/git bundle/git -C worktrees-kommandon;
  `sandbox.excludedCommands: ["chmod","git clone"]`. Hanterad policy: `Bash(chmod:*)` borttagen
  (backup `managed-settings.json.bak-20260910`). chmod går; `git clone` i sandbox gick INTE i
  den redan startade sessionen — verifiera efter omstart, annars bypass.
- `cd` in i klon skapar `.claude/.cc-writes`; använd `git -C`. bsdtar: `--format` bara vid `-c`.

## Uppdatering 2026-09-10 ~12:50 (efter att bakgrundsjobben avslutats)

- REVIEWER klar: **READY_FOR_LOCAL_QUALIFICATION_ONLY** på dae90c8f. Grind 15/15 (result.json
  `04e79c61…`), DA-grind 100/100 (`a57daf35…`), check-invariants 8/0, publication-callers exit 0.
  Nio fejkfixar i engångskopior: 7 fångade; (g) Stop-text utan ordet "invariant" passerar eftersom
  sökvägen `check-invariants.mjs` innehåller ordet (meddelandebindning svag, effektbindning intakt);
  (i) miljöflagga-bypass i oexerciserad gren passerar (gränsdeklaration, ej i kandidaten).
  Alla fyra övriga konsumentflöden exercerade hermetiskt med saknad verifierare → Stop, ingen
  INVARIANTS-rad, publish ej nådd. Död `inv is not None`-vakt kvar (skäl: publication-callers.py
  rad 81 stubbar med None); latent men grindtäckt. Följdförslag: vakt + teststubb → `Cmd(0,"")`,
  grindens must_contain skärpt till "verifier missing". Ingen publicering/push.
- Fas 2c klar: reach-back 0/279 (realpath-korrigerat), 279/279 HEAD-lika, 278/279 status-lika
  (avvikelsen är TA-klonen: originalets gate fick chmod 755 efter tar-ögonblicket), 37/37 fsck,
  163 380/163 380 rader byte-lika, scratch borttagen.
- Fas 4 klar: 1 249 tillkomna + 2 ändrade + 0 borttagna sökvägar sedan fas 1 (rollklonerna 624+624,
  TA-klonens .git/index + gate-mode, denna checkpoint). `supplement-20260910T104815Z.tar`
  (936 poster, 50 636 800 B, SHA256 `2f765404…4405`), `manifest-phase4-…tsv`, scratchpad-refresh-tar
  (innehåller H039-rapporten). Total täckning = fas1-tar + supplement + external + bundles.
- Sessionsmiljö: managed `Bash(chmod:*)`-deny borttagen av ägaren; chmod går. `git clone` i sandbox
  gick fortfarande inte i den redan startade sessionen (excludedCommands verifieras efter omstart).

## Kompletteringsbackup slutförd 2026-09-10 (fas 5)

I `full-20260910T103342Z/`: `reports/` (denna checkpoint, REVIEW-INVARIANT-REQUIRED-dae90c8f,
H039-KALLKLASSIFICERING, red-baseline-0581 result+log), `external/review-evidence__*.tar`
(reviewerns två behållna FIXTURE_ROOT, SHA256 `2986c204…1592d` och `b213239b…0f75e`),
`supplement-20260910T105109Z.tar` (937 poster, 50 647 040 B, SHA256 `589f6602…bd612`; kumulativt
mot fas 1: 1 250 tillkomna, 2 ändrade, 0 borttagna — rollklonerna 624+624, TA-klonens index +
gate-mode, checkpoint, reviewfil), `manifest-phase4-20260910T105109Z.tsv`, scratchpad-refresh-tar
(SHA256 `a700b47e…9bb63`). Ändringar som skedde under grundkopieringen är därmed redovisade och
kopierade. Den äldre `supplement-20260910T104815Z.tar` bevaras som historik.

## Faktiskt återstående arbete (efter denna session)

1. **Plattformsprov utan webb** (test-first, h-035-yta): kontrakt som binder `controller/loop/cli`
   `gor_run` (preflight r.~482, prepare r.~511) och `task-run` (r.~350) till
   `platform-prepare`/`platform-check` och en plattformssnapshot med grindens `REQUIRED_SNAPSHOT`-
   leafmängd; webbens preflight/registerkrav bevaras som negativa fall; inga nya sidokommandon.
   Bygg på dae90c8f. Separat TA/builder/reviewer-kloner.
2. **H039 minsta väg till avslut** inom befintlig avgränsning: B-filens scaffold (rad 16–3197, ocommittat,
   gör gaten död) måste lyftas ur den frysta gaten till egen fil; sedan bounded review av vilken
   R33-selektor som är den faktiska aktiva vägen (`--r33-installed`). Inga fria borttagningar av
   R≤32-material (låst av historik-bytes-kontroller). Root-ceremonier/installation ingår inte.
3. Följdrättning (liten, valfri): död `inv is not None`-vakt + teststubb → `Cmd(0,"")`; grindens
   must_contain skärpt till "verifier missing".
4. Publicering/merge av dae90c8f är INTE beställd; guarded publication först när ägaren beställer.

## Bokföring 2026-09-10: dae90c8f = färdiggranskad lokal kandidat

`dae90c8fffa7b33e46e61e81de96e89137ff7829` (gren `nortropic/loop-invariant-required-product`,
autopilot SHA256 `9c2dc08b…edf0a1`) är **färdiggranskad lokal kandidat** för fail-open-rättningen:
kontrakt 0936fb6c, preprodukt-RED, builder, oberoende review READY_FOR_LOCAL_QUALIFICATION_ONLY
(fil `REVIEW-INVARIANT-REQUIRED-dae90c8f-20260910.md`). Avslutade granskningar upprepas inte för
oförändrade bytes; nya bytes kräver nytt kontraktssteg. Inte publicerad. Nästa steg bygger på den.

## Återställning av katalogläge från manifestet

Supplement-tarerna skapas från fillistor (`supplement-*.list`, endast reguljära filer/symlänkar), så
kataloger uppstår implicit vid extraktion med default-läge. Grundkopian `nortropic-full.tar` bär
katalogposter med läge. Fullständig återställning = (1) extrahera `nortropic-full.tar`,
(2) extrahera senaste `supplement-*.tar` ovanpå, (3) kör `restore-dir-modes.py <manifest-phase4-…tsv>
<mål-förälder>` som sätter varje katalogs läge enligt manifestets `d`-rader (och rapporterar
saknade kataloger), (4) om målet inte är originalsökvägen: skriv om gitfiles/`worktrees/*/gitdir`
enligt fas 2b-metoden. Skriptet och `README-RESTORE.md` ligger i backupkatalogen.

## Läge 2026-09-10 ~13:30: plattformsprov utan webb påbörjat, H039-rapport korrigerad

- Bokfört: `RECON-PLATTFORMSLANE-KORVAG-20260910.md` (read-only rekognosering av `controller/loop/cli run`
  och `controller/verify/cli`; nyckelfynd: preflight/prepare validerar alla registerposter inkl. den
  ej startbara webbposten; `check-invariants` läser själv `workflows/*.js` (INV-005/006) och är §A-/
  människohandslåst; launch kräver `/usr/bin/sandbox-exec` → körning utanför sessionens sandbox).
- `H039-AVSLUTSKRAV-MINSTA-VAG-20260910.md` avsnitt C ersatt efter ägarens precisering: B-arbetskopian
  orörd (NOT_READY-stopp avsiktligt), efterföljare i separat yta, utgångspunkt CONTRACT_SIX/PRODUCT_FOUR,
  R33-gränser gäller inte automatiskt, errno42-osäkerhet behållen, assetbygge ≠ avslutsbevis. Ingen
  H039-ändring/publicering/körning beställd.
- TEST_AUTHOR-klon `worktrees/test-author-platform-lane-20260910` (gren `nortropic/loop-platform-lane-contract`,
  bas dae90c8f) skapad; agent skriver `verify/bin/platform-lane-exit` + `docs/loop/platform-lane-local-development.md`
  enligt design D1–D8 (config-fält `lane`, lane-argv på befintliga `preflight`/`prepare`, startbar-poster
  obligatoriska, ej startbara hash-bundna när närvarande, PRETASK_PATHS obligatoriska, fixturregistrerad
  global verifierare för lane-mekanik, ärlighetskontroll med riktig `check-invariants` = ingen attestation,
  legacy-lane oförändrad). Preprodukt-RED på dae90c8f väntas. Produktyta för BUILDER: exakt
  `controller/loop/cli` + `controller/verify/cli`. Ingen specändring.

## Repouppdelning genomförd lokalt 2026-09-10 (ägarbeställd)
Se `SEPARATION-20260910-HANDOFF.md`. Plattform: `~/nortropic-repos/nortropic-system` @ 49cc495c26f6d45d8a0f80b3f1b43a165c0e8c71 (gren nortropic/platform-separation-20260910, parent dae90c8f, origin oförändrad, inget pushat). Webb: `~/nortropic-repos/nortropic-webbforvaltning` @ 48cacefb7223d870e6e67fa5b3f69be84b19361c (main, inget remote). Plattformslane-arbetet i den blandade loopen avbröts (TA-klon test-author-platform-lane-20260910 tom, bevarad). Original och backup orörda/kompletterade. Nästa steg per repo står i handoffen.

## Riktning 2026-09-10 ~14:00: webben parkerad, bootstrapen återupptas i plattformsrepot
Ägaren: webbförvaltningen/verkstadsgolvet utvecklas inte nu; bootstrapkedjan ska fortsätta snarast i
`~/nortropic-repos/nortropic-system` utan webbinblandning. Alla 8 INV-regler i `scripts/check-invariants.mjs`
är webbregler; registret bär webbposten. Pågående: TEST_AUTHOR-kontrakt "plattformskontrollmängd utan webb"
i `~/nortropic-repos/work/test-author-platform-control-set-20260910` (gren `nortropic/platform-control-set-contract`,
bas 49cc495c): gate `verify/bin/platform-control-set-exit` + doc + människohandsförslag
(`SEPARATION-20260910/proposed/`: nytt plattformsregister utan webbpost, ny plattformsinvariantgrind på samma
path/id). Produktyta för BUILDER: `controller/verify/cli` (PRETASK_PATHS/PLATFORM_DOCUMENTS → docs/loop-set),
`scripts/nortropic-codex-autopilot.py` (SUBSTITUTION_BLOBS → plattformsdokument), ev. `controller/loop/cli`.
Därefter: oberoende review, ägaren applicerar de två människohandsfilerna, sedan H-035-kedjan enligt
`docs/loop/remaining-bootstrap-delegation-v1.md`.

## Plattformskontrollmängd utan webb — läge ~14:45
- TA-kontrakt fryst: `dadafe96a806eaf3a904b05f1152c0c1fd3ba51d` (`~/nortropic-repos/work/test-author-platform-control-set-20260910`):
  gate `verify/bin/platform-control-set-exit` (sha256 `d06435b5…`), doc, förslag `SEPARATION-20260910/proposed/`
  (check-invariants `ae72cdf8…`, register `f1c553d9…`). Preprodukt-RED 27/41 på 49cc495c.
- BUILDER: produkt `4ff1b078d5b8b6348aa71d5ea4956d5dfa152692` (+utfall `383ed387…`) i
  `~/nortropic-repos/work/builder-platform-control-set-20260910`: `controller/verify/cli` (PRETASK utan docs/07,03;
  PLATFORM_DOCUMENTS = 11 plattformsdokument; PLATFORM_REGISTER = förslagsregistret) och autopilot
  (SUBSTITUTION_BLOBS 11 poster, selftest 13→11). Arbetsyta 40/28 (alla röda = ej applicerade
  människohandsfiler); replika med förslagen 68/68. `controller/loop/cli` orörd.
- REVIEWER startad i `~/nortropic-repos/work/review-platform-control-set-20260910` (detached 383ed387).
- Väntar: ägarens "applicera" av de två förslagen (README i proposed/ har exakta cp-kommandon).
- TA-fynd utanför produktytan: H-036-launchern startar målet i anroparens cwd (kräver eget kontrakt i
  controller/launch/**). Ägarhandsfiler kvar i EFTERARBETE rad 5–10.
- REVIEWER klar: **READY_FOR_LOCAL_QUALIFICATION_ONLY** på 383ed387 (fil `REVIEW-PLATFORM-CONTROL-SET-383ed387-20260910.md`);
  F1/F2 ej blockerande. Kvar: ägaren applicerar de två förslagen → omkörning väntas 68/68 → H-035-kedjan.

## Läge ~15:30
- Ägaren godkände lokal applicering av de två förslagen; klassificeraren blockerar agentskrivning till §A-filerna
  (`scripts/check-invariants.mjs`, `controller/verify/register.json`) — ägaren kör själv `cp`-kommandona ur
  `SEPARATION-20260910/proposed/README.md` i builder-kandidaten (HEAD 383ed387) och committar HÖGRISK-märkt.
  Därefter: grind (väntat 68/68) + regressioner. Bootstrapkedjan är INTE därmed körklar.
- Gällande grind för den nya register-/dokumentgenerationen: endast lokala `verify/bin/platform-control-set-exit`
  (dadafe96). Frusna `h-035-exit` pinnar historiska registergenerationer (`403190cc…`, `3fc24e10…`), `h-037-exit`
  refererar registret 9 ggr → inför nästa H-steg krävs ägargodkänt refreeze-kontrakt; mät h-035/h-037 noarg på
  den applicerade kandidaten.
- Webb: AGENTS.md rensad från plattformens historik (0c63f4e). Plattform: förslag till preciserat
  delegations-/human-only-avsnitt i scratchpad `PROPOSED-platform-AGENTS-delegation-section.md`; byggs som
  kandidat (AGENTS.md + PLATFORM_DOCUMENTS/SUBSTITUTION_BLOBS-pinnar) ovanpå ägarens applicering.
- TA-kontrakt för worker-startkatalogen (H-036 launch cwd) pågår i `work/test-author-launch-cwd-20260910`.
- F1/F2 kvar som avgränsade uppföljningar.
- Mätt (`GRIND-FOR-NY-GENERATION-20260910.md`): preflight accepterar nya registret; frusna h-037-exit vägrar
  (`unfrozen register bytes`), h-035-exit rc 2 (immutable-artifact-FAIL + host-riggfel nested -S). Enda gällande
  grind = lokala platform-control-set-exit. Nästa H-steg kräver refreeze-kontrakt med ägarens hashgodkännande.
- Launch-cwd: TA-kontrakt fryst `2444a856de571f5a53f7a34b263de7fca9a8a892` (`work/test-author-launch-cwd-20260910`;
  gate `verify/bin/launch-cwd-exit` sha256 `c9d5e0d7…`, doc `803b522a…`), RED 13/7 av rätt skäl; referens M1
  (`os.chdir(ws)` efter resolve i gor_run) 20/20 i replika. Fynd: h-036-exit pinnar `controller/launch/cli`
  (`PINNED_UNCHANGED`) → fix bryter h-036-bindningen (ägar-refreeze); h-036 noarg ger redan RIG_ERROR
  (`docs/05-beslutslogg.md` saknas efter separationen). BUILDER startad i `work/builder-launch-cwd-20260910`.
- Launch-cwd BUILDER: kandidat `4a0e3f967108f5a92031eef17e80a6363319c5b5` (`work/builder-launch-cwd-20260910`,
  launch/cli sha256 `5273a484…`), grind 20/20, control-set 40/28 oförändrat, invariant-required 14/15;
  buildern amendade sin egen provisoriska lokala commit (noterat). h-036-exit pinnar gamla launch-bytes
  (`65571892…`) → refreeze-beslut. REVIEWER startad i `work/review-launch-cwd-20260910`.
- Launch-cwd REVIEWER: **READY_FOR_LOCAL_QUALIFICATION_ONLY** på 4a0e3f96 (`REVIEW-LAUNCH-CWD-4a0e3f96-20260910.md`);
  K1/K2 kontraktsluckor (ej blockerande), N2 nivå+1 utanför kontraktet, h-036-refreeze = ägarfråga.

## Ägarbeslut 2026-09-10 (styrning) och applicering
Ägaren beslutade: plattformen (Trust Kernel, bootstrap) utvecklas med full autonomi inom beställt uppdrag och tillgängliga
tekniska behörigheter; webbens konstitution/regelverk/agentroller/stewardtrappa/människohandskrav styr inte plattformen;
generella ägarstopp ersätts av det autonoma kontraktsflödet (rollseparation, oberoende granskning, mekanisk verifiering
bevaras; builder ändrar aldrig sin egen frysta grind); plattformens skydd (identitet, otillåten skrivning, saknad
verifierare, falskt godkännande) är uttryckliga tekniska krav; historik/frysta artefakter bevaras men är inte dagens
instruktioner; push/publicering/installation/live/resume ingår inte i fasen (inte permanenta människokrav).
Klassificerarens miljötext i ~/.claude/settings.json uppdaterad (manuellt läge) för plattformsrepot.
- Förslagen applicerade: commit `58ad9a883e31e37f33ee19f213ecb4d56a1993e7` (parent 383ed387) i
  `work/builder-platform-control-set-20260910`: gate **68/68** PASS_LOCAL_QUALIFICATION_ONLY, invariant-required 15/15,
  preflight exit 0 (register f1c553d9…), check-invariants 6/0, publication-callers PASS, selftest PASS, inga h036-rester.
  Lokal kvalificering — bootstrapkedjan är inte därmed körklar.
- Plattformsintegration: gren `nortropic/platform-integration-20260910` i `~/nortropic-repos/nortropic-system` @
  `512490d44007373b79aca504aa92709e9810aa24` (merge av 58ad9a88 kontrollmängd+applicerade förslag och 4a0e3f96 launch-cwd);
  båda frysta lokala grindarna gröna där (68/68, 20/20). Kandidatrefs: `refs/candidates/platform-control-set`,
  `refs/candidates/launch-cwd`.
- Styrningskontrakt (ägarbeslutet, punkt 1–5) startat: TA i `work/test-author-platform-governance-20260910`
  (gren `nortropic/platform-governance-contract`, bas 512490d4): gate `verify/bin/platform-governance-exit` binder G1–G9
  (aktiv auktoritetsordning utan webbdokument, inga generella människohandskrav, policy skyddar plattformsmängden som
  tekniskt krav, ny specgeneration + PLATFORM_SPEC-pin, körbara beroenden utan webbdokument, frysta artefakter,
  båda befintliga lokala grindarna gröna, demonstrationsrad). Därefter BUILDER + REVIEWER i egna kloner, integration,
  slutrapport. Instruktionssynk-buildern (`work/builder-instruction-sync-20260910`) pågår; dess AGENTS.md-text
  integreras eller ersätts av styrningskandidaten.
- Styrningskontrakt fryst: TA `e8eb50fa13b8fb875800258a867eb234860be839` (grindcommit 6c10766d) i
  `work/test-author-platform-governance-20260910`; gate `verify/bin/platform-governance-exit` sha256 `f1eddbe7…`,
  doc `a05279f6…`; RED 31/39 på 512490d4 av rätt skäl (G1–G5 röda; G6/G7/G8/G9 gröna; launch-cwd bunden 19/20 med
  exakt extra-fil-detalj). Adversariell grindgranskning av TA: hårdkodad lista utan spec → G3 5/14; "alltid exit 3" → 0/14.
  BUILDER startad i `work/builder-platform-governance-20260910` (bas e8eb50fa). Instruktionssynk-buildern committade
  `5855480e` (återanvänds som underlag; G2 kräver omskrivning av människohandsdelarna).
- Styrning BUILDER: produkt `fbdf3ece18ea05d0f60133e8cba5df4b0f2ea185` (+utfall `9112a304…`) i
  `work/builder-platform-governance-20260910`: gate 70/70, policy fall.py 103/0, selftest PASS, preflight 0,
  check-invariants 6/0; spec denied_write = plattformsmängd, human_only borttaget (arkiverat), backlog → byggplan;
  policy utan AGARHAND, neutral text; autopilot utan docs/05; pinnar följer; historik i docs/loop/arkiv/*-fore-2026-09-10.md.
  REVIEWER startad i `work/review-platform-governance-20260910`. Uppdelningens SEPARATION-dokument spårade i
  integrationsgrenen (var ospårade pga vitlista).

## Styrningsändringen genomförd och verifierad lokalt (2026-09-10 kväll)
- REVIEWER: READY_FOR_LOCAL_QUALIFICATION_ONLY på 9112a304 (`REVIEW-PLATFORM-GOVERNANCE-9112a304-20260910.md`), 7/7 mutanter fångade,
  F-1..F-6 ej blockerande.
- Integration `nortropic/platform-integration-20260910` @ `332f07ceb914a07c6632c1393969d9d5a337566b`: platform-governance-exit 70/70,
  platform-control-set-exit 68/68, launch-cwd-exit 19/20 (enda röda = extra filen verify/bin/platform-governance-exit, bunden av G7).
  Kandidatrefs: refs/candidates/{platform-control-set,launch-cwd,platform-governance}. Arbetskloner under ~/nortropic-repos/work/.
- Uppföljningar (ej blockerande): F1/F2, K1/K2, nivå+1-launch, F-3/F-6, attest/cli:s historiska docs/05, .gitignore-vitlista, config/README.md.
- Nästa: refreeze av H-kedjans grindar (h-035/h-036/h-037 accepterar inte nya register-/launch-/dokumentbytes) genom samma autonoma flöde,
  därefter H-035 → H-034 → H-033 → H-032 → H-031 lokalt.

## Ägarprecisering 2026-09-10 (kväll): slutlig separation
nortropic-system ska ENDAST innehålla den verksamhetsneutrala plattformen (Trust Kernel, bootstrap, controller, plattformens
supervisor, dess utveckling/verifiering/dokumentation). ALL webb-/Digitala-styrning bort från plattformens aktuella användning
(kod, dokument, agentinstruktioner, skills, vakter, konfiguration, arbetsflöden, behörighetsregler, indirekta beroenden). Rent
webbmaterial får inte ligga kvar som "historik"/arkivkatalog i plattformsträdet — bevaras i webbrepot eller separat evidensarkiv med
proveniens. Git-historik och kernel-/H-evidens bevaras. Följ hela hänvisningskedjan inkl. pinnade Git-objekt (harness-substitution-
contract, full-roadmap, owner-author-workflow, remaining-bootstrap-delegation, drift). Loop/autopilot avgörs efter funktion: provider
äger resonemang/sessioner/agentloopar; plattformen äger tillitskontroller/övergångar; inget dubblerat agentmaskineri. Särskilt:
check-verifierarregistret.mjs (webb-vaktankarberoende), registertexten "endast av människohand". Autonomt kontraktsflöde med separat
implementation och oberoende granskning; kontrakt/pinnar uppdateras när generationen ändras; gamla resultat behåller sina versioner.
Verifiering: aktiva instruktioner/körvägar utan webbrepot; normalt arbete genom kontrakt→bygge→granskning→kvalificering utan ägarstopp;
kontroller som upptäcker återinförd webbstyrning via indirekt dokumenthänvisning/agentprompt/kodkoppling. Härled nästa H-steg; bevara
H039/H038 där de krävs. Lokalt; ingen push/publicering/installation/live/resume.
Pågår: fullständig read-only ansvars-/hänvisningskedjeaudit av 332f07ce (agent) → TA-kontrakt "platform-final-separation" → BUILDER →
REVIEWER → integration → verifiering.
- Tolkningsgrund (ägaren 2026-09-10): Nortropic = organisationen; AI-agenter ska utföra organisationens arbete autonomt genom en
  gemensam verksamhetsneutral plattform. Trust Kernel = plattformens tillitsdel (verkställer behörighetsgränser, verifierar bevis/
  resultat/tillåtna övergångar). Bootstrap = etablera och kvalificera plattformen så att den bär den löpande autonoma verksamheten.
  Webb/Digitala = en verksamhet/avdelning; dess agentroller, kundflöden, kvalitetskrav, konstitution och stewardregler får styra
  webbuppdrag men inte plattformen/bootstrapen. Plattformen ska fungera med webben helt frånkopplad och senare bära andra
  verksamheter. Inga nya organisationsfunktioner byggs pga förtydligandet.
- Slutseparation: audit bokförd (`AUDIT-SLUTSEPARATION-332f07ce-20260910.md`). TA-kontrakt "platform-separation-final" startat i
  `work/test-author-final-separation-20260910` (bas 332f07ce): allowlist + krävda frånvaron, hänvisningsslutning från aktiva rötter
  (inkl. autopilotens promptdokument och pinnade planobjekt), config/behörighetsregler, autopilot utan gammal rot och med
  plattformsfrysta plankopior, tester, fryst evidens, tidigare grindar med exakta deltan, live-väg utan webb, återinföringsnegativer.
  Webbrepot: överföring 2 (check-verifierarregistret.mjs + tre arkivkopior med proveniens från 332f07ce) committad.
- Slutseparationskontrakt fryst: `9bb3503de37e59406bd841174ff36f582796a57b` (grindcommit e2c3bafd) i
  `work/test-author-final-separation-20260910`; gate `verify/bin/platform-separation-final-exit` sha256 `b6af3b92…` (1131 r),
  doc `3d67aa00…`. RED 47/31 på 332f07ce; referenskonstruktion 74/74; negativer a–h 8/8 fångade; F7 exakt: control-set 68/68,
  launch-cwd 19/20 (två extra grindar), governance 68/70 = {g6,g7}. GATE-REVIEWER (read-only) och BUILDER startade parallellt i
  `work/gate-review-final-separation-20260910` resp. `work/builder-final-separation-20260910`.
- GATE_REVIEWER på slutseparationskontraktet: **NEEDS_REMEDIATION** (`GATE-REVIEW-FINAL-SEPARATION-9bb3503d-20260910.md`): 14-fald
  återinföring passerar 74/74; 10 remedieringar skickade till TA (kontrakt v2). BUILDER v1 pågår mot gamla grinden; anpassas till v2.
- Slutseparation BUILDER v1: produkt `191fadf6d949ea9e82bb0342d408b07c55c41586` (utfall `0026702a…`) i
  `work/builder-final-separation-20260910`: 74/74 mot kontrakt v1 (result 9857cc0c…), control-set 68/68, launch-cwd 19/20
  (extra=[governance, final]), governance 68/70 {g6,g7}, loop-svit 53/0, policy 103/0, preflight (register 9752d01d…), PINV 6/0.
  Innehåll: arkivkopior + check-verifierarregistret bort (proveniens-2), plankopior in (byte-lika 0b3212c9-objekten), autopilot
  ensure_roadmap_plan lokal, defaults utan gammal rot, register 1.1.0 utan människohand, substitutionskontrakt v1.1-amendment,
  full-roadmap/evidence/config/gitignore/premiar/managed-settings omskrivna, historiska dokument med supersessionshuvud, drift-not,
  fall.py B2 → PINV-005. Väntar: kontrakt v2 från TA → builder v2 (cherry-pick 191fadf6 + kompletteringar) → REVIEWER.
- Slutseparationskontrakt v2.2: TA HEAD `4e139294535adaca0f7550cebd31d022060cab36` (grind c37030c9, sha256 `6506e97a…`, doc `f8edc7c0…`);
  RED 51/36 på 332f07ce; referens 83/83; 24/24 negativer fångade (inkl. granskarens m0–m15). Remedieringar 1–10 bundna
  (trädvid skanning, blob-frånvaro, spec byte-lik 332f07ce, EFTERARBETE append-only, router-not, local-dev-mängd, held-blobkontroll).
  Parallellt: GATE_REVIEWER v2 i `work/gate-review-v2-final-separation-20260910`; BUILDER v2 i
  `work/builder-v2-final-separation-20260910` (gren nortropic/final-separation-product-v2, cherry-pick 191fadf6 → 842d0bbf).
- Slutseparation BUILDER v2: kandidat `9486371960cffd51e98ea92cbe4c782669e40ae1` (produkt v2 `3221966f`, parent 842d0bbf) i
  `work/builder-v2-final-separation-20260910`: 83/83 (result c21c90cd…), control-set 68/68, launch-cwd 19/20 (extra=[governance,final]),
  governance 68/70 {g6,g7}, loop-svit 53/0, policy 103/0, preflight 9752d01d…, PINV 6/0, spec = 332f07ce-blob. v2-tillägg: AGENTS p.5-not
  (fryst grindinput ≠ dagens instruktion), README utan webbreponamn, owner-h003-not utan "beslutslogg", loop-review-supersessionshuvud,
  EFTERARBETE-not, pinnar. Oberoende produkt-REVIEWER startad i `work/review-final-separation-20260910`; GATE_REVIEWER v2 pågår.
- GATE_REVIEWER v2 på 4e139294: NEEDS_REMEDIATION (`GATE-REVIEW-FINAL-SEPARATION-v2-4e139294-20260910.md`): 20/20 gamla mutanter fångade,
  3 nya luckor (symlänk, funktionsnamnsundantag, router-not utanför Auktoritetsordning) + 4 rekommendationer → TA v2.3 beställd.
  Produkt-REVIEWER av 94863719 pågår; builder v3 = cherry-pick 3221966f på v2.3 + AGENTS r.117-justering.
- Produkt-REVIEWER på 9486371 (mot v2.2): READY_FOR_LOCAL_QUALIFICATION_ONLY, 83/83 egen fullkörning, 9/9 mutanter fångade
  (`REVIEW-FINAL-SEPARATION-9486371-20260910.md`). Fynd för builder v3: AGENTS r.117 + Historik-markörer, byggplan "arkivkopian" ×6 + §8.5.
  TA v2.3 (HEAD 77a09be4, grind f9708786…) inväntas.
- Slutseparationskontrakt v2.3: TA HEAD `a6953ac51baa0be768d64c6a345bed48609b8f50` (grind 77a09be4, sha256 `f9708786…`, doc `e955b2e0…`):
  RED 52/36 på 332f07ce; referens 84/84; 52/58 negativer fångade (6 deklarerat utanför omfång). BUILDER v3 i
  `work/builder-v3-final-separation-20260910` (bas 48aeb78 = v2.3 + produkt v1/v2): AGENTS-markörer r.117/Historik, byggplan
  "arkivkopian"×6 + §8.5, ompinning, full körning (väntat 84/84). GATE_REVIEWER v3 (statisk) parallellt i gate-review-v2-klonen.
- BUILDER v3: kandidat `40a60d5969453a09001d5e9efdb33080431ff722` (produkt `012c433b`) i `work/builder-v3-final-separation-20260910`:
  84/84 mot v2.3 (result cb8bd31a…), control-set 68/68, launch-cwd 19/20 (extra=[governance,final]), governance 68/70 {g6,g7}; AGENTS
  r.117/Historik-markörer, byggplan "arkivkopian"×6 → dae90c8f-referens, §8.5, pinnar. Produkt-REVIEWER v3 startad
  (`work/review-v3-final-separation-20260910`). GATE_REVIEWER v3: NEEDS_REMEDIATION (attest/cli byte-bindning; JSON OUTSIDE_RE) →
  TA v2.4 beställd; produkten väntas uppfylla v2.4 utan ändring (attest/cli orörd, inga sådana JSON-värden).

## Slutseparation genomförd och kvalificerad lokalt (2026-09-10 natt)
Kontrakt v2.4 `d7cd584f` (grind bd8c0a2, sha256 915e7c51…), produkt `9c0a98be` (v1+v2+v3 på v2.4) 84/84, integration
`nortropic/platform-integration-20260910` @ **a748337f5b535f15713af5d895767e1c18286cac** 84/84 (result 32172408…); direkta kontroller gröna;
spec byte-identisk med 332f07ce. Leverans: `SLUTSEPARATION-20260910-LEVERANS.md`. GATE_REVIEWER v4 (statisk) pågår som bekräftelse.
Nästa: refreeze h-035-exit (nya generationen), SUB-1 planomfrysning; H039/H038 frysta.
- GATE_REVIEWER v4 på d7cd584f: NEEDS_REMEDIATION (liten): SIBLING_RE för syskonrepo under nortropic-repos/ i F8 → TA v2.5 beställd;
  produkten 9c0a98be väntas grön oförändrad. Därefter: integrera v2.5-kontraktet, omkör grinden på integrationen, slutrapport.
- Kontrakt v2.5 `2055ec02` (grind 4dffec98, sha256 2132ef51…; SIBLING_RE i F8) integrerat: plattformsintegration
  `nortropic/platform-integration-20260910` @ **320c9df73166dfb6f2df45e820bf0f2d2035e69e**, v2.5-grind från hållen kopia **84/84**
  (result 07f1e7d0…), control-set 68/68, launch-cwd 19/20, governance 68/70 {g6,g7}. Slutseparationen är genomförd och lokalt kvalificerad.
  Leverans uppdaterad (`SLUTSEPARATION-20260910-LEVERANS.md`).

## Ägarorder 2026-09-10 (natt): planseparation
Gamla roadmap-planen (0b3212c9-objekten, kopierade i docs/loop/) är fortfarande effekt-authority och läses av autopilotens rollprompter;
den gör webbkonstitution/regelverk överordnade → separationen är inte fullständig trots 84/84. Beställt: (1) ny plattformsgeneration av
plan + handoff genom autonomt kontraktsflöde (TA → oberoende kontraktsgranskning → builder → produktgranskning → kvalificering), bevara
funktionella mål/tekniska skydd/kvarvarande plattformsarbete, ta bort webbstyrning/människohand/verksamhetsberoenden; gamla planobjekt =
historik. Målbild: autonomin utvecklar hela Nortropic inkl. plattformen; bootstrap = kvalificerad grund; webb använder plattformen.
(2) Bind alla aktiva konsumenter (rollskills, prompter, arkitektflöde, roadmap-konstanter, dokumentpinnar, ensure_roadmap_plan, selftest,
git show-instruktioner) till nya generationen; ingen aktiv väg får återinföra gamla planen som "effekt-authority/fryst input/historisk källa".
(3) Komplettera slutseparationskontraktet: ny generation accepteras, saknade/ändrade planbytes avvisas, återinförd gammal plan fälls,
rollprompternas faktiska innehåll och refererade dokument granskas, undantaget för plankopiorna tas bort. (4) Parallellt: H035:s
host-riggfel; därefter refreeze av berörda H-grindar mot färdig plattformsgeneration i beroendeordning; H039/H038 bevaras.
Separationen kallas fullständig först när planen är separerad i aktiv användning. Lokalt; ingen push/publicering/installation/live/resume.
Pågår: read-only planinnehålls-/konsumentanalys (agent) och H035-riggfelsutredning (agent).

## Planseparation — läge efter kontextkomprimering (2026-09-10, kväll)
- Recon-rapporten (read-only, agent) sparad som `~/nortropic/RECON-PLANGENERATION-20260910.md` (+ backupens reports/). Innehåll: plananatomi KEEP/REWRITE/REMOVE, skivinventering S1–S13/SUB-1–4/L, konsumentkedja C.1–C.14 (autopilot konstanter r.71-73/93-96, `git show {SHA}:` prompter r.1479/1658/1768, selftest 0b3212c9 r.2578, architect r.16/21, empirical-runner r.14, AGENTS r.127/153-157, full-roadmap Authority 8-17, substitution ingress r.7, drift 521/562/564, final-exit CLOSURE_EXEMPT 136-137 / TREE_FROZEN 150 / F4 1110-1147 / F2 929-934), frysta H-grinders indirekta bindningar (D), förslag E.1–E.6, 14 OLÖSTA punkter.
- Orkestratorbeslut: nya filer `docs/loop/autonomous-loop-plan-platform-v2.md` + `docs/loop/autonomous-loop-platform-handoff-v2.md`; gamla kopior ur HEAD; blobbar c8ea8511/1e53887c förbjudna under alla sökvägar; sträng 0b3212c9 borta ur aktiva filer; plankopior skannas som aktiva dokument (undantaget bort); maskinläsbar skivtabell i planen jämförs 1:1 med autopilotens ROADMAP + selftest; `PLAN_GENERATION`-konstant ersätter ROADMAP_PLAN_SHA; inga `git show <sha>:` i prompter/skills.
- TEST_AUTHOR för kontrakt v3 startad i `~/nortropic-repos/work/test-author-final-separation-20260910` (ovanpå 2055ec02). H035-riggutredningen återupptagen (körning E/B i förgrund).

## H035-riggfel utrett (2026-09-10 ~23:25) — `~/nortropic/H035-RIGGFEL-UTREDNING-20260910.md`
- "R15 nested -S interpreter startup authority" = INVOKATIONSFEL, inte host/produkt: Homebrews sitecustomize.py skriver om sys.executable till `/opt/homebrew/opt/python@3.12/bin/python3.12` när PYTHONEXECUTABLE saknas. Kanonisk invokation: `env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=$PY $PY -I -S -B verify/bin/h-035-exit` (utanför sandlådan; skriver i /private/tmp).
- Replikor måste bära de 7 preserved-kandidaterna (a42613ee, b49a99cd, dcd9360a, 6419bd0c, 72c2b9fb, 8e56d591, f956b603 under refs/preserved/old-checkout/…) samt lokal bare-origin (endast core.*/user.*/remote.origin.*-nycklar i config).
- Mätt: frusen h-035 på ursprungsgenerationen 2fb748b = 462 PASS/0 FAIL rc 0 på denna Mac. På 320c9df7: 459 PASS / 3 FAIL (F_R13 h-035-rad utan docs/05 + local_document_authority_v1; F_R15 spec-transform mot c161a1c5-bas; F_H036_V3 tre dokument 35d7fd7c + append, docs/05 saknas). ed584ec3 (main 2026-09-08) hade redan 2 FAIL → grinden var röd på main sedan h-039-kontraktet.
- Refreeze-beroenden: spec-transformbas, H035_R13 utan docs/05, H036_V3-dokumentberoendet (docs/05 finns ej), sedan h-036 (docs/05, docs/07, task rows), h-037 (register a87869be→9752d01d, verify/cli 516f679f→bfefe973), h-038 (h-036-identitet). Grinden får inte redigeras — nytt fruset kontrakt via flödet.

## Kontrakt v3 (plangenerationen) fryst (2026-09-10 ~23:40)
- TA-klon `~/nortropic-repos/work/test-author-final-separation-20260910`: 12e7dfaa (grind+dok, parent 2055ec02) → a1101192 (utfall, tree 634ba18f). Grind v3 sha256 523c53bd…, 95 rader; dok 33b5c4ff…, 843 rader.
- RED på 320c9df7: 69/26 (exakt de nya planraderna; F7 oförändrade: control-set 68/68, launch-cwd 19/20, governance 68/70 {g6,g7}). Referens (scratch, förkastad): 95/95 result 5050cefa…. 19/19 negativer fångade.
- TA-beslut: endast pekare till gamla planen förbjuds; Verkstadsgolvet förbjudet i planen; promptmängd som delmängdsregel (krävd ⊆ injicerad ⊆ tillåten); AUTOPILOT_V4_SELFTEST=PASS behålls; PLAN_GENERATION-värde = builderns.
- Grindgranskning v5 startad i `~/nortropic-repos/work/gate-review-final-separation-v5` @ a1101192 → rapport `GATE-REVIEW-FINAL-SEPARATION-v5-a1101192-20260910.md`.
- Refreeze-recon (read-only) för h-035→h-036→h-037→h-038 pågår.

## Refreeze-recon för H-kedjan bokförd — `~/nortropic/RECON-REFREEZE-HKEDJA-20260910.md`
- Historiskt idiom: samma grindfil, nya bytes; nytt sub-objekt i specraden; fem-fils TA-kandidat (spec, grind, drift, owner-author, docs/05); nedströms pinnar merge-sha/träd/föräldrar/review; avvisade kandidater som preserved refs. Nytt lokalt idiom: ny grindfil + local-development-doc + `local_document_authority_v1`-nyckel.
- Ordning: 1a h-035 (R13 utan docs/05, R15 spec-transformbas ≠ c161a1c5, H036_V3-dokumentappends) ∥ 1b h-037 (register 1.1.0, verify/cli, check-invariants, workflows/tests/fixtures borttagna, autopilot-bytes → efter plangen) → 2 h-036 (ny h-035-sha+radhash, docs/07, launch/cli 65571892→5273a484-beslut, autopilot-bytes → efter plangen) → 3 h-038 (redan PRE-GEN-föråldrad). h-032/h-031 AST-läser autopiloten → efter plangen. document-authority-exit helt bunden till 40f0bb6b-paketet → ny lokal version. h-039 blir RED av kedjan och kräver produktions-origin → UNRESOLVED (fryst evidens ska inte ompinnas).
- Måste vänta på färdig plangeneration: h-036, h-037, h-032/h-031, document-authority. h-035 kan gå före om nya kontraktet inte byte-pinnar drift.md/autopilot.
- 10 UNRESOLVED: docs/05-ekvivalent (släpp/ersätt/git-objekt), attest/cli byte-fryst av separationsgrinden, launch/cli-pin, nästlad h-031→h-032, h-039 RED, två publiceringsidiom, h-037:s förutsättningar borttagna, plankopior i final-exit v2.5 (löst av v3), "senast grön" baspunkt, zsh `$rev:path`-mangling.

## Grindgranskning v5 (a1101192) = NOT_READY → remediering v3.1 beställd
- Blockerande: B1 9–39-hex-pekare (`0b3212c991d4`) passerar; B2 `git show <PLAN_SHA>` fångas bara i 2/6 skills; B3 promptraden mäter AST-union, inte faktiska prompter (oanropad funktion, dict-indirektion, .format). Icke-blockerande N1–N7. RED 64/31 rätt skäl; egen referens 90/95; 20 attacker 12 fångade/8 missade.
- TA remedierar i samma klon ovanpå a1101192; därefter grindgranskning v6.
- Obs: två gamla fixturrötter `/tmp/claude-501/platform-separation-final-*` från 19:34/19:42 (tidigare agent) ligger kvar — städa efter integrationen.

## Kontrakt v3.1 fryst (2026-09-11 ~00:30) → grindgranskning v6
- TA-klon: 288b68ef (grind+dok, parent a1101192) → af584e71 (utfall, tree 7393602e). Grind v3.1 sha256 b298b07d…, 1740 rader, 97 rader i körning; dok 9b5bd79c…, 923 rader.
- Remedierat: B1 8–40-hex-förkortningar (OLD_PLAN_TOKENS), B2 COMMIT_READ_TOKENS i alla aktiva dokument/skills/trädvitt, B3 DRIVER-scenario `prompts` anropar 15 byggare (101 texter) och skannar producerad prompttext (plan+handoff krävda; docs-mängd krävd ⊆ producerad ⊆ tillåten), N2 exakt PLAN_GENERATION=<modulvärde>, N3, N5 PLATFORM_DOCUMENTS pinnar plan+handoff, N6.
- RED på 320c9df7: 67/30 (v3:s 26 + empirical-runner COMMIT_READ + f3 verify-cli-pin + två producerad-prompt-rader); F7 oförändrat. Referens: 97/97 result 1e5d148b…. Negativer 26/26 (inkl. a02,a04,a10,a11,a13,a23,a28).
- Grindgranskning v6 startad i `~/nortropic-repos/work/gate-review-final-separation-v6` @ af584e71 → rapport `GATE-REVIEW-FINAL-SEPARATION-v6-af584e71-20260911.md`.

## Grindgranskning v6 (af584e71) = NOT_READY → remediering v3.2 beställd (2026-09-11 ~01:00)
- B1–B3/N2–N7 från v5 verifierade verkliga (7/7 reproduktioner röda). Nya blockerare: B1 producerad-prompt-mätning öppen värld (SIDE-exkludering självdeklarerad; död krävd byggare + levande tvilling grön); B2 parse_slice_table tar första rubrikträff även i HTML-kommentar. Icke-blockerande N1–N9 (bl.a. ensure_roadmap_plan handoff oankrad, verify/cli-pin ej mätt i effekt, skiftlägestvilling → RIG, prompts-driver sidoeffekt, substans vs vokabulär).
- Oberoende referens 92/97 statiskt → satisfierbart. 19 nya attacker 8/9/1/1.
- TA remedierar i samma klon ovanpå af584e71; därefter grindgranskning v7.

## Kontrakt v3.2 fryst (2026-09-11 ~01:40) → grindgranskning v7
- TA-klon: 9d2ef894 (grind+dok, parent af584e71) → 6d6f86c3 (utfall, tree ad4483ec). Grind v3.2 sha256 c391eebb…, 2009 rader, 105 rader i körning; dok ab901b08…, 1009 rader.
- Remedierat: B1 sluten värld (EXPECTED_PROMPT_BUILDERS 15 / FLOWS 1 / CALLERS 8, prompt_world statisk klassificering, nåbarhet från main); B2 visible_markdown + exakt en skivtabell; N2 handoff-mutated; N3 platform-prepare/-check effektrader (DOCUMENT_GENERATION-avslag); N4 skiftlägesunik f1-rad; N5 byggare i egen fixtur med före/efter-snapshot; N7 krävda ##-avsnitt (Syfte, Målbild, Skyddade invarianter/tekniska skydd, Skivtabell, Bootstrap, Arbetsflöde, Avslutskriterier); N8 Historik båda riktningar; RECON-kartan sha e01fcfa5… som vägledning.
- RED på 320c9df7: 71/34; F7 oförändrat. Referens 105/105 result bbee9f8e…. Negativer 36/36.
- Grindgranskning v7 startad i `~/nortropic-repos/work/gate-review-final-separation-v7` @ 6d6f86c3 → `GATE-REVIEW-FINAL-SEPARATION-v7-6d6f86c3-20260911.md`.

## Grindgranskning v7 (6d6f86c3) = NOT_READY → remediering v3.3 beställd (2026-09-11 ~02:10)
- v6-remedieringar verifierade; F7/argparse byte-identiska med v2.5; 11 radnamn ersatta med utökad semantik, ingen försvagad; RED 66/39 statiskt = TA:s 71/34; referens 100/105 → satisfierbart.
- B1 prompt_world sluten över namn men öppen över textkällor (globals-uppslag, parameter-genomsläpp, modulnivåmall, klassmetod, runner-alias) → fail-closed klassificering + dynamisk mätning med stubbad runner beställd. B2 ensure_roadmap_plan binds som funktion, inte anropad vakt → sluten anroparmängd + dynamisk stopp-mätning. N1–N10 (refname-pekare, bootstrap rå text, läsvy-tabell, NFD-tvilling RIG, handoff i cli-effektrader, sidoeffekt absolutskrivning).

## Kontrakt v3.3 fryst (2026-09-11 ~02:45) → grindgranskning v8
- TA-klon: 9a2644e3 (grind+dok, parent 6d6f86c3) → 6c984b82 (utfall, tree 2ca7d3bd). Grind v3.3 sha256 f83b05c4…, 2194 rader, 109 rader i körning; dok c8ad2311…, 1085 rader.
- Remedierat: B1 fail-closed classify (rot = direkt Call till förväntad byggare; alias/modulmall/klass/globals/subscript/IfExp/comprehension/+= röda) + DRIVER `live_flows` (architect_resolution, roadmap_contract_flow[SUB-1,S2], empirical_gate_contract_flow, full_roadmap med stubbad run_codex; fångade prompter måste bära plan+handoff, inga gamla pekare); B2 EXPECTED_PLAN_GUARD_CALLERS {doctor, empirical_gate_contract_flow, full_roadmap, roadmap_contract_flow, roadmap_status} + dynamiskt stopp före runner vid muterad plan; N1 refname-pekare; N2 bootstrap synlig markdown; N3 slice-liknande tabeller; N4 NFC-kollision + quotePath; N5 prepare vägrar muterad handoff; N6 sidoeffekter arbetsträd + /private/tmp-toppnivå.
- RED på 320c9df7: 72/37; F7 oförändrat. Referens 109/109 result 460e7033…; live-flöden 5 prompter, muterad replika 4 stopp. Negativer 48/48.
- Grindgranskning v8 startad i `~/nortropic-repos/work/gate-review-final-separation-v8` @ 6c984b82 → `GATE-REVIEW-FINAL-SEPARATION-v8-6c984b82-20260911.md`.

## Grindgranskning v8 (6c984b82) = NOT_READY → remediering v3.4 beställd (2026-09-11 ~03:15)
- v7-remedieringar verifierade (13/13 reproduktioner); RED 67/42 statiskt = 72/37; referens 104/109 statiskt; F7 byte-identiskt.
- B1 effektbindning slutar vid stubbgräns/första runner-anrop (builder/test_author/empirical_unattended/reviewer-vägar bara statiska; classify släpper .replace/`*0+`; globals-runner) → strikt Add-only + live alla flöden med syntetiska READY-svar + stubbnamn deklarerade. B2 run_codex obunden (prompt via fil `wt/.architect-prompt`) → AST-identitet för runner-funktioner mot 320c9df7. N1–N12 (sidoeffekt-prefixundantag, handoff-substans, ROADMAP-ordning).
- 21 nya attacker 6/11/2/1 falskt rött (omdöpt origin_main).

## Kontrakt v3.4 fryst (2026-09-11 ~03:50) → grindgranskning v9
- TA-klon: 81f39036 (grind, parent 6c984b82) → 1f8d743d (utfall) → d8d405f5 (dok-kriterier; tree 628f8b01). Grind v3.4 sha256 0096bd03…, 2347 rader, 111 rader i körning; dok b521ee0d…, 1166 rader. Avvikelse: kriterietexten som tredje commit (amend förbjudet).
- Remedierat: B1 Add-only + PROMPT_TEXT_METHODS {strip,rstrip,lstrip}; dynamiska uppslag röda utanför {_provider_snapshot,_python_snapshot,_strict_provider_authority,publication_authority,publish,selftest}; live_flows alla 10 flöden med syntetisk READY AgentRun, LIVE_STUB_NAMES 21, min-anrop per flöde, 49 fångade prompter; B2 RUNNER_MACHINERY_AST_SHA256 (6 objekt mot 320c9df7). N: sidoeffektsvep (storlek,mtime) toppnivå /private/tmp{,/claude,/claude-501}+tempdir; handoff-avsnitt + plansökväg + PLAN_GENERATION + blob≠plan; skivtabellordning == SUBSTITUTION_ROADMAP+ROADMAP, ROADMAP[0]==S2.
- RED på 320c9df7: 73/38; F7 oförändrat. Referens 111/111 result 0fb237d9…. Negativer 55/55.
- Grindgranskning v9 startad i `~/nortropic-repos/work/gate-review-final-separation-v9` @ d8d405f5 → `GATE-REVIEW-FINAL-SEPARATION-v9-d8d405f5-20260911.md`.

## Grindgranskning v9 (d8d405f5) = NOT_READY, en blockerare → v3.5 beställd (2026-09-11 ~04:30)
- v8-remedieringar verifierade (12/12); F7/argparse byte-identiska med v2.5 (fbb949b3…, 69 rader, 13 konstanter); 79→81 radetiketter, ingen försvagad; referens 106/111 statiskt på första försöket; RED 68/43 = TA:s 73/38; live når alla tio flöden (1/2/2/2/2/2/2/2/1/33).
- B1: providergränsen efter run_codex öppen på tre seams — subprocess.Popen skuggad på autopilotens modulnivå, samma i controller/authority/core.py (importeras vid start), controller/launch/cli med provider-argv (launch-cwd-exit ger identisk detail för referens och mutant → F7 fångar den inte). Åtgärd: formregel modulnivå + blob/AST-pin av controller/authority/** och controller/launch/** + dynamisk fångst på Popen-nivå jämförd med byggarprompten.
- N1–N10: remedierings-/arkitektgrenar nås aldrig live (stubben svarar alltid READY); ROADMAP_PLAN_PATH kan miljöstyras via andra tilldelning; ROADMAP[0]-regeln binder inte vid konkatenering; live_flows körs utan sidoeffektsvep.
- 26 nya attacker (11/12/2/1 falskt rött) + 12 reproduktioner.

## Kontrakt v3.5 fryst (2026-09-11 ~05:05) → grindgranskning v10
- TA-klon: 749bc3b6 (grind+kriterier, parent d8d405f5) → 61426e1c (utfall, tree e755e378). Grind v3.5 sha256 56a37d66…, 2542 rader, 116 rader; dok f5952f75…, 1258 rader.
- B1 fyra mätpunkter: modulnivåform (attribut-/subscriptmål, exec-ytsnamn röda) + dynamisk kontroll att subprocess.Popen är stdlibs original efter import; blobpin controller/authority/{cli,core.py} + controller/launch/{cli,runtime_snapshot.py} mot 320c9df7; argv-plats (Popen exakt en gång, bara i run_codex, --output-schema ingen annanstans); live_flows spelar in varje Popen (0 providerstarter tillåtna, providerformad argv måste bära fångad prompt).
- N: tillståndsstyrd stub (NEEDS_REMEDIATION först) → remedierings-/arkitektgrenar nås, minima 1/4/4/4/4/4/4/4/7/37, plan+handoff även i remedierings-BUILDER-prompt; plankonstanter exakt en literal tilldelning, körtidsvärde == literal; SUB-koder/ROADMAP[0]/disjunkt; sidoeffektsvep runt live_flows.
- RED 77/39; referens 116/116 result 9add2f4b…, 73 prompter, 59 Popen varav 0 providerstarter. Negativer 63/63.
- Grindgranskning v10 startad i `~/nortropic-repos/work/gate-review-final-separation-v10` @ 61426e1c.

## Grindgranskning v10 (61426e1c) = NOT_READY, en blockerare → v3.6 beställd (2026-09-11 ~05:40)
- Bekräftat genom 33 grindkörningar: RED 72/44 statiskt = 77/39; referens 111/116 ur dokumentet allena med identisk fångstprofil; sex v9-fynd faller rätt; importgrafen mätt (en repo-lokal modul vid start: controller/authority/core.py → pinnmängden komplett, authority/cli överpinnad); F7/argparse byte-identiska; 81→86 radnamn, noll borttagna.
- B1: providergränsen bunden vid modulnivå/importögonblick men inte i funktions-/klasskroppar. `journal()` som byter subprocess.Popen (igenkänning på danger-full-access) är grön och avinstallerar grindens inspelare; klasskropp på modulnivå ändrar AUTOPILOT_ROLE_POLICY vid import. Åtgärd: identitetskontroll efter flödena + manipuleringssäker inspelare, exec-ytsregel över hela filen med exakt vitlista (10 ofarliga mål), formregel även för klasskroppar, körtid==literal för alla sju konstanter, provider-argv-igenkänning på flera markörer.
- N1–N8: posix_spawn, AUTHORITY_LIB obunden, remedieringsanropets identitet, vakt mot spårad kopia, falskt rött på `X = Y.copy()`, härledda plankonstanter, oläst role_policy. Falskt-rött-kostnaden för de fyra blobpinnarna ska stå i dev-doc p.8.

## Kontrakt v3.6 fryst (2026-09-11 ~06:15) → grindgranskning v11
- TA-klon: 7e0eb95a (grind+kriterier, parent 61426e1c) → 50956fa7 (utfall, tree fbc88251). Grind v3.6 sha256 8a26e60f…, 2758 rader, 117 rader; dok 98f9335b…, 1325 rader.
- B1 nu bunden i hela filen och över hela körningen: exec_surface_assignments (attributmål i exec-ytan var som helst, sys.modules/globals/vars/locals, subscript på modulnivånamn, AugAssign, setattr; undantag byte-exakt sys.dont_write_bytecode), formregel för klasskroppar, popen_identity_after (inspelarna måste finnas kvar efter flödena), flera startprimitiver (Popen + posix_spawn(p)/execv*/spawnv*/system) med fail-closed binärmängd {git}, alla sju plankonstanter körtid==literal.
- N: AUTHORITY_LIB AST-pinnad + core-fil under controller/authority/; remedieringsposition måste bära FIXTURE-1; ny rad som muterar planen OCH varje spårad kopia; falskt rött på X = Y.copy() borttaget (verifierat grönt); hopsatt docs-sökväg röd; p.8 innehåller blobpinnarnas falskt-rött-kostnad.
- RED 76/41; referens 117/117 result 575ee34c… utan produktändring; negativer 69/69 + falskt-rött-provet grönt.
- Grindgranskning v11 startad i `~/nortropic-repos/work/gate-review-final-separation-v11` @ 50956fa7.

## Grindgranskning v11 (50956fa7) = NOT_READY, två blockerare → v3.7 beställd (2026-09-11 ~06:50)
- v10-remedieringar äkta (7/7 reproduktioner); falskt-rött-provet grönt; F7/argparse byte-identiska; referens 112/5 första försöket utan produktändring.
- B1: providergränsen binds vid Popen, inte under den — `class _Boot: POPEN = subprocess.Popen` + byte av `_Boot.POPEN._execute_child` i journal() ger 112/5, popen_identity True, medan barnet tar emot neutral prompt. Åtgärd: transitiv aliasspårning av exec-objekt, förbud mot dunder-/internattribut, identitet på `_execute_child`/`__init__` före+efter, samt jämförelse av det barnet faktiskt får mot fångad byggarprompt.
- B2 REGRESSION i v3.6: indentering r.2367–2368 lade gamla-pekar-svepet av levande prompter innanför FIXTURE-1-villkoret och utanför prompt-loopen → svepet körs aldrig på grön produkt; gammal plansökväg i L-remedieringsprompt grön under v3.6, röd under v3.5. Åtgärd: rätta indentering + tio flödeskanarier.
- N1 RED-protokollet 76/41 ej reproducerbart (mätt 72/45 statiskt → 77/40). N4 kopieringsmutationsraden vakuös på baslinjen + evaderas av digest-vakt. N9 FALSKT RÖTT mätt två gånger: legitim `/usr/bin/env` eller pinnad python3.12 under flöde blir röd på sluten binärmängd. N8 skrivningar i .git/ och FIXTURE_ROOT osynliga.
- 20 nya attacker: 8 fångade, 10 missade, 2 falskt röda, 1 grön kontroll.

## Kontrakt v3.7 fryst (2026-09-11 ~08:00) → grindgranskning v12
- TA-klon: 5f7c8215 (grind+kriterier, parent 50956fa7) → e1efb141 (utfall). Grind v3.7 sha256 58cd5bd1…, 2985 rader, 118 rader; dok f7f0af86…, 1459 rader.
- B1: transitiv aliasspårning (aliasmängd på baslinjen {p,r,rc,sub}), FORBIDDEN_ATTR_TARGETS (_execute_child, __init__, __call__, __new__, __get__, __getattribute__, __subclasshook__, _posixsubprocess, _communicate, _get_handles) på vad som helst + setattr, värderegel i klasskroppar, DRIVER fångar Popen/_execute_child/__init__ + nio primitiver FÖRE modulladdning, live kräver child_total==popen_total och ingen omskriven argv mellan Popen och barn. Granskarens a11-mutant fälls av tre oberoende instrument.
- B2 rättad: svepet tillbaka i prompt-loopen; tio flödeskanarier, alla röda och var och en flaggar sitt eget flöde (gröna under v3.6).
- N1 löst: RED-fixturen byggs om från omklonad 320c9df7 → statiskt 72/46, full 77/41 (delta = fem sandboxrader); v3.6:s 76/41 var fixturfel, rättelse inskriven. N4 kopieringsraden ankrad (anchors=2) + ny rad som ompinnar ROADMAP_PLAN_BLOBS i importerad modul. N8 svep täcker .git/ och FIXTURE_ROOT. N9 ALLOWED_LIVE_BINARIES {git, env, sh, python3.12} → tre falskt-röda prov gröna (113/5).
- Referens 118/118 result 3c6f8f5a…; popen_total=child_total=333, provider_starts=0, identitet True före/efter. Negativer 84/84.
- Kvarstående deklarerade: N5 FIXTURE-1 närvarokrav, N6 AUTOPILOT_ROLE_POLICY.update() under flöden, N7 handoffens PLAN_GENERATION ej korsjämförd, N11 grinden städar inte eget FIXTURE_ROOT.
- Grindgranskning v12 startad i `~/nortropic-repos/work/gate-review-final-separation-v12` @ e1efb141.

## Grindgranskning v12 (e1efb141) = NOT_READY, två blockerare → v3.8 beställd (2026-09-11 ~09:00)
- v11-remedieringar verifierade genom reproduktion; RED reproducerbart 72/46 statiskt → 77/41, 41-radslistan identisk; referens 113/5; tre falskt-röda prov gröna.
- B1: providergränsen binds av satsformer — importtidsfångst via funktionsdefaultargument/dekoratorargument är varken Assign/AnnAssign/setattr och module_level_form hoppar över FunctionDef; de åtta os.*-primitiverna saknar inspelare under modulattributet. MÄTT: 24 riktiga processer med neutral prompt medan grinden var 113/5 grön; räknarraderna är balanserbara (19+19). Fix: installera inspelaren FÖRE exec_module + inspelare för alla nio primitiver + icke-balanserbara räknare (per-anrops-identitet/argv).
- B2 REGRESSION mot v3.6 från N9-fixen: providerrad i ett `sh -c`-element, hopsatt i körtid, via subprocess.run = grön; med ALLOWED_LIVE_BINARIES={git} röd. Fix: dela i VERKTYG (git, fri argv) och OMSLAG (env/sh/python3.12, delsträngstest över hela argv).
- Rapporteringsfel: result.json live_*-fält rapporterar MUTERADE körningen (live_out överskrivs r.2628 före serialisering r.2961) → förklarar "popen_total 59 vs 333". Två nya falskt röda från global textmatchning i aliasspårningen.
- N5/N6/N7 bekräftat immateriella för ordern (N6 styr bara modell/reasoning-effort; N7 kan bara ge motstridig etikett då gamla blobbar/sökvägar är mekaniskt förbjudna).

## Kontrakt v3.8 fryst (2026-09-11 ~10:05) → grindgranskning v13
- TA-klon: 0bd3d58f (grind+kriterier, parent e1efb141) → c4721ae8 (utfall). Grind v3.8 sha256 d97cb13e…, 3087 rader, 118 rader; dok 7f107a02…, 1558 rader.
- B1: inspelare på nio primitiver + Popen._execute_child installeras FÖRE exec_module → varje importtidsfångst (modulnivå, klasskropp, funktionsdefault, dekoratorargument, metoddefault, metaklass) får det instrumenterade objektet; import_time_starts rött; statiskt täcks args.defaults/kw_defaults/decorator_list; argv jämförs som multimängd, obalanserade barnstarter rapporteras per identitet.
- B2: ALLOWED_LIVE_TOOLS={git} exakt element; ALLOWED_LIVE_WRAPPERS={env,sh,python3.12} delsträng över hela argv + WRAPPER_ARGV_MAX=200.
- Rapporteringsfelet rättat (live_* = gröna körningen, live_mutated_* = muterade; referens 333 resp. 59). Aliasspårningen skopmedveten → tom aliasmängd på baslinjen; två falskt röda borta.
- RED 72/46 statiskt → 77/41, radlistan byte-identisk med v3.7. Referens 118/118 result a0514798…. Negativer 91/91 + fem falskt-röda prov gröna.
- OBS: referenskonstruktionens plan/handoff raderades i v3.7-städningen och regenererades mekaniskt via TA:s `v38/make_ref_product.py` — granskning v13 ska pröva om 118/118 är nåbart ur dokumentet allena (annars är kontraktet bara satisfierbart via TA-artefakter = blockerande för BUILDER).
- Grindgranskning v13 startad i `~/nortropic-repos/work/gate-review-final-separation-v13` @ c4721ae8.

## Grindgranskning v13 (c4721ae8) = NOT_READY, två blockerare med samma rot → v3.9 beställd (2026-09-11 ~11:10)
- Verifierat: v12:s B1/B2 faller rätt, fem falskt-röda prov gröna, RED 72/46 med identisk 41-radslista, F7 byte-identisk, radnamnsdiff tom, live_*/live_mutated_* korrekta. VIKTIGT: referensen nåbar ur dokumentet allena (granskaren byggde 113/5 i tre iterationer utan TA:s make_ref_product.py) → kontraktet ej beroende av TA-artefakter.
- B1: DRIVERn kör som `__main__` i samma interpreter och behåller _ORIG_PRIMS/_ORIG_EXEC_CHILD; `import __main__` + återställ `_execute_child` ger 113/5 med räknare identiska med ren referens medan riktig barnprocess kördes.
- B2: omslagsregeln fångar bara tre markörsträngar i argv. Sex gröna mutanter med bevisade barnprocesser (sh via STDIN, sh -c exec "$0", env, python3.12 -c, skript med basnamn `git`). AVGÖRANDE: barn tog emot `PROMPT=read docs/loop/autonomous-loop-plan-v1.md` på stdin medan grinden var grön — gamla planen nådde en levande prompt.
- Strukturell fix beställd: live-flöden i SEPARAT process (inspelare i eget modulnamn, original i closure), processtarter mätta UTIFRÅN via stubb-PATH som loggar argv+stdin och delegerar, realpath+sha256-identitet i stället för basnamn, markör- och OLD_PLAN_TOKEN-skanning över argv ∪ stdin ∪ env, `__main__`/type.__setattr__ i statiska förbudsmängden, vakuös aliasspårning ankras eller ersätts.
- Icke-blockerande: två påstådda rättelser i ändringstabellen gjordes aldrig (r.755, r.1408); default-/dekoratorregeln saknas i kriterietexten och fäller `def f(cmd,_r=subprocess.run)`; drivrutinens TMPDIR = cwd på sys.path.

## Kontrakt v3.9 fryst (2026-09-11 ~14:20) → grindgranskning v14
- TA-klon: 1013a75c (grind+kriterier, parent c4721ae8) → f6add80b (utfall). Grind v3.9 sha256 f030dd17…, 3381 rader, 119 rader; dok 84efc563…, 1750 rader.
- Strukturell omläggning: live-flöden mäts UTIFRÅN via stubb-PATH (git, node, python3.12, env, sh) som loggar realbinär, hela argv och (vid pipe) hela stdin till fil som grinden läser utanför produktens interpreter; binäridentitet = realpath+sha256, inte basnamn; OLD_PLAN_TOKENS + COMMIT_READ + providermarkörer skannas över argv ∪ stdin ∪ env; DRIVER_BOOT kör i privat namnrymdsdict utanför sys.modules (__main__ bär inga original); inspelare även på Popen.__init__ med init_total==popen_total; identitetsprövning vid varje anrop; GATE_NAMESPACE_TOKENS + förbud mot explicit __setattr__ och beräknat setattr-namn.
- Timeout är nu produktutfall (rc 124 + markör); ny sista rad f10_gate_reached_its_last_row_without_an_unexpected_failure ger exit 1 i stället för riggfel vid sent oväntat fel → 119 rader.
- RED 72/47 statiskt → 77/42 (exakt EN tillkommen röd rad mot v3.8: live-raden, röd av rätt skäl eftersom autopilotens egna git-starter på 320c9df7 bär docs/loop/autonomous-loop-plan-v1.md). Referens 119/119 result 9ba9fd4a…, fyra oberoende räknare alla 333. Negativer 101/101 + fem falskt-röda prov gröna.
- v13:s sju mutanter faller nu: driver-ns på formraden (+ angreppet omöjligt), stdin-gamla-planen på live-raden, fyra omslagsmutanter på live-raden, git-basnamnsskriptet på omätt-binär-raden, aliassonderna på exec-alias-raderna.
- TA-fynd: v3.8:s dokumentpatch avbröts på ankarfel före skrivning (förklarar granskningens "uteblivna rättelser"); patchskripten skriver nu även vid missat ankare.
- Grindgranskning v14 startad i `~/nortropic-repos/work/gate-review-final-separation-v14` @ f6add80b.

## Grindgranskning v14 (f6add80b) = NOT_READY, tre blockerare → v3.10 beställd (2026-09-11 ~15:20)
- Verifierat: v13:s sex mutanter faller rätt, fem falskt-röda prov gröna, RED 72/47 av 119 (+1/−0 rader, tillagd rad röd av rätt skäl: baslinjens `git cat-file -e …autonomous-loop-plan-v1.md`), F7 byte-identisk, f10-raden fungerar. Referensen nådd i FÖRSTA iterationen med v13:s dokumentbyggda konstruktion → ingen produktändring krävs.
- B1: privata namnrymden nås via sys._getframe/f_globals/f_back och gc.get_objects (ej i GATE_NAMESPACE_TOKENS; DYNAMIC_LOOKUP_NAMES matchar bara Name-anrop). VÄRST b11: inspelningslistorna byts mot list-subklasser med tom append → 114/5 grön med popen=child=init=5 medan stub_calls=333; ingenting jämför halvorna.
- B2: `_identify` löser binär med os.environ['PATH'] i drivrutinens process medan Popen löser via env=-argumentets PATH → b1 startade produktens egen binär med `PROMPT=read docs/loop/autonomous-loop-plan-v1.md` på temp-FIL som stdin, grinden 114/5 byte-identisk med referensen. Även ärvd fd (b9), stdin som fil till riktiga git (b2), `git -c alias.zz='!…'` (b7).
- B3: stubbloggens sökväg i klartext på produktens PATH, katalogen undantagen från sidoeffektsvepet (r.2876), ingen rad binder live_stub_call_total; 7 poster raderade 333→328 utan reaktion. Dokumentets p.8 r.805–811 falsifierad.
- Beställt: halva-mot-halva-rad, räknare i closure + typidentitet, frame/gc i förbudsmängden, binäridentitet i barnet (stubben loggar egen realpath+sha256) och PATH från env=-argumentet, stdin i alla kanaler + ärvda fd, git -c/GIT_*-skanning, HMAC-kedjad logg med löpnummer, svep utan undantag, egen rad för live_stub_call_total.
- Icke-blockerande: sent riggfel ger fortfarande exit 2 (except Rig före except Exception); f10-vägen skriver ingen result.json och tallyn ser bättre ut än baslinjen; node-stubben.

## ÄGARBESLUT 2026-09-11 — målbild, arbetssätt, slutkriterier, införande
- Dokument: `~/nortropic/AGARBESLUT-20260911-MALBILD-ARBETSSATT-SLUTKRITERIER.md` (kopia i backupens reports/); minne: `nortropic-agarbeslut-20260911-malbild-slutkriterier.md`.
- Målbild: autonomin identifierar behov, prioriterar, genomför och utvärderar inom organisationens mål och mandat. Bootstrap har ÄNDLIG överlämningspunkt till kvalificerad autonom drift; hela framtida Nortropic byggs inte färdigt under bootstrap. Webb/Digitala är en verksamhet som använder plattformen.
- Arbetssätt: grindändring kräver befintligt krav + konkret hinder för leveransen; sidoförbättringar är inte blockerare; budget gör aldrig ett kvarvarande fel godkänt, men skenande kostnad ska ge enklare upplägg eller ändrad implementation; riggbegränsningar bedöms mot uppgiftens hotmodell (samma användare/maskin är inget generellt undantag); rutinbeslut autonomt.
- Slutkriterier: planseparation / Trust Kernel (exit 0 räcker inte — rätt frysta verifierare körda färdigt mot exakt rätt kandidat) / lokal bootstrap-milstolpe / operativ helhet (senare, ej startad nu) + H039:s funktionskrav kvar.
- Införande: regler.md = arbetsmetodens källa, nya plattformsplanen = mål och slutkriterier, AGENTS/CLAUDE/skills hänvisar utan dubblerade regelverk; dokumentbindningar går genom pågående flöde, ingen separat grindserie.
- TILLÄMPNING: v3.10 är sista kontraktsrundan om inte ett fynd kopplas till krav + konkret hinder. Hotmodell skriven till TA: blockerande = gammal plan/webbstyrning når faktiskt agent/process, eller bevis förfalskas med vanliga produktmedel; deklarerad gräns = undanflykt som kräver avsiktlig manipulation av grindens interna objekt (frame/gc/utbytta inspelare/loggfil som samma användare).
- Tillkommande bindningar i v3.10 (kontrollerad täckning: AGENTS/CLAUDE/README/regler/byggplan redan generationsdokument; plan-avsnitten redan krävda): planens Avslutskriterier med de fyra nivåerna, Bootstrap med ändlig överlämningspunkt, Målbild med självdriven autonomi, H039-kravet bevarat i planen, regler.md som metodkälla + rad mot duplicerade regelformuleringar. regler.md flyttas in i produktytan.

## Kontrakt v3.10 fryst (2026-09-11 ~19:30) — v14-remediering + ägarbeslutets bindningar → granskning v15
- TA-klon: 672436c (grind+kriterier) → d5605db (utfall, tree 9c9f6a9f). Grind sha256 c0b2f61d…, 3720 rader, 127 grindrader; dok f91880a5…, 1993 rader.
- Ocommittad ändring från stoppad instans BEHÖLLS efter prövning: halvorna-mot-halvorna delas i `stub_calls == bare_name_starts` + `popen_total == init_total == child_total`. Skäl: PATH-stubbar ser per konstruktion bara bara-namn-starter; absolutvägsstarter binds av in-process-halvan, realpath+sha256 och slutna formmängden. b11/b4/b5 faller fortfarande (closure-heltal).
- A: kedjerad (nonce + löpnummer + HMAC), barnsidig identitet + PATH ur env=-argumentet, stdin i pipe/fil/ärvd fd, git -c/GIT_*-skanning, loggkatalogen ej längre undantagen, live_stub_call_total bunden. Sent riggfel = produktrad; result.json skrivs på f10-vägen med not_run räknade som FAIL (mätt: gate-abort → exit 1, 114/13 över hela nämnaren).
- B (ägarbeslutet): sex nya rader — Avslutskriterier med fyra nivåer, Bootstrap med ändlig överlämningspunkt, Målbild med självdriven autonomi + webb som verksamhet, H039-kravet bevarat, regler.md som metodkälla, rad mot duplicerade normativa meningar. `## Hotmodell` bunden av DOC_SECTIONS. regler.md i produktytan, ej i "rörs inte"; ompinning av CLAUDE.md + regler.md utskriven.
- regler.md-frågan mätt: WEB/HUMAN/HARD_HUMAN/OLD_PLAN/COMMIT_READ ger noll träffar; `ägarhand` r.16 och `kundflöde` r.29 matchar bara PLAN_TOKENS (gäller enbart plangenerationen) → inget ankare behövs, noll nya rader.
- RED 74/53 statiskt → 79/48 av 127 (+6 rader, −0). Referens 122/5 statiskt → 127/127 full, alla sex nya rader gröna i första iterationen. Negativer 124: 117 fångade, 7 falskt-röda prov gröna, 0 riggfel.
- Deklarerade gränser under hotmodellen: körtidsnåbarhet till grindens interna objekt (statiskt förbjudna; 13 undanflyktsformer röda, 2 godartade gröna), samma-användare-manipulation av loggfilen (DETEKTERBAR, ej förhindrad), bara-namn-nämnaren, parafrasering förbi B1–B5-ankarna (hör till produktgranskningen).
- Granskning v15 startad i `~/nortropic-repos/work/gate-review-final-separation-v15` @ d5605db, med ägarbeslutets godkännandestandard som bindande instruktion.

## Grindgranskning v15 (d5605db) = READY (2026-09-11 ~20:10) → BUILDER startad
- Inga blockerande fynd. 39 grindkörningar, alla statiska, ingen bypass. RED 74/53 av 127 (+6/−0 mot v3.9), radnamnsdiff +8/−0. Referens 122/5 i FÖRSTA iterationen byggd UR DOKUMENTET ALLENA (granskaren skrev själv de sex nya textytorna ur p.6b, öppnade inga TA-artefakter) → kontraktet är satisfierbart för en builder.
- v14:s tre blockerare verkligt stängda: b1_env_path_launder faller på fem oberoende grunder; b3 på bruten HMAC; b4/b5/b11 på tokenskanning + closure-räknare. F7 byte-identisk med v2.5 (regionsha 091ceea6, 68 rader, argparse abe14c76, 13 konstanter). Avbrottsvägen: exit 1, ROWS=116/11 över hela nämnaren, result.json med aborted:true.
- regler.md-påståendet verifierat oberoende: WEB/HUMAN/HARD_HUMAN/OLD_PLAN/COMMIT_READ = 0 träffar; PLAN_TOKENS = 2 (ägarhand r.16, kundflöde r.29) som bara gäller plangenerationen. Inget skydd förloras.
- 18 nya angrepp: tre ej fångade, alla under ägarbeslutets hotmodell — (1) `__globals__`/`__closure__`/`cell_contents` når drivrutinens namnrymd (deklarerad gräns: avsiktlig manipulation); (2) `git --config-env=alias.zz=…` går förbi git-startarlistan (icke-blockerande: når ingen live prompt, får inte räknarna att ljuga — noteras som känd gräns, ingen ny kontraktsrunda enligt ägarbeslutet); (3) ankare ≠ mening (parafras/motsägelse) — hör till produktgranskningen.
- Tio icke-blockerande N1–N10, bl.a. EXPECTED_ROW_COUNT gör legitima nya aktiva dokument röda, och `/private/tmp/claude-501` i sidoeffektsvepet ⇒ samtidiga sessioner kan ge riggröd (kör en fullkörning i taget).
- BUILDER startad i `~/nortropic-repos/work/builder-plan-generation-20260911` (gren nortropic/plan-generation, från 320c9df7). Specifikation = den hållna dev-docen; grinden körs från hållen kopia i gate-review-v15. Mål: 127/127 + PASS_LOCAL_QUALIFICATION_ONLY.
- TILL PRODUKTGRANSKNINGEN: pröva särskilt de tre ofångade klasserna ovan mot den verkliga produkten — särskilt att ankartexterna betyder vad de säger (ingen parafras som motsäger), och att ingen git-startare med --config-env införts.

## BUILDER-kandidat 40f48515 — plattformsplanen byggd, grinden 127/127 (2026-09-11 ~21:00)
- Kandidat: `40f48515ef75c48bd361b0d2afe2a60478479d0c`, tree `387c2d161d7e51a423f121c01a0a1e477e6a1a2c`, parent 320c9df7, gren `nortropic/plan-generation` i `~/nortropic-repos/work/builder-plan-generation-20260911`. 21 filer ändrade.
- Nya: `docs/loop/autonomous-loop-plan-platform-v2.md` (blob fbdbcf05), `docs/loop/autonomous-loop-platform-handoff-v2.md` (a0c0c9ed). Borttagna: autonomous-loop-plan-v1.md (c8ea8511), autonomous-loop-codex-handoff.md (1e53887c).
- Ändrade: autopilot 9ae6551e→a4dacecb, controller/verify/cli f4674d9e→e00780e4, AGENTS 8d54ece2→0f27560f, CLAUDE 772a39e8→9e1d6976, README, regler.md b28cb662→5a4f6b90, full-roadmap, substitutionskontraktet (+§15), drift.md, sex rollskills.
- Fullkörning r2 på levererad kandidat: exit 0, 127/127, PASS_LOCAL_QUALIFICATION_ONLY, result.json 5eabb235…. Evidensrot /private/tmp/nortropic-full-r2/… kvar.
- Röda på vägen (två orsaker, båda produktfix): frasen "Effect authority" träffade OLD_PLAN_TOKENS-mönstret `effect[- ]authority` → omformulerad; empiriska remedieringens inlinade `extra` saknade plan/handoff → PLAN_GENERATION + båda sökvägarna infogade. Ingen dokumenttext försvagades, ingen rad bedömdes som grinddefekt.
- VERIFIERAT AV ORKESTRATORN: grinden i kandidaten byte-identisk med hållen kopia (c0b2f61d = c0b2f61d), dev-doc likaså (f91880a5 = f91880a5) → buildern har inte ändrat sin egen domare. Under verify/ finns exakt en post (den frysta grinden); controller/verify/cli är inte i skyddade mängden (den är `controller/verify/register.json`).
- Två flaggade avvikelser till produktgranskningen: (1) grind+dev-doc kopierade in i kandidaten — krävs av f6/f10, byte-exakt; (2) amend efter fullkörning r1 (5352436d), därefter OMKVALIFICERING med r2 på levererad commit — identiskt träd.
- REVIEWER startad (read-only) → rapport `REVIEW-PLAN-GENERATION-40f48515-20260911.md`. Uppdrag utöver grinden: ankare≠mening i de sex ägarraderna, webbstyrning återinförd i SAK men inte i token, KEEP-innehåll tappat, ny providerstartyta, samt rendering av verkliga rollprompter.

## Produktgranskning av 40f48515 = NOT_READY, ett blockerande fynd (2026-09-11 ~21:40)
- Granskaren reproducerade fullkörningen oberoende: RC=0, 127 PASS/0 FAIL, rows=127, subject_head 40f48515; hållna grindar control-set 68/0, launch-cwd 19/1, governance 68/2 — alla förutsagda. Inga --held-* behövdes (kandidatens tre grindar har exakt 332f07ce-blobbarna).
- B1 BLOCKERANDE: planen r.18–19 påstår att den bevarar gamla planens kvarvarande plattformsarbete, men S4, S5, S7–S13 (h-018…h-026) saknar detaljerade exitkriterier och skivspecifika negativa kontroller i varje spårad fil vid HEAD (byggplan §7 = h-001…h-017; spec saknar h-018…h-030; substitutionskontraktet §6 = SUB-1…4, §8 = en rad per S-skiva). Gamla blobben förbjuden vid HEAD + pekare förbjuden token ⇒ innehållet onåbart för regelföljande agent. Bortfall: S4 artefakt-/base-regler + S4↔S5-gränsen, S5 seq-ordning + okänt event_type, S7 fast-forward + förväntad gammal main-SHA, S8 single-parent D. Bryter ägarbeslutets ingress om bevarade detaljkrav.
- Allt annat håller: grinden orörd (c0b2f61d) och granskaren ACCEPTERAR materialiseringen i kandidaten som kontraktsflödet; amend-trädet identiskt (387c2d16) och fullkörningen gjord på 40f48515 själv; de två produktfixarna stärker meningen; skivtabellen matchar autopilotens 15 tuplar i ordning (verifierat genom import); inget dubblerat regelverk; ALLA rollprompter (ARCHITECT, TEST_AUTHOR SUB-1+S2, GATE_REVIEWER, BUILDER, remedieringar, empiriska) namnger plan+handoff+platform-v2 med noll träffar på 22 gamla-plan-/webbmönster; ingen ny providerstartyta; de sex ägarraderna läser rätt som människa.
- Icke-blockerande: N1 amend efter grindkörning bryter builderns egen skill r.81 (skadan inträffade inte); N2 result.json-sha är inte reproducerbar för någon (fem mkdtemp-sökvägar) → redovisa exitkod/127/subject_head i stället; N3 planens r.24–25 bokstavligen osann för S1/S3/L; N4 PLATFORM_DOCUMENTS pinnar sha256, inte blob.
- BUILDER återkallad för B1 (appendix med bevarade kriterier, läst ur objektlagret utan pekare) + N3. Ny commit ovanpå 40f48515, ingen amend, omkvalificering.

## BUILDER-remediering → kandidat 65830a2f (2026-09-11 ~22:10)
- Ny commit OVANPÅ 40f48515 (ingen amend): `65830a2f41fce35c39428dd40a504ed4abd617c9`, tree `f8ac0343dde08ac43b7c8115bfa92ba0b66c10a7`, parent 40f48515. Tre filer: planen fbdbcf05→7a7be190 (+183 rader), autopilot a4dacecb→00d8d9d6 (ompinning ROADMAP_PLAN_BLOBS + selftestens planblob), controller/verify/cli e00780e4→d0f4ebf3 (ompinning PLATFORM_DOCUMENTS sha256).
- B1 åtgärdat med `## Appendix A — bevarade krav och negativa kontroller för de obyggda skivorna`: A.4 (immutabel artefakt, fallen kandidat aldrig nästa base, artefakten aldrig grindkod/register, S4↔S5-gränsen), A.5 (seq ej ts med bakåtgående klocka, okänt event_type avvisas, append-only, strömmen aldrig auktoritet), A.7 (non-force fast-forward, förväntad gammal huvudlinje-SHA, avbrott vid rörd huvudlinje, lease, idempotens, credential-läckage, statiskt force-prov), A.8 (single-parent D, aldrig merge; omverifiering från noll; B:s dom aldrig ärvd), A.9, A.10, A.11, A.12, A.13 (fem verb med typad nyttolast, sjätte avvisas, kanariefil, läsytan kan inte skriva).
- Källa: `git cat-file -p c8ea8511…` ur objektlagret; ingen pekare till commit/blob/gamla sökvägar i aktiv text. Renat vid överföringen: docs/05-skrivytor, `målbild §x.y` (dokument saknas i repot), `ägarhand`, `Verkstadsgolvet`, Slack-webhook, "tar bort människan ur merge-gaten"; "grindar registreras av ägarhand" → "registreras genom kontraktsflödet".
- N3 omskrivet sant (femton rader mot tuplarna i ordning; S1/S3 ur specraderna; L ur EMPIRICAL_GATE_PATH).
- Omkvalificering: statiskt 122/5 (fem sandboxrader), EN fullkörning efter /bin/ps: exitkod 0, 127 PASS/0 FAIL, rows=127, subject_head=65830a2f, PASS_LOCAL_QUALIFICATION_ONLY; hållna grindar control-set 68/0, launch-cwd 19/1, governance 68/2 (förutsagda). Per N2 redovisas ingen result.json-sha (körningslokala mkdtemp-sökvägar).
- Andra produktgranskningen startad (ny oberoende granskare) → `REVIEW-PLAN-GENERATION-65830a2f-20260911.md`. Uppdrag: B1 stängt i SAK per skiva mot gamla innehållet, bedöma de fem "renade" borttagningarna (särskilt om ägarhandsregistreringen ändrade säkerhetsegenskapen eller bara auktoritetsetiketten), samt full regressionskontroll.

## PLANSEPARATIONEN LEVERERAD — integration 65830a2f kvalificerad (2026-09-11 ~23:00)
- Andra produktgranskningen: READY. B1 stängt i SAK — appendix A (plan r.233–401) jämfört fält för fält mot gamla blobben: A.4 6/6, A.5 6/6, A.7 9/9 (förstärkt), A.8 8/8, A.9 5/5, A.10 6/6, A.11 5/5 (etikettbyte), A.12 7/7, A.13 7/7 negativa kontroller bevarade; ingen mätmetod mjukad. Alla sju namngivna punkter finns.
- Reningarna legitima. KRITISKA: "grindar registreras av ägarhand" → "genom kontraktsflödet" ändrar ETIKETTEN, inte säkerhetsegenskapen — defaults.denied_write mätt oförändrad, planens invariant "aldrig av den som ska dömas av den" står kvar, A.11 behåller författare≠byggare i skilda trust-domäner.
- Granskarens egen fullkörning: RC=0, 127/0, rows=127, subject_head=65830a2f. 25 egna promptrenderingar bär plan+handoff+platform-v2, 0 gamla träffar. Ingen regression, ingen amend.
- INTEGRERAT: `~/nortropic-repos/nortropic-system`, gren `nortropic/platform-integration-20260910`, fast-forward 320c9df7 → 40f48515 → **65830a2f** (ingen merge-commit), 143 spårade filer, ren arbetskopia.
- ORKESTRATORNS EGEN KVALIFICERING på integrationshuvudet: `--subject ~/nortropic-repos/nortropic-system`, exit 0, **127 PASS / 0 FAIL**, `PLATFORM_SEPARATION_FINAL_RESULT=PASS_LOCAL_QUALIFICATION_ONLY`. (Obs: grindens argument är `--subject` och `--held-{control-set,launch-cwd,governance}` — inte `--repo/--held-gate/--held-doc`.)
- Städat: kvalificeringens TMPDIR, r2/r3-evidensrötter och de två gamla fixturrötterna från 2026-09-10 borttagna.
- Icke-blockerande kvar (NB1): gamla planens designavsnitt bortom skivkriterierna (11-stegspromotionen, kraschpunktstabellen, privilegieseparationens form, två event-disambigueringar) står i inget aktivt dokument — tas vid respektive skivas frysning. NB2–NB8 kosmetiska/rapporterande.
- NÄSTA: refreeze av frysta H-grindar för plattformsgenerationen i beroendeordning (h-035 ∥ h-037 → h-036 → h-038; h-032/h-031 AST-läser autopiloten; document-authority-exit egen version) enligt `RECON-REFREEZE-HKEDJA-20260910.md` och `H035-RIGGFEL-UTREDNING-20260910.md`. Det är "nödvändiga bindningar kvalificeras för plattformsgenerationen" i ägarbeslutets lokala bootstrap-milstolpe.

## Ägarinstruktion 2026-09-11 (kväll): statusrättning + fortsatt bootstraparbete
Kontroll före ändringar: integrationshuvud `65830a2f41fce35c39428dd40a504ed4abd617c9`, rent arbetsträd, inga egna
agenter igång (en annan interaktiv session är aktiv på värden → /bin/ps före varje fullkörning kvarstår).

Två dokumentfel som ska rättas (exakt text uppmätt):
- `docs/loop/autonomous-loop-plan-platform-v2.md` r.165: "Kedjan är byggd och dess exitprov ligger i trädet."
  För starkt. Ska skilja fyra tillstånd: (1) befintlig implementation, (2) historiskt kvalificerad version,
  (3) kvalificering för dagens plattformsgeneration, (4) faktiskt kvarvarande produktarbete. En befintlig
  grindfil visar inte ensam att uppgiften är färdig.
- `docs/loop/autonomous-loop-platform-handoff-v2.md` r.38–42, punkt 4: "Ta första raden i planens skivtabell vars
  `status` är `OBYGGD` … Vid oförändrat läge är det SUB-1 / h-027." Pekar förbi kvarvarande H-arbete;
  leveransrapporten anger H-arbetet först. Ska synkas till faktisk beroendeordning.

Ägarens ramar för genomförandet: preciseringarna görs i NÄSTA H-stegs ordinarie dokumentuppdatering; nödvändiga
dokumentpinnar (`ROADMAP_PLAN_BLOBS` + selftestens planblob i autopiloten, `PLATFORM_DOCUMENTS` i
`controller/verify/cli`) hanteras genom det etablerade kontraktsflödet; INGEN separat omfattande grindserie för
statussynken. H039 ska stå kvar i den återstående vägen: refreeze-kedjan (h-035 ∥ h-037 → h-036 → h-038) är
omfrysning av BINDNINGAR och bevisar inte att H039:s kvarvarande produktarbete är färdigt. H039:s funktionskrav
kvarstår (noll registrerade runtime-rester; ingen radering/ersättning av främmande data via kapplöpningen).
Tidigare evidens och B-arbetskopians avsiktliga NOT_READY bevaras. Lokal bootstrap-milstolpe ≠ operativ
överlämning (installation, driftkvalificering, supervisor-resume, självdriven arbetsidentifiering ligger kvar på
vägen men startas inte av denna instruktion). Äldre designunderlag (NB1) tas vid respektive arbetsdels frysning.

Pågår: read-only statusmätning per H-steg (fyra tillstånd), sann beroendeordning, konkreta hinder, och förslag på
sann ersättningstext för de två dokumentställena inkl. vilka pinnar som berörs och vilka grindrader som begränsar
formuleringen.

## Statusmätning klar — fyra lägen per H-steg (2026-09-11) → `~/nortropic/STATUS-HKEDJAN-FYRA-LAGEN-20260911.md`
Mätt read-only vid 65830a2f, inga grindkörningar. `specs/tasks.spec.json` OFÖRÄNDRAD mot 320c9df7 (blob 3d810cf7)
⇒ refreeze-reconens spec-fynd gäller rakt av. Två NYA GEN-avvikelser från plangenerationen: autopilot
aedec2a3→9f22a1d4 och controller/verify/cli bfefe973→500fe140 (plus drift.md e5f8f532→e3da007a).

**Planens påstående är falskt för två skivor:** `controller/result/**` saknas helt (h-032, 0 spårade filer) och
attempt-root-inneslutningen saknas i `controller/launch/cli` (h-038, 0 träffar på `attempt`). Grindfil finns ≠
skivans produkt finns.

**Kvalificering mot 65830a2f: INGEN skiva är kvalificerad.** h-035 är uppmätt RÖD (459/3 på 320c9df7, samma spec
⇒ samma tre rader): F_R13 (radens allowed_write saknar docs/05 — NY), F_R15 (spec-transformbas c161a1c5, 25 rader
med human_only ≠ 26 utan) och F_H036_V3 (docs/05 saknas, drift.md ändrad) — de två senare RÖDA REDAN SEDAN
6ff724e6 2026-09-02, alltså före separationen. h-038 RIG-kraschar på h-036-identitet (överspelad sedan 829234d,
inte bruten av plangenerationen). h-037 RIG-kraschar på registerbytes och pekar på `workflows/` och
`tests/fixtures` som inte finns. h-036 fälls säkert (docs/07 saknas, autopilot- och launch-drift, h-035-radhash
20875ff7→88e2dbda). Resten OVERIFIERAT.

**H039 — ägarens punkt, mekanismen ordagrant:** h-039:s specrad har `depends_on: ['h-036']`, INTE h-038.
R30–R33-registren bär `h038_h032_h031_or_supervisor_resume: False`, bundet av `R33_REGISTRY_SHA256`; RED-etiketten
är `H038_H032_H031_OR_SUPERVISOR_PROGRESS_BEFORE_FULL_H039_PASS`. **H039 kräver inget av H038 — H039 förbjuder
H038 att gå framåt före full PASS.** H039:s fyra pins (owner-production-paths, h-035, h-036, h-037) stämmer i dag
⇒ ett refreeze av h-035/h-036 GÖR h-039 röd. Kvarvarande H039-produktarbete: `--r33-installed`-lanen
(installationsceremoni, post-state-validering, R33-installed-review, frusen R15-live-diagnostik, körning) —
ingen `h039-r33-*installed*`-evidens finns; blockeras dessutom av `PRODUCTION_ORIGIN` (lokalt bare-origin räcker
inte). RÄTTELSE: minnesnoterna om R32/R33 var föråldrade — R33-kontraktet ÄR publicerat i `ed584ec3`, live-r3
byggd och formellt granskad. Den avsiktligt NOT_READY B-kopian = `R33_LIVE_R2_FAILED_EVIDENCE`, fryst som
superseded NO-CREDIT; ska inte återupplivas.

**Sann beroendeordning:** (i) ompinning: h-035 ∥ h-037 → h-036 → h-038-refreeze. (ii) produktarbete: h-032
(result-kernel, ÅTERVINNS ur `~/nortropic/forensics-h036-20260827/h032-recovered-product-r128/`, kandidat
caab2e4f), h-038 (3 filer/320 rader — minsta produktytan), h-039 (`--r33-installed`). h-031 NORMAL PASS kräver
h-032-produkt. **Nästa beroendemässigt möjliga H-leverans = h-035-refreeze**: ingen grind i arbetsträdet pinnar
h-035 uppströms, riggen är uppmätt körbar (462/0 på 2fb748b), och de tre felen är fullständigt kartlagda.
h-037 är parallellt möjlig men kräver ett beslut om radens mening (suite-posten finns inte längre).

**Verifierat av orkestratorn:** `platform-separation-final-exit` v3.10 pinnar INTE h-03x-grindarnas bytes
(0 träffar) ⇒ en omfrysning av h-035 krockar inte med separationsgrinden. Spec får inte ändras (f3 kräver
byte-identitet med 332f07ce) — h-035:s tre fel sitter i grindens konstanter, inte i specen, så inget spec-byte
behövs.

**Hinder för nästa steg (B1–B11 i statusrapporten):** kanonisk invokation `-I -S -B` + `PYTHONEXECUTABLE`; sju
bevarade kandidater måste finnas i replikans ODB; lokalt bare-origin med kanonisk form; git-config-vitlista;
`/private/tmp`-skrivning kräver bypass; 19 absoluta evidenssökvägar; en fullkörning åt gången (~450 s, annan
session aktiv); `controller/attest/cli` byte-fryst av separationsgrinden medan dess funktioner hårdkodar docs/05
(berör h-038-refreeze, inte h-035); två publiceringsidiom samexisterar.

**NÄSTA HANDLING:** h-035-refreeze som nästa H-steg, med planens r.163–167/175–177 och handoffens r.41–43
rättade i samma steg (ägarens ram: preciseringarna i nästa H-stegs ordinarie dokumentuppdatering, pinnar genom
kontraktsflödet, ingen separat grindserie). Berörda pinnar: `ROADMAP_PLAN_BLOBS` (autopilot r.94–95 OCH
selftestens duplicerade literaler r.2602–2605) och `PLATFORM_DOCUMENTS` (controller/verify/cli r.86–87).

## h-035-refreeze: del B klar och grön, del A blockerad av mätt fynd (2026-09-11 sent)
TA-klon `~/nortropic-repos/work/test-author-h035-refreeze-20260911`, gren `nortropic/h035-refreeze`:
- **`f0b553d030c3cb51f5bc42f492f48aa00fd26750`** (tree c61b8558, parent 65830a2f) = DEL B: plan + handoff +
  `ROADMAP_PLAN_BLOBS` (r.94–95 OCH selftestens r.2604–2605) + `PLATFORM_DOCUMENTS` (r.86–87). 4 filer, +40/−15.
  Separationsgrinden **127/0 rc 0** på denna. Nya pinnar: plan blob 7e14d5fb (sha256 ab559724…), handoff blob
  334671cf (sha256 ca89fa9e…).
- **`a288e1692e2dc795fc7b68f56aaf45b5589ae4a2`** (parent f0b553d0) = DEL A: refryst `verify/bin/h-035-exit`
  (sha256 91aa7fe7…, 22 511 rader). Refryst grind **462/0 rc 0** på kandidaten; baslinjen 459/3 av rätt skäl.
  Negativer: 3 fullkörningar (N1 460/2, N2 461/1, N3 461/1) + 22 isolerade, alla avvisade.
  Ändrade konstanter: (a) `H035_R13_FROZEN_AUTHORITY` minus enbart docs/05-sökvägen (ytan KRYMPER, exact_value
  kvar ⇒ varje breddning faller); (b) ny `H035_PLATFORM_SPEC_DELTA` med kanoniska sha256 per deklarerad
  avvikelse — transformbasen c161a1c5 OFÖRÄNDRAD som git-objekt; (c) `F_H036_V3` ny form
  `bas[:titel] + HEAD + bas[titel:] + H036V3-APPEND + TAIL` med storlek/sha256/markörbindning, gamla
  appendkonstanten oförändrad, docs/05 flyttad till `H036_V3_RETIRED_DOCUMENTS` bunden som git-objekt vid
  35d7fd7c med krav på FRÅNVARO ur trädet.

### BLOCKERANDE FYND (mätt, reproducerat): separationsgrinden fryser hela `verify/`-trädet
`FROZEN_TREES = ("verify", "controller/h034-native", "controller/runtime-cleanup", "controller/provenance",
"SEPARATION-20260910/proposed")` (r.137) blob-OID-fryser hela grindträdet mot 332f07ce och tillåter exakt ETT
tillägg (separationsgrinden själv). Dessutom fryser de tre hållna lokala grindarna samma träd mot sina baser.
På kandidaten a288e169: **122/5** — f6 (`problems=['verify/bin/h-035-exit']`), f7 control-set 67/1, f7 launch-cwd
samma orsak, f7 governance extra röd rad (kaskad), f8 kaskad. Alla fem har samma enda orsak: grindfilens bytes.
⇒ **Ingen H-grind kan frysas om förrän frysningen ombaseras.** Det blockerar h-035, h-036, h-037 och h-038.

### ORKESTRATORNS BESLUT (autonomt, inom ägarbeslutets undantag)
v3.11 av `platform-separation-final-exit` startas som eget steg: ombasera `FROZEN_TREES`/de hållna grindarnas
förväntade radmängder så att ORDNADE och KVALIFICERADE omfrysningar av H-grindar är möjliga, med bevarad
egenskap att inget webbmaterial återvänder till `verify/`. Avvisat alternativ: placera omfrysningar med
separationsgrinden medvetet röd — ägarbeslutets Trust Kernel-kriterium säger att kvalificering kräver att rätt
frysta verifierare körts färdigt med samtliga obligatoriska kontroller; en avsiktligt röd grind är inte
kvalificering. Fyndet uppfyller ägarbeslutets undantag (befintligt krav + konkret hinder).

### Ordning härefter
1. Oberoende produktgranskning av **f0b553d0** (pågår) → integrera. Rollnot: TA skrev texten (ägarens ram att
   preciseringarna rider på H-steget) och separationsgrinden härstammar ur samma TA-linje ⇒ den oberoende
   produktgranskningen är den kompenserande kontrollen.
2. v3.11-kontraktsrunda (frysningens ombasering) genom flödet.
3. Därefter placeras a288e169 (h-035-refreeze) och kedjan fortsätter: h-037 (kräver beslut om radens mening) →
   h-036 → h-038 + h-039:s bindning.

### Deklarerade gränser/riggfynd från steget
- `--r15-owner-product-lifecycle`-lanen var redan föråldrad före denna ändring (`H035_R15_CONTRACT_SHA256` på
  modulindex 89 i stället för 83, sedan R29/R33); lanen är `EXPECTED_PREPRODUCT_RED` och ingår inte i no-arg-domen.
  Att laga den kräver spec-ändring som separationsgrindens f3 förbjuder.
- **Riggskörhet:** separationsgrindens `f4_live_flows_…` föll två gånger på främmande temp-kataloger under
  `/private/tmp/claude-501` skapade av den ANDRA aktiva sessionen (räknarna identiska 333/333/333). Falskt rött,
  inte produktfel. Kandidat till åtgärd i v3.11.
- Grinden kräver att arbetsträdet är exakt det spårade trädet: kvarlämnad `__pycache__` gav `RIG_ERROR … retained
  physical checkout`. Kör alltid med `-B`.
- Durabel rigg: bare-origin flyttad till `~/nortropic/worktrees/h035-refreeze-origin.git` (refs/heads/main == HEAD).

## Produktgranskning av f0b553d0 = NOT_READY, ett blockerande fynd (2026-09-11 sent)
- Fullkörning: separationsgrinden **127 PASS / 0 FAIL rc 0** på replika av f0b553d0, 190,99 s. Riggskörheten
  inträffade INTE denna gång.
- **B1: felaktig sakuppgift i planen r.188–190.** Texten kallar
  `H038_H032_H031_OR_SUPERVISOR_PROGRESS_BEFORE_FULL_H039_PASS` för RED-etikett. Uppmätt: grindens RED-etikett är
  `A_H039_OS_EXCLUSIVE_RUNTIME_CLEANUP_OPERATIONAL` (h-039-exit r.3369, reason R33_REASON r.1519); strängen finns
  exakt en gång, r.25407, som nionde element i `forbidden` inuti `r26_source_binding_accepts` (def r.25156) —
  R26:s källbindning, inte R30–R33:s register. **Felet kom från orkestratorns egen instruktion**, som övertog
  formuleringen från statusrekognoseringen utan att verifiera ankaret. Fältet och riktningen är verifierade och
  sanna (r.8635/8805/9007/9266/9268) — det är ankaret som var fel. LÄRDOM: verifiera varje ankare jag vidarebefordrar
  i en instruktion, annars ärver produkten felet och granskningen får bära upptäckten.
- Verifierat av granskaren genom mätning: `controller/result/**` = 0 spårade filer; `grep -ci attempt
  controller/launch/cli` = 0 och `git grep -il ATTEMPT_ROOT` tomt; pinngrafen bevisar ordningen (h-036 pinnar h-035
  OCH h-037; h-038 pinnar alla tre; h-035 binder h-037 bara via historiska objekt); h-038 röd sedan 829234d;
  h-039-exit r.1946–1951 pinnar h-035 76d3bf10 och h-036 b6fd9737 = HEAD ⇒ refreeze gör pinnen föråldrad;
  handoffens startordning dirigerar rätt; alla fyra ompinningar exakta; selftest + ensure_roadmap_plan körda gröna;
  specen sha256-identisk; noll gammal-plan-pekare i prompterna.
- Icke-blockerande N1–N6; N2 (plan r.167 självmotsägande) och N5 (`## Arbetsflöde` nämner inte kedjans företräde)
  åtgärdas i samma rättning.
- TA återkallad: ny commit ovanpå f0b553d0 med rättad mening + N2/N5, samma fyra pinnar om, en fullkörning.

## B1 rättat → kandidat 5df9213c (2026-09-11 sent)
- Ny commit `5df9213c75c4d2ab0ba8acecefd058cbe389db36` (tree 6542c5e0, parent f0b553d0) på gren
  `nortropic/h035-plan-handoff-only`. 3 filer, +20/−17. Ingen amend; `a288e169` orörd.
- Meningen omskriven utan termen "RED-etikett": `H038_…_BEFORE_FULL_H039_PASS` placeras som `forbidden`-post i
  R26:s källbindning (h-039-exit r.25398–25408 inuti def r.25156, exakt en förekomst), hash-bindningen skrivs som
  gällande R33 (`R33_REGISTRY_SHA256` r.1483; R30/R31/R32 har egna konstanter r.1188/1344/1385), och subjektet är
  `depends_on`-LISTAN (specen r.6791–6793) eftersom radens `summary` nämner H-038 två gånger. Grindens verkliga
  RED-etikett `A_H039_OS_EXCLUSIVE_RUNTIME_CLEANUP_OPERATIONAL` r.3369. TA verifierade varje ankare med radnummer.
- N2 (r.167–168) och N5 (r.216–217 i `## Arbetsflöde`) åtgärdade; N5-meningen bär ingen normativ markör och ligger
  inte i `normative_sentences(PLAN_GEN)`; kollisionsmängden tom (regler.md har 15 normativa meningar, ≥ 8 krävs).
- Endast TVÅ pinnvärden ändrade (handoffen byte-identisk med f0b553d0): planens blob
  `8b234a8f951b41388f809561d443202011121986` (autopilot r.94 + selftest r.2604) och `PLATFORM_DOCUMENTS[plan]`
  `b2a0c150…35e5` (verify/cli r.86).
- Fullkörning: **127/0 rc 0**, 191,5 s, ingen riggskörhet (tom differens i /private/tmp/claude-501 före/efter).
- KONSEKVENS att hantera vid placeringen: `5df9213c` är SYSKON till `a288e169`, inte förfader. h-035-refreeze-
  kandidaten bär alltså den orättade plantexten. `verify/bin/h-035-exit` pinnar varken plan eller handoff ⇒
  ombasering är mekaniskt trivial, MEN den gröna h-035-mätningen (462/0) är gjord på a288e169 och måste köras om
  på den ombaserade commiten före placering. Hör till placeringen efter v3.11.
- Delta-granskning beställd hos samma granskare → `REVIEW-STATUSKORRIGERING-5df9213c-20260911.md`.

## STATUSRÄTTNINGEN INTEGRERAD — integrationshuvud 5df9213c (2026-09-11 sent)
- Delta-granskningen av 5df9213c: **READY**. Granskaren mätte varje ankare själv: `RED-etikett` 0 träffar i planen;
  strängen exakt 1 förekomst r.25407 i `forbidden`-listan r.25398–25409 under `r26_source_binding_accepts` r.25156;
  fältet i R30–R33 (r.8635/8805/9007/9266); `R33_REGISTRY_SHA256` r.1483 används BARA r.9268 ⇒ "i R33 bundet av"
  är exakt; R30/R31/R32 har egna konstanter r.1188/1344/1385; specen r.6791–6793 `depends_on: ["h-036"]`.
  N5-påståendet KÖRDES i stället för att läsas (runpy + grindens egna NORMATIVE_MARKER/visible_markdown/
  duplikatnormalisering): 104 normativa meningar, 0 kollisioner, regler.md 15 (≥8), N5-meningen marker=None.
  Egen fullkörning 127/0 rc 0, 191,50 s, ingen riggskörhet.
- **INTEGRERAT:** fast-forward 65830a2f → f0b553d0 → **5df9213c** i `~/nortropic-repos/nortropic-system`,
  143 filer, rent arbetsträd. Planens fyra lägen, tvingande ompinningsordning, H039 i kvarvarande väg med rätt
  mekanism, lokal milstolpe ≠ operativ överlämning, och handoffens startordning som dirigerar till bootstrap-
  kedjan före skivtabellen — allt nu i repot.
- **NÄSTA (pågår):** v3.11 av separationsgrinden i `~/nortropic-repos/work/test-author-separation-v311-20260911`
  (gren `nortropic/separation-v311`, från 5df9213c). Uppdrag: ersätt den generella byte-frysningen av `verify/`
  med (a) exakt sökvägsmängd, (b) byte-frysning utom DEKLARERADE omfrysningar, (c) deklarationen måste namnge
  grind + basens sha256 + ny sha256, och (d) en deklarerad omfrysning måste vara KVALIFICERAD, inte bara
  deklarerad. De tre hållna grindarna får inte ändras — bara separationsgrindens F7-förväntningar på dem, och de
  ska förbli EXAKTA. Dessutom: åtgärda riggskörheten i `f4_live_flows_…` (främmande temp-kataloger under
  /private/tmp/claude-501 gav falskt rött två gånger) med bevarad förmåga att fånga produktens egna sidoeffekter.
  Avgörande prov: den ombaserade h-035-kandidaten `a288e169` måste bli GRÖN under v3.11.

## Kontrakt v3.11 fryst (2026-09-12) → grindgranskning
TA-klon `~/nortropic-repos/work/test-author-separation-v311-20260911`, gren `nortropic/separation-v311`:
`a1e37b67` (grind + kriterier, parent 5df9213c) → `00f84d0e` (utfall). Grind sha256 `3bdc0ce2…`, 3932 rader,
**131 rader** (v3.10: 127). Acceptanskandidat bevarad som `refs/test-author/v311-acceptance-fixture` = `89ec9ddb`.
- Raddiff: 1 borttagen (`f6_frozen_evidence_identical_…` delas), 5 nya (sökvägsmängd; bytes utom deklarerat;
  deklarationen = EXAKT EN ordnad H-grind `^verify/bin/h-0NN-exit$` med bas-/ny-sha256 + mode 755 + motivering;
  tokenskanning av refreezens TILLAGDA rader; kvitto bundet till kandidat + bytes), 3 omdöpta F7-rader (namnen
  kodade radantal som refreezen ändrar), 2 ändrade (f8 + riggfixen), 88 oförändrade.
- Kvalificeringsdesign: deklaration i spårad `SEPARATION-20260910/REFREEZE.json`; kvitto lämnas VID KÖRNINGEN
  (`--refreeze-receipt`), aldrig ur trädet — grinden räknar om sha256(stdout), räknar PASS/FAIL, kräver
  gate_sha256 == deklarationens new_sha256 == kandidatens bytes, subject_head == denna commit, exit 0, noll FAIL,
  PASS-antal == förutsagt, kanonisk invokation. **Deklarerad gräns: kvittot bevisar inte att körningen ägde rum.**
  Skäl att inte köra nästlat: varje H-grind har egen rigg (h-035 ~450 s, sju bevarade kandidater, bare-origin,
  git-config-vitlista, processtabell) — dyrt och sprött att baka in.
- Mätt: grön baslinje på oförändrad integration **131/131** (hållna 68/68, 19/20, 68/2 = identiskt med v3.10).
  **Acceptans: h-035-refreezen rebasad (89ec9ddb) → separationsgrinden 131/131** med hållna grindar 67/1, 19/20,
  67/3; den omfrysta h-035 själv 462/0 exit 0. Negativer **16/16 fångade**, 0 riggfel. F7-förväntningarnas
  exakthet: grindens tre domarfunktioner mot inspelade+syntetiserade utfall 13/13.
- Riggfixen: svepet jämför inte längre /private/tmp{,/claude,/claude-501}, $TMPDIR och dess förälder, utan exakt
  det grinden själv skapat. Falskt-rött-prov med främmande process som skapar/tar bort filer i alla fem tidigare
  svepta kataloger → båda sidoeffektsraderna GRÖNA; produktmutant med marker i cwd fångas fortfarande.
- Deklarerade gränser: (1) kvittot bevisar inte körningen; (2) refreezens INNEHÅLL bedöms inte (H-grindens eget
  flöde äger det); (3) svepet fångar inte hårdkodad absolut skrivning utanför grindens rötter; (4) tre
  retirement-identifierare undantagna i skanningen av tillagda rader (`docs/05-beslutslogg`, `beslutslogg\w*`,
  `human_only`) — `konstitution\w*` och `regelverk\w*` fångas fortfarande.
- Riggnot: TA:s egen förgranskning importerade grinden utan `-B` → `verify/bin/__pycache__` gav 130/1 på
  launch-cwd-raden. Raden fångade det korrekt. Regeln "-B alltid" gäller även förgranskningsskript.
- Evidens: `~/nortropic/evidence/separation-v311-20260912/` (kvitto, båda result.json, h-035 stdout,
  negativ-/probeloggar, RECONSTRUCT.md, SHA256SUMS).
- Granskning startad i `~/nortropic-repos/work/gate-review-separation-v311` @ 00f84d0e. CENTRAL FRÅGA till
  granskaren: håller kvitto-designen mot ägarbeslutets Trust Kernel-kriterium, kan en BUILDER påverka kvittot,
  och finns ett billigare ärligt alternativ (nonce som den omfrysta grinden måste eka, transkript-hashkedja,
  strukturell omhärledning av en delmängd)?

## Grindgranskning av v3.11 (00f84d0e) = NOT_READY, två blockerare → v3.12 beställd (2026-09-12)
- **B1 AVGÖRANDE:** v3.11:s enda innehållskrav på en omfryst H-grind är parsar + `expected_pass >= 20` + grön.
  Granskaren ersatte `verify/bin/h-035-exit` (22 405 rader, 462 rader-i-utfall) med en FEMRADIG leksaksgrind som
  skriver 25 PASS, körde den ÄRLIGT (exit 0, 25 PASS), byggde kvittot ur den VERKLIGA stdout:en → separationsgrinden
  `rc=0, 131/131`. Inget fabricerat. Kriteriet faller alltså mot en ÄRLIG kvalificerare, vilket är precis vad
  ägarbeslutets "exitkod 0 ensam räcker inte" förbjuder. Åtgärd (mätt av granskaren): per-grind-golv härlett ur
  BASGRINDENS frysta bytes — 227 radetikett-literaler för h-035, 0 saknas i det ärliga kvittot, leksaksgrinden faller.
  Beställt: golvet härleds MEKANISKT ur basobjektet (gäller även h-036/037/038 utan ny runda), med möjlighet att
  DEKLARERA pensionerade etiketter med motivering och ett motiverat tak.
- **B2:** grinden påstår r.3595–3596 att kvittot aldrig kan komma ur trädet, men ett OSPÅRAT kvitto i subjektets
  arbetsträd krediteras (126/5). Verkställ påståendet eller skriv om det.
- Centrala frågan besvarad: (a) delvis ja → B2; spårade kvitton är självuteslutande, ingen miljövariabel läses.
  (b) tilliten håller inte — men inte p.g.a. fabricering, utan för att kriteriet faller mot en ärlig kvalificerare.
  (b′) fabricerat kvitto (subject_head lappat på annan kandidats körning) = ACCEPTABEL deklarerad gräns under
  hotmodellen. (c) nonce-eko/nästlad körning med rätta avfärdat; **strukturell omhärledning avfärdades för snabbt**
  och är billig — det är B1:s åtgärd.
- Håller: båda avgörande körningarna reproducerade med BYTE-IDENTISK stdout (baslinje 131/131; acceptans 89ec9ddb
  131/131, hållna 67/1, 19/20, 67/3). Raddiffen mekaniskt bekräftad (TA:s tabell stämmer; granskarens uppdrag angav
  fel antal ändrade rader — mitt fel i instruktionen, 3 inte 2). 8/8 av TA:s negativer rekonstruerade faller rätt.
  F7-domarna exakta (avvikande hållen-grind-effekt → 128/3). Inget v3.10-band försvagat. Riggfixen immun mot
  främmande sessioner (`snapshot_names` borttagen).
- Icke-blockerande (11), varav två tas med i v3.12: retirement-undantagen bredare än mätningen (styrningsprosa och
  aktivt `human_only`-stopp kan smugglas — når ingen agent); **v3.11 låser upp EN grind per generation, h-036/037/038
  kräver ompinnad `FROZEN_BASE` — ODOKUMENTERAT**, ska in i utvecklingsdokumentet med hur ombasering görs.

## Kontrakt v3.12 fryst (2026-09-12) → grindgranskning
TA: `09f0ea6d` (grind + kriterier, parent 00f84d0e) → `570def4c` (utfall). Grind sha256 `c501e8fc…`, 4076 rader,
**132 rader** (131). Acceptansfixtur `refs/test-author/v312-acceptance-fixture` = `61adaf6c`.
- **B1 åtgärdad med per-grind-golv:** `gate_row_labels(source)` AST-parsar och returnerar strängkonstanter som är
  POSITIONSARGUMENT till ett anrop vid namn `check` och matchar `[A-Za-z][A-Za-z0-9_]*`. Körs på BASVERSIONEN
  (`332f07ce:<sökväg>`) och på kandidaten — ingen handskriven lista, gäller hela den tvingande ordningen.
  Mätt på basen: **h-035 251, h-036 27, h-037 21, h-038 9**. Krav: varje basetikett kvar utom deklarerade
  pensioneringar; pensionering måste finnas i basen, saknas i omfrysningen, ha ≥20 teckens motivering, **högst tre**;
  `expected_pass >= basetiketter − pensioneringar`; fail-closed under 5 härledbara basetiketter;
  `REFREEZE_MIN_PASS` borttagen. Verkliga h-035-omfrysningen pensionerar EN.
  **Statiskt, inte täckning** — 70 av 251 basetiketter finns i källan men emitterades inte i den ärliga körningen
  (grenberoende); en kvittotäckningsregel hade gett falskt rött på en korrekt omfrysning.
- **B2:** kvittosökväg vars `resolve()` ligger i/under subjektet avvisas (spårad som ospårad); utsagan omskriven.
- **N1:** de tre retirement-identifierarna undantas bara på rader som bär en retirement-BUNDEN strängkonstant
  (tilldelad `(?i)retired`-namn eller dict-nyckel som namnger en pensionering). Mätt: 5 träffar på 3 rader, alla
  bundna → 0 röda. **N3:** dokumenterat att en generation rymmer EXAKT EN omfrysning + hur `FROZEN_BASE` ompinnas
  för h-036/037/038 (de hållna grindarnas baser ompinnas inte).
- Mätt: grön baslinje `09f0ea6d` **132/132** (hållna 68/68, 19/20, 68/2 = v3.10:s stränghet intakt). Acceptans
  `61adaf6c`: omfrysta h-035 **462/0** separat kvalificerad, kvitto `bff8cf1e…`; separationsgrinden **132/132**
  (hållna 67/1, 19/20, 67/3). **Negativer 26 fall: 24 fångade, 2 falskt-röda prov gröna, 0 riggfel** — inkl.
  `n17_toy_gate_honestly_run` som faller på ENBART den nya raden med "251 base row label(s) dropped without a
  declared retirement". F7-domarnas exakthet omkörd: 13/13.
- **TA-notering värd att minnas:** kontraktet fångade sin EGEN första fixtur (`4a9882f6`) på
  `f2_tree_wide_no_web_governance_reference_outside_frozen_evidence`, eftersom `REFREEZE.json` är aktiv spårad text
  och motiveringen namngav det retirerade dokumentet. Motiveringen omskriven; v3.11:s fixtur 89ec9ddb gäller inte
  längre (v3.12 kräver den deklarerade pensioneringen) och h-035 kördes om från grunden.
- Deklarerade gränser: innehållet bedöms till FORM, inte mening (behållen etikett med tömd kropp fångas inte) ·
  kvittot bevisar inte körningen · kvittots miljö obunden · lappad subject_head · TypeError faller stängt ·
  REFREEZE_GATE_RE bredare än ordnade mängden · hårdkodade absoluta sökvägar · gate_ok självrefererande.
- Granskning startad i `~/nortropic-repos/work/gate-review-separation-v312` @ 570def4c. Huvudfråga: är "form, inte
  mening" en acceptabel deklarerad gräns under hotmodellen, eller återöppnar den B1 (t.ex. leksaksgrind som
  mekaniskt kopierar alla 251 etiketter med triviala kroppar)?

## v3.12 GODKÄND OCH INTEGRERAD — integrationshuvud 570def4c (2026-09-12)
- Grindgranskning av v3.12: **READY**, inga blockerande fynd, tio icke-blockerande. Båda blockerarna från förra
  rundan åtgärdade och håller vid falsifiering: leksaksgrinden faller nu på ENBART den nya raden (126/6,
  "251 base row label(s) dropped" + "expected_pass 25 below the per-gate floor 251"); ospårat kvitto avvisas, och
  även symlänk utifrån in i subjektet (subject `.resolve()`:as före jämförelsen).
- **Verdikt på "form, inte mening": ACCEPTABEL deklarerad gräns.** Granskaren mätte hålet i värsta realistiska form
  (X3C: den VERKLIGA 22 511-raders h-035 med tre högvärdiga kontroller, bl.a. `F_BUILDER_CANNOT_EDIT_GATE`, ersatta
  med `True`, ärlig 462/0 → grinden grön). Skäl att ändå inte fälla: (1) superset-regeln hade gett FALSKT RÖTT —
  71 av 251 basetiketter emitteras aldrig och 281 av 462 emitterade är inte statiskt härledbara; (2) fyra prövade
  skärpningar stänger inte hålet utan falskt rött; (3) hotmodellens OAVSIKTLIGA arm är helt stängd och dokumentet
  lägger avsiktligt sabotage på rollflödet; (4) handlingen är deklarerad, spårad, motiverad och takbegränsad till
  tre namngivna pensioneringar. Artskillnad mot v3.11 där hela grinden fick bytas mot fem rader.
- Verifierat genom körning: grön baslinje 132/132 med stdout IDENTISK rad för rad med TA:s evidens; acceptans
  61adaf6c 132/132 (hållna 67/1, 19/1, 67/3), `label_counts base 251, refrozen 251, retired 1, floor 250,
  missing 0`, kvitto 462/0. Basetiketter med grindens egen funktion: h-035 251, h-036 27, h-037 21, h-038 9 —
  exakt TA:s tal; h-001…h-032 är shell → fail-closed. Raddiff 131→132, en tillagd rad. 6 v3.11- och 3
  v3.10-negativer faller rätt.
- Viktigaste icke-blockerande: N1 retirement-undantaget kringgås med två rader (`RETIRED_HUMAN_KEY = "human_only"`);
  N2 per-rad-skanningen tappar träffar över radbrytning som v3.11 fångade; N3 kvittots PASS-etiketter obundna från
  grindens (döda etiketter + utfyllnad går igenom; billig komplettering mätt: 181/251 emitteras ärligt); N6
  dokumentdrift ("expected_pass ≥ 20" står kvar).
- **INTEGRERAT:** fast-forward 5df9213c → a1e37b6 → 00f84d0 → 09f0ea6d → **570def4c**, 143 filer, rent arbetsträd.
  Grind sha256 `c501e8fc…`. **Orkestratorns egen kvalificering på integrationshuvudet: exit 0, 132 PASS / 0 FAIL,
  PASS_LOCAL_QUALIFICATION_ONLY.**
- **LUCKA I ROLLFLÖDET SOM NU STÄNGS:** omfrysningens INNEHÅLL (de ändrade konstanterna i h-035) har aldrig
  falsifierats oberoende — de två senaste granskningarna prövade separationskontraktet, inte omfrysningen.
  Oberoende granskning startad i `~/nortropic-repos/work/review-h035-refreeze-20260912` @ 61adaf6c →
  `GATE-REVIEW-H035-REFREEZE-61adaf6c-20260912.md`. Uppdrag: strukturell diff bas→omfryst (22405→22511 rader), att
  varje ändring ligger inom de TRE tillåtna ämnena, bevarandeaudit (R29/R33, H034_V3, H035_R15_BASE, R26_SUCCESSOR,
  19 evidenssökvägar, interpreterpinnen), golvet med egen AST-extraktion, ≥10 egna negativer, och den avgörande
  klassen: något som omfrysningen accepterar men BASGRINDEN avvisade.

## Ägarinstruktion 2026-09-12 (morgon): sökregel, produkttyngdpunkt, kedjeplan
Kontroll före ändringar: integrationshuvud `570def4c`, rent arbetsträd, inga grindkörningar igång, 20 GiB fritt.
En agent arbetar (oberoende granskning av h-035-omfrysningens INNEHÅLL, startad 31 min tidigare) → inga samtidiga
fullkörningar startas.

**STÅENDE REGEL (ny, gäller alla rollagenter):** sök alltid lokalt innan något bokförs som saknat. En fil, ett
objekt, en produkt eller ett bevis som inte finns i arbetsträdet är INTE därmed obefintligt. Sök i git-historiken
vid tidigare commits, i bevarade referenser och kandidatreferenser, i webbrepot där material överfördes med
proveniens, i den orörda ursprungliga arbetskopian `~/nortropic`, och i backupen med dess 37 buntar och externa
arkiv. REDOVISA var det söktes. Först efter den genomgången är "saknas" en MÄTNING i stället för ett antagande.
Regeln har redan gett utfall tre gånger: den gamla planens krav för nio obyggda skivor, de sju bevarade
kandidaterna h-035 behöver, och h-032:s produkt bankad i forensikmaterialet.

**ABSOLUT KRAV (förtydligat):** att HITTA är inte att ÅTERINFÖRA. Webbmaterial får aldrig tillbaka i plattformen.
Ett fynd avgör vad filen var och om en pinnad hash någonsin var uppfyllbar — inte att filen ska tillbaka. Aldrig
verifierarsviter, fixturer eller andra webbartefakter tillbaka i trädet. Formen är den h-035-omfrysningen redan
använder: historiska bytes bundna som GIT-OBJEKT vid en historisk commit + krav på att sökvägen är FRÅNVARANDE ur
trädet. Historiken bevaras, den aktiva auktoriteten flyttas inte tillbaka.

**ORKESTRATORNS RUTIN (ny):** verifiera varje ankare som förs vidare i en instruktion, med radnummer, innan det
skickas till en rollagent. Granskningen ska vara andra försvarslinjen, inte den första. (Infört efter att mitt eget
felaktiga "RED-etikett"-ankare ärvdes ned i produkttexten och fick fällas av granskningen.)

**Verifierade ankare för kedjeplanen:** `FROZEN_BASE = "332f07ceb914a07c6632c1393969d9d5a337566b"` i
`verify/bin/platform-separation-final-exit:65`; ombaseringsproceduren i
`docs/loop/platform-separation-final-local-development.md:715–724`, som också slår fast att `CONTROL_SET_BASE`,
`LAUNCH_CWD_BASE` och `GOVERNANCE_BASE` INTE ompinnas (r.723–724).

**Kedjeplanen skriven:** `~/nortropic/PLAN-OMFRYSNINGSKEDJAN-20260912.md` (kopia i backupens reports/). Ordnad
följd: h-035-placering → v3.13 (ombasa FROZEN_BASE) → h-037 (eller historiskt avslut) → v3.14 + h-036 → v3.15 +
h-038, plus h-039:s bindning som blir inaktuell så snart h-035 ändras. Varje ombasering är en REN kontraktsrunda
utan ny semantik; granskningen ska pröva just att ingen semantik smugglats in under ombaseringens täckmantel.

**Produkttyngdpunkten vriden:** h-032:s resultatkärna startas parallellt med kedjan (ej blockerad av den; h-031:s
normala godkännande väntar på den produkten). Produkten ÅTERVINNS ur bevarat material, skrivs inte om. h-038:s
produkt startas INTE nu (h-039 förbjuder h-038 att gå framåt före full PASS).
OVERIFIERAT som måste mätas innan h-032 startas på allvar: `verify/bin/h-032-exit` AST-läser autopiloten, som
ändrats två gånger sedan h-032 kvalificerades. Faller grinden på generationen behöver även h-032 en omfrysning och
då gäller en-per-generation-regeln även den. Mätningen köas efter att granskningen släppt fullkörningsvägen.

**Pågår:** lokal sökning enligt stående regeln för (1) h-037:s svit `workflows/nortropic-verify-suite.js` och
`tests/fixtures` — vad de var, om pinnarna `ac1e21d1`/`7c02f12e`/`d77af8aa` någonsin var uppfyllbara, om innehållet
var webbspecifikt eller plattformsgeneriskt; och (2) h-032:s produkt `controller/result/**` — alla kopior, den mest
kompletta, gränserna i specraden, vad h-032-exit kräver, och om någon kopia är webbkopplad.

## Lokal genomsökning gav tre avgörande fynd (2026-09-12) — `~/nortropic/BESLUT-H037-OCH-H039-20260912.md`
Genomsökta platser redovisade: plattformsrepot (`git log --all`, refs/preserved/**, refs/candidates/**, cat-file
vid 139d3c7c/c296566f/42c20b30/13e8a903/dae90c8f/49cc495c/332f07ce), webbrepot med båda proveniens-TSV:erna, den
orörda arbetskopian `~/nortropic` (18 träd med controller/result, evidence/**, forensics-h036-20260827), backupens
37 buntar + external/ + reports/ (listat; allt som behövdes fanns i de tre första).

**FYND 1 — h-037 ÄR REDAN BYGGD OCH PUBLICERAD.** Verifierat AV MIG: `ee84b206a5fc755e0c708153559da6c4ec8df55e`
är förfader till HEAD, rörde ENDAST `controller/verify/register.json`, och flyttade registrets sha256
`c99f3b37…` → `a87869be…` = exakt grindens `PRE_REGISTER_SHA` (h-037-exit:45) → `POST_REGISTER_SHA` (:46).
Kontraktets preprodukttillstånd var verkligt: alla åtta pinnar stämde vid `139d3c7c`. Sviten fanns
(`ac1e21d1` = blob 4be58489 vid `0a677d8f`; `7c02f12e` = blob c3824981 vid `42c20b30`; `FIXTURES_TREE d77af8aa`
= tests/fixtures-trädet vid `c296566f`), togs bort i separationscommiten `49cc495c` och ligger i webbrepot med
proveniens (PROVENIENS.tsv r.323 resp. r.140–147, klass WEB/WEB_MOVE). Sviten var WEBBSPECIFIK (konstitutionens
§A6/§B6, planmallar, eval-rubriker, designblocklist, Vercel-preview) — ingen plattformsgenerisk kärna att
återanvända. **BESLUT: raden avslutas som historiskt genomförd, ingen ny mening uppfinns, sviten återinförs
aldrig.** Formen vid omfrysningen blir h-035:s: historiska bytes bundna som git-objekt vid `0a677d8f`,
`42c20b30` och `c296566f`, med samtidigt krav på FRÅNVARO ur trädet. Grindfilen ligger kvar (sökvägsmängden är
fryst + PINV-001 kräver spårad exit_test). Alla 21 etiketter bevaras → ingen pensionering (taket är tre).

**FYND 2 — h-032:s produkt finns bevarad och är webbFRI.** Mest komplett och enda oberoende granskade kopian:
`49af17a9c5f98775ef633b852cbfc19adb7dc2e1` (tree b0e075aa, ref `refs/preserved/old-checkout/heads/builder/
h032-product-mode-r4-ff09e3c4`), granskad i `~/nortropic/H032-49AF17A-INDEPENDENT-REVIEW.md`:
PRODUCT_REVIEW=READY_FOR_OWNER_GATE, ADVERSARIAL=PASS, IDENTITY=PASS, BLOCKING=NONE, delta 6 filer/2 164 rader
(taket är 12/2 200). Ta verbatim: `consumer.py` (f51dd6d4…, 199 rader) och `materialize.py` (f811022f…, 373 rader)
— byteidentiska i 11 diskträd + forensikbanken + caab2e4f. Utelämna `routing_ast.py` (dev-hjälpare),
`controller/launch/cli` (H-036 äger den), och 491-raders `materialize.py` (2e8e5028, test-author-referens).
**Webbkoppling: NOLL träffar** i samtliga blobbar och 18 träd på docs/05|docs/07|konstitution|fixtur|verify-suite|
vercel|rorjour|webb|workflows. Den enda webbkopplingen ligger i SPECRADENS `allowed_write` (`docs/05-beslutslogg.md`,
filen finns inte) och i grindens historiska referenser — inte i produkten. Autopilotdeltat måste portas OM mot
HEAD-autopiloten (`2976aa33…`), inte mot det granskade `fd9303ee`/`73c07ed6` — autopiloten har bytt TRE gånger.

**FYND 3 — NYTT MÄTT HINDER: skalgrindar kan inte frysas om under v3.12.** `verify/bin/h-032-exit` är
`/bin/bash`; kontraktets `gate_row_labels()` kör `ast.parse` → `SyntaxError` → anroparen lägger till
"row labels not derivable" → `f6_refreeze_keeps_every_base_row_label…` blir RÖD. h-035/036/037/038 är Python och
berörs inte. Hindret aktiveras ENDAST om h-032 behöver en omfrysning — OVERIFIERAT tills mätt körning gjorts.

**BESLUT 2 — h-039 och produktions-origin** skrivs in rakt ut i planen (h-039 kräver `PRODUCTION_ORIGIN`, är inte
fullt kvalificerbar lokalt, `--r33-installed`-lanen hör till den senare operativa överlämningen; bindningen
ompinnas ändå i kedjan). Texten rider med nästa kontraktsrunda eftersom planändringar flyttar pinnade värden.

**NÄSTA HANDLING (köad, kräver fri fullkörningsväg):** mätt körning av `verify/bin/h-032-exit` mot
produktfrånvarande HEAD `570def4c` för att fastställa verklig RED-baslinje och avgöra om h-032 bara saknar produkt
(→ bygg) eller också driftat mot generationen (→ omfrysning, som då blockeras av FYND 3). Referensplanens siffror
148/4 och 152/0 är från e71dfbbd-generationen och gäller INTE HEAD.

## h-035-OMFRYSNINGEN GRANSKAD OCH PLACERAD — integrationshuvud e6e4091 (2026-09-12)
**Granskning av omfrysningens INNEHÅLL: READY** (`~/nortropic/GATE-REVIEW-H035-REFREEZE-61adaf6c-20260912.md`,
453 rader). Domen: omlokalisering med DISJUNKTA acceptansmängder, inte "pinna om tills grön".
- Granskarens egna körningar: omfryst grind 462/0 rc 0; **basgrinden på samma kandidat 459/3** med exakt de tre
  namngivna raderna och inga andra. Båda emitterar 462 unika rader; enda skillnaden i etikettmängden är
  ett-mot-ett-bytet av den deklarerade pensioneringen.
- Strukturell diff: 5 hunkar, +138/−32; AST: 3 tillagda konstanter, 0 borttagna, 1 ändrad
  (`H035_R13_FROZEN_AUTHORITY`), 2 ändrade funktioner, 0 ändrade signaturer. **Noll scope creep, noll
  försvagningar, en skärpning.** Alla 12 ändrade enheter tabellerade med dom.
- De tre påståendena verifierade: (1) `allowed_write` 23→22 och `docs_impact` 6→5, borttagen post ENBART
  `docs/05-beslutslogg.md`, övriga sju fält identiska, kontrollen fortfarande `exact_value`; (2) transformbasen
  `c161a1c5` oförändrad och läses som Git-objekt, alla SEX pinnar omräknade oberoende ur verkliga artefakter;
  (3) omlokaliseringen bekräftad — 35d7fd7c-bytes hashar till `d6fb0159…`, de två kvarvarande dokumenten binds
  HÅRDARE (hel-fil-sha256), återinförande avvisas som fil/katalog/symlänk/hängande symlänk.
- Golvet reproducerat med v3.12:s egen `gate_row_labels`: 251 bas, 250 golv, 0 saknade. **"Form utan mening"
  exploateras INTE här**: av 250 behållna etiketter har exakt en ändrad kropp, och den blev STARKARE.
- **61 egna negativer, 61 fångade, 6 riggkontroller gröna, 0 riggfel.** Avgörande: `n18` rekonstruerade hela den
  för-uppdelade generationen → 458/4, röd på alla tre raderna. Acceptansmängderna är parvis disjunkta.
- Icke-blockerande NB-1…NB-7. Viktigast: **NB-6** — `h-036-exit` (r.147/912) och `h-039-exit` (r.1948/6283) pinnar
  basens sha256 `76d3bf10…` och blir RÖDA efter denna omfrysning; planerat och namngivet i planen r.183–185.
  **NB-7** — commiten ändrar TVÅ filer, inte dev-docen.

**PLACERAD av orkestratorn.** `61adaf6c` var syskon till `570def4c` (båda barn till `09f0ea6d`) → cherry-pick på
integrationshuvudet gav **`e6e4091c991ccbcaf9b7bab923a4e1e803453290`** (2 filer: `SEPARATION-20260910/REFREEZE.json`
tillagd, `verify/bin/h-035-exit` ändrad, +151/−30). Egna kvalificeringar på den OMBASERADE commiten:
- refryst `verify/bin/h-035-exit` (sha256 `91aa7fe7…`): **exit 0, 462 PASS / 0 FAIL**, `H035_GATE_RESULT=PASS`
- `platform-separation-final-exit` v3.12 med kvitto: **exit 0, 132 PASS / 0 FAIL**,
  `PASS_LOCAL_QUALIFICATION_ONLY`
Kvittot byggdes ur den VERKLIGA utskriften, `subject_head=e6e4091…`, och låg utanför subjektet (kontrollerat).
Fast-forward 570def4c → **e6e4091**, 144 spårade filer, rent arbetsträd.
Evidens: `~/nortropic/evidence/h035-placement-20260912/` (kvitto, h-035 stdout, separationskörningen, SHA256SUMS).
Temprötter borttagna; bare-origin kvar som `~/nortropic/worktrees/h035-placement-origin.git`.

**KEDJANS LÄGE:** steg 1 klart. Nästa: **v3.13** — ombasera `FROZEN_BASE` från `332f07ce` till `e6e4091`, döp om
`f6_*`-radnamnen (de bär basens åtta första tecken), mät om `f2_local_development_documents_…` och
`f1_web_transfer_provenance_2_…`, kör grön baslinje + acceptans för h-036. FÖRVÄNTAT efter denna placering:
h-036-exit och h-039-exit är nu röda på basens h-035-sha (NB-6) — det är planerat, inte en regression.

## h-032-MÄTNINGEN UTFÖRD — utfallet ändrar bilden (2026-09-12)
Körning mot produktfrånvarande integrationshuvud `e6e4091`, kanonisk miljö, fri fullkörningsväg:
`/bin/bash -p verify/bin/h-032-exit` → **EXIT=2, 0 PASS, 0 FAIL, `ODÖMBART K-RIGG — RuntimeError: candidate
controller early capability inventory`**. Evidens: `~/nortropic/evidence/h032-measure-20260912/`.

**Detta är INTE en RED-baslinje.** Grinden avger ingen produktdom alls. Felet reses på `verify/bin/h-032-exit:1471`
efter att grinden extraherat sitt eget frysta predikat `r123_controller_native_source_ok` ur sin AST (r.1450–1470)
och kört det mot kandidatens controller-källa (bytes lästa r.1442). Predikatet avvisar källan.
Mätt delfakta: autopilotens toppnivåimporter vid HEAD har **inga dubblettbindningar** (13 importer), så avslaget
ligger i en annan konjunkt i predikatet — **exakt vilken är OVERIFIERAT** och kräver en riktad diagnos.

**Konsekvens för ägarens parallellspår.** Instruktionen var att starta h-032:s produktarbete parallellt med
omfrysningskedjan, eftersom h-032 inte är blockerad av den. Mätningen visar att h-032 ÄR blockerad, men av något
annat: grinden kan inte döma på denna generation. Kedjan blir därmed:
1. diagnos av vilken konjunkt i `r123_controller_native_source_ok` som avvisar kandidatens controller-källa;
2. om det är generationsdrift → **h-032-exit måste frysas om** för att bli dömbar;
3. men en omfrysning av h-032-exit är **mekaniskt omöjlig under kontrakt v3.12**: grinden är ett `/bin/bash`-skript,
   `gate_row_labels()` kör `ast.parse` → `SyntaxError` → `f6_refreeze_keeps_every_base_row_label…` blir RÖD.
   Kontraktet måste alltså utökas att hantera skalgrindar innan h-032 kan röra sig.
Produktåtervinningen (kopian `49af17a9`, byteidentiska filer, noll webbkoppling) är oförändrat giltig — men den kan
inte kvalificeras förrän grinden är dömbar. **Starta därför inte builderarbetet för h-032 ännu.**

**Nästa handling blir därmed två spår, båda tydliga:**
(a) riktad diagnos av h-032:s riggfel (read-only, ingen fullkörning krävs — predikatet kan köras isolerat mot
    kandidatens källa precis som grinden gör det);
(b) v3.13: ombasera `FROZEN_BASE` `332f07ce` → `e6e4091`, döp om `f6_*`-radnamnen, mät om
    `f2_local_development_documents_…` och `f1_web_transfer_provenance_2_…`, kör grön baslinje + acceptans för
    h-036. Efter h-035-placeringen är h-036-exit och h-039-exit röda på basens h-035-sha — planerat (NB-6).

## Codex återupptagning — exakt första h-032-avvisning (2026-09-12)

Användaren återupptog arbetet enligt plan efter avstämning om slutkriterier och bevarande.
Återanvändning gäller hela kernel-/bootstrap-/H-historiken: implementation, frysta prov,
recept, manifest, beslut, opublicerat arbete och evidens. Historisk kvalificering behåller
sitt ursprungliga subjekt; nya generationsbindningar måste prövas, inte ges ärvd credit.

**Lokal identitet återkontrollerad:** integrationen
`/Users/elinhaggstrom/nortropic-repos/nortropic-system`, gren
`nortropic/platform-integration-20260910`, HEAD
`e6e4091c991ccbcaf9b7bab923a4e1e803453290`, `git status --short` tom.
Konfigurerad origin är `git@github.com:Nortropic/nortropic-system.git`.
`git rev-parse origin/main` misslyckades: den lokala referensen finns inte.
**ORIGIN_MAIN=OVERIFIERAT**; ingen nätverkskontroll gjord och ingen publicerad bas antagen.

**Diagnos utförd, inte full grindkörning:**

```sh
/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/h032-source-diagnosis-20260912.HuKTdM/diagnose.py
```

Exit 0 betyder att diagnosskriptet avslutades, inte H032 PASS. Skriptet extraherar
oförändrade `_R123_CONTROLLER_*`-konstanter och `r123_controller_native_source_ok`
från grindens Python-heredoc. Endast predikatet körs mot autopilotens källtext;
autopiloten importeras eller exekveras inte. En retur-observer registrerar det faktiska
avslaget utan att ändra predikatet eller dess tillåtna mängder.

- Grind-SHA256: `9281e7182c21ee5758e3e56c26e40d05bbe04f752d5e8da72a05fafa496dcf59`.
- Autopilot-SHA256: `2976aa33e82af15101c5f2b885ffa479e5892dd94ced0de6b78180b2be71c106`.
- Predikatet returnerar `false` vid **grindrad 14316**: första modulmedlemmen
  finns inte i `_R123_CONTROLLER_MODULE_FIRST_HOPS`.
- Faktiskt avvisad nod: **autopilotrad 2851**, `os.getcwd` i `parse_args()`.
  Nästa rad använder också `os.getcwd` för worktree-standardvärdet; den är inte ett
  separat observerat avslag eftersom predikatet redan returnerat.
- `git log -S 'os.getcwd'` och `git show` på
  `510f65339f1b24517ca4e120712024e3c8220857` visar övergången från fasta
  `Path.home()/nortropic/...` till arbetskatalogbaserade standardvärden.
- Grindens och produktkällans bytes var oförändrade efter diagnosen.

**Avgränsning:** första avvisningen är PROVEN; frånvaro av senare avvisningar är
OVERIFIERAT. Detta motiverar granskning av generationsdriften, inte en generell
vitlistning eller återinförande av gamla användarsökvägar. Full H032 är NOT_RUN i
denna återupptagning; tidigare rc2/0 PASS/0 FAIL behåller sin status. Ingen h-032-builder
har startats. v3.13 hanteras separat av TEST_AUTHOR och ska inte smuggla in skalgrindsstöd.

Bevarad körningsutskrift:
`evidence/h032-measure-20260912/isolated-predicate-diagnosis.json`, SHA256
`ff3d6cb20d04583f5d216de44acb5f6cdc175994503c0607c3f6a2faef204850`.
Bevarat diagnosskript i samma katalog: `isolated-predicate-diagnosis.py`, SHA256
`3711d44dedbc5bfdb39f699e8d714bee01e4bc99b2f08683328832b48ef5445e`.
Endast dessa två evidensfiler och detta kontinuitetstillägg skrevs av orkestratorn.
Ingen produkt, befintlig fryst grind, installation eller H039-WIP ändrades av diagnosen;
ingen cleanup, publicering eller supervisor-resume utfördes.

### v3.13 — avgränsad TEST_AUTHOR-arbetsyta öppnad (2026-09-12)

Read-only förkontroll visar att enbart `FROZEN_BASE`-literalbytet inte genomför
generationsövergången: F1 hämtar nu frånvarande överförda webbobjekt ur den basen;
F2 använder den som historisk gräns för aktiva dokumentnoter; F6 antar att den egna
grinden ännu inte finns i basen; F7 beräknar bara den nya deklarationens drift trots
att e6e4091 redan innehåller den kvalificerade H035-omfrysningen. Detta är ett
konkret hinder för den beslutade baslinjen, inte motiv för nya produktkrav.

TEST_AUTHOR förbereder därför endast generationsanpassningen i
`verify/bin/platform-separation-final-exit` och
`docs/loop/platform-separation-final-local-development.md`: historiska ankare och
scan-gränser bevaras, ny bytefrys binds till e6e4091, identisk ärvd deklaration
skiljs från en ny, och F7:s exakta förväntade drift härleds ur den fasta kvalificerade
basen plus högst en ny deklarerad omfrysning. Kandidatens godtyckliga drift får inte
bli sin egen tillåtna mängd. Ingen annan grind eller produkt tilldelas skrivning.
Detta är förberedelse för oberoende granskning, inte ett godkänt kontraktsutfall.

Orkestratorn skapade efter behörighetsprövning en ny isolerad lokal Git-arbetsyta:
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v313-20260912`,
gren `nortropic/loop-separation-v313`, HEAD
`e6e4091c991ccbcaf9b7bab923a4e1e803453290`, initial `git status --short` tom.
Konstruktion: exklusiv mkdir, `git init --template=`, lokal exakt-SHA-fetch från
integration, ny gren och enbart konfigurering av canonical origin-URL. Ingen
remote-observation eller nätverksfetch. Äldre arbetsytor och integration lämnades orörda.

v3.13 full baslinje, oberoende review och H036-acceptans: **NOT_RUN** vid denna notis.
H036-acceptans får inte ersättas av ett påhittat kvitto eller källformstest.
H032-diagnosens utskrift, skript och dåvarande checkpoint har kopierats som tre nya
filer till backupens befintliga `reports/`; `cmp` var tyst med exit 0 för kopiorna.
Äldre backupversioner skrevs inte över.

### Oberoende H032-diagnosgranskning (2026-09-12)

Rolltråden `h032_diagnosis_review` avslutade en egen read-only källgranskning och
isolerad in-memory-reproduktion med pinnad Python 3.12.13, `-I -S -B -`, exit 0.
Granskaren bekräftade samma `false` vid grindrad 14316/källrad 2851, exakt 11
konstanttilldelningar plus det oförändrade predikatet i extraktionen, och 22 unika
importinventarieposter exakt lika `_R123_CONTROLLER_LEGACY_IMPORTS`.
Granskaren verifierade de tre SHA256 ovan samt ren e6e4091 före/efter och fann
inga blockerande fel i den avgränsade diagnosen. Detta är granskarens
same-session-resultat, inte en ny full gatekörning eller runtimecredit.
Senare avslag, en tillräcklig rättning och H032-kvalificering är fortsatt
OVERIFIERAT/NOT_RUN; ingen tillåtelse att börja builder eller ändra vitlistan
följer av utlåtandet.

### v3.13 — patch applicerad efter ändrad sessionsåtkomst (2026-09-12)

Sessionsspärren för skrivning utanför den äldre roten hindrade TEST_AUTHOR:s första
apply_patch-anrop; det avbröts utan repofiländring. En redan väntande konstruktion
överlappade orkestratorns init/fetch av samma nya arbetsyta: init återinitialiserade
den och checkout av den redan befintliga grenen returnerade 128. Samma e6e4091-bas
och rent arbetsträd återkontrollerades; detta gav ingen testcredit och ingen ny bas.

Efter användarens ändring till full sessionsåtkomst och instruktionen ”Fortsätt
arbeta” applicerade orkestratorn TEST_AUTHOR:s oförändrade tvåfilspatch med
apply_patch. Patchkälla:
`/private/tmp/nortropic-v313-contract.Fq5ueV/candidate.patch`, SHA256
`e27f204b7dd1008c785f40f80cef137282e330f576fd6473771e08a9b789aac5`.
Arbetsytans diff är exakt två filer: grind +36/−27, utvecklingsdokument +52/−2.
`git diff --check` exit 0; inget stagat. Pinned Python `-I -S -B` med `ast.parse`
accepterade grindens källtext. Detta är syntax-/diffkontroll, inte kvalificering.

De tre hållna baserna kvarstår (`dae90c8f`, `383ed387`, `512490d4`);
`HISTORICAL_BASE=332f07ce`, `FROZEN_BASE=e6e4091`. TEST_AUTHOR fortsätter med
fokuserade prov i separat tillfällig yta. Ingen fullgate eller commit vid denna notis.
Integrationsrepots `git status --short` är tom. Den ändrade verktygsbehörigheten
utökar inte den lokala fasen till publicering, installation, live eller resume.

### v3.13 — lokal baslinje körd mot låst kandidat (2026-09-12)

Lokalt review-subjekt `531d37e594410d80d3d07975b8331715dd2508b0`, ensam parent
`e6e4091c991ccbcaf9b7bab923a4e1e803453290`, tree
`3608791e39988570357a360454113dd11f9bd5c6`. Normal lokal commit, HÖGRISK-märkt,
exakt de två ovan angivna TEST_AUTHOR-filerna +88/−29; inget annat ändrat.
Commitmeddelandets ”ej kvalificerat” anger läget vid frysningen, inte utfallet nedan.
Integration ligger kvar ren på e6e4091. `ORIGIN_MAIN=OVERIFIERAT`.

Körd full baslinje, en fullkörning på värden, exit **0**:

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v313-20260912/verify/bin/platform-separation-final-exit --subject /Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v313-20260912
```

Faktiskt slututfall: **132 unika PASS / 0 FAIL**, exakt
`PLATFORM_SEPARATION_FINAL_RESULT=PASS_LOCAL_QUALIFICATION_ONLY`.
`result.json` binder subject_head till 531d37e och frozen_base till e6e4091;
alla 132 rader är true. Resultatets subject-/held-hashar återkontrollerade mot disk;
rent kandidatworktree, tomt index, `git diff --check` exit 0. Övriga 142 spårade filer
är byte-/lägesidentiska med basen. Ingen produktfil ändrad, ingen H039-WIP öppnad för skrivning.

De oförändrade nästlade grindarna gav exakt generationsförväntad drift:
control-set rc1 67/1, launch-cwd rc1 19/1, governance rc1 67/3.
Det är inte självständiga gröna domar från dessa äldre grindar. V3.13 kontrollerade
deras exakta namngivna utfall och produktrader; extra fel var inte tillåtna.
Den ärvda deklarationen gav `refreeze_declaration=[]`, `refreeze_receipts=[]`:
**ingen ny H-grind fick omfrysningscredit** genom baslinjen.

Evidens i `evidence/v313-review-20260912/`:

- `baseline-531d37e.stdout`, SHA256
  `8d3e7d7fabe03a256771f956bbbb5c9056a8f3f14b8fd92824bc965632f08b04`.
- `baseline-531d37e.result.json`, byteidentisk kopia av grindens resultat, SHA256
  `4082f9bec782a8d6aaa8a62c1c72a2c4c0d69bce0d5d5b1518c624b1cadca0fe`.
- Ursprunglig körrot, bevarad:
  `/private/var/folders/_v/t4cy04w95gz3m782_3p5qs9h0000gn/T/platform-separation-final-nod9lgw4`.

Oberoende rolltråd `v313_gate_review`: READY i generationslinsen, inga blockerande
fynd efter 29 egna in-memory-prov och tre AST-jämförelser, provkommandon exit 0.
Ingen egen fullkörning av granskaren; READY ersätter inte fullbaslinjen ovan.
Granskaren prövade fel hash/läge, extra/borttagen fryst path, odeklarerad h037,
ärvd kontra ny deklaration, saknat/gammalt kvitto, extra nästlade fel och bortfallen
obligatorisk produkteffekt. Nya-deklarationens validering/golv/skan/kvitto är AST-identiska
med v3.12. Exakta prov och efterkontroll lämnas i samma evidensyta.

Verklig backup: `nortropic-backups-20260910/full-20260910T103342Z/bundles/v313-review-531d37e.bundle`,
SHA256 `a5120b6a0eca34b2b7e0fae2cd4087c75104a5ab776e9fedcd622ab34b7f1541`.
`git bundle verify` exit 0. Återställningsprov med ny tom Git-repo, fetch från just
bundlen och detached checkout i `/private/tmp/v313-bundle-restore.oPX4yV` gav
exakt 531d37e/3608791e, rent träd och samma två filhashar:
grind `41aa0393fcd03365920b9c19466d06826fbc4921f9594f6fc3d1f3cb75c0ed32`,
dokument `ca338c4815577ac3c12766572e096fe89ace10352824b46b87e57a76ee699595`.
Detta återställningsprov gäller denna kandidat, inte en ny verifiering av alla äldre arkiv.

**Återstår i D4:** verklig H036-acceptans är **NOT_RUN**. Den kräver avgränsad
omfrysning, oberoende granskning och samma-kandidat-kvalificering; syntetiska kvitton
eller baslinjens inherited-declaration-fall är inte ersättningar. Källavstämning av
konkreta H036-bindningar påbörjas inom TEST_AUTHOR, utan produkt-/H039-ändring.
H032:s första predikatavslag är fortsatt diagnostiserat men inte rättat; builder
för H032 startas inte. Inget push/merge, installation, root/live, cleanup eller resume.

#### Slutlig fokuserad granskning och evidenskopior

TEST_AUTHOR körde pinnad Python `-I -S -B
/private/tmp/nortropic-v313-contract.Fq5ueV/focused.py`: exit 0,
**27 förväntade utfall, 0 avvikelser** på 531d37e. Ingen kandidatändring.
Första provriggskörningens 26/1 är bevarad separat: dess sista kontroll förväntade
fortfarande ett smutsigt e6e4091-arbetsträd efter orkestratorns commit. Riggkontrollen
bands om till exakt 531d37e; kandidaten rättades inte och inget produktfel ursäktades.
Den första körningen ger ingen fullständig provcredit.

- `test-author-focused.py`: SHA256
  `9145ac414a80d48c34abdb7e5fcf0ea60547dd114e0363e849aba942629820ba`.
- `test-author-focused-531d37e.result.json`: SHA256
  `c3a9d03f58275d74ac793456b84901de1e31a0030d362d7bb1f76ad70974b190`.
- `test-author-focused-stale-rig.result.json`: bevarat första utfall, inte kandidatdom.
- `independent-review.md`: exakta oberoende provkommandon och slutlig read-only
  JSON-/identitetskontroll, SHA256
  `7b338eb4972ecca4532acb4a7d8371665fc0fce85b76b6f6a18c124ddde2af64`.

Filerna ovan ligger i samma `evidence/v313-review-20260912/`. Baslinjens stdout/resultat,
oberoende review och båda TEST_AUTHOR-utfallen samt provskript är kopierade till
backupens befintliga `reports/` med nya v313-filnamn, utan överskrivning av tidigare
evidens. Kopiorna är jämförda byte-/hashmässigt. Inga fler fullkörningar gjordes.

### H036 — konkret nästa kontraktssteg, ingen ny runtimeprodukt (2026-09-12)

TEST_AUTHOR:s avgränsade read-only helperprov rapporterar exit 0 med följande
diagnos, inte en H036-dom: `exact_config()` avvisar med `config product digest
mismatch`, och `product_phase()` kastar samma `Rig`. Helpern och configfilen är
oförändrade, men configens launcherpin avser äldre launcherbytes:

- nuvarande launcher: `5273a48480ec73550ddc915e9b2c54d396717573dd7af79fe89cbe549cf1d4f1`;
- configens förväntade launcher: `65571892948b9f7a9260ee88abb2cf5c575eda245fe1874f8ade3c7a8b202ba3`;
- helper: `35ca9dff3355bcfbd4d7536cb9658fe3342f143745547ec55f2b2cb25223eca7`;
- configfil: `460d4a89f2160ed947ed513bebc5e25de41899a9aabda613d0a233f2150ef963`.

Detta är en identifierad generations-/configbindning, inte bevis på att runtimekoden
är felaktig eller saknas. Befintlig launcher från den bevarade launch-cwd-kandidaten
ska återanvändas. H036:s egen taskform/hash och H032/H034/H037-taskhashar håller i
helperprovet; H035-taskhashen har däremot förändrats. H037:s aktuella grindhash matchar
H036-pinnen, så dessa kontroller kräver inte att H037 först skrivs om.

Orkestratorns källkontroll visar ytterligare två konkreta gränser:

1. `current_h034_identity()` jämför historiska objekt med vissa värden ur samma
   `PINNED_UNCHANGED` som dagens diskfiler kontrolleras mot. En generell repin av
   den gemensamma tabellen skulle kunna förstöra det historiska beviset. Den nya
   kontraktsriktningen måste skilja historisk och aktuell identitet.
2. Befintlig noarg-lane ger inte produktcredit; `--product` kräver ursprunglig
   tre-filsimplementation som direkt barn. Registry-lanen kräver H039-absens, medan
   dagens task/grind/produkt finns. Historisk absens får bevisas på det historiska
   subjektet men får inte beskrivas som dagens runtimekvalificering. Dessutom kräver
   separationskvittot att sista argv-elementets basnamn är grindnamnet: ett ärligt
   flaggbärande anrop ryms inte. Flaggan får inte utelämnas i bokföringen.

Nästa TEST_AUTHOR förbereder därför endast den minsta sammanhängande återkvalificerings-
och kvittovägen, med oförändrad produktkod och separat BUILDER för eventuell exakt
configpin-rättning efter kontraktsgranskning. Specens noarg-`exit_test` och dess
befintliga tre `owner_author_allowed_write` måste beaktas; en ny lokal sidolane
får inte presenteras som slutlig kvalificering av den egentliga taskvägen.
Specbloben är fortfarande fryst av separationsgrinden. Inget nytt generellt
undantag, ingen specändring eller pinändring har utförts genom denna notis.

Orkestratorn skapade exklusivt nästa isolerade arbetsyta genom lokal exakt-SHA-fetch:
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v314-h036-20260912`,
gren `nortropic/loop-separation-v314`, clean HEAD 531d37e/tree 3608791e.
**Inga filer i denna nya kandidat är ändrade ännu**. Första kontraktsförslaget
förbereds oapplicerat, för oberoende granskning; ingen H036-produktwrite eller fullgate.
V3.13 och integrationsrepot bevaras oförändrade. H036-acceptans är fortfarande NOT_RUN.

#### H036-förberedelsens faktiska stoppunkt och reproducerbar diagnos

Den oapplicerade utvecklingsdokumentspatchen blev **inte färdig**. Den längre
förberedelsen avslutades utan kandidatändring, och nästa arbetsyta är fortsatt ren
på 531d37e. Det finns ännu ingen v3.14-frys, inget nytt exit-test och ingen builder.
Detta är ofärdigt kontraktsarbete, inte ett nytt ägarstopp eller en färdig H036-leverans.

En separat kort oberoende källgranskning och TEST_AUTHOR landade i följande
arbetsriktning, **inte implementerat/fryst kontrakt**:

- överväg `--current-product CANDIDATE_SHA`, internt fixerat generationsankare
  531d37e, för att inte ändra historiska `--product BASE CANDIDATE`;
- kontrollera exakt commitobjekt, ren HEAD, objekt↔disk, lägen/hashar och kontraktets
  uttryckliga delta före oförändrade `subject_effects()`/`run_subject_matrix()`;
- skilj historiska H034/H036-objekt och dokument från aktuella identitetskontroller;
  ingen återinförd webbfil och ingen historisk PASS som dagens runtimecredit;
- TEST_AUTHOR förbereder H036-grind, separationsgrind och befintligt devdoc samt
  en enda deklarerad omfrysning; separat BUILDER begränsas till configens launcherpin,
  med launcher/helper oförändrade. Inget configundantag i F6 behövs;
- kvittots exakta argv måste binda Python, `-I -S -B`, rätt grind, den verkliga
  flaggan och kandidatargument lika `subject_head`; fel kandidat/hash/mode, dirty
  träd, extra delta, gammal configpin, historikkvitto och uteblivet/felande effektprov
  måste avvisas. Ingen godtycklig suffixlista eller maskerad kommandorad;
- noarg-vägran är befintligt produktfasbeteende. Lokal återkvalificering sluter inte
  automatiskt ordinarie task-/bootstrapvägen. Den kopplingen är fortsatt arbete inom
  kontraktsflödet, inte skäl att begära en generell fullmakt igen.

TEST_AUTHOR:s ursprungliga H036-helperkommando saknades i leveransen. Orkestratorn
gjorde därför en ny begränsad, reproducerbar read-only-körning, efter AST-kontroll av
grindens top-level-/default-/decorator-effekter. Grinden läses med `runpy` under annat
modulnamn; dess `main`, produktkod, `subject_effects` och runtimeprov körs inte.

```sh
/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /Users/elinhaggstrom/nortropic/evidence/v313-review-20260912/h036-config-diagnosis.py
```

Exit **0**, de oförändrade funktionernas faktiska utfall:
`exact_config(raw) == (False, 'config product digest mismatch')`;
`product_phase()` resar `Rig: runtime authority v2 rejected: config product digest mismatch`.
Exakt HEAD, rent träd och alla fyra lästa filhashar oförändrade efteråt.
Detta bevisar configbindningshindret, **inte runtimefel eller full H036-kvalificering**.

- `h036-config-diagnosis.py`: SHA256
  `f620e547fcd5f44cfbff23b133153b2b8165bf9498ff9aaf1b205f47f324767d`.
- `h036-config-diagnosis.json`: SHA256
  `1ba29c9fe16035107cc7322beac0d5b72c698e811f08531e1f0fd94997d862fe`.

Nästa fortsättning använder denna avgränsning och befintliga källor; gör inte om
inventering, v3.13-granskning eller dess godkända baslinje för att återfå kontext.
Nästa konkreta leverans är körbart H036-återkvalificeringskontrakt genom
TEST_AUTHOR → oberoende review, före configrättning och samlad kandidatprovning.

### Uttrycklig fortsatt autonomi till supervisor resume — 2026-09-12 10:48 UTC

Ny direkt användarinstruktion i denna Codex-tråd, ordagrant:
”Varför stannar du? du ska arbeta autonomt till supervisor resume”.
Detta utökar den tidigare lokala fasens mål/omfång framåt; det skrivs inte tillbaka
som historisk behörighet för äldre försök. Instruktionen kräver fortsatt arbete
mellan delmilstenarna utan nya generella godkännandefrågor. Ett aktivt arbetsmål
har satts till verifierad supervisor resume.

Utökningen är inte en verifieringsdom: kandidatidentitet, rollseparation, test-first,
skyddad måttstock, bevarande, faktisk publicerings-/installationsbehörighet och
säkerhetskraven ska fortfarande vara uppfyllda före respektive effekt. Inga
förbrukade försök får ny credit eller automatisk retry. En underkänd övergång
hålls stoppad medan oberoende tillåten analys/rättning/verifiering fortsätter.
Genuint ej automatiserbara credential-/ägarkeremonier får inte kringgås.

Omedelbar handling: TEST_AUTHOR har återupptagit det körbara H036-/kvittokontraktet
i den redan skapade v3.14-arbetsytan. Förkontroll: branch nortropic/loop-separation-v314,
HEAD531d37e, rent; lokal origin/main-ref saknas (`ORIGIN_MAIN=OVERIFIERAT`).
Ingen ny produkt, configrättning, publicering eller installation utförd vid denna notis.
V3.13-resultatet återanvänds; dess review och baslinje ska inte göras om för att
starta denna fortsättning. Nästa interna överlämning är till oberoende reviewer,
inte tillbaka till ägaren för ett nytt ”fortsätt”.

#### Remoteobservation och avgränsad H032-fortsättningsdiagnos

I samma session avslutades `/usr/bin/git ls-remote --exit-code origin refs/heads/main`
i integrationsrepot med exit 0: remote main observerades som
`ed584ec3088c08005f99de1da825d083e350a8d2`. Lokal `cat-file -t` bekräftade commitobjekt;
`merge-base --is-ancestor ed584ec3088c08005f99de1da825d083e350a8d2 e6e4091c991ccbcaf9b7bab923a4e1e803453290`
gav exit 0 och `rev-list --count` över samma intervall gav 49. Ingen fetch/push eller
refändring utfördes. Detta är en tidsbunden read-only-remoteobservation, inte
publiceringscredit, uppdaterad lokal origin/main-ref eller fryst gate-observerdom.

Den oberoende H032-granskaren återanvände oförändrad H032-källa
`9281e7182c21ee5758e3e56c26e40d05bbe04f752d5e8da72a05fafa496dcf59`
och autopilot `2976aa33e82af15101c5f2b885ffa479e5892dd94ced0de6b78180b2be71c106`.
En diagnostisk in-memory-kopia ändrade endast
`_R123_CONTROLLER_MODULE_FIRST_HOPS['os'].add('getcwd')`; samma predikat och
autopilotbytes returnerade då True vid grindrad 14366. Inga senare fullgrindshinder
är därmed uteslutna; de är OVERIFIERADE. Detta är lokalisering, inte antagen
kontraktsändring, produktprov eller kvalificeringscredit.

H032:s befintliga shellwrapper har heredocöppnare på rad 94, Python-payload
95–18170 och terminator 18171. Den befintliga statiska etikettfunktionen mäter
91 unika litterala etiketter (96 förekomster; 99 check-anrop varav tre dynamiska).
Detta är inte runtimekontrollernas antal. Payload-AST med 94 inledande blankrader
bevarar originalradnummer. Prefix-SHA256:
`ba6255dc454c1424cc6143150975de6969aefa4de7e903b7a816ccbc7ff658b6`;
suffix-SHA256 `503c558758fba9adc95bc037e7c8f8861fde19d12678c05c879bb74f16148a62`;
sorterade etiketter med avslutande LF:
`b7c398b9f027e37d2a73e9de96ccb4527d57eb451a237de3614966b005d00d3e`.

Senare H032-kontraktsarbete måste hantera tre parserkonsumenter sammanhängande:
omfrysningsdeklarationens ast.parse, gate_row_labels och retirement_bound_lines.
Möjlig smal väg är exakt H032-prefix/suffix bundna till fryst bas, endast
payloadändringar, bevarade radnummer och fortsatt tillagda-rader-skanning över
hela originalfilen. Ingen generell shellparser eller shellkörning behövs för
detta underlag. Det hör inte till pågående H036-v3.14-scope.

Granskarens pinnade Python-diagnos avslutades exit 0; integrationen var ren på
e6e4091. Granskaren kunde inte lösa 531d37e i integrationens ODB och gör därför
inget eget identitetspåstående om den separata kandidaten. Ingen fullgrind,
produktimport, filändring eller H032-builderstart utfördes av granskaren.

### H036 v3.14 lokal kontraktsfrys och verklig röd baslinje — 2026-09-12

Användaren förtydligade fortsatt autonomi och fulla befogenheter, därefter även
arbetsmålet med ”Gäller edits och approvals, allt.” Arbetet fortsätter mellan
delstegen utan ny generell bekräftelse. Faktiska säkerhets-/identitetskontroller
och bevarande ändras inte, och äldre försök får ingen retroaktiv behörighet/credit.

TEST_AUTHOR:s separata arbetsyta:
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v314-h036-20260912`.
Root frös genom normal lokal HÖGRISK-märkt commit (ingen amend/push):

```text
CANDIDATE=8ce985d136d112c5945b5cea520c948bcf6852a9
PARENT=531d37e594410d80d3d07975b8331715dd2508b0
TREE=a0deccb287e4a425c521f682f1a006e558c6de5f
BRANCH=nortropic/loop-separation-v314
SCOPE=4_FILES_243_ADDED_25_DELETED
PRODUCT_CHANGE=NONE
WORKTREE=CLEAN
```

Fyra filer: H036-grinden, separationsgrinden, befintligt utvecklingsdokument och
REFREEZE-deklarationen. SHA256 i samma ordning:
`95be612be7e0d48b281a0ea7552e6bb774792b0a0f6340f91791f53c29be4194`,
`4dddbdf3d8187670e9d78a4542bafb224ac2a18e0a7825a987c3fa25ce501803`,
`e7713a5e377dd18a532339b447393318f3415aaf0ee9bd770b63bccaeece84aa`,
`3797df1912a8ee214f8353fbd4544ea0b2f63b28129e478d3447bd21e6cdceeb`.

Ny lane `--current-product SHA` skiljer aktuell produktgeneration från historiska
objekt. Oförändrade subject_effects/fullmatris krävs efter statik/config; gammal
config ger verklig RED före effekter. Root fann och TEST_AUTHOR rättade att den nya
lanen annars skulle ha använt Git före befintlig trusted_git_valid-kontroll.
Historiska lanes, task/spec och launcher/helper ändrades inte.

Fokusprov före frys: pinnad Python `-I -S -B
/private/tmp/nortropic-v313-contract.Fq5ueV/v314-focused.py`, exit 0:
71 statiska kontroller, 13 virtuella identitetsfall och 8 exakta argv-fall;
korrupt historiskt digest och dålig Git-identitet avvisade. Basetiketter 27,
nya 30, saknade 0; added-line-scan 0. Detta är fokuserad provning, inte full gatecredit.
Reproducerbart script och resultat bevaras i `evidence/v314-h036-review-20260912/`:
`test-author-focused.py` SHA256 `df0c4c697b9d9356c8df10024f3584f6d2feb1bbf7e2dce66c44dabecec2db80`;
`test-author-focused-95be612.result.json` SHA256
`a9cb0adf2fa50d31f16a0568890c0c5ada09b7081eed241f403c4a4d2ee4cbff`.
Scriptets precommit-HEAD-villkor avser ursprunglig fokuskontext; det ska inte
återköras oändrat efter frys och sedan misstas för en produktregression.

Oberoende effektgranskning fann ingen root/installation/extern nätverkstrafik i
produktmatrisen, men verkliga lokala process-/signal-/Seatbelt-/socketeffekter och
temporär Git-administration. Full positiv körning ska därför ske i fristående
replika, aldrig integrationen. Röd baslinje kördes en gång i fristående
`/private/tmp/h036-v314-red.YmfcoR/repo`, från no-local/no-hardlinks-klon med egen
Git-common-dir, detached exakt kandidat och canonical origin-URL. Inga andra
matchande H-grind-/autopilotprocesser observerades före körning.

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B verify/bin/h-036-exit --current-product 8ce985d136d112c5945b5cea520c948bcf6852a9
```

Faktisk exit **1**, `H036_GATE_SUMMARY=72 PASS 1 FAIL`, `H036_GATE_RESULT=FAIL`;
enda FAIL är `A_H036_CURRENT_PRODUCT_CONFIG_BINDS_ACTUAL_LAUNCHER_AND_HELPER`
med `config product digest mismatch`. Stderr tom. Ingen fullmatris startade;
detta är avsedd pre-builder RED, ingen produkt-PASS. Samtliga 144 spårade filhashar
återkontrollerade, indexmanifest oförändrat, status rent och diffkontroll exit 0.
Replikaroten 17552→17584 KiB inklusive nya evidensfiler, klass DIAGNOSTIC_REQUIRED.
Disk före körning 20171464 KiB, över retentionregelns 15 GiB-golv.

Durabel stdout `evidence/v314-h036-review-20260912/baseline-8ce985d.stdout`, SHA256
`119209624bf0d889d01b9b9d1401809d8624f908dd8b2697667698f429f7baa6`.
Stderr och pre-files.sha256 finns intill. Självständig kontraktsreview pågår.
Separat BUILDER får efter READY endast configdelta mot exakt 8ce985d; alla fyra
frysta kontraktsbytes måste då mekaniskt vara oförändrade. H036-identitet ensam
ersätter inte den externa held-candidate-/builder-scopekontrollen.

Ny faktisk historikbundle i befintlig backup:
`bundles/v314-h036-contract-8ce985d.bundle`, SHA256
`fea27f1cbcf3ea92d7048a304c2aae9c2a6bf9270924dba3a6df23999c148ffb`;
`git bundle verify` exit 0 och full historia. Återställningsprov av just denna
nya bundle är ännu NOT_RUN. Tidigare backup/återställningsbevis bevarade.
Ingen H039-WIP, produkt, installation, publicering eller operativ resume ändrad.

Efterföljande återställningsprov av bundle `fea27f1c…`: klonad till exklusivt ny
`/Users/elinhaggstrom/nortropic-repos/work/builder-h036-current-v314-20260912`.
Bundlen saknade remote HEAD (ingen tyst defaultbranchantagelse); explicit checkout
av exakt 8ce985d skapade `nortropic/loop-h036-current-v314`. Egen `.git`, canonical
origin-URL, rent träd, exakt parent/tree/fyra kontrakthashar; samtliga 144 filhashar
och indexmanifest jämförda med RED-replikan, exit 0. `git fsck --full --no-reflogs`
exit 0. Återställbarheten för den nya kandidaten är därmed faktiskt provad.
Ingen config har ännu ändrats; arbetsytan väntar på oberoende kontraktsreview,
inte på en ny generell användarbekräftelse.

Oberoende kontraktsreview avslutad **READY, inga blockerande fynd**, bound till
8ce985d och de fyra ovanstående hasharna. Rapport:
`evidence/v314-h036-review-20260912/independent-review.md`, SHA256
`44485980a6393f5fdf748b9d2b81f7ad68fb9a6fc593b258b89bbdb7ebd31b98`.
Egna körda fokustester exit 0: 15 identitetsfall, 9 routingfall, 10 argv-fall,
statik 71/0 och fyra historiknegativer. Den verkliga RED-loggen oberoende
återkontrollerad. Ingen nativepositiv eller slutkandidatskvalificering ännu.
Hela denna avgränsade evidensmapp har kopierats till befintlig backup
`reports/v314-h036-review-8ce985d` och jämförts rekursivt utan skillnad, exit 0.

Separat BUILDER har därefter fått den återställda arbetsytan och exakt config-only-
ändring. Detta är lokal kandidat inom H036:s befintliga owner_author_allowed_write,
inte vanlig loop-task och inte nytt register-/spec-/produktpathmandat. Alla fyra
frysta kontraktsbytes, launcher och helper hålls oförändrade. Root fryser sedan
produktkandidaten för oberoende review och verklig fullmatris i separat replika.

### H036 configprodukt och fullmatris — 2026-09-12

BUILDER ändrade exakt ett launcher-digest i configen med bevarade 6657 bytes,
0644 och avsaknad av slut-LF. Config-SHA256:
`92f84d8f909bdded186c2db8b8e98f4c79e3f9f5e16c53100f7e005641a183f9`.
Övriga 143 spårade filhashar verifierade oförändrade. Root normalfrys:
`03a364bf248b99d4959cbfc3771c12dd33021b65`, enda parent 8ce985d, tree
`252486dcf05ec257d395d4314c7c36af791118df`, exakt config-only +1/−1, ren.
Oberoende faktisk helperreview verifierade disk=Git, alla fyra frysta bytes,
positiv exact_config/current_product_identity och config-/scope-negativer.
Rapport: `evidence/v314-h036-review-20260912/product-review-03a364b.md`.

Första fullmatrisen i `/private/tmp/h036-v314-product.J1DzQE/repo` gav exit 1,
**73 PASS/1 FAIL**. Enda felrad operational; dess enda falska grupp var
dynamic_profile_binding_and_git_exception och endast underfältet
cleanup_object_fanout_admin_refs_exact var falskt. Alla faktiska objekt-/index-/
own-admin-/adjacent-deny-/overlapkontroller var sanna. Spårade filer/hash/stat,
index och runtime-rootset var oförändrade vid initial efterkontroll.
Logg bevarad som `product-03a364b-r1.stdout`, SHA256
`23b13e5bdb5486374e6d16e8a236ab660069bcbe3884cae15335d2155547f3dd`.
Ingen produkt-PASS ges till detta försök.

Två källgranskningar fann samma fixturemekanism: git_exception_case behåller en
nytillkommen tom .git/worktrees-parent men kräver exakt före/efter directory_state;
None skiljer sig från []. Tom efterkatalog observerad; just första försökets
föreabsens är OVERIFIERAT eftersom det inte sparades i dess premanifest.
Detta får inte skrivas om som ett uppmätt historiskt förebevis.
Granskaren verifierade att samma frysta kontrakt tillåter förmätt tom adminparent;
[]→[] bevarar hela cleanup-oraklet. Inga produkt-/grindbytes rättades för detta.

Ny fristående replica `/private/tmp/h036-v314-product-r2.9jAeQJ/repo`, exakt samma
03a364b, skapades och föreprovet mätte avsaknad av .git/worktrees, skapade tom egen
adminparent och sparade dess tomma inventory. Därefter filer/stat/index/refs/
worktree-list/runtime-rootset före fullkörning. Första försökets sena extra
set-e-audit fick exit 1 endast när detta uttryckligen nyss skapade r2-root dök upp
i dess gamla root-lista; filstat/index/fsck-kontrollerna hade dessförinnan gått
igenom. Detta är orkestratorns kända nya fixture, inte ett nytt runtimefynd.

Full r2 kördes med samma pinnade Python/flags och absoluta grindsökvägen:

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/h036-v314-product-r2.9jAeQJ/repo/verify/bin/h-036-exit --current-product 03a364bf248b99d4959cbfc3771c12dd33021b65
```

Faktisk **exit 0, 74 unika PASS/0 FAIL, H036_GATE_RESULT=PASS**, tom stderr.
Stdout SHA256 `12fb99773e3584736f5e323d900e5d636a7810a66f693b0db8eb47661d760d58`.
Root och oberoende reviewer jämförde 144 hash-/statposter (dev/ino/type/mode/uid/
gid/nlink/size/mtime/ctime), index, refs, worktrees, tom adminparent och runtime-
rootset mot premanifest: exakt, ren status, diffcheck exit 0. R2-root 17608→17612 KiB.
Det är lokal full H036-produktkvalificering av detta subjekt, inte installation,
H039-avslut eller supervisor-resume. Första FAIL är kvar som historiskt FAIL.

Exakt verkligt r2-kvitto har skapats utanför subjektet med faktiska stdoutbytes,
argv, exit och kandidat: `evidence/v314-h036-review-20260912/h036-current-03a364b-r2.receipt.json`,
SHA256 `a7534184b63dbe3ac18d4c02c4046e355e27c41dac3b75380aac0a774bc468cf`.
Separationsfullgrinden kör nu seriellt på SAMMA r2-subjekt med `--subject` och
`--refreeze-receipt` till detta kvitto; root exec-session 7528. Den är ännu IN_PROGRESS.
Inga andra fullgrindar startas samtidigt. Read-only H037-plan-vs-code för nästa
historiska omfrysning återanvänder befintligt beslut, ingen produkt-/gatewrite.

### H036 slutkvalificering och nästa H037-steg — 2026-09-12

Exec 7528 avslutad exit 0: **132 unika PASS/0 FAIL**, terminal
`PLATFORM_SEPARATION_FINAL_RESULT=PASS_LOCAL_QUALIFICATION_ONLY`, tom stderr.
Samma fysiska 03a364b-subjekt och verkliga H036-kvitto som ovan. Durabel evidens:
`evidence/v314-h036-review-20260912/separation-03a364b.stdout`, SHA256
`0d4b2378012d120f422bce63671cc1a91c2c5f8555b098d13c95b9e93dd67d6b`;
`separation-03a364b.result.json`, SHA256
`61e2366733f3982bf0a066c2d3cf1b67d56456178328c409cb7888f852c4519a`.
Resultatets fixture är `/private/var/folders/_v/t4cy04w95gz3m782_3p5qs9h0000gn/T/platform-separation-final-2c8xyw1o`.
De hållna äldre kontrollernas exakt deklarerade listnings-/hash-RED behåller sina
egna exitkoder; inga sådana historiska RED skrivs om till gate-PASS.

Oberoende slutreview **READYLOCAL, inga blockerande fynd** på exakt 03a364b,
H036 74/0, separation 132/0, verkligt kvitto och oförändrat efterläge.
`product-review-03a364b.md` SHA256
`466e055c025504660358fb15c0999859deeed3f508f214dfc9b0ebb71d944172`.
Root jämförde även alla 144 filhashar, index och refs mot premanifest, ren status
och diffcheck exit 0. Första 73/1-försöket är fortsatt FAIL utan credit.

Produktens fullhistorikbundle `bundles/v314-h036-product-03a364b.bundle` i befintlig
backup har SHA256 `be08988917527b0d90486af31c24e7805b2efd1274980d44d98037e304bda2e4`.
Bundle verify exit 0. Faktiskt återställd till exklusivt ny
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v315-h037-20260912`,
branch `nortropic/loop-separation-v315`: egen .git, canonical origin, exakt 03a364b/
252486dc-tree, alla 144 hash-/indexposter lika och fsck exit 0 före TA-ändring.

Efter slutreview normal lokal fetch av exakt SHA och ff-only-advance av den rena
integrationen `/Users/elinhaggstrom/nortropic-repos/nortropic-system` från e6e4091
till 03a364b, exit 0. Filhash/index återjämförda exakt, status ren. Ingen remote
push, publicering, history rewrite, installation eller operativ aktivering.
Lokal origin/main-ref saknas; tidigare observerad live main ed584ec är inte denna
lokala kandidat och har inte skrivits om till publiceringscredit.

Separat TEST_AUTHOR fortsätter nu H037:s beslutade historiska omfrysning på den
återställda arbetsytan, exakt fyra kontraktsfiler. Den redan genomförda produkten
ee84b206 och dess verkliga parent 3560d61 återanvänds som historiska subjekt;
inga webbspecifika sviter återinförs i aktivt träd, ingen ny H037-produkt uppfinns.
H036, övriga produkter, spec/register och H039-WIP hålls oförändrade.
Fullkörningar fortsätter seriellt. Lokal H036-kvalificering är inte bootstrapavslut
eller supervisor-resume; det långsiktiga uppdraget fortsätter utan ny generell
tillåtelsefråga, med samma bevarande och faktiska övergångskrav.

Backupkomplettering: hela r1-/r2-replikorna samt separationskörningens genererade
fixture inklusive underliggande kontrollresultat är arkiverade, utan borttagning
av original, i `external/v314-h036-and-separation-fixtures-03a364b.tar.gz` i den
befintliga backupen. SHA256
`540491d1f8596c39a1fa7a8846d404f21df2c49a404efdcc079011a4698245fd`,
439 MiB, 16469 arkivposter. Komplett tar-listning exit 0; faktisk återläsning av
separationsresultatets JSON och r2:s separationsstdout från arkivet till cmp gav
exit 0 mot durabla original. Produktbundlens faktiska fulla återställningsprov
beskrivs ovan; detta arkivprov avser de två namngivna evidensfilerna, inte en
omkörd kvalificering. Reviewmappen har också kopierats till
`reports/v314-h036-product-03a364b-final` med rekursiv jämförelse exit 0.

### Rättelse av H039-kontinuitet — 2026-09-12, källkontroll utan liveeffekt

Två tidigare påståenden i denna journal (avsnittet med ”Sann beroendeordning”)
är fel: att installed-evidens saknas och att protected-asset-B-kopian är samma
paket som R33_LIVE_R2_FAILED_EVIDENCE. De ersätts framåt av följande faktiskt
återlästa källor. Äldre text kvarstår som historik, inte aktuell körorder.

`worktrees/h039-r33-installed-capture/installed-outcome.json`, SHA256
`4419f24b85abef154113950574dabedb42675be934138fd0d150ba0291c85553`,
binder `--r33-installed ed584ec3088c08005f99de1da825d083e350a8d2 f0877daae8612f4c5b274ae4cc04bc1bd775c01a`,
exit 0, 96249 PASS/0 FAIL, `PASS_PRE_DIAGNOSTIC_OWNER_STOP_ONLY`,
`retry_permitted:false`, `task_credit:NONE`. Faktisk stdout ligger intill,
SHA256 `f4e68424110226fedbbc5455acb929012e2ee7a195becfb000de8c5de9658911`;
oberoende granskare räknade raderna. Efteraudit
`worktrees/h039-r33-installed-independent-audit/RESULT.json` har SHA256
`7b440d9dc545256842effc585618f7c043cdd3ab006a009a1d6be0441cf915d0`.
Den historiska installed-körningen ska INTE köras om. Den gav begränsad workflow-
credit, inte H039-completion eller aktuell driftkvalificering.

Efterföljande `evidence/bootstrap-supervisor/evidence/h039-r33-r15-live-diagnostic-outcome.json`,
SHA256 `efcc5fa541ecefbfa9a6d9566110a38a51e9b2f057c0a02357d6d96875028db6`,
är förbrukad med `STORE_CHANGED_OR_UNPROVEN_OWNER_STOP`, ofullständig capture
och obevisat slutstate. Senare redan utförd observation
`worktrees/h039-r33-postfailure-observation/observation.json`, SHA256
`efdb56a797d3afa2c5976ace43500d98f3b0e006f61e7b97690c6144e4734fb6`,
binder sekvens-2-kvittot, inode 130914222, payload-SHA256
`e4d656ad7be5bfed4326ac72c94d9319540023fc0db527a121ba8890e13fd76b`.
Den bevisar uttryckligen inte full policy/noll residue eller dagens live-state.

Protected-asset-B i `worktrees/test-author-h039-protected-asset-ed584ec3` är eget
bevarat ofruset CONTRACT_SIX/PRODUCT_FOUR-arbete. Gate-SHA256
`aa9f5147d8d1192cc3353aec9a631cc234b58e31301f698334add1a866634183`,
spec `28c25cf5a58f3a0c8c84ded340b618e9d562d7ef9a4be1fd9d3c1a4734fd7db1`.
Oberoende läsande granskare verifierade 50 draftfunktioner, avsiktlig
SystemExit(2) rad 3196 och att B minus exakt draftblock är historiska A:s bytes.
R33_LIVE_R2_FAILED_EVIDENCE binder i stället fyra andra r2-evidensfiler, inklusive
`h039-r33-live-r2-consumer-failure-immutable-record-20260908.json`, SHA256
`69d6f9ce45efae6dc6e88dd2a9e4997fa4eb2da3afdabd1538b68edc45dd57a0`.
Inget av dessa paket ändras eller får ny credit genom rättelsen.

Den återlästa consumer-integration-spec.md i adapterkandidaten har nu SHA256
`bea33a27c0a2d27b3d032cafa657de4d0b917919772e30dfc72fa91a8b5b91be`;
minsta-väg-notens äldre d02a4cc5 är inte dagens bytes. Nästa H039-arbete kräver
separat efterföljare från detta bevarade underlag, med faktisk sekvens-2-/receipt-
livscykel och consumer-/adapter-/loaderkvalificering. Gamla webbdokumentsytor
är inte automatiskt skrivmandat i plattformsgenerationen. Varken en bindnings-
ompinning eller build-only bevisar det operativa avslutet. Exakt felande syscall,
adapterns laddade beteende, dagens skyddade state/processläge och full H039-
completion är OVERIFIERAT. Ingen gate/native/runtime/nätåtgärd kördes för denna
källrättelse. H037-arbetet fortsätter oberoende; ingen ny generell fullmakt begärs.

### H037 v3.15 fryst och historisk fullkvalificering — 2026-09-12

Användaren bekräftade åter full access i denna konversation. Aktuell verktygsmiljö
är danger-full-access, nätverk tillåtet och approval never. Behörighetsbytena
avbröt två rolltrådar; root verifierade interrupted och återupptog dem med normal
followup, utan ny tillåtelsefråga. Ingen säkerhetsmåttstock ändrades av detta.

Separat TEST_AUTHOR-kandidat fryst genom normal lokal commit:
`536352ffea553bd097db14698c59199b4a89f6f5`, enda parent
`03a364bf248b99d4959cbfc3771c12dd33021b65`, tree
`18e56b3e0ca4c4c16f7d595bb8d220d52589fc10`. Exakt fyra kontraktsfiler,
+307/−6, oförändrade modes; ingen ny H037-produkt. Arbetsyta
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v315-h037-20260912`.
H037-grind SHA256 `12ef5f55386a9f68e1b5019d52555d1573e2356408bf584e1a038d09e1d86045`.
Den historiskt genomförda produkten ee84b206 och parent 3560d61 körs i exakt
isolerat historiskt objektsubjekt; utflyttad svit används endast som historisk
hash-/refusal-data och återförs inte till plattformens aktuella träd.

Före freeze falsifierade reviewer första draftens borttagna checkout-force:
ett avsiktligt skip-worktree-mutantbyte blev kvar före senare positiv kontroll.
Bevarad prefreeze-diff `evidence/v315-h037-review-20260912/prefreeze-7a458c.diff`
är no-credit. Rättad projektion tar bort samma åtta forceflaggor och återställer
endast sina egna sparade fixturebytes efter observerad negativ kontroll; oväntade
bytes avvisas utan skrivning. Arkiverad grindkälla och alla ursprungliga orakel
bevaras. Projektion SHA256
`a9b19e8b78e464f640f5945adc595a8c69e370996ebcc81ff2220dc07cd7cfc6`.
Det är uttrycklig körprojektion, inte ett påstående om byte-identisk arkivkörning.
Oberoende fokuserad granskning READY på fryst kandidat före fullkörning.

Fullkörning exec 24301 i `/private/tmp/h037-v315-qualified.Ocb3a1/repo`:

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/h037-v315-qualified.Ocb3a1/repo/verify/bin/h-037-exit
```

Faktisk exit 0, **40 unika PASS/0 FAIL**, `H037_GATE_RESULT=PASS`,
`H037_CREDIT=HISTORICALLY_COMPLETED_ONLY`, tom stderr. De historiska 38 raderna
är faktiskt körda och vidareförda; två ytterligare kontroller binder nuvarande
kandidat före/efter. Stdout SHA256
`17847beff0af98320dba07838515c67901d959c72d87ab740bc27319ed717246`.
Historisk fixture `/private/tmp/h037-historical-completion-ode2bxk8` bevaras.
Root och oberoende reviewer jämförde samtliga 144 filhashar/statposter, index,
refs och status mot premanifest: exakt. Ingen task-attestation, publicering,
installation, H039-completion eller operativ resume följer av detta resultat.

Faktiskt körkvitto utanför subjektet:
`evidence/v315-h037-review-20260912/h037-536352f.receipt.json`.
Samma fysiska subjekt kör nu samlad separationskontroll med detta kvitto,
exec 67472; ännu IN_PROGRESS. Inga andra fullgrindar körs samtidigt.
Ny fullhistorikbundle `bundles/v315-h037-contract-536352f.bundle` i befintlig
backup, SHA256 `472504986d4f5f16d88b3518e625be665698d83ff9b3643dc5bd35e15a011234`,
bundle verify exit 0. Faktiskt återställningsprov av just denna bundle NOT_RUN.
Senast uppmätt disk 18625948 KiB, över 15 GiB-golvet; ingen cleanup.

### H037 slutkvalificering, bevarande och nästa avgränsning — 2026-09-12

Exec 67472 avslutades exit 0: **132 unika PASS/0 FAIL**, tom stderr,
`PLATFORM_SEPARATION_FINAL_RESULT=PASS_LOCAL_QUALIFICATION_ONLY`. Resultat-JSON
binder 536352f, pass=true, exakt 132 sanna rader. Durabla kopior:
`evidence/v315-h037-review-20260912/separation-536352f.stdout`, SHA256
`6d51823b6bf1029b9d3a138a47516857255a0219d92d222510abbcd1c611b340`, och
`separation-536352f.result.json`, SHA256
`596d4d1809686f20a5acecfbfe766dfd9108bf02e42ae8ce85a25759c3716cb5`.
H037-kvittot har SHA256
`288f50c338fb34b31aa69520eb6ecdeb1d19517ce84d3272e43478923f325293`.
Undergrindarnas egna 67/1, 19/1 respektive 67/3 är kvar som exakt förväntade
hash-/listnings-RED; deras status görs inte om till PASS.

Root och oberoende reviewer har efter fullkörningen återjämfört alla 144 filer
(SHA256 och fullstat), index, refs och status; exakt, diffcheck exit 0.
Slutreview **READY / lokalt kvalificerad**, inga blockerare:
`evidence/v315-h037-review-20260912/prefreeze-focused-review.md`, SHA256
`2f347e4246039ba5112b638d4a63a2d6c1125028f9c2942d26b9d4e29091b15e`.
Den äldre prefreeze-falsifieringen är bevarad i samma appendade review.

Efter detta avancerade root den rena lokala integrationen från 03a364b till
536352f med exakt lokal fetch och ff-only; alla 144 filhashar och index lika
med kvalificerat subjekt, ren status och diffcheck exit 0. Ny läsande
`git ls-remote --exit-code origin refs/heads/main` gav exit 0 och
`ed584ec3088c08005f99de1da825d083e350a8d2`. Lokal origin/main-ref saknas fortfarande;
den lokala integrationen har inte publiceringscredit. Ingen push eller remote-merge.

Bundlen 47250498… har nu faktiskt återställts till egen Git-root
`/Users/elinhaggstrom/nortropic-repos/work/test-author-separation-v316-h039-continuity-20260912`,
branch `nortropic/loop-separation-v316`, exakt 536352f/tree18e56b3 före TA-ändring.
Alla 144 filhashar och index jämförda, fsck exit 0, egen .git utan alternates,
canonical origin-URL. Kandidatens tidigare NOT_RUN för bundle-restore är därmed
ersatt av detta konkreta återställningsprov.

De kompletta H037-/separationsreplikorna inklusive historisk fixture är bevarade
i backup `external/v315-h037-and-separation-fixtures-536352f.tar.gz`, SHA256
`27263aeafe7d143d50bdd413f3b9626d1b616386be117e96e4064beb7e01aa3a`.
Tar-listning: 16717 poster, exit 0. Faktisk återläsning av H037-stdout och
separationsresultat-JSON till cmp mot durabla kopior gav exit 0; detta är
arkivkontroll av de två filerna, inte en omkörd grind. Original bevarade.

Nästa konkreta fel är nuvarande plan r193–198: den beskriver förbrukad installed-
körning som kvarvarande och blandar ihop protected-asset-B med failed-live-r2.
Separat TEST_AUTHOR förbereder därför en enda kontroll i befintlig separationsgrind
och dess devdoc. Senare separat implementerande roll får endast korrigera detta
planblock och de tre nödvändiga planpinnarna i autopilot/controller-verify.
Handoff/spec/register/H-grindar/REFREEZE och andra planbytes lämnas oförändrade.
Ingen sådan plan-/pinprodukt är ännu byggd eller kvalificerad.

H039-källanalysen visar att PRODUCT_FOUR fortsatt bara är assetbygge: B kräver
runtime-mediatorn oförändrad medan R15 kräver sequence1. En operativ efterföljare
måste därför skiljas från assetkvalificeringen och bindas till faktisk sekvens2-
föregångare, nytt fast försök och fas-/kvittolivscykel. Befintliga modeller och
adapterunderlag återanvänds; ingen ny runtimekod eller operativ effekt är utförd.
Exakta B-gate/spec, consumer-spec, installed-outcome/audit och diagnostik-/
efterobservationshashar ovan återlästes oförändrade även efter H037-integrationen.
Källanalys är inte formell arkitektur-/gate-/produktcredit.

Disk efter backup/restore: 17258156 KiB, fortfarande över 15728640 KiB-golvet
men begränsad marginal. Ny tung körning måste föregås av nytt df; inga skyddade
repos/evidens får tas bort för att skapa utrymme. Ingen cleanup har utförts.

### H039-kontinuitet v3.16 — kontrakt före plan-/pinrättning, 2026-09-12

Root har fryst separat tvåfils-TEST_AUTHOR-kandidat
`84aa340486b26b88f7f5d717a81112315e92d55f`, parent 536352f, tree
`fe6cb51c8718ba551dad9e4aabad7422ff742856`, +117/−2, ren status.
Grind SHA256 `fabc7a1f7c0e6de32e80f61c794f806027cede3bae59c1d72d3a13dae346d4f6`,
devdoc `289deb6dc42c960542b60a0995620365929a93dd08a6c0c526daef3031e9155a`.
Exakt en F4-rad tillkommer och denominator är 133; övriga funktioner och main
minus dessa två nya statements är AST-identiska. Grundplanen binds separat
till 536352f så framtida refreeze-generationer inte ändrar transformens källa.

TA:s faktiskt körda pinned-Python-fokus gav 14 förväntade utfall; gamla planens
faktiska nya kontroll ger false, rättad text true. Script
`/private/tmp/nortropic-v313-contract.Fq5ueV/v316-focused.py`, SHA256
`5609234f5311cfd45f90b49d78be23312a154182b6e9623e989c18cb4abbdb86`;
resultat `v316-focused.fabc7a1f7c0e.result.json`, SHA256
`8c97c8c9cdba8075431068067e8eb1d096dfe793819cd5c45da136ac07c61df1`.
Oberoende fryst kontraktsreview READY, egna helperprov 11/11 och faktiska
F4-blockprov 9/9. Rapport
`evidence/v316-h039-continuity-review-20260912/independent-review.md`, SHA256
`65c92328cf8217b33eadb92f915a3311bab046fbd6ab0ba1e355e693b0cdf5d9`.
Fokus/READY är inte full RED-baslinje eller kvalificerad planprodukt.

Fristående baslinjereplika `/private/tmp/separation-v316-red.CGYz9L/repo` är exakt
84aa340, ren, egen .git utan alternates, fsck exit 0. Premanifest för 144 filer/
stat/index/refs/status finns i parent. Första konstruktionskommandot avslutades
127 enbart därför att slutlig df låg på fel absolut sökväg /usr/bin/df;
klon/checkout/fsck hade slutförts. /bin/df mätte därefter 17238644 KiB; ingen
grind hade startat vid detta diagnostikfel och ingen permission eskalerades.

Full baslinje **IN_PROGRESS**, exec 95610, exakt:

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/separation-v316-red.CGYz9L/repo/verify/bin/platform-separation-final-exit --subject /private/tmp/separation-v316-red.CGYz9L/repo
```

NOCLOBBER stdout/stderr i parent, umask0022. Inget H-kvitto används: oförändrad
H037-deklaration är ärvd historik. Observerad hittills endast förväntad FAIL
`f4_plan_h039_continuity_records_consumed_evidence_without_retry_task_credit_or_scope_change`;
terminalresultatet är ännu inte bevisat. Förutsagt fullutfall 132 PASS/1 FAIL.

Ny faktisk fullhistorikbackup `bundles/v316-h039-continuity-contract-84aa340.bundle`,
SHA256 `a1d70d6891ac0efe87e8ff5a23f791644ca457b10b5817cb4ebb9c327a3a6b71`,
bundle verify exit 0 och faktiskt återställd till egen clean BUILDER-kopia
`/Users/elinhaggstrom/nortropic-repos/work/builder-h039-continuity-v316-20260912`,
branch `nortropic/loop-h039-continuity-v316`; alla 144 filhashar/index lika,
fsck exit 0. BUILDER läser nu kontraktet men får inte ändra förrän full korrekt
RED har verifierats. Senare exakt tre filer: planens OLD→NEW-block, två
autopilot-planblobliteraler och en controller/verify-planSHA. Handoff, spec,
register, H-grindar och H039-WIP förblir oförändrade. Integrationen kvar på
kvalificerad 536352f. Ingen ny generell godkännandefråga eller driftåtgärd.

### v3.16 faktisk RED och fryst planprodukt — 2026-09-12

Exec95610 är avslutad: exit1, **132 unika PASS/1 FAIL**, endast den nya
H039-kontinuitetsraden, tom stderr och korrekt RED_LOCAL_QUALIFICATION.
JSON har exakt133rader och rätt84aa340-subjekt. Alla144hash/stat/index/refs/
statusposter oförändrade; root och oberoende reviewer bekräftade samma sak.
Durabel `evidence/v316-h039-continuity-review-20260912/baseline-84aa340.stdout`,
SHA256 `764c63c8f80702fcd6e1dd948059c58b20adff0f3b0a36c363fa5bf39122db13`,
och `.result.json`, SHA256
`61507f251fbd76d6996a7caf31b7fed346a87ad6df70d30e2373ade81a2b3c09`.
Historisk baslinje bevaras som riktig RED, inte ett misslyckat produktbygge.

Efter RED implementerade separat BUILDER exakt tre tillåtna filer, +15/−8.
Root normalfrys `8095d947c83202e2b87801531d9f7cb1457c8719`, parent84aa340,
tree `f99b66517ad41a153f46e13a2dce51559d6f796b`, ren builderarbetsyta.
Plan SHA256 `cb0f18a774637895d8240c323f46c2dfe9dfca2735119aa9fd2e863c0553080d`,
blob `c4f3a615e5e740ffee3c4cf8353969e3134d44f3`;
autopilot `5fcfd24e8f359f96942419323865a0af999e480df48435712151f33e986c66ae`;
verify-cli `3cc601d5c917a70acae036beb4685bd429180567fa148c2f8bb758aac049326b`.
Frysta gate/devdoc/REFREEZE och andra141filer oförändrade.
Oberoende produktreview READY, faktisk readonlyHEAD-planbindning accepterad,
gammalpin avvisad, övriga AST efter enbart literalnormalisering identiska.
Review `independent-review.md` i samma evidensmapp, SHA256
`629683c75404952b2dcddd33bc807d7cbc62f46daf6c9c662b4dacb65de693b2`.

Produktens fullhistorikbundle
`bundles/v316-h039-continuity-product-8095d94.bundle` har SHA256
`5cc302c9e867a8a74a43317150dd3a3b956207ba1c43a099fe6da512badd2279`,
bundleverify0. Faktiskt återställd till exklusiv
`/private/tmp/separation-v316-product.oj5iLQ/repo`, clean8095, egen.git utan
alternates, fsck0; 141filer likaRED-baslinjen och tre nya exaktahashar.
144hash-/stat-/index-/refs-/statuspremanifest i parent. Förestorlek17636KiB,
disk16370488KiB före fullkörning, över15728640golvet.

Full produktkvalificering **IN_PROGRESS**, exec42483, ensam fullgrind:
sammapinnadePython/env/-I/-S/-B som baslinjen, absolut
`/private/tmp/separation-v316-product.oj5iLQ/repo/verify/bin/platform-separation-final-exit`
med `--subject /private/tmp/separation-v316-product.oj5iLQ/repo` och inget kvitto.
NOCLOBBER `separation.stdout`/`separation.stderr` i parent, umask0022.
Ingen integration av8095före faktiskgrönfullkörning/efteraudit.
Inget nytt H039-försök, installation eller supervisor-resume har startats.

### v3.16 full lokal kvalificering och integration — 2026-09-12

Exec42483 avslutades faktiskt med exit0. Den frysta grinden kördes med:

```sh
env PROVIDER_CALL_ALLOWED=NO MODEL_CALL_ALLOWED=NO PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/separation-v316-product.oj5iLQ/repo/verify/bin/platform-separation-final-exit --subject /private/tmp/separation-v316-product.oj5iLQ/repo
```

Utfall **133 unika PASS/0 FAIL**, tom stderr, exakt terminal
`PLATFORM_SEPARATION_FINAL_RESULT=PASS_LOCAL_QUALIFICATION_ONLY`.
Resultatet binder subject_head8095d947c83202e2b87801531d9f7cb1457c8719,
pass:true och exakt133rader. Root och oberoende reviewer återkontrollerade
144 filhashar/fullstat, index, refs och status mot premätningen: alla lika.
Ingen ny körning behövdes för efterkontrollen.

Durabel evidens i `evidence/v316-h039-continuity-review-20260912/`:

- `product-8095d94.stdout`, SHA256
  `ce13f413bd7c66b59c47623d1e72d656b8e0b9f78fe1e1015db7f2a28eea5cf3`;
- `product-8095d94.stderr`, 0 byte;
- `product-8095d94.result.json`, SHA256
  `dae57b4b6e08250319fce0b622b7dedf20cb217dc8d2cbd08e13be595fbe1c85`;
- `independent-review.md`, slutreview READYLOCAL, SHA256
  `c02e53f64fa5018fd2530e4263a5c5446cedaa73a155448d2333810a7651c350`.

Efter dessa kontroller hämtade root exakt8095 från den separata lokala
builder-kopian och utförde lokal `git merge --ff-only FETCH_HEAD` från536352f.
Integrationen `/Users/elinhaggstrom/nortropic-repos/nortropic-system`, branch
`nortropic/platform-integration-20260910`, är nu ren8095, tree
`f99b66517ad41a153f46e13a2dce51559d6f796b`. Alla144filhashar och index matchar
det körda subjektet; `git diff --check` exit0. Ingen publicering eller extern
merge har skett. Lokal origin/main-ref saknas: ORIGIN_MAIN_REF=OVERIFIERAT;
den tidigare denna sessions läsande remoteobservationen förblir daterad evidens,
inte en ny livekontroll.

Kvalificeringen gäller planens korrigerade H039-kontinuitet och dess exakta
bindningar. H039 full completion, senare sequence2-/receipt-/loaderkvalificering
och supervisor-resume får ingen credit av detta. Förbrukad installed-PASS och
diagnostik förblir förbrukade; befintliga frysta H-grindar och H039-WIP orörda.

Bevarade produktkörningsrötter: `/private/tmp/separation-v316-product.oj5iLQ`
17648KiB och
`/private/var/folders/_v/t4cy04w95gz3m782_3p5qs9h0000gn/T/platform-separation-final-5n83a8yy`
813968KiB, CREDITED för detta lokala subjekt. Fullständigt separat arkiv av
v316-fixturerna är ännu NOT_DONE; originalen bevaras och de frysta kontrakts-/
produktcommittarna har redan faktisk bundle-backup med återställningsprov ovan.
Efter körningen mättes15544352KiB fritt, 184288KiB under det stående15GiB-golvet.
Inga nya diskintensiva körningar startas under golvet och ingen cleanup har gjorts.
Avgränsad read-only TEST_AUTHOR-measurability för nästa H039-kontrakt fortsätter
oberoende av detta, med återanvändning av bevarat B-/adapter-/sequence2-arbete.

### Nästa H039-kontrakt: avgränsad intern arkitekturroutning — 2026-09-12

TEST_AUTHOR:s read-only mätbarhetssteg identifierade att bevarade B:s gamla
CONTRACT_SIX inte kan användas direkt på plattformen. Efter intern ARCHITECT-
routning är nästa väg TEST_AUTHOR för en uttrycklig asset-only-underfas inom
befintlig separationsgeneration. Detta är designvägledning, inte fryst allowed_write,
ny policy eller grindcredit. Ingen ny generell ägarfullmakt efterfrågades.

Minsta härledda kontraktyta är sex befintliga filer:

- `verify/bin/h-039-exit`;
- `specs/tasks.spec.json`, endast exakt avgränsad ny asset-medlem;
- `verify/bin/platform-separation-final-exit`;
- `docs/loop/platform-separation-final-local-development.md`;
- `SEPARATION-20260910/REFREEZE.json`;
- `controller/verify/cli`, endast den nödvändiga `PLATFORM_SPEC`-bindningen.

Den sista konsumentbindningen saknades i den preliminära femfilsytan.
Aktuell specSHA är `3e5d564cb633c5f720a715c7591a849673b0a95736e6ceb0bcac8db9e63b1b95`;
registerSHA `9752d01d4128b3fb86488875f2dac3685db51985bc2592544de97f36ffd7ee53`
ska bevaras. Ingen ny registerpost, autopilot-/plan-/handoff-/driftändring eller
återinförd webbtext behövs för denna underfas.

Konkret källhinder: separationsgrindens F3 vid2899–2916 kräver både giltig
PLATFORM_SPEC-pin och hela specens byteidentitet. F6 vid3632 och3790–3890
medger endast en vanlig H-grindsrefreeze med historiskt etikettgolv/noarg-kvitto
och undantar inga produktfiler. Efterföljaren behöver därför en uttryckligt
typad H039-underfas med exakt specprojektion, kanoniska asset-anrop, kandidat-/
kontrakt-/materialbindning och begränsat resultat. Inte en fri undantagstext,
generell bytefrys-uppluckring eller en ny generell styrmekanism. Alla andra
specbytes, skyddade ytor och refreeze-regler ska behållas. Gammal H039-källa
bevaras och autentiseras som data; ingen gammal consumed lane körs om.

Separat BUILDER-yta för asset-only är de fyra redan bevarade B-pathsen:
`controller/runtime-cleanup/install`, `controller/runtime-cleanup/native/mediator.c`,
`verify/h039/build-recipe.json`, `verify/h039/identity-manifest.json`.
Runtimebinären ska förbli exakt oförändrad. Positivt bevis måste förena faktisk
Git-relation/scope/budget med reproducerat byggmaterial och inerta container-
egenskaper; sammanhängande men felaktigt ompinnade manifest, extra path/mode,
ändrad runtime, fel payload/segment, aktiv entry och korsad fas ska avvisas.
Ännu saknas verklig sammansatt observer-/graf-/numstatmätning, kausala
attributfixturer, genuin preproduct-RED och fryst dispatch. Dessa är NOT_RUN;
modellprov eller arkitektens READY är inte ersättning.

Den senare operativa efterföljaren behöver även befintliga runtimebinärpathen,
exakt ny transaktion/kvittomatris och faktisk consumer-/loader-/ABI-kvalificering.
Asset-only löser inte detta och ger ingen H039-taskcredit, installation eller
supervisor-resume. B, dess spec och adapterspec återhashades oförändrade:
`aa9f5147d8d1192cc3353aec9a631cc234b58e31301f698334add1a866634183`,
`28c25cf5a58f3a0c8c84ded340b618e9d562d7ef9a4be1fd9d3c1a4734fd7db1`,
`bea33a27c0a2d27b3d032cafa657de4d0b917919772e30dfc72fa91a8b5b91be`.

Faktisk kapacitetsgräns: sista `/bin/df -k` gav15534912KiB ledigt, både arbets-
och backupytan ligger på samma Data-volym. Det är193728KiB under generella
15GiB-golvet. B:s bevarade byggdriver kräver dessutom21474836480byte (20GiB)
före skapande och varje lane; underskottet är5436608KiB mot den gränsen.
Ingen kompilering, fullgrind, radering eller överträdelse av golvet har gjorts.
Kapacitet, inte sakgodkännande eller verktygsbehörighet, hindrar nästa tunga prov.

Slutevidensen har kopierats till befintlig backupyta
`reports/v316-h039-continuity-final-8095d94`, rekursiv jämförelse exit0;
journalen genom v316-slutkontrollen finns i
`reports/CLAUDE-CHECKPOINT-20260912-V316-FINAL.md`, cmp exit0.
Nuvarande sexfils-H039-efterföljare är ännu inte skapad eller fryst.

### H039: separat förberedelse och återvunnet byggmaterial — 2026-09-12

Senare än föregående notis finns nu en separat TEST_AUTHOR-arbetsyta:
`/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-asset-local-8095d947-20260912`,
branch `nortropic/loop-h039-asset-local-20260912`, HEAD
`8095d947c83202e2b87801531d9f7cb1457c8719`. Den återställdes från den befintliga
produktbundlen, inte från H039-WIP. Den har tre ofrysta ändringar, +116/−1,
oförändrade modes och inget stagat:

- `specs/tasks.spec.json`: SHA256
  `2782ead32ed99ccd5d3995040df90abe399d83fd0f369662911518db3e8a8d76`;
- `controller/verify/cli`: SHA256
  `c55b36775b667f5e5b895d3477e11d4cd30edd681f01e01d1ac305e94a7747cf`;
- `docs/loop/platform-separation-final-local-development.md`: SHA256
  `5e213531ec102b902edd8c11ffbe0d854a521bc3e8d7e96fd23269f4ed3d6aec`.

Det nya specfältet är uttryckligen NOT_READY och medger ingen ny dispatch.
Övriga specbytes är exakt återställbara genom borttagning av just detta block;
CLI-deltat är enbart motsvarande PLATFORM_SPEC-pin och dokumentet append-only.
Root körde den effektgranskade
`/private/tmp/nortropic-v313-contract.Fq5ueV/h039-asset-local-preparation-static.py`
med pinnad Python3.12.13 `-I -S -B` och ändlig `env -i`-miljö; exit0:
`STATIC_PREPARATION_ONLY: exact spec projection, duplicate refusal, old fields, pin-only CLI, append-only doc, 3-path unchanged-mode scope: OK`.
ScriptSHA256 är `c63d02707b853c2778fd7d33eac8e4c6df23c046437691abb7c225dae477bb4f`.
`git diff --check` exit0. `origin/main` saknas fortfarande: OVERIFIERAT.
Ingen ny grind, kontraktsfrysning eller produktimplementation har utförts.

De tre utkastfilerna och kontrollscriptet har faktisk backup i befintlig backupyta:
`external/h039-asset-local-preparation-2782ead3-20260912.tar.gz`, 391725 byte,
SHA256 `c6abfbf828204275c0d056ba25afbbf388620ba921d3991f24a9545ed787eb8e`.
Arkivet återställdes till `/private/tmp/h039-asset-draft-restore.Su3l6G`, 1276KiB,
och samtliga fyra filer jämfördes med `cmp`, utan avvikelse. Första jämförelse-
kommandot avbröts av zsh:s specialvariabel `path`; arkivet var redan skapat och
extraherat. Endast jämförelsen återupptogs med `asset_rel`; ingen backup skrevs över.

Tidigare faktiskt byggmaterial återfanns i
`/private/tmp/h039-asset-measure-q2j4bejy`, två laner och 72 filer. Dess befintliga
arkiv `external/private__tmp__h039-asset-measure-q2j4bejy.tar`, SHA256
`68d3b85fd699674fe74ff9223c5112802b2494b9b29b44ef2fc861aff3253c75`,
återställdes till `/private/tmp/h039-asset-evidence-restore.00k4Tu/`.
Rekursiv `diff -rq` mot originalet gav exit0, även vid efterkontroll.
De tio byggoutputs är byteidentiska mellan lanerna. Bevarade 16 kommandokvitton
anger rc0/reaped och deras stdout-/stderrhashar matchade de faktiska filerna.

Oberoende granskare körde endast sex autentiserade AST-uttagna materialfunktioner
från B under pinnad Python, inte hela B eller dess byggdriver. Båda lanerna gav
46/46 materialkontroller, inklusive 23 negativa fall med omberäknade signaturhashar.
AST-projektionSHA256:
`bdc3e056de72f24cca069327c52b9a2b2667539a15e452f411e6aefbd95c612f`.
Detta är återanvändbart historiskt materialankare, inte ny kompilering, laddnings-
eller H039-credit. B/spec/adapterspec återhashades oförändrade med samma tre hashvärden
som föregående avsnitt. Inga original eller förbrukade försök ändrades.

Nästa lätta TEST_AUTHOR-steg är en metodgranskad, liten reference-only-fixture för
faktisk Git-numstat över det återvunna materialet; gamla SequenceMatcher-siffror är
inte en sådan mätning. Script får inte köra innan oberoende effektgranskning.
F3/F6, verklig kontrakt-/produktgraf, kausala attributfall och preproduct-RED återstår.
H036:s gamla 74/0 gäller sitt ursprungliga subjekt, inte automatiskt denna senare
spec-/produktstruktur; det är en senare återkvalificeringskoppling, ingen H036-edit här.

Senaste `df -k` gav15546772KiB ledigt, under både det allmänna15GiB-golvet och
B:s20GiB-bygggolv. Ingen tung grind/kompilering, cleanup, publicering, installation,
runtime eller supervisor-resume startades. Lättare kontraktsarbete fortsätter inom
befintligt mandat; kapacitetsgränsen är inte en ny godkännandefråga.

### H039: faktisk liten Git-numstat-mätning — 2026-09-12

Efter oberoende READY_METHOD_ONLY och roots fullständiga effektläsning kördes
`/private/tmp/nortropic-v313-contract.Fq5ueV/h039-asset-reference-numstat-method.py`,
SHA256 `d004e2023b6c5ffbb4092666fc6ae67655a640fa356179e4dce5424621a224f8`:

```sh
env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C PYTHONEXECUTABLE=/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 /opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B /private/tmp/nortropic-v313-contract.Fq5ueV/h039-asset-reference-numstat-method.py
```

Faktisk exit0. Ny bevarad bare-fixture
`/private/tmp/h039-asset-numstat-reference-ko8im7by`, 388KiB.
27 lokala Git-kommandon hade rc0; inga commits, branchrefs, checkout, index,
remoteoperationer, nativebyggningar eller laddningar. Två fempaths-träd mättes:
`620de98273e21df3806ac440cfa0246a15c4fbe1` →
`0074864da82499e177aeda485d328daf3194da1c`.

| Fil | Faktisk Git tillagt/borttaget |
|---|---|
| controller/runtime-cleanup/install | binär `-/-` |
| controller/runtime-cleanup/native/mediator.c | 168/0 |
| verify/h039/build-recipe.json | 282/84 |
| verify/h039/identity-manifest.json | 75/52 |

Textsumma525/136, totalt661. Dessa faktiskt observerade tal råkar vara lika den
gamla SequenceMatcher-modellen; de antogs inte i förväg. Alla fyra är M med
oförändrade modes; den femte runtimefilens blob och mode är oförändrade.
B:s fyra rena datafunktioner extraherades först efter dess exakta källhashkontroll;
AST-projektionSHA256 `49092c3254121a997d2abadf37abb11fb5e604d2b93fd597a8a045c6390e6052`.

`reference-measurement.json` SHA256
`28bc544a5880adf44e4108595452f3922b5f9c727106e76112dfaf77ad6ed877`
bär kommandon, råa utfall och inputidentiteter, `complete:true` och
`originals_unchanged:true`. Inputkontrollen omfattar72materialfiler, B, verktygen,
de fem basprodukterna och tre-filsholden. Efteråt är fortfarande exakt de tre
utkastfilerna ändrade, inget stagat, `git diff --check` exit0.

Kreditgräns: endast referensträdens faktiska numstat/scope/modes. Utan komplett
repo och attribut ger detta ingen .gitattributes-prövning; utan commits ingen
kontrakts-/produktgraf. Ingen ny kompilering, grind-, produkt- eller H039-credit.
Den högsta etiketten är `REFERENCE_ONLY_NOT_PRODUCT_GRAPH_GATE_BUILD_OR_TASK_PASS`.
8MiB-fixturkontrollen är inte en OS-kvot eller same-UID-isolering. Dess128MiB-
förkontroll ändrar inte15/20GiB-gränserna för tunga grindar och byggning.

Fixtur och script har arkiverats i befintlig backupyta som
`external/h039-asset-numstat-reference-ko8im7by-20260912.tar.gz`, SHA256
`a36e4473b68c096a294d10314303468a6e2bcae0bdc7822181f7e9dd8bd49ba6`.
Faktisk återställning till `/private/tmp/h039-numstat-backup-restore.5a8463` gav
rekursiv jämförelse och script-cmp utan avvikelse. Originalen bevaras.
Nästa arbete är sammanhängande H039-kontraktsdispatch och dess exakta F3/F6-
kopplingar, med graf-/attributprov och genuin preproduct-RED före BUILDER.

### H039: återbruk mot den operativa återstoden — 2026-09-12

Oberoende read-only återbruksgranskning och roots källkontroll bekräftar att
byggmaterialet inte är slutmålet. `listener_adapter.c:76` i den bevarade
`worktrees/h039-listener-adapter-v1-candidate` innehåller redan
`query_received_listener`: self-PID, fast flavor, FD-/flaggkontroller före/efter
och inga dup/close/retry. Returvärdet heter uttryckligen
`UNVALIDATED_ADDRESS_AND_IMAGE`. CPython3.9.6-bygglayout är inte bevis för aktuell
consumer-/kernel-ABI eller laddad symbolbild.

`evidence/bootstrap-supervisor/evidence/h039-r33-r15-live-diagnostic-run-once-r3.py:3854`
bär återanvändbar `validate_prepared`: exakt schema/sekvens, tre SCM_RIGHTS-FD,
CLOEXEC och separata runtime-/FIFO-/listener-/namngiven-socket-identiteter.
Den gamla listener-primitiven vid3934 behöver en efterföljare; oberoende
`getsockname`, requesthärledd exakt path och rebinds får inte försvinna.
Runnern är förbrukad och lästes endast som källa, inte körd eller ändrad.

Den gamla `diagnostic_predecessor_open` i bevarad R15-mediatorkälla och
`derive_receipt` i samma diagnosrunner är bundna till1→2. Sekvensannexet anger
kravförslag för en ny fast2→3-transaktion under samma OFD-lock, med exakt
predecessor, ny identitet/nonce, invalid ACK/never ACTIVE, fasbunden unwind,
kvitto och noll residue. Metadataannexets smala seq2-profil får inte bli
global metadataacceptans eller ett påhittat seq3-slutoracle. Båda annexernas
historiska NOT_APPROVED/NOT_ADMITTED-etiketter bevaras; ingen historisk
operation får nytt mandat eller credit genom denna källgranskning.

I nuvarande kvalificerade plattformssubjekt återstår bevis för en precist kvalificerad
skyddad adapterinstallation och loader: autentisering före extensionkod,
aktuell interpreter/dependencyval och faktisk symbolbild/ABI/adresssemantik,
följd av den nya livscykelns kausala fasprov. Produktens runtime måste därför
kunna ändras i den separata operativa efterföljaren; `runtime unchanged` är
asset-underfasens gräns, inte ett permanent slutkrav. Byggmaterial-PASS får
aldrig ge downstream-readiness eller supervisor-resume. Ingen laddning,
installerad-state-observation, root-/runtimekörning eller ny livetransaktion
har utförts i denna granskning.

### H039: återbrukad fyrfilsrelation verifierad i minnet — 2026-09-12

Oberoende granskare läste den rena helperclosure:n och körde pinnad
`/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B -`
med inline AST-uttag av exakt13 I/O-fria definitioner från B. B:s råa SHA256
`aa9f5147d8d1192cc3353aec9a631cc234b58e31301f698334add1a866634183`
och adapterkällans `a35dc310e05f7cf83d7175e5ee5ba3213e6a7433daaa7cc5dd25f9e92ff437fa`
kontrollerades före uttaget. AST-projektionSHA256:
`cf8552954bbf3a2ee2d2f0c12f9a4b59201ffe6ff2ca171afce7519e9b609bcb`.

Faktisk exit0, 1.12s. För vardera återställd historisk lane gav
`product_material` `FOUR_FILE_STATIC_RELATION_ONLY_NOT_GRAPH_OR_GATE_CREDIT`
och de befintliga `product_controls`29/29, mätt antal. Samstämmigt felaktig
recipe/manifest avvisades med `RECIPE_BINDING`; korsat manifest med
`MANIFEST_BINDING`. Omförseglad container med sammanhängande ny manifesthash
och fel segmenträttigheter avvisades med
`MATERIAL:container:SEGMENT_PERMISSIONS`; omförseglade korsade payloads med
`MATERIAL:container:RUNTIME_PAYLOAD`. Båda sistnämnda hade fortsatt signaturhash-
kontroll `OK`: det var materialfelet, inte en stale hash, som avvisades.

Alla79inputfiler (72historiska materialfiler, B, adapterkälla och fem aktuella
basprodukter i plattformsrepot) behöll byte-/fullstat-identitet. Ingen produktkopia,
Gitmutation, kompilering, query, native-laddning eller grindkörning utfördes.
525/136 i denna helpers budget är fortfarande den namngivna rena modellen;
det tidigare separata Git-provet är evidensen för faktisk numstat. De båda
ankarna är återbruk inför kontraktsarbetet, inte kontraktsgraf eller H039-credit.
TEST_AUTHOR är underrättad och fortsätter det separata ofrysta kontraktet.

### H039: den bevarade Git-observerns återbruksgräns — 2026-09-12

Oberoende metodgranskning och roots läsning av B:s
`h039_asset_draft_git_observe_local` bekräftar en konkret domänbegränsning:
funktionen accepterar bara `CONTRACT_SIX` eller `PRODUCT_FOUR` och kräver
`actual_changed == sorted(selected_paths)` före numstat/material. Den befintliga
rena v3.16-replikan jämför däremot `84aa340486b26b88f7f5d717a81112315e92d55f`
med `8095d947c83202e2b87801531d9f7cb1457c8719`, vars tre ändrade paths är
plan, autopilot och verifierar-CLI. Observern kan därför inte oförändrad ge
positiva H039-fakta för det subjektet. `Git complete diff surface` är den
källhärledda förväntade vägran om alla tidigare förkontroller passerar;
anropet har INTE körts och är inget uppmätt negativt prov.

Vi ändrar inte replikans config eller fasetikett för att kringgå detta och
skapar inte en separat generell observationsväg. Återbruket kräver den redan
planerade exakta kontraktsanpassningen i TEST_AUTHOR-ytan. Retained FD/name-
kontroller, rå commit-/trädauthentisering, attributkontroll och avslutande
återautentisering ska bevaras; enbart status/hashjämförelser ersätter dem inte.
Ingen ny observerkörning, produktändring eller H039-credit följer av läsningen.

Aktuell läsande kontroll: integrationskopians `git status --porcelain=v1` gav
tomt resultat; TA-kopian har fortfarande endast de tre tidigare dokumenterade
förberedelseändringarna. Agenthandtaget `v313_contract_preparation` bekräftades
RUNNING. `df -k` gav15532352KiB ledigt: tung grind/byggning kvarstår under
kapacitetsgränsen, medan den levande källförberedelsen fortsätter. Inga nya
original, frusna bevis eller förbrukade försök har ändrats eller återkörts här.

Kompletterande lätt kontroll: root körde B:s fyra oförändrade I/O-fria
`git_operation`, `git_config_exact`, `git_records` och `git_fact_controls` genom
hashbundet AST-uttag i pinnad Python3.12 med `-I -S -B -`, tom miljö utom
PATH/LANG/LC_ALL. Faktisk exit0 och33/33 distinkta kontroller. Positiva commit-,
träd- och blobposter samt fel objekthash, fel NUL-framing, dubbletter, fel numstat,
otillåten config och okända Gitoperationer prövades. AST-projektionSHA256
`a9c74f7550d59f15b12e953a5661ac859fc8a5dbd5c4626bbba4051de544c29d`.
B:s bytes och fullstat var oförändrade före/efter. Detta är enbart rena
format-/configmodellprov; inget Git-subprocessanrop, ingen faktisk observer,
produkt-, grind- eller H039-credit. Verkliga attribut-/observerfall återstår.

### H039: verkligt observermetodprov och bevarad fyrfilshållpunkt — 2026-09-12

Ovanstående återstående metodprov har därefter körts en gång, före användarens
senaste cleanupmeddelande. Hashbunden metod
`/private/tmp/nortropic-v313-contract.Fq5ueV/h039-asset-git-observer-method.py`
SHA256 `1eefcc7a430129348eb21ee32724b038df917380fa4a26a3bc49ff813c798541`
kördes med `env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C` och pinnad Python3.12
`-I -S -B`: faktisk exit0. Fyra små syntetiska, separata Git-fixturer användes;
ingen historisk grind eller förbrukad övergång återkördes.

Resultat: `evidence/v316-h039-continuity-review-20260912/h039-observer-causal-method-7z704bbk/method-result.json`,
SHA256 `d1163546ccd93d71d1648f98b78f418bdf091b0360f1313df909727562df4fc7`.
232 faktiska Git-subprocesser:112 för konstruktion,73 för positiv fyrfilsrelation,
46 för avvisat committed attribut,0 för avvisat ospårat attribut och1 enbart
config-stdin för avvisad config. Positivt utfall är uttryckligen
`LOCAL_IMMUTABLE_GIT_FACTS_ONLY_NOT_REMOTE_PUBLICATION_OR_PHASE_CREDIT`.
Negativfallen avvisade för sina avsedda orsaker; ofullständigt observerat prestate
är fortsatt markerat som okänt, inte omklassat till full poststate-PASS.
Resultatets `complete` och `originals_unchanged` är true. Oberoende granskare
kontrollerade resultatet. Detta kvalificerar metoden, inte den nya H039-grinden.

Den första fyrfilshållpunkten i
`/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-asset-local-8095d947-20260912`
är bevarad med gate/spec/CLI/utvecklingsdokument SHA256:
`4601259eef7bcbece63bb693799d6466e1393bafa70f12038e460cd992a7199c`,
`198767956fcfe456d67270c3706a56537a616b86b7578050b32373214c054c69`,
`5c5b0e15d0445fc0ef4c1ddbfd8f131a79312d978ce2845c919e40c9e6e82bc7`,
`a452a669a87aa1412f5acf8bf9062616f784014772bcd65f4f99705e61b8fb69`.
Snäv oberoende källgranskning fann inget ytterligare utöver den uttryckligen
ofärdiga enklare observern. Ingen formal READY, freeze eller positiv grinddom.
TEST_AUTHOR fortsätter i samma arbetsyta med B-observerns bevarade kontroller;
den ofärdiga observern ska ersättas, inte exekveras som kvalificerad grind.

Båda följande arkiv i den befintliga backupens `external/` har faktiskt packats
upp och jämförts, inte bara hashlistats:

- `h039-observer-causal-method-7z704bbk-20260912.tar.gz`, SHA256
  `71070a47d5a18f1c0c0032ab7f46f16846b7af699b5a5f68bb6262dbbd7e2a6e`;
  återställning `/private/tmp/h039-observer-backup-restore.rr4zhw`,
  fixturens `diff -rq` och metodens `cmp` exit0.
- `h039-local-asset-fourpath-4601259e-20260912.tar.gz`, SHA256
  `de61e967287894e5801c991c3f8c8c77ebdea13291412af005d8f30f12a68246`;
  återställning `/private/tmp/h039-fourpath-backup-restore.umzP2a`,
  fyra källor och fokusscript jämförda med `cmp`, exit0.

Backuprot: `/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z`.
Arkiv- och resultathasharna återkontrollerades efter meddelandeavbrottet och
stämmer. Original och återställningskopior är kvar. Backupen ligger på samma
volym; detta är inte ett bevis för skydd mot förlust av hela disken.

Användaren påminde därefter om tidigare dokumenterad cleanup och bad oss
fortsätta. Retentionsregeln och cleanupjournalen har återlästs. Begränsad
läsande storleks-/innehållskontroll är bokförd i cleanupjournalen; inga filer
har raderats. Senaste `df -k` gav15518000KiB: tung byggning/grind är fortfarande
under startgolvet, medan det separata källarbetet fortsätter. Integrationen
är oförändrat ren vid8095d947c83202e2b87801531d9f7cb1457c8719,
trädf99b66517ad41a153f46e13a2dce51559d6f796b. Ingen ny publiceringsauktoritet,
runtime-/root-/installationsåtgärd eller supervisor-resume hävdas.

### H039: B-observerport hållen för oberoende källreview — 2026-09-12

Efter modellfrågan återupptogs samma TEST_AUTHOR-tråd, inte en ny writer.
Ny stabil hållpunkt har exakt fyra M-paths, +1074/-1, inget stagat och
`git diff --check` exit0. Gate SHA256
`bc056934f5211f7e40b10d5243bfec8b8741e4e63a74acff3477324515b95b35`,
spec `198767956fcfe456d67270c3706a56537a616b86b7578050b32373214c054c69`,
CLI `5c5b0e15d0445fc0ef4c1ddbfd8f131a79312d978ce2845c919e40c9e6e82bc7`,
utvecklingsdokument `42df5d2905f4e511db4bef438c02fd821c3db16ac01fe6ca7b51ae523ba18aeb`.
Root återhashade alla fyra och läste wrapper/main/operation/observer inklusive
finally samt hela fokusscriptet. Fem B-helpers är enligt TA:s käll-/AST-kontroll
oförändrade; oberoende granskare prövar nu just portens nya deltan.

Den tidigare enklare observern är ersatt. Ny kod observerar två separata
commit-/trädkanter8095→C→P vidHEAD=P, binder spårade diskbytes/modes och index
i samma retained/postauth-led, använder slutna index/statusoperationer och
förmedlar även postauth-/closefel till riggutdata. HEAD läses utan taggpeeling.
Ren status ensam får inte beskrivas som frånvaro av ignorerade extrafiler.
Koden är ofryst; faktisk observer/main/native/fullgate är NOT_RUN.

TA:s genomförda rena fokuskörning före avbrottet gav exit0,76/76 förväntade.
Script `/private/tmp/nortropic-v313-contract.Fq5ueV/h039-local-asset-observer-port-focused.bc056934.py`,
SHA256 `c2317aa4edad61d9fa1a2f557468012d0ca63a4a3ebfa43bb48311e2dfd8ddce`,
pinnad Python3.12 `-I -S -B`. Root har läst scriptet och återkontrollerat dess
hash, inte kört om provet. Observern är stubbad i dispatchproven; resultatet
är varken genuin preproduct-RED, grind-PASS eller ny operativ H039-credit.

Root arkiverade de fyra hållna filerna och fokusscriptet i befintlig backup:
`external/h039-local-observer-port-bc056934-20260912.tar.gz`, SHA256
`98599ae57ddc6a2cd4acf894fcddf0afea9160bc5553a612a4695e43961edf45`.
Faktisk uppackning till `/private/tmp/h039-observer-port-restore.WRYrHe` och
fem `cmp` under `set -e` gav exit0. Arkiv800KiB, uppackning3424KiB.
Original, äldre hållpunkter och samtliga återställningskopior är kvar.

Senaste df vid återupptagning14463976KiB. Tung byggning/grind startas inte;
källreview och små avgränsade förberedelser fortsätter. Ingen modellinställning
ändrades av rådgivningssvaret. Ingen cleanup, publicering, installation eller
runtime-/supervisoråtgärd ingår i denna hållpunkt.

Oberoende källdeltareview avslutad på samma bc056934-hållpunkt: inga bekräftade
blockerare i de begärda deltan. Granskarens eget read-only byte-/AST-prov gav
exit0; fem B-helpers är ordagranna,13 rena operationsassertioner håller och
samtliga fyra källhashar var oförändrade före/efter. Detta är avgränsad
källreview, inte formal gate READY eller körd tvåkantsverifikation.

Nästa metodförberedelse använder befintligt v3.16-produktbundle
`bundles/v316-h039-continuity-product-8095d94.bundle` i backuproten ovan,
återkontrollerad SHA256
`5cc302c9e867a8a74a43317150dd3a3b956207ba1c43a099fe6da512badd2279`,7024KiB.
Planerat ett separat syntetiskt repo, högst64MiB inklusive Git/loggar och
128MiB fri metodreserv, inte ett undantag från20GiB bygg-/15GiB tunggrindgolv.
Den planerade metoden gäller den faktiska observercallablen, aldrig main:
två positiva grafrelationer och negativa föräldra-/attribut-/disk-/index-/sena
postauthfall. Inert fixturetext i två återstående kontraktspaths är inte ett
antaget kontrakt. TEST_AUTHOR förbereder script för effektreview; ingen fixture
eller faktisk observerkörning är utförd vid denna notis.

### H039: faktisk tvåkantsobserver prövad — 2026-09-12

Nästa avgränsade metod är nu körd, inte bara källgranskad. Script
`/private/tmp/nortropic-v313-contract.Fq5ueV/h039-local-two-edge-observer-method.py`
SHA256 `27b6b5cc12283d4596734a52f07ea48942861199a34afb3950b78fcb39c909e4`
kördes med `/usr/bin/env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C` och
`/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12`
`-I -S -B` följt av scriptets absoluta path: faktisk exit0,42.942915584sekunder.
Före körning läste root hela scriptet och en oberoende reviewer granskade
effekterna. Första scriptversionen e55373f7 var NOT_RUN: granskaren krävde
två extra assertions så att child-cleanup-/capture-close-fel inte bara
registreras utan också underkänner metodutfallet. Exakt denna två-radsdelta
granskades till READY_METHOD_ONLY före den enda faktiska körningen.

Fixture:
`evidence/v316-h039-continuity-review-20260912/h039-local-two-edge-method-53ms1swj`.
Resultat `captures/method-result.json`, SHA256
`072ee9434d7ff9fce6101cd97ce3e6a33c061bf309cec9616b53bf1d3ffc48e3`.
Samtliga åtta `expected_outcome_observed=true`, `complete=true` och
`originals_unchanged=true`. Två positiva relationer:8095→syntetisk C→P samt
produktlös P=C. Sex negativa: fel kontraktförälder, fel produktförälder,
attribut endast i C, diskändring dold av skip-worktree, fel index-OID och
sen aktiv mutation av redan snapshotad manifest/index. Observerstarter i
denna ordning:570,381,527,527,527,567,568,568;5022 Python-observerade
Gitstarter inklusive konstruktion. Ingen fullständig OS-processinventering
eller efterkommandegaranti härleds från detta antal.

Sista fallet gav verkligt Gitfel128 (`index file corrupt`) samt separata
postauthfel för indexbytes, manifestbytes och respektive FD/name-identitet.
Inga extra child-cleanup-, capture-close- eller retained-close-fel accepterades.
Övriga observationer ändrade inte fixturen. Sista aktiva felinjektionens två
ändrade filer är bevarade i fixturen; ingen reset/reparation/cleanup har gjorts.
Fixturens storlek34240KiB ligger inom metodens64MiB-gräns. De fyra hållna
källorna, B-källan, historiskt material, bundle och verktygsinputs var oförändrade.

Detta är `SYNTHETIC_TWO_EDGE_OBSERVER_ONLY_NOT_FROZEN_CONTRACT_PRODUCT_BUILD_OR_GATE_PASS`.
Två C-filer har uttryckligen inert fixturetext, inte ett fryst/antaget kontrakt.
Det finns ingen ny nativebyggning, laddning, main-/fullgatekörning,
publiceringsauktoritet eller operativ H039-/bootstrapcredit. Ignorerade
extrafilers frånvaro är inte bevisad av kontrollen av spårade diskbytes/index.
En separat resultatreconciliation är beställd hos den oberoende granskaren.

Root skapade backup i befintlig backuprots `external/`:
`h039-local-two-edge-method-53ms1swj-20260912.tar.gz`, SHA256
`2e4f1322a49e4a3a3d2a0339f808dfe14652fc3aa442aee5ef27274ca9e846b6`.
Faktisk uppackning till `/private/tmp/h039-two-edge-backup-restore.dEndwJ`,
`diff -rq` för hela fixturen och `cmp` för scriptet under `set -e` gav exit0.
Original, felinjektionens slutläge, råresultat och återställning finns kvar.
Samma volym: inte offhost-katastrofskydd. Senaste df före metod14328448KiB;
tunga bygg-/grindstarter är fortsatt under diskreglernas startgolv.

TEST_AUTHOR fortsätter samma sexpathsuppgift med minsta källsteg för kopplingen
mellan denna observer och redan prövade B-material-/reseal-kontroller.
Historiska byggresultat får inte ersätta ny byggkvalificering. Inga produkt-,
installerade eller historiska H039-arbetsbytes ändrades av metodkörningen.

Oberoende resultatreconciliation därefter avslutad: samtliga åtta captures,
5022 subprocessposter och bevarade mutationsbytes överensstämmer. Två positiva
och sex kausala negativa fall bekräftade; latefault har de sex förväntade
byte-/FD-/name-felen utan extra resursfel. Ingen omkörning eller bredare credit.

### H039: materialkoppling till observerfakta hållen — 2026-09-12

Nästa källtranche är genomförd och avgränsat oberoende granskad. Fyra M-paths
totalt +1854/-1, inget stagat, `git diff --check` exit0. Senaste tranchens
ändringar är enbart H039-prefixet och utvecklingsdokumentet; spec och CLI-pinnen
är oförändrade från föregående hållpunkt. Slutliga SHA256:

- gate `dbd51ba7ec70a33bf53e74252a5b338aa0106fc267f1ee0c431272210415792a`;
- spec `198767956fcfe456d67270c3706a56537a616b86b7578050b32373214c054c69`;
- CLI `5c5b0e15d0445fc0ef4c1ddbfd8f131a79312d978ce2845c919e40c9e6e82bc7`;
- utvecklingsdokument `0433b4362217187a0d9f9181d2013d00db65ac5293b7a05f34730a35360f71d9`.

13 rena B-definitioner återbrukas ordagrant från aa9f5147. Ny
`h039_local_material_binding` korsbinder B/C/P-träd, basmaterial, kandidatdisk,
modes/blob-OID och oförändrad retained runtime från samma slutförda observer.
Observern och dess operationer är AST-oförändrade från bc056934-metodsubjektet.
Main lämnar byggutdata/adapterindata osatta: inget positivt exit0 införs.
Historisk gate utanför prefixet är fortsatt exakt bevarad. F3/F6/REFREEZE,
produkt och gamla H039-arbetsytor är oförändrade.

TEST_AUTHOR körde faktiskt pinnad Python3.12 `-I -S -B` med
`/private/tmp/nortropic-v313-contract.Fq5ueV/h039-local-material-binding-focused.dbd51ba7-0433b436.py`,
exit0 och44/44. Script SHA256
`ef2993918a98cc3c5ea54eaf35a459e3c96b40cfefdc5e052c5e20be435ea71f`;
samma stem `.result.json`, SHA256
`70b50c5431b7ec2378b1f3cc2ccba08330ef9e188ce303a8b0110edfdceb32ac`,
bär exakt kommando, exit och utfall. Root läste hela script/resultat och
återhashade fyra källor. Oberoende reviewer bekräftade26 helperbyte-/AST-kontroller,
historisk byteprojektion och17 rena kopplingsfall; fel bas, disk/mode, runtime,
korsade material och giltigt omslutet men semantiskt felaktigt container-material
avvisas för rätt orsaker. Fakta c/d är uttryckligen syntetiska minnesmodeller.
Ingen observer/main/fullgate/native/build körs av fokusscriptet. Föregående
fokusscript69e79c0c… finns kvar och hade enligt TA44/44 på föregående docversion;
den sista ändringen klargör bara kodgren kontra faktisk NOT_RUN-main/RED.

Slutlig avgränsad heldreview: inga nya blockerare i denna källtranche.
Detta är INTE freeze/produkt-/bygg-/proveniens-/gatecredit. Kvar före full positiv
assetkedja: gateägd färsk materialleverans, verifierbar konsumtionsproveniens,
F3/F6 och kvittokoppling samt riktig aktuell preproduct-RED och föreskriven review.
Den gamla B-byggdrivern är uttryckligen MEASUREMENT_ONLY och dess
active_external_same_uid_consumption_provenance är UNPROVEN; även en ny
byggmätning ensam löser alltså inte provenienskravet. Ingen ny generell
styrmodell eller tillitsförsvagning infördes för att passera denna gräns.

Backup `external/h039-local-material-binding-dbd51ba7-20260912.tar.gz` i
befintlig backuprot har SHA256
`30439948a194dda91c87ebbee1dad260393d84fd0d6db25152326437931f98d2`.
Faktisk återställning `/private/tmp/h039-material-binding-backup-restore.ph1Ukm`
och sju `cmp` under `set -e` gav exit0: fyra källor, två fokusscript och det
aktuella resultatet. Tidigare hållpunkter/metodevidens kvar. Samma volym,
inte offhost-backup. Integrationen återkontrollerades ren på8095d947 och utan
stagade ändringar. ORIGIN_MAIN är fortsatt OVERIFIERAT; ingen nätverkskontroll.

Senaste df14194144KiB (~13,5GiB). Ingen tung grind eller färsk byggning startad:
15GiB tunggrindgolv och20GiB bygggolv kvarstår. Inget raderat, ingen publication,
installation, operativ retry, runtime eller supervisor-resume utfört.
