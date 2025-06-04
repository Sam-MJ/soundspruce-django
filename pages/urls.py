from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about", views.AboutView.as_view(), name="about"),
    path("refundpolicy", views.RefundPolicy.as_view(), name="refundpolicy"),
]
