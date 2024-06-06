from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

# Create your views here.
from contact.forms import ContactForm
from contact.models import Enquiry


class ContactView(FormView):
    template_name = "contact/contact.html"
    success_url = "contact:success"
    form_class = ContactForm

    def form_valid(self, form) -> HttpResponse:
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        form.save()

        return super(ContactView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("contact:success")


class SuccessView(TemplateView):
    template_name = "contact/success.html"
