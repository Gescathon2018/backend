from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views import View


class TestView(View):
    my_param = 'ciccio'
    def get(self, request):
        return HttpResponse(self.my_param)
