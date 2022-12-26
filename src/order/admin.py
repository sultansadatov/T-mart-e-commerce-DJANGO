from datetime import date
from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Payment)
admin.site.register(Order)
# admin.site.register(Shipping)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Customer)