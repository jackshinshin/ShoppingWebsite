from ast import Store
from django.urls import path
from .views import ProductDetailView, SearchView, StoreView

app_name = 'store'
urlpatterns = [
    path('', StoreView.as_view(), name = 'Store'),
    path('category/<slug:catslug>/', StoreView.as_view(), name = 'products_by_category'),
    path('category/<slug:catslug>/<slug:prodslug>/', ProductDetailView.as_view(), name = 'products_details'),
    path('search/', SearchView.as_view() ,name = 'search')
]
# {{category.get_url}}