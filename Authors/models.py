from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_bio = models.CharField(max_length=1000)
    author_pp = models.CharField(max_length=1000)

    def __str__(self):
        return self.author_name
    
