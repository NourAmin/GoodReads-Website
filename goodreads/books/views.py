#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from .models import Book
from .models import Author
from django.shortcuts import render,redirect
from books.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
 
def index(request):
    return HttpResponse("<h1> goodreads home </h1>")
    all_books =Book.objects.all()
    #template = loader_get_template('books/user.html')
    #context ={'all_books': all_books}
    #return HttpResponse (template.render(context,request))
    # html =  ''
    # for book in all_books :
    #         url = '/books' + str(Book_id) + '/'
    #         #html += "<a href=" + url + "">"" + Book.book_title + "</a>"
    # return HttpResponse(url)
