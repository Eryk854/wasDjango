from django.test import TestCase
from django.urls import reverse, resolve

class TestUrls(TestCase):

    def test_product_list(self):
        #path = reverse('product_list')
        path = '/products/'
        assert resolve(path).view_name == 'product_list'

    def test_product_details(self):
        path = reverse('product_details', kwargs={'product_id':1})
        assert resolve(path).view_name == 'product_details'