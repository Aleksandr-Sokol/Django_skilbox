# Generated by Django 4.2 on 2023-04-07 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="instance",
            options={"verbose_name": "Экземпляр", "verbose_name_plural": "Экземпляр"},
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=90, verbose_name="Наименование категории"
            ),
        ),
        migrations.AlterField(
            model_name="goods",
            name="instance",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="instance",
                to="product.instance",
                verbose_name="Экземпляр",
            ),
        ),
        migrations.AlterField(
            model_name="instance",
            name="name",
            field=models.CharField(max_length=90, verbose_name="Наименование"),
        ),
        migrations.AlterField(
            model_name="instance",
            name="vendor_code",
            field=models.CharField(max_length=90, verbose_name="Артикул"),
        ),
    ]
