from django.contrib.auth import get_user_model
from djoser.views import UserViewSet

from .serializers import AuthorCreateSerializer


User = get_user_model()


class AuthorViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = AuthorCreateSerializer