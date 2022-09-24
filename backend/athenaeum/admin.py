from django.contrib import admin
from .models import Book
from .models import Login


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'description', 'isInStock')


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Login)