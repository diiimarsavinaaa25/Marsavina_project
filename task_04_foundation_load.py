# 1. Ввод: номер дня (1-7)
day_number = int(input("Введите номер дня недели (1-7): "))
# 2. Определить название дня и режим работы
if day_number == 1:
    day_name = "Понедельник"
    schedule = "8:00 - начало смены"
elif day_number == 2:
    day_name = "Вторник"
    schedule = "8:00 - начало смены"
elif day_number == 3:
    day_name = "Среда"
    schedule = "8:00 - начало смены"
elif day_number == 4:
    day_name = "Четверг"
    schedule = "8:00 - начало смены"
elif day_number == 5:
    day_name = "Пятница"
    schedule = "8:00 - начало смены"
elif day_number == 6:
    day_name = "Суббота"
    schedule = "Отдых"
elif day_number == 7:
    day_name = "Воскресенье"
    schedule = "Отдых"
else:
    day_name = "Неверный номер дня"
    schedule = ""
# 3. Вывод результатов
print(f"День: {day_name}")
if schedule:
    print(f"Режим: {schedule}")