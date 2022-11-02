from enum import Enum
from typing import Any, Tuple

from django.db import models


# this is an abstract model, just no idea how to attach ABC to it cuz causes metaclass conflicts
class DateModel(models.Model):
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = ["created_at"]


class SlopesEnum(Enum):
    @classmethod
    def model_choices(cls) -> Tuple[Tuple[Any, Any], ...]:
        return tuple([(attr.value, attr.name) for attr in cls])


def slope_name_to_url_str(slope_name: str) -> str:
    result = slope_name.lower()
    result = result.replace(" ", "-")
    return result


def slope_url_str_to_name(url_slope_str: str) -> str:
    result = url_slope_str.replace("-", " ")
    result = result.title()
    return result
