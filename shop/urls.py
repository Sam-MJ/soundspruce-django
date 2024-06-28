from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="shop"),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product-detail"),
    path(
        "<uuid:pk>",
        views.ProductInstanceView.as_view(),
        name="product-instance-detail",
    ),
]
