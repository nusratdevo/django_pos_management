from datetime import datetime
import json
import sys
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from main.forms import product_form
from main.models.product import Order, OrderItems, Product


@login_required(login_url='/login/')
def pos_create(request):
    products = Product.objects.filter(is_active = True)
    product_json = []
    for product in products:
        product_json.append({'id':product.id, 'name':product.title, 'price':float(product.price)})
    context = {
        'products' : products,
        'product_json' : json.dumps(product_json)
    }
    # return HttpResponse('')
    return render(request, "pos/pos.html", context)


@login_required(login_url='/login/')
def checkout_modal(request):
    grand_total = 0
    if 'grand_total' in request.GET:
        grand_total = request.GET['grand_total']
    context = {
        'grand_total' : grand_total,
    }
    return render(request, 'pos/checkout.html',context)




def save_pos(request):
    resp = {'status':'failed','msg':''}
    data = request.POST
    pref = datetime.now().year + datetime.now().year
    # i = 1
    # while True:
    #     code = '{:0>5}'.format(i)
    #     i += int(1)
    #     check = Order.objects.filter(code = str(pref) + str(code)).all()
    #     if len(check) <= 0:
    #         break
    # code = str(pref) + str(code)

    try:
        orders = Order(code='', sub_total = data['sub_total'], tax = data['tax'], tax_amount = data['tax_amount'], grand_total = data['grand_total'], tendered_amount = data['tendered_amount'], amount_change = data['amount_change']).save()
        order_id = Order.objects.last().pk
        i = 0
        for prod in data.getlist('product_id[]'):
            product_id = prod 
            order = Order.objects.filter(id=order_id).first()
            product = Product.objects.filter(id=product_id).first()
            qty = data.getlist('qty[]')[i] 
            price = data.getlist('price[]')[i] 
            total = float(qty) * float(price)
            print({'order_id' : order, 'product_id' : product, 'qty' : qty, 'price' : price, 'total' : total})
            OrderItems(order_id = order, product_id = product, qty = qty, price = price, total = total).save()
            i += int(1)
        resp['status'] = 'success'
        resp['order_id'] = order_id
        messages.success(request, "Sale Record has been saved.")
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return HttpResponse(json.dumps(resp),content_type="application/json")




@login_required(login_url='/login/')
def receipt(request):
    id = request.GET.get('id')
    orders = Order.objects.filter(id = id).first()
    transaction = {}
    for field in Order._meta.get_fields():
        if field.related_model is None:
            transaction[field.name] = getattr(orders,field.name)
    if 'tax_amount' in transaction:
        transaction['tax_amount'] = format(float(transaction['tax_amount']))
    ItemList = OrderItems.objects.filter(order_id = orders).all()
    context = {
        "transaction" : transaction,
        "salesItems" : ItemList
    }

    return render(request, 'pos/receipt.html',context)



def order_list(request):
    
    # customer=Customer.objects.get(user_id=request.user.id)
   
    selector = request.GET.get('selector')
    orders=Order.objects.all()

    if selector:
        if selector == "hightolow":
                orders=orders.order_by('-grand_total')
        elif selector == "lowtohigh":
                orders=orders.order_by('grand_total')
        elif selector == "dsc":
                orders=orders.order_by('-id')
    ordered_products=[]
    for order in orders:
            ordered_product=OrderItems.objects.all().filter(order_id=order.id)
            ordered_products.append(ordered_product)
    context = {
        "orders":orders,
        "data" : ordered_products
        }

    return render(request,'pos/order_list.html',context)
 
 # Activate order Status
def order_status(request, id):
      if request.method=="POST":
           status = request.POST.get('status')
        #    order_status=request.GET.get('status')
           new_tatus= Order.objects.filter(id=id).update(status=status)
           return redirect("/order/")

      return render(request,'pos/status_change.html')


def order_traking(request, id):
    
    orders=Order.objects.all().filter(id = id)
    ordered_products=[]
    for order in orders:
        ordered_product=OrderItems.objects.all().filter(order_id=order.id)
        ordered_products.append(ordered_product)

    return render(request,'pos/order_traking.html',{'data':zip(ordered_products,orders)})
 

def delete_order(request, id):
    resp = {'status':'failed', 'msg':''}
    try:
        order = Order.objects.filter(id = id).delete()
        item = OrderItems.objects.filter(order_id = id).delete()
        resp['status'] = 'success'
        messages.success(request, 'Order Record has been deleted.')
    except:
        resp['msg'] = "An error occured"
        print("Unexpected error:", sys.exc_info()[0])
    return redirect("/order/")


def order_invoice(request):
    return render(request,'pos/invoice.html')
