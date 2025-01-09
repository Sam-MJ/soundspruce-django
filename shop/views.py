from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

from django.views import generic

from shop.models import Product, Price, ProductInstance


class ProductListView(generic.ListView):
    model = Product


def product_detail_view(request, slug):
    """product detail view, is owner is passed to see if purchase button should be shown or not."""
    product = get_object_or_404(Product, slug=slug)
    price = get_object_or_404(Price, product=product)
    is_owner = False
    if request.user.is_authenticated:
        is_owner = (
            request.user.purchase_set.all()
            .filter(product=product, completed=True)
            .exists()
        )
    context = {"product": product, "price": price, "is_owner": is_owner}
    return render(request, "shop/product_detail.html", context)


class ProductInstanceList(LoginRequiredMixin, generic.ListView):
    model = ProductInstance
    context_object_name = "purchased_products_list"

    def get_queryset(self) -> QuerySet[Any]:
        return ProductInstance.objects.filter(purchaser=self.request.user)


@login_required()
def product_download(request, slug, platform):

    product = get_object_or_404(Product, slug=slug)
    download_allowed = (
        request.user.productinstance_set.all().filter(product=product).exists()
    )

    if not download_allowed:
        return HttpResponseBadRequest(
            "Bad Request, This product is not on your purchased list."
        )

    if platform == "PC":
        file_name = product.pc_file.name

        #NGINX setup
        response = HttpResponse()
        response['Content-Disposition'] = f'attachment; filename="{file_name}'
        response['X-Accel-Redirect'] = f'/protected/{file_name}'

        return response

    elif platform == "MAC_X86":
        file_name = product.mac_x86_file.name

        #NGINX setup
        response = HttpResponse()
        response['Content-Disposition'] = f'attachment; filename="{file_name}'
        response['X-Accel-Redirect'] = f'/protected/{file_name}'

        return response

    elif platform == "MAC_ARM":

        file_name = product.mac_arm_file.name

        #NGINX setup
        response = HttpResponse()
        response['Content-Disposition'] = f'attachment; filename="{file_name}'
        response['X-Accel-Redirect'] = f'/protected/{file_name}'

        return response
