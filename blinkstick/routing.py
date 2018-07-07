from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/bs/(?P<bs_id>[^/]+)/$', consumers.BSConsumer),
]