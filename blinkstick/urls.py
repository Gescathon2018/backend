from django.conf.urls import url

from . import views
from .utils import get_services, notify

urlpatterns = []

services = get_services('webhook')

for service in services:
    service_id = service['id']
    Clazz = service['clazz']
    uri = r'webhook/{}/$'.format(service_id)
    urlpatterns.append(
        url(uri, Clazz.as_view(service_id=service_id, notify_func=notify))
    )
