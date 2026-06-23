# Kyiv Flats ML Project

## Project Goal
Predict rental prices for Kyiv apartments using machine learning. The dataset was parsed from lun.ua and contains 10,362 listings with location coordinates, building characteristics, and price information.

## File Structure
```
ML_flats/
├── data/
│   ├── kyiv_flats_data.csv          # raw scraped data (10,362 rows)
│   ├── kyiv_flats_enriched.csv      # data + engineered features (10,362 rows, 28 cols)
│   ├── metro_stations.json          # Kyiv metro stations with coordinates
│   └── dnipro_kyiv_simplified.geojson  # Dnipro river polygon (5 features)
├── cache/                           # pickle caches for API results (never re-fetch)
│   ├── drive_time_cache_driving.pkl
│   ├── drive_time_cache_transit.pkl
│   ├── cache_bus_stops.pkl
│   ├── cache_grocery.pkl
│   ├── cache_supermarkets.pkl
│   ├── cache_schools.pkl
│   └── cache_parks.pkl
├── scripts/
│   └── get_dnipro.py                # script used to fetch Dnipro GeoJSON
├── main.ipynb                       # main notebook
├── parse.ipynb                      # lun.ua scraping notebook
├── CLAUDE.md
└── .env                             # not committed — holds GOOGLE_MAPS_API_KEY
```

---

## Raw Dataset: `data/kyiv_flats_data.csv`

**Shape:** 10,362 rows × 18 columns. Parsed from lun.ua.

### Column Reference

| Column | Type | Non-null | Description |
|---|---|---|---|
| `url` | str | 10,362 | lun.ua listing URL — unique identifier |
| `price` | float | 10,308 | Rental price in the listed currency |
| `currency` | str | 10,308 | `UAH` (6,848), `USD` (3,312), `EUR` (148) |
| `address` | str | 10,016 | Street address text |
| `rooms` | float | 10,307 | Number of rooms: 1–6 (modal: 1-room 4,465, 2-room 3,315) |
| `area_total` | float | 10,308 | Total area m² (median 54, range 9–5,600) |
| `area_living` | object | 10,255 | Living area m² — stored as string, needs casting |
| `area_kitchen` | object | 10,255 | Kitchen area m² — stored as string, needs casting |
| `floor` | object | 10,308 | Floor number as string (e.g. `"5"`) |
| `total_floors` | float | 10,304 | Total floors in the building |
| `build_year` | float | 8,358 | Year built (range 1835–2026, 2,004 nulls) |
| `construction_tech` | str | 9,438 | Building tech (Ukrainian): цегляна / монолітно-каркасна / панельна / блочна / утеплена панель |
| `heating_type` | str | 9,547 | Heating (Ukrainian): централізоване / індивідуальне / автономне |
| `lat` | float | 10,025 | Latitude — 337 rows missing coordinates |
| `lon` | float | 10,025 | Longitude |
| `district` | str | 8,923 | District name in Ukrainian (1,439 nulls). Warning: contains dirty values like street names and "Нова забудова" |
| `commission` | str | 3,480 | Agent commission text — 6,882 nulls; `"без комісії"` = no commission |
| `description` | str | 10,225 | Free-text listing description |

### Price Notes
- Prices are in three currencies — **normalise to a single currency before modelling**.
- USD price range: 300–850,000 (outliers present — max is likely a data error).
- UAH price range: 3,000–99,999; median 17,000.
- EUR price range: 270–12,000; median 1,100.

### Known Data Quality Issues
- `area_living` and `area_kitchen` are `object` dtype — cast to float before use.
- `floor` is a string — cast to int.
- `district` contains noise: some rows have street names or `"Нова забудова"` (new development) instead of a real district.
- `build_year` has 2,004 nulls and physically impossible values should be filtered (e.g. < 1850 or > 2026).
- Coordinate outliers exist — a handful of `lat`/`lon` fall outside Kyiv bounds.

---

## Enriched Dataset: `data/kyiv_flats_enriched.csv`

**Shape:** 10,362 rows × 28 columns (raw columns + 10 engineered features below).
Features are only populated for the 10,025 rows that have coordinates; the rest are NaN.

### Engineered Features

| Feature | dtype | Mean | Median | Description |
|---|---|---|---|---|
| `dist_metro_km` | float | 4.09 | 3.78 | Haversine km to nearest metro station |
| `drive_time_maidan_car_min` | float | 19.4 | 18.2 | Drive time to Maidan Nezalezhnosti (Google Distance Matrix API) |
| `drive_time_maidan_transit_min` | float | — | — | Public transport time to Maidan (Google Distance Matrix API) |
| `dist_bus_stop_km` | float | — | — | Haversine km to nearest bus/tram/trolley stop (OSM) |
| `bank_side` | str | — | — | `"right"` (west bank), `"left"` (east bank), `"river"` — determined by Dnipro polygon ray-casting |
| `dist_dnipro_km` | float | — | — | km to nearest point on Dnipro river boundary (GeoJSON polygon) |
| `dist_grocery_km` | float | — | — | km to nearest grocery / convenience store (OSM) |
| `dist_supermarket_km` | float | — | — | km to nearest major chain: Сільпо, АТБ, Варус, Новус, Ашан, Велмарт, Thrash! (OSM) |
| `dist_school_km` | float | 0.52 | 0.39 | km to nearest school (OSM) |
| `dist_park_km` | float | 0.46 | 0.37 | km to nearest park (OSM) |

---

## External APIs

- **Google Maps Distance Matrix API** — key in `.env` as `GOOGLE_MAPS_API_KEY`. Enable at `console.cloud.google.com`. Billed per element; free tier covers ~40k elements/month. Results cached in `cache/drive_time_cache_*.pkl`.
- **OpenStreetMap Overpass API** — free, no key. Three public endpoints used with automatic fallback and retry: `overpass-api.de`, `overpass.kumi.systems`, `maps.mail.ru`. Results cached in `cache/*.pkl`.

## Dependencies
```
pandas, numpy, matplotlib, seaborn
scipy          # cKDTree for fast nearest-neighbour lookup
shapely        # Dnipro polygon geometry (bank side, distance)
requests       # Overpass API
python-dotenv  # .env loading
ydata-profiling
```

## Notebook Structure (`main.ipynb`)
- **Chapter 1: Feature Engineering** — all geospatial features described above

## Notes for AI Agents
- Always use `data/` prefix for data files and `cache/` prefix for pickle files.
- Overpass query function (`overpass_query`) auto-caches — never re-fetches if the `.pkl` exists.
- Google API results are cached per mode (`driving`, `transit`) in separate pkl files.
- `bank_side` uses shapely ray-casting against `data/dnipro_kyiv_simplified.geojson`, not a simple longitude threshold.
- `area_living`, `area_kitchen`, `floor` need type casting before modelling.
- `district` column is dirty — clean or drop before using as a categorical feature.
