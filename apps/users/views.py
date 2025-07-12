from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def profile(request):
    return render(request, 'users/profile.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')

def password_reset(request):
    return render(request, 'users/password_reset.html')

def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'users/password_reset_confirm.html')

@login_required
def user_detail(request, pk):
    return render(request, 'users/user_detail.html')

def user_list(request):
    return render(request, 'users/user_list.html')
