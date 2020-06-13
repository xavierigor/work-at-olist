from django_filters.rest_framework import ModelMultipleChoiceFilter
from django_filters.rest_framework import filterset as filters

from library.models import Book, Author


class AuthorFilter(filters.FilterSet):

    class Meta:
        model = Author
        fields = ["name"]


class BookFilter(filters.FilterSet):
    author = ModelMultipleChoiceFilter(field_name="authors", queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["name", "publication_year", "edition", "author"]
