# Generated by Django 5.0.2 on 2024-04-03 09:52

from django.db import migrations

def create_default_vatrate(apps, schema_editor):
    VatRate = apps.get_model('taxes', 'VatRate')
    Product = apps.get_model('products', 'Product')

    for product in Product.objects.all():
        default_vat_rate, _ = VatRate.objects.get_or_create(name='10%', rate=10, multi_tenant_company=product.multi_tenant_company)
        product.vat_rate = default_vat_rate
        product.save()


def revert_default_vatrate(apps, schema_editor):
    Product = apps.get_model('products', 'Product')

    for product in Product.objects.all():
        product.vat_rate = None
        product.save()
class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_vat_rate'),
    ]

    operations = [
        migrations.RunPython(create_default_vatrate, revert_default_vatrate),
    ]
