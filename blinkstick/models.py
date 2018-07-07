from django.db import models


MODES = (('S', 'Server'),
        ('M', 'Manual')
)


class Client(models.Model):
    email = models.CharField(max_length=100)
    mode = models.CharField(max_length=1, choices=MODES)
    led0 = models.CharField(max_length=20)
    led1 = models.CharField(max_length=20)
    led2 = models.CharField(max_length=20)
    led3 = models.CharField(max_length=20)
    led4 = models.CharField(max_length=20)
    led5 = models.CharField(max_length=20)
    led6 = models.CharField(max_length=20)
    led7 = models.CharField(max_length=20)


class Event(models.Model):
    name = models.CharField(max_length=30)


class EventClient(models.Model):
    event = models.ForeignKey(Event)
    client = models.ForeignKey(Client)


