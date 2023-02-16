from rest_framework.viewsets import ModelViewSet

from . import serializers, models


class SellerProdutViewSet(ModelViewSet):
    serializer_data = serializers.SellerProdutSerializer
    queryset = models.SellerProduct.objects.select_related('seller', 'product')