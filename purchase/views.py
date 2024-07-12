from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import stripe.error
from shop.models import Product, Price, ProductInstance
from purchase.models import Purchase
import stripe
import logging

from soundspruce.settings import DOMAIN_URL, STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET

stripe.api_key = STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "purchase/success.html"
    # thank you, and re-direct to product-instance list


class CancelView(TemplateView):
    template_name = "purchase/cancel.html"


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

    success_path = reverse("purchase:success")
    cancel_path = reverse("purchase:stopped")
    assert success_path.startswith("/") and cancel_path.startswith("/")

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price": price.stripe_price_id,
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


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        session_id = session.get("id", None)

        purchase = get_object_or_404(Purchase, stripe_checkout_session_id=session_id)
        purchase.completed = True
        ProductInstance.objects.create(
            product=purchase.product, purchaser=purchase.user
        )
        purchase.save()

    return HttpResponse(status=200)
