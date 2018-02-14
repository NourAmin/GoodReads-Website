from django.contrib import admin
from .models import Book
from .models import Author
from .models import UserProfile
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(UserProfile)