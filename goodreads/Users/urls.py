from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('login/', login, {'template_name':'users/login.html'}),
    path('logout/', logout, {'next_page': '../../users/login'}),
    path('register/', views.register, name="register"),
    path('account/',views.view_profile, name = "view_profile"),
    path('account/edit',views.edit_profile, name = "edit_profile")


]
