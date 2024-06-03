from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def manage_account(request):
    #print(request.get_full_path())
    context={
        'request' : request,
        'User' : request.user,
    }
    return render(request, "Account/account.html", context=context)

def sign_out(request: HttpRequest):
    auth_logout(request)
    return redirect("home")