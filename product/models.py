from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Наименование категории', max_length=90, blank=False)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Instance(models.Model):
    vendor_code = models.CharField('Артикул', max_length=90, blank=False)
    name = models.CharField('Наименование', max_length=90, blank=False)
    categories = models.ManyToManyField(Category, verbose_name="Категории")

    class Meta:
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экземпляр'
        constraints = [
            models.UniqueConstraint(fields=['vendor_code'], name='unique_vendor_code'),
        ]

    def __str__(self):
        return f'{self.name}_{self.vendor_code}'


class Goods(models.Model):
    price = models.IntegerField('Цена', default=0)
    count = models.IntegerField('Количество на складе', default=0)
    instance = models.ForeignKey(
        Instance,
        verbose_name='Экземпляр',
        related_name='instance',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.price}'


class Basket(models.Model):
    count = models.IntegerField('Количество', default=0)
    goods = models.ForeignKey(
        Instance,
        verbose_name='Товар',
        related_name='goods',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Покупка в корзине'
        verbose_name_plural = 'Покупки в корзине'

    def __str__(self):
        return f'{self.count}'


class UserBasket(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.CASCADE,
    )
    goods = models.ForeignKey(
        Basket,
        verbose_name='Товар',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.user}'


class Shop(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Покупатель', on_delete=models.CASCADE,
    )
    goods = models.JSONField()

    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.user}'
