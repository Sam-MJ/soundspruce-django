from django.urls import path
from . import views

app_name = "purchases"
urlpatterns = [
    path("checkout/<int:id>/<slug:slug>/", views.create_checkout_view, name="checkout"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("stopped/", views.CancelView.as_view(), name="stopped"),
]
