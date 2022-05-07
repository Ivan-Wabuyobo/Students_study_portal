from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def signup_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not User.objects.filter(username=username).exists():

                user = User(username=username, email=email, password=password2)

                user.save()
                return redirect('home')
            else:
                messages.info(request, "username already exists!!!")
                return render(request, "users/signup.html")
        else:
            messages.info(request, "The passwords didn't match!!!")
            return render(request, "users/signup.html")
            
    else:
        return render(request, "users/signup.html")


def login_user(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
