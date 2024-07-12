from django.test import TestCase
from django.urls import reverse

from accounts.models import User


# Create your tests here.
class AccountsLoginTests(TestCase):

    def test_url_available_by_name(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)


class AccountsRegisterTest(TestCase):

    def test_url_available_by_name(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        response = self.client.get(reverse("accounts:register"))

        self.assertContains(response, "<h1>Create an account</h1>")
        self.assertContains(response, "Username")
        self.assertContains(response, "Password")
        self.assertContains(response, "Continue")


class AccountsLogoutTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user("test1", "abc@123.com", "thisisatest")
        login = self.client.login(username="test1", password="thisisatest")

    def test_url_available_by_name(self):
        response = self.client.post(reverse("accounts:logout"))
        self.assertEqual(response.status_code, 200)
