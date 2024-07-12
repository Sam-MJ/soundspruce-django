from django.urls import path
from . import views

app_name = "purchase"
urlpatterns = [
    path("checkout/<int:id>/<slug:slug>/", views.create_checkout_view, name="checkout"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("stopped/", views.CancelView.as_view(), name="stopped"),
    path("webhooks/stripe/", views.stripe_webhook, name="stripe-webhook"),
]
