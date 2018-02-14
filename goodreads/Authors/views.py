from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
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
    {"author":author ,"authorName":authorName,"bio":bio,
    'BoD':BoD});

def userFollowList(request, id):
    aid = request.session.get('Author_id')
    print(aid)
    print ("+++++++++++++++++++++++++++++++++")
    attempToDuplicate= followList.objects.filter(user=request.user, author_id = request.session.get('Author_id'))
    print (attempToDuplicate)
    if len(attempToDuplicate)==0:
        followList.objects.create(user= request.user, author_id = request.session.get('Author_id'))
        return redirect('/authors', )
    else:
        return redirect('/authors', )
