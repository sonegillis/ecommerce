# Generated by Django 4.0.3 on 2023-03-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_productvariation_currency_productvariation_discount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.TextField(help_text='Keywords separated by comma', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(null=True, related_name='product', to='inventory.tag'),
        ),
    ]
