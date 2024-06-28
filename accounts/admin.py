from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User
from shop import admin as shop_admin


@admin.register(User)
class MyUserAdmin(UserAdmin):
    inlines = [shop_admin.ProductInstanceInline]
