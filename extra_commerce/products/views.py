from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Min, Q

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from utils import mixins

from . import models, serializers, permissions


class ProductImageViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()
    

class ProductViewSet(mixins.ActionSerializerMixin, ModelViewSet):
    ACTION_SERIALIZERS = {
        'retrive': serializers.RetriveProductSerializer,
    }
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.annotate(min_amount=Min('seller_products__amount'), filter=Q(seller_products__is_active=True))

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return IsAuthenticated(),

        return permissions.IsMe(),
    
    def list(self, request, *args, **kwargs):
        print(type(request.user))
        
        return super().list(request, *args, **kwargs)