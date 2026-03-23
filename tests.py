import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_set_valid_genre_for_existing_book(self):
        collector = BooksCollector()

        name_book = 'Последнее убийство на земле'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, 'Детективы')
        assert collector.get_book_genre(name_book) == 'Детективы'

    def test_set_book_genre_set_unvalid_genre_for_existing_book_empty_string(self):
        collector = BooksCollector()

        name_book = 'Последнее убийство на земле'
        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, 'XXXX')
        assert collector.get_book_genre(name_book) == ''

    def test_get_book_genre_for_book_without_genre_empty_string(self):
        collector = BooksCollector()

        name_book = 'Последнее убийство на земле'
        collector.add_new_book(name_book)
        assert collector.get_book_genre(name_book) == ''

    @pytest.mark.parametrize("books, genre, result",
                             [(['Жеребий Салема', 'Оно'], 'Ужасы', 2),
                              (['Мастер и Маргарита'], 'Фантастика', 1),
                              (['Война и мир', 'Анна Каренина', 'Преступление и наказание'], 'Роман', 0)
                              ])
    def test_get_books_with_specific_genre(self, books, genre, result):
        collector = BooksCollector()

        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        specific_genre_books_lst = collector.get_books_with_specific_genre(genre)
        assert len(specific_genre_books_lst) == result

    @pytest.mark.parametrize('book, genre', [('Шрек', 'Мультфильмы'),
                                             ('Мадагаскар', 'Комедии'),
                                             ('Тачки', 'Мультфильмы')
                                             ])
    def test_get_books_for_children_return_books_with_allowed_genres(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        test_result = collector.get_books_for_children()
        assert len(test_result) == 1

    def test_add_book_in_favorites_add_one_book_in_favorites(self):
        collector = BooksCollector()

        book_one = 'Жеребий Салема'
        book_two = 'Оно'

        collector.add_new_book(book_one)
        collector.add_new_book(book_two)
        collector.add_book_in_favorites(book_one)
        assert collector.get_list_of_favorites_books() == [book_one]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        book_one = 'Жеребий Салема'
        book_two = 'Оно'

        for i in [book_one, book_two]:
            collector.add_new_book(i)
            collector.add_book_in_favorites(i)

        collector.delete_book_from_favorites(book_one)
        assert collector.get_list_of_favorites_books() == [book_two]

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()

        result = collector.get_list_of_favorites_books()
        assert result == []

