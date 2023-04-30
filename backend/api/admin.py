from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pub_date']
    list_filter = ['author', 'pub_date']
    exclude = ('soundex',)
