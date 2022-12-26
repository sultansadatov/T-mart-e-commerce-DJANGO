# from django import views
# from django.urls import path
# from . import views


# urlpatterns = [

#     # path("cart", views.cart),
#     path("customer", views.customer),
#     path("products/<int:product_id>", views.product),
#     path("shop", views.shop)
# ]


from django import views
from django.urls import path
from . import views

app_name="product"

urlpatterns = [


    path("customer", views.customer),
    path("products/<int:product_id>", views.product),
    path("shop", views.shop, name="shop")
]