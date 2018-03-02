from django.db import models

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



















#
#
# from django.db import models
#
#
# # Create your models here.
# # class Author (models.Model):
# #     author_name = models.CharField(max_length = 100)
# #     author_bio = models.CharField(max_length = 1000)
# #     author_photo = models.CharField(max_length = 1000)
#
# #     def __str__ (self):
# #         return self.author_name + '-' + self.author_bio
# class Author(models.Model):
#     author_name = models.CharField(max_length=50)
#     author_bio = models.CharField(max_length=1000)
#     author_pp = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return self.author_name
#
#
# class Book(models.Model):
#     book_title = models.CharField(max_length=50)
#     book_category = models.CharField(max_length=50)
#     book_description = models.CharField(max_length=1000)
#     book_cover = models.CharField(max_length=1000)
#     Author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.book_title
#
#
# class Category(models.Model):
#     cat_genre = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.cat_genre
#
#
# class User(models.Model):
#     user_name = models.CharField(max_length=15)
#     user_password = models.CharField(max_length=20)
#     user_email = models.CharField(max_length=50)
#     user_pp = models.CharField(max_length=1000)
#
#     read = models.ManyToManyField(Book, related_name='user_book_read')
#     wishlist = models.ManyToManyField(Book, related_name='user_book_wishlist')
#     user_book_rate = models.ManyToManyField(Book, through='Rate')
#     user_category_fav = models.ManyToManyField(Category)
#     user_author_follow = models.ManyToManyField(Author)
#
#     def __str__(self):
#         return self.user_name + '-' + self.user_email
#
#
# class Rate(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE)  # when deleting the user you have to delete his rate to get rid of fake accounts rating
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     rate = models.IntegerField()
#
#     def __str__(self):
#         return self.rate
