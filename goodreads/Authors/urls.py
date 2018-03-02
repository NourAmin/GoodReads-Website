from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.urls import path,re_path
from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # re_path (r'^$', views.index, name ='index'),
    path('',login_required(views.authors,"authors","register"),name="authors"),
    re_path(r'(?P<id>[0-9]+)/$', views.authorDetails, name = "authorDetails"),
    # re_path(r'(?P<id>[0-9]+)/$', views.details, name = "details"), //book details
    re_path(r'(?P<id>[0-9]+)/followList/$', views.userFollowList, name='followList'),
    # re_path(r'(?P<id>[0-9]+)/wishList/$', views.userWishList, name='wishList'),//user follow list

]
