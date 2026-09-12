import pytest
from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_set_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Солярис')

        collector.set_book_genre('Солярис', 'Фантастика')

        assert collector.get_book_genre('Солярис') == 'Фантастика'

    @pytest.mark.parametrize(
        'book_name, expected_genre',
        [
            ['Солярис', 'Фантастика'],
            ['Заводной апельсин', ''],
            ['Тарас Бульба', None]
        ]
    )
    def test_get_book_genre_returns_correct_genre(self, book_name, expected_genre):
        collector = BooksCollector()

        if book_name == 'Солярис':
            collector.add_new_book('Солярис')
            collector.set_book_genre('Солярис', 'Фантастика')
        elif book_name == 'Заводной апельсин':
            collector.add_new_book('Заводной апельсин')

        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
            'genre, expected_books',
            [
                ('Фантастика', ['Солярис', 'Марсианин']),
                ('Комедии', []),
                ('Романы', []),
            ]
        )
    def test_get_books_with_specific_genre_returns_correct_books(self, genre, expected_books):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.add_new_book('Марсианин')

        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Марсианин', 'Фантастика')

        result = collector.get_books_with_specific_genre(genre)

        assert result == expected_books

    def test_get_books_genre_return_dictionary_books_genre(self):
        collector = BooksCollector()
        
        collector.add_new_book('Солярис')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('12 стульев', 'Комедии')

        expected = {
        'Солярис': 'Фантастика',
        '12 стульев': 'Комедии'
        }

        assert collector.get_books_genre() == expected
    
    def test_get_books_for_children_returns_suitable_books(self):
        collector = BooksCollector()
                
        collector.add_new_book('Солярис')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_for_children() == ['Солярис']

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.add_new_book('Оно')

        collector.add_book_in_favorites('Солярис')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Солярис', 'Оно']

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        
        collector.add_new_book('Солярис')
        collector.add_new_book('Оно')
        
        collector.add_book_in_favorites('Солярис')
        collector.add_book_in_favorites('Оно')

        collector.delete_book_from_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Солярис']

    def test_get_list_of_favorites_books_returns_correct_favorites(self):
        collector = BooksCollector()
        
        collector.add_new_book('Солярис')
        collector.add_new_book('Хоббит')
        
        collector.add_book_in_favorites('Солярис')
        collector.add_book_in_favorites('Хоббит')
        
        assert collector.get_list_of_favorites_books() == ['Солярис', 'Хоббит']
