import json
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Book
from api.serializers import BookSerializer
from users.models import Author


class BookEndpointTestCase(APITestCase):
    def setUp(self):
        self.user = Author.objects.create_user(
            username='testuser',
            email='test@test.com',
            first_name='test',
            last_name='test',
            password='testpass'
            )
        self.book = Book.objects.create(
            title="Test Book",
            description="Test Description",
            author=self.user
            )
        self.book_serializer = BookSerializer(instance=self.book)
        self.book_data = self.book_serializer.data
        self.client.force_login(self.user)

    def test_create_book(self):
        data = {
            'title': 'New Test Book',
            'description': 'New Test Description',
            'author': self.user.id
            }
        url = reverse('books-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        test_book = Book.objects.get(id=response.data['id'])
        self.assertEqual(test_book.author.id, self.user.id)
    
    def test_get_books_list(self):
        url = reverse('books-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_book_by_id(self):
        book = Book.objects.first()
        url = reverse('books-detail', kwargs={'pk': book.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        book = Book.objects.first()
        url = reverse('books-detail', kwargs={'pk': book.pk})
        updated_data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "description": "Updated Test Description",
            "pub_date": "2022-02-02"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        book = Book.objects.first()
        url = reverse('books-detail', kwargs={'pk': book.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
