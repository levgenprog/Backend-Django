from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from utils import mixins

from . import models, serializers


class ProductViewSet(ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()



class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrive': serializers.RetriveProductSerializer,
    }
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()
