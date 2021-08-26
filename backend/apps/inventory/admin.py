from backend.apps.inventory.models import Inventory, InventoryItem, InventorySession
from django.contrib import admin

# Register your models here.
admin.site.register(Inventory, InventoryItem, InventorySession)