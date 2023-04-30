from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer


User = get_user_model()


class AuthorCreateSerializer(UserCreateSerializer):
    """Сериализатор для создания автора"""
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
            ) + tuple(User.REQUIRED_FIELDS) + (
            'birth_date',
            'username',
            'password',
        )
