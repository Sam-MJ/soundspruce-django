from django.shortcuts import render
from django.views.generic import FormView, TemplateView

# Create your views here.


class ContactView(FormView):
    template_name = "contact/contact.html"
    success_url = "contact/success.html"
