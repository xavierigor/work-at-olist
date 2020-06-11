from rest_framework import serializers

from library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["name", "edition", "publication_year", "authors"]
