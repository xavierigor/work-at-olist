from django.core.management.base import BaseCommand, CommandError
from library.models import Author
import csv


class Command(BaseCommand):
    help = "Imports the given csv data into the Authors table"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    def handle(self, *args, **options):
        try:
            file = open(options["file"], "r")
        except FileNotFoundError:
            raise CommandError("File not found")
        except TypeError:
            raise CommandError("A csv type file is required")

        if not file.name.endswith(".csv"):
            raise CommandError("A csv type file is required")

        reader = csv.reader(file)
        next(reader)

        try:
            authors = Author.objects.bulk_create([Author(name=row[0]) for row in reader])

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(authors)} author(s) from CSV file"))
        except:
            raise CommandError("There was an error while importing authors")
