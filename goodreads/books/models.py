from django.db import models
from django.utils import timezone

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



class Comment(models.Model):
    post = models.ForeignKey('books.Books', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200, default="Visitor")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
