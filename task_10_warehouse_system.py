warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}
print("=" * 80)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 80)
print()
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("-" * 60)
total_warehouse_value = 0
most_expensive_material = None
max_value = 0
critical_items = []
# Вывод таблицы материалов
for material, data in warehouse.items():
    quantity = data["quantity"]
    price = data["price"]
    min_quantity = data["min_quantity"]
    total_cost = quantity * price
    total_warehouse_value += total_cost
    # Проверка на самый дорогой материал
    if total_cost > max_value:
        max_value = total_cost
        most_expensive_material = material
    # Проверка критических остатков
    if quantity < min_quantity:
        critical_items.append((material, quantity, min_quantity))
        print(f"{material} | {quantity} | {price} | {min_quantity} | {total_cost} ⚠ КРИТИЧ!")
    else:
        print(f"{material} | {quantity} | {price} | {min_quantity} | {total_cost}")
print("=" * 80)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_warehouse_value} руб")
print(f"Самый дорогой: {most_expensive_material} ({max_value} руб)")
# Критические остатки
if critical_items:
    print(f"⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
    for item, qty, min_qty in critical_items:
        print(f"  - {item}: {qty} < {min_qty}")
# Выдача со склада
print()
print("=== ВЫДАЧА МАТЕРИАЛА ===")
material_to_issue = "Цемент"
issue_quantity = 25
if warehouse[material_to_issue]["quantity"] >= issue_quantity:
    warehouse[material_to_issue]["quantity"] -= issue_quantity
    print(f"✓ Выдано {issue_quantity} единиц '{material_to_issue}'")
    print(
        f"Остаток: {warehouse[material_to_issue]['quantity'] + issue_quantity} → {warehouse[material_to_issue]['quantity']}")
else:
    print(f"✗ Недостаточно '{material_to_issue}' на складе!")