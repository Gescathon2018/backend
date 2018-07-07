from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^grafana$', views.grafana, name='grafana'),
    url(r'^$', views.room, name='room')
]