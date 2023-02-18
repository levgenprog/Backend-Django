from rest_framework import serializers 
from . import models
from products import serializers as product_serializer

class CreateSellerProductSerializer(serializers.ModelSerializer):
    seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.SellerProduct
        fields = (
            'seller',
            'product',
            'amount',
            'amount_currency',
            'is_active',
        )

class UpdateSellerProductSerializer(serializers.ModelSerializer):
    # seller = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = models.SellerProduct
        fields = (
            'amount',
            'amount_currency',
            'is_active',
        )

class SellerProductSerializer(serializers.ModelSerializer):
    product = product_serializer.ProductSerializer()
    
    class Meta:
        model = models.SellerProduct
        fields = '__all__'