from .cart import Cart

def cart_item_count(request):
    cart = Cart(request)
    total_items = sum(quantity for _, quantity in cart.items())
    return {'cart_item_count': total_items}
