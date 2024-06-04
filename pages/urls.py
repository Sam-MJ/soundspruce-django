from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("products", views.products, name="products"),
    path("contact", views.contact, name="contact"),
    path("articles", views.articles, name="articles"),
]
