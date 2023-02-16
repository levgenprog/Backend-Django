from rest_framework import serializers

from .models import Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    min_amount = serializers.DecimalField(max_digits = 14, decimal_places = 2, read_only = True)

    class Meta:
        model = Product
        fields = '__all__'

class RetriveProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only = True)
    produt_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
