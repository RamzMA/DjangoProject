from django.test import TestCase
from .models import ApplicationForm

# Create your tests here.
class ApplicationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.application = ApplicationForm.objects.create(
            name="Test User",
            email="testuser@example.com",
            drinksChoice="coffee"
        )

    def test_fields(self):
        self.assertIsInstance(self.application.name, str)
        self.assertIsInstance(self.application.email, str)
        self.assertIsInstance(self.application.drinksChoice, str)
