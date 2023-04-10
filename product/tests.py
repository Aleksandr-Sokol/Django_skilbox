import base64

from django.test import TestCase, modify_settings, override_settings
from django.conf import settings
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from product.models import Shop, Category, Instance, Goods, Basket, UserBasket
from django.urls import reverse
from django.contrib.auth import get_user_model

from product.service import parsing_scv

User = get_user_model()


class MyTest(APITestCase):
    def setUp(self):
        self.username = 'admin'
        self.password = 'admin'
        self.admin = User.objects.create_superuser(self.username, 'myemail@test.com', self.password)

        credentials = base64.b64encode(f'{self.username}:{self.password}'.encode('utf-8'))
        self.client.credentials(HTTP_AUTHORIZATION='Basic {}'.format(credentials.decode('utf-8')))

        category = Category.objects.create(name='Test')
        self.instance = Instance.objects.create(name='Test instance', vendor_code='vendor_code')
        self.instance.categories.add(category)
        self.instance.save()

    def test_smoke_instance_list(self):
        url = reverse("product:instance-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get('results')), 1)

    def test_smoke_instance_buy(self):
        goods = Goods.objects.create(price=10, count=2, instance=self.instance)
        basket = Basket.objects.create(count=1, goods=self.instance)
        user_basket = UserBasket.objects.create(user=self.admin)
        user_basket.goods.add(basket)
        user_basket.save()

        url = reverse("product:buy-goods")
        data = {
            "basket_id": user_basket.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_import_data(self):
        with open('product/examples/import.csv') as f:
            data = f.read()
        parsing_scv(data)
        instances = Instance.objects.all()
        self.assertEqual(len(instances), 4)
