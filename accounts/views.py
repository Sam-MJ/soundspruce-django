from django.forms import BaseForm
from django.http.response import HttpResponse
from django.shortcuts import render, resolve_url
from django.utils.http import url_has_allowed_host_and_scheme
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from accounts.models import User

# Create your views here.

class LoginView(auth_views.LoginView):
    form_class = forms.LoginForm
    extra_context = {"title": "Log In"}

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name, self.request.GET.get(self.redirect_field_name)
        )

        # When you press buy on a product page
        # Redirecting to stripe checkout requires a POST request which is not supported by the browser
        # Instead re-direct back to the product page.
        if redirect_to and "/purchase/checkout/" in redirect_to:
            new_url = redirect_to.split("/")
            new_url = [section for section in new_url if section]
            redirect_to = "/shop/" + new_url[-1]

        url_is_safe = url_has_allowed_host_and_scheme(
        url=redirect_to,
        allowed_hosts=self.get_success_url_allowed_hosts(),
        require_https=self.request.is_secure(),
        )

        return redirect_to if url_is_safe else ""



class PasswordResetView(auth_views.PasswordResetView):
    form_class = forms.CustomPasswordResetForm


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    success_url = reverse_lazy("pages:home")
    form_class = forms.UserRegisterForm
    success_message = "Your profile was created successfully"
    extra_context = {"title": "Register"}

    def form_valid(self, form: BaseForm) -> HttpResponse:
        valid = super(UserRegisterView, self).form_valid(form)
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get(
            "password1"
        )
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid


class RegisterConfirmView(auth_views.PasswordResetConfirmView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
