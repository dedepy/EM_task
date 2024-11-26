from load_save import save_library
def add_book(library):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    try:
        year = int(input("Введите год издания книги: "))
    except ValueError:
        print("Ошибка: год издания должен быть числом.")
        return
    for book in library:
        book_id = book['id']+1
    try:
        print(book_id)
    except:
        #В случае, если библиотека пуста выдаётся id 1
        book_id=1
    library.append({"id": book_id, "title": title, "author": author, "year": year, "status": "в наличии"})
    save_library(library)
    print(f"Книга '{title}' добавлена с ID {book_id}.")

# Функция для удаления книги
def remove_book(library):
    try:
        book_id = int(input("Введите ID книги для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    for book in library:
        if book["id"] == book_id:
            library.remove(book)
            save_library(library)
            print(f"Книга с ID {book_id} удалена.")
            return
    print("Ошибка: книга с таким ID не найдена.")

# Функция для поиска книг
def search_books(library):
    query = input("Введите название, автора или год издания для поиска: ")
    try:
        query = int(query)  # Проверим, является ли запрос числом (годом)
    except ValueError:
        pass
    results = [
        book for book in library if query in (book["title"], book["author"], book["year"])
    ]
    if results:
        print("Найдены книги:")
        for book in results:
            print_book(book)
    else:
        #В случае если название книги состоти только из чисел(1984) изменение типа переменной
        query = str(query)
        results = [
            book for book in library if query in (book["title"], book["author"], book["year"])
        ]
        if results:
            print("Найдены книги:")
            for book in results:
                print_book(book)
        else:
            print("Книги не найдены.")

# Функция для изменения статуса книги
def change_book_status(library):
    try:
        book_id = int(input("Введите ID книги: "))
    except ValueError:
        print("Ошибка: ID должен быть числом.")
        return
    new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").strip()
    if new_status not in ("в наличии", "выдана"):
        print("Ошибка: некорректный статус.")
        return
    for book in library:
        if book["id"] == book_id:
            book["status"] = new_status
            save_library(library)
            print(f"Статус книги с ID {book_id} изменен на '{new_status}'.")
            return
    print("Ошибка: книга с таким ID не найдена.")

# Функция для отображения всех книг
def display_books(library):
    if not library:
        print("Библиотека пуста.")
        return
    print("Список всех книг:")
    for book in library:
        print_book(book)


# Функция для вывода информации о книге
def print_book(book):
    print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, "
          f"Год: {book['year']}, Статус: {book['status']}")