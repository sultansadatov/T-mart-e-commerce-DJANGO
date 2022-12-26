from rest_framework import serializers


from product.models import Product, Category




class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"