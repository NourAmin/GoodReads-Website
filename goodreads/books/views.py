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

def detail(request, Book_id):
    #tit = Book.book_title
    return HttpResponse("this is details for book id:" + str(Book_id))
#"<h2>this is details for book title:</h2>" + str(book_title) +"<h2> it is category is </h2>" + str(book_category) +"<h2> it discuss </h2>" + str(book_description) +"</h2>")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'books/reg_form.html', args)

def view_profile(request):
    args = {'user':request.user}
    return render(request, 'books/profile.html', args)


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance= request.user)

        if form.is_valid():
            form.save()
            return redirect("/books/profile")
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'books/edit_profile.html', args)