import ifcopenshell
import ifcopenshell.util.element


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

# Задание 1
walls = model.by_type("IfcWall")
print("Число стен в модели:", len(walls))


first_wall = walls[0]
print(first_wall)

psets = ifcopenshell.util.element.get_psets(first_wall)

print(psets)
for pset_name, props in psets.items():
    print("Pset:", pset_name)
    for prop_name, value in props.items():
        print("    ", prop_name, "=", value)