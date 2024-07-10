import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings

CATEGORY_CHOICES = (("S", "Software"),)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=220, blank=True, null=True)
    slug = models.SlugField(unique=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField()
    demo_video = models.URLField(blank=True)
    image = models.ImageField(blank=True, upload_to="images/")
    file = models.FileField(blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[self.slug])


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)


class ProductInstance(models.Model):
    serial_number = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey("Product", on_delete=models.RESTRICT)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("product-instance-detail", args=[str(self.serial_number)])
