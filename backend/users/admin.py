from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name']
    list_filter = ['first_name', 'last_name']