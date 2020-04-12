from django.contrib import admin
from . import models


@admin.register(models.JewelryType)
class JewelryTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_added']
