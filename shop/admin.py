from django.contrib import admin
from .models import Item,Client,Purchase
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'items', 'date_purchase')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('client', 'item')