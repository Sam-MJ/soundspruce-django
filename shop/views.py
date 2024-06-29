from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

from django.views import generic

from shop.models import Product, ProductInstance


class ProductListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product


""" class ProductInstanceView(LoginRequiredMixin, generic.DetailView):
    model = ProductInstance """


class ProductInstanceList(LoginRequiredMixin, generic.ListView):
    model = ProductInstance

    def get_queryset(self) -> QuerySet[Any]:
        return ProductInstance.objects.filter(purchaser=self.request.user)
