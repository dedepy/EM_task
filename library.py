import json
import os
from lib_f import add_book, remove_book,change_book_status,search_books,print_book,display_books
from load_save import load_library, save_library



# Основная функция
def main():
    library = load_library()
    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("0. Выход")
        choice = input("Выберите действие: ")
        #В зависимости от инпута выбирается исполняемая функция
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            change_book_status(library)
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: некорректный выбор.")

if __name__ == "__main__":
    main()
