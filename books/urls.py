from django.urls import path

from .views import BookCreateView
from .views import BookDetailView
from .views import BookListView
from .views import BookUpdateView

app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
]
