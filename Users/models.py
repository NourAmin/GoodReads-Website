from django.db import models
from django.contrib.auth.models import User
from Authors.models import Author
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_pp = models.ImageField(blank = 'true',upload_to='profile_image')

    read = models.ManyToManyField('books.Book', related_name='user_book_read')
    wishlist = models.ManyToManyField('books.Book', related_name='user_book_wishlist')
    user_book_rate = models.ManyToManyField('books.Book', through='BookRate')
    user_category_fav = models.ManyToManyField('books.Category')
    user_author_follow = models.ManyToManyField(Author)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

class BookRate(models.Model):
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE)  # when deleting the user you have to delete his rate to get rid of fake accounts rating
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return self.rate

