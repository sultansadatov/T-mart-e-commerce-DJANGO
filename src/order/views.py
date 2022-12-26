from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from product.models import *

import json
import datetime


def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems=order['get_cart_items']



    context = {'items':items,'order': order,'cartItems':cartItems}
    return render(request, 'order/cart.html', context)

def checkout(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

        
    else:
        items=[]
        order={'get_cart_items':0,'get_cart_total':0,'shipping':False}
        cartItems=order['get_cart_items']
    products=Product.objects.all()

    context = {'items':items,'order':order,'cartItems':cartItems,'products': products}
        
    return render(request, 'order/checkout.html', context)


def updateItem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('productId', productId)
    print('action', action)

    customer=request.user.customer
    print(customer)
    product=Product.objects.get(id=productId)
    print(product)

    order, created=Order.objects.get_or_create(customer=customer,complete=False)
    print(order)

    orderItem, created=OrderItem.objects.get_or_create(order=order,product=product)
    print(orderItem)

    if action=='add':
        orderItem.quantity=(orderItem.quantity +1)
    elif action =='remove':
        orderItem.quantity=(orderItem.quantity -1)

    orderItem.save()
    print(orderItem)

    if orderItem.quantity <= 0:
        orderItem.delete()



    return JsonResponse('Item was added',safe=False)


def processOrder(request): 
    transaction_id=datetime.datetime.now().timestamp()
    print("5")
    data=json.loads(request.body)

    customer=request.user.customer
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    total=data['form']['total']
    order.transaction_id=transaction_id
    if total ==order.get_cart_total:
        order.complete=True
    order.save()


    ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        phone=data['shipping']['phone'],
        message=data['shipping']['message'],
        country=data['shipping']['country'],
    )

    return JsonResponse('Payment submitted...',safe=False)
