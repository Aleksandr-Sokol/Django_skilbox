from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path
from .models import Goods, Instance, Basket, Category, UserBasket, Shop
from django import forms
from django.db import transaction
from .service import parsing_scv
from .service.parsing import to_string


class CSVImportForm(forms.Form):
    csv_file = forms.FileField(label='CSV файл с данными')


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Goods._meta.fields]
    change_list_template = "admin/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        '''
        Задача от бизнеса:
        Главное - артикул!
        По артикулу ищем предмет и получаем его группу
        Если такого артикула нет, то создаем предмет, группу и запись в товары
        '''
        if request.method == "POST":
            data = request.FILES["csv_file"].read().decode('utf8')
            parsing_scv(data)



            self.message_user(request, "Данные импортированны")
            return redirect(f"../..")
        form = CSVImportForm()
        payload = {"form": form}
        return render(
            request, "admin/csv_form.html", payload
        )


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instance._meta.fields]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Basket._meta.fields]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


@admin.register(UserBasket)
class UserBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserBasket._meta.fields]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Shop._meta.fields]
    change_list_template = "admin/changelist_export.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export_catalog_item/', self.export_catalog_item),
        ]
        return my_urls + urls

    def export_catalog_item(self, request):
        if request.method == "GET":
            shops = Shop.objects.all()
            filename = "export.csv"
            response = HttpResponse(content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            response.write(to_string(shops))
            return response
        return redirect(".")