import uuid
from django.db import models

CATEGORY_CHOICES = ("S", "Software")


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(unique=True)


class ProductInstance(models.Model):
    serial_number = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey("Product", on_delete=models.RESTRICT)
    purchase_date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey("Customer", on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField
