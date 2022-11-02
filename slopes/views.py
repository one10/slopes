from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def slope(request: HttpRequest, slope_id: int) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index. %s" % slope_id)
