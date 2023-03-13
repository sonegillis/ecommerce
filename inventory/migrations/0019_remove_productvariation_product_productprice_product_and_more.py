# Generated by Django 4.0.3 on 2023-03-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_productfeature_productvariation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariation',
            name='product',
        ),
        migrations.AddField(
            model_name='productprice',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='parent_feature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.productfeature'),
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='type',
            field=models.CharField(choices=[('color', 'Color'), ('size', 'Size')], max_length=100),
        ),
    ]
