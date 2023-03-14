from django.contrib import admin
from django.template.loader import get_template

from inventory.models import Product, Category, SupportedCurrency, ProductVariation, ProductVariationDeviceImage, \
    ProductFeature, ProductVariationImage, Tag


class ProductVariationImageInline(admin.StackedInline):
    model = ProductVariationImage


class ProductVariationInline(admin.StackedInline):
    model = ProductVariation

    def price_inline(self, obj=None, *args, **kwargs):
        context = {}
        admin_response = ProductFeatureAdmin(self.model, self.modeladmin.admin_site).add_view(self.request)
        inline = admin_response.context_data['inline_admin_formsets'][0]
        return get_template(inline.opts.template).render(context | {'inline_admin_formset': inline},
                                                         self.modeladmin.request)


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


@admin.register(ProductVariationDeviceImage)
class ProductVariationDeviceImageAdmin(admin.ModelAdmin):
    inlines = [ProductVariationImageInline]


@admin.register(SupportedCurrency)
class SupportedCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("parent_category", )

    readonly_fields = ("image_tag", "thumbnail_tag")
