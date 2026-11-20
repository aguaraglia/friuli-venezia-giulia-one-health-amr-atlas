#!/usr/bin/env python3
"""Build Friuli Venezia Giulia study evidence layers from the curated literature catalog.

Geometries come from the ISTAT 2026 boundaries of this edition, from a named
facility geocoded on OpenStreetMap Nominatim (1 req/s, 2026-11-20, raw
responses in raw/nominatim/). The script does not geocode farms, kennels or shelters and does not
invent a site the catalog does not name.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = "Il segnaposto indica dove è stato condotto lo studio, non una prevalenza."
SECTOR = {
    "healthcare_amr": "AMR clinica",
    "human_antimicrobial_use": "Consumo di antimicrobici",
    "antimicrobial_stewardship": "Stewardship antimicrobica",
    "veterinary_amr": "AMR veterinaria",
    "companion_animal_amr": "AMR negli animali d'affezione",
    "environmental_amr": "AMR ambientale",
    "foodborne_amr": "AMR alimentare",
    "wildlife_amr": "AMR nella fauna selvatica",
}
# Strutture nominate geocodificate su Nominatim il 2026-11-20 (raw/nominatim/results_2026-11-20.json).
POINTS = {
    "cattinara": (13.8275253, 45.6335651, "Ospedale di Cattinara, Trieste (ASUGI)",
                  "Coordinate: OSM Nominatim, amenity=hospital 'Ospedale di Cattinara', Strada di Fiume 447, Trieste, 2026-11-20."),
    "burlo": (13.7842799, 45.6359387, "IRCCS materno-infantile Burlo Garofolo, Trieste",
              "Coordinate: OSM Nominatim, amenity=hospital 'IRCCS Materno Infantile Burlo Garofolo', Via dell'Istria, Trieste, 2026-11-20."),
}
ORGANISM = {
    "pubmed_28265870": "batteri da emocoltura (resistenze) e consumo di antibiotici in DDD",
    "pubmed_42792026": "stewardship carbapenem-sparing in Medicina interna",
    "pubmed_31888282": "resistoma delle superfici ospedaliere (84 geni di resistenza, qPCR) e NGS",
    "pubmed_38752207": "programma di stewardship antimicrobica (consumo e resistenze)",
    "pubmed_24766037": "prescrizioni di antibiotici sistemici in gravidanza",
    "pubmed_30597175": "prevalenza d'uso di antimicrobici e infezioni correlate all'assistenza (PPS ECDC)",
    "pubmed_31881675": "uso di antimicrobici negli allevamenti da latte",
    "pubmed_41599081": "batteri resistenti e geni di resistenza in rondoni (Apus spp.)",
}

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def feature(geometry, place, level, basis, studies, extra_note=""):
    note = NOTE + (" " + extra_note if extra_note else "")
    return {"type": "Feature", "geometry": geometry, "properties": {
        "place": place, "geography_level": level, "geography_basis": basis,
        "study_count": len(studies), "study_ids": "; ".join(s["id"] for s in studies),
        "authors": " | ".join(s["authors"] for s in studies), "year": " | ".join(s["year"] for s in studies),
        "title": " | ".join(s["title"] for s in studies), "sector": " | ".join(s["sector"] for s in studies),
        "organism": " | ".join(s["organism"] for s in studies), "doi": " | ".join(s["doi"] for s in studies),
        "geography_note": note}}

def point(key):
    lon, lat, _l, _s = POINTS[key]
    return {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]}

def place_basis(key, text):
    return f"{text} {POINTS[key][3]}"

def merge(geoms):
    if len(geoms) == 1:
        return geoms[0]
    polys = []
    for g in geoms:
        polys.extend([g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"])
    return {"type": "MultiPolygon", "coordinates": polys}

def main():
    catalog = load_json(ROOT / "public/data/literature-catalog.json")
    by_id = {r["id"]: r for r in catalog["records"]}
    miss = set(by_id) - set(ORGANISM)
    if miss:
        raise SystemExit("Organismo mancante: " + ", ".join(sorted(miss)))

    def card(sid):
        r = by_id[sid]; doi = r.get("doi") or ""
        return {"id": sid, "authors": r["authors"], "year": str(r["year"]), "title": r["title"].rstrip("."),
                "sector": SECTOR[r["scope"]], "organism": ORGANISM[sid],
                "doi": f"https://doi.org/{doi}" if doi else r["source_url"]}

    mun = {f["properties"]["name"]: f["geometry"] for f in load_json(ROOT / "public/geography/atlas_municipalities.geojson")["features"]}
    prov = {f["properties"]["name"]: f["geometry"] for f in load_json(ROOT / "public/geography/atlas_provinces.geojson")["features"]}
    region = load_json(ROOT / "public/geography/atlas_region.geojson")["features"][0]["geometry"]

    layers = {k: [] for k in ["human", "veterinary", "food", "environment", "wildlife", "regional"]}
    placed = {}

    def add(layer, ids, geometry, place, level, basis, extra=""):
        for sid in ids:
            placed[sid] = placed.get(sid, "") + f"{level}: {place}; "
        layers[layer].append(feature(geometry, place, level, basis, [card(s) for s in ids], extra))

    P = lambda *ids: [f"pubmed_{i}" for i in ids]
    add("human", P("28265870", "42792026"), point("cattinara"), POINTS["cattinara"][2], "struttura",
        place_basis("cattinara", "Ospedale universitario di Trieste / Cattinara nominato nell'abstract o nel testo integrale."),
        "Per lo studio 2008-2014 l'allora AOU di Trieste comprendeva anche l'Ospedale Maggiore: il segnaposto è la sede principale.")
    add("human", P("31888282"), point("burlo"), POINTS["burlo"][2], "struttura",
        place_basis("burlo", "IRCCS Burlo Garofolo nominato nel testo integrale (campionamenti ambientali nei reparti)."))
    add("human", P("38752207"), prov["Pordenone"], "Provincia di Pordenone (area sanitaria ASFO)", "provincia",
        "Programma di stewardship nell'area sanitaria di Pordenone (ospedale hub e principale spoke, circa 312.000 abitanti). Il poligono ISTAT della provincia approssima l'area ASFO.")
    add("wildlife", P("41599081"), mun["Trieste"], "Trieste (centro di recupero fauna selvatica 'Liberi di Volare')", "comune",
        "Centro di recupero nominato nel testo integrale, senza indirizzo verificato: si usa il poligono ISTAT del comune di Trieste.",
        "I rondoni sono migratori: il luogo è quello del campionamento, non dell'acquisizione dei batteri.")
    add("regional", P("24766037", "30597175"), region, "Friuli Venezia Giulia", "regione",
        "Studi su tutta la regione (database amministrativi regionali; tutti gli ospedali per acuti). Il contorno regionale non è un punto di misura.")
    add("veterinary", P("31881675"), region, "Friuli Venezia Giulia (allevamenti da latte non localizzati)", "regione",
        "Allevamenti MS e LS tutti in Friuli Venezia Giulia secondo il testo integrale; nessun allevamento localizzato.")

    if set(placed) != set(by_id):
        raise SystemExit(f"Copertura incompleta. Mancanti: {sorted(set(by_id)-set(placed))}. Extra: {sorted(set(placed)-set(by_id))}")
    names = {"human": "human_amr_evidence.geojson", "veterinary": "veterinary_amr_evidence.geojson",
             "food": "food_chain_amr_evidence.geojson", "environment": "environmental_amr_evidence.geojson",
             "wildlife": "wildlife_amr_evidence.geojson", "regional": "regional_study_outline.geojson"}
    for k, fn in names.items():
        (ROOT / "public/data" / fn).write_text(json.dumps({"type": "FeatureCollection", "features": layers[k]}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(fn, len(layers[k]), sum(f["properties"]["study_count"] for f in layers[k]))
    print("studi collocati:", len(placed))

if __name__ == "__main__":
    main()
