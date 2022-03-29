from tkinter.tix import Tree
from django.db import models

from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id     = models.CharField(max_length=250, blank = True)
    data_added  = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.cart_id
class CartItem(models.Model):
    # take a product as a foreign key since it came from other models
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart        = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.product