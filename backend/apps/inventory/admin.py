from .models import Inventory, InventoryItem, InventorySession
from django.contrib import admin

# Register your models here.
models = [Inventory, InventoryItem, InventorySession]
admin.site.register(models)