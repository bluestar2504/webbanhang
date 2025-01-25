from django.test import TestCase, Client
from django.urls import reverse
from .models import Product

class GetHomeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('home')  # Use 'home' as the URL pattern name

        # Create test data
        Product.objects.create(name='Product 1', category='Category 1', origin='Origin 1', price=10)
        Product.objects.create(name='Product 2', category='Category 2', origin='Origin 2', price=20)
        Product.objects.create(name='Product 3', category='Category 1', origin='Origin 1', price=30)

    def test_gethome_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertIn('page_obj', response.context)
        self.assertIn('categories', response.context)
        self.assertIn('origins', response.context)

    def test_gethome_view_with_filters(self):
        response = self.client.get(self.url, {'category': 'Category 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 2)

        response = self.client.get(self.url, {'origin': 'Origin 2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 1)

        response = self.client.get(self.url, {'price_range': '10-20'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 2)

        response = self.client.get(self.url, {'price_range': '>20'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj']), 1)