from django.db import models
from django.conf import settings

# Create your models here.
from shop.models import Product, Price


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.ForeignKey(Price, null=True, on_delete=models.SET_NULL)

    stripe_checkout_session_id = models.CharField(
        max_length=220, null=True, blank=True, unique=True
    )

    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
