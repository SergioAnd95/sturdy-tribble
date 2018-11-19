from django.views.generic import ListView, CreateView, UpdateView

from core.mixins import AdminRequiredMixin

from .models import Book

# Create your views here.


class BooksListView(ListView):
    """
    View for display list books
    """
    queryset = Book.objects.all()
    paginate_by = 10
    context_object_name = 'books'
    template_name = 'books/books_list.html'


class BookCreateEditBaseView(AdminRequiredMixin):
    """
    Base view for create and update books
    """
    fields = '__all__'
    model = Book
    success_url = '/'
    template_name = 'books/books_form.html'


class BookCreateView(BookCreateEditBaseView, CreateView):
    pass


class BookEditView(BookCreateEditBaseView, UpdateView):
    pass
