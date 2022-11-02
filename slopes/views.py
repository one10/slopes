from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.template import loader

from slopes.models import SlopeUpdate


def index(request: HttpRequest) -> HttpResponse:
    latest_slope_update_list = SlopeUpdate.objects.order_by("-created_at")[:5]
    template = loader.get_template("slopes/index.html")
    context = {
        "latest_slope_update_list": latest_slope_update_list,
    }
    return HttpResponse(template.render(context, request))


def slope(request: HttpRequest, slope_id: int) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index. %s" % slope_id)


def unused_test_view(request: HttpRequest) -> HttpResponse:
    latest_slope_update_list = SlopeUpdate.objects.order_by("-created_at")[:5]
    template = loader.get_template("slopes/unused_test_view.html")
    context = {
        "latest_slope_update_list": latest_slope_update_list,
    }
    return HttpResponse(template.render(context, request))
