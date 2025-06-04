from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"
    extra_context = {"title": "About"}

class RefundPolicy(TemplateView):
    template_name = "pages/refund_policy.html"
    extra_context = {"title":"Refund Policy"}
