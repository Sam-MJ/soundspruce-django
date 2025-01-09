from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin
from .models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(ModelAdmin):
    list_display = ["email", "message","sent_date"]
