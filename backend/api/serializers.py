from rest_framework import serializers

from .models import Book
from users.models import Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'description',
            'pub_date'
        ]
