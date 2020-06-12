from django.test import TestCase
from library.models import Author, Book


class ModelsTestCase(TestCase):

    def setUp(self):
        self.jon_snow = Author.objects.create(name="Jon Snow")
        self.walter_white = Author.objects.create(name="Walter White")

        self.fevre_dream = Book.objects.create(name="Fevre Dream", edition=1, publication_year=1982)
        self.fevre_dream.authors.add(self.jon_snow)

        self.the_chemistry_book = Book.objects.create(name="The Chemistry Book", edition=2, publication_year=2010)
        self.the_chemistry_book.authors.add(self.walter_white)
        return super().setUp()

    def test_author(self):
        """
        Author Model test
        """
        author_jon_snow = Author.objects.get(pk=self.jon_snow.pk)
        author_walter_white = Author.objects.get(pk=self.walter_white.pk)

        self.assertEqual(str(self.jon_snow), author_jon_snow.name)

        self.assertEqual(str(author_walter_white), author_walter_white.name)

    def test_book(self):
        """
        Book Model test
        """
        fevre_dream = Book.objects.get(pk=self.fevre_dream.pk)
        the_chemistry_book = Book.objects.get(pk=self.the_chemistry_book.pk)

        self.assertEqual(str(self.fevre_dream), f"{fevre_dream.name} - {fevre_dream.edition} Edition")
        self.assertIn(self.jon_snow, fevre_dream.authors.all())

        self.assertEqual(str(self.the_chemistry_book), f"{the_chemistry_book.name} - "
                                                       f"{the_chemistry_book.edition} Edition")
        self.assertIn(self.walter_white, the_chemistry_book.authors.all())
