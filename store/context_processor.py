from .models import Product
def product_menu_links(request):
    links = Product.objects.all()
    return dict(prod_links = links)