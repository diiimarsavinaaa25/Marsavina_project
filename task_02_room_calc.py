# 1. Задать размеры
length = 5.0    # длина в метрах
width = 4.0     # ширина в метрах
height = 3.0    # высота в метрах

# 2. Рассчитать параметры
floor = length * width  # Площадь пола
walls = 2 * (length + width) * height  # Площадь стен
volume = length * width * height  # Объем помещения

# 3. Рассчитать стоимость покраски (125 руб за м²)
price_meter = 125
total_cost = walls * price_meter

# 4. Вывод результатов (округление до 2 знаков)
print(f"Площадь пола: {round(floor, 2)} м²")
print(f"Площадь стен: {round(walls, 2)} м²")
print(f"Объем помещения: {round(volume, 2)} м³")
print(f"Стоимость покраски: {round(total_cost, 2)} руб.")