from django.urls import path, include
from rest_framework import routers

from .views import BooksViewSet
from users.views import AuthorViewSet


router = routers.DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register(r'books', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]