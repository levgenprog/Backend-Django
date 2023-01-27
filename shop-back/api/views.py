from django.shortcuts import render, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Merch
from .serializers import CategorySerializer, MerchSerializer

@api_view(['GET'])
def getCat(request):
    items = Category.objects.all()
    serializer = CategorySerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def catRetrieve(request, pk=None):
    items = get_list_or_404(Category.objects.all(), pk=pk)
    serializer = CategorySerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getMerch(request):
    items = Merch.objects.all()
    serializer = MerchSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prodRetrieve(request, pk=None):
    items = get_list_or_404(Merch.objects.all(), pk=pk)
    serializer = MerchSerializer(items, many=True)
    return Response(serializer.data)    


@api_view(['POST'])
def addData(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)