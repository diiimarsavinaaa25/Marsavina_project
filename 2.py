import ifcopenshell


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Число стен в модели:", len(walls))


first_wall = walls[0]
print("Информация о первой стене:")
print("GlobalId:", (first_wall.GlobalId))
print("Name:", (first_wall.Name))
print("ObjectType:", (first_wall.ObjectType))