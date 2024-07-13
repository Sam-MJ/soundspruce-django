from django import forms

from contact.models import Enquiry, WaitList


class ContactForm(forms.ModelForm):

    class Meta:
        model = Enquiry
        fields = ["first_name", "last_name", "email", "subject", "message"]
        widgets = {"message": forms.widgets.Textarea}


class WaitListForm(forms.ModelForm):

    class Meta:
        model = WaitList
        fields = "__all__"
        # fields = ["first_name", "last_name", "email", "product"]
