from django.db import models

# Create your models here.


class Offer(models.Model):
    category = models.CharField(max_length=20)
    value = models.FloatField(help_text="Percentage value off")
    image = models.ImageField(upload_to="offers")
    thumbnail = models.ImageField(upload_to="offers_thumbnail")
    product = models.ForeignKey('inventory.Product', related_name='offers')

    def __str__(self):
        return f"Up to {self.value}% OFF {self.category}"
