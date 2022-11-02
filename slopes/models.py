from django.db import models

from slopes.utils_standalone import DateModel, SlopesEnum

SMALL_STR_SIZE = 50
MEDIUM_STR_SIZE = 200
LARGE_STR_SIZE = 2000


class Slope(DateModel):
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
    SEASON_OPENING = "SEASON_OPENING"
    SEASON_CLOSING = "SEASON_CLOSING"


class SlopeUpdateStatus(SlopesEnum):
    APPROXIMATE = "APPROXIMATE"
    CONFIRMED = "CONFIRMED"


class SlopeUpdate(DateModel):
    slope = models.ForeignKey(
        to="Slope",
        on_delete=models.CASCADE,
        null=False,
    )
    effective_date = models.DateTimeField(null=False, blank=False)
    # this is mostly for where this update came from: hypothetical based on before, resort itself, etc.
    comment: models.CharField = models.CharField(
        max_length=LARGE_STR_SIZE, null=False, blank=False
    )
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

    def __str__(self) -> str:
        return "SlopeUpdate: %s, %s, when: %s, %s, added: %s, %s" % (
            self.slope,
            self.type,
            self.effective_date.date(),
            self.status,
            self.created_at.date(),
            self.comment,
        )
