import unittest
from io import StringIO
import sys
import os
# Импортируем тестируемую функцию и вспомогательные данные
from library import display_books

class TestDisplayBooks(unittest.TestCase):
    def setUp(self):
        # Сохраняем текущее состояние stdout, чтобы перенаправить вывод
        self.held_output = StringIO()
        self.default_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # Восстанавливаем стандартный stdout
        sys.stdout = self.default_stdout

    def test_display_books_with_books(self):
        # Тест с книгами
        library = [
            {"id": 1, "title": "Book One", "author": "Author A", "year": 2000, "status": "в наличии"},
            {"id": 2, "title": "Book Two", "author": "Author B", "year": 2010, "status": "выдана"}
        ]
        display_books(library)
        output = self.held_output.getvalue().strip()
        expected_output = (
            "Список всех книг:\n"
            "ID: 1, Название: Book One, Автор: Author A, Год: 2000, Статус: в наличии\n"
            "ID: 2, Название: Book Two, Автор: Author B, Год: 2010, Статус: выдана"
        )
        self.assertEqual(output, expected_output)

    def test_display_books_empty_library(self):
        # Тест с пустой библиотекой
        library = []
        display_books(library)
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "Библиотека пуста.")

if __name__ == "__main__":
    unittest.main()
