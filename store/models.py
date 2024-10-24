from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length =255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Collection(models.Model):
    title = models.CharField(max_length=255)

class Cart(models.Model):
    title = models.CharField(max_length=255)

class CartItem(models.Model):
    cart =
    product =
    quantity =