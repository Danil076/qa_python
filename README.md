# qa_python
Реализованные тесты:

1. test_add_new_book_add_one_book:
Проверяет, что метод add_new_book корректно добавляет одну книгу в словарь books_genre.

2. test_set_book_genre_set_genre_for_existing_book:
Проверяет, что метод set_book_genre устанавливает жанр для существующей книги.

3. test_get_book_genre_returns_correct_genre (параметризованный):
Параметризованный тест, проверяющий метод get_book_genre в трёх сценариях:
- Книга с установленным жанром
- Книга без жанра (пустая строка)
- Несуществующая книга (возвращает None)

4. test_get_books_with_specific_genre_returns_correct_books (параметризованный):
Параметризованный тест, проверяющий метод get_books_with_specific_genre:
- Поиск книг с жанром 'Фантастика'
- Поиск книг с жанром 'Комедии' (которых нет)
- Поиск книг с несуществующим жанром 'Романы'

5. test_get_books_genre_return_dictionary_books_genre:
Проверяет, что метод get_books_genre возвращает весь словарь с книгами и их жанрами.

6. test_get_books_for_children_returns_suitable_books:
Проверяет, что метод get_books_for_children возвращает только книги без возрастного рейтинга (исключает 'Ужасы' и 'Детективы').

7. test_add_book_in_favorites_add_two_books:
Проверяет, что метод add_book_in_favorites добавляет две книги в список избранного.

8. test_delete_book_from_favorites_delete_one_book:
Проверяет, что метод delete_book_from_favorites удаляет одну книгу из избранного, оставляя остальные.

9. test_get_list_of_favorites_books_returns_correct_favorites:
Проверяет, что метод get_list_of_favorites_books возвращает корректный список избранных книг.

Все тесты прошли успешную проверку.

