from django.urls import reverse
from rest_framework.test import APITestCase
from product.factories import ProductFactory

TOTAL_RECORDS = 100

class PaginationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        ProductFactory.create_batch(TOTAL_RECORDS)

    def test_product_list_uses_pagination(self):
        url = reverse('product-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('count', response.data)
        self.assertEqual(response.data['count'], TOTAL_RECORDS)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 10)  
