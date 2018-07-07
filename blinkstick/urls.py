from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^grafana$', views.grafana, name='grafana'),
    url(r'^reg_client$', views.reg_client, name='reg_client'),
    url(r'^$', views.room, name='room')
]