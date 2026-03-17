from pymongo import MongoClient

# Подключение к MongoDB с аутентификацией
client = MongoClient('mongodb://root:abc123!@localhost:27017/')
db = client['streaming_platform']
movies = db['movies']

# Создание тестовых фильмов для анализа
movies.delete_many({})
test_movies = [
    {"title": "The Matrix", "year": 1999, "isColor": True, "comments": 35000},
    {"title": "The Dark Knight", "year": 2008, "isColor": True, "comments": 45000},
    {"title": "Inception", "year": 2010, "isColor": True, "comments": 25000},
    {"title": "Casablanca", "year": 1942, "isColor": False, "comments": 18000},
    {"title": "Schindler's List", "year": 1993, "isColor": False, "comments": 28000},
    {"title": "Psycho", "year": 1960, "isColor": False, "comments": 22000}
]
movies.insert_many(test_movies)

# Анализ цветных фильмов
color_movies = list(movies.find({"isColor": True}))
color_total = sum(m.get('comments', 0) for m in color_movies)
color_avg = color_total / len(color_movies) if color_movies else 0

# Анализ черно-белых фильмов
bw_movies = list(movies.find({"isColor": False}))
bw_total = sum(m.get('comments', 0) for m in bw_movies)
bw_avg = bw_total / len(bw_movies) if bw_movies else 0

print("=" * 60)
print("АНАЛИЗ ВОВЛЕЧЕННОСТИ: ЦВЕТНОЕ vs ЧЕРНО-БЕЛОЕ КИНО")
print("=" * 60)
print(f"\nЦветные фильмы ({len(color_movies)} шт.):")
print(f"  Всего комментариев: {color_total}")
print(f"  Среднее: {color_avg:.2f}")
print(f"\nЧерно-белые фильмы ({len(bw_movies)} шт.):")
print(f"  Всего комментариев: {bw_total}")
print(f"  Среднее: {bw_avg:.2f}")
print(f"\nРазница: {color_avg - bw_avg:+.2f}")

if color_avg > bw_avg:
    percent = ((color_avg - bw_avg) / bw_avg * 100)
    print(f"\nВЫВОД: Цветные фильмы на {percent:.1f}% популярнее")
    print("Рекомендация: инвестировать в цветной контент")
else:
    percent = ((bw_avg - color_avg) / color_avg * 100)
    print(f"\nВЫВОД: Черно-белые фильмы на {percent:.1f}% популярнее")
    print("Рекомендация: создать отдельную категорию 'Классика'")
