from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from slopes.models import SlopeUpdate, Slope


def index(request: HttpRequest) -> HttpResponse:
    slope_list = Slope.objects.order_by("name")
    latest_updates_for_each_slope = []
    for slope_item in slope_list:
        latest_update = SlopeUpdate.objects.filter(slope=slope_item).latest()
        latest_update_dict = {}
        latest_update_dict["slope"] = latest_update.slope
        latest_update_dict["type"] = latest_update.type.replace('_', ' ').title()
        latest_update_dict["effective_date"] = latest_update.effective_date
        latest_update_dict["status"] = latest_update.status.replace('_', '').title()
        latest_update_dict["created_at"] = latest_update.created_at
        latest_updates_for_each_slope.append(latest_update_dict)
    context = {
        "slope_list": slope_list,
        "latest_updates_for_each_slope": latest_updates_for_each_slope,
    }
    return render(request, 'slopes/index.html', context)

def slope(request: HttpRequest, slope_id: int) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index. %s" % slope_id)


def unused_test_view(request: HttpRequest) -> HttpResponse:
    latest_slope_update_list = SlopeUpdate.objects.order_by("-created_at")[:5]
    template = loader.get_template("slopes/unused_test_view.html")
    context = {
        "latest_slope_update_list": latest_slope_update_list,
    }
    return HttpResponse(template.render(context, request))
