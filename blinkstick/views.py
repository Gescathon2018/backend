import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'blinkstick/index.html', {})


def room(request):
    return render(request, 'blinkstick/room.html')