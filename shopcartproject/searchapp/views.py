from django.shortcuts import render
from shopcartapp.models import Product
from django.db.models import Q
# Create your views here.
def searchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        search_condition= Q(prod_name__icontains=query) | Q(prod_description__icontains=query)
        products = Product.objects.all().filter(search_condition)
        return render(request,"search.html",{'query':query, 'products':products})
