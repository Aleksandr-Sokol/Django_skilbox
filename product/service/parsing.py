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
