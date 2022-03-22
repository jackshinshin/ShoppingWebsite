from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=100, blank = True)
    category_img = models.ImageField(upload_to = 'photos/categories', blank = True)
    # adding extra attributes to the model
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-category_name']
        # This allows the model for inheritance by other model class
        # abstract = True

    def get_url(self):
        return reverse('products_by_category', args = [self.category_slug])
    def __str__(self):
        return self.category_name