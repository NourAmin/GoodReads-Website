

from django.urls import include, path, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from django.conf import settings
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    # path('', views.index, name ='index'),
    path('', login, {'template_name':'./users/login.html'}),
    path('user/', include('Users.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/',include('Authors.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
