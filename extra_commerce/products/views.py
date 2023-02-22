from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from utils import mixins

from . import serializers, permissions, services


class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    product_image_services: services.ProductImageServicesInterface = services.ProductImageServicesV1()
    serializer_class = serializers.ProductImageSerializer
    queryset = product_image_services.get_product_images()
    permission_class = permissions.IsAdminOrReadOnly,
    


class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrive': serializers.RetriveProductSerializer,
    }
    product_services: services.ProductServicesInterface = services.ProductServicesV1()
    permission_classes = permissions.IsAdminOrReadOnly,
    serializer_class = serializers.ProductSerializer
    queryset = product_services.get_products()

