from rest_framework import serializers 
from . import models
from products import serializers as product_serializer


class SellerProdutSerializer(serializers.ModelSerializer):
    product = product_serializer.ProductSerializer()
    
    class Meta:
        model = models.SellerProduct
        fields = '__all__'