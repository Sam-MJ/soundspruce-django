from django.urls import path

from . import views

urlpatterns = [path("shop", views.ProductDetailView.as_view(), name="shop")]
