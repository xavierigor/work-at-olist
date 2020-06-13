from rest_framework.test import APITestCase
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorSerializerTestCase(APITestCase):

    def setUp(self):
        self.author_attributes = {
            "name": "Paul Deitel"
        }

        self.serializer_data = {
            "name": "John Snow"
        }

        self.author = Author.objects.create(**self.author_attributes)
        self.serializer = AuthorSerializer(instance=self.author)

        return super().setUp()

    def test_contains_expected_fields(self):
        data = self.serializer_data
        self.assertEqual(set(data.keys()), {"name"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], self.author_attributes["name"])

    def test_name_required(self):
        self.serializer_data["name"] = ""
        serializer = AuthorSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {"name"})


class BookSerializerTestCase(APITestCase):

    def setUp(self):
        self.jon_snow = Author.objects.create(name="Jon Snow")
        self.deitel = Author.objects.create(name="Paul Deitel")
        self.book_attributes = {
            "name": "Java How to Program",
            "edition": 1,
            "publication_year": 2018
        }

        self.serializer_data = {
            "name": "Fevre Dream",
            "edition": 2,
            "publication_year": 2018,
            "authors": [
                2
            ]
        }

        self.book = Book.objects.create(**self.book_attributes)
        self.book.authors.set([self.jon_snow])
        self.serializer = BookSerializer(instance=self.book)
        return super().setUp()

    def test_contains_expected_fields(self):
        data = self.serializer_data
        self.assertEqual(set(data.keys()), {"name", "edition", "publication_year", "authors"})

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], self.book_attributes["name"])

    def test_name_required(self):
        self.serializer_data["name"] = ""
        serializer = BookSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), {"name", "authors"})
