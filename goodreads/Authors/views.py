from django.shortcuts import render
from django.http import HttpResponse
from Authors.models import *
from books.models import *
from Authors.models import *
from Users.models import *
 def index(request):
     return HttpResponse("Hello, world. You're at the authors page")
 # Create your views here.

def authors(request):
    authors = Authors.objects.all()
    # categories = BookCategory.objects.all()
    return render(request,'authors.html',
    {'authors':authors})

def authorDetails(request,id):
    request.session['Author_id'] = id
    author = Authors.objects.get(id=id)
    authorName= author.Author_Name
    bio = author.Author_Bio
    BoD = author.Author_DoB
    return render(request,"authorDetail.html",
    {"authorId":id ,"authorName":authorName,"bio":bio,
    'BoD':BoD});
