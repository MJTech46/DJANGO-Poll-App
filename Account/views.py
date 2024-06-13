from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from Poll.models import Poll

# Create your views here.
@login_required(login_url="signin")
def manage_account(request):
    posted_count=Poll.objects.filter(pub_user=request.user.pk).count()
    voted_count=Poll.objects.filter(options__polled_users=request.user.pk).distinct().count()
    context={
        'request' : request,
        'User' : request.user,
        'posted_count':posted_count,
        'voted_count':voted_count,
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
        #print(username,password,user)
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

@login_required(login_url="signin")        
def delete_account(request: HttpRequest):
    if request.method == "GET":
        context={
            'title': "Conform Deletion"
        }
        return render(request,"Account/signin.html", context=context)
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if authenticate(username=username, password=password):
            user=CustomUser.objects.get(pk=request.user.pk)
            auth_logout(request)
            user.delete()
            return redirect("signin")
        else:
            return redirect("delacc")


@login_required(login_url="signin")
def change_icon(request: HttpRequest):
    if request.method == "GET":
        return render(request, "Account/changeIcon.html",{"User":request.user})
    if request.method == "POST":
        user=CustomUser.objects.get(pk=request.user.pk)
        image_file=request.FILES.get("uploadedicon")
        if image_file:
            user.icon.delete()                
            user.icon.save(image_file.name, ContentFile(image_file.read()))
            user.save()
        return redirect("account")

def view_account(request, pk=None):
    view_user=CustomUser.objects.get(pk=pk)
    posted_count=Poll.objects.filter(pub_user=view_user.pk).count()
    voted_count=Poll.objects.filter(options__polled_users=view_user.pk).distinct().count()
    context={
        'request' : request,
        'User' : request.user,
        'posted_count':posted_count,
        'voted_count':voted_count,
        'view_user':view_user,
    }
    return render(request, "Account/view-account.html", context=context)
