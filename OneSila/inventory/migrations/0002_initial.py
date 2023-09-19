# Generated by Django 4.2.5 on 2023-09-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('django_shared_multi_tenant', '0002_multitenantcompany_language'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='stock', to='products.product'),
        ),
        migrations.AddField(
            model_name='minimumstock',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_shared_multi_tenant.multitenantcompany'),
        ),
        migrations.AddField(
            model_name='minimumstock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterUniqueTogether(
            name='productstock',
            unique_together={('product', 'location')},
        ),
    ]
