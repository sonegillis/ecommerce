# Generated by Django 4.0.3 on 2023-03-11 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_category_thumbnail_alter_category_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='thumbnail',
        ),
    ]