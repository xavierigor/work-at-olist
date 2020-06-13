from django_filters.rest_framework import filterset as filters
from library.models import Book, Author
from django_filters import ModelMultipleChoiceFilter


class BookFilter(filters.FilterSet):
    author = ModelMultipleChoiceFilter(field_name="authors", queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["name", "publication_year", "edition", "author"]
