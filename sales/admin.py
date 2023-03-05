from django.contrib import admin

from sales.models import Cart, Order


# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "date_created", "is_ordered",)
    list_filter = ("is_ordered", "date_created")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "date_created", "cost", "currency", "is_paid", )
    list_filter = ("date_created", "cost", "is_paid")

    def user(self, order):
        return order.cart.user

    user.short_description = "Customer"
