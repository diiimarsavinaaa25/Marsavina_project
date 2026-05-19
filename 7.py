import ifcopenshell


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)
model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")
print("Всего дверей в модели:", len(doors))

min_width = 900
wide_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    if width is not None and width >= min_width:
        wide_doors.append(door)
        print("Дверь:", name, "Ширина:", round(width), "Высота:", height)

print("Найдено широких дверей (>= 900 мм):", len(wide_doors))


new_model = ifcopenshell.file(schema=model.schema)

print("Копируем широкие двери в новую модель")
for door in wide_doors:
    new_model.add(door)

output_file = "doors_wide.ifc"
new_model.write(output_file)
print("Новая модель сохранена в файл:", output_file)

print("Проверка:")
check_model = ifcopenshell.open(output_file)
check_doors = check_model.by_type("IfcDoor")
print("Дверей в новом файле:", len(check_doors))

all_ok = True
for door in check_doors:
    width = getattr(door, "OverallWidth", None)
    if width is not None and width < min_width:
        all_ok = False
        print("Ошибка: Дверь", door.Name, "имеет ширину", width)
if all_ok:
    print("Все двери соответствуют критерию (>= 900 мм)")
else:
    print("Обнаружены двери, не соответствующие критерию!")