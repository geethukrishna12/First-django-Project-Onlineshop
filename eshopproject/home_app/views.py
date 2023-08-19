from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from cart_app.models import *

# Create your views here.

def home(request):
    cat = Category.objects.all()
    prolist = Product.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)

    context = {
        'cat': cat,
        'prolist': prolist,
        'total_items':total_items
    }
    return render(request, 'index.html', context)

def productlist(request):
    prolist = Product.objects.all()
    cat=Category.objects.all()
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    context = {
        'prolist': prolist,
        'cat':cat,
        'total_items':total_items
    }
    return render(request, 'product-list.html', context)


def productdetail(request, id):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    cat=Category.objects.all()
    prodetail =Product.objects.get(id=id)
    return render(request, 'product-detail.html', {'prodetail': prodetail,'cat':cat,'total_items':total_items})

def contact(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'contact.html',{'total_items':total_items})


def myaccount(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'my-account.html',{'total_items':total_items})


def product_by_cat(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    cat=Category.objects.all()
    category=request.GET.get('category')
    if category==None:
        products=Product.objects.all()
    else:
        products=Product.objects.filter(category__name=category)
    context={'cat':cat,'products':products,'total_items':total_items}
    return render(request,'cat-product-list.html',context)


# **************************  Search **********************************

def search(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)

    if request.method=='GET':
        query=request.GET.get('query')
        if query:
            products=Product.objects.order_by('-price').filter(name__icontains=query)
            return render(request,'search.html',{'products':products})
        else:
            print("No information to show")
            return request(request,'search.html',{'total_items':total_items})

def showall_product(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_items = sum(item.quantity for item in cart_items)
    cat=Category.objects.all()
    products=Product.objects.order_by('-pk').all()

    page_num = request.GET.get("page",1)
    paginator=Paginator(products,3)
    # print(page_num)
    # # represents each item
    # print(paginator.count)
    # # represents pages after divid
    # print(paginator.num_pages)
    # print(paginator.page_range	)
    # print(paginator.page(2))


    try:
        products=paginator.page(page_num)
    except PageNotAnInteger:
        products==paginator.page(1)
    except EmptyPage:
        products=paginator.page(Paginator.num_pages)

    context={'products':products,'cat':cat,'total_items':total_items}
    return render(request,'product-list.html',context)




#
# def login(request):
#     return render(request, 'login.html')

#
# def register(request):
#     return render(request, 'register.html')


# def cart(request):
#     return render(request, 'cart.html')
# def wishlist(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_items = sum(item.quantity for item in cart_items)
#     return render(request, 'wishlist.html',{'total_items':total_items})