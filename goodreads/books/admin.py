from django.contrib import admin
from .models import Books
from .models import BookCategory
from .models import Comment

# Register your models here.
admin.site.register(Books)
admin.site.register(BookCategory)
admin.site.register(Comment)
