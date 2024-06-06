from django import forms
from django.core.validators import EmailValidator

from contact.models import Enquiry


class ContactForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ["name", "email", "subject", "message"]
        widgets = {"message": forms.widgets.Textarea}
