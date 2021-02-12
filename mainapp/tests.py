from django.test import TestCase, Client

from mainapp.models import ProductCategory, Product


class TestMainApp(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(
            name="Test1"
        )
        Product.objects.create(
            category=category,
            name='Prod1'
        )
        Product.objects.create(
            category=category,
            name='Prod2'
        ),
        self.client = Client

    def test_mainapp_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)



