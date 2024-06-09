from django.shortcuts import render, HttpResponse
from Poll.models import Poll, Option
from django.contrib.auth.decorators import login_required
from random import sample

# Create your views here.
@login_required(login_url="signin")
def home(request):
    distinct_polls = list(Poll.objects.exclude(options__polled_users=request.user.pk).distinct())
    # you can change this as per your need
    no_of_Polls_per_refresh = 6
    # for removing ValueError("Sample larger than population or is negative")
    if len(distinct_polls) < no_of_Polls_per_refresh:
        polls=distinct_polls
    else:
        # for Choosing k unique random elements from distinct_polls
        polls=sample(distinct_polls, no_of_Polls_per_refresh) 
    context={
        'request' : request,
        'User' : request.user,
        'polls' : polls,
    }
    return render(request,'Feed/home.html', context=context)

