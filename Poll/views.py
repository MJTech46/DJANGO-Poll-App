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
    return HttpResponse(f"Results of '{uuid}'")

def vewPoll(request: HttpRequest, uuid=None):
    return HttpResponse(f"Poll of '{uuid}'")  

@login_required(login_url="signin")
def pollPost(request: HttpRequest):
    if request.method == "POST":
        poll_uuid = request.POST.get("uuid")
        option_uuid = request.POST.get("RadioBtn")
        print(f"Poll uuid:{poll_uuid}\nOption uuid:{option_uuid}")
        return JsonResponse({'status':200})