from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    book_form = ReviewForm()
    reviews = book.review_set.all()
    context = {
        'book': book,
        'form' : book_form,
        'reviews' : reviews,
    }
    return render(request, 'libraries/detail.html', context)

def comments_create(request, book_pk):
    book = Book.objects.get(pk = book_pk)
    comment_form = ReviewForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.book = book
        comment.user = request.user
        comment.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'comment_form' : comment_form
    }
    return render(request, 'libraries/deatil.html', context)

def comments_delete(request, book_pk, comment_pk):
    comment = Review.objects.get(pk = comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('libraries:detail', book_pk)