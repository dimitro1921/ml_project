import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt

print("Завантаження даних... (це займе близько хвилини)")

# 1. Завантажуємо всі водні об'єкти з назвою "Дніпро" в Києві
tags = {'name': 'Дніпро', 'natural': 'water'}
dnipro_gdf = ox.features_from_place("Kyiv, Ukraine", tags)

# Залишаємо тільки полігони
dnipro_polygons = dnipro_gdf[dnipro_gdf.geometry.type.isin(['Polygon', 'MultiPolygon'])]

# 2. Розбиваємо "Мультиполігон" на окремі замкнені фігури (щоб відокремити озера)
dnipro_exploded = dnipro_polygons.explode(index_parts=False)

# 3. Переводимо в метричну систему (UTM 36N) для роботи з площею та відстанню
dnipro_meters = dnipro_exploded.to_crs(epsg=32636).copy()

# 4. ФІЛЬТР 1: Видаляємо дрібні озера
# Рахуємо площу кожного шматка в квадратних кілометрах
dnipro_meters['area_sq_km'] = dnipro_meters.geometry.area / 1_000_000
# Залишаємо тільки масивні об'єкти (більше 0.5 кв. км). Дрібні острови та озера зникнуть.
main_river = dnipro_meters[dnipro_meters['area_sq_km'] > 2]

# 5. ФІЛЬТР 2: Зменшуємо точність (згладжуємо береги)
# Параметр tolerance=150 означає, що алгоритм ігноруватиме вигини берега, менші за 150 метрів
# Збільште це число (наприклад, до 300), якщо хочете ще більш "грубий" контур
simplified_river = main_river.geometry.simplify(tolerance=150)

# Повертаємо назад у координати GPS (WGS84) для збереження
final_dnipro_wgs = simplified_river.to_crs(epsg=4326)

# Зберігаємо результат
output_file = "dnipro_kyiv_simplified.geojson"
final_dnipro_wgs.to_file(output_file, driver="GeoJSON")
print(f"Готово! Спрощений полігон збережено у: {output_file}")

# Візуалізуємо, щоб ви одразу побачили різницю
final_dnipro_wgs.plot(color='dodgerblue', edgecolor='darkblue', figsize=(10, 10))
plt.title("Дніпро: Тільки головне русло (Спрощено)")
plt.axis('off')
plt.show()