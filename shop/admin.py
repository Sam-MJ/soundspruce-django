from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("name",)}


@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ("purchase_date",)
    list_display = ("product", "purchaser", "purchase_date", "serial_number")


class ProductInstanceInline(admin.TabularInline):
    extra = 0
    model = models.ProductInstance
