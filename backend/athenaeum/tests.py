from django.test import TestCase
from .models import Book

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="Test book", authors="Test authors")

    def test_author_persists(self):
        testBook = Book.objects.get(title="Test book")
        self.assertEqual(testBook.authors, "Test authors")

    def test_book_title_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_book_authors_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')

    def test_book_ispn_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('ispn').verbose_name
        self.assertEqual(field_label, 'ispn')

    def test_book_description_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_book_condition_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('condition').verbose_name
        self.assertEqual(field_label, 'condition')

    def test_book_price_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_book_linkToBuy_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('linkToBuy').verbose_name
        self.assertEqual(field_label, 'linkToBuy')

    def test_book_isInStock_label(self):
        testBook = Book.objects.get(id=1)
        field_label = testBook._meta.get_field('isInStock').verbose_name
        self.assertEqual(field_label, 'isInStock')