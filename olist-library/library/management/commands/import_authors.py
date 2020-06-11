from django.core.management.base import BaseCommand, CommandError
from library.models import Author
import csv


class Command(BaseCommand):
    help = "Imports the given csv data into the Authors table"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        try:
            file = open(options["file"])
        except FileNotFoundError:
            raise CommandError("File not found")
        except TypeError:
            raise CommandError("A csv type file is required")

        reader = csv.reader(file)

        row_count = sum(1 for row in reader) - 1
        if row_count < 2:
            raise CommandError("File must have at least two rows")

        for i, row in enumerate(reader):
            # Ignores the first row of csv, because its a header
            if i > 0:
                Author.objects.create(name=row[0])

        self.stdout.write(self.style.SUCCESS(f"Successfully imported {row_count} author(s) from CSV file"))
