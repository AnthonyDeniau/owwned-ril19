from enum import Enum
from django.db import models
from django.contrib.auth.models import User

from ..asset.models import Asset


class EventType(Enum):
    LEND = "LEND"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    AVAILABLE = "AVAILABLE"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class HistoryEvent(models.Model):
    stakeholder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    description = models.TextField()
    event_type = models.CharField(max_length=50, choices=EventType.choices())
