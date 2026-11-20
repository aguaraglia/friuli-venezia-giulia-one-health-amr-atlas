# Ambito pubblico del Friuli Venezia Giulia One Health AMR Atlas

Edizione `fvg_amr_atlas`, pubblicata da Codex Vitae ETS. Il runtime carica soltanto le fonti `public_approved`.

La base pubblica comprende:

- confini ISTAT generalizzati al 1 gennaio 2026, letti in UTF-8: 215 comuni, 4 unità territoriali sovracomunali (Udine, UD 030; Gorizia, GO 031; Trieste, TS 032; Pordenone, PN 093) e la regione 06. I nomi bilingui (per esempio «Duino Aurisina-Devin Nabrežina») non sono ricodificati;
- sei indicatori AR-ISS 2024 (sangue e liquor), con numerosità, percentuale e intervallo di confidenza. Copertura 100%, rete regionale (laboratori ASFO Pordenone, ASUGI Trieste, ASUFC Udine). Licenza CC BY 4.0. CRAS ha meno di 20 isolati. Nessun downscaling comunale. È la fonte principale di resistenza di questa edizione, insieme al consumo J01;
- confezioni e spesa degli antibatterici J01 dagli Open Data AIFA 2024 (convenzionata e acquisti diretti, codreg 060), CC BY 4.0: consumo, non resistenza e non DDD;
- scheda ARPA FVG / Ecoscienza 3/2025 sul progetto pilota AMR in acque reflue e superficiali (5+5 depuratori non nominati), CC BY-NC-SA 4.0, senza mappa. Attribuzione: «Fonte: Laboratorio Arpa FVG, "Studi innovativi di Arpa FVG sulle acque reflue urbane", Ecoscienza 3/2025, pp. 28-30, CC BY-NC-SA 4.0». Il file derivato è distribuito con la stessa licenza, solo per usi non commerciali;
- due strutture sanitarie nominate, georiferite con Nominatim il 20 novembre 2026 (ODbL 1.0, © OpenStreetMap contributors): Ospedale di Cattinara e IRCCS Burlo Garofolo, Trieste;
- 8 studi con collegamento territoriale esplicito (20 novembre 2026), nei sei layer di evidenza. 4 studi riguardano Trieste, 1 la provincia di Pordenone e 3 la regione. Udine e Gorizia: 0 studi con luogo provinciale esplicito. Il layer umano ha 3 elementi e 4 studi. Il veterinario ha 1 elemento, la fauna selvatica 1. I layer alimentare e ambientale sono vuoti: nessuna evidenza pubblicata, non resistenza zero. Il segnaposto indica dove è stato condotto lo studio, non una prevalenza.

La letteratura con luogo esplicito è scarsa: molti lavori di Udine e di Trieste sono multicentrici senza una quota FVG separata e restano fuori dal catalogo. L'edizione si appoggia soprattutto ad AR-ISS 2024 (copertura 100%) e ad AIFA Open Data 2024 J01 (CC BY 4.0).

Non sono pubblicati i materiali di ARCS / Rete Cure Sicure FVG, della Regione Autonoma Friuli Venezia Giulia, di ASUGI, ASUFC, ASFO, del sito del Burlo, il cruscotto IZSVe né il PDF OsMed: vedi `EXCLUDED_SOURCES.md`. Non ci sono record individuali, identificativi di paziente o campione, né coordinate di RSA, aziende agricole, allevamenti o depuratori non nominati.
