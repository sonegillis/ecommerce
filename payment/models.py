from django.db import models


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to="payment_method_logo")
    detail = models.CharField(max_length=50, blank=True)
    detail_name = models.CharField(max_length=100, blank=True)
    active = models.BooleanField(default=False)
    show_qrcode = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_logo(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="/media/%s" width="150" height="150"/>' % self.logo.name)