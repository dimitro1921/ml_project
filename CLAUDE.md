# Kyiv Flats ML Project

## Project Goal
Predict rental prices for Kyiv apartments using machine learning. The dataset was parsed from lun.ua and contains ~10,000 listings with location coordinates, building characteristics, and price information.

## Data
- **Source file**: `kyiv_flats_data.csv` (~10,362 rows)
- **Coordinates coverage**: ~10,025 rows have `lat`/`lon`
- **Key columns**: `url`, `price`, `currency`, `address`, `rooms`, `area_total`, `area_living`, `area_kitchen`, `floor`, `total_floors`, `build_year`, `construction_tech`, `heating_type`, `lat`, `lon`, `district`, `commission`, `description`
- **Metro stations**: `metro_stations.json` — Kyiv metro stations with coordinates, organized by line (M1 Red, M2 Blue, M3 Green)

## External APIs
- **Google Maps API** key stored in `.env` as `GOOGLE_MAPS_API_KEY`
  - Used for: drive time to Maidan Nezalezhnosti (Distance Matrix API)
- **OpenStreetMap Overpass API** (free, no key): bus stops, grocery stores, schools, parks

## Notebook Structure (`main.ipynb`)
### Chapter 1: Feature Engineering
Features derived from coordinates and building data:

| Feature | Method | Source |
|---|---|---|
| `dist_metro_km` | Haversine to nearest station | `metro_stations.json` |
| `drive_time_maidan_min` | Google Distance Matrix API | Google Maps API |
| `dist_bus_stop_km` | Haversine to nearest stop (OSM) | Overpass API |
| `district` | Already in data; NaN filled via reverse geocoding | Existing column |
| `bank_side` | `right` if lon < 30.52 else `left` | `lon` column |
| `dist_dnipro_km` | Haversine to nearest Dnipro centerline point (OSM) | Overpass API |
| `dist_grocery_km` | Haversine to nearest supermarket (OSM) | Overpass API |
| `dist_school_km` | Haversine to nearest school (OSM) | Overpass API |
| `dist_park_km` | Haversine to nearest park centroid (OSM) | Overpass API |

### Dnipro River Note
The Dnipro in Kyiv splits the city into left bank (east, ~lon > 30.52) and right bank (west). The river boundary is approximated using a set of OSM centerline points fetched via Overpass API.

## Dependencies
```
pandas, numpy, matplotlib, seaborn, python-dotenv
googlemaps          # Google Distance Matrix API
requests            # Overpass API calls
scipy               # KD-tree for fast nearest-neighbour lookup
ydata-profiling     # EDA profiling
```

## Workflow
1. Load and clean raw CSV
2. Add geospatial features (Chapter 1)
3. EDA and correlation analysis
4. Model training and evaluation

## Notes for AI Agents
- The `.env` file (not committed) holds `GOOGLE_MAPS_API_KEY`.
- Overpass API queries use `https://overpass-api.de/api/interpreter` — no auth needed.
- Google Distance Matrix API is billed per element; batch requests in groups of 25 origins and cache results to avoid re-fetching.
- `scipy.spatial.cKDTree` is used for fast nearest-neighbour lookup against large POI sets.
- The drive-time feature uses `departure_time=now` with `mode=driving` — results are cached in a pickle file to avoid repeated API calls.
- Left/right bank threshold: `lon < 30.545` is the approximate Dnipro centre in Kyiv.
