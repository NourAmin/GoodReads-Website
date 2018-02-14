from django.db import models
from Authors.models import Author
from Users.models import UserProfile


class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return  self.name

class Books(models.Model):
    book_title = models.CharField(max_length= 100)
    book_category = models.ManyToManyField(BookCategory)
    book_description = models.TextField()
    published_at = models.DateField()
    book_cover = models.FileField(null=True,blank=True)
    Author = models.ForeignKey('Authors.Authors',null=True,on_delete=models.CASCADE)


def __str__(self):
        return self.book_title
