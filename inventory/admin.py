from django.contrib import admin

from inventory.models import Product, Category, ProductPrice, SupportedCurrency


class ProductPriceInline(admin.StackedInline):
    model = ProductPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPriceInline]
    list_display = ("name", "category", "measurement_unit", "product_price", "product_currency", "visible")
    list_filter = ("category", "product_price", "visible")

    def product_price(self, product):
        return product.product_price.price

    def product_currency(self, product):
        return product.product_price.currency

    def measurement_unit(self, product):
        return product.product_price.measurement_unit

    product_price.short_description = "Price"
    product_currency.short_description = "Currency"


@admin.register(SupportedCurrency)
class SupportedCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_filter = ("parent_category", )
