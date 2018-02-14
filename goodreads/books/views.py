from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from books.models import *
from Authors.models import *
from Users.models import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


from .forms import CommentForm


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
    categories = book.book_category.all()[0]
    return render(request,"detail.html",
    {"book":book, "categories":categories});


# def userWishList(request, id):
#     attempToDuplicate= wishList.objects.filter(user=request.user, book_id = request.session.get('book_id'))
#     if len(attempToDuplicate)==0:
#         print("+++++++++++++dup")
#         wishList.objects.create(user= request.user, book_id = request.session.get('book_id'))
#         return redirect('/books', )
#     else:
#         print("+++++++++++++dupelse")
#         return redirect('/books', )

#after AJAX
def userWishList(request, id):
    attempToDuplicate= wishList.objects.filter(user=request.user, book_id = request.session.get('book_id'))
    if len(attempToDuplicate)==0:
        print("+++++++++++++dup")
        wishList.objects.create(user= request.user, book_id = request.session.get('book_id'))
        data = {
            'rateStatus': int(1),
        }
        return JsonResponse(data)
    else:
        print("+++++++++++++dupelse")
        data = {
            'rateStatus': int(0),
        }
        return JsonResponse(data)


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

# AJAX
def userRateList(request):
    stars = request.GET.get('stars')
    bookID = request.GET.get('bookID')
    bookTitle= Books.objects.get(id=bookID).book_title
    print(bookTitle)
    checkExistedRatings= rateList.objects.filter(user= request.user, book_id = bookID)
    if len(checkExistedRatings)==0:
        rateList.objects.create(user= request.user, book_id = bookID, rate=stars)
        data = {
            'rateStatus': int(1),
            'bookTitle':bookTitle
        }
        return JsonResponse(data)
    else:
        rateList.objects.filter(user= request.user, book_id = bookID).update(rate=stars)
        data = {
            'rateStatus': int(0),
            'bookTitle':bookTitle
        }
        return JsonResponse(data)


def add_comment_to_post(request, id):
    post = get_object_or_404(Books, pk=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('details', id=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})
