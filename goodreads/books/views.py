from django.http import Http404
from django.shortcuts import render
from .models import Book
from .models import Author
from django.http import HttpResponse


# Create your views here.

def index(request):
    # book_list =Book.objects.all()
    # context = {'book_list': book_list}
    # return render(request, 'books/book_list.html', context)
   return HttpResponse("Hello, world. You're at the book index.")
def detail(request, Book_id):
    try:
    #tit = Book.book_title
        book = Book.objects.get(pk=Book_id)
    except Book.DoesNotExist:
        raise Http404("book does not exist")
    return render(request, 'books/detail.html' , {'book' :book})
