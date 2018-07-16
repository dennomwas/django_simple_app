from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Book, BookInstance, Author, Genre


def index(request):
    """
    View function for home page of site.
    """
    all_books = Book.objects.all()
    book_count = all_books.count()
    num_of_visits = request.session.get('num_of_visits', 0)
    request.session['num_of_visits'] = num_of_visits+1

    return render(
        request, 'index.html',
        context={
            'all_books': all_books,
            'book_count': book_count,
            'num_of_visits': num_of_visits
        })


class BookListView(ListView):
    model = Book
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(DetailView):
    model = Author

# def book_detail_view(request, pk):
#     book_id = get_object_or_404(Book, pk=pk)

#     return render(request, 'catalog/book_detail.html',
#                   context={'book_id': book_id})
