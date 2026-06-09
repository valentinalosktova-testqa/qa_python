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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_books_collector_init(self):
        collector = BooksCollector()
        assert collector.books_genre == {}
        assert collector.favorites == []
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    def test_add_new_book_success(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre
        assert collector.books_genre["Война и мир"] == ''

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        long_name = "A" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.add_new_book("Война и мир")
        assert collector.books_genre["Война и мир"] == ''

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

    
  
