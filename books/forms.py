from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'summary', 'publication_date',
                  'image']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': '제목',
            'author': '저자',
            'genre': '장르',
            'summary': '요약',
            'publication_date': '출판일',
        }
