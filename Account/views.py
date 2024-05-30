from django.shortcuts import render

# Create your views here.
def manage_account(request):
    #print(request.get_full_path())
    context={
        'request' : request,
        'User' : request.user,
    }
    return render(request, "Account/account.html", context=context)