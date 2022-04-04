from django.urls import path
from .views import CartView
from . import views

app_name = 'cart'
urlpatterns = [
    path('', CartView.as_view(), name = 'Cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name = 'add_item')
]
