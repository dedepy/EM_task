import unittest
from unittest.mock import patch
from io import StringIO
from library import add_book

class TestAddBook(unittest.TestCase):
    @patch("builtins.input", side_effect=["Book Title", "Author Name", "2023"])
    @patch("library.save_library")
    def test_add_book_success(self, mock_save_library, mock_input):
        # Начальное состояние библиотеки
        library = []

        # Выполняем функцию
        add_book(library)

        # Проверяем, что книга добавлена
        self.assertEqual(len(library), 1)
        self.assertEqual(library[0]["title"], "Book Title")
        self.assertEqual(library[0]["author"], "Author Name")
        self.assertEqual(library[0]["year"], 2023)
        self.assertEqual(library[0]["status"], "в наличии")
        self.assertEqual(library[0]["id"], 1)

        # Проверяем, что save_library вызвана
        mock_save_library.assert_called_once_with(library)

    @patch("builtins.input", side_effect=["Book Title", "Author Name", "not_a_year"])
    @patch("library.save_library")
    def test_add_book_invalid_year(self, mock_save_library, mock_input):
        # Начальное состояние библиотеки
        library = []

        # Перехват вывода
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            add_book(library)
            output = mock_stdout.getvalue()

        # Проверяем, что книга не добавлена
        self.assertEqual(len(library), 0)

        # Проверяем, что save_library не вызвана
        mock_save_library.assert_not_called()

        # Проверяем сообщение об ошибке
        self.assertIn("Ошибка: год издания должен быть числом.", output)

if __name__ == "__main__":
    unittest.main()
