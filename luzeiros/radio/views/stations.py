from django.http import request
from django.http import HttpResponse
from .azura import Azura


def get_stations(request):
    content = Azura()
    return HttpResponse(content.now(), content_type='application/vnd.api+json')


def get_station(request, id):
    api_client = Azura()
    response = api_client.single(pk=id)
    content = response[0]
    status_code = response[1]
    return HttpResponse(content, content_type='application/vnd.api+json', status=status_code)
