# Generated by Django 4.0.3 on 2023-03-11 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_category_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='keywords',
        ),
    ]