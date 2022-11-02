from django.db import models

from slopes.utils_standalone import DateModel, SlopesEnum

SMALL_STR_SIZE = 50
MEDIUM_STR_SIZE = 200
LARGE_STR_SIZE = 2000


class Slope(DateModel, models.Model):
    name: models.CharField = models.CharField(
        max_length=MEDIUM_STR_SIZE, null=False, blank=False
    )

    def __str__(self) -> str:
        return "Slope: {}".format(self.name)


# updates can be:
# * about opening
# * about closing
# * just a conditions update? (maybe add later, not now)
class SlopeUpdateType(SlopesEnum):
    SEASON_OPENING = "season_opening"
    SEASON_CLOSING = "season_closing"


class SlopeUpdateStatus(SlopesEnum):
    APPROXIMATE = "approximate"
    CONFIRMED = "confirmed"


class SlopeUpdate(DateModel, models.Model):
    type: models.CharField = models.CharField(
        max_length=SMALL_STR_SIZE,
        null=False,
        blank=False,
        choices=SlopeUpdateType.model_choices(),
    )
    status: models.CharField = models.CharField(
        max_length=SMALL_STR_SIZE,
        null=False,
        blank=False,
        choices=SlopeUpdateStatus.model_choices(),
    )
    effective_date = models.DateTimeField(null=False, blank=False)
    slope = models.ForeignKey(
        to="Slope",
        on_delete=models.CASCADE,
        null=False,
    )
    # this is mostly for where this update came from: hypothetical based on before, resort itself, etc.
    comment: models.CharField = models.CharField(
        max_length=LARGE_STR_SIZE, null=False, blank=False
    )

    def __str__(self) -> str:
        return (
            "SlopeUpdate:  slope: %s, type: %s, status: %s, effective_date: %s, created_at: %s"
            % (self.slope, self.type, self.status, self.effective_date, self.created_at)
        )
