# Friuli Venezia Giulia One Health AMR Atlas

Edizione regionale `fvg_amr_atlas`, pubblicata da Codex Vitae ETS sulla stessa
base delle edizioni Piemonte e Trentino-Alto Adige.

## Stato

La letteratura pubblicata con localizzazione esplicita in Friuli Venezia Giulia
è scarsa: molti studi di Udine e di Trieste sono multicentrici e non riportano
una quota FVG separata. Ne restano 8 inclusi (20 novembre 2026): 4 a Trieste
(Ospedale di Cattinara, IRCCS Burlo Garofolo e il comune), 1 in provincia di
Pordenone e 3 a scala regionale. Udine e Gorizia non hanno studi con luogo
provinciale esplicito.

L'edizione si appoggia soprattutto ad AR-ISS 2024 (copertura 100%, rete
regionale, CC BY 4.0) e ad AIFA Open Data 2024, antibatterici J01 (CC BY 4.0).

Sei layer (AMR umana, veterinaria, alimentare, ambientale, fauna selvatica,
contorno regionale):

- AMR umana: 3 elementi, 4 studi (Cattinara, Burlo Garofolo, provincia di
  Pordenone);
- AMR veterinaria: 1 elemento (allevamenti da latte non localizzati, contorno
  regionale);
- AMR alimentare: nessun elemento;
- AMR ambientale: nessun elemento (la scheda ARPA FVG non è in mappa);
- AMR nella fauna selvatica: 1 elemento (comune di Trieste);
- studi a scala regionale: 1 elemento, 2 studi.

I layer vuoti e le aree senza segnaposto sono nessuna evidenza pubblicata,
non resistenza zero. Ogni popup cita lo studio e il DOI (o il record PubMed
se il DOI non è assegnato) e ricorda che il segnaposto è il luogo dello
studio, non una prevalenza. Due strutture nominate (Cattinara e Burlo)
© OpenStreetMap contributors, ODbL. Il poligono di Pordenone approssima
l'area sanitaria ASFO.

La scheda ARPA FVG su Ecoscienza 3/2025 (acque reflue urbane) è senza
segnaposto. Fonte: Laboratorio Arpa FVG, «Studi innovativi di Arpa FVG sulle
acque reflue urbane», Ecoscienza 3/2025, pp. 28-30, CC BY-NC-SA 4.0. Il file
derivato è distribuito con la stessa licenza, solo per usi non commerciali.

Confini ISTAT 2026 (215 comuni, 4 unità territoriali sovracomunali, regione
06), letti in UTF-8. ARCS, Regione FVG, ASUGI, ASUFC, ASFO, il sito del Burlo,
il cruscotto IZSVe e il PDF OsMed sono esclusi: vedi
`metadata/EXCLUDED_SOURCES.md`.

Il conteggio in homepage e in pubblicazioni legge
`public/data/literature-catalog.json` (8).

## Pagine

Sorgente su `main`. Il sito statico è pubblicato dal branch `gh-pages`
(GitHub Pages, cartella `/`). Nessun file `CNAME`. Analitica: GoatCounter
`https://atlanteamr.goatcounter.com/count`, come le edizioni Piemonte e
Trentino-Alto Adige.

## Build locale

```bash
python3 -m http.server 8000
```

Aprire `http://localhost:8000/`.

Per rigenerare i dati pubblici servono gli input in `raw/` e, per i confini,
l'archivio ISTAT indicato in `metadata/SNAPSHOTS.tsv`. I DBF ISTAT si leggono
in UTF-8:

```bash
pip install -r requirements-geodata.txt
python3 scripts/build_istat_geography.py --source-root <Limiti01012026_g> --output-root public/geography
python3 scripts/build_literature_catalog.py
python3 scripts/build_study_evidence_layers.py
```

## Directory

- `public/`: dati e asset approvati per il sito;
- `metadata/`: fonti, snapshot, ambito pubblico e fonti escluse;
- `raw/`: curatela, esummary e risposte Nominatim;
- `scripts/`: ricostruzione del catalogo e dei layer;
- `private/`: nessun dato riservato in questa edizione.
