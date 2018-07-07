# -*- encoding: utf-8 -*-
import logging
import sys
import json
import requests

from django.core.management import BaseCommand

from blinkstick.models import EventClient

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Update state from Uanataca'

    def handle(self, *args, **options):

        self.stdout.write('*' * 90)
        self.stdout.write('Inicio Actualiza estados')
        self.stdout.write('*' * 90)

        SHOW_MODES = {
            'dnd': {
                'status': 'red',
                'description': 'Do not disturb'
            },
            'xa': {
                'status': 'orange',
                'description': 'Away'
            },
            'chat': {
                'status': 'green',
                'description': 'Available'
            }
        }

        API_KEY = 'IDuE9yiFYkAvUIHEZetYBV0C7L9nU138HWRGo5HV'

        headers = {
            'Authorization': 'Bearer {}'.format(API_KEY),
            'Content-Type': 'application/json'
        }

        for user_event in EventClient.object.filter(event__name='Hipchat'):

            email = user_event.client.email

            url = 'https://api.hipchat.com/v2/user/{}'.format(email)
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                info = res.json()
                presence = info.get('presence')
                if presence:
                    status = {
                        'is_online': presence.get('is_online'),
                        'status': SHOW_MODES.get(presence.get('show')),
                        'message': presence.get('status')
                    }

            # Notificar al cliente el estado

        self.stdout.write('*' * 90)
        self.stdout.write(_(u'Finaliza Actualiza estados'))
        self.stdout.write('*' * 90)

