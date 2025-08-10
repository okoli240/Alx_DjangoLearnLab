from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user and client
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create books
        self.book1 = Book.objects.create(title='Book One', publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title='Book Two', publication_year=2010, author=self.author2)
        self.book3 = Book.objects.create(title='Another Book', publication_year=2015, author=self.author1)

    def test_list_books_unauthenticated(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check pagination or list count
        self.assertGreaterEqual(len(response.data), 3)

    def test_filter_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for book in response.data:
            self.assertIn('Book One', book['title'])

    def test_search_books_by_author_name(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Author One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book['author'] == self.author1.id for book in response.data))

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

    def test_create_book_unauthenticated(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')
        self.assertEqual(response.data['author'], self.author1.id)

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-update')
        data = {
            'id': self.book1.id,
            'title': 'Updated Title',
            'publication_year': 2001,
            'author': self.author1.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_update_book_unauthenticated(self):
        url = reverse('book-update')
        data = {
            'id': self.book1.id,
            'title': 'Should Not Update',
            'publication_year': 2001,
            'author': self.author1.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='password123')
        url = reverse('book-delete')
        data = {'id': self.book2.id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete')
        data = {'id': self.book2.id}
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_book_detail(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

