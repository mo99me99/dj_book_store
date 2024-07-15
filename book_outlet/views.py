from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Avg
from .models import Book

# Create your views here.


def index(request):
    all_books_queryset = Book.objects.all().order_by('title')
    num_books = all_books_queryset.count()
    avg_rating = all_books_queryset.aggregate(Avg('rating')).get('rating__avg')
    # all_books_list = list(all_books_queryset)
    return render(request,
                  template_name='book_outlet/index.html',
                  context={'books': all_books_queryset,
                           'num_books': num_books,
                           'avg_rating': avg_rating}
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
