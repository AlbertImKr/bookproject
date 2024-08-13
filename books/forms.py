from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book
from .models import Rental


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book', 'return_date']
        widgets = {
            'return_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}),
        }
