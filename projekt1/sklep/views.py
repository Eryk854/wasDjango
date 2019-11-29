from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    return render(request,"Sklep/index.html")

def index1(request,tekst):
    return render(request , "sklep/glowna.html",
                  {"imie_klienta":tekst})

def product_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "sklep/list.html",
                  context)

def product_info(request,nr_produktu):
    return render(request,"sklep/product_info.html",
                {"product":products[nr_produktu-1]})

def product_details(request,product_id):
    products = Product.objects.get(id=product_id)
    context = {'product':products}
    return render(request,"sklep/product_info.html",
                context)
