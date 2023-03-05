from django.db import models

from inventory.currency import currencies


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE,
                                        null=True, blank=True, related_name='categories')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images')
    rating = models.FloatField(default=5)
    visible = models.BooleanField(default=True, help_text="Appear in product listings")
    description = models.TextField(null=True)
    thumbnail = models.ImageField(null=True)

    def get_image(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.image.name)

    def get_thumbnail(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.thumbnail.name)

    get_image.short_description = "Image Preview"
    get_thumbnail.short_description = "Thumbnail Preview"

    def __str__(self):
        return self.name


class ProductPrice(models.Model):
    product = models.OneToOneField("Product", on_delete=models.CASCADE, related_name="product_price")
    price = models.FloatField()
    measurement_unit = models.ForeignKey("MeasurementUnit", on_delete=models.CASCADE, null=True, blank=True)
    currency = models.ForeignKey('SupportedCurrency', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price)


class MeasurementUnit(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SupportedCurrency(models.Model):
    symbol = models.CharField(max_length=100, choices=currencies.items(), unique=True)

    class Meta:
        verbose_name_plural = "Supported Currencies"

    def __str__(self):
        return self.symbol
