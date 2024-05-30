from django.shortcuts import render

# Create your views here.
def createPoll(request):
    #print(request.get_full_path())
    context={
        'request' : request,
        'User' : request.user,
    }
    return render(request, "Poll/pages/createPoll.html", context=context)