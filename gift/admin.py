from django.contrib import admin
from .models import Offer

# Register your models here.


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass
