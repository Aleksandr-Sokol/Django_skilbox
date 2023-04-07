from django.db import models


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
    categories = models.ManyToManyField("Category", verbose_name="Категории", related_name='instances')

    class Meta:
        verbose_name = 'Экземпляр'
        verbose_name_plural = 'Экземпляр'
        constraints = [
            models.UniqueConstraint(fields=['vendor_code'], name='unique_vendor_code'),
        ]

    def __str__(self):
        return f'{self.name}_{self.vendor_code}'


class Goods(models.Model):
    price = models.IntegerField('Цена', blank=False)
    count = models.IntegerField('Количество на складе', blank=False)
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
    count = models.IntegerField('Количество', blank=False)
    goods = models.ForeignKey(
        Instance,
        verbose_name='Товар',
        related_name='goods',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'{self.count}'
