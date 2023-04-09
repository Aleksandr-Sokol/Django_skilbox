from rest_framework import viewsets
from .models import Goods, Instance, Basket, Category
from .serializer import InstanceListSerializer
from .service import CommonResultsSetPagination


class InstanceView(viewsets.ModelViewSet):
    """
    perform_create - действие после создания
    Если поле country пустое, то для бренда указываться country=china
    """
    queryset = Instance.objects.all()
    serializer_class = InstanceListSerializer
    pagination_class = CommonResultsSetPagination

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
        self.query_category = request.GET.get("category", "Верхняя одежда")
        return super().list(request, *args, **kwargs)
