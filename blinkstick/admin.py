from django.contrib import admin
from .models import Client, EventClient, Event

admin.site.register(Client)
admin.site.register(EventClient)
admin.site.register(Event)