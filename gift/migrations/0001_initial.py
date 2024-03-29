# Generated by Django 4.0.3 on 2023-03-18 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0027_remove_productvariationimage_product_variation_device_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('value', models.FloatField(help_text='Percentage value off')),
                ('image', models.ImageField(upload_to='offers')),
                ('thumbnail', models.ImageField(upload_to='offers_thumbnail')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='inventory.product')),
            ],
        ),
    ]
