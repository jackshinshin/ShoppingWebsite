from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    product_slug    = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=300)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default = True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    creation_date   = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('store:products_by_category', args = [self.product_slug])
    def __str__(self) -> str:
        return self.product_name

variation_choices = (
    ('color', 'Color'),
    ('size', 'Size')
)
class Variation(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    # This is for dropdown list
    variation_category  = models.CharField(max_length=20, choices=variation_choices)
    variation_value     = models.CharField(max_length=20)
    is_active           = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name