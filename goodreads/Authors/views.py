#from django.http import Http404
from django.shortcuts import render ,get_object_or_404
#from django.template import loader
#from django.template import loader
from .models import Book
from .models import Author
from . import views

# Create your views here.
 
def index(request):
    #return HttpResponse("<h1> goodreads home </h1>")
    author_list =Author.objects.all()
    #template = loader_get_template('books/index.html')
    context = {'author_list': author_list}
    return render(request, 'authors/author_list.html', context)
    # return HttpResponse (template.render(context,request))
    # html =  ''
    # for book in all_books :
    #          url = '/books' + str(Book_id) + '/'
    #          html += '<a href="' + url + '> + Book.book_title + "</a><br>'
    # return HttpResponse(html)
    # return HttpResponse(template.render(context, request))
    

def detail(request, Author_id):
    try:
    #tit = Book.book_title
        author = Author.objects.get(pk=Author_id)
    except Author.DoesNotExist:
        raise Http404("book does not exist")    
    return render(request, 'authors/detail.html' , {'author' :auhtor})
    #return HttpResponse("this is details for book id:" + str(Book_id))
#"<h2>this is details for book title:</h2>" + str(book_title) +"<h2> it is category is </h2>" + str(book_category) +"<h2> it discuss </h2>" + str(book_description) +"</h2>")


# def detail(request, Author_id):
  
#     #tit = Book.book_title
#         author = get_object_or_404(Author,pk=Author_id)
#     #except Book.DoesNotExist:
#      #   raise Http404("book does not exist")    
#     return render(request, 'books/detail.html' , {'author': author})
#     #return HttpResponse("this is details for book id:" + str(Book_id))
# #"<h2>this is details for book title:</h2>" + str(book_title) +"<h2> it is category is </h2>" + str(book_category) +"<h2> it discuss </h2>" + str(book_description) +"</h2>")



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