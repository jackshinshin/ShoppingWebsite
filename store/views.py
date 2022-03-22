from unicodedata import category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from store.models import Product
from category.models import Category
# Create your views here.
class StoreView(ListView):
    model = Product
    # queryset = Product.objects.all()
    context_object_name = 'product_list'
    template_name = 'store/store.html'
    def get_queryset(self):
        # kwargs can be used to access url variables
        
        try:
            catslug = self.kwargs['catslug']
            categories = get_object_or_404(Category, category_slug = catslug)
            return Product.objects.all().filter(category = categories, is_available = True)
        except (KeyError):
            return Product.objects.all().filter(is_available = True)
            

class ProductDetailView(DetailView):
    # template_name = "modelname_detail.html"
    model = Product
    context_object_name = 'current_product'
    def get_object(self):
        try:
            catslug = self.kwargs['catslug']
            categories = get_object_or_404(Category, category_slug = catslug)
            prodslug = self.kwargs['prodslug']
            # print(catslug)
            # print(prodslug)
            return Product.objects.get(category = categories, product_slug = prodslug, is_available = True)
        except(KeyError):
            catslug = self.kwargs['catslug']
            categories = get_object_or_404(Category, category_slug = catslug)
            return Product.objects.all().filter(category = categories, is_available = True)
        
        
        