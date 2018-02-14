from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    re_path (r'^$', views.index, name ='index'),
    # re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login/$', login, {'template_name':'books/login.html'}),
    url(r'^logout/$', logout, {'template_name':'books/logout.html'}),

    re_path('^(?P<Book_id>[0-9]+)/$', views.detail, name = 'detail'),
    path('register/', views.register, name="register"),
    path('profile/',views.view_profile, name = "view_profile"),
    path('profile/edit',views.edit_profile, name = "edit_profile")
    #url(r'^$',views.index) 
]



