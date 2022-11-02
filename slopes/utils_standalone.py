from enum import Enum
from typing import Any, Tuple

from django.db import models


# this is an abstract model, just no idea how to attach ABC to it cuz causes metaclass conflicts
class DateModel:
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SlopesEnum(Enum):
    @classmethod
    def model_choices(cls) -> Tuple[Tuple[Any, Any], ...]:
        return tuple([(attr.value, attr.name) for attr in cls])
