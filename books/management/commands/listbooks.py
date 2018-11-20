import json

from django.core.management import BaseCommand
from django.core.management.base import CommandError

from books.models import Book


class Command(BaseCommand):
    help = 'Provides loading fixtures from json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--ordering',
            help='An ordering (by publish date) type: asc/desc.',
        )

    def handle(self, *args, **options):
        if options['ordering'] == 'desc':
            books = Book.objects.order_by('-published_date', '-pk')
        elif options['ordering'] == 'asc':
            books = Book.objects.order_by('published_date', 'pk')
        elif not options['ordering']:
            books = Book.objects.all()
        else:
            raise CommandError('Please set correct ordering value: asc/desc')

        for book in books:
            self.stdout.write(f'{book}')
