from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from library.models import Author, Book


def create_author(name):
    """
    Creates an author with the specified `name`
    :param name: The name of the author
    :return: The created author
    """
    return Author.objects.create(name=name)


class AuthorViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse("library:authors-list")

        return super().setUp()

    def test_author_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_detail(self):
        author = create_author("Deitel")
        response = self.client.get(author.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Deitel")

    def test_author_create(self):
        response = self.client.post(self.list_url, {"name": "Gandalf the White"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Gandalf the White")

    def test_author_update(self):
        author = create_author("Deitel")
        response = self.client.put(author.get_absolute_url(), {"name": "Paul Deitel"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Paul Deitel")

    def test_author_delete(self):
        author = create_author("Deitel")
        author_amount_before_delete = Author.objects.count()

        response = self.client.delete(author.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.count(), author_amount_before_delete - 1)


def create_book(name, edition, publication_year):
    """
    Creates a book with the specified parameters
    :param name: The books name
    :param edition: The books edition
    :param publication_year: The books publication year
    :return: The created book
    """
    book = Book.objects.create(name=name, edition=edition, publication_year=publication_year)
    return book


class BookViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse("library:books-list")

        return super().setUp()

    def test_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail(self):
        book = create_book("Java How to Program", 1, 2018)
        book.authors.add(create_author("Paul Deitel"))
        response = self.client.get(book.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Java How to Program")

    def test_book_create(self):
        author = create_author("Martin C. Brown")
        response = self.client.post(self.list_url, {"name": "Python: The Complete Reference", "publication_year": 2018,
                                                    "edition": 1, "authors": [author.pk]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Python: The Complete Reference")

    def test_book_update(self):
        author = create_author("Paul Deitel")
        book = create_book("Java How to Program", 1, 2018)
        book.authors.add(author)
        response = self.client.put(book.get_absolute_url(), {"name": "Python: The Complete Reference", "edition": 1,
                                                             "publication_year": 2018, "authors": [author.pk]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Python: The Complete Reference")

    def test_book_delete(self):
        book = create_book("Java How to Program", 1, 2018)
        book_amount_before_delete = Book.objects.count()

        response = self.client.delete(book.get_absolute_url())
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), book_amount_before_delete - 1)
