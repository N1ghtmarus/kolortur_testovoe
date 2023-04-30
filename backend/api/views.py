from rest_framework import viewsets

from .models import Book
from .pagination import CustomPagination
from .serializers import BookSerializer
from .permissions import  IsAdminAuthorOrReadOnlyPermission


class BooksViewSet(viewsets.ModelViewSet):
    """
    ViewSet для управления книгами.
    """
    queryset = Book.objects.select_related('author')
    serializer_class = BookSerializer
    permission_classes = [IsAdminAuthorOrReadOnlyPermission,]
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
