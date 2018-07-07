from django.http import HttpResponse
from django.shortcuts import render


def room(request):
    return render(request, 'blinkstick/room.html')


def grafana(request):
    print('*'*90)
    print(request.POST)
    print('*'*90)
    return HttpResponse(status=204)
