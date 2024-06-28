import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings

CATEGORY_CHOICES = (("S", "Software"),)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    demo_video = models.URLField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[self.slug])


class ProductInstance(models.Model):
    serial_number = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey("Product", on_delete=models.RESTRICT)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    @property
    def product_name(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse("product-instance-detail", args=[str(self.serial_number)])
