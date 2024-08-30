from django.forms import BaseForm
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.http import url_has_allowed_host_and_scheme
from . import forms
from accounts.models import User

# Create your views here.


# this is so you can log in with an email
""" class LoginView(auth_views.LoginView):
    form_class = forms.LoginForm """


""" class PasswordResetView(auth_views.PasswordResetView):
    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data["form"].fields["email"].label = "Email address"
        return context_data """


""" class PasswordChangeView(auth_views.PasswordChangeView):
    success_url = reverse_lazy("password_change_done") """


""" class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("password_reset") """


class UserRegisterView(SuccessMessageMixin, CreateView):
    template_name = "accounts/register.html"
    form_class = forms.UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form: BaseForm) -> HttpResponse:
        valid = super(UserRegisterView, self).form_valid(form)
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get(
            "password1"
        )
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        next_page = self.request.GET.get("next")
        if next_page:
            context["next"] = next_page
        return context

    def get_success_url(self):

        if url_has_allowed_host_and_scheme(self.request.POST.get("next"), None):
            redirect_to = self.request.POST.get("next")
        else:
            redirect_to = None

        return redirect_to or reverse_lazy("pages:home")


class RegisterConfirmView(auth_views.PasswordResetConfirmView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
