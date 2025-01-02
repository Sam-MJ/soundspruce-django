from django import forms
from django_recaptcha.fields import ReCaptchaField, ReCaptchaV3

from contact.models import Enquiry, WaitList


class ContactForm(forms.ModelForm):

    captcha = ReCaptchaField(
    widget=ReCaptchaV3(
        attrs={
            'required_score':0.85
        },action="contact"
    )
)
    class Meta:
        model = Enquiry
        fields = ["first_name", "last_name", "email", "subject", "message"]
        widgets = {"message": forms.widgets.Textarea}


class WaitListForm(forms.ModelForm):

    class Meta:
        model = WaitList
        fields = "__all__"
        # fields = ["first_name", "last_name", "email", "product"]
