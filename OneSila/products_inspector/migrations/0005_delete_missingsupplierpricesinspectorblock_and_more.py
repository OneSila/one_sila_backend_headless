# Generated by Django 5.1.1 on 2025-02-05 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products_inspector', '0004_inspector_created_by_multi_tenant_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MissingSupplierPricesInspectorBlock',
        ),
        migrations.CreateModel(
            name='MissingSupplierPriceInspectorBlock',
            fields=[
            ],
            options={
                'verbose_name': 'Inspector Block Missing Supplier Prices',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('products_inspector.inspectorblock',),
        ),
    ]
