# Generated by Django 5.1.1 on 2024-10-11 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_inventorymovement_product'),
        ('shipments', '0010_populate_inventorylocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipmentitemtoship',
            name='inventorylocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.inventorylocation'),
        ),
    ]
