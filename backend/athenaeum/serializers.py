from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'authors', 'ispn', 'description', 'condition', 'price', 'link_to_buy', 'is_in_stock')