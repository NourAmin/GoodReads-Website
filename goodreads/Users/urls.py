from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('login/', login, {'template_name':'users/login.html'}),
    path('logout/', logout, {'template_name':'users/logout.html'}),
    # path('login/', views.login,name="loginpage"),
    # path('logout/', logout, {'template_name':'users/logout.html'}),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name = "view_profile"),
    path('profile/edit',views.edit_profile, name = "edit_profile")
]
