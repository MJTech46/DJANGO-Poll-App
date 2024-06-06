from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.hashers import make_password

# Create your views here.
@login_required(login_url="signin")
def manage_account(request):
    context={
        'request' : request,
        'User' : request.user,
    }
    return render(request, "Account/account.html", context=context)

@login_required(login_url="signin")
def sign_out(request: HttpRequest):
    auth_logout(request)
    return redirect("signin")

def sign_in(request: HttpRequest):
    if request.method == "GET":
        return render(request,"Account/signin.html")
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(username=username, password=password)
        print(username,password,user)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect("signin")
        

def sign_up(request: HttpRequest):
    if request.method == "GET":
        return render(request,"Account/signup.html")
    if request.method == "POST":
        username=request.POST.get("username")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        conform_password=request.POST.get("cfmpassword")
        if password == conform_password:
            CustomUser.objects.create(
                username=username,
                first_name=firstname,
                last_name=lastname,
                password=make_password(password)
            ).save()
            return redirect("signin")
        else:
            return render(request,"Account/signup.html")