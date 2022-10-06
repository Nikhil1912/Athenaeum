from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Test book", authors="Test authors")

    def test_author_persists(self):
        testBook = Book.objects.get(title="Test book")
        self.assertEqual(testBook.authors, "Test authors")    