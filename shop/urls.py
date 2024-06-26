from django.urls import path

from . import views

urlpatterns = [
    path("shop/<slug:slug>/", views.ProductDetailView.as_view(), name="product-detail")
]
