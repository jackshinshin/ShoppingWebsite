from django.contrib import admin
from .models import Product, Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'images', 'price', 
                    'stock', 'category', 'creation_date', 
                    'modification_date', 'is_available')
    prepopulated_fields = {'product_slug':('product_name',)}
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)