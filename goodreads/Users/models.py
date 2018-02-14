from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from Authors.models import Authors


class readList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Books',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)



# class RatedList(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     book=models.ForeignKey('books.Books',on_delete=models.CASCADE)
#     rate_val = models.IntegerField()

class wishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Books',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class followList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    author=models.ForeignKey('Authors.Authors',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

# class rateList(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     book=models.ForeignKey('books.Books',on_delete=models.CASCADE)
#     rate_val = models.IntegerField()

class rateList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey('books.Books',on_delete=models.CASCADE)
    Choices = (
        (1,  '*'),
        (2,  '**'),
        (3,  '***'),
        (4,  '****'),
        (5,  '*****'),
      )
    rate = models.IntegerField(default=1, choices=Choices)
