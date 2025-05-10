from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
from shop.models import Product, ProductInstance, Price, ProductDistributable
from purchase.models import Purchase
from accounts.models import User


class TestProductInstanceList(TestCase):

    def setUp(self) -> None:
        """Create a user, product, price, purchase and product instance objects to test full product delivery"""
        self.user = User.objects.create_user("test1", "abc@123.com", "thisisatest")
        login = self.client.login(username="test1", password="thisisatest")

        Product.objects.create(
            name="SausageFileConverter",
            stripe_product_id="1",
            slug="sausage-file-converter",
            category="S",
        )
        self.product = Product.objects.get(name="SausageFileConverter")

        Price.objects.create(product=self.product, price=7500, stripe_price_id="1")
        self.price = Price.objects.get(stripe_price_id="1")

        purchase = Purchase.objects.create(
            user=self.user,
            product=self.product,
            price=self.price,
            stripe_checkout_session_id="1",
            completed=True,
        )

        self.product_instance = ProductInstance.objects.create(
            product=purchase.product, purchaser=purchase.user
        )

        mock_file = SimpleUploadedFile("SausageFileConverter_1.3.3.exe", b"this is test content, hello world!")
        self.product_deliverable = ProductDistributable.objects.create(
            product=purchase.product, title="PC v1.3.3", file=mock_file
        )

    def test_product_exists_in_product_instance_list(self):
        """Product exists in library after purchase"""
        response = self.client.get(reverse("shop:product-instance-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SausageFileConverter")
        self.assertContains(response, "Download")
        self.assertNotContains(response, "You own no products")
        self.assertQuerySetEqual(
            response.context["purchased_products_list"], [self.product_instance]
        )


class TestProductDetailList(TestCase):

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

    def test_product_detail_exists(self):
        response = self.client.get(reverse("shop:product-detail", kwargs={"slug": "sausage-file-converter"}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SausageFileConverter")
        self.assertContains(response, "Buy Now")
