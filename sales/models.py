import string
import random

from django.core.exceptions import ValidationError
from django.db import models

from inventory.currency import currencies


# Create your models here.


class Order(models.Model):
    cart = models.OneToOneField('Cart', on_delete=models.CASCADE, null=True, unique=True)
    order_id = models.CharField(max_length=30, unique=True)
    cost = models.FloatField()
    currency = models.CharField(max_length=10, choices=currencies.items())
    payment_method = models.ForeignKey('payment.PaymentMethod', on_delete=models.CASCADE, default='1')
    state = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    shipping_address = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=15, default='')
    is_paid = models.BooleanField(default=False)
    order_status = models.ForeignKey('OrderStatus', null=True, on_delete=models.SET_NULL, related_name='orders')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    payment_screenshot = models.ImageField(null=True, upload_to='payment_screenshots')

    @staticmethod
    def get_random_string():
        lower_case_letters = string.ascii_lowercase
        upper_case_letters = string.ascii_uppercase
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        return ''\
            .join(random.choice(random.choice([lower_case_letters, upper_case_letters, numbers])) for i in range(6))

    def __str__(self):
        return self.order_id

    def save(self, **kwargs):
        if not self.order_id:
            self.order_id = 'PS5RESTOCK-' + self.get_random_string()
        super(Order, self).save(**kwargs)


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cart', null=True)
    anonymous_customer = models.ForeignKey('customer.AnonymousCustomer', on_delete=models.CASCADE,
                                           related_name='cart', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_ordered = models.BooleanField(default=False)

    def clean(self):
        if self.user and self.anonymous_customer:
            raise ValidationError("User and anonymous user are mutually exclusive. Only one of them should be set")

    def is_empty(self):
        return len(self.cart.products) == 0

    is_empty.short_description = "Is empty"


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items', null=True)
    product = models.ForeignKey('inventory.Product', on_delete=models.CASCADE, related_name='products')
    measurement_unit = models.ForeignKey('inventory.MeasurementUnit',
                                         on_delete=models.CASCADE, related_name='measurement_units')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('cart', 'product', 'measurement_unit')

    def __str__(self):
        return "{} has ordered {} of {}".format(self.cart.user.email, self.quantity, self.product.name)


class OrderStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Order Status'

    def __str__(self):
        return self.name
