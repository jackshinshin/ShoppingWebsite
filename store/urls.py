from ast import Store
from django.urls import path
from .views import ProductDetailView, StoreView
urlpatterns = [
    path('', StoreView.as_view(), name = 'store'),
    path('<slug:catslug>/', StoreView.as_view(), name = 'products_by_category'),
    path('<slug:catslug>/<slug:prodslug>/', ProductDetailView.as_view(), name = 'products_details'),
]
