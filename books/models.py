import logging

from django.db import models
from django.db.models.signals import post_delete, post_save
from django.utils import timezone

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
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.title}: {self.price}({self.isbn})'

    class Meta:
        ordering = ('-published_date', '-pk')


logger = logging.getLogger(__name__)


def log_create_update_model_action(sender, instance, created, update_fields, **kwargs):
    if created:
        logger.info(f'Created instance of Book: {instance}')
    else:
        logger.info(f'Updated instance of Book: {instance}')


def log_delete_model_action(sender, instance, **kwargs):
    logger.info(f'Deleted instance of Book: {instance}')


post_save.connect(log_create_update_model_action, sender=Book)
post_delete.connect(log_delete_model_action, sender=Book)
