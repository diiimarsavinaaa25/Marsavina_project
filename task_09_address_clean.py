addresses = [
    "  г. Москва, ул. Ленина, д. 10  ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100  "
]
print("=== СРАВНЕНИЕ ===\n")
for i, address in enumerate(addresses, 1):
    print(f"#{i}")
    print(f"ДО: '{address}'")
    # 1. Удалить лишние пробелы (в начале и конце)
    cleaned = address.strip()
    # 2. Добавить пробелы после сокращений (г., ул., д.)
    # Заменяем "г." на "г. " если после точки нет пробела
    cleaned = cleaned.replace("г.", "г. ").replace("ул.", "ул. ").replace("д.", "д. ")
    # 3. Унифицировать запятые (добавить пробел после запятой)
    cleaned = cleaned.replace(",", ", ")
    # Убираем двойные пробелы
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    print(f"ПОСЛЕ: '{cleaned}'")
    print()