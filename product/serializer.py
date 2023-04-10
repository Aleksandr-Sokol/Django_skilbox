from .models import Goods, Instance, Basket, Category, UserBasket
from rest_framework import serializers


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class InstanceListSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Instance
        fields = ['vendor_code', 'name', 'categories']



class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instance
        fields = ['id', 'vendor_code', 'name', 'categories']


class BasketSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(required=False, allow_null=True)

    class Meta:
        model = Basket
        fields = ['id', 'count', 'goods']