from django.contrib.auth.models import AbstractUser
from django.db import models


class Author(AbstractUser):
    """Модель автора"""
    birth_date = models.DateField(verbose_name='Дата рождения', null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'