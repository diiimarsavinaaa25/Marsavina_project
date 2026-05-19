import ifcopenshell


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

storeys = model.by_type("IfcBuildingStorey")
# walls
# doors
# window


print("Схема IFC:", model.schema)
print("Этажей:", len(storeys))

# Вывод информации о каждом этаже
print("\nСписок этажей:")
for storey in storeys:
    name = storey.Name
    elevation = storey.Elevation if storey.Elevation else "None"
    print("Этаж:", name, "Отметка:", elevation)

# Заголовок
print("\nЗаголовок: Количество этажей и отметки")