from django.test import TestCase
from mixer.backend.django import mixer
#from projekt1.sklep.models import Order, Product, OrderedProducts


class TestModels(TestCase):

    def test_order_total_price(self):
        #products = [Product.objects.get(pk=1), Product.objects.get(pk=2)]
        #products = [mixer.blend('sklep.Product'), mixer.blend('sklep.Product')]
        order = mixer.blend('sklep.Order',products=[{'product': products[0], 'order' :1,'amount': 3},
                                                    {'product': products[1], 'order': 1,'amount': 4}])
        assert order.get_total_prices == 44.21
