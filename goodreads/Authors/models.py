from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_bio = models.CharField(max_length=1000)
    author_pp = models.ImageField(blank = 'true',upload_to='profile_image')

    def __str__(self):
        return self.author_name
