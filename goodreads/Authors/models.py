from django.db import models
# Create your models here.
# class Author (models.Model):
#     author_name = models.CharField(max_length = 100)
#     author_bio = models.CharField(max_length = 1000)
#     author_photo = models.CharField(max_length = 1000)

#     def __str__ (self):
       # return self.author_name + '-' + self.author_bio 
class Author (models.Model):
    author_name = models.CharField(max_length = 50)
    author_bio = models.CharField(max_length = 1000)
    author_pp = models.CharField(max_length = 1000)

    def __str__(self):
        return self.author_name 

class Book (models.Model):
    book_title = models.CharField(max_length = 50)
    book_category = models.CharField(max_length = 50)
    book_description = models.CharField(max_length =1000)
    book_cover = models.CharField(max_length=1000)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.book_title

    
