# Generated by Django 4.2.6 on 2023-10-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_always_on_stock'),
        ('customs', '0003_alter_hscode_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hscode',
            name='product',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]
