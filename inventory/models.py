from django.core.exceptions import ValidationError
from django.db import models

from inventory.currency import currencies


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="category_images", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="category_thumbnails", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE,
                                        null=True, blank=True, related_name='categories')
    keywords = models.TextField(null=True, help_text="Keywords separated by comma")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.image.name) if self.image else ''

    def thumbnail_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.thumbnail.name)\
            if self.thumbnail else ''

    image_tag.short_description = "Image Preview"
    thumbnail_tag.short_description = "Thumbnail Preview"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='products')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    rating = models.FloatField(default=5)
    visible = models.BooleanField(default=True, help_text="Appear in product listings")
    description = models.TextField(null=True)
    keywords = models.TextField(null=True, help_text="Keywords separated by comma")
    tag = models.ManyToManyField('Tag', related_name="product")

    def __str__(self):
        return self.name

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.image.name) if self.image else ''

    def thumbnail_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="60" height="60"/>' % self.thumbnail.name) \
            if self.thumbnail else ''

    image_tag.short_description = "Image Preview"
    thumbnail_tag.short_description = "Thumbnail Preview"


PRODUCT_FEATURE_TYPES = (
    ("color", "Color"),
    ("size", "Size"),
)


class ProductFeature(models.Model):
    is_cleaned = False
    type = models.CharField(max_length=100, choices=PRODUCT_FEATURE_TYPES, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_feature")
    parent_feature = models.ForeignKey("ProductFeature", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ('type', 'value', 'product')

    def clean(self):
        self.is_cleaned = True
        if self.type == "color":
            self.validate_color(self.value)
        super(ProductFeature, self).clean()

    @staticmethod
    def validate_color(color: str):
        if not color.startswith("#") and (len(color) == 7 or len(color) == 9):
            raise ValidationError("Invalid color code")

    def save(self, *args, **kwargs):
        if not self.is_cleaned:
            self.full_clean()
        super(ProductFeature, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name or ''} {self.product.name}"


DISCOUNT_TYPES = (
    ("flat", "Flat"),
    ("percentage", "Percentage"),
)


class ProductVariation(models.Model):
    feature = models.OneToOneField("ProductFeature", on_delete=models.CASCADE,
                                   related_name="product_variation", null=True)
    measurement_unit = models.ForeignKey("MeasurementUnit", on_delete=models.CASCADE, null=True, blank=True)
    currency = models.ForeignKey('SupportedCurrency', on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPES, null=True, blank=True)

    def __str__(self):
        return f"{self.feature.name or ''} {self.feature.product.name} cost {self.price}"


class ProductVariationImage(models.Model):
    product_variation = models.ForeignKey("ProductVariation",
                                          on_delete=models.CASCADE, related_name="production_variation_image")
    image = models.ImageField(upload_to="product_variation_images")
    thumbnail = models.ImageField(upload_to="production_variation_thumbnails")

    def __str__(self):
        return str(self.product_variation)


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


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
