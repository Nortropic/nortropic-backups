# Två stora råarkiv — avgränsat fortsatt representationsbyte

Källa är användarens direkta uppdrag i denna konversation: ”precis, fortsätt
autonomt nu med att lösa detta och sedan göra klart bootstrap, trust kernel”,
efter beskedet att GitHub ska avlasta disken utan förlust av bootstrap/kernel.
Detta är agentens dokumenterade konkreta urval inom det fortsatta backup- och
diskuppdraget, inte ett påstående om ett nytt ordagrant tvåfilsbeslut från ägaren.
Den tidigare åttafilsnotisen och dess genomförande är oförändrad historia; den
används inte som generell raderingsregel.

Urvalet är ENDAST dessa två reguljära backuprepresentationer under
`/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z/external/`:

- `scratchpad-refresh-20260910T195603Z.tar`, 2574610432 bytes,
  SHA256 e36549ff754265541ef9569c2b740ee1ca63303cd4893b9826386a23036aca6a.
- `scratchpad-refresh-20260910T202553Z.tar`, 3271506944 bytes,
  SHA256 c106845cf80c9d0657883183c00bc8256eecaedf8eab8d2a6727076ed05f54da.

Deras mindre lokala ersättningar finns i denna transferkatalog:

- `scratchpad-refresh-20260910T195603Z.tar.local-representation.gz`,
  1313152963 bytes, SHA256
  58bcc04b0a14c1ff90f8ef1faf7946d1487f07478f6e7a0a0a3c4f0b4c39e4ea.
- `scratchpad-refresh-20260910T202553Z.tar.local-representation.gz`,
  1665404714 bytes, SHA256
  25d4c02522ae19ba45c1fa2d127561f19fed0a1e2801a218b693e04f01733799.

Båda har faktiskt avkodats och jämförts byte för byte med sina oförändrade
original. Kvitton: respektive `.tar.local-encoding.json`. Kodningen ändrar inga
interna tarbytes, Git-objekt eller evidens. Gzipfilerna är lokala, inte uppladdade.
Fjärrersättningen är i stället exakt45 numrerade råsegment i privata repo
Nortropic/nortropic-backups, ID1367371291, release
`backup-20260912-large-scratchpad-segments`. Ordning, offsets, hela arkivhashar
och delhashar finns i large-external-manifest.json.

Före någon pensionering måste samtliga45 faktiska fjärråterläsningar vara klara,
slutkvittot och fjärridentiteter stämma, båda lokala kodningar återjämföras med
råfilerna, och observerbara öppna-fil-/processberoenden saknas. En fortfarande
aktiv transfer är ett stopp för just dessa två raderingar. Repo/worktree/ref,
ursprunglig scratchpad, arbetskopior, hållna källor, manifests, kvitton och den
känsliga H036-loggen ingår inte och förblir kvar.

Detta är inte pensionering av unik evidens och inte en påstådd full ny
filsystemsrestaurering. Gamla tarhashar kan återskapas exakt antingen genom lokal
gzipavkodning eller sammanfogning av rätt råsegment från GitHub. Gör detta i en
ny budgeterad återställningsyta, aldrig genom att skriva över originalarbete.
Gamla inode-/ctime-/runtimeidentiteter och förbrukade försök återfår ingen credit.

Status vid denna notis: NOT_EXECUTED. Faktiskt genomförande, om förkontrollerna
passerar, ska stå i large-raw-retirement-execution.jsonl och
large-raw-retirement-result.json. Denna förberedelsenotis skrivs inte om som ett
historiskt genomförandekvitto. Ingen generell radering, produktändring eller
runtimeflytt följer.
