# Generated by Django 5.0 on 2024-01-05 07:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eKart_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('company_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('profile_image', models.ImageField(upload_to='seller/')),
                ('login_id', models.IntegerField(null=True)),
                ('account_number', models.BigIntegerField(default=0)),
                ('bank_name', models.CharField(max_length=20)),
                ('bank_branch', models.CharField(default='', max_length=20)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('status', models.CharField(default='pending', max_length=50)),
            ],
            options={
                'db_table': 'seller_tb',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_no', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='Product/')),
                ('rating', models.FloatField(default=0)),
                ('status', models.CharField(default='available', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eKart_admin.category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
            options={
                'db_table': 'product_tb',
            },
        ),
    ]
