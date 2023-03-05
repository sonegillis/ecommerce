from django.contrib import admin

from customer.models import Customer, AnonymousCustomer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "referral_code", "points", "phone_number")


@admin.register(AnonymousCustomer)
class AnonymousCustomerAdmin(admin.ModelAdmin):
    list_display = ("date_created", "last_seen")
    list_filter = ("date_created", )
