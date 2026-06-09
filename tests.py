import pytest
from main import BooksCollector

class TestBooksCollector:
    
    def test_books_collector_books_genre_init(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    def test_books_collector_favorites_init(self):
        collector = BooksCollector()
        assert collector.favorites == []

    def test_books_collector_genre_init(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_books_collector_genre_age_rating_init(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    @pytest.mark.parametrize("name, expected_in_books_genre", [
    ("Война и мир", True),
    ("", False),
    ("А" * 41, False),
    ])
    def test_add_new_book_various_names(self, name, expected_in_books_genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected_in_books_genre

    def test_add_new_book_duplicate_only_one_key(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Война и мир")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.books_genre["Война и мир"] == "Фантастика"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Несуществующий жанр")
        assert collector.books_genre["Война и мир"] == ''

    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre("Неизвестная книга", "Ужасы")
        assert "Неизвестная книга" not in collector.books_genre

    def test_get_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.get_book_genre("Война и мир") == "Фантастика"

    def test_get_book_genre_not_exists(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Отсутствующая книга") is None

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Война и мир", "Мастер и Маргарита"]

    def test_get_books_with_specific_genre_empty(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_books_with_specific_genre("Ужасы") == []

    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert collector.get_books_for_children() == ["Война и мир"]

    def test_get_books_for_children_empty(self):
        collector = BooksCollector()
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert "Война и мир" in collector.favorites

    def test_add_book_in_favorites_book_not_exists(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Нет книги")
        assert "Нет книги" not in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        collector.delete_book_from_favorites("Война и мир")
        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_book_in_favorites("Война и мир")
        assert collector.get_list_of_favorites_books() == ["Война и мир"]

    
  
