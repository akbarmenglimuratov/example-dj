from csv import list_dialects
from django.contrib import admin
from .models import Book, Genre

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['name', 'genre', 'author']

class GenreAdmin(admin.ModelAdmin):
    model = Genre
    list_display = ['name']

admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)