from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from product.tasks import send_new_product_notifications
from .services.products import list_products, get_product, list_brands, get_brand

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
import json
import datetime
from product.models import Brand

from django.http import JsonResponse

from order.models import *
import json



# Create your views here.

def cart(request):
    return render(request, "product/cart.html")

def customer(request):
    return render(request, "product/customer-review.html")

def product(request, product_id):
    products = get_product(product_id)

    context = {
        'products': products
    }
    return render(request, "product/product-details.html", context=context)



def shop(request):

    if request.user.is_authenticated and request.user.is_superuser is False:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    
    brands = Brand.objects.all()
    if "brand" in request.GET.keys():
        print(request.GET["brand"])
        products = Product.objects.filter(
            brand_id_id__name=request.GET["brand"])
    
    
    sizes = Size.objects.all()
    if "size" in request.GET.keys():
        print(request.GET["size"])
        products = Product.objects.filter(
            size_id_id__name=request.GET["size"])



    colors = Color.objects.all()
    if "color" in request.GET.keys():
        print(request.GET["color"])
        products = Product.objects.filter(
            color_id_id__name=request.GET["color"])


    categorys = Category.objects.all()
    if "color" in request.GET.keys():
        print(request.GET["color"])
        products = Product.objects.filter(
            color_id_id__name=request.GET["color"])


    if "min_price" in request.GET.keys():
        print(request.GET["min_price"])
        products = Product.objects.filter(
            price__gte=request.GET["min_price"], price__lte=request.GET["max_price"])

    context = {'items': items, 'products': products,
               'cartItems': cartItems, 'order': order, 'brands': brands, 'sizes': sizes, 'colors':colors, 'categorys':categorys }

    return render(request, 'product/shop.html', context)

class BrandPageView(ListView):
    model = Product, Size, Color
    template_name = 'product/shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['sizes'] = Size.objects.all()
        context['color'] = Color.objects.all()
        return context
    def get_queryset(self):
        print(self.request.GET.get('min_value'), )
        brand = self.request.GET.get('brand')
        if brand:
            self.queryset = Product.objects.filter(brand_id_id__name=brand)
        else:
            self.queryset = Product.objects.all()
        return self.queryset
    def get_queryset(self):
        size = self.request.GET.get('size')
        if size:
            self.queryset = Product.objects.filter(size_id_id__name=size)
        else:
            self.queryset = Product.objects.all()

        return self.queryset
    def get_queryset(self):
        color = self.request.GET.get('color')
        if color:
            self.queryset = Product.objects.filter(color_id_id__name=color)
        else:
            self.queryset = Product.objects.all()

        return self.queryset


    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            self.queryset = Product.objects.filter(color_id_id__name=category)
        else:
            self.queryset = Product.objects.all()

        return self.queryset


    def get_queryset(self):
        min_price = self.request.GET.get('min_value')
        max_price = self.request.GET.get('min_value')

        print(min_price, max_price)


        if min_price and max_price:
            
            self.queryset = Product.objects.filter(price__gte=min_price, price__lte=max_price)
        else:
            print('ADFGDFGDGDGDGDsd')
            self.queryset = Product.objects.all()

        return self.queryset
    