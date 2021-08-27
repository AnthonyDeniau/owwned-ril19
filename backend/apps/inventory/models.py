from enum import Enum
from ..asset.models import Asset
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT

class Status(Enum):
    OK = "OK"
    NON_FUNCTIONAL = "NON_FUNCTIONAL"
    LOOSE = "LOOSE"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

# Create your models here.
class InventorySession(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return f"{self.start_date} - {self.end_date} - {self.manager}"

class InventoryItem(models.Model):
    inventory_session = models.ForeignKey(InventorySession, on_delete=models.RESTRICT)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    inventorist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    comment = models.TextField()
    status = models.CharField(max_length=255, choices=Status.choices())

    def __str__(self) -> str:
        return f"{self.inventory_session} - {self.asset} - {self.inventorist} - {self.date} - {self.comment} - {self.status}"

class Inventory(models.Model):
    invetory_session = models.OneToOneField(InventorySession, on_delete=models.CASCADE)
    inventory_item = models.OneToOneField(InventoryItem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.invetory_session) + " " + str(self.inventory_item)
