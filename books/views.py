from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import BookForm
from .forms import CustomUserCreationForm
from .models import Book
from .mixins import GroupRequiredMixin


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    ordering = ['-publication_date']

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            queryset = Book.objects.filter(title__icontains=query)

        sort = self.request.GET.get('sort')
        if sort == 'title':
            queryset = queryset.order_by('title')
        elif sort == 'author':
            queryset = queryset.order_by('author')
        elif sort == 'date':
            queryset = queryset.order_by('publication_date')

        genre = self.request.GET.get('genre')
        year = self.request.GET.get('year')
        if genre:
            queryset = queryset.filter(genre=genre)  # 장르로 필터링
        if year:
            queryset = queryset.filter(
                    publication_date__year=year)  # 출판 연도로 필터링

        return queryset


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    success_url = reverse_lazy('books:book_list')


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book_list')


class BookUpdateView(GroupRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'

    def get_success_url(self):
        return reverse_lazy('books:book_detail', kwargs={'pk': self.object.pk})


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book_list')
    permission_required = 'books.delete_book'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
