from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class CartView(TemplateView):
    template_name = 'store/cart.html'