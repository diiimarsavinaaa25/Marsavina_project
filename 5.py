import ifcopenshell


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

doors = model.by_type("IfcDoor")

min_width = 900
narrow_doors = []

for door in doors:
    name = door.Name
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)

    if width is not None and width < min_width:
        narrow_doors.append(door)
        print("Дверь:", name, "Ширина:", round(width), "Высота", height)

print
if len(narrow_doors) > 0:
    print("Найдено узких дверей:", len(narrow_doors))
else:
    print("Узких дверей не обнаружено")