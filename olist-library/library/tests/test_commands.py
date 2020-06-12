import os
import csv
from io import StringIO
from conf.settings import BASE_DIR

from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):
    def setUp(self):
        self.file_dir = os.path.join(BASE_DIR, "authors.csv")

        file = open(self.file_dir, "r")
        self.reader = csv.reader(file)
        return super().setUp()

    def test_can_import_authors(self):
        out = StringIO()
        options = {"file": self.file_dir}

        next(self.reader)
        row_count = sum(1 for row in self.reader if row)

        call_command("import_authors", stdout=out, **options)

        # Check if the text below is IN the output value of the management command
        self.assertIn(f"Successfully imported {row_count} author(s) from CSV file", out.getvalue())
