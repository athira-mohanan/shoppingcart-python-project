from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Product,Category
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allProdCat(request,c_slug=None):
    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,cat_slug=c_slug)
        products=Product.objects.all().filter(category=c_page,prod_available=True)
    else:
        products=Product.objects.all().filter(prod_available=True)
    paginator=Paginator(products,6)
    try:
        current_page=int(request.GET.get('page','1'))
    except:
        current_page=1
    try:
        prod_per_page=paginator.page(current_page)
    except (EmptyPage,InvalidPage):
        prod_per_page=paginator.current_page(paginator.num_pages)

    return render(request,"category.html",{'category': c_page, 'products': prod_per_page})

def proDetails(request,c_slug,product_slug):
    try:
        product=Product.objects.get(category__cat_slug=c_slug,prod_slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"product.html",{'product':product})
