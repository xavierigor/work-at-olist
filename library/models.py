from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Author(models.Model):

    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("library:authors-detail", kwargs={"pk": self.pk})


class Book(models.Model):

    name = models.CharField(_("name"), max_length=255)
    edition = models.PositiveSmallIntegerField(_("edition"), default=1)
    publication_year = models.PositiveSmallIntegerField(_("publication year"))
    authors = models.ManyToManyField(Author, verbose_name=_("authors"), related_name="books")

    def __str__(self):
        return f"{self.name} - {self.edition} Edition"

    def get_absolute_url(self):
        return reverse("library:books-detail", kwargs={"pk": self.pk})
