from rest_framework.generics import (
    # RetrieveUpdateDestroyAPIView,

    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)



from api.serializers import ProductSerializers, CategorySerializer

from product.models import Product, Category

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'pk'


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # lookup_field = 'pk'