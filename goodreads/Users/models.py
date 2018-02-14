from django.db import models
from django.contrib.auth.models import User
from Authors.models import Author


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_pp = models.ImageField(blank = 'true',upload_to='profile_image')

    read = models.ManyToManyField('books.Book', related_name='user_book_read')
    wishlist = models.ManyToManyField('books.Book', related_name='user_book_wishlist')
    #user_book_rate = models.ManyToManyField('books.Book', through='Rate')
    user_category_fav = models.ManyToManyField('books.Category')
    user_author_follow = models.ManyToManyField(Author)

    def __str__(self):
        return self.user_name + '-' + self.user_email

