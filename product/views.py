from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .models import Goods, Instance, Basket, Category, UserBasket, Shop
from .serializer import InstanceListSerializer, BasketSerializer
from .service import CommonResultsSetPagination
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status


class InstanceView(viewsets.ModelViewSet):
    queryset = Instance.objects.all()
    serializer_class = InstanceListSerializer
    pagination_class = CommonResultsSetPagination
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = super().get_queryset().prefetch_related("categories")
        if self.query_name is not None:
            queryset = queryset.filter(name__contains=self.query_name)
        if self.query_category is not None:
            need_categories = Category.objects.filter(name=self.query_category).all()
            queryset = queryset.filter(categories__in=need_categories)
        return queryset

    def list(self, request, *args, **kwargs):
        self.query_name = request.GET.get("name", None)
        self.query_category = request.GET.get("category", None)
        return super().list(request, *args, **kwargs)


class UserBasketView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    @transaction.atomic()
    def buy(self, request, *args, **kwargs):
        """
        Совершить покупку из корзины
        В качестве упрощения таблица хранится в базе
        В результате требуется много запросов для выполнения данного действия
        """
        user_basket_id = request.data.get("basket_id")
        try:
            user_basket = UserBasket.objects.filter(id=user_basket_id).first()
            baskets = user_basket.goods.prefetch_related("goods").select_related('goods')
            serializer = BasketSerializer(baskets, many=True)
            data = serializer.data
            goods_update = []
            basket_ids = []
            for d in data:
                basket_ids.append(d['id'])
                instance_id = d['goods']['id']
                instance_count = d['count']
                goods = Goods.objects.filter(instance=instance_id).first()
                goods.count = goods.count - instance_count
                goods_update.append(goods)
            user_basket.delete()
            Basket.objects.filter(id__in=basket_ids).all().delete()
            Goods.objects.bulk_update(goods_update, ["count"])
            Shop.objects.create(user=request.user, goods=data)
        except Exception as e:
            raise ValidationError({'Error': f'Произошла ошибка {e}'})
        return Response(data, status=status.HTTP_200_OK)
