from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Book

# Create your views here.


def index(request):
    all_books_queryset = Book.objects.all()
    # all_books_list = list(all_books_queryset)
    return render(request,
                  template_name='book_outlet/index.html',
                  context={'books': all_books_queryset}
                  )


def book_detail(request, slug):
    identified_book = get_object_or_404(Book, slug=slug)
    return render(request,
                  template_name='book_outlet/book-detail.html',
                  context={'book': identified_book}
                  )


def book_detail_id(request, id):
    identified_book = get_object_or_404(Book, pk=id)
    slug_title = identified_book.slug
    redirect_path = reverse('book-detail', args=[slug_title])
    return HttpResponseRedirect(redirect_to=redirect_path)
