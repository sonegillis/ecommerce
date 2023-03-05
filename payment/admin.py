from django.contrib import admin

from payment.models import PaymentMethod


# Register your models here.


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    list_filter = ("active",)
