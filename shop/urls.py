from django.urls import path

from . import views

urlpatterns = [
    path("shop/<slug:slug>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("shop/", views.ProductListView.as_view(), name="products"),
    path(
        "shop/<uuid:serial_number>",
        views.ProductInstanceView.as_view(),
        name="product-instance-detail",
    ),
]
