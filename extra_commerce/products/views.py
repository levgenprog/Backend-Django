from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from . import models, serializers

class ProductViewSet(ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()



class ProductImageViewSet(ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()