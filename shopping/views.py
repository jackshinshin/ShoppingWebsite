from django.shortcuts import render
from store.models import Product
from django.views.generic import ListView

class HomePage(ListView):
    model = Product
    template_name = 'homepage.html'
    context_object_name = 'product_list'