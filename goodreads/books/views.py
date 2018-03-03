from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from books.models import *
from Authors.models import *
from Users.models import *

from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

def index(request):
    books = Books.objects.all()
    categories = BookCategory.objects.all()
    return render(request,'index.html',
    {'books':books,'categories':categories})


def authors(request):
    authors = authors.objects.all()
    return render(request,'authors.html',
    {'authors':authors})

def details(request,id):
    request.session['book_id'] = id
    book = Books.objects.get(id=id)
    summary = book.book_description
    return render(request,"detail.html",
    {"book":book,"summary":summary,
    'categories':categories});


def userWishList(request, id):
    attempToDuplicate= wishList.objects.filter(user=request.user, book_id = request.session.get('book_id'))
    if len(attempToDuplicate)==0:
        wishList.objects.create(user= request.user, book_id = request.session.get('book_id'))
        return redirect('/books', )
    else:
        return redirect('/books', )

def userReadList(request, id):
    attempToDuplicate= readList.objects.filter(user=request.user, book_id = request.session.get('book_id'))
    if len(attempToDuplicate)==0:
        readList.objects.create(user= request.user, book_id = request.session.get('book_id'))
        return redirect('/books', )
    else:
        return redirect('/books')


def categories(request,category_id):
    category = categoryList(user_id= request.user.id,category_id=category_id)
    category.save()
    return JsonResponse(1,safe=False)

def search(request):
    text_search = request.GET.get("in")
    book_list = Books.objects.filter(book_title__icontains= text_search)
    author=Authors.objects.filter(Author_Name__icontains=text_search)
    return render(request,'search.html',
    {'book_list':book_list ,'author':author})

#
# def rate_book(request,rate_value,book_id):
#     rate = RatedList(user_id= request.user.id,book_id = book_id,rate_val = rate_value )
#     rate.save()
#     return JsonResponse(1,safe=False)

# Template AJAX
def userRateList(request):
    stars = request.GET.get('stars', None)
    bookID = request.GET.get('bookID', None)
    print("%_%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    rateList.objects.create(user= request.user, book_id = bookID, rate=stars)
    print("no stars"+stars)
    print("bookid"+bookID)
    data = {
        'rateStatus': int(1)
    }
    return JsonResponse(data)
