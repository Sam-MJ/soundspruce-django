from django.urls import path
from . import views

app_name = "contact"
urlpatterns = [
    path("", views.ContactView.as_view(), name="contact"),
    path("success", views.SuccessView.as_view(), name="success"),
]
