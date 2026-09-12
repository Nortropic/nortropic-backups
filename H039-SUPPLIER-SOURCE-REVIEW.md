# H039 supplier: avgränsad käll-/effektreview

2026-09-12, oberoende GATE_REVIEWER. Inga bekräftade blockerare i den hållna aee/dcd-porten. Detta är inte immutable freeze-READY, byggklartecken eller faktisk acceptanskredit. Senare rörliga efterföljare ingår inte.

## Låst underlag

Granskad arbetsyta: `/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-asset-local-8095d947-20260912`. Följande fulla SHA256 verifierades under reviewn:

- Gate: `aee154f81c871b34eb1b3bf4f79b907b7057627e669605716d1e3b159f1552d9`.
- Utvecklingsdokument: `dcd1fb68ddb87341e667698fde4396fddd22d79dbfc940318b137e3f111a3db9`.
- Spec: `198767956fcfe456d67270c3706a56537a616b86b7578050b32373214c054c69`.
- Verify CLI: `5c5b0e15d0445fc0ef4c1ddbfd8f131a79312d978ce2845c919e40c9e6e82bc7`.
- B-källa: `aa9f5147d8d1192cc3353aec9a631cc234b58e31301f698334add1a866634183`.

Bevarat delta `/private/tmp/nortropic-v313-contract.Fq5ueV/h039-local-build-supplier.aee154f8-dcd1fb68.diff`, SHA `72074a47365a74da2235a95c929f7a11b86a4b6c9e0265b590f1f0bd634ec16d`, jämfördes exakt med hela skillnaden från bevarade b921f5a5/c7196b7f-föregångare. AGENTS och gate-reviewer-SKILL lästes; relevanta regler, byggplan, aktiv plan/handoff samt evidens-/substitutionskontrakt var lästa i denna reviewkedja.

## Käll- och effektbedömning

Sex B-effekthjälpare är byte-exakta: compiler_envelope, inventory, wait_state, group_action, group_snapshot och bounded_command. Portdiffen mot B:s preflight/build_reference lästes uttryckligen. Av redan befintliga funktioner ändras endast main; materialpredikat, observer, Git-operationer och tidigare retained/ACL/close-hjälpare är oförändrade.

Main behåller samma argumentform. Endast separat produktkant och korrekt materialsnapshot går vidare till intern supplier. P=C/frånvaro stoppar före supplier, byggrotskapande och kompilator, men inte före den befintliga observern. Noarg/gamla selectors förblir avslag. Bas-mediator tas från autentiserade basmaterialfakta; retained runtime från samma observersnapshot. Ingen produktkälla återläses som bas och ingen extern adapterpath/receipt accepteras. Den inerta grindägda adaptern är 6955 bytes, SHA `a35dc310e05f7cf83d7175e5ee5ba3213e6a7433daaa7cc5dd25f9e92ff437fa`.

Suppliern skapar exklusiv privat parent och två separata lanes. Varje lane använder åtta fasta receptkommandon: sju clang och ett ld, med exakt ersättningsmiljö och deny-default-profil. Ingen genererad nativeprodukt laddas eller körs. Däremot använder granskad livscykelkod systemets ACL/libproc/waitid för metadata, ägda gruppobservationer och städning. Okänd ägarskap/identitet tillåter inte signal eller reap. Fel, rester och close-fel ger inte positiv supplierretur; filer bevaras utan automatisk omkörning eller filstädning.

Efter inventering och rotidentitetskontroll läses tio outputs per lane med retained_read, färsk digest, storleksjämförelse och högst 1 MiB per levererad output. Båda bytekartorna passerar den kausala rebuild/material-kedjan. Verktyg/headers återkontrolleras, båda fulla laneinventarierna jämförs igen efter materialpredikaten och ägda descriptors stängs före lyckad retur. Lyckad supplier ger fortfarande main exit 2 med `NOT_READY_F3_F6_RECEIPT_AND_FROZEN_ACCEPTANCE`.

300 s och 4 MiB sammanlagd stdout/stderr-capture gäller per kommando, med separat högst 10 s ägd cleanup; det är ingen övergripande wall-clockgräns för hela preflight/byggning. Child-filer begränsas till 64 MiB per fil. 20 GiB kontrolleras före skapande och varje lane. Inventariets 2 GiB efterkontroll är ingen diskkvot. Serialisering utan auktoriserad samtidig skrivare är den uttryckliga bygggränsen; universell extern same-UID-konsumtionsproveniens förblir UNPROVEN.

## Faktisk granskarevidens och gräns

TA:s redan körda fokus `/private/tmp/nortropic-v313-contract.Fq5ueV/h039-local-build-supplier-focused.aee154f8-dcd1fb68.py`, SHA `2b513080c8782654784e033e05a8ef28179044dbc71dfc5b81f981e3bc987765`, lästes helt. Resultatet med samma stem `.result.json`, SHA `dbadf16a2b22089aeed3db3c29ab5cfdbbca0a0cb6553b01fc90cbf73e3ccf3d`, avstämdes: exit 0, 125 unika sanna kontroller, raw_stdout lika parsed result. OS-, verktygs-, header- och child-effekter är där simulerade; historiska materialbytes är inte färska byggoutputs. Fokusscriptet återkördes inte av granskaren.

Egna läsande verifieringskommandon kördes med exakt prefix `/opt/homebrew/Cellar/python@3.12/3.12.13_4/Frameworks/Python.framework/Versions/3.12/bin/python3.12 -I -S -B -` och inline stdin-program i verktygsposterna `93cd4f` (exit 0, 4.507 s: sex B-definitioners exakta källa, portdiffar, befintliga funktionsdeltan och TA-resultatreconciliation) samt `12ebc6` (exit 0, 0.911 s: exakt hållen tvåfilsdiff, adapterliteral, spec/CLI-pinnar och rent recept-/profiluttag). I det senare exekverades endast reference_recipe och compiler_envelope, inga effektfulla definitioner. Det rena AST-uttagets SHA256 över `ast.dump(module, include_attributes=False)` var `81d4dd34412110dff29e80c23ffdaeeb414746108c8d76add844a516264dba63`; utfall två lanes, åtta fasta kommandon och tio outputs per lane, exakt miljö och förväntade scalargränser.

Ingen faktisk supplier, kompilering, native/query, observer, main eller fullgrind kördes av granskaren. Ingen kandidat eller produkt ändrades. Faktisk sammansatt körning, dess positiva/negativa effekter, F3/F6/receipt-bindning och fryst acceptans återstår separat. Denna rapport sparar avslutad review och granskar inte efterföljaren.
