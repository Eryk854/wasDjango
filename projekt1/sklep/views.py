from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import OrderForm,ComplaintForm
from .models import Product, Order,Complaint,OrderedProducts,Comments,Discount
# Create your views here.


def index(request):
    return render(request,"Sklep/index.html")


def product_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}
    return render(request, "sklep/list.html",
                  context)


def product_details(request,product_id):
    products = Product.objects.get(id=product_id)
    comments = Comments.objects.filter(product=products)
    context = {'product':products,
               'comments':comments}
    return render(request,"sklep/product_info.html", context)


def add_comment(request):
    if request.method == 'POST':
        id = request.POST.get('item_id')
        if len(request.POST.get('comment').strip()):
            product = Product.objects.get(id=id)
            comment = Comments(
                text=request.POST.get('comment'),
                product=product
            )
            comment.save()

        return HttpResponseRedirect('/products/'+id)


def order_details(request,order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.discount_code:
        total_price = order.total_price_with_discount()
    else:
        total_price = order.get_total_prices()
    products = order.get_products()
    return render(request,"sklep/order_details.html",
                        {'products':products,
                         'total_price':total_price})


def _price_of_cart(products):
    suma = 0
    for product,amount in products:
        suma+=product.price * int(amount)
    return round(suma,2)


def order(request):
    products_to_order = _get_products_in_cart(request)
    amounts = []
    code = request.GET.get('code')
    if code:
        if Discount.objects.filter(code=code):
            discount = Discount.objects.get(code=code).discount
            request.session['discount'] = Discount.objects.get(code=code).id
        else:
            discount = 'Nie poprawny kod!'
            if discount in request.session:
                del(request.session['discount'])
    else:
        discount = None

    request.session.modified = True
    for product in request.session['cart']:
        amounts.append(product['amount'])
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = Order(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                address=form.cleaned_data['address'],
                delivery=form.cleaned_data['delivery'],
            )
            if 'discount' in request.session:
                discount_object = Discount.objects.get(pk=request.session['discount'])
                order.discount_code = discount_object
                del(request.session['discount'])
            order.save()
            i=0
            for product in products_to_order:
                order_product = OrderedProducts(
                    product=product, order=order, amount=amounts[i]
                )
                i+=1
                order_product.save()
            request.session['cart'] = []

            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()

    products = zip(products_to_order,amounts)
    sum = _price_of_cart(products)
    products = zip(products_to_order,amounts)
    return render(request, 'sklep/order_form.html',{
        'form':form,
        "products":products,
        'discount': discount,
        'sum':sum})


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


def cart(request):
    products_in_cart = _get_products_in_cart(request)
    amounts = []
    for product in request.session['cart']:
        amounts.append(product['amount'])
    products = zip(products_in_cart,amounts)
    sum = _price_of_cart(products)
    products = zip(products_in_cart, amounts)

    return render(request,"sklep/cart.html",{"products":products,
                                             "sum":sum})


def _get_products_in_cart(request):
    products_in_cart = []
    for product in request.session.get('cart', []):
        product = Product.objects.get(pk=product['item'])
        products_in_cart.append(product)
    return products_in_cart


def add_to_cart(request):
    if request.method == "POST":
        if 'cart' not in request.session:
            request.session['cart'] = []

        item_id = request.POST['item_id']
        amount = request.POST['amount']
        flag = True
        for item in request.session['cart']:
            if item['item'] == item_id:
                flag = False
        if flag:
            product = {'item':item_id,'amount':amount}
            request.session['cart'].append(product)
            request.session.modified = True
        else:
            for item in request.session['cart']:
                if item['item'] == item_id:
                    print(amount)
                    item['amount'] = int(item['amount']) + int(amount)
                    request.session.modified = True

    return HttpResponseRedirect("/cart")


def delete_item(request,product_id):
    request.session['cart'] = [d for d in request.session['cart'] if d.get('item') != product_id]
    request.session.modified = True
    return HttpResponseRedirect("/cart")


def vote(request):
    if request.method =="POST" and request.POST.get('vote'):
        product = Product.objects.get(pk=request.POST.get('item_id'))
        product.sum = product.sum + int(request.POST.get('vote'))
        product.votes += 1
        product.save()
        product.rating = round(product.sum/product.votes, 2)
        product.save()

    return HttpResponseRedirect('/products/'+str(request.POST.get('item_id')))
