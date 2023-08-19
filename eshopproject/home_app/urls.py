from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('productlist', views.productlist, name='productlist'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('contact', views.contact, name='contact'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('product_by_cat',views.product_by_cat,name='product_by_cat'),
    path('search',views.search,name='search'),
    path('showall_product',views.showall_product,name='showall_product'),

    # path('wishlist', views.wishlist, name='wishlist'),
    # path('cart', views.cart, name='cart'),
    # path('checkout/',views.checkout,name='checkout'),
    # path('login', views.login, name='login'),
    # path('logout', views.login, name='logout'),
    # path('register', views.register, name='register'),



]
