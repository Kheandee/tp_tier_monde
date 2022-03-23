from django.http import HttpResponse
from django.shortcuts import render
from .models import Events

# Create your views here.
def index(request):
    dernier_event = Events.objects.order_by('id')
    context = {'event_list': dernier_event}
    return render(request, 'event/index.html', context)
