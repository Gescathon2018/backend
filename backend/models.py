from django.db import models

class Email(models.Model):
    email = models.CharField(max_length=50)

class Mode(models.Model):
    MODES = (
        'S':'Server',
        'N':'Normal'
    )
    mode = models.CharField(max_length=1, choices=MODES)

class Leds(models.Model):   
    leds = models.CharField(max_length=1)
