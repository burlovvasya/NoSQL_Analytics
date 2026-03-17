from pymongo import MongoClient
from pprint import pprint

# Подключение к MongoDB с аутентификацией
client = MongoClient('mongodb://root:abc123!@localhost:27017/')
db = client['streaming_platform']
subscriptions = db['subscriptions']

# Очистка коллекции перед вставкой
subscriptions.delete_many({})

# Создание коллекции subscriptions с документами
subscriptions_data = [
    {
        "name": "Basic",
        "price": 299,
        "quality": "SD",
        "devices": 1,
        "features": ["Доступ к каталогу", "Реклама"]
    },
    {
        "name": "Standard",
        "price": 449,
        "quality": "HD",
        "devices": 2,
        "features": ["Доступ к каталогу", "Без рекламы", "Скачивание на 1 устройство"]
    },
    {
        "name": "Premium",
        "price": 649,
        "quality": "4K UHD",
        "devices": 4,
        "features": ["Доступ к каталогу", "Без рекламы", "Скачивание на 3 устройства", "Dolby Atmos"]
    },
    {
        "name": "Student",
        "price": 199,
        "quality": "HD",
        "devices": 1,
        "features": ["Доступ к каталогу", "Реклама", "Студенческая скидка"]
    },
    {
        "name": "Family",
        "price": 799,
        "quality": "4K UHD",
        "devices": 6,
        "features": ["Доступ к каталогу", "Без рекламы", "Детский профиль", "Родительский контроль"]
    }
]

result = subscriptions.insert_many(subscriptions_data)
print(f"Добавлено {len(result.inserted_ids)} подписок")

# Проверка созданных документов
print("\n=== Все подписки ===")
for sub in subscriptions.find():
    pprint(sub)
