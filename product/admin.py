from django.contrib import admin
from .models import Goods, Instance, Basket, Category


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instance._meta.fields]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Basket._meta.fields]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]
