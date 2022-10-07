from email.policy import default
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    isbn = models.TextField(default='', max_length=13, blank=True)
    description = models.TextField(default='', blank=True)
    condition = models.TextField(default='', blank=True)
    price = models.FloatField(default = 0.00, blank=True)
    link_to_buy = models.URLField(blank=True)
    is_in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)

    class Meta:
        db_table="Login"