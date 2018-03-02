from django.db import models

# Create your models here.
class Authors(models.Model):
    Author_Name = models.CharField(max_length= 100)
    Author_DoB=models.DateField(null=True, blank=True)
    Author_Bio= models.CharField(max_length=200)
    # image = models.FileField(null=True,blank=True)

    def __str__(self):
        return self.Author_Name
