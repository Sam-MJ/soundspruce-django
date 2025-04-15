from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from shop.models import Product, Price


# Create your tests here.
class AccountsLoginTests(TestCase):

    def test_url_available_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)


class AccountsRegisterTest(TestCase):

    def test_url_available_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("register"))

        self.assertContains(response, "<h1>Create an account</h1>")
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")
        self.assertContains(response, "Continue")


class AccountsLogoutTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user("test1", "abc@123.com", "thisisatest")
        login = self.client.login(username="test1", password="thisisatest")

    def test_url_available_by_name(self):
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 200)


class BuyButtonReDirect(TestCase):

    def setUp(self):
        """Create product and price objects"""

        Product.objects.create(
        name="SausageFileConverter",
        stripe_product_id="1",
        slug="sausage-file-converter",
        category="S",
        )
        self.product = Product.objects.get(name="SausageFileConverter")

        Price.objects.create(product=self.product, price=7500, stripe_price_id="1")

    def test_login_required_on_checkout(self):
        """When the user isn't logged and presses the button to checkout, they should be re-directed to the login page"""
        response = self.client.get(reverse("shop:product-detail", kwargs={"slug": "sausage-file-converter"}))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("purchase:checkout", kwargs={"id": 1, "slug": "sausage-file-converter"}))
        self.assertRedirects(response, expected_url="/register/login/?next=/purchase/checkout/1/sausage-file-converter/", status_code=302)

        response = self.client.get("/register/login/?next=/purchase/checkout/1/sausage-file-converter/")
        self.assertContains(response, "Please login to continue")
