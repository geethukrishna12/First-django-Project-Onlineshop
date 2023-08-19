from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User name already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password1)
                user.save();
                # print("successfully registered")
                messages.info(request,'successfully regstred')
                return redirect('login')
        else:
            messages.info(request,'Password is not match')
            # print("password is not match")
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            mydata=User.objects.all()
            return redirect('/')
        else:
            # messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')