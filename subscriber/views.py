from django.shortcuts import render_to_response
from subscriber.models import Subscriber
from subscriber.models import Issue
from subscriber.models import Order

# Create your views here.

def subscribers(request):
    return render_to_response('subscribers.html',
                             {'subscribers': Subscriber.objects.all()})

def subscriber(request, subscriber_id=1):
    return render_to_response('subscriber.html',
                             {'subscriber': Subscriber.objects.get(id=subscriber_id)})