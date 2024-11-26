import json
import os
# Файл для хранения данных библиотеки
LIBRARY_FILE = "library.json"

# Функция загрузки библиотеки из файла
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []

# Функция сохранения библиотеки в файл
def save_library(library):
    with open(LIBRARY_FILE, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)