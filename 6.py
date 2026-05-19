import ifcopenshell
import ifcopenshell.util.element

file_path = r"C:\Users\diiim\Desktop\Учебка политех\1 курс_2сем\PythonProject\Example_1.ifc"

model = ifcopenshell.open(file_path)

walls = model.by_type("IfcWall")

if walls:
    first_wall = walls[0]
    original_name = first_wall.Name
    print("Исходное имя первой стены:", (original_name))

    new_name = "MODIFIED_" + str(original_name)
    first_wall.Name = new_name
    print("Новое имя:", (first_wall.Name))

    psets = ifcopenshell.util.element.get_psets(first_wall)
    if "Pset_WallCommon" in psets:
        print("Исходные свойства:", psets["Pset_WallCommon"])

    output_file = "_modified.ifc"
    model.write(output_file)
    print("Модель сохранена в файл:", (output_file))

    print("Проверка")
    model2 = ifcopenshell.open(output_file)
    walls2 = model2.by_type("IfcWall")
    print("Имя первой стены в новом файле:", (walls2[0].Name))

    psets2 = ifcopenshell.util.element.get_psets(walls2[0])
    if "Pset_WallCommon" in psets2:
        print("Свойства Pset_WallCommon:", psets2["Pset_WallCommon"])
else:
    print("Стены не найдены!")