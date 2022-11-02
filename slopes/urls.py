from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("slope/<int:slope_id>", views.slope, name="get_slope"),
    path("unused_test_view", views.unused_test_view, name="unused_test_view"),
]
