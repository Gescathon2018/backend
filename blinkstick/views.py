from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string

from blinkstick.models import Client, Event, EventClient


def room(request):
    return render(request, 'blinkstick/room.html')


@csrf_exempt
def grafana(request):
    print('*'*90)
    print(request.body)
    print('*'*90)
    return HttpResponse(status=204)


def reg_client(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        token = get_random_string(length=60)

        client = Client(email=email, token=token)
        client.save()

        response = {'token': token}

        return response

    pass


def subs_event(request):

    if request.method == 'POST':

        token = request.POST.get('token')
        event = request.POST.get('event')

        try:

            client = Client.objects.get(token=token)
            event = Event.objects.get(name=event)

            eventclient = EventClient(event=event, client=client)

            eventclient.save()

        except Exception as e:

            raise PermissionDenied


def unsubs_event(request):

    if request.method == 'POST':

        token = request.POST.get('token')
        event = request.POST.get('event')

        try:

            client = Client.objects.get(token=token)
            event = Event.objects.get(name=event)

            eventclient = EventClient(event=event, client=client)

            eventclient.delete()

        except Exception as e:

            raise PermissionDenied







