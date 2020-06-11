from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):

    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField(_("name"), max_length=255)
    edition = models.PositiveSmallIntegerField(_("edition"), default=1)
    publication_year = models.PositiveSmallIntegerField(_("publication year"))
    authors = models.ManyToManyField(Author, verbose_name=_("authors"), related_name="books")

    def __str__(self):
        return f"{self.name} - {self.edition} Edition"
