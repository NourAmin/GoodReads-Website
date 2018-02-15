#from django.http import Http404
from django.shortcuts import render ,get_object_or_404
#from django.template import loader
from .models import Book
from .models import Author

import re
from django.db.models import Q
# Create your views here.
 
def index(request):
    #return HttpResponse("<h1> goodreads home </h1>")
    book_list =Book.objects.all()
    #template = loader_get_template('books/index.html')
    context = {'book_list': book_list}
    return render(request, 'books/book_list.html', context)

    

def detail(request, Book_id):
    try:
    #tit = Book.book_title
        book = Book.objects.get(pk=Book_id)
    except Book.DoesNotExist:
        raise Http404("book does not exist")    
    return render(request, 'books/detail.html' , {'book' :book})


def search(request):
    #create SearchForm Class
    text_search = request.GET.get("in")
    book_list = Book.objects.filter(book_title__icontains= text_search)
    author=Author.objects.filter(author_name__icontains=text_search)

    return render(request,'books/search.html',
    {'book_list':book_list ,'author':author})

# return books of specific author
def get_author_books(request,id):
    return HttpResponse(Book.objects.filter(author=id))




# def favorite(request, Book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     try:
#         selected_book = Author.book_set.get(pk=request.POST['book'])
#     except (eyEror, Book.DoesNotExist):
#         return render(request , 'books/detail.html' ,{
#             'book': book,
#             'error_message': "you did not select a valid song"
#         })
#     else:
#         selected_book.is_favorite = true
#         selected_book.save()
#         return(request,'books/detail.html',{'book':book})    
