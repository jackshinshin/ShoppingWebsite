from ast import Try
from .models import Cart, CartItem
from .views import _cart_id
def counter(request):
    cart_counter = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_items = CartItem.objects.all().filter(cart = cart)
            for item in cart_items:
                cart_counter += 1
        except (Cart.DoesNotExist):
            pass
    return dict(
        cart_counter = cart_counter
    )