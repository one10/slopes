from abc import ABC

from django.db import models

MEDIUM_STR_SIZE = 200


class DateModel(ABC, models.Model):
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Slope(DateModel):
    name: models.CharField = models.CharField(max_length=MEDIUM_STR_SIZE)
