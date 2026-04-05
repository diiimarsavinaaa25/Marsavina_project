# Создать словарь с 5 материалами и ценами
materials_prices = {
    "Цемент": 450,
    "Кирпич": 1200,
    "Песок": 350,
    "Щебень": 800,
    "Арматура": 2500
}
print("Исходный прайс:", materials_prices)
# Добавить 2 новых материала
materials_prices["Бетон"] = 3200
materials_prices["Доска"] = 1800
print("После добавления:", materials_prices)
# Изменить цену одного (+10%)
materials_prices["Цемент"] = materials_prices["Цемент"] * 1.10
print(f"Цена цемента увеличена на 10%: {materials_prices['Цемент']} руб")
# Удалить один материал
removed = materials_prices.pop("Песок")
print(f"Удален материал: Песок (цена: {removed} руб)")
# Рассчитать среднюю цену
price = sum(materials_prices.values()) / len(materials_prices)
print(f"\nИтоговый прайс: {materials_prices}")
print(f"Средняя цена материалов: {round(price, 2)} руб")