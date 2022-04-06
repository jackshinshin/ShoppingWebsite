from unicodedata import category
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from store.models import Product
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
class StoreView(ListView):
    model = Product
    # queryset = Product.objects.all()
    context_object_name = 'product_list'
    template_name = 'store/store.html'
    max_per_page = 3
    def get_queryset(self):
        # kwargs can be used to access url variables
        try:
            catslug = self.kwargs['catslug']
            categories = get_object_or_404(Category, category_slug = catslug)
            return Product.objects.all().filter(category = categories, is_available = True)
        except (KeyError):
            return Product.objects.all().filter(is_available = True)

    def item_each_page(self):
        products = self.get_queryset()
        paginator = Paginator(products, self.max_per_page)
        page = self.request.GET.get('page')
        return paginator.get_page(page)
    def get_context_data(self, **kwargs):
        paged_products = self.item_each_page()
        kwargs.update(
            products = paged_products
        )
        
        return super().get_context_data(**kwargs)

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
    def get_context_data(self, **kwargs):
        every_product = Product.objects.get(category__category_slug = self.kwargs['catslug'], product_slug = self.kwargs['prodslug'])
        in_cart = CartItem.objects.filter(product = every_product, cart__cart_id = _cart_id(self.request)).exists()
        kwargs.update(
            item_already_added = in_cart
        )
        return super().get_context_data(**kwargs)
        
        
        