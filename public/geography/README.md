# Geografia pubblica

La cartografia pubblica dell'edizione Friuli Venezia Giulia comprende:

- `atlas_region.geojson`: confine regionale ISTAT 2026 (codice 06);
- `atlas_provinces.geojson`: 4 unità territoriali sovracomunali ISTAT 2026 (ex province, «unità non amministrative»): Udine (UD 030), Gorizia (GO 031), Trieste (TS 032), Pordenone (PN 093);
- `atlas_municipalities.geojson`: 215 comuni ISTAT al 1/1/2026.

I file sono letti in UTF-8 dal DBF ISTAT, quindi i nomi bilingui (per esempio «Duino Aurisina-Devin Nabrežina», «Savogna d'Isonzo-Sovodnje ob Soči») sono corretti.

Gli studi della letteratura curata stanno in layer distinti sotto `public/data/`. Due strutture nominate sono geocodificate tramite OSM Nominatim: l'Ospedale di Cattinara e l'IRCCS Burlo Garofolo (Trieste). Lo studio sui rondoni usa il poligono del comune di Trieste; il programma di stewardship ASFO usa il poligono di Pordenone; gli studi regionali usano il contorno regionale. Nessuna RSA, azienda agricola, depuratore o struttura non nominata è localizzata.
