from django.db import models
from isbn_field import ISBNField

# Create your models here.


class Book(models.Model):
    """
    Model to represent book in app
    """

    title = models.CharField(max_length=100)
    authors_info = models.CharField(max_length=256)
    isbn = ISBNField(unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    published_date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}: {self.price}({self.isbn})'

    class Meta:
        ordering = ('-pk', )
