from django.urls import path
from .views import CartView
from . import views

app_name = 'cart'
urlpatterns = [
    path('', CartView.as_view(), name = 'Cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name = 'add_item'),
    path('decrement_item/<int:product_id>/', views.decrement_item, name = 'decrement_item'),
    path('remove_item/<int:product_id>/', views.remove_item, name = 'remove_item'),
]
