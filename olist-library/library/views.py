from rest_framework import viewsets

from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.order_by("-pk")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("-pk")
    serializer_class = BookSerializer

