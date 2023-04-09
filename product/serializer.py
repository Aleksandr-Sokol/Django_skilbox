from .models import Goods, Instance, Basket, Category
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
