# Generated by Django 3.2.11 on 2023-03-05 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0001_initial'),
        ('customer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_ordered', models.BooleanField(default=False)),
                ('anonymous_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='gamesales.anonymouscustomer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Order Status',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30, unique=True)),
                ('cost', models.FloatField()),
                ('state', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('shipping_address', models.CharField(default='', max_length=100)),
                ('phone_number', models.CharField(default='', max_length=15)),
                ('is_paid', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('payment_screenshot', models.ImageField(null=True, upload_to='payment_screenshots')),
                ('cart', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.cart')),
                ('order_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='sales.orderstatus')),
                ('payment_method', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='payment.paymentmethod')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.cart')),
                ('measurement_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurement_units', to='inventory.measurementunit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='inventory.product')),
            ],
            options={
                'unique_together': {('cart', 'product', 'measurement_unit')},
            },
        ),
    ]
