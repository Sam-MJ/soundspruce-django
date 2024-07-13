from django.db import models
from django.core.validators import EmailValidator

# Create your models here.

PRODUCT_CHOICES = (("P", "PhotoGPStoMetaData"),)


class Enquiry(models.Model):
    first_name = models.CharField(name="first_name", max_length=100, blank=False)
    last_name = models.CharField(name="last_name", max_length=100, blank=False)
    email = models.EmailField(name="email", blank=False, validators=[EmailValidator])
    subject = models.CharField(name="subject", blank=True, max_length=200)
    message = models.TextField(name="message", blank=False)
    sent_date = models.DateTimeField(name="sent_date", auto_now_add=True)


class WaitList(models.Model):
    first_name = models.CharField(name="first_name", max_length=100, blank=False)
    last_name = models.CharField(name="last_name", max_length=100, blank=False)
    email = models.EmailField(name="email", blank=False, validators=[EmailValidator])
    product = models.CharField(choices=PRODUCT_CHOICES, default="P", max_length=20)
    contact_permission = models.BooleanField(
        "Contact me with development updates", default=False
    )
    date = models.DateTimeField(name="date", auto_now_add=True)
