from django.shortcuts import render

# Create your views here.

from django.views import generic

from shop.models import Product


class ProductDetailView(generic.DetailView):
    model = Product
