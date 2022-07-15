from django.shortcuts import render, redirect

from django.db import IntegrityError

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'account/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"],
                                                password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('fridge:home')
            except IntegrityError:
                return render(request, 'account/signupuser.html',
                              {'form':UserCreationForm(),
                               'error':"That username has alreadty been taken. \
                                        Please use another one."})
        else:
            return render(request, 'account/signupuser.html',
                          {'form':UserCreationForm(),
                           'error':"Passwords didn't match"})
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'account/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,
                            username=request.POST["username"],
                            password=request.POST["password"])
        if user is None:
            return render(request, 'account/loginuser.html',
                          {'form': AuthenticationForm(),
                           'error':'Username and password did not match'})
        login(request, user)
        return redirect('fridge:home')

def home(request):
    return render(request, 'account/home.html')