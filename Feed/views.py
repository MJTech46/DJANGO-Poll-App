from django.shortcuts import render, HttpResponse
from Poll.models import Poll
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="signin")
def home(request):
    polls = Poll.objects.order_by('-pub_date')[:6]
    context={
        'request' : request,
        'User' : request.user,
        'polls' : polls,
    }
    return render(request,'Feed/home.html', context=context)