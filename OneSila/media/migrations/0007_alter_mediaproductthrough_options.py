# Generated by Django 5.1.1 on 2024-09-19 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0006_media_created_by_multi_tenant_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediaproductthrough',
            options={'ordering': ('sort_order',)},
        ),
    ]
