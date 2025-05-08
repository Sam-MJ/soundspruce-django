from django.contrib import admin

from . import models

# Register your models here.

class PriceInlineAdmin(admin.TabularInline):
    model = models.Price
    extra = 0

class ProductDescriptionInline(admin.StackedInline):
    model = models.ProductDescriptionSection
    extra = 0

class ProductDistributableInline(admin.TabularInline):
    model = models.ProductDistributable
    extra = 0

@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductDescriptionSection)
class ProductDescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductDistributable)
class ProductDistributableAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin, ProductDescriptionInline, ProductDistributableInline]
    # prepopulated_fields = {"slug": ("name",)}

# Product Instance Admin
class ProductInstanceInline(admin.TabularInline):
    extra = 0
    model = models.ProductInstance

@admin.register(models.ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ("purchase_date",)
    list_display = ("product", "purchaser", "purchase_date", "serial_number")
