from django.db import models
from Authors.models import Author
from Users.models import UserProfile



class Category(models.Model):
    cat_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_genre

class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    book_description = models.CharField(max_length=1000)
    book_cover = models.CharField(max_length=1000)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return self.book_title



    
