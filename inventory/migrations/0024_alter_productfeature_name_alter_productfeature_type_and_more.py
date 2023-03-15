# Generated by Django 4.0.3 on 2023-03-15 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_alter_product_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeature',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='type',
            field=models.CharField(blank=True, choices=[('color', 'Color'), ('size', 'Size')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='value',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]