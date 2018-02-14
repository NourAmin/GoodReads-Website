from django.urls import include, path, re_path
from django.contrib import admin
from goodreads import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('users/', include('Users.urls')),
    path('authors/',include('Authors.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
