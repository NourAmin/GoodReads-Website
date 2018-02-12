#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from .models import Book
from .models import Author

# Create your views here.
 
def index(request):
    return HttpResponse("<h1> goodreads home </h1>")
    all_books =Book.objects.all()
    #template = loader_get_template('books/index.html')
    #context ={'all_books': all_books}
    #return HttpResponse (template.render(context,request))
    # html =  ''
    # for book in all_books :
    #         url = '/books' + str(Book_id) + '/'
    #         #html += "<a href=" + url + "">"" + Book.book_title + "</a>"
    # return HttpResponse(url)

def detail(request, Book_id):
    #tit = Book.book_title
    return HttpResponse("this is details for book id:" + str(Book_id))  `
#"<h2>this is details for book title:</h2>" + str(book_title) +"<h2> it is category is </h2>" + str(book_category) +"<h2> it discuss </h2>" + str(book_description) +"</h2>")