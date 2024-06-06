from django.db import models
from django.core.validators import EmailValidator

# Create your models here.


class Enquiry(models.Model):
    name = models.CharField(name="name", max_length=100, blank=False)
    email = models.EmailField(name="email", blank=False, validators=[EmailValidator])
    subject = models.CharField(name="subject", blank=True, max_length=200)
    message = models.TextField(name="message", blank=False)
    sent_date = models.DateTimeField(name="sent_date", auto_now_add=True)
