from django.shortcuts import render, HttpResponse
from Poll.models import Poll, Option
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="signin")
def home(request):
    polls = Poll.objects.exclude(options__polled_users=request.user.pk).distinct()
    context={
        'request' : request,
        'User' : request.user,
        'polls' : polls,
    }
    return render(request,'Feed/home.html', context=context)

@login_required(login_url="signin")
def postedPolls(request):
    posted_polls=Poll.objects.filter(pub_user=request.user.pk)
    context={
        'request' : request,
        'User' : request.user,
        'polls' : posted_polls,
    }
    return render(request,'Feed/home.html', context=context)

@login_required(login_url="signin")
def votedPolls(request):
    voted_options=Option.objects.filter(polled_users=request.user.pk)
    voted_polls=Poll.objects.filter(options__in=voted_options)
    context={
        'request' : request,
        'User' : request.user,
        'polls' : voted_polls,
        'voted_options' : voted_options,
    }
    return render(request,'Feed/home.html', context=context)