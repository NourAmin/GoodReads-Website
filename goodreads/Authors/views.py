from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404
from .models import *


def index(request):
    return HttpResponse("Hello, world. You're at the authors page")
# Create your views here.

def detail(request, Author_id):
    try:

         author= Author.objects.get(pk=Author_id)
    except Author.DoesNotExist:
        raise Http404("book does not exist")
    return render(request, 'authors/detail.html' , {'author' :author})

