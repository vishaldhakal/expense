from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from home.views import index

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        check_point = 0
        try:
            users = User.objects.get(email=username)
            check_point = 1
        except:
            pass
        if check_point == 1:
            user = auth.authenticate(username=users.username,password=password)
        else:
            user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            ctx={
                'error':"Username or Password doesnot match"
            }
            return render(request, 'accounts/login.html',ctx)
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == "POST":
        #get form values
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        #Checking
        if password == password2:
            #check username
            if User.objects.filter(username = username).exists():
               return render(request, 'accounts/register.html',{'error':"Username already exists !"}) 
            else :
                if User.objects.filter(email = email).exists():
                    return render(request, 'accounts/register.html',{'error':"Email already exists !"}) 
                else :
                    user = User.objects.create_user(username = username,password=password,email=email)
                    user.save()
                    return render(request, 'accounts/login.html',{'error':"Account Sucessfully created Please Login Now!"})  

        else:
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def index(request):
    return render(request, 'base.html')