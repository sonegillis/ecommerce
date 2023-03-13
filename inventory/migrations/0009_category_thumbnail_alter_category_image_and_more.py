# Generated by Django 4.0.3 on 2023-03-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_remove_product_image_remove_productprice_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='category_thumbnails'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='color',
            field=models.CharField(help_text='Color code for e.g #000000 is black', max_length=9),
        ),
    ]