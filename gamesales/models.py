from django.db import models
import string
import random


class Customer(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='profile')
    referral_code = models.CharField(max_length=100, unique=True)
    points = models.IntegerField(default=0)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    shipping_address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    @staticmethod
    def get_random_string():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(6))

    def __str__(self):
        return "{}".format(self.user.username)

    def save(self, *args, **kwargs):
        if not self.referral_code:
            self.referral_code = Customer.get_random_string()
        return super(Customer, self).save()


class AnonymousCustomer(models.Model):
    id = models.UUIDField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_seen = models.DateTimeField(auto_now=True)
