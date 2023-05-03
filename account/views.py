from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:home')
                else:
                    return redirect('account:login')
            else:
                form = LoginForm()
                return render(request, 'acc/login.html', {'form': form,'mess': 'نام کاربری یا رمز عبور اشتباه است'})
    else:
        form = LoginForm()
    return render(request, 'acc/login.html', {'form': form})
@login_required
def profile(request):
    user = request.user

    return render(request, 'acc/profile.html', {'user': user})
@login_required
def logoutuser (request):
    if request.method == 'GET':
            logout(request)
            return redirect('account:login')
