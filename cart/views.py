
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from .models import CartItem, Cart
from store.models import Product
# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def add_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
    return redirect(reverse('cart:Cart'))
class CartView(ListView):
    model = CartItem
    template_name = 'store/cart.html'
    context_object_name = 'current_items'

    def get_context_data(self, **kwargs):
        total = 0
        total_num = 0
        tax = 0
        grand_total = 0
        try:
            cart = Cart.objects.get(cart_id = _cart_id(self.request))
            cart_items = CartItem.objects.filter(cart = cart, is_active = True)
            for item in cart_items:
                total += item.product.price * item.quantity
                total_num += item.quantity
            tax = (5*total)/100
            tax = round(tax, 0)
            grand_total = total + tax
        except Cart.DoesNotExist:
            pass
        kwargs.update(
            Total_price = total,
            Total_number = total_num,
            Tax = tax,
            Grand_Total = grand_total
        )
        return super().get_context_data(**kwargs)
    