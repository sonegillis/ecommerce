from django.contrib import admin
from django.template.loader import get_template

from inventory.models import Product, Category, SupportedCurrency, ProductVariation, \
    ProductFeature, ProductVariationImage, Tag


@admin.register(ProductVariationImage)
class ProductVariationImageAdmin(admin.ModelAdmin):
    pass


class ProductVariationImageInline(admin.StackedInline):
    model = ProductVariationImage


@admin.register(ProductVariation)
class ProductVariation(admin.ModelAdmin):
    inlines = [ProductVariationImageInline]


class ProductVariationInline(admin.StackedInline):
    model = ProductVariation


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    inlines = [ProductVariationInline]

    def get_inline_instances(self, request, obj=None):
        yield from ((inline, vars(inline).update(**{"modeladmin": self, "request": request}))[0] for inline in
                    super().get_inline_instances(request, obj))


# @admin.register(ProductVariationDeviceImage)
# class ProductVariationDeviceImageAdmin(admin.ModelAdmin):
#     inlines = [ProductVariationImageInline]


@admin.register(SupportedCurrency)
class SupportedCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("parent_category", )

    readonly_fields = ("image_tag", "thumbnail_tag")
