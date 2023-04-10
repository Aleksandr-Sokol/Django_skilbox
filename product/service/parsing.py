import csv
from product.models import Goods, Instance, Basket, Category
from django.db import transaction


@transaction.atomic()
def parsing_scv(data: str):
    lines = csv.reader(data.split('\n'), delimiter=',')
    for line in lines:
        instance, instance_created = Instance.objects.get_or_create(vendor_code=line[0], defaults={'name': line[1]})
        if instance_created:
            categorie_names = line[-1].split('|')
            for categorie_name in categorie_names:
                categorie, _ = Category.objects.get_or_create(name=categorie_name)
                instance.categories.add(categorie)
            instance.save()
        goods, good_created = Goods.objects.get_or_create(instance=instance,
                                                          defaults={'price': line[2], 'count': line[3]})
        if not good_created:
            goods.count += int(line[3])
            goods.save()


def to_string(shops: list) -> str:
    result = []

    for shop in shops:
        user = shop.user
        id = shop.id
        data = shop.goods
        for d_dict in data:
            summa = d_dict.get("summ", 0)
            count = d_dict.get("count", 0)
            name = d_dict["goods"]["name"]
            vendor_code = d_dict["goods"]["vendor_code"]
            result.append(f'{id}, {user}, {count}, {summa}, {name}, {vendor_code}')
    return '\n'.join(result)
