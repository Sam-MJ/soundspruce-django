from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    pass
