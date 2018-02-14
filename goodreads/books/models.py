from django.db import models
from Authors.models import Author
from Users.models import UserProfile





class Book(models.Model):
    book_title = models.CharField(max_length=50)
    book_category = models.CharField(max_length=50)
    book_description = models.CharField(max_length=1000)
    book_cover = models.CharField(max_length=1000)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_title


class Category(models.Model):
    cat_genre = models.CharField(max_length=20)

    def __str__(self):
        return self.cat_genre



class Rate(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)  # when deleting the user you have to delete his rate to get rid of fake accounts rating
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return self.rate
