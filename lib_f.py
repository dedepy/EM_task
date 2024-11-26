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
        book_id=1
    library.append({"id": book_id, "title": title, "author": author, "year": year, "status": "в наличии"})
    save_library(library)
    print(f"Книга '{title}' добавлена с ID {book_id}.")