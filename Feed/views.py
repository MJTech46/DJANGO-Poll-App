from django.shortcuts import render, HttpResponse
from Poll.models import Poll

# Create your views here.
def home(request):
    polls = Poll.objects.order_by('-pub_date')[:6]
    context={
        'request' : request,
        'User' : request.user,
        'polls' : polls,
    }
    return render(request,'Feed/pages/home.html', context=context)