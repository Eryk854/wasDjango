from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import OrderForm,ComplaintForm
from .models import Product, Order,Complaint,OrderedProducts
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


def order_details(request,order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = order.get_total_prices()
    products = order.get_products()
    return render(request,"sklep/order_details.html",
                        {'products':products,
                         'total_price':total_price})


def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                delivery=form.cleaned_data['delivery']
            )
            order.save()
            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()

    return render(request, 'sklep/order_form.html',{'form':form})

def complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = Complaint(
                name=form.cleaned_data['name'],
                message=form.cleaned_data['message']
            )
            complaint.save()
            return HttpResponseRedirect('/complaint/'+str(complaint.id))
    else:
        form = ComplaintForm()
    return render(request,"sklep/complaint_form.html",{'form':form})

def complaint_details(request,complaint_id):
    complaint = get_object_or_404(Complaint,pk=complaint_id)
    return render(request,"sklep/complaint_details.html",
                  {'complaint':complaint})