# В строках исходного текстового файла (dates1.txt) все
# даты представить в виде подстроки. Поместить в новый
# текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.

import re

# Название исходного и результирующего файлов
INPUT_FILE = "dates1.txt"
OUTPUT_FILE = "february_dates.txt"

# Регулярное выражение для поиска дат в форматах ДД.ММ.ГГГГ или ДД/ММ/ГГГГ
# \d{2} - две цифры дня, [./] - разделитель точка или слэш,
# \d{2} - две цифры месяца, \d{4} - четыре цифры года
DATE_PATTERN = r"\b(\d{2})[./](\d{2})[./](\d{4})\b"


def process_dates():
    try:
        # Чтение данных из исходного файла
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            content = file.read()

        # Поиск всех дат. findall вернет список кортежей вида ('ДД', 'ММ', 'ГГГГ')
        all_dates = re.findall(DATE_PATTERN, content)

        # Фильтрация и форматирование дат за февраль ('02') с помощью спискового включения
        # Формируем строку в требуемом формате ДД/ММ/ГГГГ
        february_dates = [
            f"{day}/02/{year}" for day, month, year in all_dates if month == "02"
        ]

        # Запись отфильтрованных дат в новый текстовый файл
        with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
            for date_str in february_dates:
                out_file.write(date_str + "\n")

        print(f"Обработка завершена успешно.")
        print(f"Всего найдено дат за февраль: {len(february_dates)}")
        print(f"Результаты сохранены в файл: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Ошибка: Исходный файл '{INPUT_FILE}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    process_dates()