from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm
from django.db.models import Count

# Create your views here.
def index(request):
    authors = Author.objects.annotate(book_count=Count('book'))
    context = {
        'authors': authors,
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    book_form = BookForm()
    books = author.book_set.all()
    context = {
        'author': author,
        'book_form' : book_form,
        'books' : books,
    }
    return render(request, 'libraries/detail.html', context)

def books_create(request, author_pk):
    author = Author.objects.get(pk = author_pk)
    book_form = BookForm(request.POST)
    if book_form.is_valid():
        book = book_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author.pk)
    context = {
        'book_form' : book_form,
    }
    return render(request, 'libraries/detail.html', context)