from django.contrib import admin
from books.models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ['name', 'author']

admin.site.register(Books, BooksAdmin)
