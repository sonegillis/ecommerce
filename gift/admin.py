from django.contrib import admin
from .models import Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):
    model = Offer
