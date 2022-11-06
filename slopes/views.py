from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

from slopes.models import Slope, SlopeUpdate
from slopes.utils_standalone import (slope_name_to_url_str,
                                     slope_url_str_to_name)


def _get_latest_updates_for_a_slope(slope_item: Slope) -> Dict:
    latest_update = SlopeUpdate.objects.filter(slope_id=slope_item.pk).latest()
    latest_update_dict = {}
    latest_update_dict["slope"] = latest_update.slope
    latest_update_dict["type"] = latest_update.type.replace("_", " ").title()
    # https://strftime.org/
    # latest_update_dict["effective_date"] = latest_update.effective_date.strftime("%b %-d, '%y")
    latest_update_dict["effective_date"] = latest_update.effective_date.strftime(
        "%B %-d, %Y"
    )
    latest_update_dict["slope_url"] = slope_name_to_url_str(latest_update.slope.name)
    latest_update_dict["status"] = latest_update.status.replace("_", "").title()
    # latest_update_dict["created_at"] = latest_update.created_at.strftime("%m/%d/%y")
    latest_update_dict["created_at"] = latest_update.created_at.strftime("%b %-d, %Y")
    return latest_update_dict


def index(request: HttpRequest) -> HttpResponse:
    slope_list = Slope.objects.order_by("name")
    latest_updates_for_each_slope = []
    for slope_item in slope_list:
        latest_updates_for_each_slope.append(
            _get_latest_updates_for_a_slope(slope_item)
        )
    context = {
        "slope_list": slope_list,
        "latest_updates_for_each_slope": latest_updates_for_each_slope,
    }
    return render(request, "slopes/index.html", context)


def slope(request: HttpRequest, slope_id: str) -> HttpResponse:
    slope_name = slope_url_str_to_name(slope_id)
    current_slope = Slope.objects.get(name=slope_name)
    try:
        latest_update = _get_latest_updates_for_a_slope(current_slope)
    except SlopeUpdate.DoesNotExist:
        latest_update = None
    context = {
        "slope": current_slope,
        "latest_update": latest_update,
    }
    return render(request, "slopes/slope.html", context)


def unused_test_view(request: HttpRequest) -> HttpResponse:
    latest_slope_update_list = SlopeUpdate.objects.order_by("-created_at")[:5]
    template = loader.get_template("slopes/unused_test_view.html")
    context = {
        "latest_slope_update_list": latest_slope_update_list,
    }
    return HttpResponse(template.render(context, request))


def page_not_found_view(request: HttpRequest, exception: Exception) -> HttpResponse:
    return render(request, "404.html", status=404)
