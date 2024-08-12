from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    ordering = ['-publication_date']


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
