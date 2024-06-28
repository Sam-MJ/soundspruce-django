from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from . import forms
from accounts.models import User

# Create your views here.


# this is so you can log in with an email
class LoginView(auth_views.LoginView):
    form_class = forms.LoginForm


class PasswordResetView(auth_views.PasswordResetView):
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data["form"].fields["email"].label = "Email address"
        return context_data


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")
    form_class = forms.UserRegisterForm
    success_message = "Your profile was created successfully"


class RegisterConfirmView(auth_views.PasswordResetConfirmView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
