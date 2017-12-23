from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product


def cart_home(request):
    cart_obj, new_obj = Cart.objects.get_or_new(request)
    return render(request, 'carts/home.html', {})


def cart_update(request):
    product_id = 1
    product_obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.get_or_new(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    return redirect('cart:home')
