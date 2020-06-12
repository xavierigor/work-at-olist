from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from library.models import Author, Book

User = get_user_model()


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
