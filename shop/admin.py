from django.contrib import admin

from . import models

# Register your models here.


class PriceInlineAdmin(admin.TabularInline):
    model = models.Price
    extra = 0

@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    pass

# product content
class ProductContentTextInline(admin.StackedInline):
    model = models.ProductContentText
    extra = 0

class ProductContentVideoInline(admin.StackedInline):
    model = models.ProductContentVideo
    extra = 0

class ProductContentImageInline(admin.StackedInline):
    model = models.ProductContentImage
    extra = 0

class ProductContentCarouselInline(admin.StackedInline):
    model = models.ProductContentCarousel
    extra = 0

class ProductDistributableInline(admin.TabularInline):
    model = models.ProductDistributable
    extra = 0

@admin.register(models.ProductContentText)
class ProductContentTextAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductContentVideo)
class ProductContentVideoAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductContentImage)
class ProductContentImageAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProductContentCarousel)
class ProductContentCarouselAdmin(admin.ModelAdmin):
    pass

###

@admin.register(models.ProductDistributable)
class ProductDistributableAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin, ProductContentImageInline, ProductContentTextInline, ProductContentCarouselInline, ProductContentVideoInline, ProductDistributableInline]

# Product Instance Admin
class ProductInstanceInline(admin.TabularInline):
    extra = 0
    model = models.ProductInstance

@admin.register(models.ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ("purchase_date",)
    list_display = ("product", "purchaser", "purchase_date", "serial_number")
