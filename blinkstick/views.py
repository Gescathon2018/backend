from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def room(request):
    return render(request, 'blinkstick/room.html')


@csrf_exempt
def grafana(request):
    print('*'*90)
    print(request.body)
    print('*'*90)
    return HttpResponse(status=204)
