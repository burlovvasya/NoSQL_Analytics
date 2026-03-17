from pymongo import MongoClient

# Подключение к MongoDB с аутентификацией
client = MongoClient('mongodb://root:abc123!@localhost:27017/')
db = client['streaming_platform']
subscriptions = db['subscriptions']

# Находим текущую цену Basic подписки
basic_subscription = subscriptions.find_one({"name": "Basic"})
if basic_subscription:
    current_price = basic_subscription.get("price")
    print(f"Текущая цена Basic: {current_price}")
    
    # Увеличиваем цену на 10%
    new_price = round(current_price * 1.1)
    result = subscriptions.update_one(
        {"name": "Basic"},
        {"$set": {"price": new_price}}
    )
    
    if result.modified_count > 0:
        print(f"Цена успешно обновлена. Новая цена: {new_price}")
        print("Изменение: +10%")
    else:
        print("Ошибка при обновлении")
else:
    print("Подписка Basic не найдена")

# Проверяем все подписки после обновления
print("\n=== Все подписки после обновления ===")
for sub in subscriptions.find():
    print(f"{sub['name']}: {sub['price']} руб.")
