from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

# Create your views here.
from soundspruce.settings import DEFAULT_FROM_EMAIL, NOTIFY_EMAIL
from contact.forms import ContactForm, WaitListForm
from contact.models import Enquiry, WaitList


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm

    def form_valid(self, form) -> HttpResponse:
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        form.save()

        full_message = f"""
            Received message below from {first_name} {last_name}: {email},
            subject: {subject}
            ________________________
            {message}
            """

        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[NOTIFY_EMAIL],
        )

        return super(ContactView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("contact:success")


class WaitListView(CreateView):
    form_class = WaitListForm
    template_name = "contact/waitlist.html"

    def get_success_url(self) -> str:
        return reverse_lazy("contact:success")


class SuccessView(TemplateView):
    template_name = "contact/success.html"
