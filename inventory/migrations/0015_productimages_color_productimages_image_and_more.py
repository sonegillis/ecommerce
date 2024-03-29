# Generated by Django 4.0.3 on 2023-03-11 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_remove_productimages_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='color',
            field=models.CharField(default=0, help_text='Color code for e.g #000000 is black', max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimages',
            name='image',
            field=models.ImageField(default='', upload_to='product_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='inventory.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimages',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='product_thumbnails'),
            preserve_default=False,
        ),
    ]
