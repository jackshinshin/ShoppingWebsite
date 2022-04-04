from ast import Store
from django.urls import path
from .views import ProductDetailView, StoreView

app_name = 'store'
urlpatterns = [
    path('', StoreView.as_view(), name = 'Store'),
    path('<slug:catslug>/', StoreView.as_view(), name = 'products_by_category'),
    path('<slug:catslug>/<slug:prodslug>/', ProductDetailView.as_view(), name = 'products_details'),
]
# {{category.get_url}}