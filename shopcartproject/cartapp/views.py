from django.shortcuts import render, redirect, get_object_or_404
from shopcartapp.models import Product
from .models import  Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
#** add cart items to the table Cart,CartItem
def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart_id=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart_id=Cart.objects.create(cart_id=_cart_id(request))
        cart_id.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart_id)
        if cart_item.quantity < cart_item.product.prod_stock:
            cart_item.quantity +=1
            cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=product,quantity=1,cart=cart_id)
        cart_item.save()
    return redirect('cartapp:cart_detail')

# Get details of cart from Cart and CartItem table
def cart_detail(request,total=0,counter=0,cart_items=None):
        try:
            cart_id=Cart.objects.get(cart_id=_cart_id(request))
            cart_items=CartItem.objects.filter(cart=cart_id,active=True)
            for cart_item in cart_items:
                total +=(cart_item.product.prod_price * cart_item.quantity)
                counter +=cart_item.quantity
        except ObjectDoesNotExist:
            pass
        return render(request,"cart.html",dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart_id=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart_id)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cartapp:cart_detail')

def full_remove(request,product_id):
    cart_id=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_items=CartItem.objects.get(product=product,cart=cart_id)
    cart_items.delete()
    return redirect('cartapp:cart_detail')