from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#from django.contrib.auth.models import User,Book, Author
from django.shortcuts import render,redirect
from Users.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from Users.models import *
from books.models import *

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'users/reg_form.html', args)
@login_required
def view_profile(request):
    userName = {'user':request.user}
    UserRateList=rate.objects.filter(user=request.user)
    UserReadList=readList.objects.filter(user=request.user)
    UserWishList=wishList.objects.filter(user=request.user)
    UserFollowList=followList.objects.filter(user=request.user)
    print (UserRateList)
    return render(request, 'users/profile.html', {'UserRateList':UserRateList, 'UserReadList':UserReadList, 'UserWishList':UserWishList, 'UserFollowList':UserFollowList})
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance= request.user)

        if form.is_valid():
            form.save()
            return redirect("/users/profile")
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'users/edit_profile.html', args)
