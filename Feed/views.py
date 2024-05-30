from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #print(request.get_full_path())
    context={
        'request' : request,
        'User' : request.user,
    }
    return render(request,'Feed/pages/home.html', context=context)