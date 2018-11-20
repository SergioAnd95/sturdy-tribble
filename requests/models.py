from django.db import models

# Create your models here.


class Request(models.Model):

    method = models.CharField(max_length=10, default='GET')
    path = models.CharField(max_length=256)
    status_code = models.IntegerField()
    headers = models.TextField()
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} - {self.path} - {self.status_code}'

    class Meta:
        ordering = ('-time', )
