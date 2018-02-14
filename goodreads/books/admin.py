from django.contrib import admin
from .models import Books
from .models import BookCategory

admin.site.register(Books)
admin.site.register(BookCategory)
