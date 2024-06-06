from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.
class ContactTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact:contact"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("contact:contact"))
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_template_content(self):
        response = self.client.get(reverse("contact:contact"))
        self.assertContains(response, "<h1>Contact</h1>")
        self.assertNotContains(response, "Not on the page")
