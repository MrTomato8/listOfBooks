from django import forms
from books.models import Books


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
