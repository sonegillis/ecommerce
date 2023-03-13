# Generated by Django 4.0.3 on 2023-03-12 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_remove_productvariation_product_productprice_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariationimage',
            name='device_type',
        ),
        migrations.RemoveField(
            model_name='productvariationimage',
            name='product_variation',
        ),
        migrations.AlterField(
            model_name='productfeature',
            name='parent_feature',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.productfeature'),
        ),
        migrations.CreateModel(
            name='ProductVariationDeviceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(choices=[('mobile', 'Mobile'), ('tablet', 'Tablet'), ('desktop', 'Desktop')], max_length=20)),
                ('product_variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_variation_image', to='inventory.productvariation')),
            ],
        ),
        migrations.AddField(
            model_name='productvariationimage',
            name='product_variation_device_image',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.productvariationdeviceimage'),
            preserve_default=False,
        ),
    ]