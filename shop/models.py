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

    pc_file = models.FileField(storage=protected_files, blank=True)
    mac_x86_file = models.FileField(storage=protected_files, blank=True)
    mac_arm_file = models.FileField(storage=protected_files, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product-detail", args=[self.slug])

    def get_product_description(self):
        return self.productcontenttext_set.filter(type="LONG").order_by("order")

    def get_accordion_sections(self):
        return self.productcontenttext_set.filter(type="ACCORDION").order_by("order")

    def get_carousel_images(self):
        return self.productcontentcarousel_set.order_by("order")

    def get_videos(self):
        return self.productcontentvideo_set.order_by("order")

    def get_images(self):
        return self.productcontentimage_set.order_by("order")

class ProductContentBlock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(blank=False, max_length=120)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        abstract = True

class ProductContentText(ProductContentBlock):
    TEXT_TYPE_CHOICES = [
        ("ACCORDION", "Text content for an accordion element"),
        ("LONG", "Long text description"),
        ("SHORT", "Short text description")
    ]

    type = models.CharField(blank=False, max_length=120, choices=TEXT_TYPE_CHOICES)
    content = models.TextField(blank=False)

class ProductContentVideo(ProductContentBlock):
    video = models.URLField(blank=False)

class ProductContentImage(ProductContentBlock):
    image = models.ImageField(blank=True, upload_to="images/")

class ProductContentCarousel(ProductContentBlock):
    carousel_image = models.ImageField(blank=False, upload_to="images/")
    lightbox_image = models.ImageField(blank=True, upload_to="images/")

# not yet implemented
class ProductDistributable(models.Model):

    DISTRIBUTABLE_TYPE_CHOICES = [
        ("PC", "PC executable"),
        ("MAC_ARM", "Mac silicon executable"),
        ("MAC_INTEL", " Mac Intel executable"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.CharField(blank=False, choices=DISTRIBUTABLE_TYPE_CHOICES, max_length=120)
    file = models.FileField(storage=protected_files, blank=True)


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
