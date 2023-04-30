from django.db import models

from users.models import Author


class Book(models.Model):
    title = models.CharField(verbose_name='Название книги', max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Автор книги'
        )
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateField(
        verbose_name='Дата публикации',
        auto_now_add=True
        )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title[:79]
