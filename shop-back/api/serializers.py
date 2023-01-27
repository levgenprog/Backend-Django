from rest_framework import serializers
from .models import Category, Merch

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
    
class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = "__all__"