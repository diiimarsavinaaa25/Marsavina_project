import ifcopenshell


file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")
print("Число стен в модели:", len(walls))