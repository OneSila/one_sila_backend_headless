# Generated by Django 5.1 on 2024-08-30 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0006_alter_vatrate_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='vatrate',
            name='created_by_multi_tenant_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='%(class)s_created_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vatrate',
            name='last_update_by_multi_tenant_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='%(class)s_last_update_by_multi_tenant_user_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
