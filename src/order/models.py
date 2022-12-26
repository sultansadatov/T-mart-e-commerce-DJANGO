from django.db import models
from users.models import User
from product.models import Product
from datetime import date

# Create your models here.

class Payment(models.Model):
    payment_tip = models.CharField(max_length=255)
    allowed =  models.BooleanField()



# class Order(models.Model):
#     Payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
#     User_id = models.IntegerField()
#     Cart_id = models.IntegerField()
#     order_date = models.DateField()
#     shipping_id = models.IntegerField()
#     shipping_date = models.DateField()
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def _str_(self):
		return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def _str_(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping=True
        orderItems=self.orderitem_set.all()
        print("4**************")
        
        return shipping







class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total =self.product.price *self.quantity
        return total


class ShippingAddress(models.Model):
    phone = models.CharField(max_length=200, null=False)
    message = models.CharField(max_length=500, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.address