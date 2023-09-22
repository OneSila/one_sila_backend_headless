# Generated by Django 4.2.5 on 2023-09-22 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_shared_multi_tenant', '0007_alter_multitenantcompany_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('price_incl_vat', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PENDING', 'Pending'), ('PENDING_INVENTORY', 'Pending Inventory'), ('TOPICK', 'To Pick'), ('TOSHIP', 'To Ship'), ('DONE', 'Done'), (
                    'CANCELLED', 'Cancelled'), ('HOLD', 'On Hold'), ('EXCHANGED', 'Exchanged'), ('REFUNDED', 'Refunded'), ('LOST', 'Lost'), ('MERGED', 'Merged'), ('DAMAGED', 'Damaged')], default='DRAFT', max_length=17)),
                ('reason_for_sale', models.CharField(choices=[('SALE', 'Sale'), ('RETURN', 'Return goods'), ('SAMPLE',
                 'Commercial Sample'), ('GIFT', 'Gift'), ('DOCUMENTS', 'Documents')], default='SALE', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.PROTECT, to='django_shared_multi_tenant.multitenantcompany')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(blank=True, null=True)),
                ('multi_tenant_company', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.PROTECT, to='django_shared_multi_tenant.multitenantcompany')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
