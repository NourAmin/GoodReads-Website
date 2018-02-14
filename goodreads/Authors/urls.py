from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

 urlpatterns = [
    # re_path (r'^$', views.index, name ='index'),
    path('',login_required(views.authors,"authors","register"),name="authors"),
    re_path(r'(?P<id>[0-9]+)/$', views.authorDetails, name = "authorDetails"),

 ]
