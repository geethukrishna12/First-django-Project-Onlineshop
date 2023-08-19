from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
def cartdetail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    # print(total_items)
    return render(request, 'cart.html', {'cart_items': cart_items,'total_price':total_price, 'total_items':total_items})

# @login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        if request.method == 'POST':
            quantity = int(request.POST.get('quantity', 0))
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.quantity += 1
                cart_item.save()
    return redirect('cartdetail')


def update_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cartdetail')

def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect('cartdetail')


def wishlist(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items,'total_items':total_items})



def add_to_wishlist(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')

def remove_from_wishlist(request, pk):
    wishlist_item = get_object_or_404(Wishlist, pk=pk)
    wishlist_item.delete()
    return redirect('wishlist')

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    # print(total_items)
    return render(request,'checkout.html',{'total_items':total_items,'total_price':total_price,'cart_items':cart_items})