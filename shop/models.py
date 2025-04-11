import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

protected_files = FileSystemStorage(location='protected/')

CATEGORY_CHOICES = (("S", "Software"),)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    stripe_product_id = models.CharField(
        max_length=220, blank=True, null=True, unique=True
    )
    slug = models.SlugField(unique=True)

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    description = models.TextField(blank=True)
    demo_video = models.URLField(blank=True)
    image = models.ImageField(blank=True, upload_to="images/")
    carousel_image1 = models.ImageField(blank=True, upload_to="images/")
    carousel_image2 = models.ImageField(blank=True, upload_to="images/")
    lightbox_image1 = models.ImageField(blank=True, upload_to="images/")
    pc_file = models.FileField(storage=protected_files, blank=True)
    mac_x86_file = models.FileField(storage=protected_files, blank=True)
    mac_arm_file = models.FileField(storage=protected_files, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[self.slug])


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(default=0)

    def get_display_price(self):
        return f"{self.price / 100:.2f}"


class ProductInstance(models.Model):
    """SN and purchase date are auto-generated, product and purchaser are assigned at creation"""

    serial_number = models.UUIDField(default=uuid.uuid4, primary_key=True)
    purchase_date = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey("Product", on_delete=models.RESTRICT)
    purchaser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    mac_download_allowed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product-instance-detail", args=[str(self.serial_number)])
