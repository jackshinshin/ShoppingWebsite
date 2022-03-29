from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # pre-populated fileds
    prepopulated_fields = {'category_slug':('category_name',)}
    list_display = ('category_name', 'category_slug')
admin.site.register(Category, CategoryAdmin)