from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    description = models.TextField(default='')
    isInStock = models.BooleanField(default=False)

    def __str__(self):
        return self.title