from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import TemplateView
from shop.models import Product, Price
from purchases.models import Purchase
import stripe
import logging

from soundspruce.settings import DOMAIN_URL, STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY


# Create your views here.
@login_required(login_url="accounts:login")
def create_checkout_view(request, id, slug):

    if not request.method == "POST":
        return HttpResponseBadRequest()

    # get price and products from model
    price = get_object_or_404(Price, id=id)
    product = get_object_or_404(Product, slug=slug)

    # create purchase
    purchase = Purchase.objects.create(user=request.user, product=product)

    success_path = reverse("purchases:success")
    cancel_path = reverse("purchases:stopped")
    assert success_path.startswith("/") and cancel_path.startswith("/")

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": price,
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=DOMAIN_URL + success_path,
            cancel_url=DOMAIN_URL + cancel_path,
        )
    except Exception as e:
        return HttpResponseBadRequest(e)

    purchase.stripe_checkout_session_id = checkout_session.id
    purchase.save()

    return HttpResponseRedirect(checkout_session.url)


class SuccessView(TemplateView):
    template_name = "purchases/success.html"
    # thank you, and re-direct to product-instance list


class CancelView(TemplateView):
    template_name = "purchases/cancel.html"
