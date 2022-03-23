
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 

# Create your views here.


def register(request):
    return render(request, 'event/register.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()    
    user = User.objects.create_user(username, email, pwd)
    user.last_name = name
    user.first_name = firstname
    user.save()
    context = {'user':user}
    return render(request, 'event/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None :
        login(request, user)
        return render(request, 'event/welcome.html', context)
    else:
        return render(request, 'event/error_log.html')

def index(request):
    dernier_event = Events.objects.order_by('id')
    context = {'event_list': dernier_event}
    return render(request, 'event/index.html', context)

def liste(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'event/liste.html', {'event':event})
