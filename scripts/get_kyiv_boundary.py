"""
Fetches the administrative boundary polygon for Kyiv city from Nominatim (OSM)
and saves it as data/kyiv_boundary.geojson.

Run once from the project root:
    python scripts/get_kyiv_boundary.py
"""

import json
import requests
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "data" / "kyiv_boundary.geojson"

resp = requests.get(
    "https://nominatim.openstreetmap.org/search",
    params={
        "q": "Kyiv, Ukraine",
        "format": "json",
        "polygon_geojson": 1,
        "limit": 3,
    },
    headers={"User-Agent": "kyiv-flats-ml/1.0 (research project)"},
    timeout=30,
)
resp.raise_for_status()
results = resp.json()

# Pick the result whose geometry covers the largest area (city, not suburb)
best = max(
    (r for r in results if "geojson" in r),
    key=lambda r: r.get("importance", 0),
)

print(f"Using: {best['display_name']}")
print(f"Geometry type: {best['geojson']['type']}")

geojson = {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "geometry": best["geojson"],
        "properties": {"name": "Kyiv", "osm_id": best.get("osm_id")}
    }]
}

OUTPUT.write_text(json.dumps(geojson), encoding="utf-8")
print(f"Saved → {OUTPUT}")
