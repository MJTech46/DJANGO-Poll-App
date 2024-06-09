from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Option, Poll
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="signin")
def createPoll(request: HttpRequest):
    if request.method == "GET":
        #print(request.get_full_path())
        context={
            'request' : request,
            'User' : request.user,
        }
        return render(request, "Poll/createPoll.html", context=context)
    
    if request.method == "POST":
        #print(request.POST)
        User = request.user
        pollText = request.POST.get("pollText")
        optionsCount = int(request.POST.get("optionsCount"))
        #saving data to poll model
        poll = Poll(
            poll_text = pollText,
            pub_user = User
        )
        poll.save()
        #saving data to options model
        for i in range(0, optionsCount):
            option = Option(
                poll = poll,
                option_text = request.POST.get(f"answerOptions{i+1}")
            )
            option.save()
        return redirect('createPoll')

def results(request: HttpRequest, uuid=None):
    poll=Poll.objects.get(uuid=uuid)
    options=poll.options.all()
    total_vote=0
    percentages=[]
    #for finding total vote
    for option in options:
        total_vote+=option.polled_users.count()
    #for finding each percentage for each option
    for option in options:
        try:
            result=(option.polled_users.count()/total_vote)*100
        except ZeroDivisionError:
            result=0
        percentages.append(result)
    context={
            'request' : request,
            'User' : request.user,
            'polls': [poll],
            'options': zip(options,percentages)
        }
    return render(request, "Poll/pollResult.html", context=context)

def vewPoll(request: HttpRequest, uuid=None):
    return HttpResponse(f"Poll of '{uuid}'")  

@login_required(login_url="signin")
def pollPost(request: HttpRequest):
    if request.method == "POST":
        #getting data from POST
        poll_uuid = request.POST.get("uuid")
        option_uuid = request.POST.get("RadioBtn")
        print(f"Poll uuid:{poll_uuid}\nOption uuid:{option_uuid}")
        #making obj
        POST_poll=Poll.objects.get(uuid=poll_uuid)
        POST_option=Option.objects.get(uuid=option_uuid)
        #checking if user previouly voted on this Poll before
        has_voted=Option.objects.filter(poll=POST_poll, polled_users=request.user.pk)
        print(has_voted)
        if has_voted:
            #removing the old vote and repalcing with new vote
            option=has_voted[0]
            option.polled_users.remove(request.user.pk)
        #else adding the user to the option
        POST_option.polled_users.add(request.user)
        return JsonResponse({'status':200})

@login_required(login_url="signin")
def postedPolls(request):
    posted_polls=Poll.objects.filter(pub_user=request.user.pk)
    context={
        'request' : request,
        'User' : request.user,
        'polls' : posted_polls,
    }
    return render(request, "Poll/postedPolls.html", context=context)

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

@login_required(login_url="signin")
def delPoll(request: HttpRequest):
    if request.method == "POST":
        poll=Poll.objects.get(uuid=request.POST.get("uuid"))
        if poll.pub_user.pk == request.user.pk:
            poll.delete()
    return redirect("postedPolls")
