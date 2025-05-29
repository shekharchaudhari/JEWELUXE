from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Product,Category
from django.shortcuts import get_object_or_404
from .cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem
from django.views.decorators.http import require_POST
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth import logout
from django.contrib import messages
# Create your views here.

def home(request):
    print(list(messages.get_messages(request)))
    featured_products = Product.objects.all()[:6]  # Show 6 products
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })
def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id,
    })
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'store/cart_detail.html', {
        'cart_items': cart_items,
        'total': total
    })


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product_id=product_id, quantity=quantity)
    return redirect('cart_detail')

@require_POST
def update_cart_quantity(request, product_id):
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product_id=product_id, quantity=quantity, update_quantity=True)
    return redirect('cart_detail')

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )
            cart.clear()
            return render(request, 'store/checkout_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})


def custom_logout(request):
    messages.success(request, "You’ve been logged out.")
    logout(request)
    return redirect('home') 

def test_message(request):
    messages.success(request, "This is a test message.")
    return redirect('home')    