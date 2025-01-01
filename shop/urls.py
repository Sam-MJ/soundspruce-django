from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="shop"),
    path(
        "library/",
        views.ProductInstanceList.as_view(),
        name="product-instance-list",
    ),
    path("<slug:slug>/", views.product_detail_view, name="product-detail"),
    path("<slug:slug>/download", views.product_download, name="product-download"),
]
